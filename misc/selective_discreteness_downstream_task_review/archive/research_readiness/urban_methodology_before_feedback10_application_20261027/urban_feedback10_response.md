# Feedback 10: answers and current decisions

The policy choices are now much clearer. The remaining model issue is how movement-specific skipping fits the physical common-feeder geometry. It is not another question about allocating frozen waiting targets.

| Question | Current status |
|---|---|
| 1. Legal lanes | **Resolved:** B for the starting bay/shared-lane scenario; permissions remain scenario-dependent. |
| 2. Binding location and progressive loading | **Resolved in principle:** bind at actual lane admission and count earlier admissions when processing later packets. Physical placement is part of the Q3 issue below. |
| 3. Unadmitted remainder | **Resolved policy:** no binding target; retain priority within its movement and continue considering other movements. **Open model detail:** how that processing maps to physically accessible paths. |
| 4. Old multi-lane waiting targets | **Withdrawn:** your answer to Q3 removes its premise from the selected empty-loaded model. |
| 5. Receiving allowance | **Resolved:** retain A, with the dependency correction below. |

## 1. Legal lanes: B is the starting scenario, not a universal rule

Agreed. Both layouts are legitimate scenario choices. For the starting bay configuration, select a left-only bay alongside a lane shared by left and through/right traffic. This allows the heterogeneous lane order you want and gives left traffic a genuine lane-choice alternative.

The exclusive-target layout remains valid where the scenario specifies it. Corresponding V2/V3 cases and their comparison models must share the chosen permissions; the existing movement-exclusive V0 remains its neutral case. This decision selects a configuration, not one permission matrix for every scenario.

## 2. Two different meanings were being compressed

The earlier question concerned **what later packets see during one allocation calculation**. Once an earlier packet has added traffic to a lane, the next packet must see that addition. That progressive update is already agreed and does not need another vote.

The newer question concerned **where along the road a fresh lane choice first becomes binding**: before travelling through the feeder, or when the traffic can actually enter a realized lane. Both locations could use progressive updates, so the questions are logically distinct. I did not make that distinction clear enough.

Taken together, your answers 2 and 3 provide the useful rule: **only admitted mass becomes lane-committed; later packets count the earlier actual lane admissions.** The unadmitted remainder is not assigned fictitious lane loads. I record that rule, rather than asking you to repeat the earlier progressive-loading decision. Where this allocator sits relative to a physical common feeder is the remaining Q3 consistency issue.

## 3. The remainder is unassigned; processing order is distinct from physical passage

Accepted: the remainder stays with its link-end physical stock, without a frozen lane target. It gets priority over later packets of the same movement next time. A failed left allocation does not by itself require the allocator to stop inspecting later through packets.

This explicitly replaces my proposed frozen waiting-target convention. Your proposal also corrects my Candidate B description, which unnecessarily made an unassigned residual stop all later logical processing.

Your earlier explanation that link ordering determines the allocation server's processing order supports this interpretation. **Inspecting a later packet does not itself establish that the packet can physically pass.** Two situations must remain distinct:

- In a logical allocation waiting pool, through traffic may be admitted after an unsuccessful left packet if its own path is accessible and its transfer constraints permit it.
- If the left traffic already occupies the front of a single physical common lane, through traffic behind it cannot pass merely because through service is available. That requires independently accessible space or an explicitly different physical arrangement.

The current draft put the allocator at the front of a physical common feeder and imposed a common prefix gate there. It does not yet distinguish that physical gate from the logical movement-specific processing you intend. **That connection remains open in the model; the processing policy itself is agreed.** I should not declare the full coupled rule finished before reconciling them.

One related qualification matters with the chosen shared-lane permissions: a full bay alone does not make a left packet wholly unadmittable if the shared lane is reachable and has room. Also, a lack of left-turn junction service is not automatically a prohibition on joining an upstream lane queue. The admission constraint and the stop-line service constraint must refer to the appropriate physical boundary.

## 4. Why it appeared, and why it now disappears

This question came from **my additional assumption that unadmitted mass already carried fixed future lane totals**. Those totals would determine where the mass must eventually go, but not which share enters first when only part can transfer. That was the distinction behind the proportional-versus-queue-balanced alternatives.

Your answer 3 rejects creating those waiting commitments. There is consequently no old multi-lane waiting vector to ration in the selected empty-loaded model. Already admitted traffic has a realized lane and follows that lane's order.

**Withdraw Q4. No further allocation choice is needed for it.** The old example remains a conditional illustration of an assumption we are not selecting.

## 5. Retain A, while correcting the dependency explanation

A does simplify the receiving calculation by avoiding a separately depleted receiving pool. It does **not** eliminate sequential dependence between discharge states: a head must still clear before its next head is exposed, and that clearance changes the currently competing set and subsequent sharing.

Those dependencies belong to the elapsed-service/current-head rules already selected. A removes the additional pool-exhaustion mechanism; it does not make the successive head states independent.

With that correction, **retain A as instructed**. The constant average receiving convention and existing boundary histories stand. No event-history refinement or new phase model is opened.

## What remains open

Only the **physical application of movement-specific skipping** remains to reconcile with the current common-feeder representation. The intended policy is recorded; no replacement joint model is derived in this answer-only response.

The answers above close or withdraw the other points at the level discussed. No next task, model-development pass, implementation or experiment is started.
