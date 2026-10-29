# D1 verdict — a chronology-safe point-diverge task is conditionally viable

Date: 2026-09-15  
Status: D1 complete; RM4 stopped at the next user gate

## Conclusion

There is now a supported intersection of RQ1 and RQ2, but it is narrower than an ordinary freeway-ramp experiment.

**Recommendation: proceed to detailed formulation only for an elementary “B1-P” proof task: one metered input and one mainline input merge into one ordered stream, propagate over a first-order link, and encounter a fixed-supply one-stream/two-output point diverge. Require the two merge-input eligibility profiles to be non-overlapping.**

This construction avoids spatial lane changing and gives the merged stream a physically unambiguous chronology. It can test whether retaining route order changes useful metering sensitivity at a downstream restriction. It is not yet approved for formulation, and it does not support a general claim about ordinary overlapping multilane freeway traffic.

## Separate verdicts

| Question | D1 verdict | Boundary |
|---|---|---|
| RQ1, narrow B1-P | **Conditionally positive** | First-order merge quantities, LTM propagation, and a one-stream point diverge suffice; no lane-changing or independent speed state is needed. Non-overlap at the merge is mandatory. |
| RQ1, ordinary overlapping/multilane B1 | **Not compatible under current contracts** | Simultaneous continuous inputs have no source-backed unique total chronology, and real multilane exit access may require distributed lane behavior. |
| RQ2, scientific diagnosticity | **Positive as a test, not as a predicted win** | The meter changes upstream admission timing; service at the downstream diverge is fixed. The task asks whether propagated order changes the control gradient/outcome beyond route-aware aggregate models. |
| RQ2, independence from TSC | **Distinct causal question, shared primitive** | It tests indirect arrival shaping and order transport across a link, not local green allocation. It reuses ordered-access semantics and is therefore a second application/transfer test, not a second independent physics contribution. |
| Evidence feasibility | **Adequate for formulation** | Carey supplies ordered cohort/diverge semantics; Wright and FIFOQ supply strong aggregate alternatives; Boukhellouf et al. supply a no-discretionary-lane-change microscopic point-diverge benchmark. Exact gradient and evaluator settings remain RQ3–RQ5 work. |

## The B1-P mechanism

### Physical chain

1. A fixed mainline demand and a continuously controlled ramp-release schedule approach a first-order merge.
2. Only cases in which their actual eligibility-time intervals do not overlap are admissible. Their chronological union is therefore unique; no artificial whole-package tie-break or sub-packet interleaving is invoked.
3. The combined ordered route-mass stream propagates on the established first-order long-link backbone.
4. It reaches a one-upstream/two-output point diverge: one output is continuing mainline, the other is an exit with fixed supply/storage.
5. Ordered service inspects the earliest eligible route mass. When exit-bound head mass cannot enter the exit, later through mass cannot pass it in this single-stream abstraction. Output/link storage produces ordinary spillback.
6. The only optimized intervention is upstream ramp admission. Downstream route choice, topology and supply remain fixed.

This mechanism consumes continuous mass, fixed route identity/position, eligibility time and cumulative-mass order. It does not consume physical vehicle locations, gaps, lane-change trajectories, independently evolving speed, or optimized downstream service.

### Why this is not merely the signal task under freeway labels

The signal task changes local service allocation at the same node whose order/access state is observed. B1-P changes arrivals upstream while the downstream restriction remains fixed. A result therefore tests whether useful sensitivity survives the chain **meter → merge chronology → long-link propagation → fixed route-sensitive service**. That is a transfer/propagation question absent from the isolated green-allocation task.

The distinction is limited but real. B1-P does not establish a new local-access primitive: the same M3-owned exact-versus-relaxed service decision is reused at an unactuated point diverge.

## Minimum fair comparison ladder

| Rung | Information retained | Question it rules out |
|---|---|---|
| Destination-aware aggregate LTM/full FIFO | route totals/proportions, sending and receiving supply | Is ordinary route-aware first-order flow sufficient? |
| Partial-FIFO node | the above plus declared Wright-style mutual restriction | Is a calibrated aggregate blockage fraction sufficient? |
| FIFOQ/composition-memory aggregate | the above plus route-specific excess queue memory | Is the effect only delayed destination composition? |
| Carey-style time-cohort FIFO | route labels plus cell/link entry-time cohorts, but proportional mixture within a cohort | Is time-cohort resolution sufficient without exact within-cohort order? |
| Exact ordered continuous mass | realized route sequence/rank and eligibility profile | Does finer order change forward service, gradients, or downstream improvement? |
| Aggregate time-step refinement | repeat relevant aggregate/cohort rungs at finer time resolution | Is an apparent benefit merely a coarse time-discretization artifact? |

All rungs must use the same physical demands, route totals, merge quantities, supplies, action and objective accounting. A positive result against a memoryless aggregate alone is not sufficient. If refinement removes the difference, the correct finding is aggregate/cohort sufficiency at the required resolution.

## Minimum mechanism-isolating contrasts

- Hold coarse interval totals and route totals fixed while changing the within-interval order of through-bound and exit-bound mass.
- Use two admissible metering schedules that place the ramp cohort in different mainline gaps without any overlap at the merge.
- Include an unconstrained-exit neutral case in which order should not change total service.
- Include a constrained-exit case in which head composition can change short-horizon through service and total time.
- Include a time-step refinement/equivalence check and report whether the exact-order advantage survives.

These are formulation requirements, not executed experiments or assumed outcomes.

## Contract ownership and reopening consequences

- **No M1 G2 reopening is needed for B1-P** if non-overlap is enforced and verified for every tested action/scenario. M1's existing leading-time order is then unambiguous rather than being interpreted as physical resolution of overlap.
- **M1 G2 must be reopened** before admitting overlapping mainline/ramp eligibility profiles or making a general physical merge-order claim. The closed plan explicitly calls its whole-package overlap serialization behaviorally passive and nonphysical.
- **M3 remains the decision owner** for exact ordered versus bin/cohort-relaxed service and any lossy within-bin canonicalization. D1 identifies an experiment dependency; it does not approve that service operator.
- A realistic multilane exit-access region, lane anticipation, capacity drop, or dynamic lateral redistribution would require a separate common-physics review. It may not be hidden inside this point node.

## Source basis and limits

The source audit is in `../extraction/d1_mechanism_evidence.md`.

- Carey et al. directly distinguish proportional mixing, cell/link entry-time cohorts, and order-dependent diverge blocking, but do not define cross-input chronology for an overlapping merge.
- Wright et al. establish a first-order aggregate partial-FIFO alternative and explicitly expose the lane-geometry/weaving tradeoff.
- FIFOQ shows that aggregate route-composition memory can already cure important off-ramp artifacts.
- Boukhellouf et al. show that a deliberately elementary point diverge can be benchmarked in microscopic tools without discretionary lane changing, while warning that real multilane diverges are richer.
- Muñoz–Daganzo and Newell support the empirical/distributed-lane boundary, not the narrow mechanism's exact order claim.

Accordingly, B1-P is a credible proof-of-mechanism and gradient-transfer candidate, not an operational ramp-metering benchmark or evidence that selective order will outperform the strongest aggregates.

## Next gate

The user must choose whether to formulate B1-P, defer B1, or reopen the broader merge/common-physics question. The decision request is in `../reporting/d1_user_gate.md`. No RQ3–RQ5 formulation, implementation, simulation, or project-file amendment has begun.

