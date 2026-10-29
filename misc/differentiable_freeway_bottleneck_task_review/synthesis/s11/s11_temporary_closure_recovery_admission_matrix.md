# S11 temporary-closure recovery admission matrix

Date: 2026-09-30. Status: **closed; G4-A approved and TCR-E accepted at
[S11-UG1 / TCR-R1](../../reporting/s11/s11_20_temporary_closure_recovery_admission_findings_and_gate.md).**
Source basis: [S11 source audit](../../extraction/s11_temporary_closure_recovery_source_audit.md).

## Approved task boundary

- Removable one-lane obstruction on an otherwise three-lane homogeneous freeway.
- Fixed closure/reopening schedule and lane-uniform upstream infrastructure VSL.
- Same demand, routes, population, event schedule and known inputs.
- Strong spatial aggregate state plus full predecision history for the comparator.
- Candidate hidden bundle: lane allocation, gaps, order, leaders and lane-change
  memory; no presumption that lane occupancy alone is sufficient.
- Metric roles reviewed as a set under complete affected-demand accounting.

## Causal-chain audit

| Link | Best supporting evidence | What is still missing | Result under G4-A |
|---|---|---|---|
| Event → recovery phase | FB0021 restores capacity after a non-recurrent event and counts complete clearance; S11-S1 observes 2–5 minute abrupt and 12–30+ minute gradual post-clearance recovery. | None for existence/accounting. | Pass. |
| Common VSL → arrivals | Established in the prior VSL corpus and FB0021's aggregate sensitivity. | Exact voluntary-response law remains a later protocol detail. | Pass for admission. |
| Common VSL → lane preparation | S06-S2 reports VSL-associated lane redistribution near merges; S11-S2's calibrated work-zone simulation reports different lane-change counts across VSL algorithms. | No direct fixed-reopening field result; causal mediation by lane changes is not isolated. | Qualified pass. |
| Lane/gap/order → transient service | S11-S3 associates lane changes, relaxation and waves with recovery discharge; S11-S4 identifies relational gap creation; S11-S1 documents lane-resolved transient post-clearance flow. | No single source links state at fixed reopening to subsequent receiving/discharge. | Partial, transferred across contexts. |
| Hidden state survives strong aggregate history | The relational variables in S11-S4 are finer than ordinary total density/flow/speed. | No exact-history collision, observer residual test or sufficiency result. Aggregate history may encode the consequential wave/queue state. | Unresolved. |
| Transient service → useful action distinction | Complete-clearance accounting is available from FB0021 and metric guidance. | No same-history common-action ranking, sign guarantee or full action-set comparison. | Fail/unresolved. |
| Decision distinction → useful gradient | Fixed-time reopening permits piecewise analysis in principle. | No admitted decision distinction, lane-aware derivative, boundary robustness or independent downstream improvement. | Not reached. |

## Reapplication of the S05 obstruction

Let reopening restore a service law determined only by the shared aggregate
queue/state, event schedule and known capacity. If common advice changes only
arrival time or queue placement, complete all-cohort accounting retains the S05
arrival-dominance problem: the review has no reason for slower advice to become a
better action.

The literature suggests a possible escape only if advice changes lane-changing
preparation and the resulting relational state changes transient service. The
individual premises are plausible, but the joint term is not identified for the
S11 domain and its sign is not fixed: a lane change can briefly increase measured
flow while its disturbance later creates waves and reduces discharge. Assigning
a favorable state-dependent recovery capacity would therefore assume the result.

## Strong-observer audit

| Observer issue | Finding | Consequence |
|---|---|---|
| Spatial aggregate queue, speed, density and cumulative counts | These can represent queue size, wave propagation, restored capacity and recovery history. | A memoryless aggregate comparator remains inadmissible. |
| Lane allocation and lane-change activity | Not generally reconstructible from one contemporaneous link total, but may leave signatures in full spatial speed/flow history. | Plausible hidden information is not an exact information-loss certificate. |
| Gaps, leaders and lane-change memory | S11-S4 shows response depends on relational variables finer than aggregate totals. | Their independent effect after conditioning on strong history is untested. |
| Unknown inputs/heterogeneity | Driver response, compliance and event operations can mimic hidden-state residuals. | A later test would need identical inputs or an explicit uncertainty contract. |

