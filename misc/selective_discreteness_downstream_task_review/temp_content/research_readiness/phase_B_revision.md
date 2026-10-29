> Historical review record. The implementation-phase framing is retired following the user clarification of 26 October 2026. Current material: [review_decisions.md](review_decisions.md).

# Urban refinement: settled traffic principles and the next discussion

Updated 23 October 2026 after the user opens the next review task. Phase B now has an unapproved categories 3–5 proposal. The preceding four traffic principles are settled for the present stage and do not block this discussion. The inherited fixed-commitment rule is retained by default; provisional retargeting is deferred. Concrete coupled laws and their integrated contracts remain to be specified, especially under Q2/Q4.

[Feedback 4 response and current four-question status](../../reporting/research_readiness/urban_feedback4_response.md)

[Current proposal: fair comparison, complete sensitivity and scientific credit](phase_B_categories_3_5_principle_proposal.md)

## Current four-question status

| Original topic | Principle status | Remaining model work |
|---|---|---|
| Q1 / initialization | Settled for development and early validation: load from empty; direct prescribed states deferred | Preparation, accounting and required-case coverage |
| Q2 / allocation and access | Responsive desired allocation agreed; fixed allocation retained for controlled diagnostics | Concrete allocation/commitment interface, perceived cost/information, solution and physical-access law |
| Q3 / service | Average phase-fraction service accepted for this stage; active phase clock deferred | Shared-lane service/resource and receiving law; complete conditional sensitivity |
| Q4 / order | Exact incoming allocation order and realized lane order retained; local mixing deferred | Consistent waiting/admission order under the chosen commitment and physical-access model |

The broad option selections do not need to be repeated. Specification work is still required before the methodology is reconstructible, but that is not a reason to describe all four principle questions as unresolved. The existing no-reassignment contract already supplies the default for a valid commitment while waiting. There is no new mandatory fixed-versus-provisional principle vote absent a reason to reconsider it. The concrete allocation point and compatibility with that seam still require a reviewable model proposal.

## What feedback 4 establishes

Average service is explicitly selected. The accepted movement/phase permission map supplies its dependence on allocated fractions. The response corrects the accompanying zero-gradient generalization: changing green duration can act through switching-time sensitivity. Average service is chosen for its fit to the current abstraction and reduced timing complexity, without assuming that every realized flow or objective gradient is nonzero.

Eligible, reachable mass may enter partially whenever positive feasible receiving is available. A packet need not fit as a whole. Its remainder stays upstream. Positive lane capacity or room alone does not prove physical access or travel eligibility. No small positive admission cutoff, rounding or mass deletion is selected.

The user's upstream-queue proposal separates logical assignment from physical entry. An assignment can complete in source order while its mass remains upstream, so a physical wait need not stop subsequent logical allocation. Pending lane-specific queues are initially logical records/views of mass in the existing upstream link, counted there exactly once. They do not provide extra physical storage, zone occupancy or early service readiness. Physical upstream lane expansion is not inferred.

Appending directly to an already valid desired lane is a reuse of an earlier choice. Without that choice, bypassing the allocation solver would change the responsive model; being far upstream is not itself a lane-assignment rule.

## UR-G3-Q1: default commitment and its deferred alternative

The existing ID is retained and its earlier framing refined. Its original A/B candidates describe independent-access versus strict common-feeder physical admission. They remain conditional access alternatives, rather than a universal scheduling rule. New C/D candidates describe waiting-target behavior:

- **C: commit after logical allocation (default).** Responsive shares produce lane-targeted upstream waiting mass; valid commitments stay fixed until entry. This is the documented reading of the staged proposal that preserves the inherited rule. Compatibility with the existing seam must be established in the concrete proposal.
- **D: keep targets provisional until entry (deferred).** Waiting shares could respond again to changed conditions; admission would fix realized lane membership. This is a distinct alternative requiring explicit reconsideration of commitment, order and priority. It is neither selected nor a new mandatory gate.

Feedback 4 proposes upstream assignment without requesting later retargeting. Retain C's fixed-commitment default; do not attribute a new retargeting decision to the user. This is not approval of a concrete solver or changed physical interface. A desired target can be reused only while it remains valid under the chosen policy. No reassignment of actual resident traffic is proposed. A genuine conflict discovered while constructing the model must reopen the smallest affected contract, rather than activating D locally.

UR-G3-Q1 remains Type 2: its physical ownership and commitment interface must be consolidated before dependent components close. C1 now explicitly consumes that contract alongside C2/C3 and comparison. This is a dependency clarification; the existing 15 IDs and classifications remain intact.

## Existing contracts and review boundary

M2's closed G2 uses one precommitted lane per entry, conservative U/Z transfer, retained upstream residuals, delay eligibility and no silent load balancing/reassignment. Locate the responsive allocation step relative to that seam. Any changed commitment meaning or physical ownership must be explicitly reconsidered before adopting a concrete replacement. The accepted M2 record, approved milestone plans and simulator are unchanged.

V0–V4, effective-service action, complete TST, continuous mass, fixed routes/permissions, per-lane local refinement, physical storage/conservation and staged evidence remain accepted. P8 reconsideration remains authorized. Neither a specific equilibrium nor a complete access/service transaction is approved here.

The category-led principles-first format and feedback-2 readability instruction remain accepted. Follow-up questions are collected with the written response; interactive console prompts are not used. Prior corrections remain: fixed lanes can have continuous sensitivities, responsive choice is not a smoothness guarantee, redistribution is not intrinsically defragmentation, and deterministic allocation does not justify deleting lane order.

## Categories 3–5: next review task opened, recommendations unapproved

After clarification that Q2/Q4 do not block the current principle gate, the user asks whether next-step material is ready and then authorizes opening that task. The opening produces the focused discussion proposal and supporting evidence. It does not repeat the Q1–Q4 vote or select their missing concrete laws.

| Topic | Current proposal | Status |
|---|---|---|
| UR-G4; Type 2 | Rival-specific lawful observations/history inference and matching; universal indistinguishable pairs as stronger diagnostics where feasible | Provisional; user review pending |
| UR-G5; Type 2 | Complete TST under the existing D2 control/clearance default; common sufficiently long horizon where local clearance holds | Provisional; user review pending; actual selected-law derivatives remain later |
| UR-C7-Q1; Type 1 | Adjacent causal/source explanation backed by a complete equation/source map | Provisional presentation approach; attribution requirement already established; no new global ID or gate |

The proposal distinguishes matching common exogenous inputs from forcing equal endogenous allocation outputs. It also makes the D2 reading explicit: a candidate-independent fixed clearance policy removes direct candidate-service dependence after the handoff, without removing the response of the inherited traffic state. D2 remains a default and its numerical continuation is unselected. These clarifications synchronize the live candidates; they do not approve a new method.

The 15 IDs, 33 candidates and ownership/dependencies are retained. UR-C4-Q1/Q2, C5-Q1, C6-Q1 and the exact C7 source records remain dependent component work. The next allowed action is discussion/revision of this proposal, followed by consolidation of shared contracts before formal component closure. Q2/Q4 return only for a genuine conflict or materially different traffic assumption, not merely because equations remain to be written.

Settlement of the traffic principles and opening the new discussion do not close all shared contracts or approve implementation. No installation, numerical gradient check, optimization or SUMO stage is opened. The later authorized coupled proposal uses the existing commitment default and returns any necessary amendment explicitly.

[Settled traffic-principle proposal](phase_B_categories_1_2_principle_proposal.md)

[Full inventory and candidates](../../extraction/research_readiness/urban_open_question_register.md)

[Discussion history](phase_B_dialogue.md)
