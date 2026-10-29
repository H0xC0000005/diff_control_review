# BP-R Stage 3 — S3-G2-N: allocation at the mandatory merge

Date: 2026-10-06. **Closed by user approval: S3-G2-N.A.** Reference S3-G2.A and
upstream-admission S3-G2-M.A remain approved. The supplied originals qualify CM
and local IT. See [source audit](../../../extraction/rm12/bp_r_stage3/supplied_originals_audit.md)
and [equations/static examples](../../../synthesis/rm12/bp_r_stage3/source_laws_and_merge_choices.pdf).

## Problem statement

When ramp and mainline traffic simultaneously want the same receiving lane,
how should its finite receiving be divided? This selects service allocation;
it does not move the meter, command merge speed/gaps, or add a capacity penalty.

**Ownership:** Type 2/user, S3-G2-N, depends on G1/G2.A/G2-M.A and source E1.
Mixed split: E1.N is Type 1/reviewer source/operator qualification; E2.N is
Type 1/reviewer transcription after selection. E3 comparisons and E4 control/
clearance audit depend on N. Reopen N if transcription needs variable/optimized
priority, violates shared receiving or changes its physical meaning.

## Assumed model-chain function

Upstream permission changes admission into the finite KW ramp. Propagation
determines available merge traffic and donor speed. The node awards receiving;
actual entry generates accelerating disturbances, which affect later traffic,
exits and complete TST. Allocation therefore helps determine control response.

At the shoulder-lane receiver, the non-ramp group includes mainline through
demand and compatible lateral demands at that interface. All share the same
receiving budget. Within that group, use the journal's incoming-demand
proportions. Other lanes retain local IT. This grouping is an explicit task
adaptation, not a theorem for arbitrary networks.

## Core gap

The supplied journal specifies local lane-flow allocation; the 1997 paper
proves its special-lane/class construction. Neither uniquely fixes the merge
manuscript's mandatory-entry priority adjustment. The third paper would be needed
for that *exact* reproduction, but the user declares it unavailable and directs
continuation without further retrieval. An accessible original CTM merge rule permits
a defensible adaptation. Adopting either candidate below changes traffic
evolution and cannot be inferred from source access alone.

## Common contract

Use continuous sending demands and the same receiving, restricted by currently
active moving constraints. Serve all demand when it fits; otherwise allocate
the receiving once. Pair every transfer's donor debit and receiver credit.
Descriptor counts do not add population. Preserve donor demand limits and
include every compatible incoming movement in the budget. Do not subtract an
arbitrary new acceleration penalty or give each stream full receiving separately.

These are source-grounded *task adaptations*, not established full-task
validation. Event generation follows actual transfer/donor traffic, not the
upstream command. Coupled numerical scheduling remains dependent transcription;
event derivatives and solver degeneracies remain later questions.

## A — fixed junction priority; reallocate unused shares (recommended)

Give the ramp a fixed share of contested receiving. When both streams can use
their shares, serve them; when one lacks demand, the other uses the remainder.
The share is a physical task parameter strictly between zero and one, common
to all models and rate schedules. It is not optimized or refit per intervention.
Its eventual value/range needs disclosed task evidence and robustness review;
the source manuscript's 40% adjustment does not specify it.

Direct basis: Daganzo's [1994 original, Section 3.2](https://escholarship.org/content/qt9pz309w7/qt9pz309w7.pdf).
Applying it to the continuum–particle receiver and grouping other incoming
movements is the proposed adaptation; the PDF states the operator.

**Pros:** direct merge-specific original support; explicit junction priority,
finite receiving and unused-share reallocation; keeps the closest merge
manuscript's qualitative priority intent without inventing its calibration;
separates physical preference from the meter's admitted demand.

Physical motivation: geometry, lane access and merging/right-of-way behavior
can support an approximately stable contested share over the chosen operating
conditions. Geometry alone does not determine its value. Geometry can also
affect total receiving and individual sending capacities, which are distinct
from the allocation share. Fixed priority is a declared approximation, not a
universal geometry-only law or a requirement that both approaches be saturated.

**Cons:** adds one declared priority parameter; joined physical/control behavior
is not reproduced source validation. That parameter can affect ramp congestion,
entry speeds and disturbances, so it must remain common and inspectable.

**Dependency/consequence:** approve the fixed-priority family, then bind its
receiving, update and event interfaces. Numeric settings need provenance and
cannot be chosen to guarantee favorable representation results.

