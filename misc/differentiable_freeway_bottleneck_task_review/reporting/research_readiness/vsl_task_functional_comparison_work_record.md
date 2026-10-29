# Functional comparison of the two VSL tasks

2026-10-29. **Topic: a short colleague-facing comparison of model behavior.**
The user reports that Wang supports taking VSL first and asks for a small
PDF with a brief introduction followed by a straight comparison table.
This is documentation of established conclusions; it opens no implementation
or experiment and changes no scientific decision.

[One-page comparison PDF](../../synthesis/research_readiness/vsl_task_functional_comparison.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_task_functional_comparison.tex)

[Final build log](vsl_task_functional_comparison_build.log)

## Content and source basis

Compare the completed task-first formulation with the current adapted
Subraveti/Han/Carey model, rather than an incomplete S13 draft. The brief
introduction defines E/A/B and their shared continuous-mass, finite-cohort,
constant-advice and full-time objective. Ten table rows compare spatial
state/propagation, early merging, lateral permissions, advice/capacity,
forced-merge sharing, queuing/storage, post-exit effects, time accounting,
sensitivity and concealed lane information.

Keep the earlier qualifications explicit: exponential distance decay is
conditional on sufficient adjacent service; the old bounds keep preparation
free and B unqueued; the old point-service ceilings are separately fixed;
the new nominal diagram remains fixed while advice caps sending. New
receiving priorities are fixed equal reference weights, not incentive-based,
and E has no extra receiving-work cost. Neither TST formula creates a
merge penalty independently of the traffic dynamics. The new final-A
statistic is sufficient only on the declared two-state example. Describe
functional differences without claiming a performance advantage or native
identity of our adaptations to any complete published model.

Use plain prose without internal review labels, approval history, colleague
names or a discussion pipeline in the public PDF. Keep the requested format
to introduction plus three-column table, without an additional report section.
Use 10 pt text on one A4 portrait page with 15 mm margins and row separators.

[Earlier six-point comparison and clarifications](vsl_feedback16_old_and_peer_backbone_comparison.md)

[Source/module explanations](vsl_literature_backbone_peer_work_overview.md)

[Completed task-first formulation](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

[Current complete model](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.tex)

[Current colleague-facing model report](../../synthesis/research_readiness/vsl_literature_backbone_review_report.tex)

## Files, commands and checks

Add the comparison PDF/LaTeX, this work record and final build log. Add its
link to the package README and record the request/conclusion in the topic
discussion log. Preserve both existing reports, model contracts, proofs,
source audits, feedback and all other existing files. The pre-existing
AGENTS.md/PLANS.md edits remain untouched.

Inspect with `rg`, `sed`, `git status --short` and installed pypdf. Save
before-file hashes in `/tmp/vsl_functional_comparison_20261029/before.json`.
Use `apply_patch` to author the document. Verify `pdflatex --version` and
build twice after the final source edit:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_functional_comparison_20261029/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_task_functional_comparison.tex
```

Copy the PDF beside its LaTeX source and retain the final log above. Use
Python 3.11.9 and installed pypdf for document-only checks:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_functional_comparison_20261029/document_checks.py
git status --short
```

Verify one page, all ten rows and both columns, font embedding/readable
10 pt text, PDF text/positions, no warnings or overfull/underfull boxes,
working local links and preservation of prior files. No raster visual
audit is claimed: pdftoppm, mutool, Ghostscript and PyMuPDF are unavailable,
and no dependency is installed. Exact check output is saved in
`/tmp/vsl_functional_comparison_20261029/validation.json`.

Final document checks pass: one page, ten complete comparison rows,
embedded fonts at the declared 10 pt body size, no build warnings or
overfull/underfull boxes, and 175 working local record/navigation links.
The lowest text baseline is about 148 PDF points above the page bottom,
comfortably inside the 15 mm margin. Only the README and discussion log
change among existing files; all 606 other snapshotted files, including
both main reports and model contracts, are byte-preserved.

The agreed scientific content is unchanged. Empirical information value,
gradient usefulness and physical fidelity retain their previously stated
evidence limits. No new methodological question arises from this summary.
The next allowed action is colleague reading/discussion; simulator work
and traffic experiments remain outside this task.
