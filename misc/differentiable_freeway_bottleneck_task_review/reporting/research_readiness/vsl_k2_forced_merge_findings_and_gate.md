# A compact forced merge can be formed from one waiting stream and finite receiving

**K2 can form a concrete forced-merge candidate:** continuing traffic passes
first, while unfinished ending-lane traffic joins one continuous-mass queue
and uses the receiving service left after that traffic. Unserved mass stays
present, completed merging leaves the ending lane exactly once, and the queue
drains after the finite cohort has arrived. Its delay contributes directly to
total system time (TST).

The important physical qualification is where that waiting traffic fits. A
source-compatible construction uses a finite final road section whose entry
and exit histories describe storage and travel. When its receiving constraints
stay slack at the upstream interface, the queue remains contained there and
H1's preparation window can remain homogeneous. This needs a declared terminal
section and an early-to-terminal handoff; it cannot be obtained by attaching
an unlimited point queue to the old clock.

**Subsequent T1 selection and completed joined qualification, 2026-10-14.**
The user selected T1's finite physical section, described handoff and restricted
own-lane-first member. The exact H1/T1 contract is now assembled, with active
early receiving and positive forced waiting in one physically contained domain.
The original Pass 2 evidence review is finished at contract confirmation before
freeze. T2 is unselected. The T1/T2 descriptions below retain their choice-time
meaning; the current confirmation report supersedes their open status.

[Current joined model and final original-stage gate](vsl_t1_joined_model_and_gate.md)

Date: 2026-10-14. **At the K2 delivery checkpoint, the user had approved K2 and this bounded qualification was
finished at the original VSL-B2-G1 interface gate.** The proposed terminal
law, physical separation and exact upstream adaptations are not yet an
adopted full methods contract. The successor's modeling-chain stage remains
open pending this concrete disposition. No simulator construction or traffic
experiment was opened.

## What the forced-merge model actually does

There are two streams at the permanent lane end. The adjacent continuing
stream includes traffic that originally occupied that lane and traffic that
already completed an early merge. The other stream consists only of traffic
still on the ending lane. That lane has no forward continuation: its traffic
must obtain lateral receiving to exit. Being forced to merge means it must
wait when service is unavailable; it does not mean it can enter without space.

The first candidate carries P1's own-lane-first principle into this terminal
interaction. At each instant, feasible continuing flow takes service first.
An available ending-lane request takes the residual, subject to its own
sending limit and a separate late merge-work factor. The late factor describes
service consumed, not additional vehicles. Once accepted, that mass has
completed the lane change and crosses the final task exit; it is not added
back to the upstream preparation stock.

The elementary member restricts continuing traffic to a range where that
first claim can be served immediately. Consequently, only ending-lane traffic
needs a waiting queue. Its arrivals come from H1's predicted early-transfer
state and physical travel clock. Its service comes from a declared finite
downstream receiving rate and the continuing flow competing for it. Neither
arrival nor service is supplied from a post-action reference trajectory.

The queue records how much ending traffic is ready but not yet served. If
that mass is positive, it uses all feasible residual service. If it is zero,
it cannot discharge more than the newly available traffic. When the last
continuing arrival has passed, the remaining ending mass can use the receiver
without that competition, and finite positive service guarantees clearance.

This is an arrival-aware fluid merge server. It keeps continuous mass and
lane-specific competition, but introduces no vehicle-by-vehicle maneuver,
leader following, individual gap sampling or discrete ordering requirement.
All queued ending traffic has the same destination and the same service-work
class in this member.

## The two options as traffic pictures

The common forced-merge mechanism is a **service point at the permanent lane
end**: continuing traffic claims service first and ending traffic waits for
what remains. The two options give that waiting different physical meanings.
Neither introduces a new distributed lane-changing law inside the terminal
area. The distributed early-merging mechanism remains H1.

**T1 is a physical queueing section followed by a point merge.** Imagine a
short final stretch of ending lane on which traffic can travel toward the
lane end and form a real waiting line. Upstream of that stretch, traffic is
still in H1's homogeneous early-preparation window. At its downstream end,
one compulsory merge rule determines who exits.

The core addition is the final stretch's length, finite storage and boundary
entry/exit histories. Those histories account for traffic still traveling as
well as traffic delayed by the merge, and permit a physical receiving check.
They do not retain separate traffic states at successive interior positions.
The model is therefore a compact boundary-count description of a physical
queueing section; it is not a uniformly mixed reservoir or a new spatial
lane-changing model.

T1 chiefly addresses **whether terminal waiting can fit on the road without
disrupting the homogeneous preparation model**. Its admitted domain keeps
the queue contained downstream. If the receiving check fails, the proposed
one-way H1 handoff is no longer justified; the current candidate does not then
silently turn into a general spillback solver. The price is a new physical
handoff: early merging stops before this final section, and queued terminal
motion need not be homogeneous. H1's homogeneity is retained in preparation,
not asserted throughout the entire corridor.

