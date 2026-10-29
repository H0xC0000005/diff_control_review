> Historical review record. The implementation-phase framing is retired following the user clarification of 26 October 2026. Current material: [traffic_principles.md](traffic_principles.md).

# What must the urban model explain about queues, bay access and service?

Updated 23 October 2026 after feedback 4. All four broad principles are settled for this stage: loading from empty, responsive desired allocation, effective average service and exact order without deliberate local mixing. Logical assignment is separated from physical zone entry. Established lane commitments remain fixed by default; revisable waiting targets are a deferred alternative. Concrete coupled laws remain to be specified, especially under Q2/Q4.

A left-turn bay has room for four vehicle equivalents. A turner can use that room if it can reach the opening. If through traffic obstructs the opening, more left-turn service may achieve little until through service removes the obstruction. Two approaches with the same traffic totals can therefore respond differently to the same service allocation. Whether the proposed model captures that difference, and whether it helps choose service, remain questions to test.

The established urban review already gives us the experiment: allocate effective service, count everybody's time through completion, and compare cases that separate order, storage and access. The missing part is a model explaining what actually happens in those cases. The VSL report illustrates the intended standard: a reader can follow its traffic assumptions to a particular predicted outcome. Urban needs that clarity for its own traffic mechanisms.

| What the old review tells us | What the model still needs to explain |
|---|---|
| Initial queues can vary | Where that traffic is, whether it has reached service, and how the chosen starting queue is obtained |
| The bay has finite room and traffic has an order | Whether a particular turner can reach the opening |
| Each movement receives a service allocation | How shared traffic uses that allocation and how service removes an obstruction |
| Exact order is stored, while its use was left for later | Whether the model obeys that order exactly or deliberately approximates it |

These differences matter because filling them in can change the predicted benefit of left versus through service. They are not all equally large choices: initialization may reuse what already exists, while the coupled access and service rules still need actual modeling decisions.

## 1. Do we need to prescribe traffic already on the road?

The immediate question is how to obtain the starting queues needed by the urban experiments. We can let queues form from an empty road, or describe a nonempty road directly. M1 deferred the second capability; it did not reject it scientifically.

Why care? Ten vehicle equivalents waiting at the stop line can use extra service immediately. The same amount newly entering a long approach cannot. If the comparison intends the same physical start, matching counts without matching arrival readiness can create an apparent order benefit that actually comes from initialization.

**Candidate A — describe the queued road directly.** Supply the desired initial queue, its route/lane composition and enough travel history to say what is ready for service. This makes particular queue patterns easy to target, including patterns difficult to produce by the chosen loading process. Its cost is a new initialization capability: an occupancy number alone cannot supply the missing travel history. This extension is deferred.

**Candidate B — let the queue form first.** Start with empty physical links and use a common preparation period to create the desired queued situation. The traffic and its history are produced together, which reuses the existing approach. The limitation is that the selected preparation may not produce every queue pattern the experiment needs.

The user accepts B for development and early validation. A later direct initializer would need new experiment evidence and a separate decision. The preparation must be fixed while candidate service allocations are compared, and its contribution to the time account must be explicit. If the candidate allocation also changes how the starting queue forms, we are asking a different control question and must include that effect in the sensitivity. Coverage of every eventual queue case is not claimed here.

