# RM9.20 — First compact-state audit and finite-merge gate

Date: 2026-10-01. Status: **Historical first audit; RM9-UG1 subsequently closed with A approved as Default.**

Current continuation and pending RM9-UG2 are in the
[latest findings](rm9_30_allocator_contract_and_control_chain.md). The candidate
inventory below preserves the first-gate reasoning, not an unresolved UG1.

## Findings

Candidate A has progressed beyond family admission. The source/analytic audit
established three constraints on any defensible formulation:

1. Combining several inner lanes into one rest group preserves mass but does not
   generally supply closed dynamics. Adjacent-lane receiving/incentives can differ
   at the same group totals. A two-physical-lane case avoids that particular
   aggregation, while equivalent scalar or observable reconstruction remains valid.
2. Lane contrast is not automatically hidden. On explicitly stated free-flow
   observation maps, known different lane speeds plus road-total density/flow,
   and sometimes an independent speed statistic, can identify the split. This
   is a conditional identifiability result, not universal aggregate sufficiency.
3. Merely moving waiting between ramp and mainline gives no all-stream total-time
   benefit if complete departure history is unchanged. A useful action/gradient
   must affect actual departure timing/service or another approved outcome.

Read the [mathematical audit PDF](../synthesis/rm9/rm9_compact_state_and_observer_audit.pdf)
and [source/claim audit](../extraction/rm9_source_and_claim_audit.md) for assumptions,
proofs and exact limits. No feasible identical-history/action certificate, adopted
compact law, verified candidate gradient or independent useful gradient is yet
established. The conditional results do not refute the approved family.

