# Option B: a mandatory-transfer model and its place in the VSL task

**Current continuation, 2026-10-13.** VSL-B2 has executed the approved P1
qualification to a new receiver/motion choice. The local R1 receiving rule is
source-backed, but current receiving alone does not generally predict future
service. Compact and small spatial realizations remain unselected; MP6 is open.
The B1 gate below retains its delivery-time meaning.

[Executed P1 review and receiver/motion gate](vsl_b2_joined_service_findings_and_gate.md)

Date: 2026-10-13. Status: **The authorized model-qualification review is
complete at VSL-B1-G1. A model form and bounded amendment are proposed;
replacement equations and an applied operating domain are not approved.**

Current continuation: the user approves P1, closing the Option B/P1 review
direction and proposal discussion. Jointly qualify traffic-state-dependent
adjacent receiving and receiving-constrained completed merging, with own-lane
priority first. The component-4 direction and component-5 assumption change
are approved; exact state, motion, timing and MP6 laws remain open. The findings
and earlier alternatives below retain their meaning. Broader interface changes
are not granted automatically, and no remaining review is executed here.

[P1 approval and bounded review readiness](vsl_p1_approval_and_review_readiness.md)

[P1: one concrete component improvement and remaining questions](vsl_p1_preparation_transfer_improvement_proposal.md)

[Original framework, component verdicts and shared responsibilities](vsl_feedback3_existing_framework_component_audit.md)

## The model that can take shape

The useful replacement direction is a small continuous model of **mandatory
transfer between neighboring lanes**. Traffic in the ending lane requests a
merge; the model determines how much can actually move, given available traffic
and space in the adjacent lane. Unserved traffic remains present and still
needs to merge. Changing the common speed can change how this traffic reaches
and competes for that space. It does not automatically create a fixed number
of extra completed merges for every additional second.

This direction addresses the whole question set. It gives the transfer law a
physical meaning, represents the service that limits completion, and connects
merging to the traffic costs paid where it happens. However, it cannot yet be
qualified as a drop-in replacement for S13's preparation equation. The old
interface sends unfinished merge mass to a separate, simultaneous exit batch.
A model that responds to the adjacent lane's crowding may need to exchange
receiving conditions and flows over time instead. That is the central
methodological choice reached by this review.

**My recommendation is to permit a bounded review of that local interface
amendment, rather than require the replacement to preserve the scalar handoff.**
This remains an elementary task candidate: one lane drop, one finite cohort,
one common speed action, continuous mass, and time counted until everyone exits.
The evidence does not yet establish its final state size, common-speed response,
useful gradient, or jointly valid applied regime. MP6 therefore remains open;
it is a requirement on the complete proposed model, not a label earned by
borrowing its parts from papers.

## Why the adjacent lane matters

Imagine two preparations with the same ending-lane traffic and the same combined
traffic in the two continuing lanes. In the first, the lane directly beside the
ending lane is crowded and the farther lane is relatively clear. In the second,
those occupancies are reversed. The total continuing traffic is unchanged, but
the immediately available merge space can differ. A model that sees only the
combined continuing mass cannot generally distinguish these preparations.

This is a statement about local service, not yet a certificate that the best
VSL action differs. That stronger conclusion requires the complete dynamics
and time accounting. It also does not prove that a full lane profile is the
minimum remedy: a compact measure of adjacent receiving might be enough in a
declared restricted model.

Even an initially balanced continuing pair is insufficient justification by
itself. A transfer adds traffic first to the adjacent lane. Unless subsequent
outflows or redistribution maintain the required equivalence, that selective
inflow can break the balance. Common advice does not supply such a balancing
law. We must either justify the grouping dynamically or retain the distinction
that controls receiving.

These are reduction arguments made in this review. Their short mathematical
examples are in the supporting note; they are not simulated traffic results.

[Information and departure-time examples, PDF](../../synthesis/research_readiness/vsl_b1_interface_examples.pdf)

## What the lane-change model would mean

