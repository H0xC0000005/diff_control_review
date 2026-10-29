# Remaining questions for the joined lane model

Questions posed on 26 October 2026, before feedback 7. **Historical question note:** the feedback-7 amendment resolves the last follow-up through source-order packets with progressive per-packet lane balancing. The original questions below remain for traceability. The batch is ready for explicit closure; no next batch is opened.

[Current amendment response and qualifications](../../reporting/research_readiness/urban_feedback7_amendment_response.md)

[Feedback 7 response](../../reporting/research_readiness/urban_feedback7_response.md)

[Historical explanation of the resolved frozen-queue question](queue_snapshot_choice.md)

The agreed foundation is internal bay geometry, queue-based lane choice, joint splitting of a homogeneous source block, elapsed-rate lane service and reuse of downstream receiving room. Fixed commitments, original source-block order and realized-lane order remain constraints on the formulation.

## Which traffic does a driver count when comparing queues?

Two lanes can have equally long stopped queues while one has more traffic already approaching or committed to it. Counting that traffic can change the preferred lane; counting only the ready queue can give a different allocation.

Queue-based perception is agreed. Its precise content is open: which visible or committed approaches count, how far the observation extends, and how congestion is normalized across lanes. The current provisional reading includes queue plus committed approaches, counted once, without service-plan knowledge or forecasting motion. A stopped-only reading remains possible; neither interpretation is an additional user decision yet.

**The next proposal needs to define the perceived congestion measure and explain its traffic meaning.**

## How does a homogeneous block enter partly while keeping its commitments?

The agreed example fills both accessible lanes and leaves 0.2 upstream. That establishes the desired static behavior without inventing an order between new lane targets. A changing traffic state also needs a rule for which lane amounts enter as receiving becomes available and which amounts remain waiting.

Physical location and lane target must stay distinct. If the intended additions were fixed at bay 0.4 and other lane 0.6, but actual additions were 0.3 and 0.5, the pending targets are 0.1 for each lane. Both can be physically on the common feeder. I currently read “0.2 on the shared lane” as that common physical location; this interpretation remains provisional.

**The next proposal needs to specify the allocation location, feasible partial admissions and residual target accounting together.** It must preserve existing commitments and traffic order, respect physical blockage and causal travel/receiving, and conserve mass. This is a joint traffic-law question, not another `A.pieces`/`A.curve` choice.

## How do competing lanes share limited downstream room?

Suppose two independent ready lanes can each send 0.8, while their common exit can receive only 1.0. Both 0.5/0.5 and 0.2/0.8 use all the available room. Receiving reuse alone does not select between them.

**The next proposal needs a simultaneous sharing rule**, based on declared physical priorities or feasible demand, that works with elapsed-rate service and physical FIFO. It must explain how blocked or exhausted demands release room to other reachable traffic. This introduces no phase precedence or software lane-visiting priority.

These are remaining scientific definitions for the combined model. They do not reopen the five agreed directions, and none of their precise answers is selected by this note. Numerical implementation and experiments remain separate.

[Agreed choices and current decisions](review_decisions.md)

[Detailed traffic examples and candidate history](coupled_lane_access_and_service_discussion.md)
