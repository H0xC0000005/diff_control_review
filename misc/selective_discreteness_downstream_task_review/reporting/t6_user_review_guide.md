# How to review the T6 proposal

Date: 2026-09-10  
Purpose: single entry point for the T6 user gate

## Short version

T6 proposes one effective-service green-allocation task with five primary variants. The main scientific progression is:

```text
V0 task/equivalence check
  -> V1 shared-lane order without a bay
  -> V2 finite-bay storage without order emphasis
  -> V3 finite-bay access/order test
  -> V4 held-out robustness
```

The user accepted V0–V4 as the primary suite. The former V5 has been removed and renamed I1, a conditional post-suite integration/network test that may be required later but is not part of the first scientific campaign.

If you want the shortest sufficient review, read Sections 1–3 below and then answer the seven questions in Section 4. The other files are supporting detail.

## 1. First read: understand the six task variants

Read [`../synthesis/primary_green_allocation_suite.md`](../synthesis/primary_green_allocation_suite.md).

This is the most important T6 file. For every variant it tells you:

- whether the junction is isolated or corridor-embedded;
- whether all four symmetric approaches have exclusive lanes, a shared lane, or a finite turning bay;
- how route/movement traffic is allocated and matched;
- which mechanism is intentionally activated; and
- what conclusion the variant can and cannot support.

The key distinctions are:

| Variant | Layout | What changes scientifically | Intended question |
|---|---|---|---|
| V0 | Isolated; full-length movement-exclusive lanes; no bay | No selective mechanism | Do all implementations agree when local order should not matter? |
| V1 | Isolated; one lane shared by left and through/right; no bay | Ordered head-of-line eligibility | Can order alone alter service under equal movement totals? |
| V2 | Isolated; feeder/through lane plus finite left-turn bay | Physical bay storage and overflow | Is lane/storage-aware aggregate state already sufficient? |
| V3 | Same finite-bay layout as V2 | Ordered ability to reach the bay | Does exact order add information beyond aggregate lane/storage state? |
| V4 | Held-out isolated cases spanning V1/V3 layouts | Demand, storage, order, initial queue, and supply vary | Is any advantage robust and conditional on identifiable regimes? |
| I1 (not a primary variant) | Two-node arterial; downstream focal junction optimized, upstream signal fixed | Post-suite integration and initial network behavior | If later required, does the accepted isolated mechanism survive the intended local-detail/aggregate-link composition? |

Focus especially on whether V1 and V2 cleanly isolate order and storage before V3 combines them. I1 no longer requires a T6 inclusion decision.

## 2. Second read: review the common scientific contract

Read [`../synthesis/experiment_formulation.md`](../synthesis/experiment_formulation.md).

This file explains what remains identical across all variants:

- the action is continuous effective service under fixed phase topology;
- the output is not claimed to be an executable signal schedule;
- routes, ordering, geometry, and phase structure are fixed during differentiation;
- the primary objective is clearance-complete total system time, with delay as an equivalent companion measure;
- forward accuracy, derivative correctness, internal optimization, and richer-evaluator usefulness are separate claims; and
- equivalence or negative findings are legitimate outcomes.

It also expands the seven proposed defaults as D1–D7. Each subsection explains the operational picture, rationale, and condition for later revision; these defaults are part of the T6 review rather than already fixed decisions.

The bottom of that file contains the formal seven-item T6 approval request.

## 3. Read only if you want to audit the technical details

### Mathematical definitions

Read [`../synthesis/experiment_formulation_formal.pdf`](../synthesis/experiment_formulation_formal.pdf).

Use this to inspect:

- the constrained green-allocation parameterization;
- how phase allocation becomes movement service capacity;
- total-system-time units and clearance treatment;
- directional derivatives and finite-difference checks;
- what “aggregate-matched order pair” means formally; and
- positive, equivalent, partial, negative-transfer, and model-failure outcomes.

You do not need to read the `.tex` source unless you want to edit or audit the PDF generation.

### Baseline and fairness definitions

Read [`../synthesis/baseline_realization_matrix.md`](../synthesis/baseline_realization_matrix.md).

Use this to check whether every representation receives the same task. It distinguishes:

- homogeneous macro;
- structured movement/partial-FIFO queue;
- lane/storage-aware aggregate;
- proposed selective-order model;
- order-aware forward reference; and
- microscopic external evaluator.

It also separates representation comparisons from optimizer comparisons. The main question is whether the allowed adaptations are fair and whether any baseline is being denied information it should legitimately possess.

Then read [`../synthesis/literature_adoption_matrix.md`](../synthesis/literature_adoption_matrix.md) if you want to audit practical adoption. It maps each role to specific papers, distinguishes equation transcription from code reuse, records currently verified public implementations, states the necessary project adaptation, and identifies what must not be imported. The main judgment is whether the proposed literature affinity is strong enough and whether B1/B2 source combinations remain scientifically fair.

### Work and status audit

Read [`t6_completion_report.md`](t6_completion_report.md) only if you want the file-change list, assumptions, commands, validation results, and phase status. It contains no additional scientific proposal.

## 4. Decisions requested from you

You can answer these directly without commenting on every paragraph:

1. **Variant hierarchy:** Do V0–V4 and their formal gradient paths isolate the mechanisms correctly?
2. **Junction default:** Is the proposed rotationally symmetric four-leg junction with four protected service groups—north–south through/right, north–south left, east–west through/right, and east–west left—and matched approach traffic an acceptable default?
3. **Post-suite boundary:** Confirm that corridor test I1 is outside the primary campaign and may be opened later only if needed.
4. **Action and objective:** Do you approve effective-service allocation and clearance-complete total system time/delay?
5. **Baselines:** Do you approve the representation ladder and its capability-boundary rules?
6. **Evidence order:** Do you approve forward checks, derivative checks, perturbation transfer, matched optimization, then external evaluation in that order?
7. **Deferred numbers:** May exact lengths, demands, horizons, seeds, tolerances, optimizer, and budgets remain defaults until the relevant implementation and experiment plans can calibrate them?

If all are acceptable, a concise response such as “approve T6, with V5 as follow-on” or “approve T6, including V5 in the first campaign” is sufficient.

## 5. What is not being approved here

T6 approval would not:

- authorize implementation;
- modify the project roadmap or Milestone 2 files;
- claim executable phase timing;
- approve exact numerical experiment settings; or
- approve the Part-II future-task map.

Part II remains a separate literature-review and discussion item because the current map was not considered convincing enough.
