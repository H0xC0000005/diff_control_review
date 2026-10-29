# Literature comparison report: first-draft work record

**Historical v1 record.** The user subsequently expands the backbone and
removes standalone Section 4 within a 2.5-page budget. The first-draft PDF
and source below are archived byte for byte; the original build log and
verification describe that version. Their recorded original artifact paths
precede the archive. Current work is in the
[revision record](vsl_literature_backbone_review_revision_work_report.md).

2026-10-21. **Option 2 user-selected; requested first draft delivered.**
The analytical review remains complete. This is a presentation pass; the
draft and JM1 findings are not marked accepted by the user.

The user selects a comparison-led report because the literature should be
the foundation of its answer. Draft four sections: requirements; closest
published models; the selected completed model; recommendation and evidence
limits. Keep the main body at two pages, with references excluded. Use the
accepted VSL report's plain causal explanations, explicit assumptions and
nearby source credit. The result is two pages of main text plus one page
of eight IEEE references, with 10 pt main text and 18 mm margins.

## Artifacts and changes

- [First draft PDF](../../synthesis/research_readiness/vsl_literature_report_versions/v1/vsl_literature_backbone_review_report.pdf).
- [Archived LaTeX source](../../synthesis/research_readiness/vsl_literature_report_versions/v1/vsl_literature_backbone_review_report.tex).
- [Final LaTeX build log](vsl_literature_backbone_review_draft_build.log).
- [Document verification](vsl_literature_backbone_review_draft_validation.json).
- This work record.

Update the package README with the draft link; append the user's choice
and delivery to the successor dialogue; update the temporary
[structure discussion](../../../../context_snapshots/diff_minimal_meso/temp_content/vsl_review_report/report_structure_candidates.md)
with option 2 selected and the report available. Preserve the original
candidate reasoning as proposal-time discussion. No model, source audit,
proof, numerical contract, accepted report or prior finding is edited.

## Coverage and source ownership

| Report part | Existing authority reused | What is stated and qualified |
|---|---|---|
| Requirements and literature comparison | [Backbone comparison](vsl_published_backbone_findings.md), [reading/reference record](../../extraction/research_readiness/vsl_published_backbone_sources.md), feedback 13–14 | Jin–Jin is simpler for a spatial-information task; Wei is a serious history-aware aggregate model; Subraveti preserves the lane question; Carey supports conservative allocation. This is a bounded inspection, not global best-model selection. |
| Selected model and assumptions | [Joined model](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf), [assumptions](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md), [source/interface audit](../../extraction/research_readiness/vsl_methodology_review_source_and_interface_audit.md) | Retain lane-density preferences and select complete Han budgets/VSL cap. Identify the normalization/sharing/fallback/diagonal composition as ours, crediting Carey/Wright principles. Declare the closed cohort, common FD, free outlets, old-state movement and unit-headway assumptions. Source calibration and wave/max-throughput guarantees do not transfer. |
| Findings and recommendation | [JM1 findings](vsl_methodology_review_findings_and_gate.md), [analytical addendum](../../synthesis/research_readiness/vsl_methodology_review_analytical_addendum.pdf) | State complete residual/sensitivity results as review deductions. Preserve switching qualifications, actual service-information loss, the sufficient one-scalar observer, free-regime zero action value, and unproved positive control/gradient value. |

All eight cited works were already in the qualified review records. No
new primary paper is represented as newly read in this writing pass; no
new web search or download was needed. References are numbered by first
appearance. Preserve the archived Jin manuscript dates and the Subraveti
2019/2020 metadata discrepancy rather than inventing a reconciled version.

## Commands and verification

Inspect current reports, source/assumption audits, discussion and status with
`rg`, `cat`, `sed`, `tail` and `git status --short`. Verify installed tools
with `command -v`, Python `shutil.which`, `pdflatex --version` and
`kpsewhich`. Edit documents with `apply_patch`. No dependency installation
or environment modification is performed.

Build with the installed pdfTeX, and run two passes after the final source
edit to settle the references:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_literature_report_draft1/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the PDF beside its `.tex` and the final log to the reporting folder.
Use installed pypdf to extract and read all pages, check that sections 1–2
are on page 1 and sections 3–4 on page 2, and verify that references occupy
page 3. Check font sizes, embedded fonts, the local companion link,
citation/bibliography order and absence of unresolved references or
overfull/underfull boxes. No raster page rendering is claimed: this
environment has no available PDF rasterizer. Page/text/font/build checks
are document checks, not mathematical proofs or traffic validation.

Record a before-edit snapshot at
`/tmp/vsl_literature_report_draft1/before.json` covering 569 existing files.
After all edits, run:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_literature_report_draft1/document_checks.py
git status --short
```

The document checks pass: two main-text pages plus one reference page,
eight matched citations/references, minimum 10 pt declared text, no final
build warnings or overflow messages, resolved local links, preserved prior
dialogue, and unchanged hashes outside the three allowed navigation/
discussion edits. All newly created files are report artifacts. The three
pre-existing tracked changes in AGENTS.md, PLANS.md and memo.txt remain
untouched. Exact hashes, counts and tool versions are in the verification
JSON; extracted text is retained in the temporary build folder.

## Limits, status and next allowed action

The assumptions are the already selected model's assumptions; no new
scientific choice is made. Illustrative geometry/advice values remain
illustrative and no experiment configuration is frozen. The concise report
explains the selection and its findings; full equations and proofs remain
in the existing linked companion. No positive action advantage, numerical
gradient correctness, physical fidelity or global simplicity is claimed.

The first draft is delivered for reading and revision. This is not user
acceptance of either the report or JM1 findings. The next allowed action is
bounded report revision in response to feedback. The old report/Step 4,
separate historical gates, closed ramp line and urban package remain
unchanged. No simulator/test/runner code, traffic experiment, AD/FD run,
optimization, dependency, sub-agent or external message occurs in this pass.
