# Urban methodology review: questions, evidence and conclusions

**Latest update, 28 October: clean colleague-facing reports are ready for review.** Red tints and reader-irrelevant implementation/review scaffolding are removed. Scientific explanations, provenance, equation bodies and numbering remain unchanged. The [current guide](unified_methodology_draft.md) links the separate clean copies; earlier versions are preserved. This is an editorial completion, not a new scientific question or implementation task.

**Latest update, 28 October:** feedback 11 applies the first report-improvement batch, including the parallel approach geometry, causal equation introductions and colleague-facing prose. The current topic is report review. The VSL section order remains; [structural alternatives](report_structure_options.md) are proposals only. The earlier discussion history below is retained; the [current reading guide](unified_methodology_draft.md) and [decision record](review_decisions.md) define the latest status.

Updated 27 October 2026. This is an independent scientific review. The A–F implementation phases and component checkpoints do not organize its discussion or documents.

A left-turn bay can have room while through traffic prevents a turner from reaching it. Extra left-turn service may then help less than through service that removes the obstruction. The review asks what traffic information and laws are needed to explain that difference, and whether their sensitivities support better service decisions.

The established urban task supplies the research questions and comparison design. The VSL report supplies a standard of completeness and explanation: a reader can reconstruct the admitted traffic, selected laws, comparisons and conditional sensitivity without inventing a missing traffic rule. It does not supply urban traffic assumptions or prove useful gradients.

[First unified technical draft and current reading guide](unified_methodology_draft.md)

[Agreed current-ready-head receiving rule](receiving_priority_timing.md)

[Feedback 9: capability-aware allocation, answered](../../reporting/research_readiness/urban_feedback9_response.md)

[History refinement deferred by the timestep-scope clarification](service_history_consistency.md)

[Accepted drafting syllabus](methodology_draft_next_work.md)

[Agreed rival-selection policy](../../reporting/research_readiness/urban_feedback8_response.md)

[B1/B2 candidates retained for later concrete selection](aggregate_rival_questions.md)

[Closed lane-allocation, access, storage and service discussion](coupled_lane_access_and_service_discussion.md)

[Closed principles batch: comparison, sensitivity and scientific credit](comparison_sensitivity_and_credit_proposal.md)

[Agreed traffic principles](traffic_principles.md)

[Current conclusions and open choices](review_decisions.md)

[Feedback 5: stronger aggregate information and a local explanation of sensitivity](../../reporting/research_readiness/urban_feedback5_response.md)

**Current topic: consolidated methodology ready for review.** The user closes the questions and authorizes applying the agreements. The report now removes frozen waiting state, preserves movement-specific processing and implements occupied-lane access explicitly. The full conditional sensitivity is updated. Numerical/native-model qualification and scientific experiments remain later; no implementation is started.

[Consolidated report and source map](unified_methodology_draft.md)

[Feedback 10 answer and statuses](../../reporting/research_readiness/urban_feedback10_response.md)

[Report and explicit review points](unified_methodology_draft.md)

## The logical topics

| Topic | Scientific question | Current position |
|---|---|---|
| **1. Traffic world** | What traffic is present, how did its queues arise, and when is it eligible to reach service? | Assumptions settled, including loading from empty. Joined physical ownership, propagation and eligibility still need coherent transcription. |
| **2. Traffic behavior** | How do intended lanes, reachable bay access, finite storage, service and order determine who moves? | Behavioral choices closed after the amendment: progressive per-packet balancing in source order, movement grid with retained route identity, elapsed-rate service and receiving reuse. Joined transcription remains later work. |
| **3. Fair comparison** | What can the simpler models legitimately know and explain, and what would count as added value from order? | Policy discussion closed by the user; A/A working preferences, exact rivals and reference/evaluator mappings remain later definition. Original-series macro conversion, native subsets and observation updates remain allowed. |
| **4. Complete sensitivity** | How does a service change affect every released unit's time through final clearance? | Agreed: derive one-step discharge/next-state responses first and compose their effects into complete TST. Actual laws, derivative regularity and horizon/endpoint treatment remain open. |
| **5. Explanation and scientific credit** | Can a reader follow the traffic argument and identify what was borrowed, adapted or defined here? | Both adjacent causal/source explanation and a complete supporting source map are agreed. Exact credit follows the selected laws. |

