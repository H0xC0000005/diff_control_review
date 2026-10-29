# One proposed improvement: make preparation merging use actual receiving

Date: 2026-10-13. Status: **P1 approved as the bounded Option B qualification
direction; proposal discussion closed and the next review ready to open.**
The user approves the P1 contract and confirms its main emphasis: jointly
establish how adjacent through-lane traffic determines available receiving,
and how that availability constrains completed ending-lane merging. Exact
state, motion, timing and applied-domain laws remain to be qualified. This
approval record does not execute that review or authorize implementation.

[Approval, accepted clarification and review readiness](vsl_p1_approval_and_review_readiness.md)

## Recommendation and traffic meaning

I recommend **one component substitution now**: replace S13's guaranteed
per-second completion rule with a preparation-transfer rule that lets ending-lane
traffic request a merge when physically available and completes it only using
the actual adjacent lane's receiving opportunity. For the first candidate,
give that lane's continuing traffic priority and let merging use the remaining
opportunity. This is a concrete candidate within Option B.

Imagine an ending lane with traffic ready to move over. The old rule says that
a prescribed fraction finishes merging as time passes. The proposed rule asks
whether the target can take it after accommodating its own traffic. If there
is spare receiving, merging can occur; if there is none, the request remains
unfulfilled. A slower advice action helps only if its effect on traffic progress
and service actually creates a better opportunity. Extra elapsed time alone
does not guarantee a completed fraction.

The proposed substitution targets **component 4, mandatory preparation
transfer**. It also changes component 5's associated assumption: preparation
receiving is no longer declared sufficient in advance. It is checked by the
same completion rule. This is one proposed transfer component with an explicit
assumption change, not two independently designed traffic subsystems.

I would leave the other component replacements to the next review. A particular
lane-state enlargement or exit-service replacement is not yet justified by
the evidence: its necessity depends on what this transfer rule needs from the
surrounding traffic model. Their open questions remain in the proposal below.

## The old/new change

| Aspect | Old S13 contract | Proposed P1 contract |
|---|---|---|
| **Merge request** | The remaining ending mass loses a fixed fraction per elapsed second; completed transfer is prescribed directly. | Ending traffic requests transfer at the first physically available local opportunity. Desire is simple; completion is determined separately. |
| **Available traffic** | Remaining ending mass and the preparation clock determine the transfer amount. | Only traffic actually available at that opportunity can transfer. Its availability must come from the declared motion model, not an added speed multiplier. |
| **Receiving and competition** | Preparation receiving is assumed nonbinding; no early allocation is resolved. | Continuing traffic receives its own feasible longitudinal service first. Merging uses the receiver's remaining opportunity, subject to its gap-work allowance and available donor traffic. |
| **Unfulfilled merging** | The prescribed exponential decay determines what remains. | Unserved requests remain represented in the ending lane. They may advance there when longitudinal service permits, but are not counted as completed merges. |
| **Mass versus receiving work** | Equal transferred mass leaves the ending group and enters the continuing group; late merges use extra receiving work. | Preserve the same paired mass accounting. The early gap allowance also consumes receiving work, not extra vehicle mass. Its numerical relation to the late-work parameter remains to qualify. |
| **Advice response** | Lower realized speed lengthens preparation and automatically increases completion under the fixed time law. | Advice affects physical progress, availability and receiving through the eventual common traffic contract. The amount completing may increase, decrease or remain unchanged. No sign is imposed. |
| **Output to exit service** | End-of-preparation remaining mass at one common traversal time feeds the proportional exit batch. | Remaining mandatory mass retains its meaning. Keeping the scalar/timing handoff requires the next review's conditions; no replacement arrival or exit law is chosen here. |

This is more than putting a receiving cap on the old exponential: the
unjustified physical-time completion clock is removed from the candidate.
It is also less than adopting a full spatial lane model. The proposal identifies
one local completion rule; how compactly its inputs can be supplied is a
remaining global modeling question.

[Original nine components and their responsibilities](vsl_feedback3_existing_framework_component_audit.md)

## What the substituted component would do

**Problem statement.** How can preparation predict feasible completed merging
without assuming that a fixed fraction finishes every physical second?

**Model-chain function.** The preparation component changes how much traffic
still needs a mandatory merge before exit service. It must preserve continuous
mass and distinguish a request from an accepted transfer. It does not choose
the common speed or replace the complete-time objective.

**Core gap.** S13's current completion rule has no input for the actual adjacent
receiver or its own competing traffic. Adding those inputs introduces a real
scientific interface obligation; they cannot be obtained from combined
continuing mass by assertion.

