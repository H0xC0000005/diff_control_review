# Selected M2: first source, speed and activation qualification

Date: 2026-10-15. Method-first review only.

## Outcome and stopping point

Recorded the user's approval of M2 and closed CP-D2's direction choice.
Retained one aggregate service account with sufficient internal information;
M1 remains the exact conditional reference. Approval did not choose an exact
speed/recovery law, independent A penalty or ordinary-overload regime.

Executed the next bounded source and analytical pass. It establishes that
subcapacity flow does not identify speed without a traffic regime, and that
the inspected insertion-speed relations rely on congested-approach conditions.
For an explicitly defined speed-recovery-only completion, the inherited empty,
low-load task admits undisturbed passage. If that completion is uniquely
causal, it has travel-only complete TST and common fastest advice. This is
not a theorem about all M2 updates.

Also showed analytically that an amended ordinary-overload domain can retain
H1's free-flow preparation branch, per-lane sending and conservative terminal
storage protection. This does not qualify a full M2 or identify which lane
queues, actual insertion speed, extra capacity loss or an optimal policy.

**The opening source/speed/activation pass is complete at CP-M2-D1. The whole
M2 terminal-law review and Step 3 remain open.** The new physical choice is
F (qualify maneuver-origin slowing under the old load domain) versus D
(explicitly allow ordinary congestion to create slow discharge). D is
provisionally recommended for first source-based qualification if its domain
and independently justified ordinary ceiling are accepted. Neither route
is selected. This is a genuine G3 methodological stop, not a new roadmap
stage or a return to the already selected M2 architecture.

## Files saved and synchronized

New artifacts:

- [M2 selection and scope](vsl_m2_selection_and_scope.md).
- [Traffic findings, direct answers and F/D comparison](vsl_m2_first_restriction_findings_and_gate.md).
- [Speed/activation mathematical source](../../synthesis/research_readiness/vsl_m2_speed_and_activation_audit.tex)
  and [three-page PDF](../../synthesis/research_readiness/vsl_m2_speed_and_activation_audit.pdf).
- [Viewed-reference audit](../../extraction/research_readiness/vsl_m2_speed_activation_source_audit.md).
- [Final LaTeX build log](vsl_m2_speed_and_activation_build.log).
- This report and [verification metadata](vsl_m2_start_validation.json).

Updated current entries in `README.md`, `vsl_successor_00_opening_plan.md`,
the short methods outline, Step 3 protocol/plan, overall progress, candidate
inventory and C-P plan. Added subsequent-decision notices to the feedback-5
response and M1 findings; linked the new source audit from the prior reference
list. Archived selection, analytical findings, proposal/status and stop in
the dialogue. Earlier delivery records and validation metadata remain historical.

No accepted predecessor/M1 mathematical artifact, user feedback, root
instruction/roadmap or production source was edited. Preexisting Git-visible
AGENTS.md, PLANS.md and memo.txt changes are preserved. The package remains
saved on disk under its existing Git-ignored path.

## Assumptions and scientific limits

M2 selection approves the shared architecture and qualification direction,
not every feedback mechanism suggested in the discussion. A slow A queue
is not automatically another loss. No scalar Markov reduction, future-speed
oracle, spatial preparation/recovery model or wider objective is adopted.

The conditional undisturbed result explicitly assumes that unqueued free
passage creates no loss and there is no separate compulsory-maneuver burden.
Its unique-solution consequence is conditional on uniqueness of whichever
completion is proposed; no generic well-posedness theorem is inherited.
The compatible overload construction is an analytical nonempty domain, not
a calibrated parameter set or an instruction to lower capacity for a positive
result. M1's MP6, clearance and scalar-equivalence proofs remain specific to M1.

CP-D1/CP-D2 and S3-M1/S3-M2 remain closed. CP-M2-D1 is open under G3; D
would explicitly reopen only no-ordinary-overload, while F needs a new entry
mechanism. G2 and G4 remain fixed. The next allowed action is the physical
activation/domain decision, followed only by its authorised bounded law
qualification. Step 4, implementation and experiments are unopened.

## Commands and checks

Used read-only `cat`, `sed`, `rg`, `git status --short`, Python standard-library
hashing and primary-source web open/find. Read the finalized handoff/current
authority chain and current feedback. Rechecked the actual 2011 conference
text and selected 2016/LTM passages, with limits in the reference list; did
not probe SUMO or other simulator binaries.

Edited documents through `apply_patch` and a bounded Python replacement of
the live candidate section. A documentary exact-context patch was rejected
without changing files, then corrected. No scientific fallback was introduced.

Verified pdfTeX 1.40.25, TeX Live 2023/Debian with `pdflatex --version`.
Built from `synthesis/research_readiness/`, using the installed fonts/packages:

```text
mkdir -p /tmp/vsl_m2_start_build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/vsl_m2_start_build vsl_m2_speed_and_activation_audit.tex
```

Two successful passes resolved the usual first-pass outline warning. Copied
the final PDF and `.log` using standard-library `shutil.copy2`, retaining the
`.tex` beside the PDF. No package installation was needed.

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_m2_start_checks.py
```

Checks cover current links/anchors and decision status, protected-file hashes,
strict PDF parse/text/fonts, clean final build, and exact symbolic FD/speed/
travel identities. Counts and hashes are in the metadata. These are artifact
and algebra checks, not mechanical proofs of the conditional trajectory or
traffic validation. No raster visual inspection is claimed.

No traffic integration, numerical gradient/AD/FD experiment, fitting,
optimisation, simulator code or environment modification was performed.
