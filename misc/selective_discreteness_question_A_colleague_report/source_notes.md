# Source and production notes

Date: 2026-09-08

## Reporting job

- Audience: technically informed traffic/simulation colleagues who are not specialists in differentiable mesoscopic traffic simulation.
- Scope: literature gap, baseline models, component ancestry, minimality, and safe novelty/contribution claims for the proposed simulator architecture.
- Primary decision supported: whether the project has a literature-led, defensible scientific position and what comparison logic is required to test it.
- Delivery: one standalone LaTeX/PDF report, outside the closed review package's internal `reporting/` folder.
- Condensed delivery: `report_abstract.tex` and `report_abstract.pdf` provide a separate two-page professor-facing synthesis without a bibliography; the full report remains unchanged.

## Required-structure mapping

- Technical summary: `Technical summary: the project occupies a narrow open intersection`.
- Key findings/evidence: baseline ladder, work-by-work experiment roles, component ancestry, minimal-set argument, and evidence-chain sections.
- Scope and definitions: `Methods, scope, and interpretation limits`, with terms also defined where first needed.
- Methodology: corpus construction and coding summarized in the methods section; detailed protocol remains in the closed review package.
- Limitations/uncertainty: integrated into each major argument and collected in the methods/limits section.
- Recommended next step/further question: omitted from the reader-facing report because downstream task selection is outside the evidence reviewed here.
- Visual evidence: omitted because the evidence is categorical/model-comparative rather than a quantitative trend; exact lookup is better served by the baseline and ancestry tables.

## Evidence inventory

The report draws on the frozen review package at `../selective_discreteness_literature_review/`, principally:

- `reporting/closure_record.md`
- `reporting/review_report.md`
- `reporting/limitations.md`
- `reporting/prisma_counts.csv`
- `synthesis/model_taxonomy.md`
- `synthesis/baseline_map.md`
- `synthesis/novelty_gap_report.md`
- `extraction/evidence_matrix.csv`
- `extraction/baseline_feasibility.md`
- `extraction/r6_evidence_audit.md`
- `records/master_records.csv`

Project component definitions were checked against:

- `../../PROJECT_CONTEXT.md`
- `../../PLANS.md`
- `../../docs/milestones/milestone_0_ltm_baseline.md`
- `../../docs/milestones/milestone_1_ordered_route_mass_ledger.md`

No new external paper or metadata query was required for this report. Consequently, no new retrieval artifact was added to `../selective_discreteness_literature_review/archive/`. Future queries should be archived there as requested.

## Interpretation safeguards

- The report says “open intersection in the reviewed corpus,” never universal absence.
- Component relationships are classified as inheritance, adaptation, or composition; no individual component is called a first invention.
- The minimum-set claim is relative to the project's fixed-route, fixed-phase, node-facing target phenomena, not all mesoscopic behavior.
- The lane-local state and order-conditioned service are described as proposed architectural components rather than completed model capabilities.
- The report does not select a downstream task, amend the project plan, or approve implementation.

## Build and QA

Build from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error report.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error report_abstract.tex
```

QA should confirm successful compilation, resolved references/citations, page count, and rendered-page legibility.
