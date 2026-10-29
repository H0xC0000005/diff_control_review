# T6 completion report

Date: 2026-09-10  
Status: T6 Part-I work complete; awaiting user approval; T7 not opened

## Outcome

Candidate A has been translated into a proposed scientific task contract. Five explicitly separated primary variants define what changes, how traffic is allocated, and why each variant exists:

- V0: isolated, movement-exclusive, no bay—macro/equivalence control;
- V1: isolated, shared lane, no bay—pure head-of-line order;
- V2: isolated, finite left-turn bay—storage without order emphasis;
- V3: isolated, finite left-turn bay with aggregate-matched order pairs—main accessibility/order test;
- V4: isolated combined held-out family—robustness and conditional sufficiency.

During T6 review, the user accepted V0–V4 and removed the former V5 from the primary suite. It is retained only as conditional post-suite integration/network test I1, to be opened later if necessary.

The formal contract fixes effective-service semantics, continuous feasible allocation, clearance-complete total system time including source queues, stable-signature directional derivative checks, aggregate-matched order pairs, fixed scenario banks, and explicit positive/equivalent/negative-result logic.

The current gate should be reviewed through `t6_user_review_guide.md`; it provides the reading order and consolidates the seven decisions without adding new scientific content.

## Files changed or produced

- `discussion/t5_closure_record.md`
- `discussion/t6_dialogue.md`
- `synthesis/future_task_map.md`
- `synthesis/primary_green_allocation_suite.md`
- `synthesis/baseline_realization_matrix.md`
- `synthesis/experiment_formulation.md`
- `synthesis/experiment_formulation_formal.tex`
- `synthesis/experiment_formulation_formal.pdf`
- `reporting/t6_completion_report.md`
- `reporting/t6_user_review_guide.md`
- `README.md`
- `discussion/protocol_approval_record.md`
- `review_protocol_plan.md`
- `archive/manifest.csv`

During user review, the proposed-default section of `synthesis/experiment_formulation.md` was expanded into D1–D7 so each default states its operational meaning, rationale, and permissible evidence-based revision path. This was a presentation clarification, not a decision-status change.

LaTeX auxiliary/build files were generated beside the PDF for reproducibility. No project source, test, configuration, milestone, roadmap, or context file was modified.

## Assumptions and open decisions

- Part II remains unapproved and outside this T6 formulation pending further literature review.
- The rotationally symmetric four-leg, four-service-group construction is the user-directed default; its detailed scenario realization remains part of the open T6 review.
- Exact numeric geometry, demand, horizon, seed-count, tolerances, optimizer, and budget are deliberately deferred to interface-aware calibration and later experiment planning.
- Corridor test I1 is outside the primary campaign and may be opened later only if needed after V0–V4.
- SUMO remains the proposed richer evaluator, but its exact effective-service realization mapping is not silently fixed here.

## Commands and validation

- Inspected the current downstream-status audit, T4 evidence codebook/matrix, project roadmap, and active Milestone 2 Phase-B records for compatibility.
- Compiled the formal contract with `latexmk -pdf -interaction=nonstopmode -halt-on-error experiment_formulation_formal.tex`.
- The first build exposed a missing optional `enumitem` package; removing that formatting-only dependency resolved the build without changing content.
- Recompiled the initial contract to a stable three-page PDF; the later variant-gradient amendment expanded the validated contract to five pages.
- Checked artifact existence, phase-status consistency, manifest uniqueness, required variant coverage, decision-status labels, and T6 gate presence.

## Evidence and limitations

The report structure was shaped using the technical analytical-report workflow: answer first, then definitions, model/experiment specification, limitations, and explicit decisions. Evidence provenance is maintained through record IDs and the T4 matrix/audit. No quantitative experiment has been run; T6 specifies what later evidence must mean.

## Current phase and next allowed action

T5 Part I is closed. T6 Part-I work is complete but awaits the seven decisions in `../synthesis/experiment_formulation.md`. T7 may open only after T6 approval. The Part-II map requires a separate literature-review/discussion continuation and is not authorized by T6 approval.

The current T6 revision additionally formalizes $f$, $x$, $df/dx$, the complete state-sensitivity chain, and the separate V0–V4 propagation paths. These definitions remain at the T6 approval gate.
