# Source colors and relationship labels for the report

2026-10-22. **Historical source-color pass, followed by the source-hierarchy revision.**
Its final stronger-palette PDF/LaTeX are preserved as v3 below. The subsequent
[hierarchy revision](vsl_literature_backbone_review_hierarchy_work_report.md)
incorporates the agreed dependency account without changing the equations.
The analytical review remains complete. Formula/source attribution reuses
the accepted source audits; it makes no new modeling decision or scientific
claim. The selected model, task, evidence and historical gates are unchanged.

## What changed

Update the [report PDF](../../synthesis/research_readiness/vsl_literature_report_versions/v3/vsl_literature_backbone_review_report.pdf)
and [adjacent LaTeX](../../synthesis/research_readiness/vsl_literature_report_versions/v3/vsl_literature_backbone_review_report.tex)
with an in-report mapping table and moderate source colors. Key components,
formula terms, citations and reference-list entries use the matching color.
Most prose stays neutral. Standard conservation/calculus stays neutral so
that routine algebra is not presented as an invented traffic component.
Mixed-origin formulas use more than one color. The retained literature
comparison and expanded backbone remain the report's structure; Section 4
is not restored.

Archive the [v2 PDF/LaTeX](../../synthesis/research_readiness/vsl_literature_report_versions/v2/README.md)
unchanged, update the package README, selected structure and successor
dialogue, and point the historical v2 work record to its archived artifacts.
Add this record, the [final build log](vsl_literature_backbone_review_color_build.log)
and [document verification](vsl_literature_backbone_review_color_validation.json).

## Color mapping

| Report reference / role | Color | Hex | Meaning |
|---|---|---|---|
| [1] Jin–Jin | Slate gray | #56617B | Comparison-only aggregate/spatial model. |
| [2] Wei–Han–Wang | Brown | #895B32 | Comparison-only history-aware aggregate model. |
| [3] Subraveti article | Grass green | #317D37 | Retained lane-density framework and desire forms. |
| [4] Han 2016 | Purple | #7146A9 | Density-dependent discharge, receiving and recovery slope. |
| [5] Han 2017 | Blue | #165CA7 | Nominal no-drop cap and VSL sending cap. |
| [6] Carey et al. | Amber | #947112 | Adapted diagonal transport, receiving/fallback principles. |
| [7] Subraveti thesis | Magenta | #A5418A | Source clarification of 2:2:1 lookahead. |
| [8] Wright et al. | Cyan | #23828C | Adapted equal-priority capped-sharing kernel. |
| This study | Muted red | #B53D36 | Our task/member definitions, composition and derived residual/sensitivity. |
| Standard algebra | Neutral charcoal | #2A2A2A | No exclusive source ownership or invention claim. |

Source color applies to a rule/component, not ownership of its variable
names. The cited work and explicit relationship label carry the meaning;
color alone is not the only distinction. The reference list retains the
same eight entries and IEEE numbering.

| Relationship | In-report styling | Interpretation |
|---|---|---|
| B | Plain sans-serif B in source color | Source form retained/re-expressed, including notation/index changes. It does not identify the whole adapted task as a native published benchmark. |
| A | Bold sans-serif A in source color | We adapt or compose the indicated source principle; source guarantees/calibration are not inherited. |
| D | Bold sans-serif D in this-study red | Defined/derived here, including elementary parameter/boundary choices. This is not a novelty claim. |
| S | Neutral sans-serif S | Standard identities, conservation, population-time accounting or chain-rule calculus. |

## Formula attribution reconciled with the existing audit

