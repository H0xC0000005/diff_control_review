# BP-R — task, reduction and response assessment

Date: 2026-10-06. E1–E3 complete as a bounded source/static audit.
[Primary evidence and access limits](../../../extraction/rm12/bp_r/primary_source_audit.md)
are authoritative for source claims. Everything below is reviewer synthesis or
a conditional comparison obligation, not a newly adopted physical model.

## Semantic result and candidate boundary

**The family worth retaining is a local active merge whose discharge responds
to the entry and acceleration of merging traffic.** Metering changes actual entry;
entry affects disturbances and their evolution; those disturbances can change
exit timing. This is a physical control route beyond merely relocating queues.
It is a source-supported family lead, not an approved set of task equations.

The potential retained detail is the evolving disturbance associated with
merging/accelerating traffic: its location, speed/recovery status and interaction
with nearby traffic. We do not yet know whether lane/cohort order is required,
or a small continuous statistic and memory is adequate. The purpose is to find
the least representation that preserves the decision response, not assume that
discrete identity must survive.

A semantic example: a meter holds some ramp traffic, so fewer slow entrants
disturb a busy mainline now. The road may then discharge traffic more effectively,
but held ramp traffic also accumulates waiting. Whether the balance is favorable
depends on the entire subsequent exit history. A compact model that correctly
predicts this balance is an acceptable result. This example describes the
question; it is not a constructed positive scenario or a prescribed policy.

## E1 — control leverage and full task transfer

| Chain link | Disposition | What a concrete task still needs |
|---|---|---|
| Permission rate → actual ramp release | Supported as a source modeling/control concept | Source permission, queue and feasible release must be distinguished; empty ramp and rate saturation must be handled conservatively. |
| Release → actual merge entry | Source-dependent, incompletely transferable | A point-ramp rule and a ramp travel/receiving process are different mappings. Do not equate them silently. |
| Entry/traffic regime → changing discharge | Physical family support | Choose and qualify a particular endogenous law/reference; do not combine unrelated sources as one validated mechanism. |
| Discharge → complete exit history | Necessary causal route, not yet a matched certificate | Include approach/merge/downstream travel, receiving limitations and every overflow/entrance queue. |
| Exit history → all-stream TST through clearance | Inherited accounting requirement | Fixed common finite demand/population, common initial traffic and full tail accounting. Source steady discharge and terminal throughput are insufficient. |
| Useful common rate variation | Plausible, not established for the exact task | At least one feasible nontrivial action regime must remain after counting holding costs; do not assume minimum/maximum rate is or is not universally best. |

**E1 disposition:** positive physical rate/discharge lead; **partial**, not a
completed finite-storage, finite-cleared, all-stream-TST task admission. The
fixed-service queue-relocation obstruction is not universal to this family.
Neither field discharge recovery nor a congestion-memory controller gain proves
the required complete objective benefit.

If two schedules have identical complete cumulative exit histories for the same
arrivals/initial population, their complete system times agree regardless of
where queues sit. If histories differ, equality no longer follows, but useful
rate decisions still need assessment. Different endpoint exit totals, mean
capacities or intermediate queue locations alone do not decide the question.

## E2 — the strong competitors must remain live

These are evidence-backed families or explicitly labeled proposed comparison
interfaces. They are not an automatically compatible hierarchy of equations.

| Family / role | Retained state and independent update | Strength | Unresolved qualification |
|---|---|---|---|
| Spatial ACTM-style aggregate; accounting/receiving anchor (RM0001) | Road-section mass, ramp inventory, constrained flows and storage/allocation | Captures travel, spatial congestion, ramp holding and receiving limits; rules out a weak one-number baseline | Its source law is not an exact reduction of the richer merge family; fixed capacity does not establish disturbance dynamics. |
| CTM with congestion memory (RM0003) | Section density/inventory and a retained congested/decongested mode | Captures different service after different congestion histories without lane identity | Thresholds, joint receiving, finite storage and mode initialization must be qualified for the selected task. Exact for its own law, not proven exact for the physical reference. |
| Endogenous mean/moment capacity (RM10-P01, S12A005) | Entry regime, traffic parameters and insertion statistics supplied by a declared model/interface | Captures disturbance effects on mean service without retaining every vehicle | Mean/steady closure is not automatically a dynamic transient closure. Current inputs must be independently modeled; do not feed reference-derived future moments into the rival. |
| Lane-aggregate spatial/capacity family (RM10-P02) | Per-lane aggregate quantities, lateral-flow/capacity coupling | Retains lane contrast while discarding individual identity; a serious competitor to ordered cohorts | Source mean-capacity partition is not a completed dynamic rate/TST law. A lane-aggregate rival cannot be described as lane-blind. |
| Compact evolving disturbance statistic; **reviewer interface candidate only** | Conserving traffic state plus a proposed speed/recovery/moment state evolving from common inputs | Could preserve the relevant memory with continuous mass and few extra variables | No closed sufficient statistic or update law has been proved here. An exponential recovery term is not inferred or adopted from the source particles. |
| Lane-stream/accelerating-event hybrid; richer reference lead (RM8-P01/RM0011) | Lane stream fields plus evolving accelerating obstructions | Direct physical mechanism and discharge evidence | Source discrete event generation, sampling, priority and geometry are reference-transfer issues. It is not already an approved continuous-mass simulator or gradient reference. |

