# SUMO installation guide: offline-video revision and checks

**Later executed installation check, 2026-10-29.** The user reports a
shutdown hang. The helper now adds --quit-on-end, progress reporting and
a delayed stack diagnostic. One independent bounded off-screen lane-drop
check passed through MP4 decoding; the same Fontconfig warning appeared.
[Diagnosis, fix and retained evidence](sumo_gui_shutdown_troubleshooting.md).
The original guide-writing scope and static-only record are preserved below.

2026-10-29. The user clarifies that visual understanding can be served by a
downloaded video; live GUI forwarding is unnecessary if the revised route
is easier. Revise the guide and installation helper accordingly. This
authorizes documentation/helper changes, not installation, simulation,
rendering or encoding runs.

## Result and boundaries

The default becomes isolated SUMO/libsumo installation plus an occasional
TraCI sumo-gui pass under Xvfb/Mesa, PNG sequence export, external FFmpeg
encoding, MP4 metadata/full-decode checks and download to Windows. Live
GUI is optional and no longer an installation acceptance requirement.
The server still needs its off-screen rendering stack and encoder; this
does not imply that ordinary headless libsumo outputs native movies.

The dummy cases, inputs, control schedule, time step, seed and completion
criteria are unchanged. The checker adds --video and --video-fps, captures
one image request per completed step while traffic remains, records each
request and following flush step, and flushes the last request during the
normal completion step. It preserves source PNGs and rejects missing or
invalid frames. FFmpeg uses libx264/yuv420p, emits a 25-fps stream and
repeats pictures to implement the chosen input playback rate. No physical
interpolation or scientific-model smoothing is introduced.

The default input rate is 5 fps with one-second simulation steps: nominal
5x playback. Rate 1 gives nominal real-time playback. These rates and
duration are recorded. Automated file/decode checks remain distinct from
the user's assessment that the downloaded movie is meaningful.

## Sources actually reviewed

- [SUMO's built-in-video versus PNG-sequence options](https://sumo.dlr.de/docs/FAQ.html#building-videos-from-sumo-gui).
- [Deferred screenshot API](https://sumo.dlr.de/pydoc/traci/_gui.html).
- [SUMO GUI and window options](https://sumo.dlr.de/docs/sumo-gui.html).
- [Ubuntu 24.04 Xvfb](https://manpages.ubuntu.com/manpages/noble/man1/Xvfb.1.html).
- [Ubuntu xvfb-run display/authentication/lifecycle](https://manpages.ubuntu.com/manpages/noble/man1/xvfb-run.1.html).
- [Mesa software rendering](https://docs.mesa3d.org/envvars.html).
- [FFmpeg conversion/decode options](https://manpages.ubuntu.com/manpages/noble/man1/ffmpeg.1.html).
- [FFmpeg numbered sequences and input frame rate](https://manpages.ubuntu.com/manpages/noble/man1/ffmpeg-formats.1.html).
- [FFmpeg libx264 codec](https://manpages.ubuntu.com/manpages/noble/man1/ffmpeg-codecs.1.html).
- [ffprobe JSON properties and frame counts](https://manpages.ubuntu.com/manpages/noble/man1/ffprobe.1.html).

Direct FFmpeg website opens timed out. Ubuntu's primary package manpages
for the server's available FFmpeg 6.1.1 were read instead; unavailable
pages are not treated as inspected evidence. apt-cache/command discovery
confirm Xvfb and FFmpeg are not installed and that rendering packages are
available in the configured cache. No package transaction was executed.

## Files, preservation and verification

[Current guide](sumo_installation_guide.md)

[Current checker](sumo_installation_checks/run_check.py)

[Current static validation](sumo_installation_guide_validation.json)

[Earlier guide, helpers and validation, preserved together](sumo_installation_guide_versions/live_gui/sumo_installation_guide.md)

The existing guide/helper/source record and validation are archived byte
for byte, keeping their local links. Current README, index, assessment and
discussion records point to the video route. The requirements and case
creator remain unchanged. All scientific contracts, archived research,
feedback and both implementation repositories remain unchanged.

Static checks parse Python, exercise --help without importing SUMO, parse
the eight input XML documents, check Bash/embedded Python syntax, resolve
local links, and verify archive/preservation hashes. Rendering/encoding
command construction is checked from the helper AST, without pretending
that this supplies a runtime video result. The measured FFmpeg metadata,
decoding and manual Windows playback checks await installation.

Staged helpers are in /tmp/sumo_video_guide_20261029. Commands:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_video_guide_20261029/prepare_delivery.py
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_video_guide_20261029/validate_delivery.py --staged
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/sumo_video_guide_20261029/apply_delivery.py
git diff --check
```

The apply command requires escalation only to write the standalone review
repository outside the writable workspace. No dependencies, server/client
configuration or remote Git history are changed. This revision stops after
guide delivery; the next possible action is an authorized installation
check, with Windows movie inspection at the end. VSL model selection and
full Phase A remain deferred.
