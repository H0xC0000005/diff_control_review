# Compact report: IEEE references and component attribution recheck

Date: 2026-10-19. **Requested editorial/reference revision completed.**
The methodology page target is 2.5 pages excluding references; main text
remains nominal 10 pt. This is a report correction within Step 4.

[Revised PDF](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Revised LaTeX source](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

[Equation/source credit and reading limits](../../extraction/research_readiness/vsl_compact_report_source_and_coverage_map.md)

[Build log](vsl_report_reference_revision_build.log)

[Verification record](vsl_report_reference_revision_validation.json)

## What changed and why

The second pass makes the formulation's intellectual ownership more
explicit. The lane-transfer equation credits the conservative paired-source
structure in Nagalur Subraveti et al. and the receiving-work/own-lane-priority
ingredients in Carey et al. The triangular diagram and finite-terminal
boundary ingredients retain Jin's LTM citation. Point insertion and bounded
acceleration receive Leclercq et al.'s 2011/2016 mechanism credit; the profile
is explicitly described as a derivative of the 2016 isolated passing curve.
Kong et al. receives credit for the regular event correction alone.

The report continues to identify the homogeneous minimum/length scale,
speed-mismatch work, representative marks, service table/guards, E-only
recent-mass renewal and model-specific derivative deductions as definitions
or deductions here. A citation does not transfer those choices to its source.
All 11 displayed equation groups and the complete service table remain
unchanged from the initially delivered report.

The bibliography expands from four to six already reviewed references.
All entries now use IEEE numbered style, author initials, quoted titles,
abbreviated journal names, verified volume/issue where available, page
ranges, publication dates and DOI links. Citations appear in first-use
order. IEEE-style multiple citations use separate brackets. This is a
reference-style revision; the existing one-column methodology layout remains.

Final publication metadata improves the formerly incomplete Jin, Carey
and Kong entries. Carey is now cited as the 2015 journal article while the
inspected author manuscript remains dated 2013. Kong's published 2024
Proc. IEEE record replaces its incomplete preprint entry. The Nagalur
Subraveti reference uses the 2019 publisher online/institutional year;
the PDF header's 2020 discrepancy remains explicit in the supporting map.
The 2011 Leclercq reference is the conference text actually viewed, rather
than the different journal DOI on the author's upload landing page.

The source/coverage map, current report plan, four entry-point notices,
progress and dialogue are synchronized. The feedback inbox is unchanged.
The initial source/PDF and coverage-map bytes are preserved in the
[v1 archive](../../synthesis/research_readiness/vsl_report_versions/v1/README.md).
Initial build and validation records are unchanged.

## Commands and checks

Read the existing report, accepted equations/source audits, feedback,
current plan and Git status using `sed`, `rg`, Python and `git status --short`.
Rechecked selected primary text and publisher/author metadata through the
web tool; reading limits and primary links are in the source map. Publisher
403s and a Yperman PDF timeout supply no new content evidence; existing
primary manuscripts/local PDFs and authoritative metadata provide the
recorded credit. No new general literature sprint is opened.

Saved the 459 pre-edit package hashes and exact feedback hash to
`/tmp/vsl_reference_revision_before.json`. Used the existing `pdflatex`
and installed review environment with `pypdf`; no dependency was installed.
`cite.sty` is already available. Complete IEEE entries are written directly
in LaTeX, so no new bibliography package is needed.

Two final LaTeX passes, from `synthesis/research_readiness/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_reference_revision_latex vsl_compact_methods_report.tex
```

The resulting PDF is copied beside its source. The retained final-pass log
has no warnings, unresolved references or overfull/underfull boxes.

Artifact checks:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_reference_revision_checks.py
git status --short
```

Checks compare all 11 equation environments and the service table exactly
against v1; inspect citation order/resolution, six DOI targets, PDF text,
page positions, 10 pt body type and embedded fonts; verify changed-document
links, feedback preservation, v1 copies and all protected package hashes.
The method extent is measured through its last line before the reference
heading, including font descent and excluding footer numbers. The PDF has
three physical pages; its methodology ends before the third-page midpoint.
References follow it and are excluded from that measurement.
Detailed results are saved in the verification record. No raster visual
inspection is claimed; PDF text/geometry and LaTeX box checks are used.

**Results: passed.** The methodology occupies about 2.34 pages excluding
references, with nominal 10 pt main text and all 13 fonts embedded. All
11 equation groups and the service table match v1 exactly. Six citations
resolve in first-use order with six DOI targets; the final build is clean.
All 570 local links and 22 heading anchors across the nine changed/new
Markdown documents pass. Nine existing package files changed and seven
files were added; none were deleted. All 450 protected existing artifacts,
the feedback text and the exact v1 copies pass their hash checks. The
pre-existing root Git edits remain the only tracked repository changes.

## Assumptions, status and stop

The accepted task, global assumptions, admission domain, four model
components, information comparison, objective and regular sensitivity
contract are unchanged. Existing scientific/evidence limitations remain in
the review archive; their discussion remains outside the compact PDF under
the user's writing instruction. No new methodological choice arises here.

No simulator code, dependency installation, traffic/ODE run, optimization,
AD/numerical-gradient or SUMO experiment occurs. No colleague is contacted.
Root repository edits present before the task are preserved.

This reference revision is complete for user reading. Overall Step 4,
the original Step 3 formal-closure record and optional SUMO status are
unchanged. The next allowed action is a requested report correction or a
separately opened companion item; none starts automatically.