| Formula/component | Source color and relationship | Basis and limit |
|---|---|---|
| Eq. (1) capacity/critical density | Neutral S | Standard triangular-diagram identities; no exclusive Han invention claim. |
| Eq. (1) Q law | Purple B density-dependent branch; blue B nominal cap | Existing Han source reconciliation: [4] supplies homogeneous law/recovery lineage and [5] states the capped no-drop branch explicitly. The min form is the same re-expression already selected. |
| Eq. (2) D/R and recovery slope | Blue B sending; purple B receiving/slope; purple A lane-wise mapping | Source forms are retained, but their application to one target allowance shared across straight/diagonal arrivals is our interface adaptation. |
| Eq. (3), route and lookahead | Green B desire/route form; magenta B lookahead; red D member conventions | Source forms and thesis weights are retained. Mode/direction/empty/finite-end choices remain declared member definitions, not recovered author code. |
| Eq. (4) | Red D | Our joint normalization/request composition. |
| Eq. (5) | Cyan A, with nearby amber A receiving context | The fixed-priority capped kernel is adapted from Wright; Carey supports receiving/unused-share principles. This is not the complete Wright MIMO solver or unchanged Carey algorithm. |
| Fallback, f and final E | Amber A fallback; red D f composition and compulsory lane-end rule | The three-lane sequencing and permanent-end closure remain ours. |
| Eq. (6) | Neutral S; nearby amber A transport | Standard mass balance applied to the selected forward/diagonal flow topology. |
| Eqs. (7)–(8) | Neutral S prefix/calculus; red D residual-dependent terms | The task-specific exact residual and its state/direct-speed derivatives are derived here using standard accounting/calculus. The complete derivative includes both colored and neutral terms. |

Read the already completed
[source/interface audit](../../extraction/research_readiness/vsl_methodology_review_source_and_interface_audit.md),
[allocator source boundaries](../../extraction/research_readiness/vsl_allocator_sources_and_adaptations.md),
[Han source reconciliation](../../extraction/research_readiness/vsl_congestion_join_sources_and_adaptations.md)
and [global assumptions/source record](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md).
No new literature search or primary full-paper reading is claimed.

## Build and checks

Use installed `pdflatex`, `xcolor`, core LaTeX/amsmath and pypdf. Inspect
files with `rg`, `sed`, `cat` and `git status --short`; edit with
`apply_patch`. Probe installed TeX packages with `kpsewhich`. Archive files
with Python file tools. No dependency installation or environment change
is performed. The final document uses standard 10 pt text to fit the key
and expanded model within the existing 2.5-page budget; mathematical script
sizes remain standard. Custom fractional-size trials are not used in the
delivered source.

Build twice after the final source edit:

```bash
pdflatex -interaction=batchmode -halt-on-error -file-line-error -output-directory /tmp/vsl_literature_report_color3/latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_literature_backbone_review_report.tex
```

The PDF has three pages; main text including the key occupies about 2.27
pages, excluding references. There are no final warnings or overfull/
underfull boxes. The prior eight equations, inline mathematical expressions
and bibliography content match after removing style wrappers/whitespace.
The same regular-branch assumptions, exact residual and comparison remain.

Validate actual RGB text-drawing operators in the PDF, including imported
source colors on the model page and matching references. Check palette
contrast on white and inspect a generated palette preview. The source
colors have moderate lightness and contrast greater than 4.5:1 on white;
explicit labels/citations remain available without color. This does not
claim universal color-vision discrimination or a rendered-PDF visual audit.
No PDF rasterizer is available; inspect extracted text/positions, fonts,
color operators and the TeX layout log. No traffic experiment is involved.

Before-edit snapshot:
`/tmp/vsl_literature_report_color3/before.json` (580 existing files).
Run:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_literature_report_color3/document_checks.py
git status --short
```

All document checks pass: unchanged mathematical/bibliographic content,
eight settled equation labels/references, resolved current links, actual
palette use, byte-preserved v2 archive and unchanged protected files beyond
the six allowed report/navigation edits. The pre-existing tracked changes
in AGENTS.md, PLANS.md and memo.txt are untouched. Exact counts, colors,
contrast ratios, hashes and tool versions are in the verification JSON.

## Status and next allowed action

**Palette intensity follow-up, 2026-10-22.** The user approves the color
direction and requests a little more saturation and brightness throughout.
Increase each source hue and this-study red by about 0.10 HSV saturation
and 0.035 HSV value; warm amber slightly to preserve readable contrast.
Lighten neutral charcoal slightly while keeping it neutral. The mapping
above gives the delivered values. Inspect the before/after palette preview,
rebuild twice with the command above and rerun the same document checks.
All tints retain contrast above 4.5:1 on white. Text, mathematics, attribution,
layout and methodological status are unchanged. Before-edit copies and the
palette comparison are retained under `/tmp/vsl_palette_tune/`.

The upgraded report is delivered for user reading. The presentation labels
do not change methodological decision status or imply report/JM1 acceptance.
The next allowed action is bounded feedback/revision. No simulator code,
traffic or numerical-gradient test, optimization, new review sprint,
dependency installation, sub-agent or external communication occurs. The
accepted old VSL report, closed ramp line and separate urban work are intact.
