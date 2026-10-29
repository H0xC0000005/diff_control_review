# Accepted compact VSL methods report: clean final format

Date: 2026-10-20. **User-accepted report; clean finalization completed.**
The user states that the report is satisfactory and explicitly requests
normal text and any necessary final formatting/coherence corrections.

[Final PDF](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Final LaTeX source](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

[Source and equation coverage](../../extraction/research_readiness/vsl_compact_report_source_and_coverage_map.md)

## Final formatting and coherence

Removed all red text commands, the revision-highlighting wrappers and their
unused color package, and the feedback/revision notice below the title.
The first heading now reads “Research questions” to match its three bullets.
The clean report keeps the accepted five-part structure, five global
assumptions, four model components, adjacent source/adaptation credit,
seven IEEE references, and the local H/saltation explanations.

Reviewed the paragraph flow, symbol introductions, source links, service
table and equation references. The approved text needs no further substantive
rewrite. The PDF's content matches the reviewed red version after removing
the notice and pluralizing that heading, allowing only layout whitespace
and line-end hyphenation differences. All 11 equation groups and service
branches preserve their mathematical content.

The PDF has four physical A4 pages and about 3.46 pages of methodology
excluding references, within the 3.5-page target. Main text is nominal
10 pt. Page breaks preserve the traffic overview, service/table block and
complete-sensitivity block. Normal black text, embedded fonts, resolved
equation/citation links and a clean build are checked in the verification record.

## Records and commands

Changed the current source/PDF, source/coverage map, current report plan,
four entry-point notices, progress and dialogue to record acceptance and
the normal-color final artifact. The feedback inbox is unchanged. Exact
pre-finalization source/PDF/map bytes are retained in the
[v5 archive](../../synthesis/research_readiness/vsl_report_versions/v5/README.md).
Prior work reports, proofs, results, build logs and validations are preserved.
The 485 pre-edit package hashes and feedback hash are recorded in
`/tmp/vsl_clean_final_before.json`.

Read the repository context/roadmap, accepted report and relevant records
using `sed`, Python and `git status --short`. The existing toolchain is
`/usr/bin/pdflatex`, pdfTeX 3.141592653-2.6-1.40.25 (TeX Live 2023/Debian).
After initial label resolution, two final passes run from
`synthesis/research_readiness/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_clean_final_latex vsl_compact_methods_report.tex
```

[Final build log](vsl_clean_final_build.log)

Verification uses the already installed review Python/pypdf environment:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_clean_final_checks.py
git status --short
```

[Verification record](vsl_clean_final_validation.json)

Checks compare approved PDF content and equations against v5, confirm all
text is black and review notices are absent, inspect page extent and
10 pt type, and verify embedded fonts, IEEE/cross-reference destinations,
local links, exact archives, feedback and protected hashes. The final
build has no warnings or overfull/underfull boxes. PDF text, drawing
instructions and geometry are inspected; no raster inspection is claimed.

## Assumptions, acceptance and next allowed action

The user's acceptance closes the bounded report-writing and revision item.
It does not create new empirical evidence or authorize simulator development,
experiments, urban alignment or another review stage. The accepted traffic
assumptions, information rights, objective, derivative domain and scientific
limits in the review archive are preserved. No dependency installation or
scientific run occurs, and the pre-existing root Git edits are preserved.

This clean report is finalized. Broader Step 4 companion work and historical
stage-closure records retain their existing scope. The next allowed action
is an explicitly requested companion item or further editorial correction;
none starts automatically.