**T2 is a vertical fluid queue at the merge point.** Imagine a counter or
waiting list attached to the lane end. Traffic reaches that point according
to H1's travel clock; any mass not accepted immediately is entered on the
list until service becomes available. “Vertical” means that the mathematical
queue consumes time but has no represented road length. Vehicles are not
literally stacked above one another.

The core addition is an unserved-mass account with arrival and departure
timing. H1 keeps the full original early-preparation length. The queue does
not move backward into H1 or change its motion and early opportunities.
This option chiefly addresses **how finite forced service turns arrivals
into departures and complete time with the smallest model change**. It
accepts the absence of upstream feedback as an analytical approximation;
it does not establish where the real waiting traffic fits.

For example, with three units waiting, T1 interprets them as part of the
ending lane's physical occupied stock and checks the terminal section,
including any other traffic still traveling there. T2 records three units
on its virtual waiting list and counts their delay, without a road-space
check. Both have the same proposed point-service principle, but their
preparation lengths, arrivals and physical-feedback claims differ.

| Option | Mental picture | Main problem it addresses | Main added assumption or cost |
|---|---|---|---|
| **T1** | A finite physical approach/queue section ending at one compulsory merge point. | Justify a domain in which a real terminal queue leaves H1 preparation unaffected. | A separate terminal section and early-transfer handoff; terminal waves/queue extent are implicit in boundary histories. |
| **T2** | A vertical continuous-mass waiting list at the compulsory merge point. | Calculate terminal delay and departures while retaining the original H1 preparation window. | Waiting has no represented footprint or feedback into preparation; this is a deliberate approximation. |

At the clarification checkpoint, no equations or recommendation changed and
T1/T2 remained unselected. The user subsequently selected T1; see the current
joined-contract confirmation report linked above.

## Why physical storage is the remaining interface choice

A scalar waiting queue alone says how many units are delayed. It does not say
whether the back of that queue reaches traffic still preparing upstream.
That is the distinction between a useful terminal account and an unexplained
one-way attachment to H1.

The qualification therefore examined a finite terminal reach: a final part
of the existing fixed road length, immediately before the lane end. The
cohort begins in the homogeneous preparation window upstream of it; the
terminal reach is initially empty. Entry/exit cumulative counts record the
mass traveling or waiting there. These are histories at boundaries, not
independent traffic states at successive interior positions.

Link-transmission theory supplies both the earliest physically eligible
departure and the limit on how much upstream traffic can enter before a
backward restriction reaches the interface. Its queue amount is different
from its total occupied stock: some stock may still be traveling toward the
lane end. Counting only waiting mass against storage would be insufficient.