There is no justification for challenging only a memoryless fixed-capacity
aggregate. Equally, a compact model's mean-capacity success does not demonstrate
all action-response fidelity. The comparison must identify precisely which
closure is challenged and what it retains.

## Fair initialization, projections and memory

For a future BP-R formulation, one physical initial state and common forcing
define the scenario. The richer model receives its declared initial state; each
reduction receives the stated projection, including any admitted lane totals,
moments, congestion mode or other initial memory. All controllers may know the
same declared physical scenario. A reduction is a restriction on its independent
state/update representation, not a claim that the initializer secretly withheld
facts from its controller.

Any estimator, retained earlier record or compression procedure must be declared
and available on the same terms. If a purported reduction simply reruns the
fine model, then it has retained that representation elsewhere. If it receives
fine-state corrections after every action, the test measures an oracle-assisted
predictor. Neither settles independent compact closure. Parameters and scenario
selection likewise cannot be fitted separately to each tested intervention using
the reference's future response. These are comparison obligations, not assumed
restrictions on real operational sensing.

This is why the earlier deterministic-information theorem remains true without
closing BP-R. Complete initial knowledge can determine the true future while a
chosen compressed model predicts it inadequately. A bad compression does not
prove that useful information is unknown, or that all compressions fail.

## E3 — what survives a common-rate comparison?

| Evidence level | Current status | What it cannot yet establish |
|---|---|---|
| Physical disturbance/service mechanism | Supported at family level | Minimum retained representation |
| A weak closure omitting a genuine mode/mechanism can fail | Supported in source-specific settings | Failure of a strong compact or lane-macro reduction |
| Similar mean service can coexist with different transients | Supplementary forward evidence | Same-public-initialization, same-rate response or different complete TST; equality of full observation history |
| Independent strong reductions predict a different response to the same rate change | **Unestablished for a matched admitted local task** | No source controller comparison is substituted for this claim |
| Difference changes useful complete-TST action ranking/direction | **Unestablished** | A discharge difference may be irrelevant or correctly captured by a compact refinement |
| Correct and independently useful gradients | **Not reviewed/validated at this stage** | Differentiability, an adjoint or internal optimization alone is insufficient |

In particular, the queued/unqueued comparison does not eliminate a rival that
already retains ramp queue and entry speed. The transient evidence does not
eliminate a dynamic memory/moment rival that was never tested against it. There
is no theorem here that every aggregate closure is sufficient; there is also
no certificate that lane/cohort/identity detail is indispensable.

## Disposition and smallest successor

**Partial family support with an evidence-limited joined task/comparison.** E1
supports the physical route; E2 produces qualified rivals and state/projection
obligations; E3 does not admit a completed control-relevant reduction distinction.
This is neither a positive hidden-information study nor a universal scoped-to-all-
models negative. No new law is adopted, so BPR-G2 is not triggered.

If continued, the smallest successor is **one bounded Stage 3 formulation bridge**:
first qualify a single local rate-controlled family under finite receiving/storage
and complete TST; then state its strong reduction comparisons. Resolve reference
events versus continuous-mass task semantics explicitly before adopting a law.
If no coherent bridge survives, stop; do not invent extra lanes, private stochastic
realizations or a favorable capacity law to guarantee a result. If a compact
closure suffices, record that as a valid research outcome. Stage 4 remains
conditional and unopened.