The evidence supports this narrower choice. [VSL specifies one restricted initial traffic family](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L44). Urban [names initial state](../../synthesis/experiment_formulation_formal.tex#L25) and [varies initial queue](../../synthesis/primary_green_allocation_suite.md#L109), while [M1 defers direct nonempty initialization](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md#L49). The missing connection is how urban obtains its required starts; the standard itself does not require Candidate A.

## 2. Is physical obstruction enough, or must drivers also change their lane choices?

The central distinction is between wanting the bay and being able to reach it. The trapped turner still wants to turn left even when the bay has room. A model that sends it into the bay merely because space is available would erase the obstruction we want to study.

Both candidates below therefore need an actual physical-access rule. They differ in how much lane-choice behavior to add around it.

**Candidate A — hold intended lanes fixed and model what blocks access.** Each traffic group has a declared intended lane. Its ability to reach that lane depends on the queue, geometry and available room. This isolates the order/access mechanism: service helps by moving traffic that physically obstructs the turner. It is a useful starting point when routes and lane permissions already determine the intended destination. It misses changes in lane preference where drivers have genuine alternatives.

**Candidate B — let lane preferences respond to congestion, then enforce physical access.** Where more than one lane is legal, drivers may prefer a less congested lane. That response can change the queues that later obstruct the bay. This is a stronger behavioral model, but it adds assumptions about drivers' information and response. A preferred lane must still be reachable; changing a preference cannot move traffic through an obstruction.

For a turner with only one legal approach path, B offers no alternative destination and does not solve its access problem. Its added value arises when other traffic can make meaningful lane choices. B is now the agreed main direction, with A retained for controlled diagnostics. The earlier context discussed this direction but did not select a concrete waiting-zone equilibrium. The allocation cost and physical-access law still need specification; that does not reopen the broad choice of responsive allocation.

Fixed lane assignment can still have continuous control sensitivities: more service can drain a fixed-lane queue faster without a threshold switching. Responsive allocation adds a possible physical sensitivity path; it does not guarantee smooth or useful gradients. It is also not inherently packet defragmentation—splitting traffic between lanes can create more fragments.

Feedback 4 makes a useful separation: a packet can receive desired lane shares and wait upstream even when it cannot physically enter the zone. Such lane-specific waiting records remain views of upstream mass, not extra physical buffers or admitted zone traffic. Reusing an already valid desired lane can avoid a repeated allocation solve; inventing a target because traffic is far upstream would change the behavior.

The existing fixed-commitment contract supplies the default: responsive allocation creates valid lane commitments, and waiting mass keeps those targets until admission. Provisional targets that can adapt while waiting remain a distinct deferred alternative; no extra principle vote is needed to preserve the inherited rule. The concrete proposal must establish where commitment occurs and how the allocation step feeds M2's ingress. No change to its timing, physical partition or actual resident lane membership is approved here.

The gap is visible directly in the records: [VSL defines transfers](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L121), whereas [urban's access expression lists what access depends on](../../synthesis/experiment_formulation_formal.tex#L165). The inherited [M2 neutral domain excludes shared-lane and pocket obstruction](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md#L26), and [the urban handoff leaves the bay rules to be supplied](../../synthesis/project_impact_matrix.md#L19). We still need the rule explaining why spare room is reachable in one queue and unreachable in another.

## 3. Does service act continuously, or through separate opportunities in time?

Giving left and through traffic half the service budget each does not tell us when either can move. If a left-turn block is at the front of a shared lane, the timing of its service can determine how long through traffic behind it waits. The choice can change both total time and which reallocation looks beneficial.

**Candidate A — treat the allocation as a continuous service rate.** Each movement has service available at its allocated average rate. A coupled traffic rule decides how order, access, shared lane capacity and downstream room limit its use. This preserves the accepted urban simplification and avoids introducing a signal cycle. Its challenge is to explain blockage coherently under averaged service; a capacity bound alone does not do that, and average service cannot reproduce every red/green effect.

**Candidate B — give the same budget an explicit pattern in time.** Specify when movements receive service opportunities. A front turner waits until its opportunity, and following traffic responds to that wait. This makes timing-related blockage easier to interpret, but the prediction now depends on an additional timing pattern. It changes the accepted omission of within-cycle timing and would need that extra modeling choice to be agreed. It does not by itself add a new optimized cycle or sequence.

Feedback 4 explicitly selects A's average-rate meaning for the present stage. Phase-group fractions scale service for their permitted movements; an active phase clock is deferred. This principle question is settled. Physical lane capacity, movement service opportunity and realized discharge remain distinct, and the coupled shared-lane law still needs specification.

The justification needs one qualification: changing a green duration can have a nonzero effect through its switching time, even when an instantaneous on/off mask stays unchanged at most sampled times. Average service avoids that extra timing treatment; it does not establish that phase-based gradients are inherently zero or that realized-flow gradients are always nonzero.

[VSL specifies the law that determines service](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L161). Urban [specifies average capacity while omitting within-cycle timing](../../synthesis/experiment_formulation_formal.tex#L40). The inherited [M0 signal branch also assumes common service exposure for an input's movements](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_0_ltm_baseline.md#L426); independently allocated left/through service in a shared lane needs its own compatible rule. This is a traffic-law choice, not a missing numerical coefficient.

## 4. How much of the actual order must control movement?

Keeping an exact record of order does not mean every model operation obeys it. The question is whether service and access follow that record exactly, or intentionally ignore some small-scale order differences to simplify the model.

**Candidate A — preserve the selected lane order exactly.** Under the chosen physical-access rules, traffic cannot pass a blocker merely because a coarser representation places both in the same group. This gives a clear reference for obstruction. The cost is more detailed state and more changes in which traffic block is currently active. Exact order also cannot rescue an incorrect access or service law.

**Candidate B — allow a declared amount of local mixing.** Retain order between groups but treat some mass within a group as mixed. This could reduce complexity and directly test whether a coarser representation is enough. It can also let a turner pass a through block that would obstruct it under exact order. A small group size does not guarantee a small waiting-time or gradient error. The user defers this optional direction for the current development path; it is not a required comparison campaign here.

Following feedback 3, I recommend exact incoming and realized per-lane order without deliberate local mixing. This is a defensible scope choice, not evidence that mixing is impossible or exact order guarantees better gradients. Exact lossless adjacent merging remains a separate allowed bookkeeping operation.

Lane allocation can create separate ordered streams, but occupancy alone does not identify their fronts. In one shared lane with no bypass, four through units ahead of a blocked left-turn unit can discharge; the reverse order cannot, despite identical composition. Deterministic allocation does not generally remove that distinction.

Link package order controls allocation processing, while actual admissions and downstream conditions create realized lane states. Existing within-lane order is retained. Feedback 4 separates completion of logical allocation from physical entry: the first packet may be assigned to upstream waiting records without entering the zone, so its physical wait need not stop logical processing of the next packet.

An eligible, reachable packet can enter partially whenever positive feasible receiving is available; it need not fit as a whole. The residual remains upstream. Positive room or service alone does not establish reachability, and no small positive admission cutoff is selected. Later physical entries must obey the actual common-queue or independent-path geometry, not merely the labels of the waiting queues. The earlier scan-versus-prefix alternatives remain physical-access possibilities rather than a universal metadata scheduling choice.

A model organized around passage times—when ordered traffic enters or leaves—could implement either choice. It is a way to organize traffic evolution, not a third amount of order information.

The [VSL branch rules determine modeled behavior](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L182). Urban's [accepted P8 record left the order-resolution policy open](../../synthesis/project_impact_matrix.md#L33). The present direction retains exact order and defers deliberate mixing. A strict global physical-admission prefix is not inferred from exact allocation processing.

## What is settled and what still needs discussion

Q1 is settled for development and early validation: load from empty. Q3 is settled for this stage: use effective average service. Q2 uses responsive desired allocation and Q4 preserves exact order without deliberate local mixing. All four broad choices are settled. Valid lane commitments remain fixed under the existing default; provisional retargeting is retained as a deferred alternative rather than another required gate.

The allocation cost, physical access, shared service and precise update law remain to be proposed. Those are the model specification under the agreed directions, not evidence that all four original principle questions are still unresolved. Any later detail that changes the traffic predictions returns for discussion.

The accepted experiment still uses continuous traffic mass, fixed routes and geometry, per-lane local refinement and physical storage, with complete total system time. V0–V4 and the established comparison/evidence requirements remain the basis. Consolidate these principles and continue the remaining global discussions before formal component closure. A later authorized coupled proposal uses the agreed principles and returns genuine conflicts as explicit amendments. No positive cutoff, extra physical buffer, reassignment of resident traffic or replacement commitment interface is approved here.

[Overall review plan](phase_A_proposal.md)

[Full question set and supporting ownership/dependency map](../../extraction/research_readiness/urban_open_question_register.md)

[Decision and discussion record](phase_B_revision.md)

[Feedback 2 work record](../../reporting/research_readiness/urban_feedback2_work_report.md)

[Feedback 3 response and critical corrections](../../reporting/research_readiness/urban_feedback3_response.md)

[Feedback 4 response: settled principles and upstream waiting](../../reporting/research_readiness/urban_feedback4_response.md)