The candidate separates three things that the fixed completion rate collapses:
**wanting to merge, being available to merge, and being accommodated**. This
separation allows simple behavior without pretending that completed service
is independent of traffic conditions.

The simplest behavioral candidate is that ending-lane traffic wants to move
over at the next feasible opportunity in the preparation region. A location-
dependent desire is an alternative if its added behavior is needed. Neither
choice says that the requested amount is completed. A constant desired share
can also be meaningful, provided it is a share of specified available demand,
with a declared relation to road progress and sending; it is not a constant
physical-time completion hazard.

The adjacent lane then receives both its own advancing traffic and traffic
from the ending lane. An allocation rule must resolve that competition. A
gap allowance may make a merging unit use more receiving opportunity than an
ordinary unit, while the transferred traffic mass itself remains unchanged.
The same accepted transfer must leave the donor and enter the recipient.
Any unmet request remains in the donor; no traffic may disappear at the lane end.

Carey's mandatory-transfer and receiving-allocation framework is the provisional
principal candidate for this bounded reduction. It offers simple desire rules,
gap-weighted receiving, and explicit priority alternatives. Its proportional
rule is a candidate, not a universal service law. Subraveti's lane-drop model
is a valuable check on the importance of density, route urgency and neighboring
conditions, but its incentive, cooperation and capacity-drop equations should
not be spliced into Carey to fill missing parts. These are different source
models, and neither whole model is adopted here.

