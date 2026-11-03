# SUMO preparation on the server and a Windows SSH client

**Current viewing requirement, 2026-10-29.** The user accepts exported video
instead of a live connection. The [revised installation guide](sumo_installation_guide.md)
therefore prioritizes Xvfb/Mesa rendering on Ubuntu, native PNG frames,
external FFmpeg encoding and MP4 download to Windows. Live X11 is optional.
This simplifies the client/network setup while adding server rendering and
encoding packages. Those packages and their runtime behavior remain to be
tested. The earlier live-GUI feasibility assessment is preserved below.

**Follow-up procedure, 2026-10-29.** The user requests a tailored guide
with runnable dummy checks and Windows viewing instructions.
[Installation guide](sumo_installation_guide.md). The procedure is now
written; installation and runtime/visual checks remain unperformed.

2026-10-29. **Read-only feasibility assessment; installation and display tests
have not been performed.** The user requests programmable SUMO, preferably
libsumo, and a GUI visible on a Windows 11 PC over the usual SSH connection.
This is useful preparation while the VSL model choice remains open. It
does not select a VSL version or reinstate SUMO as a required validation layer.

**The requirements are technically compatible with this server.** Use
libsumo for Python-controlled runs without a GUI and TraCI with sumo-gui
for visual inspection. Forward the Linux GUI through SSH to an X server
on Windows. A physical server monitor or full Ubuntu desktop is unnecessary
for that arrangement. The end-to-end display path still needs a check
from the user's PC.

## What was verified

| Item | Observed state and implication |
|---|---|
| Server platform | Ubuntu 24.04.4 LTS, x86-64, glibc 2.39. Compatible Linux wheels are published. |
| Current Python | Python 3.12.13 in an existing Conda environment. Use a separate environment for SUMO; do not alter either traffic project's environment. |
| SUMO installation | No sumo or sumo-gui executable on PATH; no libsumo, traci or sumolib module in the inspected Python environment; apt reports SUMO uninstalled. |
| Distribution package | The configured apt cache offers SUMO 1.18.0. It is an alternative, but mixing it with current Python bindings would create avoidable version uncertainty. |
| SSH display prerequisites | openssh-server and xauth are installed; /etc/ssh/sshd_config contains X11Forwarding yes and its included configuration directory is empty. This session has no DISPLAY. Client forwarding, key/session restrictions and an actual window remain untested. |
| GUI runtime libraries | X11 and GL libraries are visible; the distro FOX and GLU packages are not recorded as installed. The chosen wheels may bundle dependencies. Actual executable startup must establish whether any system libraries need adding. |
| GPU | A read-only check outside the sandbox sees an NVIDIA Tesla V100 and driver 580.126.09. The initial sandbox check failed, so it is not evidence of a broken driver. This does not verify X11/OpenGL rendering on the Windows client. |

The current official release is 1.28.0, dated 2026-10-08. PyPI publishes
eclipse-sumo for Linux glibc 2.28+ x86-64 and libsumo for CPython 3.12 on
that platform. Matching traci and sumolib 1.28.0 releases are also available.
That supports a binary installation route, not a claim that installation
or GUI startup has already passed.

[Official downloads and release](https://sumo.dlr.de/docs/Downloads.php)

[Application wheel](https://pypi.org/project/eclipse-sumo/1.28.0/)

[Python 3.12 libsumo wheel](https://pypi.org/project/libsumo/1.28.0/)

[TraCI release](https://pypi.org/project/traci/1.28.0/)

[sumolib release](https://pypi.org/project/sumolib/1.28.0/)

## Programming and viewing

libsumo runs the simulator in the Python process and avoids TraCI's socket
communication overhead. It is a good default for later automated runs.
For viewing, Python can instead launch sumo-gui through TraCI. Both runs
use SUMO and can use the same scenario, controls and common API subset;
libsumo has documented API differences, so complete interchangeability
should not be assumed.

The important limitation is **libsumo plus GUI**, which SUMO documents as
highly experimental outside Windows and unsupported on Windows. Here the
simulation would run on Linux, but its GUI support remains experimental.
The user's requirements can be met without relying on that combination:
use libsumo without a GUI, and TraCI for visible sessions.

[libsumo capabilities and limitations](https://sumo.dlr.de/docs/Libsumo.html)

[Python TraCI with sumo or sumo-gui](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html)

For Windows, MobaXterm is a practical first option: it provides an X server
and an SSH client with X11 forwarding. SUMO still executes on Ubuntu;
its window is displayed on the PC. A conventional terminal-only SSH
connection does not by itself provide this display service. MobaXterm's
documentation describes OpenGL support, but performance and compatibility
with this server's actual GUI must be tested.

[MobaXterm: X server and SSH X11 forwarding](https://mobaxterm.mobatek.net/documentation.html)

## Proposed setup sequence

**Prepare the isolated server installation.** In a separately authorized
setup pass, create an environment and install matching release packages.
For the existing Conda installation, the proposed commands are:

```bash
conda create -n sumo python=3.12 pip
conda activate sumo
python -m pip install eclipse-sumo==1.28.0 libsumo==1.28.0 traci==1.28.0 sumolib==1.28.0
```

These commands have not been executed. The Python installation is at user
level; adding missing operating-system libraries could require administrator
access. Check sumo and sumo-gui startup, imports and selected executable
paths before deciding which, if any, runtime packages to add. Record the
actual installed versions. Avoid silently combining the apt 1.18 executable
with 1.28 bindings or compiling inside an active Conda environment.

[Supported installation routes](https://sumo.dlr.de/docs/Installing/index.html)

**Connect the Windows display.** Start MobaXterm's X server and reconnect
to Ubuntu with X11 forwarding enabled in the SSH session settings. Check
DISPLAY in that new session; SSH should set it automatically. Launch
sumo-gui there. Check that the road and vehicles render, and that zoom,
pan and stepping work, rather than treating an empty window as a pass.
The server alone cannot establish this visual result for the user's PC.

**Finish with installation checks only.** With an existing stock SUMO
example, verify a short libsumo run, a TraCI-controlled GUI session and
one saved image. These are proposed environment checks, not a new VSL
scenario, traffic study, calibration or validation result. Stop after
reporting the version record and the user's visual confirmation; do not
continue into VSL implementation or policy experiments.

## Remaining gaps and fallback

There is no identified OS or Python incompatibility. Installation remains
unperformed, and the exact missing-runtime-library set is not yet known.
The main unverified requirement is usable remote GUI rendering, including
OpenGL and interaction speed over the user's connection. The existing
SSH configuration is encouraging but does not prove that complete path.

If X11 proves unreliable or too slow, retain the server libsumo installation
and assess an application-streaming/remote-desktop route separately. A
same-version Windows SUMO installation is another fallback for selected
visual runs using the same scenario and control settings. Those alternatives
need not be installed in the initial setup pass.

sumo-gui can save native snapshots for paper illustrations; vector output
depends on the build. Saving images from SUMO itself avoids dependence on
capturing a remote-desktop window. Screenshot capability is documented,
but has not been tested on this server.

[GUI snapshots and rendering](https://sumo.dlr.de/docs/sumo-gui.html#screenshots)

## Work and responsibility record

Inspection used /etc/os-release, uname, Python import discovery, apt-cache,
dpkg-query, ldconfig and the SSH configuration. The GPU check was repeated
with minimum escalation after the sandbox probe failed. Official SUMO,
PyPI and MobaXterm documentation supplied the capability/install evidence.
No package download/installation, display configuration change, traffic run
or repository implementation change was performed. The next possible task
is the bounded environment setup above; the VSL model decision remains open.
