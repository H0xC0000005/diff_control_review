# S05.90 — Analytical construction work report

Sprint: [S05](../../00_review_sequence.md#s05) · Role: 90 work / verification · Predecessor: S04 / approved Candidate A · Gate: DG-AC1.

Date: 2026-09-17. Status: authorized Candidate A executed to planned finding
stop; DG-AC1 / DG-R2 pending user review. Preceding DG-MUG1 remains closed.

## Files changed

New: synthesis/s05/rb_certificate_analysis.tex and generated PDF;
extraction/rb_certificate_source_audit.md; reporting/s05/s05_20_rb_certificate_findings_and_gate.md
and this report; search/rb_certificate_query_log.csv and rb_certificate_access_log.csv.
Updated current continuation/status in README, s04_99_rb_diagnostic_methodology_closure.md
and s04_80_rb_diagnostic_phase_A_dialogue.md. Synchronized the living inventory with DG-R2;
earlier scientific alternatives are preserved. No old source/extraction/search/
archive evidence, code/tests/config, feedback or urban milestone/roadmap edited.
Existing tracked AGENTS.md/PLANS.md edits remain the user's unchanged work.

## Assumptions and findings

Free-flow derivation: equal lane speeds, admissible conservative transfer,
adequate receiving and a bounded transfer-rate condition for the short contrast.
Its early continuous-mass witness is not native last400m evidence. Past lane
inputs are explicitly unknown, not asserted identical full forcing.
Queue derivation: advice-independent work-conserving service, finite completion,
all-cohort accounting and cumulative-arrival dominance. None is automatically
applied to native following/merging. Sources ground conditional classes, not an
adopted or repaired whole model. No categorical shifts, smoothing, discontinuous
capacity law or Gap7 exception. Root certificate remains unproved; missing
service/information link is explicit. Proposed held100/cap504 is unapproved.

## Commands and provenance

Read-only rg, sed, git status; archived-PDF extraction using existing
/home/zpz/miniconda3/envs/differential_sim/bin/python with pypdf; three exact
browser queries and two primary direct retrievals documented in new logs.
Default python lacked pypdf and pdftotext was absent from PATH; used the already
known interpreter without installation/environment change. These were document-
reading limitations, not SUMO/server checks or paper requests.
Verified command -v latexmk/pdflatex resolves /usr/bin tools. All edits use apply_patch.
One multi-file status patch failed its exact-line context check; no partial
edits applied. Corrected the patch context without changing scientific content.

PDF build from repository root:

`latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rb_certificate_latex_<unique> misc/differentiable_freeway_bottleneck_task_review/synthesis/s05/rb_certificate_analysis.tex`

Actual command used `/tmp/rb_certificate_latex_TOmp7D` as the output directory.
After confirming the destination did not exist, placed the generated PDF with
`cp -n /tmp/rb_certificate_latex_TOmp7D/rb_certificate_analysis.pdf misc/differentiable_freeway_bottleneck_task_review/synthesis/s05/rb_certificate_analysis.pdf`.
The initial successful build had two small text overfull warnings; rephrased
those lines and rebuilt. Final build has no warnings/undefined references or
overfull boxes. Retain PDF/.tex in synthesis/; auxiliaries remain temporary.
Artifact rendering is not a traffic experiment.

## Validation

PASS: LaTeX compilation, four readable/text-extractable pages, 176046 bytes;
SHA256 c42bf273f8168aa2ee1aac108f2ff5d0b7abd80e0997f2889d93f8ea92439127.
Checked extracted headings/text and every page has substantive text; no final
LaTeX warnings. No separate rasterized visual inspection is claimed.

PASS: 56 package Markdown documents /161 local links, no broken targets;
11 unique inventory IDs. New query/access logs each contain three valid CSV
records. Budget arithmetic checked: 2×2×10×(2+4)=240, total24+48+192+240=504.
That is proposed arithmetic, not an approved increase or measured run count.

PASS: all169 protected-file hashes unchanged and all17 archive entries match
the unchanged manifest. git status still shows only the user's pre-existing
AGENTS.md/PLANS.md changes. No experiments/rb_diagnostic implementation directory
and no misplaced temp_content review directory exist. Review artifacts remain
inside the original misc package.

Code/traffic/numerical-gradient tests do not apply. Conditional proofs are
analytically inspected, not experimentally validated. No traffic scores,
matching residuals or robust-positive label exist. Unresolved risks: transfer
admissibility, consequential history collision, actual advice/merge coupling,
action-menu completeness, native/field transfer, minimum state and gradients.

## Next allowed action

Read findings and choose/adjust DG-R2. Reference experiments require explicit
implementation/run authorization and any G3/G4 amendment approval. Analytical
continuation requires an explicit model contract before using new dynamics.
No next work follows automatically.
