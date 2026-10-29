# AS1: unequal initial lane loads fit the existing traffic model

Date: 2026-10-19. **AS1 completed and user-accepted. Step 3 remains open.**
The user accepted this initialization/forward finding and directed continuation.
The exact amended contract below is now fixed for the dependent review.
AS2 has subsequently been user-accepted and AS3's action/full-gradient and
consistency review is delivered at the original Step 3 closure gate.
The mathematical and work/verification artifacts retain their delivery-time
status and are preserved.

[AS1 acceptance and AS2 authorization](vsl_as1_acceptance_and_as2_opening.md)

[Accepted AS2 information findings](vsl_as2_information_findings_and_checkpoint.md)

[Current AS3 findings and final Step 3 gate](vsl_as3_findings_and_step3_closure_gate.md)

The main finding is that **we can restore the intended A/B imbalance without
adding a traffic mechanism**. Each lane can remain homogeneous along its
length while carrying a different initial amount. The existing model already
treats adjacent A and far B differently: A supplies space for E to merge and
shares forced-merge service with E; B carries its own traffic past the drop.
Initial equality between A and B was a restriction on the chosen traffic
family, not a requirement of those mechanisms.

The amendment therefore changes the starting traffic, and counts its mass
correctly, while keeping the established preparation, terminal travel,
service sharing and recovery laws. The forward-model arguments survive
under their existing sufficient bounds. The important qualification is that
this does **not** establish an information advantage or better VSL advice.
Those are the next two review blocks.

## What changes at the root

Initialize E, A and B independently on the same uniform footprint. Total
traffic is the sum of the three actual lane populations. The load competing
for adjacent receiving is E plus A, while B must separately fit its own
service. In particular, B is no longer inferred by setting it equal to A.

For the central comparison, keep E traffic, combined A+B traffic, geometry
and physical coefficients fixed. Shift some continuing traffic from B to A
or back again. Total traffic and its free-travel contribution to TST are
unchanged. What can change is the space available to early E merging and the
arrival mix presented to the shared point service.

The existing load and storage bounds still apply to **each** candidate
split. We have not admitted arbitrary imbalance at arbitrary loading. The
terminal and recovery account still start empty, the cohort is finite,
there are no postdecision arrivals, and advice is one common constant value.
The full formulas, units and split restrictions are in the supporting PDF.

## What the review establishes

| Part of the model | Direct finding and traffic meaning |
|---|---|
| **Homogeneous preparation** | **Independent A/B loads are compatible.** Early transfer conserves E+A. Its receiving limit uses A's actual load; B need not equal A. Each remaining lane body can stay uniform along its length. |
| **Travel and handoff** | **The existing lane-specific arrivals remain valid.** Prepared E and A enter the terminal according to their own current densities; B enters at its independently initialized density. No new cells, lane changes or travel clock are needed. |
| **Finite storage** | **The same conservative protection still works.** Counting all three lane populations gives a total smaller than one terminal lane's storage, so none of the lane entrances blocks the homogeneous preparation in this admitted domain. This does not establish general spillback behavior. |
| **Forced service and recovery** | **The selected laws remain well-defined.** Their root, service and positive-budget bounds depend on current A/E flows, marks and recovery history, not initial A/B equality. B retains independent unqueued passage under its own bound. |
| **Queue events and clearance** | **The accepted complete-forward argument transfers.** E offers still decrease and A offers increase through the single pulse. The same compatible queue tests and event-separation bound give unique causal continuation and finite clearance for every allowed advice. |
| **Conservation and TST** | **Both remain complete after correcting total mass.** The travel term counts the initial positions of all three lane populations; the waiting term counts A and E delays. Completion stays at the choke. |
| **Existence of the intended traffic contrast** | **A genuinely unequal family is admitted.** An exact example keeps E and A+B fixed while swapping A/B crowding. One endpoint has enough adjacent service for every early offer; the other initially limits early merging by receiving. |
| **Information, decisions and gradients** | **These are not settled by AS1.** Local service can differ, but permitted history may reveal the split, and distinct traffic predictions may still favor the same advice. Those questions belong to AS2 and AS3. |

The forward conclusion is an extension of the accepted conditional proof,
with its assumptions checked component by component. It is not a new general
theorem for arbitrary traffic inputs, nor independent empirical validation.

## A concrete way to picture the contrast

Use common density units. Both preparations start with **0.60 units in E**
and **0.55 units across the continuing lanes**. In one, A has 0.20 and B
0.35; in the other, A has 0.35 and B 0.20. The ending lane and the continuing
total look identical at initialization, while the adjacent lane is more
crowded in the second preparation.

For one exact shared choice of the retained physical scales, at the highest
advice the ending traffic offers 1.20 flow units in both preparations. The
available receiving alternative is 1.30 in the first and 1.15 in the second.
The actual early transfer therefore starts at 1.20 and 1.15 respectively.
The actual density-transfer rate also includes the same preparation-length
factor in both cases. Strict inequalities make the difference persist over
a positive initial progress interval.

This is a static analytical example, not a traffic run or a recommended
calibration. It proves that the restored split can matter inside the
existing laws. It does not yet give a matched predecision history, a complete
TST comparison, an optimal-advice split or a gradient-usefulness result.

## What this checkpoint closes, and what follows

The exact amendment removes initial A/B equality, uses independent lane
loads and their actual total mass, and retains the existing sufficient
admission conditions and traffic laws. **No new modeling choice was needed
to complete AS1.** The user has accepted this qualified forward contract
as the input to AS2. This does not close the original Step 3.

AS2 will next ask whether the E-plus-continuing-total rival can distinguish
these initial splits from all its permitted observations and history. It
must be allowed to infer A where the available record permits that; it is
not forced to assume equal continuing lanes. An initial-state-dependent
E+A load cannot be supplied as a common parameter if that leaks the hidden
split. The compact rival with an additional adjacent-lane statistic remains
part of that comparison. The subsequent AS2 delivery is linked above.

The old ending-only reconstruction and symmetric action examples remain
valid within their original restricted family. They do not answer the new
Level 2-to-Level 3 question. Applied physical admission remains open, SUMO
optional, Step 4 unopened, and the ramp/urban lines closed. No traffic or
gradient experiment, simulator implementation or installation was performed.

[Exact amended contract and forward argument, PDF](../../synthesis/research_readiness/vsl_as1_asymmetric_forward_contract.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_as1_asymmetric_forward_contract.tex)

[Component and proof dependency map](../../extraction/research_readiness/vsl_as1_initialization_proof_map.md)

[Bounded AS1–AS3 plan](vsl_ab_asymmetry_requalification_plan.md)

[Work, exact checks and preservation record](vsl_as1_review_work_report.md)
