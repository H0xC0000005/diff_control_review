# Exact information first: the chain and the next insertion decision

Date: 2026-10-07. Option A / G1 is approved and its bounded review is performed.
**Subsequent decision:** Q-E is now closed as E1, the sampled insertion proposal.
The [latest findings](sampled_insertion_findings.md) qualify its causal and
conservative reset and assess simultaneous prescribed paths. Full joined
feedback/clearance remain partial; E2 is unselected. The inventory below preserves
the proposal considered before selection.
The exact-state construction is now the primary task. Every distinct restriction
may be retained; storage, runtime and compression are not acceptance criteria.

**Keeping the exact records removes the earlier recovery-summary gap. It gives
us the information needed to pose the source motion and traffic-service problem.
The complete control model still needs an explicit rule joining a new merge
entry to that problem. Nothing found here shows that exact retention is
unacceptable or that approximation is necessary.**

## The big picture

The meter permits traffic to enter the ramp approach. Some of that traffic later
merges into the freeway. A slow entrant may hold back following traffic while
accelerating. The exact model remembers each restriction's location, speed and
traffic association, and evolves it against its own traffic field. It then
predicts exits and the waiting/travel time of the whole population.

If two restrictions recover differently, we keep both. If the source needs a
past speed measurement, we keep the own-model history needed to calculate it.
There is no need to invent an average restriction or reconstruct discarded
positions. Exact duplicates can share a record when equivalence is certified,
but that is optional.

This first construction is allowed to retain as much information as the reference
needs. Once it is qualified, it can provide an anchor for asking which information
can safely be removed. A reduced competitor does not have to be completed in
parallel with this pass. The original full-history hidden-information question,
control benefit and useful gradients remain separate claims.

## What was added to the chain

The construction now specifies the information carried between these functions:

**Permission → ramp propagation → actual merges → restriction creation and
motion ↔ traffic service → exits → complete system time.**

Population remains continuous and conserved. Restriction records are descriptions
of traffic effects; creating one does not add another vehicle to the objective.
The same traffic solution must determine both the restriction's downstream speed
and the resulting service. A guessed capacity penalty is unnecessary.

We also resolved an accounting detail. A traffic-count label can stay constant
along a restriction on a lane segment without lane changes. If traffic enters
or leaves that lane along the segment, the label must be adjusted using those
actual transfers. Otherwise a correct position/speed record can be attached to
the wrong traffic count. The new source-correction identity supplies that
adjustment from the model's own accepted-transfer records, without approximation.
It does not decide how a transfer exactly at the restriction is attached.

The source literature supplies retained moving restrictions, their own coupled
motion and traffic solution, and a ramp-merge application. Those are positive
grounds to continue the exact route. The existing moving-boundary algorithm
also averages the ordinary traffic field numerically; exact restriction retention
does not make a finite mesh an exact continuum solution.
[Daganzo/Laval moving-boundary method](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf),
[Laval/Cassidy/Daganzo merge application](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf).

## The remaining issue, through an example

Suppose the ramp's descriptor counter begins three quarters of the way to its
next unit threshold. Over the next second, an accepted half-unit transfer would
cross that threshold halfway through the interval.

The source's sampled generation sees the new restriction at the interval's end.
An event-resolved extension would create it at the halfway crossing and include
its effect during the rest of the interval. Both can keep every restriction and
conserve every fraction of traffic mass. They predict different activation times.
In a coupled model, the earlier restriction could also change later accepted
flow; we cannot simply move its timestamp after calculating the entire interval.

The example checks the clock using a supplied mathematical counter. It is not
a reached traffic scenario or evidence of a different optimal metering policy.

The journal's sampled clock is known. What remains to bind is its **complete
birth/reset prescription at our approved mandatory node**, or an explicitly
declared event-resolved extension. This includes when the new condition begins,
which traffic-count value it attaches to, and the coupled continuation. The
inspected sources do not uniquely supply that whole adaptation. Complete
well-posedness at coincident births and eventual clearance remain obligations.

## The next decision: how a new merge restriction enters the model

**Problem statement:** should we bind the proposed insertion/reset under the
already selected sampled reference, or explicitly reopen that reference's clock
to pursue an event-resolved model?

**Function in the chain:** accepted merging/lateral transfer creates a new
restriction; its motion and count condition affect subsequent traffic service.
The upstream meter, fixed receiving priority and full-system-time objective
remain the same.

