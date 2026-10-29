# The merging rule can follow traffic; its receiving state now needs a closure

The review establishes a concrete local causal model for P1: **occupied space
limits what the adjacent through lane can accept; its own forward traffic
claims part of that service; merging uses what remains.** Accepted traffic
then changes the receiving lane's occupancy and can change later service. This
is the requested joint dependence between traffic state, available service and
completed merging.

The first further methodological choice is how the elementary task predicts
that receiving state over time. The old ending/combined-continuing masses do
not generally determine it. Even adding the current receiving limit is not a
general autonomous closure: identical limits can hide different remaining
storage. A compact state or a justified restriction may suffice, so the finding
does not force a full lane model. It does require us to choose and qualify the
receiver/motion representation before treating P1 as a complete replacement.

Date: 2026-10-13. Status: **VSL-B2 executed to its first further methodological
choice, VSL-B2-G1.** Local source dependencies and reference calculations were
reviewed; no receiver-state enlargement, new motion law or applied task was
adopted. The remaining joined-domain review stops here, as the approved plan
requires.

**Post-gate route choice, 2026-10-13.** The user chose B2-A for the first
qualification review while keeping B2-B available if a compact representation
cannot account for a consequential spatial dependency. This selects a review
order, not a receiver model or law. The original gate wording below remains
the delivery-time record; the updated return rule follows its source links.

## The big picture: service must be predicted before its gradient can guide speed

The VSL companion asks whether retaining the right traffic information helps
predict useful common-speed changes. That question depends on a coherent
forward chain: advice changes physical progress and service opportunities;
available service determines feasible merging; the resulting traffic and
unfinished merging determine complete travel and waiting time.

P1 repairs the place where S13 prescribed completion from elapsed time. The
present review shows how to replace that prescription locally. It also shows
why a traffic-dependent receiver cannot simply be attached as an external
input: if future acceptance is supplied from outside the predictor, we have
not established the information-to-service relationship we intend to verify.
We must predict it from admitted initial information and the same physical
advice used by every comparator.

This is a task-model decision, independent of simulator implementation. It
precedes a new information witness, derivative validation and independent
gradient-usefulness evidence. S13's accepted conditional result remains intact;
none of those stronger results is transferred to P1 by this review.

## What lane-change model can now be formed

The candidate is an elementary mandatory-request model with own-lane priority.
Traffic physically available in the ending lane requests a merge. The adjacent
target's occupied space and capacity limit receiving. Traffic advancing within
that through lane gets its feasible service first. The remaining budget admits
as much requested merging as its gap-work allowance permits. Accepted mass
leaves the donor and enters the target once; an unsuccessful request stays
unmerged and may advance in its ending lane if that motion is feasible.

Carey's R1 and its CTM receiving context provide the source basis for this
local structure. The native update carries local occupancies and residual
traffic. It does not supply the desired compact common-VSL lane-drop task
without a reduction and action/boundary qualification.

The paper defines R1 explicitly; its numerical examples use R2's proportional
sharing. The local rule is source-backed as a model candidate, while its
suitability for this VSL regime remains unverified.