The first blocking formulation decision is shared receiving allocation.
The [ramp source](https://repository.tudelft.nl/file/File_3728cefd-b910-49de-a341-d342fbbd5369)
prioritizes ramp entry and excludes mainline spillback onto the ramp. The
[node source](https://doi.org/10.1016/j.trb.2017.09.001) supports explicit priorities
and unused-supply redistribution, and cautions against demand-dependent priority
under nodal invariance. Neither finite capacity alone nor the separate VSL batch
law resolves this choice.

## RM9-UG1 — how should competing flows share finite merge receiving?

**Classification and ownership:** Type 2 review-global, user adoption. Affects
RM9-G2 and dependent G3/G4. The approved single-ramp open-loop action and strong
history/accounting contracts stay fixed. This is a new allocation-law choice,
not a reapproval of RM8 Candidate A.

**Problem statement:** When the ramp and mainline want more than the receiving
lane can accept, what rule gives their realized flows while respecting both
donor availability and the shared receiving limit?

**Assumed model-chain function:** The open-loop meter limits the ramp offer.
A merge allocator converts that offer and local mainline/lateral offers into
realized flows. Rejected traffic remains waiting; accepted traffic changes
receiving state, redistribution, departure timing and the objective.

**Core gap:** The admitted family does not choose this allocator. A published
ramp-priority assumption has a restricted domain; source branch/budget details
need a separate consistency audit. Giving all entrants a demand-proportional
share may look neutral, but is not automatically a valid first-order traffic
node. The choice can change queues and gradient signs, so it needs an explicit
contract before a closed forward map can be formulated.

### Candidate A — demand-independent priorities with unused-supply redistribution (recommended)

Use a standard first-order merge allocation family: fixed positive priorities
attached to physical entering streams, independent of current offers and meter
rate. When an input cannot use its allotted share, redistribute that supply to
other eligible inputs. Every realized flow respects donor demand and the shared
receiver budget. At a multilane interface, represent all conflicting lateral/
longitudinal/ramp transfers jointly or prove the split update uses one budget.

Review priorities as declared structural parameters, potentially linked to
physical capacities; do not select numerical values to obtain an action reversal.
No equal-priority or calibrated ratio is frozen by choosing the family.
The source is RM0018's explicit-priority framework; the eventual local coupling
and compact representation still require transcription and audit.

**Pros:** Has a clear literature basis and conservation/receiving contract.
Separates scarcity allocation from current demand manipulation. Supports
piecewise sensitivity analysis while leaving a genuine possibility of aggregate
or scalar sufficiency. Avoids guaranteed entry beyond receiving.

**Cons:** Priority ratios may be site dependent; the source does not calibrate
them for the proposed task. A node law alone does not model acceleration-related
capacity loss or establish hidden-state/action relevance. Multilane coupling and
source branch issues remain to be resolved before an exact model is admitted.

**Dependencies and scientific consequence:** Freeze the family first, then
jointly audit lane flows/receiving/storage and observer functions. Hold the same
priorities across comparisons. A positive result must not depend solely on one
chosen priority ratio or an imposed lane-service penalty. No richer simulator or
production adoption follows from approval.

### Candidate B — explicit finite-receiving ramp preference

Give ramp traffic preferential service, but cap it by permitted demand and
actual receiving; the mainline takes remaining supply. When the ramp cannot use
supply, the mainline may use it. Specify a bounded priority ratio or lexicographic
ramp preference explicitly rather than assume every meter release can enter.
This retains a close semantic relation to RM0004's ramp-focused setting while
making rejected ramp mass and its finite storage visible.

**Pros:** Keeps a recognizable local-ramp service interpretation and lets the
review inspect whether preferential metering itself exposes the proposed effect.
Can have a simple piecewise forward structure with clear inactive-rate cases.
Finite receiving still allows ramp blockage when physical service is exhausted.

**Cons:** Preferences can shift congestion to the mainline; published
always-accepted-ramp results do not validate this bounded adaptation. Strong
preference may suppress the very ramp-receiving sensitivity being sought.
Full departure accounting remains necessary to distinguish benefit from queue
relocation. No universal field-valid preference is established.

**Dependencies and scientific consequence:** Treat this as a specified traffic
allocation assumption shared by all models, not additional control. Fixed-ratio
preference is a restricted case of A; lexicographic preference is a substantive
boundary case. Diagnose priority-dependent results and retain all mass when
receiving or ramp storage binds.

### Candidate C — deliberately stylized proportional-cohort allocation

Define a local finite cohort/batch interaction and allocate its available
service proportionally to represented stream mass or offers, with a separately
specified exposure/clearance rule. This can be analytically tractable and close
to the accepted VSL proof style. Its semantics must explicitly be a finite-cohort
analytical adaptation, rather than claim to inherit a standard continuous-flow
merge node or a field-calibrated ramp law.

**Pros:** Provides a transparent model for isolating information and accounting;
may enable a small conditional analytical certificate with few event branches.
Can serve as a proof kernel before a later traffic-model validity review.

**Cons:** Demand-proportional node allocation has an invariance warning in the
standard first-order framework. A batch kernel alone need not represent
continuing ramp arrivals, queue formation or merging capacity. A constructed
positive result would have a narrower physical-evidence claim and need explicit
extension/ablation support before becoming a research-ready ramp task.

**Dependencies and scientific consequence:** Requires approval of a new
cohort/exposure law and a narrower claim, while preserving complete accounting
and the strong observer. It cannot silently replace the current operational
finite-ramp formulation. It does not modify or invalidate the closed VSL result.

**Provisional recommendation: A.** The methodological priority is a lawful,
source-backed allocation. Keep priority parameters explicit, then test state
sufficiency and useful actions instead of engineering a hidden-state certificate
through symmetry, mixing or arbitrary service penalties. B is viable if ramp
preference is the intended physical assumption; C is a defensible but more
restricted analytical task requiring a declared scope change.


## Original stop and subsequent disposition

This audit originally stopped at RM9-UG1. The user subsequently approved A as
Default and instructed continuation. That closes UG1 without closing RM9 or
approving complete lane equations. The [approval record](../discussion/rm9_allocator_a_approval_and_continuation.md)
and [new findings/gate](rm9_30_allocator_contract_and_control_chain.md) supersede
this document as current instructions. Historical alternatives remain above;
the closed VSL result and multi-ramp deferral remain unchanged.
