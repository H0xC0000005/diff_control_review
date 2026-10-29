# T1 — what a compact disturbance memory can and cannot yet do

Date: 2026-10-07. **Bounded qualification completed; partial support, no adopted compact law.**
Authorization: [continuation 63](../../../rm12_63_bp_r_stage3_event_memory_continuation.md).
Read the [plain-language findings](../../../reporting/rm12/bp_r_stage3/event_memory_findings_and_gate.md)
first. Source locations are in the [primary audit](../../../extraction/rm12/bp_r_stage3/event_memory_source_audit.md);
equations/proofs are in [PDF](event_memory_math.pdf) and [TeX](event_memory_math.tex).

## 1. Exact event memory is a bookkeeping result

For each descriptor-generating transfer stream, retain the remainder of its
cumulative actual transfer relative to the next source threshold. The streams
include discretionary lane changes as well as the ramp-related transfers;
one global ramp-entry counter cannot replace the source's separate streams.
Advance those remainders using this model's own actual transfers at the declared
source sampling times. The floor difference determines new disturbance births.
Retain all continuous transfer mass in the ordinary traffic balance.

This exactly reproduces source event counting given the same transfer sequence
and sampling, without a future-reference input, random birth or integerized
traffic. Under the descriptor-free startup subcase, a memory-aware candidate
can avoid an early penalty by using ordinary service until a descriptor exists.
This is a necessary activation ingredient, not a complete compact model: event
existence is not the same as binding, and independent models need not generate
identical transfers after their predictions diverge. We have not frozen a
Boolean-gated mean capacity as the service law.

## 2. Recovery does not have one universally supported clock

The supplied CM updates desired speed from realized speed. Traffic ahead can
limit that speed and the distance traveled. The same birth age is therefore
not enough to reconstruct motion in general. A constraint can also be nonbinding
while surrounding traffic is slow, without having attained KW free speed.
Deleting it permanently at the first nonbinding observation needs a future-
redundancy argument; an instantaneous check is not such a proof.

In the conditional level-road/free-downstream subcase, the sampled nonlinear
acceleration recurrence has an exact closed expression. Birth time, position
and birth speed reconstruct motion; records can be organized as age/birth-speed
cohorts. Here a cohort means a group with the same declared birth conditions,
not additional physical vehicles. Homogeneous free motion permits this
reconstruction without personal identities. The vehicle parameter vmax and
traffic free speed u are distinct; the source's u below vmax permits finite
attainment of u. No continuous exponential curve replaces the source's sampled
update, and no fixed timeout is adopted for constrained motion.

Even in that subcase, preserving kinetics alone does not give transient service.
Wave/void interaction and shared receiving still need their traffic coupling.
The free case is an analytical check, not a silently narrowed study task or a
proof that its policy optimization is nontrivial.

## 3. Why count plus average speed is not a complete general update

Without a traffic cap, the source's level-road acceleration update is affine
in speed, so count and summed speed can update that sum. Clamping each desired
speed by surrounding traffic destroys this property in general. Two lists can
have the same count and speed sum, but different fractions above the cap; their
clamped sums differ. The PDF proves this with symbolic admissibility conditions.

This establishes failure of that particular exact one-step moment closure over
the displayed local input domain. It is not a reachable equal-history freeway
pair, a TST difference, a no-finite-statistic theorem, or proof that every
macro/memory model fails. A restricted source family or additional statistics
could still close the response. A current clipped-speed sum does not by itself
provide its next update or the spatial restriction's effect on exits.

## 4. A source-preserving endpoint is available without names

Keep the lane-wise collection of restriction positions and realized speeds,
with fixed type parameters if needed, plus the ordinary traffic field and
per-stream birth remainders. Treat the collection as an unlabelled distribution.
Its initial projection is supplied from public initialization, and births and
motion use its own traffic. Subject to a well-defined label-independent source
coupling, merely permuting descriptor names does not change the update.
Spatial order is still represented by position; removing names does not remove
that order.

This is a conditional relabeling/equivalence result, not a compression result.
One atom per source descriptor retains the detailed configuration and can scale
with the number of restrictions. It is useful as a reference endpoint against
which a grouping rule can be assessed. It is not admitted as the sole compact
rival, and it does not settle the still-partial mandatory-node/coincidence solver.

Grouping nearby positions/speeds could produce a stronger compact rival.
However, substituting a group's mean trajectory for all its members, treating
every location in a bin as obstructed, or adding group penalties can change
the active set and double-charge disturbance effects. No such rule is inferred
from the exact distribution representation. This is the concrete remaining
state-and-service gap.

## 5. Candidate state/interface proposal, not an adopted equation

| State or input | Meaning and units | Initial projection / own update | Qualification |
|---|---|---|---|
| Lane/cell traffic and entrance waiting | Continuous vehicle-equivalent inventories; density where required | Existing public mass projection and conservative own flows | Existing approved accounting, joined solver still partial |
| Transfer remainder, separately per generating stream | Dimensionless progress to a descriptor threshold | Public cumulative remainder; own actual transfers at source sampling | Exact event-count bookkeeping |
| Restriction birth records/cohorts | Sampled birth time, origin position, birth speed; optional fixed type | Public initial records and own donor-speed births | Free-motion kinetic reconstruction only |
| Unlabelled position/speed distribution | Descriptor counts over metres and m/s; not traffic population | Public descriptor projection; own-source motion, births and certified removal | Lossless endpoint conditional on joined coupling; no compactness theorem |
| Grouped spatial recovery information | Numbers of restrictions in declared position/speed groups, with retained bounds/moments | A grouping projection and independent transport/service rule must be declared | Proposed review family; no bins, representative trajectory or penalty law adopted |

The ordinary receiving, priority and permitted physical traffic are the same.
A service operator must enforce source restrictions causally without extra mass,
artificial receiving or future-reference updates. Empty/nonbinding limits must
be qualified; population, entrance waiting, full exits and TST remain in the
conservative traffic field. Merely accumulating descriptor counts is not TST.

## 6. Literature does not close the missing compact service law

The audit preserves evidence for mean-capacity accuracy, aggregate bounded-
acceleration models and explicit leader/traffic coupling. None of the inspected
methods binds the proposed phase-plus-grouped-recovery map under all the current
task's births, interactions and receiving conditions. This is a bounded transfer
finding, not a claim that no such method exists in the literature.
Published compact alternatives remain important rivals; the current strict
source-matching requirement is not a universal standard for useful prediction.

## Disposition and review-tree position

**Partial positive:** exact threshold progress; conditional source-sampled
free-motion memory; a conditional unlabelled exact representation.
**Scoped negative:** a birth-age clock and count/mean-speed closure cannot be
promoted as generally exact based on these deductions.
**Open:** a genuinely reduced independently evolving recovery/service law for
the full current task; complete joined events/clearance; control leverage;
gradient correctness and usefulness.

The [next state-granularity discussion](../../../reporting/rm12/bp_r_stage3/event_memory_findings_and_gate.md)
asks whether A's qualified compact family should extend to grouped spatial
restriction information. T1 is approved; this proposal is not an implicit T2
waiver. A/B family coordination, source physics, actuator and predecessor
closures remain unchanged. Stage 3 stays open; Stage 4 remains unopened.