The component's proposed inputs are the ending traffic physically available
to transfer, the adjacent lane's own traffic demand/service, its local receiving
budget, and a declared gap-work allowance. All refer to the same physical
transfer opportunity and accounting interval. “Receiving” here means how much
traffic the target can accommodate given its capacity and occupied space.
It is not simply the total mass in both continuing lanes.

The proposed output is the accepted lateral mass and the remaining unmerged
mass, together with the receiving work consumed. Each accepted unit leaves the
ending lane and enters its permitted adjacent target once. Requests are not
subtracted merely because they were made. Longitudinal and lateral transfers
must share consistent donor and receiver budgets; the complete source/reduction
update must be checked before freezing equations.

The request policy is deliberately elementary: all locally available traffic
that needs to leave the ending lane tries at its first opportunity. Its
opportunities must be tied to the declared traffic motion on fixed road
geometry. Repeating an attempt once per arbitrary time tick, or resizing the
road discretization with advice, would not establish the intended speed
response. The fixed-geometry motion interpretation is left for the next review.

## Why this allocation is the first candidate

Carey, Balijepalli and Watling offer an eager mandatory-request case and several
receiving priorities. Their R1 serves the receiving lane's own traffic before
using spare receiving for lateral entrants, with a gap allowance. Their R2
shares scarce receiving in proportion to effective demands. The native
algorithms also move unmerged traffic within its existing lane when service
allows. These are local source ingredients; neither rule supplies a complete
common-VSL permanent three-to-two task.

