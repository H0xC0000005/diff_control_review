# SUMO installation and checks: server runs, videos on Windows

Prepared 2026-10-29 for Ubuntu 24.04.4 LTS/x86-64 and a Windows 11 SSH
client. **This is a procedure to follow, not a completed installation.**
Initial checks were static. A later troubleshooting pass verified the
off-screen lane-drop check through MP4 encoding after correcting GUI
shutdown. Windows playback remains for the user to confirm.
[Diagnosis and bounded verification](sumo_gui_shutdown_troubleshooting.md).

**Default viewing route: render on Ubuntu, download an MP4 and inspect it
on Windows.** This meets the user's visual-understanding requirement while
removing the need for live GUI forwarding. Install one pinned SUMO release
in a separate Conda environment. Use libsumo for ordinary automated runs;
use TraCI with off-screen sumo-gui only when generating visual examples.
The server needs Xvfb/OpenGL and an encoder; Windows needs a video player.
Live interactive GUI remains an optional addition.

The recording route uses native PNG snapshots and external FFmpeg, as
described by SUMO. It does not depend on built-in SUMO video encoding or
experimental libsumo GUI support.
[SUMO video options](https://sumo.dlr.de/docs/FAQ.html#building-videos-from-sumo-gui),
[libsumo limitations](https://sumo.dlr.de/docs/Libsumo.html).

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

SUMO installs into the new `sumo` environment. Generated networks and
results go under `SUMO_CHECK_ROOT`, outside both implementation repositories.
The case creator refuses an existing workspace. If repeating preparation,
use another workspace name or reuse the completed one without recreating it.
Each check creates a new result directory and preserves earlier results.

## 2. Install matching binaries and Python interfaces

The inspected server already has Miniconda. The user has since installed
and named the dedicated environment `sumo` (earlier guide versions called
it `sumo-1.28`). If it already exists, activate it and skip creation. For
a fresh installation, initialize shell support without modifying `.bashrc`:

```bash
source /home/zpz/miniconda3/etc/profile.d/conda.sh
conda create --name sumo --no-default-packages python=3.12 pip
conda activate sumo
python -m pip install --only-binary=:all: -r "$SUMO_GUIDE_DIR/sumo_installation_checks/requirements-sumo.txt"
python -m pip check
```

If an environment called `sumo` already exists, inspect it or choose
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
The 240-step limit detects a case that fails to clear after repeated
updates. It cannot interrupt a blocked startup, socket call or shutdown;
the wall-clock wrapper in Section 6 bounds that separate risk. The
off-screen lane-drop run has now been checked as documented below; the
other commands remain instructions to run, not newly reported test results.

## 5. Add off-screen rendering and video tools on Ubuntu

For your viewing purpose, **recording on the server and downloading a video
is the simpler default**. Windows needs only your existing file-transfer
connection and an MP4 player. It needs no X server, X11 forwarding, SUMO
installation or live graphics connection for this route.

The server still needs to draw SUMO's native view. Xvfb supplies a virtual
display; Mesa supplies software OpenGL; FFmpeg turns numbered PNG frames
into a video. This is off-screen GUI rendering, separate from libsumo's
ordinary run without a GUI. Software rendering applies to the pictures;
it changes no traffic rule or control command. Xvfb can run without physical
display hardware, and its wrapper manages the temporary display and xauth.
[Ubuntu Xvfb](https://manpages.ubuntu.com/manpages/noble/man1/Xvfb.1.html),
[xvfb-run](https://manpages.ubuntu.com/manpages/noble/man1/xvfb-run.1.html),
[Mesa software-rendering setting](https://docs.mesa3d.org/envvars.html).

The original assessment found Xvfb and FFmpeg absent. The user has now
installed the system packages successfully; skip this transaction if
already completed. For a fresh server, an administrator can add the
rendering runtimes once:

```bash
sudo apt-get update
sudo apt-get install xvfb xauth ffmpeg mesa-utils libgl1 libglu1-mesa libgl1-mesa-dri libglx-mesa0
```

This installs rendering/encoding tools, not a second SUMO release or a
desktop environment. It does not call for changing the NVIDIA driver.
If you cannot install system packages, this one-time administrator action
is a remaining prerequisite for the proposed route.

In your ordinary Ubuntu SSH shell, with the SUMO environment active, test
the virtual display independently of Windows:

```bash
LIBGL_ALWAYS_SOFTWARE=true xvfb-run -a -s "-screen 0 1600x1000x24 +extension GLX" glxinfo -B
ffmpeg -version
ffprobe -version
ffmpeg -hide_banner -encoders | grep -F libx264
```

Expected: an OpenGL renderer such as llvmpipe, no GLX error, and an available
`libx264` encoder. Xvfb sets DISPLAY for its child command; do not manually
set DISPLAY or enable X11 forwarding for these commands. `-a` selects an
available virtual display number. The larger virtual screen accommodates
the GUI window and its 1280×720 saved view. A successful renderer diagnostic
is a prerequisite, not proof that the eventual movie looks correct.

SUMO also has direct video output in builds with FFmpeg support compiled
in. The guide uses its documented PNG-sequence route with external FFmpeg,
so the installed SUMO build need not include that encoder feature.
[SUMO video options](https://sumo.dlr.de/docs/FAQ.html#building-videos-from-sumo-gui).

## 6. Record the dummy case and watch it on Windows

Use the SUMO environment and initialize the paths in the shell running
the check. These custom variables are not carried automatically into a
new terminal. The preparation workspace must already exist from Section 3:

```bash
conda activate sumo
SUMO_GUIDE_DIR=/home/zpz/repos/diff_control_review/misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness
SUMO_CHECK_ROOT="$HOME/sumo_installation_checks_1_28"
ls "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py"
ls "$SUMO_CHECK_ROOT/lane_drop/test.sumocfg"
```

Run the entire command, including the Python program after xvfb-run's
options. Each trailing backslash joins the following line:

```bash
timeout --signal=INT --kill-after=10s 120s \
  env LIBGL_ALWAYS_SOFTWARE=true \
  xvfb-run -a -s "-screen 0 1600x1000x24 +extension GLX" \
  python -u "${SUMO_GUIDE_DIR:?Set SUMO_GUIDE_DIR in this shell}/sumo_installation_checks/run_check.py" \
  --workspace "${SUMO_CHECK_ROOT:?Set SUMO_CHECK_ROOT in this shell}" \
  --case lane_drop --backend traci --video --video-fps 5
```

The 120-second wall-clock bound applies only to this small installation
check. If it expires, the check has failed; it is not evidence that traffic
completed. The timeout sends an interrupt, then stops its own process
group if cleanup still waits. It does not target unrelated runs.

The helper now launches GUI checks with **--start --quit-on-end**. The
first flag starts simulation; the second lets the off-screen GUI exit
when the client closes the simulation. Without the second, ordinary
traci.close() can wait for a GUI window that nobody can close on Xvfb.
Keep the shutdown wait so output files finish flushing before validation.
[SUMO GUI shutdown option](https://sumo.dlr.de/docs/sumo-gui.html),
[TraCI close behavior](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html).

Progress is printed immediately and saved atomically in `progress.json`:
created → starting_sumo → connected → simulating → closing_sumo →
sumo_closed → encoding_and_checking_video → passed. A Python stack dump
is emitted after 30 seconds if the check is still running; it identifies
the current call and is not itself a timeout or an automatic failure.
The bound above is what prevents an indefinite wait.

One command starts an off-screen sumo-gui, performs the existing control
and completion checks, saves frames and encodes `scenario.mp4`. No window
should appear on your PC or the server console. The example's traffic,
seed, one-second time step and speed-command schedule are unchanged.

Expected: `PASS`, all 12 cars completed, and a printed result-folder path.
That folder includes the earlier logs/data plus:

- `scenario.mp4`: H.264 video with yuv420p pixels for ordinary PC playback.
- `view.png`: a representative native frame, useful for close inspection.
- `frames/`: the numbered source PNGs, preserved rather than deleted.
- `frames.csv`: frame index, screenshot-request time and the following step
  that flushed the deferred capture.
- `video_command.json`, `ffmpeg.log`, `ffprobe.json` and `decode.log`:
  encoding/probing commands, properties and a complete decode check.

The helper verifies every expected frame's dimensions, encoded format,
positive/consistent duration and full MP4 decoding. Encoding failures leave
the PNGs and available diagnostics intact. File names are local paths on
Ubuntu, not on Windows. The screenshot API writes on the next simulation
step, so the last pending request is flushed by the normal completion step;
no request is left unflushed at exit.
[SUMO screenshot API](https://sumo.dlr.de/pydoc/traci/_gui.html),
[FFmpeg image sequences](https://manpages.ubuntu.com/manpages/noble/man1/ffmpeg-formats.1.html),
[H.264 encoder](https://manpages.ubuntu.com/manpages/noble/man1/ffmpeg-codecs.1.html),
[ffprobe](https://manpages.ubuntu.com/manpages/noble/man1/ffprobe.1.html).

**Playback time is explicit.** The dummy case supplies one picture per
one-second simulation update. `--video-fps 5` plays those pictures at five
per second: nominally **5× simulation time**. Use `--video-fps 1` for
nominal real-time playback. The MP4 stream is written at 25 fps by repeating
pictures; that does not add intermediate simulated states or smooth the
traffic model. The result JSON records the time step, chosen playback
rate and encoded duration. `--frame-delay` is ignored for offline recording.
The two frame times in the CSV describe the deferred request/flush, rather
than asserting a separately measured render timestamp.

On **Windows**, download `scenario.mp4`, `view.png` and optionally the
small data/JSON records using your usual SFTP client. MobaXterm's file
browser or WinSCP is sufficient; no special graphical SSH session is needed.
You can also run `scp` in Windows Terminal/PowerShell, substituting your
normal SSH alias and the full result path printed by the checker:

```powershell
scp "YOUR_SSH_ALIAS:/full/result/path/scenario.mp4" "$env:USERPROFILE\Downloads\scenario.mp4"
```

Use your usual SSH port/options if not already in that alias. Open the MP4
locally and check that lanes/cars are visible throughout, the lane-count
transition is understandable and motion is plausible for the stated
playback rate. Inspect the PNG at full size. A technically decodable but
blank video is not a visual pass. The JSON therefore leaves
`manual_video_check` as `pending_on_windows` until you confirm playback
and scene content. This user check replaces live-GUI acceptance for the
default installation route.

For future visualization, keep the actual scenario, SUMO version, seed and
control sequence with the movie. A separate render run must use those
same inputs/controls to illustrate that run; it does not automatically
reproduce a libsumo trajectory merely because both APIs are similar.
Render short examples as needed rather than recording every automated run.

## 7. Troubleshooting and optional live inspection

| Symptom | Next action |
|---|---|
| Stops at `closing_sumo` with little CPU activity | Use the corrected helper with `--quit-on-end`. The earlier helper could wait for an off-screen GUI to exit. A running older process does not pick up source edits. |
| Fontconfig `reset-dirs` warning | The successful verification produced the same warning. Inspect the progress stage; this warning did not block rendering or encoding in that check. |
| Script path becomes `/sumo_installation_checks/run_check.py` | Initialize SUMO_GUIDE_DIR in the current shell and activate the SUMO environment. This is an empty variable, not incorrect Bash parsing. |
| Wrong executable or module version | Reactivate `sumo` and inspect command/module paths before proceeding. |
| `xvfb-run`/`xauth` missing or Xvfb fails to start | Install the Section 5 prerequisites; inspect the error. A failed virtual display is separate from the Python interface. |
| Missing `.so` or GLX context error | Check the stated runtime packages. If needed, use the exact missing-library message; e.g. FOX runtime is `libfox-1.6-0`. Repeat the Xvfb/Mesa `glxinfo -B` check. |
| Renderer works but TraCI cannot connect | Inspect the new result folder's `sumo.log` and terminal output for failed sumo-gui startup. |
| PNG sequence missing or incomplete | Treat capture as failed; check the SUMO log and frame request/flush records. The encoder must not silently skip missing expected frames. |
| `libx264` unavailable or encoding fails | Use the Ubuntu FFmpeg build with that encoder; preserve `ffmpeg.log` and frames. A file appearing on disk alone is not an encoding pass. |
| MP4 decodes but looks blank/wrong | Treat rendering as failed. Inspect `view.png` and software OpenGL before changing network or traffic parameters. |
| Clip seems too fast | Check `video-fps` and the recorded simulation step. Five frames per second here means 5× playback, not five new traffic updates per simulated second. |
| Cars do not finish or teleport | Inspect the trace and log; do not count removed traffic as completed. |

For a stalled run, use another terminal and the output folder printed
after `[created]`. Do not infer progress from CPU usage alone:

```bash
SUMO_RUN_DIR="/full/path/printed/by/the/checker"
cat "$SUMO_RUN_DIR/progress.json"
tail -n 30 "$SUMO_RUN_DIR/sumo.log"
ps -C sumo-gui,python,Xvfb,ffmpeg -o pid,ppid,stat,wchan:25,comm
```

Frames already present prove that rendering started. A child-process wait
at closing_sumo points to shutdown; a current encoding stage points to
FFmpeg. Log output can remain buffered before shutdown. The one-time
Python stack dump provides a more precise location if needed. Preserve
partial output folders; reruns receive new names automatically.

**Live GUI remains optional** when you want to pause interactively, click
vehicles or change the camera while running. In that case start MobaXterm's
X server on Windows, enable SSH X11 forwarding, reconnect and confirm an
SSH-assigned DISPLAY. Then use the existing live command:

```bash
python "$SUMO_GUIDE_DIR/sumo_installation_checks/run_check.py" --workspace "$SUMO_CHECK_ROOT" --case lane_drop --backend traci --gui --frame-delay 0.2
```

This route still needs working remote OpenGL and a responsive connection;
its success is not required for offline-video acceptance.
[MobaXterm forwarding documentation](https://mobaxterm.mobatek.net/documentation.html).

If the server's rendering stack cannot be prepared, a matching Windows
SUMO installation can run the copied dummy-case folder locally. That is a
fallback visual run, not verification of server rendering. It is unnecessary
when the MP4 route succeeds. No virtual display or Windows client setup has
been tested as part of writing this guide.

## 8. Record the installation and stop

After the checks, save the resolved versions in the workspace:

```bash
conda list --explicit > "$SUMO_CHECK_ROOT/conda-explicit.txt"
python -m pip freeze > "$SUMO_CHECK_ROOT/pip-freeze.txt"
sumo --version > "$SUMO_CHECK_ROOT/sumo-version.txt"
netconvert --version > "$SUMO_CHECK_ROOT/netconvert-version.txt"
ffmpeg -version > "$SUMO_CHECK_ROOT/ffmpeg-version.txt"
dpkg-query -W xvfb xauth ffmpeg libgl1-mesa-dri libglx-mesa0 libglu1-mesa > "$SUMO_CHECK_ROOT/rendering-packages.txt"
```

Together with `cases.json`, the result directories and source PNGs, these
identify the installation and input member. Add a brief Windows playback
note: player used, whether roads/cars/motion were visible, the chosen
playback rate and the specific video inspected. Keep credentials and
connection keys out of that record.

| Check | Acceptance |
|---|---|
| Environment/packages | Matching SUMO versions, intended paths and no `pip check` conflict. |
| Dummy-case preparation | Both expected lane-count networks generated, with input hashes and logs. |
| Headless Python control | Section 4 checks pass; every car finishes and speed control is observed without teleportation. |
| Server rendering/video | Off-screen TraCI check passes; frame sequence, encoded properties and full MP4 decoding are verified. |
| Viewing on your PC | You download and inspect the MP4 and PNG; scene content is meaningful. Live X11 is optional. |

Stop after reporting these results. This establishes a programmable SUMO
installation and a usable visual-output route. It establishes neither
VSL-model agreement nor research validity, and starts no simulation
development, optimization, calibration or traffic experiment.