[Jin: continuous LTM queue, vacancy and boundary-count relations](https://arxiv.org/pdf/1405.7080)

[Yperman, Logghe and Immers: link propagation and merge-node allocation](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf)

Within a conservative parameter restriction, terminal receiving at the
preparation interface stays nonbinding even though forced merging queues.
For example, requiring the entire finite cohort to fit inside one terminal
lane's jam storage is stronger than necessary, but gives an analytical
sufficient bound; compatible input-flow limits also apply. This proves a
nonempty restricted construction with finite waiting and no spillback into
H1. It does not show that arbitrary demand or every real taper satisfies it.

There is a consequential old-to-new change. The final section has no further
distributed early transfers in this candidate: ending traffic proceeds to
the compulsory node, where service is allocated. H1 therefore operates over
the shorter upstream part of the same total road length. We have not appended
extra road, omitted its travel time, or silently disabled a part of the old
preparation law. The handoff and exclusion of further lateral sources are
**proposed restrictions requiring adoption**. A real site would need a
justification for that treatment; the literature does not establish it for
this hypothetical three-to-two task.

The terminal reach can contain congested motion represented implicitly by
its boundary histories. H1's preparation window remains homogeneous in the
admitted no-spillback domain. This does not claim that an actual terminal
queue is uniform or instantaneous. No internal position profile is retained,
but the added terminal geometry and wave/storage meaning are real scientific
changes and are presented at the gate below.

## S13 was concrete analytically; its physical forced merge was not qualified

The user's reason for opening K2 is sound: a complete revised stack needs
a specified compulsory-merging, holding and departure rule. One detail of
the premise needs correction. S13 already specified a conditional fluid
choke law: unfinished merging used extra receiving work, and a simultaneous
batch received proportional service. That was enough to define its
analytical objective and certificate.

What it did not establish was a physically qualified lane-end model for
staggered arrivals, finite storage, queue influence and changing competing
flow. K2 supplies a concrete candidate for those missing responsibilities;
it does not repair an unspecified or mathematically incomplete S13 proof.

[Accepted S13 mathematical service contract](../../synthesis/s13/s13_m2_model_contract.pdf)

## How service becomes TST: a small reference example

Consider four ending-lane and four continuing units arriving evenly over
two seconds. The receiver has four work units per second. Continuing units
use one work unit each; ending units use two. Assume donor sending does not
bind. These are hand-reference quantities, not selected traffic parameters.

During the arrival pulse, continuing flow takes two work units per second.
The remaining two work units complete one ending unit per second, while two
ending units arrive. The ending queue therefore grows to two units. Once
continuing arrivals stop, two ending units per second can exit; the queue
clears one second later. Integrating queued mass over time gives three
vehicle-equivalent seconds of additional delay. Every unit eventually exits.

Now spread the same arrivals over four seconds, leaving preparation outcomes
unchanged. Continuing flow claims only one work unit per second and ending
arrivals fit the remaining service. There is no queue. Nevertheless, those
later arrivals take more total time:

| Reference arrival pulse, measured from its first eligible arrival | Terminal queue delay | Sum of eligible arrival times | Sum of complete exit times |
|---|---:|---:|---:|
| Eight units evenly over two seconds | 3 veh-eq s | 8 veh-eq s | **11 veh-eq s** |
| The same units evenly over four seconds | 0 veh-eq s | 16 veh-eq s | **16 veh-eq s** |

This illustrates why reducing queueing alone does not establish a better
speed policy. The arithmetic includes all eight units' eligible arrival and
waiting times. It is an isolated terminal reference, not a reachable H1
comparison, a parameter sweep or an optimizer result. A whole-road comparison
also includes each action's physical travel to the first eligible arrival.

Priority also matters. With two ordinary and two forced-merge units already
waiting, the same extra-work factor and receiving rate give identical final
clearance under own-lane-first and proportional batch service, but different
TST. The mathematical note works out five versus six vehicle-equivalent
seconds. A work total or final clearance time therefore cannot substitute
for an allocation rule. Proportional service is a serious rival, especially
for cooperative merging, but it can require a continuing-lane queue as well;
it is not silently substituted into the one-queue member.

[Carey, Balijepalli and Watling: own-lane-first and proportional rules](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

## What this means for an interior speed optimum

Forced merging supplies a mechanism that can oppose the travel-time benefit
of faster advice. Its existence does **not ensure** an optimum between the
minimum and maximum advice. The relevant question is whether the complete
TST benefit from changed preparation outweighs the added travel time in part
of the admitted range, and then stops outweighing it elsewhere.

There is a stronger diagnostic result for this candidate. When completed
preparation is held unchanged across actions, receiving and merge-work costs
are fixed, and longitudinal sending does not bind the merge server, merely
making the same traffic arrive earlier cannot worsen complete TST under the
proposed own-lane-first rule. The mathematical note proves this through
cumulative departures. The fastest action can remain best even with a real
forced-merge queue.

An interior optimum would therefore need a sufficiently consequential change
in preparation or another separately justified service mechanism. H1 can
change preparation through its admitted state/service response, but this
pass derives no whole-model interior optimum or hidden-state action split.
Fastest, slowest, interior, common-action and scalar-sufficient outcomes remain
valid results. No priority, cost factor or road partition is chosen to force
the desired shape.

This is a stage-level finding: adding the missing compulsory-merge model
can complete the traffic chain, but it cannot by itself transfer S13's
positive control certificate to the revised task.

## Direct MP1–MP6 answers and the minimal stack delta

| Question | Direct result of K2 |
|---|---|
| **MP1: opportunity and speed** | H1 still predicts early completion. Advice also changes terminal arrival timing and instantaneous competition. Reserving a terminal section changes where early preparation ends; that is an explicit shared handoff proposal. |
| **MP2: feasible merging** | Terminal completion can be defined by available ending traffic, finite residual receiving work and conservative queue discharge. “Forced” does not bypass a binding receiver. |
| **MP3: required information** | With initial continuing symmetry and initially empty terminal storage, aggregate mass plus the initial ending statistic still initializes the whole proposed candidate. Terminal queues and histories are predicted internal states, not extra initial observations or reference oracles. |
| **MP4: early and late costs** | The candidate counts every unit's full road travel and terminal delay. Early completion changes how much later traffic needs the extra-work service class. Queue influence on H1 is excluded only by a physical receiving/storage domain, not ignored by default. |
| **MP5: departures** | An explicit arrival-aware own-lane-first server yields complete departures and finite clearance. Equal total work does not imply equal TST under another priority. The old proportional-batch mean is not reused. |
| **MP6: joint regime** | A restricted analytical construction can join H1, finite terminal storage, positive forced-merge waiting, no spillback to preparation and full clearance over a bounded advice range. Its road partition, terminal priority and no-further-early-transfer restriction require adoption; its joint applied calibration remains absent. |

The primary replacement is component 6: a receiver-limited arrival-aware
forced-merge server and its stored residual, replacing S13's simultaneous
proportional batch for this candidate. Components 3–5 need the explicit
preparation/terminal interface and shorter early-opportunity domain. The
total road length and component 7's complete-time objective remain fixed.
Component 8 retains initial symmetry and the strong ending-statistic rival.
Component 9 must later qualify derivatives and decision usefulness for the
new complete law; the existence of its queue is not that evidence.

## Original VSL-B2-G1: adopt which terminal meaning?

**Problem statement.** Should the candidate's compulsory queue be given a
finite physical terminal reach with a defined preparation handoff, or remain
an explicitly virtual terminal approximation attached to the full H1 clock?

**Assumed model-chain function.** H1 determines early transfer and terminal
inflow. The receiver-priority server determines completed forced merging and
departures; storage determines whether waiting can affect H1. Complete TST
counts both road travel and all residual delay.

**Core gap.** The reviewed sources supply boundary-count storage/propagation
and local receiving allocation, but do not select this task's terminal
reach, early-transfer cutoff or compulsory-merge priority. K2 approval opened
their qualification; it did not adopt those scientific choices. A spatial
storage interpretation changes the shared geometry/opportunity interface;
a virtual queue leaves physical feedback as a declared approximation.

**Candidate T1 — finite terminal reach, with the restricted one-queue server.**
Its mental model is a **physical queueing section plus a point merge**.
It addresses whether terminal waiting can remain physically separated from
H1 preparation. Reserve a final part of the existing road length for traveling/holding before
the compulsory node. Use compact lane-boundary histories and the receiving
criterion to admit a no-spillback domain. End distributed early transfers at
the reach's entrance. Use the proposed own-lane-first server in a domain where
continuing flow is served immediately; the ending queue remains the only
waiting class. **Pros:** forms a complete conditional forward candidate with
physical travel, finite storage, explicit receiving, full departures and a
verifiable no-feedback restriction; keeps H1 homogeneous and needs no interior
position state. **Cons:** changes the early-opportunity boundary and introduces
a terminal region with implicit congested motion. Excluding further early
changes there and using strict continuing priority are adaptations needing
site/domain justification. The sparse finite-cohort bound is conservative.
This reopens G3/VQ3-P/T/S for the interface, with G2 fairness and G4 accounting
dependencies; it does not adopt spatial B inside H1.

**Candidate T2 — an explicitly virtual terminal queue.** Keep early preparation
through the full original H1 window. Its mental model is a **vertical fluid
queue at the merge point**, addressing departure and delay accounting while
assuming that waiting has no upstream effect. Attach the same arrival-aware residual
server to its predicted lane-end arrivals. All waiting remains counted, and
the exact priority and service law stay visible. Treat queue location and lack
of upstream influence as a deliberate theoretical approximation, not a finite
road-storage conclusion. **Pros:** changes primarily the choke component,
preserves the full early-opportunity length and offers a small analytical
information/gradient verification member. **Cons:** a positive queue on the
real ending lane can occupy the preparation area; the proposed homogeneous
motion and continued early opportunities are then not physically qualified.
A nominal queue cap alone does not establish storage or backward-wave
feasibility. It can complete an abstract model, but its applied interpretation
and evaluator mapping need a weaker stated claim. This requires an explicit
G3 approximation decision and G1/G4 claim consequence; it is not equivalent
to T1 merely because their server equations match.

**Provisional recommendation: T1**, if retaining a physical storage/receiving
interpretation is part of the intended elementary task. The proposed
own-lane-first rule is the minimal source-aligned continuation to qualify;
proportional or cooperative terminal service remains a distinct model-form
rival, not an already closed priority decision. T2 is a viable choice only
with its virtual/no-feedback limitation expressly accepted. Neither option
is adopted here, and no new mechanism is recommended solely to obtain an
interior optimum.

The bounded K2 evidence pass is finished. **Pass 2 remains open at this
specific terminal-contract adoption gate; Passes 3–4 have not begun.** The
next allowed action is disposition of these concrete terminal meanings.
The review stops as instructed before adopting the partition, exact forced
priority or virtual approximation.

[Original-stage progress](vsl_review_progress.md)

[Forced-merge equations, storage proof, reference cases and speed limit](../../synthesis/research_readiness/vsl_k2_forced_merge_contract.pdf)

[Viewed-paper references and source/adaptation audit](../../extraction/research_readiness/vsl_k2_terminal_source_and_interface_audit.md)

[Files, commands and verification record](vsl_k2_work_report.md)