[Carey et al., primary manuscript, §§4–5 and Algorithms A1/A2](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

### Recommended first version: own-lane priority, following R1

Use the continuing lane's feasible own service first, then accommodate as much
requested merging as its unused receiving permits. This makes “early merging
uses spare receiving” an explicit local allocation rather than an unconditional
assumption. Requests can fail even while continuing traffic advances.

**Pros.** It offers a small, transparent first substitution and directly exposes
when receiving prevents completion. It can preserve the original continuing
traffic's immediate service when its own demand is feasible. That gives the
best initial chance of retaining the existing travel/handoff reduction under
qualified conditions. It needs no stochastic vehicles, individual gaps or
new fitted urgency curve.

**Cons.** Priority is a behavioral assumption, not a finding that all freeway
merges behave this way. It can postpone merging until the lane end. Transferred
traffic can crowd the target later, so immediate priority does not guarantee
zero future delay or an unchanged common traversal time. The ideal-response
and batch conditions still need qualification.

**Dependencies and consequences.** Actual receiving and available traffic must
come from autonomous predicted state. A separate early/late priority choice
must be justified in the joint domain. Eventual lane-end service must hold and
clear unmerged traffic with all its waiting counted. A failure of those
conditions returns to the smallest affected state, timing or boundary contract;
it does not authorize an automatic larger model.

### Viable alternative within the same component: proportional sharing, following R2

Let continuing and merging demand share scarce receiving according to their
effective work demands. This is a distinct allocation of the same resource,
not a second proposed stack modification.

**Pros.** It allows both traffic classes to receive service when neither can
finish immediately. It directly represents the competition that can delay
continuing traffic while helping merges, and is closer to S13's existing
proportional exit interpretation. It is a serious alternative if absolute
continuing priority is inappropriate for the admitted traffic regime.

**Cons.** When receiving binds, it can immediately reduce continuing flow.
The common-traversal reduction then cannot be kept merely by changing a merge
fraction. Consequential waiting and motion would need consistent treatment,
potentially requiring another component amendment.

**Dependencies and consequences.** It needs the same receiver/availability
contract as R1, plus an adequate account of the resulting early delays. It
cannot inherit the exit's half-clearance mean for preparation traffic. This
version remains available in the living candidate record, without approval
or a parallel review being opened.

**Approved review order: qualify R1 first.** The reason is its smaller
immediate coupling burden. This choice is not based on obtaining a positive
speed benefit. If the regime evidence instead supports proportional sharing,
that would justify reconsidering the candidate and its smallest timing
consequence. Neither allocation is adopted by this proposal.

## A small example of what actually changes

This is a single-opportunity arithmetic illustration, not a traffic run or a
calibrated parameter choice. Six continuous units in the ending lane are
available and request merging. Four ordinary units request their own advance
into the adjacent lane. Each accepted merge consumes two units of receiving
work. All quantities below refer to that same opportunity.

| Adjacent receiving budget | Own traffic served under the proposed priority | Merging completed | Ending traffic still unmerged |
|---|---|---|---|
| Ten units of work | Four units | Three units | Three units |
| Four units of work | Four units | Zero | Six units |

Ending traffic and elapsed time can be the same in these two cases. The
receiver's condition changes the proposed completion prediction; the old
completion law cannot distinguish them through receiving. The transfer remains
conservative, and its extra work is charged where it occurs.

For the first row, proportional sharing would instead serve 2.5 ordinary units
and 3.75 merging units. It completes more merging immediately, but delays some
continuing traffic. This is why allocation matters to time and why the two
versions have different consequences for retaining the old neighboring
components. None of these local numbers establishes which common VSL action
improves the complete cohort outcome.

## The exact extent of the proposed change

The primary change is to component 4's completion law. Component 5's blanket
receiving-slack assumption is replaced by that law's finite acceptance check.
There is no additional standalone receiving subsystem proposed here.

However, **one substituted component does not mean an unchanged interface**.
The new local receiver input is an actual added requirement. The current
two-group state is not known to supply it. We therefore cannot claim that this
is already an executable substitution into S13 with every neighboring formula
unchanged. Its feasibility is strong as a local flow component, conditional as
a closed elementary common-VSL task.

The preference is to preserve the existing neighboring components wherever
their conditions survive. Their required amendments, if any, should be shown
as separate old/new changes after the next review establishes necessity. In
particular, neither three lane-total states nor a full spatial profile is
selected now. A compact receiving statistic remains a serious possibility,
and any lawful compact rival must receive the same admitted information.

## What the next review must resolve

| Existing question | What this proposal contributes | What remains unresolved |
|---|---|---|
| **MP1: opportunity and its clock** | A concrete request policy replaces guaranteed time-based completion. | How common advice changes physically available traffic and transfer opportunities on fixed geometry. More time may confer no preparation benefit. |
| **MP2: feasible completion** | A specific candidate makes completion depend on available traffic, own-lane service and unused receiving. | Exact source/reduction budgets, updates and consistent interval units before equation freeze. |
| **MP3: continuing-lane grouping** | Identifies the adjacent receiver as the relevant service input. | Whether the existing grouping can supply it, or which smallest observable/inferable state addition is necessary. |
| **MP4: early/late costs** | Early merges consume an explicit local receiving budget. | Later crowding, any upstream waiting, early/late gap and priority compatibility, and the net complete-time balance. |
| **MP5: departures and average time** | Avoids proposing an exit replacement before its necessity is known. | Whether common travel and synchronized proportional exit remain valid; any consequential chronology must be counted if they do not. |
| **MP6: joint applied regime** | Gives one concrete component candidate to qualify jointly with its neighbors. | A single finite-population, speed/receiving/grouping/boundary regime over the same action range. The applied task remains unqualified. |

Initial observation and scalar sufficiency, native equal-history matching,
derivative correctness and independent usefulness remain their existing
contracts. S13's positive certificate and one-scalar sufficiency are preserved
for S13, not transferred to P1. If eager feasible merging finishes at the first
opportunity for every advice, the extra-time preparation benefit can disappear;
that is an admissible result. Analytical references, finite-difference
sensitivities and direct search remain strong rivals for the one scalar action.

The proposal is **Type 2**, under G3/VQ3-T with VQ3-P/S dependencies. The user
has approved P1's direction, associated receiving-assumption change and R1-first
qualification order. Receiver information consequences belong to G2; timing
and evidence consequences belong to G4. Exact global state, response and timing
contracts remain open; source indices and notation become Type 1 only after
those contracts close. Approval of this review contract does not certify a
complete applied allocation or its interfaces.

## Where this proposal stops

One modification is approved as the next qualification direction, with the
smallest viable source allocation and its genuine alternative explained. The
Option B/P1 direction and proposal discussion are closed. The next allowed
action is the bounded methodological review of the remaining state, motion,
receiving, cost and boundary questions. It is ready to open without another
broad planning round; this approval exchange does not execute it.

At VSL-B1-G1, P1 is the accepted continuation. This does not grant every broader
receiving/timing amendment described in B1-L. Stop the next review at its
completed gate or a further methodological choice affecting the stack. The
common bounded action, complete-time purpose, elementary companion role and
S13/urban/ramp closures remain intact. No simulator, dependency installation
or traffic experiment is opened.

[Existing MP1–MP6 definitions and ownership](vsl_r1_modeling_problem_inventory.md)

[Earlier source/interface evidence and reference list](../../extraction/research_readiness/vsl_b1_source_and_interface_audit.md)

[Work record, source recheck and document validation](vsl_p1_work_report.md)
