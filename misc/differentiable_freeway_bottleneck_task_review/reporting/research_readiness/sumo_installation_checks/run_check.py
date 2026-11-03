#!/usr/bin/env python3
"""Check SUMO control/completion and optionally render PNGs and an offline MP4.

APIs: https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html
      https://sumo.dlr.de/pydoc/traci/_gui.html
Runtime checks are intentionally separate from VSL scientific validation.
"""
from __future__ import annotations

import argparse
import csv
import faulthandler
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
import struct
import subprocess
import sys
import time
from uuid import uuid4
import xml.etree.ElementTree as ET

VERSION = '1.28.0'
PACKAGES = ('eclipse-sumo', 'libsumo', 'traci', 'sumolib')


def encode_movie(output: Path, frames: list[Path], fps: float) -> dict:
    """Encode native frames; verify dimensions, the encoded stream and full decode."""
    for image in frames:
        header = image.read_bytes()[:24]
        if len(header) < 24 or header[:8] != b'\x89PNG\r\n\x1a\n' or struct.unpack('>II', header[16:24]) != (1280, 720):
            raise RuntimeError(f'Missing/invalid 1280x720 frame: {image}')
    movie = output / 'scenario.mp4'
    ffmpeg, ffprobe = shutil.which('ffmpeg'), shutil.which('ffprobe')
    command = [ffmpeg, '-hide_banner', '-nostdin', '-n', '-framerate', str(fps),
               '-start_number', '0', '-i', str(output / 'frames' / 'frame_%06d.png'),
               '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '20',
               '-pix_fmt', 'yuv420p', '-r', '25', '-movflags', '+faststart', str(movie)]
    (output / 'video_command.json').write_text(json.dumps(command, indent=2) + '\n')
    converted = subprocess.run(command, capture_output=True, text=True, timeout=180)
    (output / 'ffmpeg.log').write_text(converted.stdout + converted.stderr)
    if converted.returncode:
        raise RuntimeError('Video encoding failed; inspect ffmpeg.log. PNG frames are retained.')
    probe_command = [ffprobe, '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                     '-show_entries', 'stream=codec_name,width,height,pix_fmt,nb_read_frames,avg_frame_rate:format=duration',
                     '-of', 'json', str(movie)]
    probe = subprocess.run(probe_command, check=True, capture_output=True, text=True, timeout=60)
    metadata = json.loads(probe.stdout)
    (output / 'ffprobe.json').write_text(json.dumps(metadata, indent=2) + '\n')
    stream = metadata['streams'][0]
    duration = float(metadata['format']['duration'])
    expected_duration = len(frames) / fps
    if (stream.get('codec_name') != 'h264' or stream.get('pix_fmt') != 'yuv420p'
            or (stream.get('width'), stream.get('height')) != (1280, 720)
            or int(stream.get('nb_read_frames', 0)) <= 0
            or not math.isfinite(duration) or duration <= 0
            or abs(duration - expected_duration) > 1 / fps + 0.1):
        raise RuntimeError('Encoded stream properties/duration do not match the image sequence; inspect ffprobe.json.')
    decoded = subprocess.run([ffmpeg, '-hide_banner', '-nostdin', '-v', 'error', '-xerror',
                              '-i', str(movie), '-map', '0:v:0', '-f', 'null', '-'],
                             capture_output=True, text=True, timeout=120)
    (output / 'decode.log').write_text(decoded.stdout + decoded.stderr)
    if decoded.returncode:
        raise RuntimeError('Full MP4 decode failed; inspect decode.log.')
    return {'file': str(movie), 'input_frames': len(frames), 'input_fps': fps,
            'output_fps': 25, 'duration_s': duration, 'expected_duration_s': expected_duration,
            'codec': stream['codec_name'], 'pixel_format': stream['pix_fmt'], 'full_decode_passed': True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--case', choices=('straight', 'lane_drop'), required=True)
    parser.add_argument('--backend', choices=('libsumo', 'traci'), required=True)
    parser.add_argument('--gui', action='store_true', help='TraCI only; needs a working display.')
    parser.add_argument('--video', action='store_true', help='TraCI only; save native frames and MP4. Run under xvfb-run on a server.')
    parser.add_argument('--video-fps', type=float, default=5, help='PNG sequence playback rate, 0 < fps <= 25; default 5 (nominal 5x at 1 s steps).')
    parser.add_argument('--frame-delay', type=float, default=0.2, help='Wall-clock seconds per live GUI step; ignored for --video.')
    parser.add_argument('--max-steps', type=int, default=240)
    args = parser.parse_args()
    args.gui = args.gui or args.video
    if args.gui and args.backend != 'traci':
        parser.error('Use --backend traci for GUI checks; libsumo GUI is not assumed.')
    if args.max_steps <= 0 or not math.isfinite(args.frame_delay) or args.frame_delay < 0:
        parser.error('Use positive --max-steps and finite nonnegative --frame-delay.')
    if not math.isfinite(args.video_fps) or not 0 < args.video_fps <= 25:
        parser.error('Use a finite --video-fps in (0, 25].')
    if args.gui and sys.platform.startswith('linux') and not os.environ.get('DISPLAY'):
        parser.error('DISPLAY is unset; use xvfb-run for offline video, or an X11-enabled SSH session for live GUI.')
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
    mode = '-video' if args.video else '-gui' if args.gui else ''
    output = root / 'results' / f'{args.case}-{args.backend}{mode}-{run_id}'
    output.mkdir(parents=True, exist_ok=False)
    result = {'status': 'failed', 'case': args.case, 'backend': args.backend, 'gui': args.gui,
              'created_utc': datetime.now(timezone.utc).isoformat(), 'seed': 42,
              'python': sys.executable, 'python_version': platform.python_version(),
              'output_directory': str(output), 'video_requested': args.video,
              'manual_gui_check': 'pending' if args.gui and not args.video else 'not applicable',
              'manual_video_check': 'pending_on_windows' if args.video else 'not applicable'}
    rows, departed, arrived, teleports = [], set(), set(), []
    api, started, error = None, False, None
    baseline_observed = low_set = high_set = low_observed = high_observed = screenshot_requested = False
    screenshot = output / 'view.png'
    captures, pending_capture = [], None
    if args.video:
        (output / 'frames').mkdir()
    steps = 0

    def progress(stage: str, **details) -> None:
        result['stage'] = stage
        record = {'stage': stage, 'utc': datetime.now(timezone.utc).isoformat(), 'steps': steps, **details}
        temporary = output / 'progress.json.tmp'
        temporary.write_text(json.dumps(record, indent=2) + '\n')
        temporary.replace(output / 'progress.json')
        print(f'[{stage}] ' + ' '.join(f'{key}={value}' for key, value in details.items()), flush=True)

    progress('created', output=str(output))
    # A blocked socket call or GUI shutdown can otherwise look completely idle.
    faulthandler.dump_traceback_later(30, repeat=False)
    try:
        if args.video:
            result['video_tool_versions'] = {}
            for tool in ('ffmpeg', 'ffprobe'):
                executable = shutil.which(tool)
                if not executable:
                    raise RuntimeError(f'{tool} is not on PATH; install the offline-video tools first.')
                report = subprocess.run([executable, '-version'], check=True, capture_output=True, text=True, timeout=15)
                result['video_tool_versions'][tool] = {'path': executable, 'version': report.stdout.splitlines()[0]}
            result['software_rendering_request'] = os.environ.get('LIBGL_ALWAYS_SOFTWARE', '')
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
            command += ['--start', '--quit-on-end']
        if args.video:
            command += ['--window-size', '1400,900', '--window-pos', '0,0']
        result['command'] = command
        progress('starting_sumo', binary=binary)
        api.start(command)
        started = True
        result['sumo_api_version'] = list(api.getVersion())
        progress('connected', version=result['sumo_api_version'][1])
        result['simulation_step_s'] = api.simulation.getDeltaT()
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
            if pending_capture is not None:
                pending_capture['following_step_time_s'] = now
                captures.append(pending_capture)
                pending_capture = None
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
            if steps % 20 == 0:
                progress('simulating', time_s=now, active=len(active), arrived=len(arrived))
            if args.video and api.simulation.getMinExpectedNumber() > 0:
                filename = f'frame_{steps - 1:06d}.png'
                api.gui.screenshot('View #0', str(output / 'frames' / filename), 1280, 720)
                pending_capture = {'index': steps - 1, 'file': filename, 'request_time_s': now}
            elif args.gui and not args.video and now >= 40 and not screenshot_requested:
                api.gui.screenshot('View #0', str(screenshot), 1280, 720)
                screenshot_requested = True
                # SUMO writes the requested image on the following simulationStep.
            if args.gui and not args.video and args.frame_delay:
                time.sleep(args.frame_delay)
        remaining = api.simulation.getMinExpectedNumber()
        if remaining or departed != expected or arrived != expected:
            raise RuntimeError(f'Incomplete example: departed={len(departed)}, arrived={len(arrived)}, remaining={remaining}.')
        if teleports:
            raise RuntimeError(f'Unexpected teleportation in dummy example: {teleports}')
        if not all((baseline_observed, low_set, high_set, low_observed, high_observed)):
            raise RuntimeError('Speed command/readback or actual slowing/recovery check did not complete.')
        result['completion_time_s'] = api.simulation.getTime()
        if pending_capture is not None:
            raise RuntimeError('A deferred screenshot was not flushed by the final normal simulation step.')
        progress('closing_sumo', time_s=result['completion_time_s'], arrived=len(arrived))
        api.close()
        started = False
        progress('sumo_closed')
        trips = ET.parse(output / 'tripinfo.xml').findall('tripinfo')
        if {item.attrib['id'] for item in trips} != expected or len(trips) != len(expected):
            raise RuntimeError('Trip output does not contain exactly the 12 expected completed vehicles.')
        if any(float(item.attrib.get('arrival', '-1')) < 0 or
               item.attrib.get('vaporized', '').lower() not in ('', '0', 'false') for item in trips):
            raise RuntimeError('Trip output contains an unfinished or removed vehicle.')
        if args.video:
            if len(captures) != steps - 1 or not captures:
                raise RuntimeError('Incomplete frame-request record.')
            frames = [output / 'frames' / item['file'] for item in captures]
            progress('encoding_and_checking_video', frames=len(frames))
            result['video'] = encode_movie(output, frames, args.video_fps)
            result['video']['nominal_playback_speed'] = args.video_fps * result['simulation_step_s']
            shutil.copyfile(frames[min(39, len(frames) - 1)], screenshot)
        elif args.gui and (not screenshot_requested or not screenshot.is_file() or screenshot.read_bytes()[:8] != b'\x89PNG\r\n\x1a\n'):
            raise RuntimeError('GUI did not produce the expected PNG; inspect the SUMO log.')
        result['status'] = 'passed'
        progress('passed', arrived=len(arrived))
    except BaseException as exc:
        error = exc
        result['error'] = f'{type(exc).__name__}: {exc}'
        progress('failed', error=result['error'])
    finally:
        if started:
            try:
                progress('cleanup_wait')
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
        if args.video:
            result['frame_requests_flushed'] = len(captures)
            with (output / 'frames.csv').open('w', newline='') as stream:
                writer = csv.DictWriter(stream, fieldnames=['index', 'file', 'request_time_s', 'following_step_time_s'])
                writer.writeheader()
                writer.writerows(captures)
        (output / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
        faulthandler.cancel_dump_traceback_later()
    if error:
        print(f'FAIL: {result["error"]}\nDetails: {output}', file=sys.stderr)
        return 130 if isinstance(error, KeyboardInterrupt) else 1
    view_mode = 'offline video' if args.video else 'live GUI' if args.gui else 'no GUI'
    print(f'PASS: {args.case}, {args.backend}, {view_mode}; all 12 vehicles finished.')
    print(f'Outputs: {output}')
    if args.video:
        print('Download scenario.mp4 and view.png; playback and scene correctness still need your confirmation.')
    elif args.gui:
        print('Inspect view.png and the visible Windows window; visual correctness still needs your confirmation.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