[Carey, Balijepalli and Watling: primary manuscript](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

[Subraveti, Knoop and van Arem: archived primary article](../../archive/full_text/FB0030.pdf)

This proposed model form retains continuous traffic and fixed lane adjacency.
It does not require individual gaps, stochastic vehicles, discrete identities
or an exact vehicle-order model. Its continuous information needs are the
traffic still requiring transfer, the receiving opportunity of the actual
target, and the longitudinal traffic that competes for or replenishes that
opportunity. How compactly these can be represented remains a reduction
question. A single source cell, a prescribed receiving time series, or total
lane masses alone cannot be assumed sufficient without checking what they
omit.

## How it connects to preparation, exit service and total time

The existing methodological stack has the right scientific roles: a common
action changes traffic evolution; traffic determines service and departures;
departures determine complete time; initial observations support autonomous
predictions. The proposed amendment concerns the information exchanged within
that chain. It is independent of current simulator APIs or implementation progress.

| Interface | What can remain | What the proposed transfer model needs qualified |
|---|---|---|
| Common advice into traffic | One bounded, constant, lane-uniform speed action | A declared effect on longitudinal demand/motion; advice need not equal actual speed when receiving binds |
| Traffic into lane transfer | Conserved continuous mass and fixed neighboring-lane permissions | Available mandatory demand, target receiving and competition from same-lane traffic |
| Preparation into exit service | Unfinished merging remains consequential | A scalar final merge mass is sufficient only under proved receiving and timing restrictions; otherwise local state and time-resolved flows must connect the regions |
| Exit service back into preparation | Finite downstream receiving | If exit congestion restricts upstream receiving, that feedback must be represented or excluded by a justified domain restriction |
| Traffic into the objective | Complete cohort time, including moving and waiting traffic | Use the actual departure trajectory and include any upstream holding; preserve the meaning of the objective even if its closed formula changes |
| Initial information into prediction | Fair common observations and autonomous forecasts for every action | Any additional receiving information must have a declared initial observation/inference contract; no future reference values may be supplied |

The important point about early merging is that it uses receiving space too.
It can be beneficial when that space is spare upstream and scarce later. It can
also delay continuing traffic upstream, or move the same conflict to another
location. The model should decide between these outcomes through consistent
service and departures. Counting fewer unfinished merges at the exit is not
enough to establish a net benefit.

Likewise, a service calculation must explain **when** traffic leaves. Suppose
two classes need the same total receiving work. Serving ordinary continuing
traffic first or serving merge traffic first can produce the same final
clearance time but different average completion times. The supporting note
gives a hand-computed example. S13's half-clearance mean is correct for its
proportional simultaneous batch; it cannot be carried over solely because
the new model preserves total work.

Allowing departures at different times within the same finite cohort does not
open streaming external demand. It does change the old batch interface, which
is why it belongs at a methodological gate. The proposed amendment does not
change the complete-time research objective or authorize a new arrival population.

## MP6: when would this be a jointly defensible task?

There is a credible structural route, but **no jointly admitted applied domain
yet**. Continuous conservation and receiving-constrained mandatory transfer
are supported ingredients. The inspection does not establish a single elementary
reduction that also supplies the intended common-speed response, three-to-two
boundary, aggregation, early/late cost balance and departure chronology over
one action range. This is a bounded evidence result, not proof that such a
domain cannot exist.

First, the common action must have one consistent meaning throughout the model.
Under a declared ideal free-flow response, advice may set the longitudinal
speed. Under binding receiving, the actual progress can be slower and differ
between lanes even with common advice. Changing only a preparation duration
while leaving all sending and receiving untouched would not establish the
response of the proposed model. Nor does adding an arbitrary speed factor to
merging establish a synchronized-flow law. No such specialized law is admitted
by this review.

Second, the grouping and cost assumptions must hold in the same conditions.
Upstream spare space and a constrained exit are not logically incompatible:
they describe different places and potentially different times. But a queue
from the exit can consume that upstream spare space. An admissible sequential
reduction therefore needs to show that the required receiving remains slack
throughout preparation for the relevant cohort and actions. A coupled reduction
can instead represent the loss of that slack, at the price of more state and
timing. Neither option may assume the favorable part of each regime while
ignoring their interaction.

Third, the lane-end boundary must close the population. The primary model must
hold any traffic that has not merged, allow its subsequent feasible transfer,
and count its waiting until exit. Increasing desire near the lane end does not
guarantee available receiving. Carey supplies a useful local transfer framework,
but not the whole permanent three-to-two VSL boundary contract. Subraveti has a
native lane-drop application, but its receiving branches and common-speed
adaptation still need their own audit. Source labels cannot discharge this
population-closure obligation.

Finally, the domain must support the proposed sensitivity, not just one forward
trajectory. Fixed geometry and population, coherent speed/flow parameters,
known receiving and behavioral branches, and explicit boundary cases are
necessary before interpreting a local derivative. Source minimum operations
and switching rules need not be smoothed to make the result look differentiable;
any ordinary derivative applies within its declared regime. Whether that
derivative improves traffic in an independent evaluator remains a later evidence
layer.

The existing common-VSL studies support traffic relevance without proving this
combination. Zhang's three-to-two study uses microscopic interactions and a
different control/accounting setting; its calibration at 100 km/h does not
validate this proposed action range. Roncoli's continuous multi-lane control
model directly chooses lateral flows, giving it an actuator our common-speed
task does not have. These precedents help set boundaries, rather than supply
a missing endogenous merge response.

[Zhang et al.: primary lane-drop VSL manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

[Roncoli et al.: primary multi-lane control paper](https://skoge.folk.ntnu.no/prost/proceedings/ifac2014/media/files/1657.pdf)

## What this establishes for MP1–MP6 and the simpler rivals

The review supports a model in which local receiving determines completed
merging and departure timing determines complete traffic time. It does not
establish that S13's simplifying assumptions describe that traffic together.
The answers below explain this distinction; they preserve S13's accepted
conditional result and do not select replacement equations.

| Question | Direct answer and core finding | Traffic meaning and limit of the finding |
|---|---|---|
| MP1: What determines merge opportunity over the preparation section? | **The inspected models describe merge requests through available traffic and road location; they do not justify S13's fixed per-second completion fraction as an applied traffic law.** | A fraction of traffic wanting to merge at a location is different from a fraction guaranteed to finish merging every second. Slower progress can also reduce the traffic offered for transfer, so extra time in the same road section does not automatically produce more completed merges. The exact response to common advice remains unresolved. |
| MP2: What determines how much requested merging actually finishes? | **Available traffic and the adjacent lane's receiving space limit completion; merging traffic competes with that lane's own advancing traffic.** | A crowded target can leave requests unserved even when drivers want to merge. That traffic remains in the ending lane and still needs an opportunity later. A completed-transfer rate cannot generally stay fixed while these service constraints change. This supports the proposed model structure, without selecting one exact allocation rule. |
| MP3: Can the continuing lanes be combined without losing relevant information? | **Not in general. The same combined mass can hide different amounts of space in the lane that actually receives the merge.** | Swapping crowding between the adjacent and farther continuing lanes can change immediate merge service while leaving their total unchanged. Initial balance is also insufficient: merges add traffic first to the adjacent lane and can break that balance. A compact receiving statistic might preserve the distinction; necessity of a full lane profile is not established. |
| MP4: Why could early merging help, and are its costs covered? | **Early merging can use spare space upstream, but it still consumes receiving opportunity there. A net time saving is conditional, not established by fewer late merges alone.** | Early merging can delay continuing traffic upstream and relocate the conflict. It helps only when delay avoided later outweighs the extra travel and interaction delay caused earlier. S13 counts slower travel but assumes no additional upstream receiving delay; the spare-upstream/constrained-exit conditions have not been jointly established over the advice range. |
| MP5: Does the simplified exit calculation determine average complete time? | **Only under its stated batch and proportional-service assumptions. Final work and final clearance alone do not determine average time.** | Two allocations can finish all traffic at the same time yet keep different amounts waiting along the way. S13's mean of half the clearance time is correct for its simultaneous proportional batch, but other arrival patterns or priorities can change that mean. Departure timing is therefore consequential whenever those restrictions do not hold. |
| MP6: Do these ingredients define a jointly justified applied VSL task? | **Not yet. The review supports a plausible merging model, but does not establish that the complete task's assumptions hold together across the same advice-speed range.** | The missing evidence concerns the joined prediction: how advice changes actual progress, whether upstream receiving stays spare or becomes restricted, how unmerged traffic waits and eventually exits, and whether all resulting time is counted consistently. Supported ingredients do not establish this whole response across an action range, or prove a useful gradient. |

The strongest compact rival should follow the qualified model's actual causal
information. S13's aggregate-plus-initial-ending-mass model remains exactly
sufficient for S13. If the replacement needs adjacent receiving as well, that
same information must be available to a lawful compact predictor, rather than
withheld to favor explicit lane state. It is not yet known whether one extra
statistic, a few continuous states, or a local spatial profile is sufficient.

An aggregate predictor with full count/speed history and state-dependent
capacity is also a serious rival. Wei's aggregate VSL model makes this concrete.
Useful speed control need not be caused by lane preparation; aggregate inflow
management or capacity-drop avoidance can provide an alternative explanation.
Those model-form explanations should be compared honestly, without inserting
their different laws into a purported information-only comparison.

[Wei, Han and Wang: primary aggregate VSL model](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

For one scalar action, analytical references where available, finite-difference
sensitivities and bounded direct search remain strong methods. A correct and
externally useful gradient can coexist with a compact predictor and successful
direct search. This review establishes no optimizer advantage, reachable
full-history collision in a new model, calibrated parameter prevalence, or
external gradient usefulness. Its connection to the urban task remains the
shared information → service/departure → sensitivity → useful perturbation
question, not a claim that the same traffic mechanism or discrete order is needed.

## VSL-B1-G1: how much of the preparation/exit interface may change?

**Problem statement.** Must Option B preserve the sequential two-group,
scalar-to-batch interface, or may it retain the smallest local receiving and
within-cohort timing distinctions required by a source-supported transfer model?

**Assumed model-chain function.** Preparation and exit service together must
determine feasible transfers, all consequential traffic delay, and departures
under the same common action. Their interface must carry enough information
for that prediction, while remaining elementary.

**Core gap.** A locally defensible transfer mechanism has been identified, but
the old interface's sufficiency is not established when target receiving or
arrival/service chronology matters. Choosing a new state, speed response or
timing law changes the methodological stack. The review stops before doing so.

**Ownership and dependencies.** Type 2, owned by the user under G3 and
VQ3-P/T/S. G1's elementary role remains fixed. G2/VQ2 must subsequently check
observation and compact-rival fairness; G4/VQ4 must check preservation of complete
accounting and derivative meaning. No production milestone is opened.

### B1-R — require a restricted sequential reduction

Continue qualification only for a source-based reduction that can justify
nonbinding preparatory receiving, an equivalent continuing group and the
declared batch/service conditions over its common-action domain. The transfer
law may be revised; S13's fixed time hazard is not mandatory. A fastest-only or
information-independent result is an admissible outcome.

**Pros.** Gives the clearest analytical benchmark and strongest chance of an
exact compact predictor. It limits state, keeps preparation and exit modules
separate, and makes derivative/reference checks transparent.

**Cons.** The restrictions are not jointly qualified by this review. Enforcing
them may exclude the lane-service differences motivating revision, or remove
the useful preparation effect. This cannot be described as applied admission
merely by retaining simple equations.

**Dependencies and consequences.** MP6 must justify all restrictions together;
MP3 and MP5 must establish interface sufficiency. Failure returns to this gate
or an explicitly conditional task role, rather than adding hidden receiver
corrections. A changed transfer/action law still needs approval before adoption.

### B1-L — permit a bounded local receiving and chronology amendment

Allow the candidate reduction to distinguish the ending lane, its adjacent
receiver and the farther continuing lane wherever those roles affect service.
Permit preparation and exit service to exchange local receiving conditions and
time-resolved flows, with upstream feedback represented when consequential.
Use Carey's simple mandatory-transfer framework as the provisional principal
reduction candidate; assess a declared allocation rather than assembling a
hybrid of source equations. No number of spatial segments, exact state vector,
allocation, speed-to-flow response or lane-end boundary is selected by this permission.

Keep one finite cohort and one common bounded action. The next bounded contract
proposal must justify each additional state and return to this gate if a large
spatial/behavioral model is required. It must allow compact sufficiency and a
negative useful-preparation result. This is permission to propose and qualify
the smallest amendment, not permission to implement it.

**Pros.** Addresses receiving, grouping, early/late costs and chronology together.
It allows the modeled traffic to determine whether preparation pays, instead
of assuming that benefit at the handoff. A small continuous interaction region
could preserve the elementary role and make its information requirements explicit.

**Cons.** More continuous state and event structure may be necessary. Source-to-
reduction validity, common-speed response and compact sufficiency remain
unproved, and the useful direction may disappear. This could exceed the task's
intended simplicity; permitting the amendment is not proof that it will succeed.

**Dependencies and consequences.** Explicitly relax the G3 starting grouping
and scalar/batch interface for qualification only. Keep G1, the physical common
action and complete-time objective unchanged. Close the resulting global state,
response and timing contracts before local transcription; then audit G2/G4
consistency. Do not promote the full spatial Candidate C automatically.

**Provisional recommendation: B1-L.** The main evidence gap concerns the relation
between transfer and local service, not just the formula for a merging rate.
Permitting the smallest receiving/timing amendment lets Option B address that
gap without committing to a larger simulator. B1-R remains viable if a carefully
restricted analytical role is preferred. If neither can remain elementary,
stop applied refinement and discuss the task role rather than expand it by default.

The authorized B1 review is complete. Feedback 3's subsequent component
diagnosis is delivered, and the user accepts its general flow and most details.
The explicitly requested improvement proposal is delivered as P1 and now
approved as the bounded continuation. Its review-direction/proposal discussion
is closed. The next allowed action is P1's remaining state, motion, receiving,
timing and joint-domain qualification, ready to open without another broad
plan. Approval does not select every broader B1-L amendment or freeze exact
joined laws. Stop that review at its completed gate or any further methodological
choice affecting the stack. This approval exchange performs no such review,
implementation, traffic experiment or evaluator selection.

[Source locations, adaptations and unresolved interfaces](../../extraction/research_readiness/vsl_b1_source_and_interface_audit.md)

[Work record and document validation](vsl_b1_work_report.md)
