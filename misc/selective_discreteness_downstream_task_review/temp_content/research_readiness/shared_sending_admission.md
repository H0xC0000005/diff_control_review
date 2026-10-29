# Shared-sending question: superseded for new allocations by feedback 9

**Current disposition after feedback 9:** compute a new allocation using known transfer feasibility, rather than requiring a full unconstrained assignment followed by a separate rationing decision. The former A/B question and recommendation are withdrawn as the current gate for new allocations. This note retains the conditional precommitted-target example for traceability. No reply is needed on its old binary choice.

[Separate feedback 9 answer and qualifications](../../reporting/research_readiness/urban_feedback9_response.md)

For a fresh allocation with known feasible admission 0.6, the selected ideal queue-balancing direction can directly admit 0.2/0.4 and leave queues 0.4/0.4. This is not automatically approval of former Candidate B with an independently fixed target vector. Existing valid waiting commitments remain constraints; feedback 9 does not itself authorize retargeting them. Dynamic changes in feasibility must be handled consistently in later transcription, which is not opened by this answer.

The remaining text is the historical conditional case: it assumes valid targets already exist independently of the present capacity. That case is not a general argument for ignoring known constraints when creating a new allocation.

The agreed example assigns a homogeneous packet to two legal lanes. Existing queue loads are 0.2 and 0; the packet has mass 1. Ideal intended balancing assigns 0.4 and 0.6. Those commitments stay fixed. Each lane's physical storage is 0.5, so their admission allowances are 0.3 and 0.5. With nonbinding feeder sending, the accepted result is admission 0.3/0.5 and pending targets 0.1/0.1.

Now change only the shared feeder bound: **at most 0.6 can pass in this update**. The whole parent packet is ready, its commitments already exist, and both branches are accessible. This may be a capacity-limited sending bound; no delayed-time query is involved. The same two legal alternatives are assumed as in the agreed example, without expanding the primary lane permissions.

Both following rules use all 0.6 and preserve the original targets, source-parent order and mass. They differ in which targeted portions enter first:

| Admission rule | Enters lane 1 / lane 2 | Pending targets | Lane counts after the update |
|---|---:|---:|---:|
| Follow the fixed target proportions, with feasible caps and reuse | 0.24 / 0.36 | 0.16 / 0.24 | 0.44 / 0.36 |
| Balance actual destination queues, within the same fixed target caps | 0.20 / 0.40 | 0.20 / 0.20 | 0.40 / 0.40 |

**Follow fixed target proportions.** The packet already intends a 40:60 split. Share scarce admission in that ratio, capping a lane when it cannot receive more and reusing capacity for the other target. This uses the existing commitments as the admission weights. It keeps intended allocation and physical realization distinct, but need not equalize the realized queues during a partial admission.

**Balance realized queues.** After respecting the fixed target amounts and physical bounds, give more of the current admission to the less occupied lane. This retains ideal equality in the actual queue state where feasible. It does not retarget traffic: the unserved target amounts remain upstream. It adds a queue-balancing criterion to the timing of realization, beyond balancing the full intended assignment.

Both preserve total intended load 0.6/0.6 when each lane's physical count and pending commitment are added. The earlier agreement settles that intended total; the original nonbinding-sending example does not distinguish these two admission rules. No artificial ordering of the homogeneous packet's target children is required by either rule.

This matters at the present scope because the **end-of-step state itself differs**. Its response to the shared sending bound and to queues already formed by previous control can differ. These are ingredients of the timestep-to-timestep sensitivity chain. A fixed-state direct response to the current signal can still be zero when that signal does not affect admission; no immediate TST difference is claimed merely from moving mass between source/feeder and lanes.

**Historical recommendation, withdrawn as a new-allocation gate:** target-proportional sharing had been provisionally favored for the independently precommitted case. Feedback 9 instead requires known physical feasibility inside creation of a new allocation. Neither old candidate becomes the general accepted allocation law by that correction.

**No current decision is requested on this old comparison.** The new-allocation dependency is settled by feedback 9; the exact coupled rule and handling of changed feasibility remain later transcription under the existing order, conservation and valid-commitment constraints. The user asks only for the feedback answer, so no next step is started here.
