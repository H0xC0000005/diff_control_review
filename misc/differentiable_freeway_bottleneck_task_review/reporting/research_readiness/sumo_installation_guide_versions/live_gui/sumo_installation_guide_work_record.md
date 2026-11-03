# SUMO installation guide: scope, sources and checks

2026-10-29. The user requests a tailored installation procedure, local dummy
checks and Windows GUI testing after the feasibility assessment. Deliver
the guide and executable installation-check helpers; do not execute the
installation, network conversion, traffic checks or GUI in this task.

The guide retains the isolated Python 3.12 / SUMO 1.28.0 wheel route,
libsumo for runs without a GUI and TraCI for visible sessions. Installation
helpers create a straight road and a native three-to-two dummy network,
then check querying/control/completion and optionally a deferred PNG.
These examples do not specify a VSL scientific model or its validation.
The Windows visual confirmation is kept separate from automated results.

## Official documentation reviewed

- [Downloads and Python wheels](https://sumo.dlr.de/docs/Downloads.php).
- [Installation and Linux build qualifications](https://sumo.dlr.de/docs/Installing/Linux_Build.html).
- [libsumo and GUI/API limitations](https://sumo.dlr.de/docs/Libsumo.html).
- [TraCI Python startup, stepping and diagnosis](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html).
- [Hello SUMO input construction](https://sumo.dlr.de/docs/Tutorials/Hello_SUMO.html).
- [Vehicles, routes and speed variation](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html).
- [Simulation query API](https://sumo.dlr.de/pydoc/traci/_simulation.html).
- [Edge lane-count API](https://sumo.dlr.de/pydoc/traci/_edge.html).
- [Vehicle speed and road API](https://sumo.dlr.de/pydoc/traci/_vehicle.html).
- [Maximum-speed API](https://sumo.dlr.de/pydoc/traci/_vehicletype.html).
- [GUI API, boundary and deferred screenshot](https://sumo.dlr.de/pydoc/traci/_gui.html).
- [GUI operation and start flag](https://sumo.dlr.de/docs/sumo-gui.html).
- [Trip completion output and vaporized flag](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html).
- [SUMO wheel command launchers](https://github.com/eclipse-sumo/sumo/blob/main/build_config/pyproject/eclipse-sumo.toml).
- [Application wheel release](https://pypi.org/project/eclipse-sumo/1.28.0/).
- [libsumo wheel release](https://pypi.org/project/libsumo/1.28.0/).
- [MobaXterm X11 and OpenGL settings](https://mobaxterm.mobatek.net/documentation.html).

Conda 26.3.2 create options were checked from the installed CLI. Current
OS/package metadata and the existing assessment supply the server facts.
Only primary sources support technical instructions. Failed underscore-dot
pydoc URLs were corrected to the working slash paths; no inaccessible
release-source response is treated as inspected evidence. Live API docs
support the calls; runtime compatibility with the pinned packages is still
to be checked after installation.

## Delivered files and verification boundary

[Installation guide](sumo_installation_guide.md)

[Pinned package list](sumo_installation_checks/requirements-sumo.txt)

[Case creator](sumo_installation_checks/prepare_cases.py)

[Python checker](sumo_installation_checks/run_check.py)

[Document/helper validation](sumo_installation_guide_validation.json)

Static checks parse both Python helpers, parse all eight generated input
XML documents, inspect IDs/departures/lanes, exercise --help without SUMO,
and check each guide shell block with bash -n. They check local links,
file hashes and that only the intended documentation/helper files change.
They do not run netconvert, SUMO, libsumo, TraCI or a GUI. No fake backend
is used to manufacture a simulation result.

The trip-output check accepts false/0/absent vaporized flags and rejects
removed or incomplete vehicles. The screenshot request is followed by
additional simulation steps. Initial motion, slowing and later acceleration
are separate observations. These details were checked against the API
and output definitions, not demonstrated by an executed trajectory.

Preparation/validation helpers are under
`/tmp/sumo_installation_guide_20261029/`. Commands are:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_installation_guide_20261029/prepare_delivery.py
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_installation_guide_20261029/validate_guide.py --staged
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_installation_guide_20261029/apply_delivery.py
git diff --check
```

The apply helper needs filesystem escalation only because the standalone
review repository is outside the current writable roots. Existing review
changes are preserved. The urban and VSL implementation repositories,
scientific contracts, archived evidence and feedback remain untouched.
No dependencies, environment configuration or remote repository are changed.

The guide-writing task ends here. Installation can be a subsequent,
explicitly authorized tooling task ending at the listed checks and Windows
visual confirmation. Model selection and full VSL Phase A remain on hold.
