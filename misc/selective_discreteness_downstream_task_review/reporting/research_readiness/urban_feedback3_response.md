# Responsive lane allocation should complement physical access and lane order

22 October 2026. Response to feedback 3 on the first principle proposal.

Historical response. [Feedback 4](urban_feedback4_response.md) subsequently selects average service and separates upstream logical lane assignment from physical zone entry. The old phase-clock question below is settled. All four broad principles now guide the concrete model work, with fixed commitment retained by default and provisional retargeting deferred.

I now recommend responsive lane allocation as the main direction. It lets the modeled traffic react to meaningful lane alternatives instead of relying on one externally fixed split. That is a traffic-behavior reason to choose it. Three stronger claims in the feedback need correction before they are used to close the model: fixed lane assignment does not imply threshold-only gradients; redistribution is not inherently packet defragmentation; and deterministic lane assignment does not generally erase order within the resulting lanes.

## 1. Loading from empty is sufficient for the present development scope

Candidate B is recorded as accepted for development and early validation. Use a common preparation to form the required queues, keeping that preparation fixed while the candidate allocation varies. Account explicitly for the traffic and time belonging to preparation.

Directly prescribed nonempty states remain deferred. If later experiment evidence shows an important queue family is not adequately represented, its extension can be proposed then. This decision does not claim that every future V4 case has already been shown reachable by the selected preparation, and it does not require a general initializer now.

## 2. Why responsive allocation is the stronger main direction

Your first argument is persuasive as a modeling philosophy: where drivers have legal lane alternatives, preferences can respond to congestion and expected service. Consider two lanes available to through traffic, one also carrying left turns. If left-turn traffic accumulates there, approaching through traffic may prefer the other lane. That changes which traffic later obstructs the bay. A shorter queue is not necessarily preferable when its service is slower; a perceived cost must be specified rather than assuming equal occupancy. A model intended to represent such situations should have a way to express that response.

Your credibility concern also supports using responsive allocation for the broader study. A result that depends on an arbitrary fixed split would need a narrow interpretation. Fixed-allocation scenarios remain legitimate controlled tests, however: they can isolate access or order without another behavioral mechanism. They are not inherently invalid or unrealistic. Responsive behavior also needs defensible assumptions and validation; adding an equilibrium does not automatically make a scenario representative.

The gradient argument needs a different justification. Even in one permanently assigned lane, more service can drain a queue faster and lower everybody's time. The lane assignment, geometry and binding type of constraint can all stay the same. In a bay case, extra through service can also move the time at which an obstruction clears. Fixed geometry therefore does not make the dynamics fixed, and continuous sensitivity is not confined to threshold points.

Responsive allocation can add a useful physical path: service changes lane conditions, those conditions change intended shares, and feasible admissions change subsequent queues. But it need not make that path smooth. A deterministic rule that always selects the currently best lane can jump when the preferred lane changes. An equilibrium can have changing active constraints or require a solution-selection rule. We should choose the traffic behavior we need, then establish its conditional sensitivity, rather than add redistribution solely to obtain more gradients.

