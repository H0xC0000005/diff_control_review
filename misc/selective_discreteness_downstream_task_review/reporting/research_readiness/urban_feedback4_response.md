# The four principles are settled; lane assignment and physical entry are different

23 October 2026. Response to feedback 4.

**All four broad principle choices are now settled for this stage. Questions 2 and 4 still need a concrete coupled model, rather than another vote on their overall direction.** Your upstream-queue proposal separates lane assignment from physical entry. I use the existing fixed-commitment rule as the default: once the allocator commits waiting mass to a lane, its target remains fixed until admission. Revisable targets are a distinct deferred alternative, not another mandatory gate.

| Original question | What is now agreed | What remains |
|---|---|---|
| **1. Starting queues** | Load from empty for development and early validation; direct prescribed states are deferred | Specify the preparation and accounting when constructing the cases |
| **2. Lane allocation and access** | Use responsive desired allocation, then enforce actual access and storage; preserve an established lane commitment while waiting | Specify the allocation cost, exact commitment interface and access law |
| **3. Service** | Use effective average service at this stage; no active phase clock | Specify how shared-lane demand/order uses that service without exceeding physical resources |
| **4. Order and mixing** | Respect incoming package order at allocation; retain realized lane order; defer deliberate local mixing | Apply that order consistently to the chosen waiting/admission arrangement |

The unfinished model work belongs especially to questions 2 and 4. Detailed equations, reference checks and derivatives are specifications under the settled principles, rather than reasons to mark every broad decision unresolved. The principles do not determine one unique access law: later alternatives that predict different traffic behavior still return for discussion. This status concerns the current categories 1–2 discussion; the later comparison, sensitivity and scientific-credit work is not declared complete.

## Average service: agreed, with one correction to its justification

I record your choice of average service as accepted for this stage. The existing movement/phase permission map already turns allocated phase fractions into average movement service rates. No new discussion is needed merely to establish that relationship.

A phase-based model does not inherently have zero sensitivity to green split. Extending a green interval can let more waiting traffic leave, even though the signal's instantaneous state stays unchanged at most times. The change acts through the switching time. An implementation that differentiates only a fixed on/off mask can miss that path. Traffic-light research does calculate congestion sensitivities with respect to green/red durations using event-aware methods; this is evidence against a universal zero-gradient claim, not a method we are adopting here. [Geng and Cassandras, 2012](https://arxiv.org/abs/1204.1910).

Average service avoids that extra timing model and fits the already selected urban abstraction. It gives service capacity a direct continuous dependence on the allocation. Realized flow or total time can still be insensitive where another constraint binds. Its advantage is a simpler, appropriate model for this stage, rather than guaranteed nonzero or useful gradients everywhere.

## You are right that the front packet can be split

If an eligible, reachable packet contains three vehicle equivalents and the available admission amount is 0.4, admit 0.4 and retain 2.6 upstream. A packet never has to fit as a whole. This is already consistent with continuous traffic mass and the accepted partial-split semantics.

My earlier example concerned **zero usable admission**, not a large packet failing an all-or-nothing fit test. But zero usable admission can arise for more reasons than the lane having no capacity or no space. A bay can have room while a through queue obstructs its opening. A packet can also be not yet travel-eligible. Splitting a packet addresses its size; it does not create a physical path or make it arrive sooner.

I would not add a small positive cutoff now. Refusing otherwise feasible tiny transfers changes waiting and potentially clearance, even if the mass is retained. The present principle is to allow positive feasible continuous transfers and to retain whatever cannot enter. A numerical assertion tolerance is separate from a traffic rule that stops positive flows; no such cutoff is selected.

## Your upstream-queue proposal separates two operations that should be distinct

Choosing a desired lane need not mean physically entering the lane zone. A package can be processed in incoming order, receive a desired lane, and wait upstream while that lane has no usable receiving space. The allocation process can then consider the next package without claiming that the first one has entered the zone.

This is a useful refinement of the earlier question. It avoids making “cannot enter now” automatically mean “the allocation process cannot finish handling this package.” These are logical operations, not extra simulation time steps or a newly specified physical server. Physical admission remains a separate decision: another package may use its own path only if that path is actually accessible. Labeling two upstream queues does not itself establish independent physical access.

To retain the accepted aggregate upstream model, these lane-specific waiting queues should initially be understood as **records or views of mass still in the upstream link**, not new physical lane buffers. That mass remains in the upstream occupancy and time account exactly once. It consumes zone storage only on actual admission, and its service readiness must follow actual travel/entry history. If instead the queues are intended as new physical upstream lanes, that would require a different geometry and propagation specification.

Your shortcut—append to an already desired lane without solving again—is valid when that lane target has already been chosen under the agreed policy. If no target exists yet, “far upstream” does not determine it. Substituting an arbitrary lane at that point would silently replace responsive choice with a fixed rule. The shortcut can therefore be a reuse of an earlier decision, rather than a competing model in its own right.

## Preserve commitment by default; provisional targets would be a different model

I initially treated fixed versus provisional waiting targets as another required question. The inherited M2 contract already keeps a committed lane fixed. There is no need to reopen that rule just because allocation now supplies the commitment. The default reading of your proposed append is therefore an actual commitment to the waiting lane. The concrete proposal must show where that commitment occurs and how it feeds the existing seam.

For completeness, the two behavioral possibilities remain distinct. Both can process incoming mass in recorded order, allow partial physical entry and retain unadmitted mass upstream. Neither grants passage through a real obstruction.

**Commit when the allocator assigns the waiting lane.** Responsive allocation chooses a lane or continuous lane shares; the resulting waiting pieces keep those targets until physical admission. Later arrivals can respond to updated conditions, but already assigned pieces do not move between waiting queues. This closely matches your proposed separation of allocation and waiting, gives a clear queue order, and can feed M2's single-precommitted-lane ingress. Its limitation is that a waiting piece cannot revise its choice when lane conditions change.

**Keep targets provisional until physical admission—a deferred alternative.** Waiting mass could revise desired shares as conditions change, with actual admission fixing realized lane membership. This represents more pre-entry adaptation but requires new rules for source order, waiting priority and access, without making changes of intent into free physical lane changes. It would explicitly reconsider the inherited precommitment meaning. It is not required for the current direction and has not been selected.

**The default is commitment at allocation**, followed by physical admission when feasible. This reads your staged proposal consistently with the existing no-reassignment contract; it does not approve a particular solver or physical bay-access law. Reusing a desired target is valid only when the chosen policy still treats it as valid. It cannot silently freeze a provisional target or invent a missing one.

I record the separation of logical assignment and physical entry as agreed, with fixed commitment retained as the default rather than attributing a new retargeting decision to you. The older scan-versus-prefix question becomes part of the actual access law under that arrangement, not a universal scheduler vote independent of the road. If the concrete model cannot support the intended cases under this commitment, it must bring back the smallest justified amendment.

The four principles can guide the later model proposal: loading from empty, responsive intended allocation, average service and exact order without deliberate local mixing. None needs another broad principle-level vote. Q2/Q4 especially need their concrete coupled allocation, waiting, access and service laws. The remaining global discussions still precede formal component closure; this does not close every global/detail question or approve implementation. No simulator experiment is opened by this discussion.

[Updated principle proposal and status](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md)

[Supporting evidence and scope notes](../../extraction/research_readiness/urban_feedback4_evidence_notes.md)

[Current decision record](../../temp_content/research_readiness/phase_B_revision.md)

[Work record and checks](urban_feedback4_work_report.md)
