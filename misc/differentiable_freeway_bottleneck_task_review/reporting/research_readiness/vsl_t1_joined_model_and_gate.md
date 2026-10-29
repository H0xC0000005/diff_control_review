# A complete elementary model: homogeneous preparation, then a finite terminal queue

**Subsequent user closure, 2026-10-14.** The user accepted this assembled
conditional H1/T1 contract, explicitly closed Step 2 and opened Step 3.
The exact mathematical source/PDF below remain unchanged; their approval
and artifact identity are fixed by the linked closure record. The findings
and confirmation wording below retain their delivery-time status.

[Approved Step 2 closure](vsl_step2_model_closure.md)

[Executed Step 3 opening and current evidence choice](vsl_step3_findings_and_gate.md)

T1 completes the missing physical connection. Traffic first travels through
a homogeneous preparation window, where ending-lane requests compete with
adjacent-lane traffic for receiving service. It then enters a finite final
section. Traffic still on the ending lane must obtain service at the permanent
lane end; if service is insufficient, it waits on that section and eventually
exits. The model accounts for both the travel paid by everyone and the delay
paid by unfinished merging.

**The original modeling-chain review is now finished at its contract
confirmation gate.** One complete conditional forward model can be specified
without resolving positions inside H1. The checks below establish that its
preparation, terminal storage, forced service and complete-time objective can
describe the same cohort over the same advice range. They do not establish
useful gradients, an interior optimum or a calibrated freeway model.

Date: 2026-10-14. Review: **VSL-B2, original roadmap Pass 2**.
The user selected **T1**, including its reviewed finite physical section,
preparation handoff and restricted own-lane-first terminal member. T2 is
unselected. This report consolidates the exact H1/T1 contract for confirmation;
it does not start the next review stage.

[Combined equations, assumption register and analytical checks](../../synthesis/research_readiness/vsl_h1_t1_joined_contract.pdf)

## The model's central idea

The important quantity is not a fixed proportion that succeeds in merging.
It is **the service left after the adjacent lane serves its own traffic**.
Ending-lane traffic requests early transfer, but only the part that fits that
remaining service completes it. A completed transfer removes mass from the
ending lane and adds exactly that mass to the adjacent lane. The adjacent
lane consequently has a larger own-flow claim at the next opportunity, so
less service may remain for further merging.

This is an autonomous feedback loop inside the traffic model. We know the
initial lane densities, predict accepted transfers, update those densities
and recompute the next spare service. We do not prescribe a future receiving
trajectory obtained from another simulation. On H1's admitted free-flow
branch, the raw receiving ceiling stays at lane capacity; the state dependence
appears in how much of that capacity is already claimed. This is a particular
elementary mechanism, not a description of synchronized-flow gap acceptance.

Common advice affects physical progress and ordinary flow. Its effect on
early preparation is measured per unit distance, using a fixed physical
opportunity scale. Extra elapsed time does not automatically create extra
successful merges. In the declared speed-dependent triangular diagram,
changing advice can also change density headroom and therefore how much
merging succeeds before the handoff.

The terminal then makes that predicted preparation consequential. Traffic
that merged early arrives in the ordinary adjacent stream. Traffic that
did not merge arrives in the forced-merge stream and needs more receiving
work per unit mass. That extra work can produce waiting. Whether a slower
advice saves enough of this waiting to repay its longer travel remains a
question about the complete objective.

## What T1 adds, and what it preserves

Imagine an early-preparation section followed by a short final approach to
the lane end. Early transfers operate in the first section. In this
elementary member, further lateral transfers stop at the handoff; remaining
ending-lane traffic travels through the final approach and merges only at
its downstream point. The two sections divide the same fixed road length.
No road length or travel time is added to obtain the queue.

The final approach retains lane-boundary entry and exit histories. Those
histories distinguish traffic still traveling from traffic whose minimum
travel time has elapsed but which has not exited. Both occupy physical
stock; only the second contributes excess terminal delay. Counting just
the waiting counter against storage would miss the traveling stock.

Finite storage and backward-wave travel determine whether terminal entry
can keep accepting H1's approaching traffic. For this first member, the
declared domain keeps that receiving constraint nonbinding throughout the
advice range. A conservative sufficient condition is that the entire
cohort fits within one terminal lane's jam storage, with capacity-compatible
entry flows. It is stronger than necessary but permits a direct proof.
There can still be a real downstream queue: storage can accommodate the
traffic even when the merge point cannot serve it immediately.

Boundary histories give physical propagation and storage without keeping
independent states at successive interior positions. That is the established
link-transmission approach. T1 can have implicit nonuniform queued motion in
the terminal section; H1's upstream occupied body stays homogeneous under
the proved nonbinding handoff. Homogeneity is not asserted for the whole road.