You remember the earlier research direction correctly. The [project context](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L178) discusses perceived resistance and desired allocation, followed by physical access and storage limits. It also explicitly leaves the exact equilibrium rule open. The [review's source anchor](../../extraction/research_readiness/urban_feedback3_evidence_notes.md) supplies useful equilibrium ideas but does not select our waiting-zone entry law. Equal preference should be interpreted for the movement's usable alternatives under the chosen model, not as equal occupancy of all lanes.

There is one interface issue to resolve openly. The accepted M2 scaffold uses precommitted lanes and explicitly does not rebalance load. A responsive choice near zone entry is therefore a new behavior to place relative to commitment, not something M2 already implements. A reasonable direction is to determine intended shares before actual admission, then preserve realized lane membership and order. If that requires moving the existing commitment point, the affected contract must be explicitly reconsidered. I am not proposing continuous reassignment of traffic already inside the zone.

The defragmentation argument is different. Separating movements can make some lane streams simpler, so your intuition can hold in particular cases. Splitting one route-mass block between two lanes can also increase the number of fragments. Adjacent identical fragments can sometimes be merged losslessly afterwards, but that is a separate bookkeeping operation. Lane allocation should be justified by traffic behavior; its memory/computation effect remains something to measure.

**Updated recommendation:** develop Candidate B, responsive intended allocation followed by explicit physical access and finite-storage admission. Keep Candidate A for controlled diagnostics. The perceived resistance, information used, commitment point and actual allocation/access law remain to be chosen. This is a direction, not an already specified equilibrium model.

## 3. A rate can depend on phase allocation without an active-phase clock

I agree with retaining rate-based service. The established formulation already says how phase-group allocation contributes to a movement's average service rate: permitted groups contribute their allocated fractions, scaled by the movement's saturation rate. More allocation to a group raises the available rate for its permitted movements.

That differs from switching service on and off according to the actual phase at a particular instant. The latter needs a phase clock and within-cycle pattern, which the accepted urban abstraction omits. The clarification is about which meaning you intend, not whether rate-based service is sensible.

We also need to distinguish physical lane capacity, allocated movement-service opportunity and realized discharge. A shared lane cannot independently supply its full physical capacity to every movement. Demand, order, access and receiving limits determine how much of the available service is actually used. The remaining coupled service rule must explain that use, rather than multiply independent capacities into a final answer.

My recommendation is the established average-rate interpretation. Its basic phase-permission mapping does not need to be re-debated. The shared-lane service law still needs specification. A real active-phase clock remains a separate, unselected alternative unless that is the intended correction.

## 4. Keep exact order where it matters; do not equate lane occupation with order

Omitting local mixing from the current development path is reasonable. It is optional complexity with no demonstrated benefit here. We can defer it without establishing that it is impossible to implement or intrinsically creates bad gradients. Some mixing maps are continuous; they can flatten a meaningful sensitivity by erasing order. Exact ordered models also have changes in the active front. The validity of a gradient path matters more than simply having fewer paths.

The important correction concerns what allocation preserves. Imagine a single realized shared lane with four through units and one left-turn unit, with no bypass at that point. The left-turn exit is blocked while through discharge is possible. If through traffic is at the front, it can leave; if the left-turn unit is at the front, it obstructs that discharge. Both cases have the same lane occupancy and movement composition. Deterministic lane assignment does not make them the same traffic state.

Allocation can replace one incoming link-wide ordering with separate realized lane sequences. It does not generally replace those sequences with occupancy totals. Exact order need not impose one global FIFO across independent lanes, but the order in each shared lane can remain decisive. That distinction is already explicit in [the project context](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md#L162).

**Updated recommendation:** retain exact incoming order, construct realized per-lane ordered streams conservatively, and preserve their order under the selected access/service rule. Defer deliberate local mixing. Keep exact adjacent lossless merging where its existing conditions hold. This is consistent with continuous traffic mass and does not require individual vehicle dynamics.

Your subsequent clarification makes the intended separation clearer: incoming package order determines the allocation process's service order; actual lane occupation is produced by allocation dynamics and downstream traffic. I accept that distinction. It does not require one permanent global discharge order across the realized lanes.

My recommended reading of actual lane occupation is the traffic actually admitted to each lane, with its resulting sequence and readiness. Its order is generated by admissions, rather than copied as one global link-wide discharge order. Nothing in your clarification explicitly selects an occupancy-only replacement, so I retain the existing ordered lane state. The physical state and service law still need specification. One narrower question remains: when the front package cannot enter, does exact allocation order require every later package to wait, even if a separate path is physically usable?

## Remaining questions, collected here for written discussion

You asked to discontinue interactive console questions. The remaining choices are collected below with this response. The console entries did not select a phase clock or a blocked-front policy; neither is inferred from them.

**A. Does phase dependence mean average service or actual on/off timing?** With average service, each movement's rate reflects the allocated fractions of the groups that permit it. With an active phase clock, the rate changes when phases switch, so the timing pattern becomes part of the traffic model. The first matches the established task and is my recommendation. The second may be useful but adds the previously omitted within-cycle assumptions. Agreement that service is a rate does not distinguish the two.

**B. What happens when the first package cannot enter?** Suppose the first package seeks a full left-turn bay and a later package could enter a genuinely independently accessible through lane. There are two distinct meanings of exact order:

- **Consider packages in their recorded order, keeping independent paths usable.** Leave the blocked package upstream, then admit later traffic only if its path is physically accessible. This retains a stable processing order without making one blocked destination close all other lanes. M2 uses this idea for precommitted independent lanes; extending it to the bay still needs a physical-access rule. Room alone is not permission to pass a real obstruction.
- **Require admitted traffic to be a strict prefix of the incoming queue.** Nothing behind the front package enters until it can be served. This is a natural description of one physical feeder queue with no bypass before allocation. Applied where paths really are independent, it adds cross-lane head blocking through the allocation server itself. That is a consequential traffic assumption, not merely exact bookkeeping.

I recommend making physical accessibility decisive: retain independent service where independent access exists, and enforce front blocking where the common queue actually prevents passage. The selected access model must specify that boundary. Your clarification establishes the importance of processing order but does not yet choose this blocked-front behavior. The supporting inventory records it explicitly as UR-G3-Q1.

## What is recorded now

| Topic | Disposition after this feedback |
|---|---|
| Initial queues | Candidate B accepted for development and early validation; direct prescribed states deferred |
| Responsive lane allocation | Recommendation changed to B; your preference recorded; concrete behavior remains open with the corrections above |
| Rate-based service | Rate principle endorsed; average-rate interpretation recommended; actual phase-clock meaning awaits clarification |
| Exact order and local mixing | Incoming package order governs allocation processing; realized lane states arise from admission/downstream dynamics; local mixing deferred; existing within-lane ordering retained |
| Blocked front at allocation | Newly explicit shared question UR-G3-Q1; processing order versus strict admission-prefix behavior remains open |

The phase interpretation and blocked-front choice remain open for written discussion. No false gradient guarantee, erased lane order, specific equilibrium or replacement of the M2 commitment contract is treated as accepted. The review remains in its current traffic-world/behavior discussion; it has not opened implementation or experiments. Future review questions will accompany the written response rather than appear in interactive prompts.

[Updated principle proposal](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md)

[Evidence and source-scope notes](../../extraction/research_readiness/urban_feedback3_evidence_notes.md)

[Current decision record](../../temp_content/research_readiness/phase_B_revision.md)

[Work record and checks](urban_feedback3_work_report.md)
