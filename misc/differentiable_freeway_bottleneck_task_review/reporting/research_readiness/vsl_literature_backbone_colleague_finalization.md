# Final colleague-facing presentation

2026-10-22. **Editorial finalization requested after the user accepts the
content.** This pass makes the report suitable for colleagues without
changing the established model, information comparison or evidence claims.

[Final PDF](../../synthesis/research_readiness/vsl_literature_backbone_review_report.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_literature_backbone_review_report.tex)

[Build log](vsl_literature_backbone_colleague_build.log)

[Document checks](vsl_literature_backbone_colleague_validation.json)

[Preceding PDF/LaTeX archive](../../synthesis/research_readiness/vsl_literature_report_versions/v5/README.md)

## Reader-facing changes

Use the exact requested title, “VSL task with established peer work as
backbone & minimal adapted dependencies,” in both the document and PDF
metadata. Remove the subtitle/date line and internal author metadata.
Retain all source colors. Replace B/A/D/S attribution shorthand with full
words and a plain-language color legend; the prose still distinguishes
retained formulas, source-based adaptations and task-specific choices.

Remove phrases aimed at the review discussion, including “declared member,”
“member conventions,” “reviewed pair” and “direct finding for this review.”
Explain the task configuration, two initial states and source adaptations
directly. Replace source-specific R2/R3/A3 algorithm labels with the
proportional allocation, priority sharing and forward-continuation ideas
they denote; retain the citations and original labels in the supporting
source audit. Retain the source Equation 14 pinpoint reference.

Remove relative links to internal companion PDFs. Remove archival version
and header-date notes from the public reference list, retaining the same
eight works, years, titles, publication details, DOI/arXiv identifiers and
IEEE numbering. Detailed provenance remains in the review records. Remove
repeated explanatory sentences without removing a substantive model claim.
Define FD as fundamental diagram; replace compressed lookahead and
movement-coupling phrases with ordinary traffic prose. Keep the assumptions
heading and list together. Preserve the newly explicit Section 3.7 design.

## Assumptions and scientific limits

All display and inline mathematics are unchanged. The task remains a
continuous-mass lane-cell model using a Subraveti backbone, inherited Han
congestion budgets/VSL caps and a Carey-led movement adaptation with Wright
support. The shared service, finite-cohort setup, constant advice, complete
time objective and regular-branch derivative are unchanged.

The public report still states that the construction is relative to the
compared literature, without proving global minimality; that normalization
and three-lane sequencing are behavioral adaptations; and that speed
differences and acceleration recovery are not modeled separately. The
compact local reading is sufficient only for the two-state pair, the search
reference is not a certified global optimum, derivatives can fail at
switches, and numerical validation remains future work. Color changes
neither certify the assembled model as a source author's implementation
nor imply novelty.

## Files and commands

Update the live PDF/LaTeX, package introduction, source-first overview,
feedback-15 follow-up and successor dialogue. Add this record, the final
build log/check JSON and the v5 archive. Preserve older archives, the
accepted original VSL report, all source/assumption/evidence contracts,
analytical results, feedback files and the urban/ramp lines. Pre-existing
AGENTS.md, PLANS.md and memo.txt edits are unchanged.

Inspect with `rg`, `sed` and `git status --short`; edit using `apply_patch`.
Use the installed pdfTeX/TeX Live 2023 toolchain and Python 3.11/pypdf.
Before editing, retain a file-hash snapshot and before copies in
`/tmp/vsl_colleague_finalization/`; copy the before PDF/LaTeX to v5.
Build twice after the final source edit:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_colleague_finalization/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

Copy the built PDF beside its source and retain the final log above. Run
the document-only verification with:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_colleague_finalization/document_checks.py
git status --short
```

Checks compare all seven display environments/eight equations and 72 inline
expressions, source palette and formula-color markup, bibliography identity
and citation numbering, exact title/metadata, removal of internal notes,
page count, font embedding, working local record links and preservation of
other snapshotted files. Inspect PDF text/positions and color operators;
no raster PDF visual audit is claimed because no rasterizer is installed.
The main text occupies three pages at 10 pt; references occupy page 4.
Final checks pass: seven display environments retain the same eight
equations, all 72 inline expressions are unchanged, all source tints occur
in the PDF, the exact title is present in text and metadata, and the
assumptions heading stays with its list. The build has no warnings or
overfull/underfull boxes. All 193 checked local links resolve; 596 other
snapshotted files and the v5 before copies are preserved. Exact results
are recorded in the linked JSON.

No simulator code, dependency installation, traffic trajectory, numerical
gradient check, optimization or experiment is performed. Presentation is
finalized under the user's request; analytical status and evidence limits
remain unchanged. No new methodological gate arises. The next allowed
action is colleague reading or further bounded report feedback.
