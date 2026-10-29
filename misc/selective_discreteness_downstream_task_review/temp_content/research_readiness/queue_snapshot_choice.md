# Historical question: what does the allocator do with a frozen queue?

Originally discussed 26 October 2026. **Superseded by the feedback-7 amendment:** the user withdraws the freeze and selects sequential packets with progressive per-packet lane balancing. The former question and recommendation below are retained as history, not current alternatives. The last question in this batch is resolved; explicit closure is still pending and no next batch is opened.

[Current amendment response](../../reporting/research_readiness/urban_feedback7_amendment_response.md)

## The difference in your example

The bay already holds 0.2; the other lane is empty. One new homogeneous unit can legally use either lane. Assume equal geometry/cost scales and enough physically reachable room for either outcome.

**Balance the incoming load against the frozen background.** The allocator chooses lane amounts together. It sends 0.4 to the bay and 0.6 to the other lane, so both end at 0.6. It uses the starting queues once and accounts for how much of this new load it puts in each lane. It need not process drivers one by one or update an observed queue between them. This is the one-shot equilibrium interpretation.

**Keep the entire preference fixed while assigning the load.** The other lane was cheaper at timestep start and remains cheaper in the calculation, however much new traffic is assigned there. Under deterministic least-cost choice, all of the new unit is intended for that lane.

| Interpretation | New mass to bay / other lane | Resulting loads |
|---|---|---|
| Frozen background, joint balancing | 0.4 / 0.6 | 0.6 / 0.6 |
| Fully fixed costs, deterministic least-cost choice | 0 / 1.0 | 0.2 / 1.0 |

The second result follows from the stated least-cost rule, not from frozen observations alone. A different fractional choice rule based on the same observations could be defined, but it would require its own explicit model. No such extra rule is selected here.

## Why this point was raised

Feedback 6 asks for one-shot lane equilibrium and uses the balanced split. Feedback 7 freezes the observed queue to avoid chained updates. Those requests can coexist: keep the background fixed and compute a balanced assignment jointly. They cease to describe the same allocation if “frozen” also removes the new load from the balancing calculation.

That changes traffic, rather than just computation. The table gives different lane occupancies and therefore different conditions for subsequent filling and blockage. For instance, increasing the initial bay queue from 0.20 to 0.22 changes the balanced additions to 0.39/0.61. The strictly fixed-cost least-cost assignment stays 0/1 while the other lane remains cheaper. This difference can affect the allocation's response to queues produced by earlier signal control; it does not establish which model has more useful full-system gradients.

## How to resolve it simply

**My provisional recommendation is to freeze the observed background and retain one joint balancing calculation.** This preserves the earlier equilibrium behavior and removes sequential observation updates. Its inputs are the starting queue, the traffic being allocated and fixed legal/geometry data; no service-plan knowledge or future queue observation is required. The allocation variables remain coupled within that one calculation, so this does not remove every dependency from the model.

If the intention is instead to exclude all same-step load balancing, the fixed-cost interpretation is a different valid simplification, with the changed behavior shown above. The decision to confirm is therefore whether avoiding the sequential update chain still permits a joint equilibrium calculation. This recommendation is not recorded as user approval.

The eventual law must define the physical traffic group being allocated, so arbitrary software packet cuts do not change the answer. That is a construction requirement, not an extra question about target priority. Physical receiving is still consumed, existing targets stay fixed, and source/realized-lane order remains. The residual and receiving-sharing questions stay settled.

[Feedback 7 response: brief agreements and current status](../../reporting/research_readiness/urban_feedback7_response.md)
