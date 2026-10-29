# Feedback 8: unified model reporting and verification

Date: 2026-10-16. **Reporting complete; scientific status unchanged.**
The active checkpoint remains MP6-Q1. Applied MP6 and Step 3 remain open;
Step 4 is unopened. This is a recap of the functionally complete conditional
model, not another model or protocol review.

## Delivered result

The user requested the original S13 backbone, an explicit old-to-new
component map, the new formulations with brief mathematics, and a separate
full mathematical report. The delivery is:

- **Ten-page model recap:** traffic meaning and causal chain first; the
  original nine-component map; modified versus added responsibilities;
  selected formulas; compact initialization and accounting; what the current
  forward result establishes and what remains unqualified. The added page 9
  briefly introduces six previously identified literature rivals.
- **Eighteen-page mathematical report:** historical S13 calculation and
  certificate, current domain/units, H1 preparation, footprint/handoff,
  physical terminal, work-root/priority laws, recovery derivation and renewal,
  local causal construction, positive service, whole-domain event/clearance
  proof, mass/TST, information and sensitivity limits, the complete analytical
  A-delay/active-renewal family, physical-identification deductions and a
  source/proof map. It consolidates existing results, not unreviewed future
  gradient evidence.

[Framework and component recap, PDF](../../synthesis/research_readiness/vsl_feedback8_model_stack_recap.pdf)

[Complete mathematical report, PDF](../../synthesis/research_readiness/vsl_feedback8_full_mathematics.pdf)

[Equation, decision and reused-reference map](../../extraction/research_readiness/vsl_feedback8_model_stack_source_map.md)

## Assumptions and scientific boundaries

Retain the currently selected H1/T1/S-E-P/W-F/R-E/O-R law, original constant
advice interval and sufficient domain, known empty terminal/history, finite
cohort, continuing symmetry, continuous mass, fixed cutoff and choke-line
complete local TST. The reports clarify notation for the shared budget and
recovery reading; they do not change formulas, source attribution, parameter
meaning, initial information or objective endpoint.

S13 remains valid and closed under its original assumptions. Its action split
and gradient-direction certificate are explicitly historical and not inherited
by the current stack. Prior alternative laws are retained as diagnostics or
rivals, not mixed into the primary. The complete A-delay witness retains its
possibly extreme scales and uncalibrated interpretation. E non-requeueing
requires the monotone H1 pulse and other selected conditions, not merely a
finite cohort. Actual crossing speeds, joint parameter validity, useful
actions/gradients and independent SUMO performance remain unestablished.

No new external paper was viewed. Literature roles and source limits are
reused from the existing primary-source audits. Neither a citation nor a
symbolic identity establishes empirical validity of the joined law.

## Files changed

Twelve new artifacts:

- `synthesis/research_readiness/vsl_feedback8_model_stack_recap.tex`
- `synthesis/research_readiness/vsl_feedback8_model_stack_recap.pdf`
- `synthesis/research_readiness/vsl_feedback8_full_mathematics.tex`
- `synthesis/research_readiness/vsl_feedback8_full_mathematics.pdf`
- `synthesis/research_readiness/vsl_feedback8_math_core.tex`
- `synthesis/research_readiness/vsl_feedback8_math_forward.tex`
- `synthesis/research_readiness/vsl_feedback8_math_support.tex`
- `extraction/research_readiness/vsl_feedback8_model_stack_source_map.md`
- `reporting/research_readiness/vsl_feedback8_recap_build.log`
- `reporting/research_readiness/vsl_feedback8_mathematics_build.log`
- `reporting/research_readiness/vsl_feedback8_reporting_work_report.md`
- `reporting/research_readiness/vsl_feedback8_reporting_validation.json`

Seven existing review records linked/synchronized: README, successor opening
plan, progress, Step 3 review plan, dialogue, living candidate inventory and
methods outline. Prior bodies retain their delivery-time scope; the PDFs
provide the unified current reading. No open choice or gate status changes.

The only user-feedback change is `### 8` → `### 8 (answered)` in
`temp_content/feedback/vsl_refinement_feedback.md`, as permitted by that file.
Its entire remaining content is preserved. The fresh snapshot protects
376 other root/feedback/closed-task/prior-review artifacts. The package is
Git-ignored; pre-existing root edits in `AGENTS.md`, `PLANS.md` and `memo.txt`
remain unchanged. No production source/test/config/environment was edited.

## Commands and verification

Read-only inspection used `rg --files --no-ignore`, `rg -n`, `cat`, `sed`,
`tail`, `git status --short`, `command -v` and `kpsewhich`. Read repository
context, handoff/current review and feedback records; then the original S13
contract/certificate, H1/T1, S-E, S-E-P, O-R, J4/W-F, WF-Q1 and MP6-Q1
mathematical/source artifacts. No implementation milestone was opened.

Fresh preimages and preservation hashes:
`/tmp/vsl_feedback8_before.json`.

Installed `/usr/bin/pdflatex` was verified. Existing mathematical/layout
packages suffice. TikZ and external raster renderers were unavailable;
the recap's simple chain uses native LaTeX boxes/arrows. No installation
or renderer substitution affecting content was needed. PDF text, page
coverage, links, font resources and logs are checked; raster visual
inspection is not claimed.

Build commands:

