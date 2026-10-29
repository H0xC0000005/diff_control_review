# Concrete lane model discussion: opening work record

26 October 2026. **Closed by the user:** “Comparison, sensitivity and scientific credit: agreement on principles.” **Current topic:** “Concrete traffic model: lane allocation, bay access, storage and service.” The requested discussion material is prepared. All concrete recommendations remain unapproved; no implementation phase or experiment is opened.

[Read the concrete discussion](../../temp_content/research_readiness/coupled_lane_access_and_service_discussion.md)

[Candidate definitions and hand comparisons, PDF](urban_coupled_lane_model_candidates.pdf)

[Retained mathematical source](urban_coupled_lane_model_candidates.tex)

[Sources and assumptions](../../extraction/research_readiness/urban_coupled_model_source_and_assumption_notes.md)

## What is closed and what is newly proposed

The decision record and discussion log record the user's explicit closure. Original-series access through declared macro conversion, the one-step-to-complete-TST sensitivity explanation and both source-credit approaches remain agreed. Q1–Q4, fixed valid commitments, continuous mass, exact order and the deferred retargeting/mixing directions are preserved. Closure supplies no numerical horizon, tolerance, traffic law or principal rival.

The new packet compares five scientific choices through shared examples: physical bay-opening representation, perceived lane cost, new target chronology/profile after a split, mixed-lane average service and shared downstream receiving. Ten named subvariants supplement the 15 stable IDs and 34 earlier high-level candidate entries. Their names distinguish axes rather than replace high-level A/B labels or create implementation checkpoints.

The material provisionally recommends an explicit internal opening, a current-pressure cost and an elapsed-rate FIFO server. It investigates cumulative target profiles and favors receiving reuse as a direction. A cost vector does not determine target chronology, and node feasibility constraints do not determine a joint allocation/priority rule. Those limitations are explicit. The packet is not presented as a reconstructible complete model or evidence of better gradients.

Hand examples distinguish partial admission from physical bypass, queue-pressure preference from service-aware work, and two exact-prefix service meanings. At the same feasible four-group allocation, their current departures and analytically derived local slopes differ. These are algebraic illustrations, not simulator runs, calibrated settings or gradient-validation experiments.

## Files changed

New artifacts:

- The descriptive discussion document linked above.
- The candidate `.tex`/PDF pair.
- The source/assumption record.
- This work record and [document verification result](urban_coupled_model_opening_validation.json).

Updated existing records:

- [Decisions](../../temp_content/research_readiness/review_decisions.md): explicit closure, newly opened topic, provisional recommendations and specification levels.
- [Topic guide](../../temp_content/research_readiness/review_plan.md), [overview](urban_readiness_overview.md) and [gap explanation](urban_vsl_standard_gap_explainer.md): current navigation and relation to the remaining model-definition gaps.
- [Closed principles record](../../temp_content/research_readiness/comparison_sensitivity_and_credit_proposal.md): a closure notice and link to the new discussion, preserving its scientific content.
- [Living inventory](../../extraction/research_readiness/urban_open_question_register.md): ten named subvariants and relevant C2/C3 explanatory links, without changing prior candidate definitions or scientific relationships.
- [Completeness/topic map](../../extraction/research_readiness/urban_review_completion_and_work_map.md): current topic and navigation; completeness criteria and report budget retained.
- [Discussion log](../../temp_content/research_readiness/review_dialogue.md): user authorization, closure and opening rationale, new coupling issue and candidate status.

User feedback, root instructions/context/roadmap, approved plans, M2 implementation records, source/tests/configs, previous reports/validation snapshots and VSL artifacts are not edited.

## Evidence, assumptions and limits

Read repository instructions/context/roadmap, feedback, T6/T7 authority and the accepted task/variant/adoption records. Inspected the inherited M0 link/signal definitions and code, M1 timing/ledger rules, M2 closed globals and the still-proposed component receiving/capacity/eligibility choices. Existing implementation progress does not determine the review's scientific selection.

Bounded primary text checks cover T0030's node-exit equilibrium scope and T0010's directional physical-queue context. The source record gives exact URLs and reading depth. They do not supply the proposed zone-entry costs, exact bay-access law, shared-lane clock or joint receiving operator. No source uniqueness or gradient theorem is transferred. The new costs and local service comparisons are explicitly defined-here prototypes; generic node feasibility and causal link physics remain inherited references.

The internal-opening candidate changes concrete local section/target ownership beyond the simplest upstream-only waiting view and must be reconciled with the inherited seam. Mouth alignment would amend the refinement-domain description. Neither expands lane permissions; responsive choice is inactive when only one target is legal. Local section capacities and delays must reconcile with the physical/matched aggregate model. The existing boundary-time history and new local service clocks still need a consistent joined timing formulation.

The current-pressure cost is finite without knowing service; the work cost assumes known average service and needs zero-service handling. Intended-vector partition invariance does not establish invariance of newly created target order. Both target-piece and cumulative-profile directions need a concrete, order-consistent interpretation. Receiving reuse still needs an actual priority/allocation law. A complete V0–V4 model and neutral/reference checks remain future scientific work; no tested new local LTM network is claimed.

## Commands, build and verification

Working directory: `/home/zpz/repos/diff_minimal_meso`. Inspection used `rg`/`rg --files`, `cat`, `sed`, `head`, `tail`, read-only `git status --short`, and bounded web searches of primary sources. Edits used `apply_patch`. A pre-edit content snapshot records 776 files at:

`/tmp/urban_coupled_model_opening_before_20261026.json`

The local toolchain is pdfTeX 1.40.25, TeX Live 2023/Debian. Two successful passes build the candidate note:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/urban_coupled_model_latex_20261026 misc/selective_discreteness_downstream_task_review/reporting/research_readiness/urban_coupled_lane_model_candidates.tex
```

Run twice, then copy the PDF beside the retained source. The auxiliary files stay in that `/tmp` directory. The final build has no LaTeX warnings or box overflows. The six-page PDF is checked with existing pypdf 6.15.0; raster inspection is not claimed because the probed renderers are unavailable. No package is installed. The main document's small Mermaid diagram represents the physical road topology, not review stages.

The preservation/link/inventory checker is retained at `/tmp/urban_coupled_model_opening_document_check_20261026.py`:

```bash
python3 /tmp/urban_coupled_model_opening_document_check_20261026.py
git status --short
```

The linked verification result records local links/cited lines, stable IDs and all prior candidate definitions, named-variant coverage, scientific relationships, closure notices, PDF/source integrity and protected files. No traffic simulation, finite-difference/autograd check, optimization, SUMO run or scientific acceptance test is performed. Analytic hand comparisons do not establish forward fidelity, gradient correctness of an implementation or downstream usefulness.

**Document verification passed:** 140 local links/cited lines checked; all 15 question IDs and 34 earlier candidate entries preserved; all ten named subvariants present across the discussion, supporting record and mathematical source. Of 776 snapshotted files, 768 are byte-identical and eight are the intended live-record updates; the six new artifacts are accounted for. No protected or outside-snapshot change was found. The final six-page PDF matches its build output, contains readable extracted text on every page and has a clean LaTeX log. Read-only Git status still lists only the pre-existing tracked changes to `AGENTS.md`, `PLANS.md` and `memo.txt`.

## Remaining discussion

The next conversation can examine the five concrete questions and refine the candidate constructions. No recommendation is approved by this opening. Target chronology/profile, joint downstream allocation and timing compatibility are still incomplete, and any genuinely conflicting scientific assumption must be identified explicitly. The review remains organized by its traffic questions; simulator changes and numerical experiments require their own authorization.
