# SUMO video check: off-screen GUI shutdown wait

2026-10-29. Installation troubleshooting only; no VSL model is changed.

The reported run was waiting after traffic and rendering had completed.
The server held 93 native frames and 12 complete trip elements, with final
arrival at 93 s. The trip XML footer was still missing and the encoder
had not started. This was a partial installation result, not a passed run.

Read-only host process inspection found the checker sleeping in a child
process wait, its SUMO launcher also waiting, and the native GUI waiting
for events. The installed TraCI 1.28 close implementation calls the child
process's wait by default. The helper supplied --start but omitted
--quit-on-end. Its off-screen window could therefore remain open, while
Python waited before reaching encoding. Low CPU usage was consistent with
that wait, not evidence that rendering never occurred.

The correction adds --quit-on-end to GUI launches, keeps waiting shutdown
for complete output flushing, and adds stdout/progress.json stages plus
a one-time Python stack dump after 30 seconds. Section 6 is self-contained,
uses the actual environment name sumo and has an external wall-clock bound.
The encoder filter uses grep, removing the accidental ripgrep dependency.
These changes affect installation control/diagnostics only; the traffic
inputs, 1 s updates, seed, speed commands and completion checks are unchanged.

[Official GUI option](https://sumo.dlr.de/docs/sumo-gui.html)

[TraCI close documentation](https://sumo.dlr.de/docs/TraCI/Interfacing_TraCI_from_Python.html)

[Maintainer guidance for GUI output/shutdown](https://github.com/eclipse-sumo/sumo/issues/16407)

## Independent bounded verification

A separate copy of the existing dummy inputs was placed under
/tmp/sumo_shutdown_fix_20261029/workspace. The corrected helper ran with
the installed sumo environment under a 60-second outer bound. It completed
normally, without reaching that bound. The user's original live run was
not stopped, signalled, restarted or overwritten.

| Observed check | Result |
|---|---|
| SUMO / Python | 1.28.0 / Python 3.12.14 |
| Traffic | 12 departed and 12 arrived; no teleports |
| Progress | GUI closed normally; simulation completed at 94 s in 94 steps |
| Control | Initial motion, low-cap readback/slowing and restored-cap acceleration all observed |
| Images | 93 flushed 1280×720 source frames |
| MP4 | H.264/yuv420p; 25 fps; 465 encoded frames; 18.6 s at nominal 5× playback |
| Decode | Full decoding passed |
| Warning | The same Fontconfig reset-dirs warning appeared; it did not block this run |

The checker was created at 10:46:01.588 UTC and recorded passed at
10:46:10.467 UTC (about 8.9 s wall time). This is one installation example,
not a traffic-model performance result. Native frames were inspected on
the server; Windows playback still needs the user's confirmation.

[Verification movie](sumo_installation_verification/gui_shutdown_20261029/scenario.mp4)

[Representative image](sumo_installation_verification/gui_shutdown_20261029/view.png)

[Recorded check result](sumo_installation_verification/gui_shutdown_20261029/result.json)

[Video properties](sumo_installation_verification/gui_shutdown_20261029/ffprobe.json)

## What to do with the earlier run

It has the old code loaded. Stop that installation test with Ctrl+C in
its original terminal. Its old cleanup path may wait again; a second
Ctrl+C can interrupt that wait. Keep its partial folder as diagnostic
evidence, rather than counting it as a passed check. Do not reinstall
packages or change system fonts to address this shutdown defect.

Then follow the corrected Section 6 in the SUMO shell. The new helper
prints its output directory and stage transitions. Any new issue can be
located with progress.json, the stage messages and the delayed stack dump.
The external timeout bounds only the new check, leaving unrelated runs alone.

[Updated guide](sumo_installation_guide.md)

## Evidence and file record

The inspected original run was
lane_drop-traci-video-20261029T102319Z-ef9ef0b3. Host inspection was read-only;
the sandbox's PID namespace did not show that run, so minimum escalation
was used before drawing process-state conclusions. No strace attachment,
package installation or system-configuration repair was performed.

The copied verification input hashes equal the original workspace's
case manifest. Runtime evidence below is copied unchanged from the new
temporary run; full source PNGs remain in that run folder. The verified
helper SHA-256 is `792febf8d3c5dd259f5c139ddefb917f69cd37c5e3b36e107e76343a0565cfb2`.

The diagnosis and the new installation check were authorized by the user's
request to locate this failure. They open no research experiment or
simulator development. All review-model records, source feedback and both
implementation repositories remain unchanged. Stop at this delivered fix;
the user can inspect/retry the installation example and download the movie.

Exact bounded verification command (temporary copied inputs and helper):

```bash
/usr/bin/env LIBGL_ALWAYS_SOFTWARE=true PATH=/home/zpz/miniconda3/envs/sumo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin /usr/bin/timeout --signal=INT --kill-after=5s 60s /usr/bin/xvfb-run -a -s "-screen 0 1600x1000x24 +extension GLX" /home/zpz/miniconda3/envs/sumo/bin/python -u /tmp/sumo_shutdown_fix_20261029/run_check.py --workspace /tmp/sumo_shutdown_fix_20261029/workspace --case lane_drop --backend traci --video --video-fps 5
```
