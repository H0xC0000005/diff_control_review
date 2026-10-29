# Feedback 9: feasibility belongs inside the allocation

Your dependency is sound: **a new allocation should use the currently known transfer capability as a constraint**. Queue balancing should choose among feasible allocations. I made a particular precommitted-target case carry the general design question; that is not a reason to require an unconstrained assignment followed by a separate rationing decision.

For a fresh allocation in the example, the known feeder limit allows 0.6 to enter. With existing queues 0.2/0 and lane admission allowances 0.3/0.5, ideal balancing of that feasible admission gives **0.2/0.4**, leaving lane queues **0.4/0.4**. The remaining 0.4 stays upstream. We should not first manufacture a 0.4/0.6 assignment for the whole unit while ignoring the known sending limit, then ask how to ration it. The intended assignment, feasible admitted amounts and any waiting records need a consistent construction.

This corrects the setup of new allocation; it is **not simply a selection of my former Candidate B**, which assumed the full target vector was already independently fixed. I withdraw the old two-option question and recommendation as the current gate for new allocations.

The useful technical distinction is between **known feasible limits** and **final realized discharge**. We can know sending, receiving, available storage and current accessibility before allocating without already knowing the final flow. If allocation changes blockage, those allocation-dependent constraints must be enforced during the calculation, or updated as earlier transfers consume resources. That is consistent with your qualification. It does not require predicting a later outcome and feeding it back as an already known input.

There is one boundary to preserve: the earlier example explicitly postulated **valid commitments made previously**. Knowing today's capacity does not itself cancel those commitments. Your proposal governs how new assignments are formed; it does not automatically authorize retargeting existing waiting traffic. The old arithmetic remains valid for that conditional case, but should not define the normal new-allocation architecture or force the earlier binary question.

Queue-based preference can remain the selected driver model, while physical feasibility constrains what can be transferred. This does not require a new service-aware queue-clearing cost. The [existing backbone](../../../../context_snapshots/diff_minimal_meso/src/diff_minimal_meso/simulation.py#L279) already computes sending/receiving limits before its node-flow calculation; the refined allocator should likewise use the relevant known limits consistently.

**Status:** feedback 9 is answered and capability-aware allocation is the agreed direction. The exact coupled transcription is not claimed complete. Unified methodology drafting remains unfinished; no next-step work or new question is opened in this response, as requested.