[Carey et al., primary manuscript, §§2–5](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

Two aspects of through-lane conditions matter here. **The target's occupancy
limits acceptance; the approaching own-lane traffic claims that acceptance.**
A clear target can still offer little spare service if own traffic uses its
available budget. A crowded target can restrict both flows. Speed alone is
not a sufficient description of either relationship.

The accepted merge also enters the target's stock balance. Priority protects
the continuing traffic's immediate allocation; it does not erase the mass
that has moved into its lane. Consequently, the rule is a coupled traffic
process, even with very simple merge desire. It is not a new guaranteed
completion fraction with a congestion correction attached.

### Making the P1 example depend on traffic state

In the original illustration, six units are ready to merge, own traffic
requests four units, and each merge uses twice an ordinary unit of receiving
work. The reviewed receiving relation can generate the ten/four budgets from
different target occupancies: a target with ten occupied units offers ten
units of receiving work; a target with twenty-two occupied units offers four,
under the declared illustrative storage/capacity parameters.

Own traffic receives four units in both cases. Three units merge in the first;
none merge in the second. The target therefore receives seven or four units
of actual traffic. The gap allowance consumes service work, not additional
vehicle mass. This makes the original allocation example a state-to-service-
to-merging example, rather than leaving the receiving numbers unexplained.

Those quantities are reference arithmetic, not calibrated task parameters or
a traffic experiment. The complete equations and assumptions are in the
supporting note.

[Mathematical explanation and checked examples](../../synthesis/research_readiness/vsl_b2_joined_service_contract.pdf)

## Why the current receiving limit cannot simply become the new state

A receiving limit reports how much can enter now. It can conceal how much
spare storage remains before receiving starts to fall. Imagine two target
sections that both currently permit ten units of receiving work. One contains
ten units of traffic and the other twenty. Both receive seven units and release
two. Their resulting stocks are fifteen and twenty-five. Under the same
illustrative receiving relation, the first still permits ten units; the second
now permits only seven and a half.

| Quantity | Less occupied target | More occupied target |
|---|---|---|
| Current receiving limit | Ten | Ten |
| Own traffic served | Four | Four |
| Completed merging | Three | Three |
| Actual inflow / outflow | Seven / two | Seven / two |
| Next receiving limit | Ten | Seven and a half |

The current service and all these current flows are identical. The future
service differs because the current receiving limit hid different occupied
stocks. Combined continuing mass can also be held identical by compensating
in the farther lane. Thus the old grouped masses plus the current receiving
scalar do not generally predict the next receiving limit in this family.

The finding is specific. It does not prove that another scalar cannot suffice,
that history cannot reveal the stock, or that the elementary task must retain
every lane and position. A restricted state family might let us infer the
receiver's stock from existing masses and initial conditions. A compact stock
variable might otherwise be enough. But either route needs an autonomous
outflow and availability law as well: knowing stored mass does not by itself
predict the downstream constraint or the next own-lane demand.

That is the new decision. We have a local allocation law; we have not yet
chosen the representation that makes its inputs evolve consistently.

## How this fits the original stack

| Original component | Present finding and exact change status |
|---|---|
| **1. Geometry/population and grouping** | Keep the finite cohort and three-to-two geometry. Ending/combined-continuing masses do not generally determine local receiving. A sufficient restriction or receiver-state representation now requires a decision; no lane-state size is selected. |
| **2. Advice and response** | Keep one common bounded advice action. The native fixed-speed cell motion does not automatically define changing realized speed on fixed geometry. The physical action mapping remains to qualify with the chosen representation. |
| **3. Longitudinal progress** | The candidate needs physically available donor traffic, own-lane demand and target outflow. S13's common traversal time supplies none of those local dependencies in general. A compact motion closure may suffice, but is not adopted. |
| **4. Mandatory transfer** | P1's receiving-constrained completion direction is approved. R1 now has an explicit source-supported local state/service interpretation. Whole-task availability and shared donor sending budgets still require the surrounding closure. |
| **5. Preparation receiving** | The approved change from assumed slack to checked acceptance is retained. The local stock-based receiving relation is a credible ingredient; its autonomous task realization is the current gate. |
| **6. Choke and departures** | Preserve the receiving-work concept. The common-traversal/proportional-batch reduction remains conditional; no new arrival, exit priority or lane-end law is selected. |
| **7. Complete-time objective** | Keep travel and waiting until all cohort mass exits. Its calculation must follow the eventual joined trajectory; final work or clearance alone cannot generally determine the mean. |
| **8–9. Information, comparators and sensitivity** | Keep fair initial information, autonomous forecasts and separate gradient evidence. Neither full lane necessity nor new useful gradients follow from the local receiving counterexample. |

The primary approved substitution remains component 4, with component 5's
explicit assumption change. The additional representation/motion requirement
is exposed as a shared interface choice, not silently absorbed into that
component. Source free-flow cells are tied to one fixed speed and interval;
changing cell length with advice would alter the geometry, while leaving the
native advance unchanged would leave the speed-to-progress meaning unresolved.

## Direct answers for MP1–MP6 and the compact rivals

| Question | Answer from this pass |
|---|---|
| **MP1: opportunity and clock** | **Eager requests can be elementary, but the common-speed opportunity clock is not yet closed.** The physical donor/progress model must determine which traffic reaches each opportunity; extra elapsed time does not guarantee extra completion. |
| **MP2: feasible completion** | **Own-lane priority gives a definite receiving-limited local completion rule.** The checked examples respect receiving work and paired mass. Full available-traffic and aggregate donor-sending semantics remain dependent on the motion closure; no complete fixed-geometry update is certified. |
| **MP3: continuing grouping** | **The old grouping and even a current-receiving scalar are not generally sufficient.** The new one-balance counterexample identifies hidden receiver stock. A restrictive inference or compact autonomous state remains viable; full spatial lane state is not proved necessary. |
| **MP4: early/late costs** | **Feasible early merges can alter later receiving, so immediate priority does not establish cost-free preparation.** Net time and early/late compatibility remain to evaluate after the receiving/motion contract closes. |
| **MP5: departures and mean time** | **The old mean-time reduction still needs its common-arrival and proportional-service conditions.** This pass does not establish those conditions for the coupled candidate; no departure replacement is adopted. |
| **MP6: joint regime** | **A complete applied regime is not admitted.** Receiver/motion closure is unselected; the same advice range, timing restrictions and eventual lane-end clearance have therefore not been established together. |

The strongest compact rival remains important. S13's initial ending-mass
scalar still reproduces S13 exactly. Adding a current receiving limit can
reproduce the local allocation when its other inputs are known, but the
counterexample defeats a general future update using that limit alone.
A compact predictor with a sufficient receiver stock or informative history
is not defeated. Aggregate VSL/history/capacity-drop models remain serious
rivals: a snapshot ambiguity is not a reachable equal-full-history certificate.
No optimizer advantage is claimed; analytical sensitivities, finite differences
and direct search retain their later comparison role.

## VSL-B2-G1: what representation should predict receiving over time?

**Problem statement.** Which smallest receiver and physical-motion closure
should P1 use so that traffic predicts its own future receiving service under
the common advice, rather than receiving being supplied externally?

**Assumed model-chain function.** This closure supplies available ending traffic,
own-lane demand, local occupied space and outflow to the approved transfer rule.
Accepted merges feed back into it. It also determines the timing information
available to exit service and the complete-time objective.

**Core gap.** The source supplies these quantities through spatial lane dynamics;
S13's cohort totals and common travel duration do not generally recover them.
The receiving scalar loses stock information on the capacity-limited branch.
We must choose a reduction or a small spatial representation and justify its
restrictions. That changes shared state/motion meaning, so it is a Type 2
G3/VQ3-P/T/S decision, with G2 information and G4 timing consequences. It cannot
be settled by source transcription or a numerical convention.

### The choice in plain terms: how much of the target lane must be remembered?

Both routes keep P1's mandatory merge requests and through-lane own-traffic
priority. Both must let the same fixed-geometry, common-speed task predict
future receiving from its own traffic. They differ in the meaning of the
receiving state: **is the amount of traffic in a short merge area enough, or
does it matter where that traffic sits within the area?**

The checked example above shows why some occupied-space information matters.
Two targets can each accept ten units now and handle exactly the same current
flows, yet a target holding ten units and one holding twenty next accept ten
and seven and a half. A model that remembers only today's receiving number
cannot tell them apart. This example supports a compact *stock* explanation;
it does **not** show that positions must be tracked.

For the remaining distinction, imagine two equally full target areas: one
has a queue near the downstream exit, while the other is crowded near the
merge location. A one-stock description gives them the same local state if
its other admitted inputs also match. A position-aware description can tell
them apart, so it could predict different times at which space opens for a
merge. This is a conceptual test of what the representations can express,
**not** a demonstrated reachable witness or a proved VSL benefit.

| Direct comparison | B2-A: one accountable local stock | B2-B: a short position-aware region |
|---|---|---|
| **Core idea** | The merge area acts as one traffic container: incoming and outgoing mass change its occupancy, which changes later receiving. | Keep a short road segment's traffic locations because local crowding, progress and downstream release may affect acceptance at different times. |
| **Main change from S13** | Give the target an autonomous occupied-space and physical-motion account, inferred from old state if defensible or added as the smallest continuous state. | Add bounded local lane-position state and motion for the ending and adjacent lanes, plus the downstream boundary needed to evolve it. |
| **What it distinguishes** | Targets with different stocks even when their current receiving limits match. | Those stock differences and, if the law supports it, different queue locations at the same total stock. |
| **What could defeat it** | Position-dependent blockage, donor arrival or outflow may make one stock insufficient over the admitted advice range. | Extra spatial detail may add an independent modeling program without improving the elementary task's information test. |
| **When justified** | A closed, physically defensible reduced state predicts receiving, available donor traffic and exit timing. | A concrete service or timing dependency cannot be represented by the compact closure within the task's useful scope. |

### B2-A — qualify the compact account first

**Modeling philosophy.** Keep only the traffic memory needed for future
service. The target's occupied stock rises when own traffic and accepted
merges enter and falls when traffic leaves; its resulting space constrains
the next receiving opportunity. Common speed must affect the physically
available traffic and movement on the same fixed road. A known or constant
outflow cannot simply be supplied to make the bookkeeping easy.

**Main change and possible result.** First ask whether the existing grouped
masses and declared initial conditions already determine that target stock in
a defensible restricted task. If they do, the old state may support a compact
closure. If they do not, the smallest additional continuous stock is a
candidate change requiring a decision and fair initial information for every
comparator. Either way, the task needs a justified local movement/outflow law;
stock alone is not the whole lane-change model.

**Pros.** This is the smallest plausible change to the accepted stack and
the strongest compact information rival. If it closes, an elementary
information/gradient test may remain analytically clear.

**Cons.** Carey's spatial source does not establish a one-stock reduction.
Queue location, changing downstream supply or arrival timing may defeat it.
It may also remove the preparation advantage the task hoped to study.

**Dependencies and consequences.** Qualify the region, storage, donor
availability, outflow and speed response together. Recheck G2 information
fairness and G4's complete-time chronology. The common traversal and
exit-batch simplifications survive only under proved restrictions.

### B2-B — qualify a short position-aware region if needed

**Modeling philosophy.** Keep just enough local road position to know whether
traffic can reach the lane end, where the adjacent lane has room and when
traffic clears downstream. Occupancy, movement and acceptance then evolve
together under P1's same request and own-lane-priority rule.

**Main change and possible result.** The old grouped cohort gains bounded
local ending-lane and target-lane occupancy and motion, with a declared
downstream boundary. This could preserve queue-location effects that one
stock cannot. It does not commit to a cell count, whole-road lane expansion
or the earlier full-model Candidate C.

**Pros.** It follows the source's local occupancy/progress/receiving
dependencies more directly and can express spatial crowding where the compact
account cannot.

**Cons.** It changes more of the state and timing stack, may exceed the
elementary companion role, and still does not establish the speed actuator,
lane-end clearance, source regime or useful gradients.

**Dependencies and consequences.** Establish the smallest consequential
region and shared donor/receiver budgets under G3, then recheck G2's initial
information and G4's exit timing. A substantial spatial program would call
for reconsidering the elementary task's scope, not automatic promotion of C.

**Provisional recommendation: qualify B2-A first.** The checked result proves
a missing stock distinction, while position sensitivity remains a plausible
but unproved further need. A compact closure deserves the first bounded
qualification. If it fails on a concrete service or timing dependency, bring
that evidence back before selecting B2-B. Neither route, any extra state, nor
any exact motion law is adopted at this gate.

The pass stops here. The next allowed action is the user's decision on the
receiver/motion qualification route, followed by its bounded methodological
review. No new representation or dependent traffic law is adopted in this pass.

[Source audit and complete viewed-paper reference list](../../extraction/research_readiness/vsl_b2_source_and_reduction_audit.md)

[Work record and verification limits](vsl_b2_work_report.md)

## Post-gate choice: try the compact account, retain the spatial return route

The user's analogy captures the main difference. B2-A treats the merge
opportunity like a local choke with an accountable amount of occupied space:
traffic entering and leaving changes what it can accept next. B2-B models a
short merging region and can additionally distinguish where traffic is along
the road. It is a *potential* generalization in that spatial sense. It is not
automatically a strict mathematical extension: A would have to arise from
B under matching priority, boundary, movement and timing assumptions before
that inclusion could be claimed.

Here the "local choke" analogy describes an aggregate account of *upstream*
merge opportunities and adjacent receiving. It does not relocate every
early attempt to the permanent lane end. Both qualification routes retain
a later compulsory, service-limited request for residual ending-lane
traffic; the exact lane-end law remains a shared question.

**Accepted review order.** Qualify B2-A first without assuming its one-stock
closure is valid. Ask whether it can predict the available donor traffic,
the target's own demand, local receiving, outflow and resulting complete time
under the same fixed geometry and bounded common-speed advice. Any restriction
that makes this possible must also leave a meaningful elementary task and a
fair comparison with simpler predictors.

**When to return to B.** If A needs an arbitrary future receiving or outflow
input, an unjustified instant-mixing assumption, or an advice-range restriction
that hides consequential queue location, donor arrival, spillback or exit
timing, stop and identify the smallest spatial region that would restore the
missing dependency. B remains a candidate; it is not adopted automatically.
The reason should be a concrete traffic prediction A cannot make, not merely
that a spatial model is richer.

**What B would not cure by itself.** If the obstacle is whether own-lane
priority is the right allocation, how common advice changes physical speed,
or how unfinished traffic is served at the permanent lane end, adding
longitudinal positions does not decide that law. Reopen the smallest affected
shared contract instead of treating B as a general rescue.

The next allowed action is the bounded B2-A qualification. It stops at its
completed review gate or the first new choice that changes shared traffic,
information or time semantics. No simulator work or applied MP6 regime is
authorized by this route choice.
