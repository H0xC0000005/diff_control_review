# C-P review opened: first source/interface work and gate

Date: 2026-10-14. Scope: source-backed methodology review and analytical
interface checks. The user selected C-P, then explicitly directed opening
the next step. The review was opened and substantively begun; it did not
stop after a console-only plan.

The first source/interface pass is delivered at VSL-CP-G1 with Type 2 CP-D1:
effects-based point capacity versus causal continuous slow-entry/recovery
history. P-H is provisionally recommended and P-E remains a strong simpler
rival or explicitly selectable phenomenological primary. Neither is selected.
This is a service-law choice within closed S3-M2, not a new C-P/C-Z choice.
The complete terminal qualification and Step 3 are unfinished.

[Main findings and gate](vsl_cp_first_findings_and_gate.md)

[Opened plan and review order](vsl_cp_qualification_review_plan.md)

## Completed work and assumptions

Reused finalized handoff/reading-list context, S13/S12/H1/T1 evidence, frozen
traffic laws and current approval/feedback records. Inspected primary point-
merge acceleration and first-order capacity-drop sources, their native
inputs, mean versus transient meanings and exact source-version limits.

Formed the two-queue finite-terminal/coupled-point interface. Proved that
the conservative total-mass storage bound does not require zero A delay;
extended local TST accounting to A's eligible queue; stated a sufficient
positive-service clearance condition; and derived conditional A+E/G
initialization under known initial service state and a unique causal law.
These are interface deductions, not a selected or empirically admitted node.

Assumptions are retained H1 conservative arrivals/common ideal progress,
initially empty terminal, admissible mass-conserving departure histories,
fixed choke-line objective and known service initialization for the sufficiency
statement. No native insertion speed, priority share, numerical physical
parameter, service-memory kernel or smoothing rule is fixed. Source vehicle
events are not integerised primary traffic. The node must still prove its
own well-posedness/clearance and independent-reference fitness.

## Files changed

Created:

- `reporting/research_readiness/vsl_cp_qualification_review_plan.md`.
- `reporting/research_readiness/vsl_cp_first_findings_and_gate.md`.
- `extraction/research_readiness/vsl_cp_source_and_interface_audit.md`.
- `synthesis/research_readiness/vsl_cp_interface_foundations.tex` and `.pdf`.
- `reporting/research_readiness/vsl_cp_interface_foundations_build.log`.
- `reporting/research_readiness/vsl_cp_opening_work_report.md`.
- `reporting/research_readiness/vsl_cp_opening_validation.json`.

Updated the current progress, live candidate inventory, Step 3 plan/protocol,
source audit, accepted C-P continuation note, opening dialogue and package
entry notices. The exact H1/T1 source/PDF and other accepted mathematical
artifacts, production code/configs/dependencies, user feedback and existing
scientific results are untouched. Preexisting root AGENTS.md/PLANS.md/memo.txt
edits remain unchanged.

## Commands and artifact verification

Used read-only `cat`, `sed`, `rg`/`rg --files` and `git status --short`.
Primary-source `web__run` search/open/find supplied the recorded reading.
Direct conference publisher access and a 2016 figure screenshot failed;
primary conference text and repository manuscript text were available.
No claim depends on an unviewed figure or a downloaded full-paper archive.

Verified installed pdfTeX 1.40.25, TeX Live 2023/Debian. Built the new
supporting note using existing Computer Modern fonts. The first successful
compile exposed duplicate internal equation-link names; used unique
hyperlink names and rebuilt without those warnings. No equation changed
for that document correction and no package was installed.

From the review package:

```text
pdflatex --version
mkdir -p /tmp/vsl_cp_interface_build
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/vsl_cp_interface_build synthesis/research_readiness/vsl_cp_interface_foundations.tex
cp /tmp/vsl_cp_interface_build/vsl_cp_interface_foundations.pdf synthesis/research_readiness/vsl_cp_interface_foundations.pdf
cp /tmp/vsl_cp_interface_build/vsl_cp_interface_foundations.log reporting/research_readiness/vsl_cp_interface_foundations_build.log
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_cp_opening_checks.py
```

The scratch checks verify document targets/anchors/current statuses, accepted
artifact hashes and PDF structure/text/fonts/build warnings. They contain
no traffic solver, rollout, optimizer or numerical derivative. No raster
preview of the new PDF is claimed.

[Verification metadata](vsl_cp_opening_validation.json)

All checks passed: 24 Markdown files, 418 local links and 30 heading
anchors. Both accepted H1/T1 source/PDF hashes are unchanged. The new
three-page, 131256-byte PDF passed strict parsing/text checks, uses outline
Type 1 fonts and has no overflow or duplicate-link warning. These checks
do not establish a traffic law or useful gradient.

## Remaining gap and next allowed action

The source/interface pass is finished. CP-D1 is the new dependent
methodological choice; P-H is provisionally recommended, P-E is viable and
retained as a strong rival. No exact continuous finite-time service/recovery
law, applied MP6 regime or positive gradient result is admitted. The old
action certificate does not transfer automatically.

Stop at VSL-CP-G1 for the service-closure choice. After selection, qualify
the exact node/state and its dependent storage/conservation/clearance and
information/gradient/reference contracts. The complete C-P review and
Step 3 remain open. Step 4, implementation, installations, traffic experiments,
urban changes and the closed ramp line remain unopened.
