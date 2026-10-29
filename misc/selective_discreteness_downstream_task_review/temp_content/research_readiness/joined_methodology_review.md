# Joined-model questions: feedback 10 status

**Current disposition after the user's closure and authorized consolidation:** this policy question set is closed. The agreements are applied in the [current model](unified_methodology_draft.md). Physical access and logical scanning are explicitly separated; the former interface check is complete at the definition level. Historical questions and feedback statuses below are preserved for traceability, not a request to answer again.

**Historical status immediately after feedback 10, before consolidation:** Q1 is resolved for the starting scenario; Q2's binding/progressive-loading principle is resolved; Q3's no-target and movement-specific processing policy is resolved, with its physical access/interface still open; Q4 is withdrawn; Q5 retains A with a correction about sequential head dependencies. The user requests answers only. No new joint transcription or next task is opened.

[Feedback 10: answers and resolved/open status](../../reporting/research_readiness/urban_feedback10_response.md)

## Historical question text before feedback 10

The candidate explanations below are preserved as the questions the user answered. Their old recommendations and “open” wording are not current decisions. In particular, frozen waiting targets are unselected, Q4 is withdrawn, and the constant average receiving convention is selected.

27 October 2026. Expanded after the user asks to separate the functions mixed in the earlier short paragraphs.

[Methods proposal with the same expanded decision appendix](../../reporting/research_readiness/urban_compact_methods_report.pdf)

The previous note combined lane permissions, commitment timing, waiting targets and partial entry. These choices affect different traffic responses and are separated below.

**These choices remain open within the current joined-model review.** Written equations illustrate a proposed completion. Continuous mass, exact order, progressive queue loads, capability-aware fresh allocation and current-head sharing remain agreed.

Permissions determine which allocation questions are active: a unique legal target removes discretionary lane choice. Question 4 applies only if binding multi-lane waiting targets exist; it is not a general gate for fresh allocation.

## 1. Which lanes may a left turner use?

A bay and an adjacent lane do not automatically give a left turner two alternatives. This matters because the agreed responsive allocator can react to queues only where the permission matrix offers a real choice. An exclusive-lane model can still study storage and ordered access, but it does not exercise adaptive left-turn allocation.

**Candidate A: left turns use only the bay; through/right use only the continuation.** Suppose the bay already holds 0.2 units and the other lane is empty. With enough room and transfer capacity, a new left-turn unit must all go to the bay. The resulting loads are 1.2 and 0. This gives a simple storage/access case. A turner cannot avoid a busy bay by choosing the adjacent lane.

**Candidate B: the bay is left-only, while the adjacent lane also permits left turns alongside through/right.** In the same unconstrained example, the new left unit splits 0.4/0.6, giving loads 0.6/0.6. Choice now responds to queues created by earlier control. The shared lane can also contain left and through heads in different orders, so its stop-line obstruction must use the already selected elapsed-service rule.

**I provisionally favor B if responsive lane allocation is intended to be active in the main bay experiment.** This revises the earlier draft's exclusive-lane illustration as a preferred main realization: that illustration left the selected allocator with no legal choice. A remains a valid simpler control, not a defective traffic model. V2 and V3 must use the same chosen permissions, as must their comparison models; otherwise a change in legal movements could be mistaken for an order effect. No extra control series is required merely by listing A.

## 2. Where should a new lane choice become binding?

Where drivers first commit determines which queue snapshot shapes their choice. Keep the physical common feeder and bay opening inside the local zone under both candidates. The question concerns the decision location, not moving the bay opening or reopening the rejected mouth-aligned geometry.

**Candidate A: commit before entering the common feeder.** A left-turn unit observes bay/other loads 0.2/0 and receives targets 0.4/0.6 when both are legal. It carries those targets while travelling or waiting in the feeder. This describes an earlier lane-choice intention and fits the earlier prototype. Known capability at that entry boundary can constrain present transfer, but current branch room cannot be treated as guaranteed room when the unit later reaches the fork.

**Candidate B: make the new choice at the eligible fork front.** If the observed loads have become 0/0.5 by then, the same new unit instead receives targets 0.75/0.25, assuming ample entry capability. Earlier commitment would retain 0.4/0.6. Thus the locations can predict different lane populations even though both preserve valid commitments and use only current queue information.

**I provisionally favor B for this first joined model**, because the relevant current branch limits and the new allocation refer to the same physical entry attempt. Feedback 9 does not logically force this location: early choice is also possible if current transfer capability and future branch admission are distinguished honestly. If the intended traffic story is that drivers have already chosen their future lane before entering the feeder, A is the appropriate direction and the written model must reflect that. Under unique legal targets, this location alone does not create a lane-choice effect.

## 3. Does the unadmitted remainder receive a binding lane target now?

Known capability determines how much can enter now, but it does not by itself say what a waiting record commits the rest to. With loads 0.2/0, branch entry allowances 0.3/0.5 and common sending 0.6, both candidates first admit 0.2/0.4. They agree with feedback 9 on this present entry. Their difference concerns the 0.4 that remains physically upstream.