## B — share in proportion to current incoming demand

Extend the journal's target-cell proportional allocation pattern to the mandatory
node. Under excess demand, each group gets its fraction of total incoming
demand; otherwise all demand advances. No independent priority parameter is
introduced. This is a mandatory-node extension of verified local IT, not the
1997 paper's proven general-junction solution.

**Pros:** consistent allocation pattern across the reference's local receivers;
no additional fixed share; continuous conservation and full use of available
receiving; a clean alternative when demand-based sharing suits the physical task.

**Cons:** contested shares follow available sending demands rather than a
separately specified junction preference. When those demands change, metering
can change both arriving traffic and its service fraction, which changes
mechanism interpretation. Queuing alone does not imply changing shares: if both
sending demands remain at fixed capacities, B gives a fixed capacity-proportional
share. This also does not reproduce the manuscript's exact priority adjustment.

**Dependency/consequence:** approve the mandatory-node extension and use it
in all models. Comparing B with A is an allocation-family ablation, rather
than varying one physical parameter inside A.

## Fair semantic comparison

Hand operator evaluations, not traffic simulations: receiving is 100 units
in one interval and each group wants 90. A with an illustrative ramp share
of 30% serves 30 ramp/70 mainline; B serves 50/50. If instead mainline wants
20 and ramp wants 90, A serves 80 ramp/20 mainline; B serves about 81.82 ramp/
18.18 mainline. Both use 100; different traffic waits. If total demand fits,
both serve every demand. The 30% example is not a recommended calibration.

| Aspect | A: fixed priority | B: demand proportional |
|---|---|---|
| Contested share | Fixed physical preference until demand exhaustion | Current demand ratio |
| Spare receiving | Reallocated | Full receiving used when demand is sufficient |
| Additional commitment | One fixed share | Demand-based allocation assumption |
| Closest direct evidence | Original CTM merge construction | Journal local IT pattern, extended to mandatory node |
| Meter may alter | Admission, queue and disturbance states | Those states plus contested demand fraction |
| Proven full-TST benefit / useful gradient | No | No |

## Saturation, receiving and the interpretation of A/B

The user proposes A as geometry-driven sharing when approaches are saturated,
and B as proportional sharing when individually unsaturated demands together
exceed downstream service. The first is a useful physical motivation; the
second is a possible traffic case, not B's exclusive or established preferred
domain. Both laws operate whenever combined sending demand exceeds the shared
receiving, whether the restriction is local merge capacity or downstream
congestion, and whether one or both approaches queue.

Distinguish offered arrivals, current sending demand and actual served flow.
B uses current sending demand: what the approaches can offer before shared
receiving is allocated. It cannot use its own realized flow as the input ratio.
Each approach's saturation relative to its own sending capacity does not
determine whether the combined demand exceeds receiving.

With both approaches pinned to fixed sending capacities, B also gives a fixed
ratio. If A's priority matches that ratio, A and B coincide in that regime;
they need not coincide when demand falls on one side. When combined demand
fits receiving, both serve all demand. Thus A/B is a choice of competition law
under scarcity, not a prescribed switch between saturated and unsaturated
traffic. No evidence in the current sources selects B solely because a
bottleneck is farther downstream. No new regime-switching rule is proposed.

This clarification corrects B's earlier overly broad suggestion of varying
shares during any queued interval. The subsequent user instruction approves A.
B remains unselected, not established as universally unrealistic: both laws
are constrained by physical sending and receiving. The selected approximation
is an explicit stable junction preference, not a geometry-only theorem.

**Approved choice: A.** It has direct merge-specific primary support
and makes priority explicit. B is viable under a different allocation assumption.
Neither is preferred on runtime or a promised positive result. Exact reproduction
of the missing third source remains a separate evidence condition; fetching it
is not required to discuss these alternatives.

## Status and next allowed action

**S3-G2-N.A is approved and closed.** The user chooses fixed priority and
unused-share reallocation, declares the third paper unavailable despite renewed
institutional access attempts, and authorizes continuation. No further retrieval
is required. Exact reproduction of that source's calibration is out of this
pass; no value of priority is inferred from its reported 40% adjustment.

The authorized continuation has now completed its bounded source/static audit.
See the [post-priority findings and S3-G3 disposition](post_priority_findings_and_disposition.md):
the core is source-grounded, but complete reference/clearance and strong compact
transient contracts remain partial. Stage 3 awaits user disposition; Stage 4,
experiments and development remain unopened.
