# VSL-R1: core-mechanism qualification and first methodological gate

Latest continuation, 2026-10-13: the user accepted MP1–MP6 and opened Option B
qualification. It is delivered at VSL-B1-G1, the receiving/timing interface
gate. This report's completed R1 findings and S13 admission limits are preserved.

[Current lane-change model, stack fit, MP6 and gate](vsl_b1_lane_change_model_and_gate.md)

Date: 2026-10-12. Status: **Bounded review completed to gate VSL-R1-G1;
applied core not admitted and no replacement selected.**

## Traffic finding and significance

Slowing traffic before a lane drop can help only if it changes something useful
before the narrow exit. Giving everybody longer to travel is not enough: the
extra time must improve completed merging or another consequential traffic
process enough to repay the travel and interaction costs.

The source recheck exposes the first choice we cannot resolve as a minor
refinement. **S13 holds a merge-completion rate fixed per unit elapsed time.
The inspected lane-drop source instead makes lateral demand a fraction of
traffic demand. These are different control models when speed changes.** A
slower speed may give more time while also reducing the rate at which that
flow-based model transfers traffic. Those effects can cancel in an elementary
free-flow reduction. Distance-based lane-change desire likewise does not alone
establish a benefit from extra time.

This is not a finding that VSL cannot help or that the accepted certificate is
wrong. It identifies why borrowing conservative transfers and finite receiving
does not yet justify S13's particular action response as an applied traffic
model. Its positive analytical result remains valid under its stated laws.
We have reached a choice about the preparation model's physical meaning, before
another round of detailed equations or evaluator design.

One part of the reduction has a clearer basis: the inherited choke batch is
consistent with a gap-weighted proportional receiving allocation **if** all
class demand is exposed at once, receiving is constant and both classes are
served in proportion to their remaining masses. That is a conditional resource
reduction of the audited priority rule, not adoption of a spatial CTM.

[Mathematical audit: transfer clocks and conditional receiving reduction](../../synthesis/research_readiness/vsl_r1_transfer_clock_and_service_audit.pdf)

## Scope opened by the user

The user explicitly opened the previously proposed bounded review and required
a stop at a completed review gate or a methodological-stack choice. This step
examined the joined common-speed, completed-transfer, preparation/choke
receiving and complete-time mechanism, together with its strongest simpler
explanations. It reused S13 and accepted sources rather than opening an
unrestricted model search.

The scope includes a source-to-reduction argument and small analytical checks
of what the assumptions imply. It excludes selecting new traffic laws,
constructing a spatial simulator, calibrating parameters, choosing an evaluator,
running traffic/gradient experiments and continuing the closed ramp line.
No implementation milestone is opened. The usefulness-first contribution
mapping is accepted and is not a question at this gate.

## What the focused recheck establishes

Consider the same group of traffic approaching a three-to-two lane drop. Some
traffic is still in the lane that ends; the rest is already in the continuing
lanes. A common lower speed gives that group longer to travel through the
preparation section. It also delays everybody. The proposed benefit is that
more merging is completed before the narrow exit, leaving less disruptive work
there. The review asks whether that benefit follows from a credible traffic
mechanism and whether it repays all the added delay.

### 1. Extra time helps only if it produces enough extra completed merging

Traffic in the ending lane has to merge. How urgently it wants to merge and
how much can actually merge are separate questions. A request succeeds only
when the target lane can receive it. Knowing that drivers become more eager
near the lane end therefore does not tell us how much additional merging a
lower speed will complete.

S13 answers that question with an explicit assumption: the same fraction of
the remaining ending-lane mass can transfer per unit elapsed time, regardless
of the common speed. More time in the preparation section then means more
completed merging. This is the mechanism behind its accepted benefit.

There is another possible response. If the transfer rate falls with traffic
speed, slower traffic may merge less per second while spending more seconds
in the section. In the audit's simple case where the rate is proportional to
speed, these effects exactly cancel: the amount still needing to merge at the
lane drop stays the same. Slowing then adds travel time without that preparation
benefit. This is an analytical diagnostic, **not a simulation or a theorem about
either whole published model**; their other traffic interactions can matter.

