# VSL successor opening — documentary work report

Date: 2026-10-12. Status: **Opening proposal complete; stopped for user review.**
Detailed methodological qualification and implementation are not opened.

## Files changed

Created the root opening plan; short methods outline; inherited-kernel LaTeX/PDF;
preliminary baseline/evidence-gap screen; dialogue; this work report; and the
document-validation JSON. Added a current opening notice and links to README.
No existing source, accepted equation, feedback entry, result or production file
was edited. AGENTS.md and PLANS.md were already modified when this task began;
their contents are preserved by this task.

[Opening plan](../../vsl_successor_00_opening_plan.md)

[Methods outline](../../synthesis/research_readiness/vsl_successor_methods_outline.md)

[Kernel note PDF](../../synthesis/research_readiness/vsl_successor_kernel_note.pdf)

[Editable LaTeX](../../synthesis/research_readiness/vsl_successor_kernel_note.tex)

[Baseline screen](../../extraction/research_readiness/vsl_successor_baselines_and_evidence_gaps.md)

[Dialogue](vsl_successor_opening_dialogue.md)

[Validation record](vsl_successor_opening_validation.json)

## Inspection and assumptions

Followed the finalized handoff reading list and linked authorities. Inspected
the repository's objective/gradient sources, objective tests, diagnostic config
and approved environment records only to respect repository inspection rules;
their interfaces and numerical defaults did not constrain the proposed task.
No test runner or simulator was invoked. No applicable VSL implementation plan
exists: this review is separate from project milestones, and S13's M2 denotes a
mechanism member rather than project Milestone 2.

Primary online checks revisited Wei–Han–Wang, Carey, Hegyi and the Delle Monache
abstract. Other paper-level statements reuse accepted local extraction rather
than claiming a new whole-paper audit. No broad successor search, author contact,
external messaging or literature-wide absence/novelty conclusion occurred.

Assumed the accepted elementary direction uses the S13 finite cohort and ideal
longitudinal response as its conditional starting kernel. Retained transfer and
batch/service laws as adaptations requiring later qualification. SI units and
initial-statistic terminology are transcription clarifications only. No law,
scientific acceptance threshold, calibration value or evaluator was newly adopted.

## Commands and document verification

Read-only inspection used `cat`, `sed`, `rg`, `rg --files`, `ls` and
`git status --short`; primary URLs were inspected with the web tool. A Python
standard-library SHA-256 snapshot recorded 937 existing files across the three
review packages, production source/tests/configs/scripts, approved plans,
reports and feedback plus the three root authority files:
`/tmp/vsl_successor_opening_20261012_preservation_snapshot.json`.

Verified `pdflatex --version`: pdfTeX 1.40.25, TeX Live 2023/Debian.
No dependency installation. Existing `pypdf` in
`/home/zpz/miniconda3/envs/differential_sim` supplies document text/page checks;
that environment is used only for PDF inspection, not traffic execution.

Build the note twice from the repository root, keeping compiler byproducts and
logs in a new task-specific temporary directory and retaining only the PDF beside
its source:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/vsl_successor_opening_20261012_latex misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_successor_kernel_note.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=/tmp/vsl_successor_opening_20261012_latex misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_successor_kernel_note.tex
```

Document checks cover successful compilation, PDF page/text integrity, LaTeX
layout/reference warnings, resolution of added local links, expected artifact
presence and preservation of existing material. The machine-readable validation
record stores actual outcomes and hashes. These are documentary checks; no
traffic, calibration, finite-difference, AD or optimizer test was run. Compilation
does not validate the traffic methodology.

All checks passed: the final PDF has three substantive pages, no LaTeX
layout/reference warnings and readable extracted text on every page. All 76
local links across the five new Markdown documents and README resolve.
SHA-256 comparison preserves 936 of the 937 snapshotted existing files exactly;
the sole intentional existing-file change is README navigation. Eight new
task artifacts are present. Closed S13/urban/ramp evidence, user feedback,
production files and the preexisting AGENTS.md/PLANS.md changes are unchanged.

The first two PDF builds exposed a nearly empty page containing a carried-over
paragraph. Condensed introductory prose and adjusted spacing without changing
equations, then rebuilt twice with the commands above and repeated the page/text
checks. No raster visual inspection was performed; PDF integrity, extracted
content and compiler layout diagnostics were checked. `misc/` is already ignored
by Git, so these review artifacts are saved locally and are not staged. That
existing repository policy was left unchanged.

## Risks, phase and next allowed action

Remaining scientific burdens: transfer-law validity, priority-sensitive mean
time, advice/realized-speed mapping, conditional exact-history reachability,
initial scalar observability, parameter prevalence, independent evaluation and
precise novelty. The present derivative is inherited analytical evidence only.
No empirical or implementation gradient-usefulness result is claimed.

Ramp review remains closed. S13 and urban Part I remain closed with unchanged
claims. The VSL successor is at its opening-proposal checkpoint; the next allowed
action is user review followed by an explicitly authorized bounded detailed
claim/source-qualification pass. No production milestone has been opened.