```text
python3 /tmp/vsl_feedback8_build.py vsl_feedback8_model_stack_recap
python3 /tmp/vsl_feedback8_build.py vsl_feedback8_full_mathematics
```

Each invokes `pdflatex -interaction=nonstopmode -halt-on-error
-file-line-error` three times in its own directory under
`/tmp/vsl_feedback8_latex`, then copies the PDF and final log. The first
build exposed three long displayed equations and one loose paragraph.
Reflowed the equations and paragraph without changing the mathematics;
limited contents depth to main sections to keep it on one page. Both final
build logs are clean, with no underfull/overfull or reference/rerun warnings.
The mathematical report's retained main TeX includes the three adjacent
body sources; it is not a concatenation of stale historical reports.

Exact algebra/transcription checks:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_feedback8_algebra.py
```

Twenty-nine symbolic identities and eighteen rational static checks pass.
They cover S13's reference objective/derivatives, H1 branches and conservation,
FD inverse/root derivatives, W-F anchor and direct-advice exclusion, recovery
derivatives/area, complete travel accounting, identification identities and
the coupled-delay witness's exact static values/inequalities. These are not
traffic integration or numerical gradient checks and do not mechanically
certify the quantified forward/witness proofs or physical validity.

Record synchronization and permitted feedback annotation:

```text
python3 /tmp/vsl_feedback8_sync.py
```

Final document/PDF/source/status/preservation verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_feedback8_checks.py
```

Quantitative checks and artifact hashes are stored in the linked validation
JSON. **Final checks passed:** nine Markdown records, 524 local Markdown
links and 29 heading targets; five TeX sources, 94 unique mathematical labels
and 51 resolved formula/section references; 15 local PDF links and 66 internal
PDF destinations. Both PDFs use Type 1 fonts and clean build logs. All 376
protected hashes match; the feedback change is exactly its permitted suffix.
Twenty-nine symbolic identities and eighteen static checks pass. These
results verify the reporting and supporting algebra, not physical validity
or the quantified proofs mechanically.

No failed scientific criterion is weakened. No traffic/ODE rollout,
calibration, numerical derivative, optimization, SUMO run, simulator code,
dependency change or detached process occurred.

## Current status and next allowed action

Feedback 8 is answered and this reporting task stops. Review the two PDFs
before resuming the remaining information/action/full-objective gradient and
updated SUMO evidence contracts when directed. No remaining review block
was advanced by producing these reports. MP6-Q1 remains the active checkpoint;
applied MP6 and Step 3 remain open, Step 4 and implementation/experiments
unopened. S13, urban and ramp closures are unchanged.

[Machine-readable verification](vsl_feedback8_reporting_validation.json)

## Requested addition: brief literature rivals

The user asks to add a brief section on the literature baseline/rival models.
Added it to the model-stack recap, now ten pages, at page 9. It introduces
Wei–Han–Wang's aggregate history/capacity-drop model, Jin–Jin's compact
lane-drop control, Hegyi's METANET predictive control, Carey's lane-aware
receiving CTM, Nagalur Subraveti's density-driven mandatory merging and
Delle Monache's LWR speed-control gradients. Each has a brief traffic
interpretation, comparison role and source link. The section distinguishes
published-model rivals from our information and optimizer controls.

This reuses the archived baseline screen; no new paper or model is adopted.
The eighteen-page mathematical PDF and its sources are unchanged. MP6-Q1
and all scientific/review statuses remain unchanged. No experiments or
implementation are opened. Next allowed action is reading the amended recap.

Fresh preservation snapshot: `/tmp/vsl_feedback8_rivals_before.json`.
Rebuilt only the recap with the existing build command. Checked the new
page, references, PDF text/fonts/log and preserved mathematical artifacts.
No mathematical equations changed, so the prior algebra checks were retained
without rerunning them. Synchronized the source map, current page count and
dialogue. The verification JSON records this addition and checks all 388
artifacts protected by the fresh snapshot, alongside the original checks.

The addition passes the PDF/build, 528 local Markdown-link, 30 heading-target
and 388 fresh preservation checks. The mathematical PDF remains byte-for-byte
unchanged. No scientific gate or benchmark adoption changes.

## Requested refinement: illustrate the current backbone

Replaced the first page's textual current chain with boxed stages and
arrows. S13 and the current stack now appear side by side, showing the
input, preparation, timing, service and complete-time chain. The current
point-merge box explicitly shows E admissions updating recovery and the
recovery account returning available budget to service. A/E labels are
explained beneath the figure. Progress-based preparation is retained;
the diagram does not reinstate S13's elapsed-time completion law.

Updated the recap TeX/PDF/build log, this report, dialogue and verification
record only. The recap stays ten pages; the literature section remains on
page 9. The mathematical report, model equations and scientific status are
unchanged. User quick-reference discussion mode remains active; no pending
review block is opened.

Snapshot: `/tmp/vsl_feedback8_backbone_before.json`, protecting 390 other
artifacts. Rebuilt using `python3 /tmp/vsl_feedback8_build.py
vsl_feedback8_model_stack_recap`, then ran the existing document/PDF checks
with an additional layout-content and preservation check. Native LaTeX boxes
and arrows require no new package. Both chains and the status text fit on
page 1, with a clean build log. Checked extracted layout and page continuity;
raster visual inspection is not claimed. No equations changed and no algebra
or traffic experiments were rerun. Next allowed action is reading the revised
figure during the ongoing quick-reference discussion.