The exact strong-history question remains coherent but unresolved. S11 provides
no basis for weakening it to an approximate observer.

## Metric-role audit under G3-A

| Candidate | Evidence-supported role | Main strength | Failure mode / guardrail |
|---|---|---|---|
| All-cohort total system time or total delay through common clearance | **Recommended primary decision metric for a later protocol.** FB0021 uses complete recovery-tail delay; work-zone studies value travel-time/delay effects. | Covers event and recovery costs across the affected cohort and supports welfare comparison. | A long horizon can dilute a localized mechanism; report recovery decomposition. |
| Queue-clearance time or queue duration | **Recommended secondary operational metric.** Incident/work-zone sources treat recovery duration as operationally meaningful. | Sensitive to recovery and easy to interpret. | Can improve by shifting waiting to the source or outside the measured queue; pair with total delay. |
| Time-resolved post-reopening discharge/throughput | **Recommended mechanism diagnostic.** S11-S1/S3 measure transient discharge changes. | Locates and signs the proposed service mechanism. | Short windows can reward temporary surges or exclude unfinished traffic; do not use alone for useful-control value. |
| Queue length and residual/unfinished demand | **Required guardrail and diagnostic.** FHWA guidance treats queue length separately from delay. | Exposes horizon truncation, spillback and queue relocation. | A shorter queue alone need not mean less total cost. |
| Mean speed and speed variance | Supporting operational/safety diagnostics. | Common in VSL evaluations and useful for response/compliance checks. | Can improve while delay or completion worsens. |
| Lane-change count/distribution | Mechanism diagnostic, not a target. | Tests whether advice reaches the proposed hidden-state channel. | Fewer lane changes are not automatically better and do not prove causality. |

This role assignment is an S11 evidence recommendation for user review at
TCR-R1. It is not an experimental objective freeze.

## Derivative-regime classification

| Regime | Expected derivative status | Review implication |
|---|---|---|
| Fixed reopening time; continuous lane-resolved state; smooth service closure; unchanged active set | Ordinary chain rule through two time regimes is plausible. | Reopening itself need not block gradients. |
| Continuous sending/receiving with min/max constraints or queue-clearance event time | Piecewise or directional derivative; stable away from ties and switching surfaces. | Later checks must report active sets and perturb away from boundaries. Clearance time needs event-time sensitivity care. |
| Hard lane permissions with discrete lane assignment, lane-change acceptance, leader/order switches or exact queue-emptying changes | Hybrid/nonsmooth and possibly discontinuous response. | Pathwise AD can be undefined, one-sided or uninformative; smoothing would be a methodological choice requiring approval. |
| Fixed terminal horizon with residual cost | Easier differentiability than stopping exactly at clearance, provided the residual is conservative. | Useful as a later numerical formulation, but it does not repair absent decision relevance. |

No combined gradient claim is admitted because the decision path is not admitted.

## G4 verdict map

| G4 choice | Meaning applied to current evidence | S11 result | Consequence |
|---|---|---|---|
| **A — mechanism-and-obstruction screen (working default)** | Require source-supported links without assuming the critical transfer and retain the strong-history question. | **TCR-E — evidence inconclusive.** The reopening-specific state-to-service and observer links remain missing. | Close Option 3 at admission unless new direct evidence is supplied. Candidate B analytical screen remains separately meaningful because it explicitly constructs the missing service coupling rather than claiming it from reopening evidence. |
| B — complete certificate in S11 | Require a proved/observed matched pair and useful action distinction now. | Not satisfied; also exceeds approved task-admission scope. | Close/defer with an even stronger unmet burden. |
| C — composed cross-context hypothesis | Accept adjacent sources as sufficient motivation for a protocol that tests the missing transfer. | Admit a later full protocol as a hypothesis test, not as an evidence-supported path. | Requires explicit relaxation of G4-A and pre-registration that the crucial service/observer links are unproved. |

## Final S11 conclusion

Under the user's approved G4-A, Option 3 receives **TCR-E**. Recovery is a
valid and potentially resolution-sensitive scenario, but the reviewed evidence
does not support the full hidden-information-to-useful-VSL-decision chain. The
negative result is localized: it does not show that lane/gap/order never matters,
and it does not invalidate the analytical Candidate B branch. The user accepted
this result and closed S11.