These are logical categories, not successive approval stages. Categories 1–2 are discussed together because the traffic world and behavior constrain each other. The user-selected approach remains to settle overall assumptions before details that depend on them, and to discuss principles before filling in concrete model choices. This is a way to make the scientific argument understandable, not a requirement to process every question through an implementation pipeline.

The topics inform one another. A rival's selected equations may expose a missing fairness assumption. A derivative may reveal a missing access rule. Such findings belong with the affected scientific question and its recorded decision. Questions may be revisited when evidence requires it; unrelated settled decisions stay settled. Source work accompanies each law rather than waiting for a final reporting step.

## What is agreed and what remains open

All planned broad discussion batches are closed. The four traffic directions remain: load from empty; responsive desired allocation followed by physical access; effective average service; exact incoming/realized lane order without deliberate mixing. Logical assignment may finish while mass waits upstream. Pending records count that physical mass once, with no extra storage or early eligibility. Valid commitments stay fixed; retargeting is deferred.

No further broad vote is needed. The [decision record](review_decisions.md) records feedback 9 and its limits. The [inventory](../../extraction/research_readiness/urban_open_question_register.md) retains fifteen IDs and thirty-four high-level candidate paragraphs, now qualifying new allocation by known feasibility. Exact coupled transcription remains later work. The user asks to answer feedback 9 only and not continue; no new question or next step is opened. Later reports keep the step/completion/action status brief, and full PDF review waits until finished.

The closed concrete packet retains eleven named directions including `A.joint`, explicitly one packet's lane amounts within source-order processing. Frozen observations and the extra target-order/partial-admission questions are withdrawn. Ideal equality is as feasible without moving old traffic; imperfect preferences are deferred. The new comparison discussion retains all fifteen IDs and thirty-four high-level candidates. It changes no permissions, commitments or traffic-order policy.

The [original-series clarification](../../reporting/research_readiness/urban_macro_time_series_clarification.md) refines that same comparison candidate. Fine-grained source data may be converted into macro state by the model itself, and successful reconstruction is a valid result. Observation schedules distinguish the tested predictive task; forecasting without later updates is not a mandatory comparison protocol. No candidate or principle checkpoint is added.

V0–V4, four-group effective-service action, complete total system time, continuous mass, fixed routes/permissions, conservative physical storage and the accepted comparison/evidence obligations remain the foundation. A claim of useful sensitivity requires richer-evaluator evidence; an internally correct derivative or decreasing objective is insufficient. External perturbation evidence before full optimization remains an accepted scientific requirement, independent of document organization.

## How the review builds a complete explanation

Each topic should explain the traffic problem, meaningful alternatives, decisive evidence and current conclusion in connected prose, using a common example when helpful. There is no mandatory section template. Keep the detailed source, interface and derivation records where they help check an argument, rather than making procedural fields carry it.

The overall model must eventually account for reachable access, service, residual order, storage and upstream effects together. A comparison needs specified rival laws and their lawful observations. A derivative needs those selected laws and complete clearance accounting. These are actual scientific dependencies. They do not create separate component-acceptance or plan-freezing steps for the review.

Check the combined explanation as it becomes concrete: one physical mass account, compatible clocks, feasible resources, appropriate neutral/symmetry behavior, fair information and accurate source credit. The compact report should present that joined argument. Its provisional 4–6-page budget is a writing aid, not a scientific gate. Numerical correctness, calibration and demonstrated control usefulness remain distinct later evidence tasks.

[Supporting completeness criteria and topic map](../../extraction/research_readiness/urban_review_completion_and_work_map.md)

[Why the questions follow from the VSL standard](../../reporting/research_readiness/urban_vsl_standard_gap_explainer.md)

[Discussion record and the 26 October clarification](review_dialogue.md)

[Recovered authorities](../../extraction/research_readiness/urban_authority_and_gap_audit.md)

Simulator development, installations, traffic/gradient/optimization/SUMO runs and V5/I1 remain outside this review assignment. The implementation workflow continues to govern project implementation when separately opened.
