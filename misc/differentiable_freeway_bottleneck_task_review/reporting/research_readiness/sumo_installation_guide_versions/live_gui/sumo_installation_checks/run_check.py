#!/usr/bin/env python3
"""Check SUMO startup, state queries, a speed command, completion and optional PNG.

APIs: https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html
      https://sumo.dlr.de/pydoc/traci/_gui.html
Runtime checks are intentionally separate from VSL scientific validation.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import importlib
from importlib.metadata import version
import json
import math
import os
from pathlib import Path
import platform
import shutil
import sys
import time
from uuid import uuid4
import xml.etree.ElementTree as ET

VERSION = '1.28.0'
PACKAGES = ('eclipse-sumo', 'libsumo', 'traci', 'sumolib')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--case', choices=('straight', 'lane_drop'), required=True)
    parser.add_argument('--backend', choices=('libsumo', 'traci'), required=True)
    parser.add_argument('--gui', action='store_true', help='TraCI only; needs a working display.')
    parser.add_argument('--frame-delay', type=float, default=0.2, help='Wall-clock seconds per GUI step.')
    parser.add_argument('--max-steps', type=int, default=240)
    args = parser.parse_args()
    if args.gui and args.backend != 'traci':
        parser.error('Use --backend traci for GUI checks; libsumo GUI is not assumed.')
    if args.max_steps <= 0 or not math.isfinite(args.frame_delay) or args.frame_delay < 0:
        parser.error('Use positive --max-steps and finite nonnegative --frame-delay.')
    if args.gui and sys.platform.startswith('linux') and not os.environ.get('DISPLAY'):
        parser.error('DISPLAY is unset; reconnect from an X11-enabled Windows SSH session.')
    if any(os.environ.get(key) for key in ('LIBSUMO_AS_TRACI', 'LIBSUMO_GUI')):
        parser.error('Unset LIBSUMO_AS_TRACI and LIBSUMO_GUI in this test shell.')
    root = args.workspace.expanduser().resolve()
    folder = root / args.case
    config = folder / 'test.sumocfg'
    if not config.is_file() or not (root / 'cases.json').is_file():
        parser.error('Prepare the workspace with prepare_cases.py first.')
    definition = json.loads((root / 'cases.json').read_text())['cases'][args.case]
    for name, digest in definition['files_sha256'].items():
        if hashlib.sha256((folder / name).read_bytes()).hexdigest() != digest:
            parser.error(f'Example file changed: {name}; prepare a new workspace.')
    expected = {node.attrib['id'] for node in ET.parse(folder / 'routes.rou.xml').findall('vehicle')}
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid4().hex[:8]
    output = root / 'results' / f'{args.case}-{args.backend}{"-gui" if args.gui else ""}-{run_id}'
    output.mkdir(parents=True, exist_ok=False)
    result = {'status': 'failed', 'case': args.case, 'backend': args.backend, 'gui': args.gui,
              'created_utc': datetime.now(timezone.utc).isoformat(), 'seed': 42,
              'python': sys.executable, 'python_version': platform.python_version(),
              'output_directory': str(output), 'manual_gui_check': 'pending' if args.gui else 'not applicable'}
    rows, departed, arrived, teleports = [], set(), set(), []
    api, started, error = None, False, None
    baseline_observed = low_set = high_set = low_observed = high_observed = screenshot_requested = False
    screenshot = output / 'view.png'
    steps = 0
    try:
        result['package_versions'] = {name: version(name) for name in PACKAGES}
        if any(value != VERSION for value in result['package_versions'].values()):
            raise RuntimeError(f'Expected all four packages at {VERSION}: {result["package_versions"]}')
        binary = shutil.which('sumo-gui' if args.gui else 'sumo')
        if not binary:
            raise RuntimeError('SUMO executable not found on PATH; activate the SUMO environment.')
        api = importlib.import_module(args.backend)
        result['api_module'] = api.__file__
        command = [binary, '-c', str(config), '--seed', '42', '--no-step-log', 'true',
                   '--tripinfo-output', str(output / 'tripinfo.xml'), '--log', str(output / 'sumo.log')]
        if args.gui:
            command += ['--start']
        result['command'] = command
        api.start(command)
        started = True
        result['sumo_api_version'] = list(api.getVersion())
        if VERSION not in str(result['sumo_api_version'][1]):
            raise RuntimeError(f'Unexpected SUMO binary/library version: {result["sumo_api_version"]}')
        actual_lanes = [api.edge.getLaneNumber(edge) for edge in ('up', 'down')]
        if actual_lanes != definition['lane_counts']:
            raise RuntimeError(f'Unexpected lane counts: {actual_lanes}')
        if args.gui:
            (xmin, ymin), (xmax, ymax) = api.simulation.getNetBoundary()
            api.gui.setBoundary('View #0', xmin - 10, ymin - 30, xmax + 10, ymax + 30)
        while api.simulation.getMinExpectedNumber() > 0 and steps < args.max_steps:
            api.simulationStep()
            steps += 1
            now = api.simulation.getTime()
            departed.update(api.simulation.getDepartedIDList())
            arrived.update(api.simulation.getArrivedIDList())
            teleports.extend(api.simulation.getStartingTeleportIDList())
            active = api.vehicle.getIDList()
            speed = limit = road = ''
            if 'v0' in active:
                if now >= 5 and not low_set:
                    api.vehicle.setMaxSpeed('v0', 5.0)
                    if not math.isclose(api.vehicle.getMaxSpeed('v0'), 5.0, abs_tol=1e-9):
                        raise RuntimeError('Speed-cap command did not read back as 5 m/s.')
                    low_set = True
                if now >= 15 and not high_set:
                    api.vehicle.setMaxSpeed('v0', 13.9)
                    if not math.isclose(api.vehicle.getMaxSpeed('v0'), 13.9, abs_tol=1e-9):
                        raise RuntimeError('Restored speed cap did not read back as 13.9 m/s.')
                    high_set = True
                speed = api.vehicle.getSpeed('v0')
                limit = api.vehicle.getMaxSpeed('v0')
                road = api.vehicle.getRoadID('v0')
                baseline_observed |= 3 <= now < 5 and speed > 5.5
                low_observed |= 9 <= now < 15 and speed <= 5.05
                high_observed |= now >= 20 and high_set and speed > 5.5
            rows.append([now, len(active), len(departed), len(arrived), speed, limit, road])
            if args.gui and now >= 40 and not screenshot_requested:
                api.gui.screenshot('View #0', str(screenshot), 1280, 720)
                screenshot_requested = True
                # SUMO writes the requested image on the following simulationStep.
            if args.gui and args.frame_delay:
                time.sleep(args.frame_delay)
        remaining = api.simulation.getMinExpectedNumber()
        if remaining or departed != expected or arrived != expected:
            raise RuntimeError(f'Incomplete example: departed={len(departed)}, arrived={len(arrived)}, remaining={remaining}.')
        if teleports:
            raise RuntimeError(f'Unexpected teleportation in dummy example: {teleports}')
        if not all((baseline_observed, low_set, high_set, low_observed, high_observed)):
            raise RuntimeError('Speed command/readback or actual slowing/recovery check did not complete.')
        api.close()
        started = False
        trips = ET.parse(output / 'tripinfo.xml').findall('tripinfo')
        if {item.attrib['id'] for item in trips} != expected or len(trips) != len(expected):
            raise RuntimeError('Trip output does not contain exactly the 12 expected completed vehicles.')
        if any(float(item.attrib.get('arrival', '-1')) < 0 or
               item.attrib.get('vaporized', '').lower() not in ('', '0', 'false') for item in trips):
            raise RuntimeError('Trip output contains an unfinished or removed vehicle.')
        if args.gui and (not screenshot_requested or not screenshot.is_file() or screenshot.read_bytes()[:8] != b'\x89PNG\r\n\x1a\n'):
            raise RuntimeError('GUI did not produce the expected PNG; inspect the SUMO log.')
        result['status'] = 'passed'
    except BaseException as exc:
        error = exc
        result['error'] = f'{type(exc).__name__}: {exc}'
    finally:
        if started:
            try:
                api.close()
            except Exception as exc:
                result['close_error'] = f'{type(exc).__name__}: {exc}'
        result.update(steps=steps, departed=len(departed), arrived=len(arrived),
                      initial_motion_observed=baseline_observed,
                      teleports=teleports, low_cap_readback=low_set, restored_cap_readback=high_set,
                      actual_slowing_observed=low_observed, actual_acceleration_observed=high_observed)
        with (output / 'trace.csv').open('w', newline='') as stream:
            writer = csv.writer(stream)
            writer.writerow(['time_s', 'active', 'departed', 'arrived', 'v0_speed_mps', 'v0_limit_mps', 'v0_road'])
            writer.writerows(rows)
        (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    if error:
        print(f'FAIL: {result["error"]}\nDetails: {output}', file=sys.stderr)
        return 130 if isinstance(error, KeyboardInterrupt) else 1
    print(f'PASS: {args.case}, {args.backend}, gui={args.gui}; all 12 vehicles finished.')
    print(f'Outputs: {output}')
    if args.gui:
        print('Inspect view.png and the visible Windows window; visual correctness still needs your confirmation.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