The inspected literature gives reasons to take this distinction seriously.
Carey separates desired lane changes from the receiving allocation that allows
them. Subraveti makes desired lateral transfer a fraction of longitudinal
traffic demand, whose free-flow branch depends on speed and density. Neither
provides S13's fixed per-second completion law under common VSL. Density,
incentives and available receiving space could change the response, but their
actual roles would have to be specified.

**Finding:** the rule connecting speed to completed merging is a substantive
traffic assumption. It can change the useful direction of a speed adjustment.
The sources support the ingredients of merging; they do not yet establish this
particular control response.

[Selected primary pages and exact source locations](../../extraction/research_readiness/vsl_r1_primary_source_join_audit.md)

### 2. The simplified exit calculation makes sense within its stated conditions

At the narrow exit, traffic that still needs to merge consumes more of the
available receiving resource than traffic already in a continuing lane. Think
of receiving as the limited opportunity to admit traffic through the exit.
Extra merging work uses more of that opportunity; it does not create extra
vehicles.

S13 treats the whole group as available for service at once. Its allocation
lets both kinds of traffic leave in the same proportion of their remaining
amounts. With constant receiving capacity and no other binding sending limit,
the remaining traffic declines at a constant rate. Some leaves early and some
late, so the average time spent in this service stage is half the time needed
to clear the whole group. The audit shows how this calculation follows from a
declared receiving rule.

Those conditions matter. In spatial traffic, arrivals and receiving capacity
can change over time. Giving one kind of traffic priority also changes when
vehicles leave. The same total work, and even the same final clearance time,
need not imply the same average delay.

**Finding:** the inherited exit calculation is internally coherent under its
batch and allocation assumptions. This supports S13 as a conditional reference;
it does not establish that an actual lane drop operates in that regime.

### 3. Moving a merge upstream helps only if there is spare receiving there

A merge needs room in the target lane wherever it happens. If early merging
uses capacity that is already scarce upstream, it can create delay there.
Completing the merge earlier may therefore relocate some cost. To obtain the
intended benefit, the preparation section must have enough spare receiving
while unfinished merging at the narrow exit remains costly.

S13 already counts the longer travel time. Its simplification is to assume
that early merging creates no additional receiving delay. The review found
no source-supported operating range that establishes this assumption together
with costly late merging across the proposed speed choices. That joint regime
remains to be justified for an applied task.

There is also a concrete reason to examine the two continuing lanes separately.
The ending lane merges directly into its adjacent lane. Compare two situations
with the same total traffic in the continuing lanes: in one, the adjacent lane
is nearly full and the farther lane has room; in the other, their occupancies
are reversed. When adjacent receiving is restrictive, these situations offer
different immediate merge opportunities despite identical combined traffic.

**Finding:** treating the continuing lanes as one shared resource needs a
physical justification. S13's imposed symmetry remains valid within S13. A
source-coupled extension would have to justify that reduction or retain the
additional receiving information it needs. This establishes no universal need
for a full lane model or individual vehicle state.

### 4. The research question must remain fair to simple explanations

S13's accepted information result is conditional: matched aggregate
observations can hide different amounts of traffic still needing to merge,
with different useful speed directions. But S13 also gives a strong compact
answer. Supply the initial ending-lane mass as one additional continuous
quantity, and an aggregate model can reproduce the grouped model's subsequent
traffic, objective and derivative exactly. It predicts future merging from
that initial quantity and the same laws; it receives no future reference
outcome. The finding concerns consequential information and its compact
representation, rather than establishing a need for a larger lane model.

Other simple explanations also remain credible. The speed-scaled diagnostic
above tests whether the assumed preparation benefit survives a different
transfer response. Aggregate VSL models can retain traffic history, downstream
receiving limits and congestion-related capacity reduction. Wei's model does
this while excluding individual lane changing: it tracks cumulative counts and
groups traffic by its entry speed. VSL may help through those mechanisms too.
That model remains a separate challenger; we have not established that its
equations, observations and derivatives provide a matched comparison here.
Published continuous lane models may already contain relevant receiving
information, so lane resolution and continuous transfer alone add no novelty.

Finally, one speed variable admits strong optimization references: an analytical
optimum, a bounded search over speeds and gradients estimated from small speed
perturbations. Their success can coexist with useful gradients. The primary
question is whether the retained information produces a trustworthy direction
for improving the traffic outcome; optimizer superiority requires separate
evidence.