[Jin: empty-link demand, vacancy and boundary histories, §3](https://arxiv.org/pdf/1405.7080)

At the merge point, feasible adjacent continuing flow is served first.
Ending traffic uses the residual receiving work, subject to its own sending.
The nominal domain guarantees that continuing flow can pass immediately,
so only the ending stream needs a waiting queue. Failed requests remain
in its stock. After the finite arrival pulse ends, positive residual
service clears every remaining unit.

Own-lane-first allocation and weighted receiving have a literature basis.
Their extension to this compulsory point, the constant late-work factor and
the absence of lateral transfers inside the terminal section are declared
task adaptations. Choosing a finite physical section follows familiar
simulation practice; it does not make these additional restrictions empirical
facts about every lane drop.

[Carey, Balijepalli and Watling: R1 and the proportional alternative, §5](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

## What the joined check establishes

The consolidation checks more than whether each component works separately.
It gives an algebraic example in which **early receiving limits
merging**, **unfinished traffic queues at the lane end**, and
**terminal entry remains unrestricted**, all for the same fixed geometry,
initial cohort and bounded advice range.

At its faster action, the adjacent lane's own claim and the work consumed
by early transfers exhaust the local receiving budget. At its slower action,
the initial request fits. Some ending mass still reaches the compulsory
node. There its weighted work requirement exceeds the available receiving,
so a positive queue forms. Nevertheless, the finite section has enough
physical storage to keep accepting the prescribed upstream flow.

This example is a compatibility proof, not a selected scenario, calibration,
traffic rollout or positive control certificate. It strengthens the earlier
sparse existence argument by including an active upstream service limit.
The mathematical note supplies exact branch arithmetic and all domain
inequalities. No parameters were selected to obtain an interior optimum.

| Question | Direct answer for the consolidated H1/T1 member |
|---|---|
| **MP1: what determines opportunity and speed response?** | Preparation depends on progress, available ending traffic and spare receiving. Common advice changes the clock and the declared normalized headroom. Longer elapsed time alone does not guarantee more completion. |
| **MP2: what makes merging feasible?** | Early transfers must fit donor availability and residual adjacent receiving. Forced transfers must fit eligible ending demand and residual terminal service. Failed requests stay present in both parts. |
| **MP3: what lane information is required?** | The adjacent lane is distinguished from the other continuing lane. With initial continuing symmetry, known footprint and empty terminal state, total mass plus one initial ending-mass statistic reconstructs the whole model. Full lane observations or discrete order are unnecessary in this member. |
| **MP4: are early and late costs compatible and counted?** | Early transfers use an explicit local receiving budget while upstream motion remains free flow. Late transfers use an explicit larger-than-ordinary work class and can queue. Full travel through both sections and all terminal delay enter TST; no separate early waiting is assumed in the admitted branch. |
| **MP5: what determines complete time?** | Physical entry histories, minimum travel time and the specified arrival-aware priority determine departures. Every unit clears. Complete TST follows those departures, not a simultaneous-batch mean or final work alone. |
| **MP6: can the parts hold together?** | **Yes as a restricted analytical task:** a nonempty joint domain supports active early receiving, positive forced waiting, finite physical storage, a homogeneous upstream window and finite clearance over one advice range. **Applied admission remains unestablished:** the sources do not jointly calibrate this footprint, opportunity scale, response, priority and work factors. |

No new shared methodological choice was required to make T1 internally
complete. The consolidation makes one conservative domain refinement:
the fixed receiving-work ceilings also fit the surviving-lane capacity
at the slowest allowed advice. This keeps the exit physically compatible
throughout the declared speed range and narrows the earlier candidate;
it adds neither traffic state nor another service mechanism.

## The smallest old-to-new stack change

The first intended change remains P1's replacement of fixed early completion.
The additional terminal change is necessary because the accepted finite
footprint produces staggered arrivals and a physically located queue.

| Existing responsibility | S13 reference | Consolidated H1/T1 member |
|---|---|---|
| **Geometry/cohort and propagation, components 1 and 3** | Simultaneous entrance cohort; one common traversal time. | A known finite uniform initial footprint; physical passage times. The fixed road is divided into preparation and terminal sections. |
| **Common action and response, component 2** | One bounded common advice, realized as the preparation travel speed. | The same common advice sets the admitted preparation speed and terminal free-flow parameter. Queued terminal traffic may move more slowly. |
| **Early transfer and receiving, components 4–5** | Fixed per-time completion with nonbinding early receiving. | Eager opportunity-scaled requests constrained by the adjacent lane's own claim and receiving. Accepted transfers update that lane's subsequent claim. |
| **Forced service, component 6** | Extra work and proportional clearance of a simultaneous batch. | Finite physical terminal storage and an arrival-aware own-lane-first server; unfinished ending mass waits and clears. |
| **Objective, component 7** | Complete mean time under the conditional batch law. | The same complete-population objective, evaluated from the new departures. Travel plus eligible-queue area is an equivalent accounting identity on the admitted branch. |
| **Information and evidence, components 8–9** | Ending statistic sufficient; accepted conditional certificate. | The ending statistic remains sufficient under stated initial symmetry. New gradient correctness, information-dependent action and independent-usefulness claims await the next stage. |

S13 remains an unchanged, complete conditional analytical reference. This
successor changes its physical/task assumptions; it is not an exact reduction
of S13, Carey CTM or a generic lane-drop simulator.

## The short methodology that can now be written

Define a finite, initially uniform cohort on three upstream lanes approaching
a permanent three-to-two drop. The two continuing lanes start symmetrically,
but only the adjacent one receives ending-lane transfers. The fixed geometry
includes a preparation window and an initially empty finite terminal section.
One bounded constant common advice is the intervention; it sets the preparation
free-flow speed and the terminal free-flow parameter, while queued traffic may
move more slowly.

Model early merging as conservative continuous-mass transfer. Available ending
traffic requests transfer over a fixed physical opportunity scale. Adjacent
ordinary flow claims receiving first. The remaining budget determines realized
merging, which updates ending and adjacent densities. The chosen free-flow
domain preserves the uniform upstream occupied body.

Transport the resulting lane streams through the terminal section using their
boundary histories and finite travel/storage limits. Stop further early
transfers at its entrance. At the permanent lane end, serve ordinary adjacent
arrivals first and complete forced merging from residual work. Retain unserved
ending mass, enforce sending and receiving, and follow the cohort through full
clearance. State the no-spillback domain before evaluating actions.

Measure complete TST from the unexited population, including both sections'
travel and all excess terminal delay. Give the aggregate-plus-ending-statistic
rival the identical geometry, initial profile, parameters and predicted-history
capability. Treat the effect of advice on the optimum, derivative correctness
and independently evaluated control usefulness as separate subsequent claims.

## What this does and does not finish

**Finished:** the original VSL-B2/Pass 2 evidence review now delivers a complete
joined conditional forward contract. It no longer stops at an unspecified
receiver, an unexplained travel clock or a choice between physical and virtual
waiting. The selected T1 interpretation and the exact proposed equations are
assembled in one document.

**Still a confirmation gate:** the user has selected T1. The assembled exact
H1/T1 equations, domain and analytical claim boundary are presented for final
contract confirmation before being frozen as the successor model. This is
the original VSL-B2-G1 gate's final disposition, not another independent
design sprint or a request to reconsider T1.

**Recommendation:** confirm the assembled H1/T1 member as the successor's
conditional analytical traffic contract and close Pass 2's contract gate.
Its source/adaptation limits stay part of that contract; applied validity
and useful control remain separate claims.

**Still unproved:** changing preparation may or may not outweigh slower
travel. With preparation held fixed, the earlier-arrival dominance result
remains applicable to this work-conserving member, even with a queue.
An interior optimum or a hidden-state action split is therefore not promised.
Neither the source join nor an eventual internal optimum would establish
empirical validity or useful gradients.

The strongest immediate information rival is **aggregate mass plus the ending
statistic**: it can predict the identical dynamics here. Aggregate models with
history or capacity-drop mechanisms also retain their full capabilities.
Analytical sensitivity, finite differences and direct one-dimensional search
remain serious control rivals. A cooperative/proportional forced-merge rule is
a genuine model-form alternative, with different priority and potentially
continuing-lane waiting; T1 selection does not qualify that alternative or
silently insert it into the selected one-queue member.

**Next allowed action after contract confirmation:** open the original Pass 3
comparison/evidence review against this specific model. Its central question
is whether retained information changes a useful speed decision, with matched
observations and separate derivative and independent-evaluation evidence.
Pass 3 has not started. Simulator code, dependencies, traffic experiments and
the closed ramp line remain outside this task.

[Original-stage progress and confirmation status](vsl_review_progress.md)

[Viewed-paper list and source/adaptation limits](../../extraction/research_readiness/vsl_k2_terminal_source_and_interface_audit.md#t1-selection-and-joined-qualification--2026-10-14)

[Work report, files and verification](vsl_t1_work_report.md)
