#!/usr/bin/env python3
"""Create two disposable SUMO installation examples; never overwrite a workspace.

Input format: https://sumo.dlr.de/docs/Tutorials/Hello_SUMO.html
These are installation examples, not specifications of the research task.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

VERSION = '1.28.0'
VEHICLES = 12
CASES = {'straight': (1, 1), 'lane_drop': (3, 2)}


def source_files(case: str) -> dict[str, str]:
    upstream, downstream = CASES[case]
    vehicles = '\n'.join(
        f'  <vehicle id="v{i}" type="car" route="route0" depart="{3 * i}" '
        f'departLane="{i % upstream}" departSpeed="0" '
        f'color="{("1,0.2,0.2" if i == 0 else "0.2,0.5,1")}"/>'
        for i in range(VEHICLES)
    )
    return {
        'nodes.nod.xml': '''<nodes>
  <node id="start" x="0" y="0"/>
  <node id="middle" x="400" y="0"/>
  <node id="finish" x="800" y="0"/>
</nodes>
''',
        'edges.edg.xml': f'''<edges>
  <edge id="up" from="start" to="middle" numLanes="{upstream}" speed="13.9"/>
  <edge id="down" from="middle" to="finish" numLanes="{downstream}" speed="13.9"/>
</edges>
''',
        'routes.rou.xml': f'''<routes>
  <vType id="car" accel="2.6" decel="4.5" sigma="0" length="5"
         minGap="2.5" maxSpeed="13.9" speedFactor="1" speedDev="0"/>
  <route id="route0" edges="up down"/>
{vehicles}
</routes>
''',
        'test.sumocfg': '''<configuration>
  <input>
    <net-file value="network.net.xml"/>
    <route-files value="routes.rou.xml"/>
  </input>
  <time>
    <begin value="0"/>
    <step-length value="1"/>
  </time>
</configuration>
''',
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path, help='New workspace; must not already exist.')
    args = parser.parse_args()
    root = args.output.expanduser().resolve()
    binary = shutil.which('netconvert')
    if not binary:
        parser.error('netconvert is not on PATH; activate the SUMO environment first.')
    version = subprocess.run([binary, '--version'], check=True, capture_output=True, text=True, timeout=30)
    if not re.search(r'\b1\.28\.0\b', version.stdout):
        parser.error(f'Expected netconvert {VERSION}; got {version.stdout.strip()}')
    root.mkdir(parents=True, exist_ok=False)
    metadata = {'created_utc': datetime.now(timezone.utc).isoformat(), 'seed': 42,
                'netconvert': binary, 'netconvert_version': version.stdout.strip(), 'cases': {}}
    for case, counts in CASES.items():
        folder = root / case
        folder.mkdir()
        for name, content in source_files(case).items():
            ET.fromstring(content)
            (folder / name).write_text(content)
        command = [binary, '--node-files', str(folder / 'nodes.nod.xml'),
                   '--edge-files', str(folder / 'edges.edg.xml'),
                   '--output-file', str(folder / 'network.net.xml')]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=60)
        (folder / 'netconvert.log').write_text(completed.stdout + completed.stderr)
        if completed.returncode:
            raise SystemExit(f'netconvert failed for {case}; inspect {folder / "netconvert.log"}.')
        network = ET.parse(folder / 'network.net.xml').getroot()
        actual = tuple(len(network.find(f"edge[@id='{edge}']").findall('lane')) for edge in ('up', 'down'))
        if actual != counts:
            raise SystemExit(f'Unexpected lane counts for {case}: {actual}, expected {counts}.')
        metadata['cases'][case] = {'vehicles': VEHICLES, 'lane_counts': list(counts),
            'files_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                             for p in sorted(folder.iterdir()) if p.is_file()}}
    (root / 'cases.json').write_text(json.dumps(metadata, indent=2) + '\n')
    print(f'Created straight and lane_drop examples in {root}')
    print('No traffic simulation has been run by this command.')


if __name__ == '__main__':
    main()