**Finding:** a sufficient scalar, an aggregate explanation or an equally
successful simple optimizer is a legitimate outcome of this review. None
should be weakened or excluded to manufacture an advantage. The matching
information example is established inside S13; an equivalent reachable example
in a qualified physical traffic model remains unproved. Existing field and
microscopic evidence shows that speed and lane interactions can matter, but
does not identify the fixed-time completion law or its useful-gradient regime.

[Wei–Han–Wang, primary methods §§1.2–2.1](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

[Existing common-VSL domain evidence and counterevidence](../../extraction/s06_reference_mechanism_source_audit.md)

The review establishes a coherent conditional benchmark and identifies the
physical assumptions needed to carry its result into an applied lane-drop task.
The first unresolved choice is how common speed changes completed merging.
That choice governs the benefit and the gradient, so it remains at the stated
methodological gate below.

## Admission verdict

| Burden | Result at this checkpoint |
|---|---|
| Accepted mathematical kernel and complete accounting | Preserved; no error or amendment to S13 |
| Conditional receiving-resource interpretation | Supported under the stated simultaneous-batch and proportional-allocation restrictions |
| Source-derived, speed-independent physical-time transfer rate | Not established; a flow-fraction rate has a different speed response |
| Joint early-receiving, adjacent-group and late-service regime | Not admitted; cannot infer it from common speed or total continuing mass |
| Smallest state in S13 | One initial ending-mass scalar suffices exactly |
| Applied information/gradient verification task | Not admitted at this gate; further work requires an explicit traffic-model direction |
| External usefulness or optimizer superiority | No new evidence; no experiments conducted |

This step delivers the promised bounded verdict and stops at its first
methodological choice. It is not the full model-family robustness pass or
completion of all four transition stages.

## VSL-R1-G1 — choose the primary preparation-model interpretation

**Problem statement.** Should the first VSL verification retain S13's fixed
physical-time preparation law as an explicit conditional benchmark, or should
its primary traffic model be changed to a source-coupled flow/receiving system
before an applied usefulness claim is pursued?

**Assumed model-chain function.** Advice determines realized longitudinal motion
and feasible lateral transfers. Their completed amount and interaction costs
feed receiving, departures and complete time. The derivative follows that
entire chain. Initial observations initialize autonomous prediction.

**Core gap.** No inspected primary source jointly supplies the present fixed
time rate, nonbinding early receiving, symmetric continuing resource and batch
choke under the common-speed action. Replacing the time rate with a source
fraction can change or eliminate the useful direction; activating receiving
changes state and accounting. These choices cannot be made as transcription.

**Ownership and dependencies.** Type 2; user owns the direction. This is a
concrete gate for VQ3-T with VQ3-P/S dependencies. A changed law/state/action map
requires an explicit G3 amendment; consequential observation or outcome changes
return to G2/VQ2 or G4/VQ4. No closed contract has been silently reopened.
Source indices and notation remain Type 1 under C1-Q1 after that choice.

**Current continuation.** The inventory-first instruction made MP1–MP6 explicit;
the user accepted them and subsequently opened Option B's bounded qualification.
VSL-B1 is delivered at the smallest local receiving/timing interface choice.
The old R1 alternatives below remain useful context; the current expanded
options are B1-R/B1-L at VSL-B1-G1. No exact replacement model is adopted.

[Modeling problem inventory and question ownership](vsl_r1_modeling_problem_inventory.md)

### Candidate A — retain S13 as the conditional elementary verification

Keep the exact time-based conservative transfer, ideal common speed, nonbinding
preparation and proportional batch choke. State every assumption in the paper
methods. Close the observer, compact-state and derivative-check protocol within
that benchmark; external traffic validity remains a separate future layer.

**Pros.** Already complete and accepted as a mathematical reference. It keeps
one action and one sufficient scalar, gives exact directions and an optimum,
and can be a transparent first verification without a new traffic stack.

**Cons.** It provides conditional usefulness within the declared model, not
independently validated traffic usefulness. It does not settle the physical
clock, realistic regime or novelty of the exact verification. This is an
explicit narrowing of the immediate applied ambition.

**Dependencies and consequences.** Preserve S13 and the compact rival; agree
on the conditional role under G1/G4 before describing this as the first completed
task methodology. This choice still opens no implementation or experiment.

### Candidate B — admit a bounded source-coupled preparation/receiving reduction

Assess a bounded source-grounded revision against the full MP1–MP6 inventory:
the physical meaning of transfer, feasible sending/receiving, continuing-group
aggregation, consistent early/late costs, departure chronology and a joint
operating regime. Each issue can close through a justified restriction, a
minimal revision or an explicit unresolved/conditional outcome. The remedy
must follow the identified problems; it is not organized around fitting a
speed-dependent merging rate.

The accepted inventory was reviewed in VSL-B1. Carey is the provisional principal
reduction candidate; Subraveti is a separate lane-drop/density check. A local
receiving/timing amendment is recommended at the new gate, without source fusion
or adoption of any exact law/state. Constant parameters and grouped/batch
assumptions may remain if justified. S13's scalar sufficiency remains specific
to S13; no particular synchronized-flow law has been established.

**Pros.** Addresses the actual missing physical join and preserves the eventual
applied usefulness target. A sourced response can falsify the intended benefit;
its compact state can be assessed fairly instead of withholding a statistic.
A small valid reduction could remain suitable for an elementary methodology.
The joint scope allows lane service to determine completion and avoids charging
preparation and exit costs under incompatible assumptions.

**Cons.** This changes the primary traffic contract. Receiving or adjacent
imbalance may require additional continuous state and destroy the elementary
reduction. A qualified transfer relation may produce no preparation advantage; source
branches are not automatically gradient-admissible. No positive applied result
or closed reduced law has been supplied by this review.
Matching forward merging at one speed would not establish its response to
speed changes. Qualifying the operating regime and joint costs may prevent
retention of the current two-group/batch reduction.

**Dependencies and consequences.** Requires an explicit G3 amendment direction
before deriving/admitting replacement equations, followed by the smallest
necessary G2/G4 consistency checks. Maintain common action, complete time and
strong rivals. If qualification needs a substantial new stack, return to the
elementary role instead of defaulting to Candidate C.

[Full modeling problem inventory for Candidate B](vsl_r1_modeling_problem_inventory.md)

### Candidate C — use a fuller published spatial lane model as the primary core

Adopt one source's spatial occupancy, longitudinal/lateral sending and receiving,
arrivals and departures faithfully, with a separately specified common-VSL
mapping. This can resolve receiving and chronology through explicit dynamics,
while still requiring source branch and conservation checks.

**Pros.** More direct physical/source accountability; the full receiving state
and departure chronology expose effects the batch suppresses. Published
reference cases give a stronger forward-adoption basis.

**Cons.** A fuller state and speed-control integration may exceed the elementary
companion role. Neither source supplies the whole intended observer/gradient
task. Forward adoption does not establish derivative usefulness, and complexity
itself adds no contribution.

**Dependencies and consequences.** Requires explicit G1/G3 system-scope review,
then observation/objective/evidence checks. It is a new model program, not the
next local refinement. No construction is authorized by listing it.

**Provisional recommendation, clarified in follow-up discussion.** For the
current applied-usefulness target, B is the recommended amendment direction.
The user's preference for revision supports this direction. Its target is the
full set of modeling qualifications exposed by VSL-R1. MP1–MP6 were accepted
and the user opened B's qualification, now delivered as VSL-B1. The new
recommendation is B1-L's smallest local receiving/timing amendment; it is
unapproved. No positive preparation benefit or information gap is required.
The prior feedback-led next-task wording remains superseded.

Preserve S13's closed conditional result. Its exact equations can remain an
optional mathematical reference; a revised primary model need not retain the
fixed rate. Candidate A is appropriate only if the immediate goal is explicitly
narrowed to conditional analytical verification. Do not select C by default.
No replacement equation, state or execution plan has been adopted; the current
discussion is VSL-B1-G1, not another inventory-opening request.

[Why revision is recommended, and what a fixed proportion can mean](vsl_r1_fixed_rate_justification_response.md)

[Synchronized living model candidates](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md)

[Work report, source access limits and document checks](vsl_r1_work_report.md)
