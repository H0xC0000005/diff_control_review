# SUMO validation: restricted-task usefulness, then natural-lane-drop transfer

**Current decision:** C-P coupled point qualification with choke-line
completion is accepted; S3-M2's representation/objective choice is closed.
Exact coupled-law and reference qualification remain open. S3-M1's ladder
stays fixed; earlier candidate statuses below are historical.

[Accepted direction and current gate closure](vsl_step3_coupled_point_decision.md)

**Current qualification, 2026-10-14:** the user's through-traffic disturbance
discussion reframes S3-M2 around compulsory-service coupling and the
completion domain. Point-versus-finite junction geometry alone does not
establish that mechanism. The accepted ladder remains fixed; no revised
primary law is approved. This earlier bridge remains supporting history.

[Current traffic reasoning and revised gate](vsl_step3_merge_feedback_and_completion_response.md)

**SUMO is selected for the independent reference, 2026-10-14.** The user
approved proceeding with this direction and completing the validation chain.
The present work executes its documentary qualification. It does not build
the reference or run a traffic experiment.

The central question is straightforward. Our elementary model may suggest
a lower speed because it predicts that better preparation will save more
forced-merge waiting than the slowdown adds in travel. SUMO should receive
that speed limit and determine the traffic outcome through its own vehicle
interactions. We can then ask whether the suggested change actually helps.

Most of that bridge can now be specified: the common intervention, finite
population, causal preparation, observation roles, independent service,
complete-time accounting, parameter provenance and comparison sequence.
**The user has accepted the ordered ladder:** verify/optimise H1/T1, validate
the restricted task with SUMO S-P, then test transfer with SUMO S-L. S3-M1's
evaluation-strategy choice is closed. The cutoff is preserved in S-P and
explicitly relaxed in S-L's transfer condition. The earlier alternatives
and recommendation history below explain that decision.

Step 2 remains closed and unchanged. The resumed source/evidence review and
protocol assembly are delivered at VSL-S3-G1. Step 3 remains open for S3-M2's
point-versus-finite S-P boundary selection and protocol freeze. Step 4 is
unopened. The earlier S3-M1 options below are decision history.

[Current traffic findings and final physical-reference gate](vsl_step3_reference_qualification_and_final_gate.md)

[Accepted ladder and current decision closure](vsl_step3_validation_ladder_decision.md)

## The validation chain in traffic language

Start with a physically feasible traffic preparation and its actual recorded
past. The controllers receive only their admitted initial information. The
elementary predictor estimates how each possible common advice changes
preparation, arrivals, forced waiting and complete population-time. Its
gradient supplies a feasible direction, or an optimizer supplies one fixed
advice. SUMO receives that intervention on a replay of the same preparation.
Its vehicles respond to speed limits, gaps, braking and the chosen merge
geometry. Every member of the initial cohort is followed to the agreed exit.
The resulting complete time answers whether the predicted improvement survived.

This makes SUMO the **benchmark reference**. A good outcome is credible evidence
against the selected richer traffic model, including behavior absent from H1.
Its designation as reference truth does not establish field accuracy for this
particular lane drop. The network, driver assumptions and calibration remain
part of the result's stated scope.

There are three different questions along this chain. First, can omitted
ending information change the preferred action inside H1/T1? Second, is the
implemented H1/T1 derivative correct? Third, does following it help in SUMO?
A positive answer to one does not stand in for either of the others. SUMO
also need not provide a differentiable objective: applying the suggested
speed changes and measuring their outcome is enough to test usefulness.

## What must remain common, and what SUMO determines independently

| Part of the chain | Direct contract and meaning |
|---|---|
| **Road and population** | Use one permanent three-to-two drop, the same declared preparation/terminal geometry, and a fixed decision-time cohort. No later arrivals enter the evaluated task. The terminal starts empty. The remaining terminal interpretation is the gate below. |
| **Control** | Apply one constant, common, bounded permitted speed to the task's declared lanes from the decision onward. It is the same numerical advice passed to H1. Native acceleration, safety and congestion determine actual speed in SUMO. Their difference from H1's ideal response is prediction error to examine. |
| **Early intention** | Every eligible dropping-lane driver has a reason to join the adjacent lane. An external request generator may expose this intention in preparation; it supplies requests, not completed transfers or future gaps. A fixed selected fraction would be a separately declared demand variant, not a return to a fixed completed proportion. |
| **Realised merging** | SUMO's safety, motion and selected native lane/junction interactions determine completion and delay. Do not impose H1's spare-receiving calculation or its work-weighted outflow as the reference's realised service. |
| **Initial model state** | Project actual cohort counts into the predictor's total and ending mass, using one ordinary reference vehicle as one vehicle equivalent. The predictor retains its uniform-footprint assumption. Native gaps and positions are richer reference state, not new state given to G. |
| **Available information** | Give A the complete admitted aggregate history and lawful inference; give A+E the initial ending statistic as well. G receives the equivalent coarse lane state. Full reference trajectories are evaluator records, not a source of extra controller information. |
| **Objective** | Sum each initial vehicle's elapsed time from the common decision to crossing the agreed completion section, including the last vehicle's clearance. Compare this with population-count integration as an independent accounting check. |

