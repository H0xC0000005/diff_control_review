# SUMO installation and checks: Ubuntu server, Python, Windows GUI

Prepared 2026-10-29 for Ubuntu 24.04.4 LTS/x86-64 and a Windows 11 SSH
client. **This is a procedure to follow, not a completed installation.**
The accompanying scripts have been checked without installing or running
SUMO; actual runtime and Windows display results remain to be established.

Install one pinned SUMO release in a separate Conda environment. Use
**libsumo for automated runs without a window** and **TraCI with sumo-gui
for visible sessions**. The simulation runs on Ubuntu; an X server on
Windows displays its window over SSH. This satisfies the programming and
viewing requirements while avoiding dependence on experimental libsumo GUI
support. No physical server display or full Ubuntu desktop is required.
[libsumo documentation](https://sumo.dlr.de/docs/Libsumo.html).

The examples below test the installation. They do not select either VSL
formulation, calibrate merging, establish useful gradients or make SUMO a
required research-validation layer.

## 1. Files and working locations

Keep the supplied helpers beside this guide:

- [Pinned packages](sumo_installation_checks/requirements-sumo.txt).
- [Create the dummy cases](sumo_installation_checks/prepare_cases.py).
- [Run the Python checks](sumo_installation_checks/run_check.py).

On the **Ubuntu server**, use Bash. Set these variables in the shell where
you follow the guide:

```bash
SUMO_GUIDE_DIR=/home/zpz/repos/diff_control_review/misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness
SUMO_CHECK_ROOT="$HOME/sumo_installation_checks_1_28"
```

SUMO installs into the new `sumo-1.28` environment. Generated networks and
results go under `SUMO_CHECK_ROOT`, outside both implementation repositories.
The case creator refuses an existing workspace. If repeating preparation,
use another workspace name or reuse the completed one without recreating it.
Each check creates a new result directory and preserves earlier results.

## 2. Install matching binaries and Python interfaces

The inspected server already has Miniconda. Initialize its shell support
without modifying `.bashrc`, then create a dedicated environment:

```bash
source /home/zpz/miniconda3/etc/profile.d/conda.sh
conda create --name sumo-1.28 --no-default-packages python=3.12 pip
conda activate sumo-1.28
python -m pip install --only-binary=:all: -r "$SUMO_GUIDE_DIR/sumo_installation_checks/requirements-sumo.txt"
python -m pip check
```

If an environment called `sumo-1.28` already exists, inspect it or choose
a new name; do not overwrite another environment. The pins are SUMO,
libsumo, TraCI and sumolib **1.28.0**, the official release checked for this
guide. Linux application wheels and CPython 3.12 libsumo wheels are available.
`--only-binary` makes a missing compatible wheel an explicit installation
failure instead of silently attempting a source build. The Python packages
can be installed at user level; any later missing OS libraries are separate.
[Official package installation](https://sumo.dlr.de/docs/Downloads.php#python-packages-virtual-environments),
[application release](https://pypi.org/project/eclipse-sumo/1.28.0/),
[libsumo release](https://pypi.org/project/libsumo/1.28.0/).

Do not add the Ubuntu apt SUMO executable to this environment. The server's
cached apt metadata offers 1.18.0, which is a different release. A source
build or PPA is unnecessary for the initial wheel route. If a source build
ever becomes necessary, the official documentation advises against building
inside an active Anaconda environment.
[Linux installation/build notes](https://sumo.dlr.de/docs/Installing/Linux_Build.html).

Check which programs and modules the active environment supplies:

```bash
command -v python
command -v sumo
command -v sumo-gui
command -v netconvert
sumo --version
netconvert --version
sumo-gui --version
python - <<'PY'
import importlib
from importlib.metadata import version
for package in ('eclipse-sumo', 'libsumo', 'traci', 'sumolib'):
    print(package, version(package))
for module in ('sumo', 'libsumo', 'traci', 'sumolib'):
    loaded = importlib.import_module(module)
    print(module, loaded.__file__)
PY
```

Expected: executable locations and module paths belong to this environment,
and all four package versions are 1.28.0. `pip check` reports no broken
requirements. `sumo-gui --version` checks loading, not actual rendering.
If that command requires a display or reports a GUI-library problem,
complete the headless checks and diagnose the GUI path in Sections 5–7.

Set SUMO_HOME for this shell from the installed package:

```bash
export SUMO_HOME="$(python -c 'import sumo; print(sumo.SUMO_HOME)')"
unset LIBSUMO_AS_TRACI LIBSUMO_GUI
```

Installed bindings already import normally; this setup needs no manual
`PYTHONPATH` addition. If module paths point elsewhere, inspect inherited
`PYTHONPATH` or a same-named local Python file before proceeding.

## 3. Create two tiny cases

```bash
python "$SUMO_GUIDE_DIR/sumo_installation_checks/prepare_cases.py" --output "$SUMO_CHECK_ROOT"
```

The creator invokes the installed `netconvert` to build networks and
checks the resulting lane counts. This builds inputs; it does not advance
traffic. Its XML follows SUMO's elementary nodes/edges/routes construction.
[Hello SUMO tutorial](https://sumo.dlr.de/docs/Tutorials/Hello_SUMO.html).

| Case | Contents | Why it is included |
|---|---|---|
| `straight` | Two consecutive 400 m edges, one lane each. | Tests loading, stepping, queries, a speed command and trip completion with simple geometry. |
| `lane_drop` | Two consecutive 400 m edges, three lanes followed by two. | Tests basic lane-count geometry and provides an intuitive GUI example using SUMO's native behavior. |

Each case contains exactly 12 cars, departures every three seconds, a
13.9 m/s speed limit and one-second simulation steps. Imperfection and
speed-factor variation are zero; check runs use seed 42. Speeds here and
in the API are in **m/s**. These settings are disposable installation
inputs, not VSL research parameters. The lane-drop case does not prescribe
the review's preparation/forced-merge zones or any policy-validation ladder.
[Vehicle and route definitions](https://sumo.dlr.de/docs/Definition_of_Vehicles,_Vehicle_Types,_and_Routes.html).

The workspace contains `straight/`, `lane_drop/` and `cases.json`.
Each case has XML inputs, `network.net.xml`, `test.sumocfg` and
`netconvert.log`. The manifest records input hashes and the converter version.

## 4. Test Python control on the server without a GUI

Run each command after the preceding one succeeds:

```bash
python "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py" --workspace "$SUMO_CHECK_ROOT" --case straight --backend libsumo
python "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py" --workspace "$SUMO_CHECK_ROOT" --case straight --backend traci
python "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py" --workspace "$SUMO_CHECK_ROOT" --case lane_drop --backend libsumo
```

The libsumo run exercises the in-process library. The headless TraCI run
also launches the installed SUMO executable and tests its socket interface.
The common operations are documented by SUMO, subject to libsumo's API
limitations.
[Python control](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html),
[simulation queries](https://sumo.dlr.de/pydoc/traci/_simulation.html).

The checker reads lane counts and live vehicle states. At simulation time
5 s, it lowers red car `v0`'s maximum speed to 5 m/s; at 15 s, it restores
13.9 m/s. It verifies command readback, an actual low-speed sample after
settling, subsequent acceleration, all 12 departures/arrivals, no teleports
and a completed trip record for each car. This is ordinary vehicle control,
not a VSL control law. The speed need not jump immediately when the limit
changes: SUMO still handles acceleration and deceleration.
[Speed command semantics](https://sumo.dlr.de/pydoc/traci/_vehicletype.html),
[completed-trip output](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html).

Expected terminal output begins with `PASS` and reports 12 finished cars.
Each invocation writes a unique folder under `results/`:

- `result.json`: pass/fail, versions, command, counts and control observations.
- `trace.csv`: active/completed counts and `v0`'s speed, limit and road.
- `tripinfo.xml`: one completed-trip record per car.
- `sumo.log`: simulator messages for diagnosis.

A failure returns a nonzero exit status and preserves the available outputs.
The 240-step limit prevents an endless test; reaching it with unfinished
traffic is a failure, not clearance. These are expected outcomes, not
measured results from this guide-writing task.

## 5. Prepare the display from your Windows 11 PC

On **Windows**, use MobaXterm with its X server running. Create or edit
your normal SSH session, retain the usual host/user/key/port or gateway,
and enable **X11-Forwarding** in its SSH settings. Reconnect through that
session. A separate old terminal or an already-running tmux session may
retain no display or an expired display; begin with the fresh SSH shell.
[MobaXterm documentation](https://mobaxterm.mobatek.net/documentation.html).

In that **Ubuntu shell**, check:

```bash
printenv DISPLAY
```

Expected: an SSH-assigned value such as `localhost:10.0`. Do not substitute
`:0` or your PC's IP manually for this forwarded connection. The inspected
server already has xauth and configured X11 forwarding, so no SSH service
restart or full desktop installation is part of the default procedure.
If DISPLAY is empty, fix forwarding before trying SUMO graphics.

If the administrator can add small diagnostic applications, the commands
below install a basic X client and an OpenGL diagnostic, not SUMO:

```bash
sudo apt-get update
sudo apt-get install x11-apps mesa-utils
xclock
```

A clock should appear on Windows. Close it, then check:

```bash
glxinfo -B
```

This should report an OpenGL renderer without a GLX error. A working clock
confirms basic X11 only; it does not prove OpenGL rendering. These diagnostic
packages are optional: if you lack administrator access, test sumo-gui
directly and preserve its error if it fails.

## 6. View the lane drop and test a controlled GUI session

In the same fresh SSH shell, activate the environment again and restore
the guide/workspace variables from Section 1:

```bash
source /home/zpz/miniconda3/etc/profile.d/conda.sh
conda activate sumo-1.28
SUMO_GUIDE_DIR=/home/zpz/repos/diff_control_review/misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness
SUMO_CHECK_ROOT="$HOME/sumo_installation_checks_1_28"
unset LIBSUMO_AS_TRACI LIBSUMO_GUI
sumo-gui -c "$SUMO_CHECK_ROOT/lane_drop/test.sumocfg" --seed 42 --delay 100
```

This first GUI check has no Python controller. Press Play or single-step,
pan/zoom, and inspect the three-to-two road and moving cars. Close this
window before the automated GUI check. A blank canvas or window frame
alone is not a rendering pass.
[GUI operation](https://sumo.dlr.de/docs/sumo-gui.html).

Then run the Python-controlled visible check:

```bash
python "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py" --workspace "$SUMO_CHECK_ROOT" --case lane_drop --backend traci --gui --frame-delay 0.2
```

It starts the GUI automatically, runs the same control checks and closes
its window after completion. `--frame-delay` slows wall-clock playback
only; use 0.5 or 1.0 for more viewing time. Pausing the GUI can also pause
progress while TraCI waits; resume Play to continue. Closing it early
interrupts the check and should produce a failure record.

The checker requests `view.png` at about simulation time 40 s and advances
another step: SUMO's screenshot call saves on the **next** simulation step.
The image is written on Ubuntu in the new result folder. Download it with
MobaXterm's SFTP browser or your usual file-transfer client.
[GUI commands and deferred screenshot](https://sumo.dlr.de/pydoc/traci/_gui.html).

Confirm yourself that the Windows window renders cars/lanes, responds to
interaction, and the downloaded image is meaningful. A valid PNG file
alone cannot prove that it contains a correctly rendered scene. Consequently
the JSON leaves `manual_gui_check` as `pending`; your visual confirmation
completes that part of installation acceptance. For later paper figures,
native snapshots are preferable to capturing the whole remote window;
vector export is available only when enabled by the build.

## 7. Diagnose the failing layer

| Symptom | Next action |
|---|---|
| Wrong program or module version | Reactivate `sumo-1.28`; inspect command/module paths. Remove an old SUMO tools path from this shell's import path if it is overriding installed bindings. |
| Missing `.so` before any window opens | Record the exact library name. An administrator can add its runtime package: `libGL.so.1` → `libgl1`; `libGLU.so.1` → `libglu1-mesa`; `libFOX-1.6.so.0` → `libfox-1.6-0`. Wheels may already bundle some of these; install only what the actual failure requires. |
| No DISPLAY / cannot open display | Reconnect with the Windows X server and SSH X11 forwarding enabled. Check key/gateway restrictions if the server configuration appears correct. |
| Clock works, but GLX fails or SUMO has a blank canvas | Check MobaXterm's OpenGL setting; use the one-command diagnostic below. The CPU/Python installation may already be sound. |
| TraCI cannot connect | Inspect its new result folder's `sumo.log` and terminal error: a failed SUMO/GUI startup can look like a connection problem. |
| Some vehicles do not finish / a teleport is reported | Inspect the trace and log. This is a failed example check; do not silently count removed traffic as completed. |
| GUI is correct but too slow | Keep libsumo for automated server runs. Consider a separate application-streaming setup or a matching Windows GUI installation for selected visual examples. |

MobaXterm documents indirect OpenGL as an option. Try it for one command
only, after a normal attempt fails:

```bash
LIBGL_ALWAYS_INDIRECT=1 sumo-gui -c "$SUMO_CHECK_ROOT/lane_drop/test.sumocfg" --seed 42 --delay 100
```

If that fixes viewing, the same prefix can be applied to the Python GUI
command. It is not guaranteed to fix every GLX problem. Do not treat a
working NVIDIA/CUDA probe as proof of a working remote display.

A virtual display such as Xvfb can support later automated image generation,
but by itself does not display an interactive window on your PC. If X11
cannot be made usable, a native Windows SUMO 1.28.0 GUI can instead run the
same small XML example locally. That is a separate local visual run, not
proof that server-to-PC forwarding works. Use the official matching-release
Windows package if choosing this fallback.
[Windows downloads](https://sumo.dlr.de/docs/Downloads.php#windows).

For that fallback, install or extract the matching Windows release, copy
the entire generated `lane_drop` folder to the PC, start `sumo-gui.exe`,
and use File → Open Simulation to open its `test.sumocfg`. The relative
network/route paths remain valid when the folder is copied intact. Basic
local viewing needs no Python installation. This additional Windows SUMO
installation is unnecessary for the primary SSH-forwarding route.

## 8. Record the installation and stop

After the checks, save the resolved package lists and executable versions
in the workspace:

```bash
conda list --explicit > "$SUMO_CHECK_ROOT/conda-explicit.txt"
python -m pip freeze > "$SUMO_CHECK_ROOT/pip-freeze.txt"
sumo --version > "$SUMO_CHECK_ROOT/sumo-version.txt"
netconvert --version > "$SUMO_CHECK_ROOT/netconvert-version.txt"
```

Together with `cases.json` and the result directories, these identify the
actual installation and input member. Record a brief Windows visual-check
note: SSH client/version, whether roads/cars and interaction worked, and
which screenshot you inspected. Do not copy credentials or connection keys
into this record.

| Check | Acceptance |
|---|---|
| Environment and packages | Matching versions, intended paths and no `pip check` conflict. |
| Case preparation | Both expected lane-count networks generated; logs and hashes retained. |
| Headless Python control | Three commands in Section 4 pass; all 12 vehicles finish in each; speed control is observed and no teleport occurs. |
| Remote visible control | TraCI GUI check passes and the user confirms the Windows view and saved image. |

Stop after reporting these results. Passing means SUMO is ready as a
programmable and viewable tool. It establishes neither VSL-model agreement
nor research validity. There is no automatic continuation into simulation
development, optimization, calibration or traffic experiments.
