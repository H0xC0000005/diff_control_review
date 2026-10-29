# B2-A compact-closure qualification: work record

Date: 2026-10-13. Status: **Method-only review executed to VSL-B2A-G1;
no receiver or motion model adopted.**

## Scope and result

The user selected B2-A as the first route and instructed continuation of the
review sprint. Examined the strongest compact traffic meaning rather than
assuming the one-stock reduction works: an adjacent receiver stock coupled to
own-lane-first service, physically available donor requests, outflow and
complete-time accounting on fixed geometry under one common VSL.

The stock resolves the earlier current-receiving ambiguity, but does not by
itself predict travel/arrival timing. A primary variable-speed CTM paper gives
a concrete free-flow counterexample to the naive fractional-stock outflow.
The hand case at half a region per tick verifies finite physical clearance
against a geometric release tail. The LTM boundary-count paper shows a
compact motion precedent but does not close distributed interior lateral
transfer. The methodological gate therefore compares compact upstream
travel history with a short spatial upstream region for the preparation
stage. A point-only replacement of every upstream early attempt is retained
as a simpler rival; point service at the later compulsory lane end is a
shared boundary, not a substitute for early preparation. The review stopped
there, before adding state or revising the task.

[Decision-facing finding and gate](vsl_b2a_compact_closure_findings_and_gate.md)

[Primary-source locations, complete viewed-paper list and limits](../../extraction/research_readiness/vsl_b2a_compact_closure_source_audit.md)

## Files, commands and verification

Added this work record, the decision-facing B2-A report and its source audit.
Updated current README navigation, the living candidate record, the MP
question inventory and the phase dialogue. Earlier B2/S13 reports,
mathematical notes, user feedback, project context and production files
were not changed. Existing unrelated repository edits remain untouched.

Commands/tools: `rg`, `cat`, `sed`, `git status --short`, primary-web
`search_query`/`open`/`find`, `apply_patch`, and standard-library Python
with exact `fractions.Fraction` and document preservation/link checks.
No dependency installation, traffic rollout, calibration, optimization,
simulator development or scientific gradient test was performed.

The exact arithmetic check yielded physical exits of one-half and
one-half in the first two ticks, versus one-half and one-quarter under
repeated current-stock release; physical remaining mass was zero
after two ticks versus one-quarter under the naive rule. This checks a
reference deduction, not a simulated traffic experiment. Document
verification covers the changed review artifacts and protected files;
its final checks passed: 213 protected review files are unchanged,
142 local links and heading anchors resolve, the phase dialogue is
append-only, the earlier B2 gate is byte-identical, and the exact
half-speed reference calculation agrees with the stated table.

## Assumptions, risks and next action

The half-speed check assumes an initially uniform free-flow mass and
fixed speed during the two-tick example. It does not assert a calibrated
VSL response, a congested correction, or that every compact state fails.
The sources do not jointly establish a compact-history task with
distributed upstream R1 merging. B remains a possible return route for
consequential spatial failure, while common-speed physics and compulsory
lane-end service remain shared problems for either route.

Current review phase: **VSL-B2A-G1**, a Type 2 choice over compact upstream
travel-history state or a small spatial upstream merging region. The
point-only upstream replacement is a simpler rival outside the accepted
task; a point law at the terminal choke belongs to component 6 and does
not resolve this gate. G1/G2/G3/G4 consequences are exposed in the gate
report. The next allowed action is the user's disposition of the corrected
upstream gate. No dependent qualification starts automatically.

## Two-stage scope correction — 2026-10-13

The initial gate wording conflated a point-only replacement of the entire
preparation process with point treatment of the *later* forced merge. The
user identified this ambiguity. The former would lose distributed early
preparation; the latter retains it and leaves component 4's upstream
motion and receiving gap open. The half-speed counterexample concerns
movement in the finite upstream area, not the permanent lane-end service.
The decision-facing report, living candidates, MP inventory, source audit,
README, B2 gate addendum and dialogue were clarified accordingly. This is
a correction of the review's scope description, not adoption of a new
motion law, receiver representation or lane-end service law.
The correction used `rg`, `sed`, `git status --short` and `apply_patch`;
a standard-library Python link check found all 146 local targets across
the eight synchronized review files. No traffic experiment or scientific
test was run for this prose correction.