[Speed-limit intervention](https://sumo.dlr.de/docs/Simulation/Variable_Speed_Signs.html)

[Requests, native motivations and safety](https://sumo.dlr.de/docs/TraCI/Change_Vehicle_State.html)

The early request interface is useful because the two terminal mappings do
not create identical native incentives. A lane with no onward connection
creates a route-driven need to change lanes. A lane with a valid yielding
connection at the boundary can continue through that connection; early
requests may therefore need to be supplied explicitly. Neither mapping
should be assumed to produce the same preparation merely because both are
called a lane drop.

## Finite vehicles can represent the same amount of traffic without rounding the predictor

Declare the reference cohort first and use its exact lane counts as continuous
vehicle-equivalent masses in H1. That avoids rounding an already specified
continuous scenario into a different population. The analytical family also
contains compatible integer-count members: for a common total of 24 vehicles,
its lower-ending proportions give 12 ending, 6 adjacent and 6 other continuing
vehicles; its higher-ending proportions give 14, 5 and 5. Integer multiples
preserve those proportions. This is only a population arithmetic example,
not an adopted size, calibrated density or proof that the corresponding
microscopic preparation is feasible.

Actual positions and gaps must pass native feasibility checks. Their average
lane densities can initialise H1, but individual vehicles do not create an
exact continuous uniform density field. Record this approximation rather
than claim state equivalence. In particular, the analytical proof of identical
complete histories cannot be transplanted into SUMO by relabelling lanes or
by ignoring differences in the recorded past.

Use a causal loading recipe and choose the decision point before any evaluated
vehicle enters the terminal. All evaluated vehicles must already be present,
with no insertion backlog or scheduled later arrival for that cohort.
Replaying the same prefix for each advice preserves the initial situation.
A saved snapshot alone is insufficient because the official state documentation
lists unsaved internal lane-change and some car-following state.

[Insertion and delayed departure](https://sumo.dlr.de/docs/Simulation/VehicleInsertion.html)

[State/replay limitation](https://sumo.dlr.de/docs/Simulation/SaveAndLoad.html#known-issues)

This remains a finite-cohort task. A failed initialisation is not repaired by
silently introducing streaming demand, forced insertion, fractional microscopic
vehicles or loss of traffic. The later execution plan must specify the fixed
count/position construction and its checks before looking at advice outcomes.

## The initial-information result and the SUMO result have different evidential jobs

The H1 construction already establishes a complete aggregate-history ambiguity
and exact sufficiency of the ending scalar. Those results remain conditional
on its closed law. For factors one through two, the constructed pair shares
the fastest optimum; sufficiently large shared late-work factors can instead
separate preferred actions. The positive range remains unqualified as traffic.

SUMO's first role is to judge predicted speed changes on admitted physical
preparations. A claim that its own aggregate observations cannot select the
right action would additionally require its own observation/inference evidence.
Matching only total mass at the decision cannot establish that stronger claim.
If an aggregate history estimator recovers the ending statistic, retain that
recovery as a sufficiency result.

The aggregate observer is a declared lane-blind channel set, not the whole raw
SUMO output. Lane labels and lateral coordinates are additional information.
Declare the channel set and record construction before outcomes; preserve
every admitted channel and inference in A. Lane-resolved evaluator data may
audit the task, but must not leak future merging or receiving to any predictor.

## Complete time includes everything the advice can change

Use a fixed completion section after the chosen compulsory interaction.
Every initial vehicle contributes until it crosses that section. Upstream
preparation travel, deceleration, terminal approach, merge waiting and any
driving inside the boundary connection all count. A downstream continuation
may prevent artificial network-end effects, but its later travel is outside
the objective and it must not create another bottleneck affecting the task.

SUMO's trajectory output supplies front-bumper positions and native lane
identity. Use a consistent front-crossing convention and record the numerical
time resolution. TripInfo is a cross-check, not a substitute: its duration
starts at insertion, and unfinished trips are omitted by default. Low-speed
waiting and time loss also have different meanings from complete population-time.

[Trajectory fields and position convention](https://sumo.dlr.de/docs/Simulation/Output/FCDOutput.html)

[TripInfo and unfinished population](https://sumo.dlr.de/docs/Simulation/Output/TripInfo.html)

Disable task-removing teleportation and account for all IDs. A nonclearing
cohort, collision or removal fails reference admission; it is not a short,
apparently successful TST. An execution horizon based on H1's fluid clearance
bound is not automatically a clearance bound for SUMO. The later numerical
plan must specify its continuation, failure and resolution rules in advance.

## Parameters should explain observed behavior before they explain a preferred policy

Geometry, population and speed bounds are common supplied inputs. SUMO's
driver and safety parameters belong to the independent reference and need
source/version provenance. H1's opportunity, receiving and extra-work
parameters are effective predictor parameters, not aliases for a SUMO flag.
For example, a gap-acceptance setting is not a direct measurement of the
constant late-work factor.

Fit or bound the effective predictor parameters against development traffic
traces: early transfer counts, continuing/ending departures, residual stock
and complete delay. Use one parameter set across the declared advice range
and observer comparisons. Retain jointly unidentifiable parameter ranges;
one discharge trace is not enough to claim a unique decomposition into
receiving and extra work. No parameter may be fitted to the held-out preferred
advice or selected solely because it enters the positive analytical range.

An unsuccessful joint fit is useful evidence about the elementary model's
scope. Record it and reopen the smallest affected contract if a new law is
needed. Do not add a downstream metering signal, prescribed exit headway or
fixed-work Python server just to make SUMO reproduce H1. Factory settings may
define a reproducible synthetic benchmark; they do not supply field calibration.

The present sprint selects no numerical traffic parameters and fits nothing.
The exact dataset, fit criteria, tolerances and held-out manifest belong to
the separate execution proposal after the terminal meaning is closed.

## What the comparison would establish

After internal forward/conservation and derivative verification, transfer
identical feasible advice perturbations to each fixed reference preparation.
At the fastest bound, test feasible decreases; elsewhere retain both feasible
directions. Report predicted sign, actual complete-time change and action
ranking separately. Small-step and resolution checks belong to execution.

Then evaluate the selected fixed advice, alongside fastest/slowest endpoints,
the admitted aggregate peer and the scalar-equivalent A+E/G forms. Analytical
sensitivity, finite differences and bounded scalar search remain serious
optimizer rivals. A direct search on the same predictor separates optimizer
effects from model effects; a budgeted search in SUMO supplies a richer
decision benchmark. Its objective-call cost must remain visible.

Neither an interior optimum nor a representation advantage is an acceptance
requirement. A correct gradient that fails to improve SUMO time is negative
transfer. A correct gradient that helps while direct search also works is
usefulness without optimizer superiority. A+E/G agreement establishes compact
sufficiency inside H1; SUMO's microscopic representation does not make full
lane/identity/order state necessary for the predictor.

## The terminal question: are we testing a restricted road or a predictor approximation?

**Decision history.** The user subsequently accepted S-P first and S-L as
the transfer condition. The options below retain their rationale and limits;
the choice of assessment order is closed in the linked decision record.

**Problem statement.** Does the reference enforce no further lateral merging
between the preparation handoff and the compulsory boundary, or let a normal
ending lane's remaining drivers find gaps there?

**Assumed model-chain function.** This is the last physical step that turns
unfinished preparation into delay and complete TST. H1 stops early sources
at the handoff; T1 moves each lane through a finite reach and serves the
remaining ending traffic at a priority boundary. The independent reference
must give this step a physical meaning while producing its own service.

**Core gap.** The accepted cutoff is a declared analytical adaptation, not
an established lane-drop fact. SUMO supports a normal dead-end lane and
converging lane connections with right-of-way. They create different
opportunities for the same unfinished drivers. The selected simulator does
not determine which physical interpretation the benchmark is meant to test.

Imagine ten drivers still in E at the handoff, while A is crowded. In a
restricted terminal, those ten remain in E and seek service at the boundary.
In a normal ending lane, some can use gaps while approaching it, including
while slowing. The second case can leave fewer drivers for the final conflict
and can alter the travel-versus-waiting balance. That is the central mechanism
of the task, not incidental implementation detail.

### S-P: a restricted terminal followed by a native priority connection

Retain the cutoff as a physical benchmark restriction. No lateral lane changes
occur on the ordinary terminal lanes. At the downstream boundary, E and A
feed the same outgoing lane, while B continues separately. E yields to A;
SUMO's junction gaps, braking and downstream motion determine actual service.
An early request generator may be needed because E now has a valid onward
connection. No fixed-work fluid server is inserted into SUMO.

**Pros.** Closest physical counterpart to the closed handoff and boundary
priority; preserves the direct restricted-task comparison and contains the
remaining compulsory queue in real road space. Native interaction can still
disagree with H1's constant work approximation.

**Cons.** Represents a deliberately restricted approach and an intersection-
style yielding connection. Connection geometry, internal motion, turning
speed restrictions and approach visibility can introduce delay different from
normal freeway merging. Those effects need their own admission and full-time
accounting. A right-of-way rule does not prove that continuing traffic never
slows. The docs themselves caution that double connections are unsuitable
for some ordinary motorway merges.

**Dependencies and consequence.** G3 fixes the terminal as a task restriction;
G4 bounds usefulness to this constructed benchmark. Inspect explicit generated
priority rather than rely on defaults: the PlainXML page gives inconsistent
left/right default-priority descriptions in two sections. Internal-link
choice and geometric/time budgeting must close before a build. There is no
primary equation change, but this is a declared reference interpretation.

### S-L: a normal ending lane with native compulsory lane changes

Keep the permanent lane drop and early intention, and give E no onward lane
connection. Drivers must move into A to continue. They may seek safe gaps in
the terminal approach as well as upstream, and unsuccessful drivers decelerate
or wait near the lane end. SUMO's normal mandatory/cooperative behavior
determines the final conflict. H1/T1 remains the compact predictor, with its
cutoff and point server explicitly treated as approximations to that behavior.

**Pros.** Directly tests the intended freeway preparation/late-merging mechanism
with ordinary native lane-ending behavior. Avoids creating the penalty through
an artificial junction's turning or crossing rules. Provides the clearer first
operational usefulness test if the aim is advice for a normal lane drop.

**Cons.** Does not enforce the exact terminal cutoff or restricted priority
server. Remaining drivers can exploit additional gaps; ordinary traffic may
also slow. A positive analytical result may vanish. Initial/history and
parameter mapping still need admission, and this cannot be reported as an
exact same-law or same-restriction terminal comparison.

**Dependencies and consequence.** Reopen only G3's physical-reference
interpretation of the cutoff, with the corresponding G4 claim boundary.
The proposed consequence is a changed correspondence between predictor and
reference, not a revision of H1/T1 equations or adoption of a spatial primary
model. G2's observation fairness remains unchanged. An amendment is required
before calling the natural terminal the admitted counterpart.

[Native lane-number reduction](https://sumo.dlr.de/docs/Simulation/Motorways.html#reduction-in-the-number-of-lanes)

[Converging connections and right-of-way](https://sumo.dlr.de/docs/Networks/PlainXML.html#connection-descriptions)

[Junction motion and internal links](https://sumo.dlr.de/docs/Simulation/Intersections.html)

## Methodological consistency with the closed task

The user asked which option fits the established stack, emphasizing that
methodological consistency contributes to validation credibility.
**S-P is the closer counterpart to the currently frozen task.** It preserves
the sequence of early merging, a terminal with no further lateral transfers,
and compulsory joining under continuing-lane priority. S-L permits additional
terminal transfers and therefore needs the previously identified correspondence
amendment. Its ordinary-road interpretation does not erase that difference.

Task consistency and equation identity have different jobs. The reference
should preserve the declared geometry, merge opportunities, priority meaning,
population, intervention and objective. It may use independent gap acceptance,
braking and car-following to produce service and delay. These differences are
what make it a useful independent test. In particular, preserving priority
does not require imposing T1's zero continuing delay, fixed work factor or
predicted discharge on SUMO; doing so would weaken the independent evidence.

S-P's consistency still does not establish its physical fitness. Its native
yielding connection must represent the intended boundary conflict without
letting unrelated turning/connection geometry create the apparent benefit.
That qualification remains necessary. S-L is valuable for checking transfer
to a normal lane drop, but that is a separately declared approximation/
robustness question rather than the first exact-restriction task comparison.

**Recommendation history: qualify S-P first for the existing
restricted task.** The earlier recommendation prioritized normal-road
semantics. The user's clarification makes preservation of the accepted task
the first validation requirement, while realised service remains independent.
S-L remains a viable later transfer check if explicitly opened, or an
alternative primary reference if its G3/G4 amendment is approved. The later
accepted ladder selects S-P first and S-L transfer second; no experiment is
authorized by that strategy closure.

## Proposed validation ladder and its claims

The user proposed model-based policy training, then SUMO S-P, then SUMO S-L,
and asked whether this can build progressively stronger credibility.
**This is a sound proposed assessment ladder, provided each step supplies
evidence for its own claim.** In the present elementary task, the policy is
one selected constant advice. The user has now accepted this assessment
order. It does not open a new adaptive controller or authorize experiments.

| Accepted stage | Scientific question and possible claim |
|---|---|
| Verify H1/T1, then optimise advice in it | Is the forward calculation and full-objective derivative correct, and does the selected advice improve the model objective? This establishes internal correctness/optimisation; training success alone is not external validation. |
| Evaluate frozen advice/gradient perturbations in SUMO S-P | Does the advice help when the same restricted merge opportunities are governed by independent native interactions? A positive held-out result supports usefulness for the admitted restricted task. |
| Evaluate the same frozen advice/gradient perturbations in SUMO S-L | Does useful guidance survive native terminal gap-seeking that H1 omits? A positive held-out result adds transfer/robustness evidence for the qualified natural lane-drop setting. |

The last step broadens applicability. It does not supersede the exact-task
test or prove that every S-L configuration is more accurate. S-P and S-L
also share the SUMO engine; they are two reference conditions, not two
independent simulators. If S-P passes but S-L fails, retain usefulness for
the restricted task and report a limit of the terminal approximation.

Freeze the predictor parameters and selected advice/decision rule before
held-out reference outcomes. Development calibration may be declared, but
retuning after seeing S-P outcomes changes what is later being transferred
to S-L and must be labelled. Qualify common population/intervention/observer/
completion accounting, and compare with matched baselines within each
reference. Raw time differences between different reference conditions do
not by themselves measure policy improvement.

Successful policy transfer and useful gradients remain distinct. To attribute
usefulness to the gradient, retain the feasible small-perturbation sign/ranking
checks as well as final-advice performance. Strong compact/aggregate and
direct-search rivals remain in the protocol. No superiority, information
necessity or positive action split is presumed from the proposed order.

**Status: accepted assessment order; S3-M1 closed.** S-P is selected first;
S-L's subsequent G3/G4 correspondence relaxation and transfer claim are
accepted at the methodological level. Their actual reference mappings remain
to be qualified. No native admission or experiment has been executed.

## Direct disposition of the planned Step 3 questions

| Question | Direct answer after selecting SUMO | Remaining closure burden |
|---|---|---|
| **Q1: information and fairness** | H1's complete-history ambiguity and ending-scalar sufficiency remain established. Exact cohort counts can be shared without rounding; reference history and richer state are separate records. | Admit causal initial preparations and the actual observer record. No exact SUMO history collision is claimed. |
| **Q2: decision relevance** | Conditional action separation and the common-fastest small-work regime are retained. SUMO should judge advice without requiring either to survive. | Qualify parameter ranges on development evidence, then retain all held-out outcomes. |
| **Q3: gradient correctness** | The complete-time derivative and future convergence/AD/difference hierarchy stay fixed. SUMO judges perturbation outcomes rather than supplying the internal derivative. | Numerical implementation and error budgets require a separate approved execution plan. |
| **Q4: independent usefulness** | SUMO and the model → S-P → S-L assessment order are accepted. Advice, population, causal replay, independent service, complete accounting, provenance and comparisons have a connected draft contract. | Qualify the selected terminal mappings and consolidate Step 3. The choice is closed, but no runnable evaluator is admitted. |

This pass completes the bounded documentary work that is independent of the
terminal interpretation. **The whole Step 3 review is not yet closed.** The
new finding challenges the assumption that native lane-drop capability alone
completes the reference mapping; it does not invalidate the closed H1/T1
mathematics. S3-M1's strategy decision is now closed. The next allowed review
action is bounded qualification of the selected interfaces, starting with
S-P. Simulator development, installation, traffic experiments,
Step 4 and the ramp line remain unopened.

[Source evidence and adaptation limits](../../extraction/research_readiness/vsl_step3_reference_and_evidence_audit.md#sumo-selected-bridge-qualification-and-terminal-evidence)

[Updated first-verification draft](../../synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md)

[Work report and document verification](vsl_step3_sumo_work_report.md)