**Candidate A: assign the waiting remainder now, then keep that intention fixed.** After selecting entry, balance the remaining 0.4 as waiting targets 0.2/0.2. Later packets see that committed load, and the remainder cannot change destination merely because later queues or capacities differ. This is the exact waiting convention proposed in the specification, not an unconstrained target computed before current entry.

**Candidate B: leave the unadmitted remainder unassigned until a later entry attempt.** Only the mass actually admitted acquires a binding lane choice. If, at the next opportunity, only the second legal lane has room and remains preferable, all remaining 0.4 may enter it. Under A, only its already committed 0.2 can do so. B delays creation of a target; it does not cancel a genuinely valid old target.

**I provisionally retain A to respect the existing default that logical assignment creates fixed waiting commitments.** I am not asking whether already valid targets may be changed. The point to clarify is whether the capacity-aware allocator creates valid targets for the unadmitted remainder at all. Under B, later packets on a common feeder wait for that unassigned prefix to be processed; when processing resumes, they see earlier realized assignments. Choosing B would explicitly amend the logical-waiting-assignment default for new mass. It would not authorize retargeting traffic whose commitment is already valid.

## 4. If old multi-lane targets are binding, how should scarce entry be shared?

**This question is conditional.** It applies to an already committed homogeneous remainder whose targets span multiple lanes. If the selected model leaves all unadmitted mass unassigned, this case does not arise in its ordinary empty-loaded development path and need not block it. The earlier mandatory A/B question for fresh allocation remains withdrawn.

Suppose a genuinely old remainder has targets 0.2/0.2, current lane loads 0/0.2, enough branch room, but common sending permits only 0.2 to enter. Fixed targets determine eventual destination totals; without a further rule they do not say which portions enter first.

**Candidate A: advance the remaining targets proportionally, subject to caps and reuse.** Admit 0.1/0.1, leaving lane loads 0.1/0.3. This treats the target shares as progressing at the same fractional pace when no individual cap intervenes. It adds that interpretation of partial progress to the fixed-total commitment.

**Candidate B: balance current queue loads within the fixed target caps.** Admit 0.2/0, leaving loads 0.2/0.2. The remaining target is then 0/0.2. No destination total is changed: the second share waits longer, while more of the first share enters now. This treats old targets as fixed total quotas rather than a requirement of proportional progress.

**I provisionally favor B if this case is retained**, using the same queue-based criterion within the old caps. Neither candidate retargets the block or creates a lane-target sequence inside it. This is a choice about realizing a valid old commitment under a new limit, not a return to fixing fresh targets without known capability.

## 5. Does downstream receiving act as an average rate or a consumable timestep allowance?

The inherited propagation model supplies an amount that the downstream section may receive during the update. The elapsed head solver also needs to know how that amount limits its internal service calculation. Two conservative interpretations can leave different lane queues at the next boundary. This is why the choice belongs to the present timestep model.

Consider a one-unit timestep and an exit that can receive 0.6 units, although its physical rate capacity is 1. Lane A has a ready head for that exit throughout. Lane B first serves an existing 0.5-unit head to another exit at rate 1; its next, already resident head then joins A halfway through the step. Both lanes have head-rate cap 1 and equal green weights when competing for the common exit. Sending and the other exit are nonbinding.

**Candidate A: spread the receiving allowance as a constant average rate.** The exit offers rate 0.6 for the whole step. A alone receives 0.3 during the first half; each lane receives another 0.15 during the second. Final common-exit discharges are 0.45/0.15. This is the receiving convention in the current equations. It puts receiving on the same step-average-rate basis as effective service, but stretches the allowance across the interval.

**Candidate B: serve at the physical receiving rate until the timestep allowance is spent.** A receives 0.5 in the first half. The remaining 0.1 is then shared by the two current heads, giving final discharges 0.55/0.05. The solver respects physical rate 1 and total receiving 0.6; it treats that allowed amount as available to current service rather than reserving a uniform fraction for later in the step.

**I provisionally retain A for the current average-rate model**, while making its effect on the advantage of an earlier head explicit. B is the better match if the intended meaning is a pool of currently usable downstream room. Neither is deduced from the endpoint allowance alone. Both retain current-ready-head sharing, effective signal rates and the existing boundary-history interpolation; neither equalizes final lane totals or introduces actual signal phases. The different final discharges make this a boundary-state choice, not a request for an intermediate-time gradient or the deferred event-history upgrade.

## What can remain later

The homogeneous-mixture ablation is optional. Its current formula covers exclusive targets; shared permissions require a matching comparison definition. It cannot replace stronger native rivals.

Numerical calibration, native-rival qualification, horizon values and reference-program settings remain later work. Bookkeeping and clearance conventions need new discussion only if they conflict with the chosen traffic behavior.

**Current topic: joined-model clarification. The materials are ready; the choices remain open.**

[Detailed candidate equations](../../reporting/research_readiness/urban_methodology_specification.pdf)

[Sources and scope](../../extraction/research_readiness/urban_methodology_specification_sources.md)
