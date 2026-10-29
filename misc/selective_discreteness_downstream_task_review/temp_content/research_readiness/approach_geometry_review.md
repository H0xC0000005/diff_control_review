# Approach geometry: a parallel through/right lane

**Current disposition, 28 October:** feedback 11 authorizes incorporating the proposed geometry in the first PDF revision batch. It is now represented by U to parallel F1/F2, F1 to left-only B and through-only T1, and F2 to shared through/right T2. Through traffic chooses between feeders at actual admission from U, using their current local loads and feasible receiving. Both feeders end at the bay-opening cross-section. Traffic retains its realized feeder; no resident cross-lane reassignment is added. The current report and companion are synchronized. The suitability assessment below is historical rationale; its former “adoption open” status is superseded by this authorization.

[Feedback-11 revision](../../reporting/research_readiness/urban_feedback11_response.md)

27 October 2026. **Status: assessment and provisional recommendation.** The user asks whether a three-lane stop-line layout is sound and whether the two-lane layout is too simple. This reopens only the representative geometry/permission choice for discussion. No replacement is selected, and the current PDFs retain the previously selected geometry.

The proposal is sound as a traffic-model case. Its useful addition is an independently accessible parallel path: blockage in the lane feeding the left bay need not stop every through vehicle. I provisionally recommend it as the representative case, retaining the simpler geometry as a diagnostic. This is a judgment about the test's scope, not evidence of improved prediction or gradients.

## What the two cases represent

**Existing report case.** One physical local feeder F branches to a left-only bay B and a left/through/right continuation T. Left turns have two legal stop-line targets. Exact order can matter both before the fork and within the shared continuation. With no independent parallel feeder, an obstruction in F can affect all approach traffic. This is a coherent minimal mechanism test, but it cannot test how a parallel lane moderates that effect.

**User's proposed case.** Read the layout as two upstream lanes and three lanes at the stop line:

- The upstream left/through lane feeds the finite left-only bay and the through-only continuation.
- A parallel upstream through/right lane continues to the shared through/right stop-line lane.

The bay opening stays inside the local zone. The parallel lane needs its own physical occupancy, propagation, storage and ordered service. Sending all three terminal lanes through the old single F would retain the old common bottleneck and miss the intended distinction.

Suppose the bay is full and the first lane's head needs to turn left. Through traffic physically behind it waits, while traffic already in the accessible parallel lane may continue if service and downstream room permit. The FHWA Traffic Signal Timing Manual describes both turn-bay entry obstruction and overflow that impedes an adjacent through lane; it does not imply that every parallel lane must be blocked. This supports the mechanism, not a specific numerical setup or a claim about which information representation wins.

[FHWA Traffic Signal Timing Manual, section 6.7.6: turn-bay interactions](https://ops.fhwa.dot.gov/publications/fhwahop08024/chapter6.htm)

The richer case asks whether retained order still matters when traffic has an alternative lane. The extra lane may attenuate the effect; a weak or absent advantage for the selective model is a legitimate result. The two-lane case is useful for checking the mechanism but alone gives a limited basis for broader claims.

## What would change if adopted

This is more than adding capacity. In the proposal, left turns must use the bay, whereas the existing report also lets them use T. Mixed left/through order remains in the upstream feeder; through traffic gains possible alternatives between the two upstream lanes. Responsive allocation would therefore have to respect where those alternatives are physically reachable. A resident in the blocked feeder cannot jump to the parallel lane merely because it has room. The exact admission location and connectivity must be written before incorporating the geometry into the model.

The shared through/right lane does not automatically create a new order effect. Those movements share the current effective service group; differing saturation or outgoing receiving constraints can make their order matter, while identical effective conditions can make them equivalent for service. No new signal group or microscopic lane-changing model is implied.

Continuous mass, fixed routes, actual-admission commitment, occupied-lane FIFO, average service, current-ready-head receiving and complete TST remain the agreed principles. V2/V3 and compared models must use matched geometry, permissions and available information; the added capacity is not itself evidence for order retention.

**Remaining choice:** use this geometry as the representative case, add it as a companion case, or retain the current geometry alone. The provisional recommendation is the first, keeping the old case as a small diagnostic. Adoption and a consistent topology/allocation transcription remain unapproved. No experiments, implementation or PDF rewrite are undertaken in this assessment.

[Current report and reading guide](unified_methodology_draft.md)

[Decision record](review_decisions.md)