**Core gap:** a birth count alone does not specify the complete insertion into
the joined traffic solution. A record's timestamp, location and count attachment
must agree with the transfer that produced it. Changing activation timing changes
the finite-model forward response. This is a concrete scientific transcription
choice; engineering cost is irrelevant to its comparison.

### E1 / option A — bind the source-nearer sampled insertion first

Use the declared source update times. At an update boundary, accepted transfers
from the completed interval advance their own counters and generate every new
record. For the ramp, birth is at the physical merge point. For a sampled
discretionary transfer, use its declared target-section entry coordinate as an
explicit insertion transcription to qualify. Initialize motion from the donating
stream's source speed at the interval's request phase and attach the record to
the updated own traffic count at that location.

New restrictions act from this update boundary onward. They do not retroactively
reduce already accepted mass. Existing restrictions remain coupled during the
completed interval. Keep every distinct newborn signature; coincident records
must receive a source-consistent joint continuation rather than jitter or an
average path. A receiver-cell label is not itself permission to choose an
arbitrary location inside the cell.

**Pros:** follows the journal's explicit sampled generation; gives a definite
state phase and conservative birth interface; starts from the nearest existing
source rather than adding sub-interval event dynamics.

**Cons:** activation has the source sampling delay relative to a continuous
threshold interpretation. The proposed node/target-entry placement, birth-speed
sampling and post-transfer count attachment are still adaptations to qualify;
the cited convergence results do not establish the whole joined model or its
control sensitivities.

**Dependency/consequence:** approve this concrete reset proposal as the first
qualification target, not as a completed solver. Recheck the exact joint
node/birth continuation, one-sided source attachment and clearance. Any conflict
returns to this contract. The sampled clock is a declared model level, not proof
that exact continuum event timing is unnecessary.

### E2 / option B — activate at actual accepted-transfer threshold crossings

Evolve the actual cumulative transfer continuously in the model's declared
within-interval solution. At its first threshold crossing, create the restriction
at the corresponding transfer location, using the donating stream's own speed
and traffic count at that event. Continue the coupled traffic solution from that
event, so the new restriction can affect later receiving and transfers. Resolve
simultaneous events together; do not take event times or speeds from a future
reference run.

**Pros:** makes activation follow the model's actual accepted-transfer history;
removes the delayed-start feature of the sampled birth prescription; exposes a
causal event-time dependence on metering without discarding retained information.

**Cons:** extends the journal's sampled recipe. It requires a qualified own
within-interval transfer solution, event reset and simultaneous-event continuation.
Resolving crossings does not by itself prove well-posedness, clearance or useful
gradients. A post hoc interpolation of a completed step would not meet this rule.

**Dependency/consequence:** explicitly approve the event-resolved extension of
the reference transcription by reopening S3-G2.A's sampled-clock contract and
its dependent onset/inactive comparison timing. Continuous mass, M.A, N.A and
public initial threshold progress stay fixed. Preserve the requirement to match
inactive reference states, but requalify which states are inactive under the
new clock. Earlier sampled-onset findings remain dated evidence. Then qualify
the joined event solution. No new vehicle-launch law or microscopic gap model
is implied. This reopening has not been selected or performed.

**Provisional recommendation: E1 first**, because it preserves the selected
reference's sampled generation. That clock is not being reopened under E1.
Its insertion adaptations must be tested against
the source and conservation before it is accepted as a complete law. E2 remains
a legitimate exact-information extension. Neither choice uses cost or compression
as a reason to approximate recovery state.

## Where we stand

| Obligation | Result |
|---|---|
| Exact retained state | Allowed and specified; every distinct restriction may remain. |
| Source-correct traffic-label accounting | Derived on regular segments; point-source attachment still needs binding. |
| Own motion/service route | Source-backed ingredients and explicit information interfaces; joined birth/reset qualification pending. |
| Entire control model | Partial; clearance and complete TST rate leverage unproved. |
| Need for approximation, hidden-information necessity, useful gradients | Not established. |

**Q-G is closed as G1. S3-G2-Q-E is closed as E1, Type 2/user; E2 is unselected.**
Bounded reset/prescribed-path qualification is complete; further joined qualification is reviewer-owned;
final whole-model adoption and Stage 3 closure remain pending. Approximate
recovery reduction is unopened. Stage 4 and experiments remain unopened.

Optional details: [technical construction](../../../synthesis/rm12/bp_r_stage3/exact_information_chain_assessment.md),
[source audit](../../../extraction/rm12/bp_r_stage3/exact_information_source_audit.md),
[mathematical companion](../../../synthesis/rm12/bp_r_stage3/exact_information_chain_math.pdf)
and [work report](work_report.md).
