# Why these urban questions follow from the VSL standard

Originally prepared 20 October 2026; topic organization clarified 26 October. Explanatory companion to the review proposals; the gap assessment itself does not select a model.

The principles batch is closed and the [concrete traffic discussion](../../temp_content/research_readiness/coupled_lane_access_and_service_discussion.md) is open. [Feedback 6](urban_feedback6_response.md) selects internal geometry, queue-based choice, elapsed-rate service and receiving reuse, and removes the artificial target-order choice for a homogeneous joint split. This narrows the selected-law gaps below; exact dynamic coupling still remains. [Source/assumption notes](../../extraction/research_readiness/urban_coupled_model_source_and_assumption_notes.md) distinguish inherited physics, selected directions, project-defined prototypes and unfinished laws.

[The feedback-7 amendment](urban_feedback7_amendment_response.md) withdraws frozen observations and selects source-order progressive per-packet balancing. It resolves the last question in this batch; route identity and lane-order distinctions remain. The broader completion criteria below do not authorize starting a next batch or construction pass.

**Current conclusion after feedback 8:** the traffic-behavior batch is closed, and [rival selection](urban_feedback8_response.md) now has an agreed policy rather than an unresolved principle-level family choice. A/A are working preferences; exact model states/laws/adaptations remain later definition. This does not complete the concrete comparison gap below or authorize a next set. Information access and prior traffic choices stay fixed.

The user subsequently closes that final broad discussion batch. [The next-work recommendation](../../temp_content/research_readiness/methodology_draft_next_work.md) concerns writing and checking the actual joined laws, sensitivity and comparison/reference definitions before the compact report. The completeness gaps below therefore guide formulation work; they do not require another generic questionnaire.

The [current review plan](../../temp_content/research_readiness/review_plan.md) and [first traffic proposal](../../temp_content/research_readiness/traffic_principles.md) apply feedback 2: short causal explanations and conceptual candidates replace the mandatory question template. The category mapping below remains the explanation of why the questions are needed. The [feedback-1 response](urban_feedback1_category_first_discussion.md) records the earlier agreement on category-led discussion.

The [feedback-3 response](urban_feedback3_response.md) records the later loading-from-empty decision, updated responsive-allocation recommendation and corrections about gradients, defragmentation and lane order. The VSL/urban comparison below remains a source-backed explanation of the gaps; current choices and pending interpretations are maintained in the live decision record.

[Feedback 4](urban_feedback4_response.md) settles average service and separates logical upstream assignment from physical zone entry. All four broad principles are now settled for the present stage, with established commitment retained by default and provisional retargeting deferred. The concrete coupled laws remain to be proposed. This distinction does not weaken the eventual goal of a reconstructible model.

The [comparison, sensitivity and credit record](../../temp_content/research_readiness/comparison_sensitivity_and_credit_proposal.md) now incorporates feedback 5: the maximum aggregate information boundary, local-to-system sensitivity and both credit approaches are agreed. Their concrete definitions and selected laws remain open. The [feedback 5 response](urban_feedback5_response.md) distinguishes principle agreement from the remaining specification gaps. Earlier [source comparisons](../../extraction/research_readiness/urban_categories345_evidence_notes.md) remain supporting evidence, with their old recommendations superseded where noted.

The old urban review established **what to test and how to interpret the result**: allocate four effective-service fractions, count complete total system time (TST), and use V0–V4 to separate order, storage, accessibility and robustness. The VSL refinement went further in specifying **the model that generates the outcomes**: its traffic world, selected laws, comparison information and complete conditional sensitivity are stated together and presented with clear scientific credit.

The two anchors do different jobs. The research questions determine which traffic distinctions the urban study needs. The VSL standard determines how completely and clearly those distinctions must be formulated. The proposed questions connect them: they close the missing definitions needed to turn the accepted urban experiment into a reconstructible methodology.

Some work is consolidation and explanation. Some requires a traffic-law decision before an explanation can be complete. The comparison below concerns specification and presentation; it makes no claim that either branch has already demonstrated numerical or empirical gradient usefulness.

## The five logical gaps and their questions

| Logical category | Property demonstrated by the VSL formulation | Urban questions that supply that property | Completion criteria |
|---|---|---|---|
| **1. One coherent traffic world** | The initial population, admitted states, physical accounts and component clocks fit together | **UR-G1, UR-G2, UR-C1-Q1** | U2, U4, U5 |
| **2. Rules that determine traffic evolution** | Fixed state and parameters determine access, service and the next state through selected laws | **UR-G3, UR-G3-Q1, UR-C2-Q1, UR-C3-Q1** | U3, U4 |
| **3. A concrete, fair comparison** | The predictors, their available information and the meaning of their comparison are explicit | **UR-G4, UR-C4-Q1, UR-C4-Q2, UR-C6-Q1** | U7 |
| **4. The sensitivity of that complete model** | Local derivatives follow the selected laws through every relevant feedback to complete TST | **UR-G5, UR-C5-Q1** | U5, U8 |
| **5. An understandable and attributable explanation** | The reader can follow the causal model and distinguish borrowed, adapted and study-defined equations | **UR-C7-Q1**; exposition applies across all questions | U6, U10 |

This gives every substantive question one primary home. Some dependencies cross categories: UR-G2's service clock constrains category 2, and the forward laws constrain category 4. **UR-G0** defines the completion standard for the whole table. **U1**, the concrete task, is largely established already. **U9**, the whole-model consistency check, asks whether all five explanations agree as the model becomes concrete; it is not another traffic component or approval stage.

UR-G3-Q1 was made explicit after feedback 3 and refined after feedback 4. Logical assignment may complete before physical entry; waiting-target commitment is a separate choice, while actual common-queue or independent-path admission follows the selected access law. The original 14 IDs remain intact, with this one shared subquestion retained.

These categories explain **why the work is needed**. The supporting question map records which scientific topics share an assumption and what evidence each needs. It does not impose the implementation Type 1/Type 2 closure procedure or a discussion pipeline. The older A/R/N/E annotations distinguish accepted material, recoverable evidence, a new scientific decision and later execution evidence; they describe the source of an answer rather than its place in an approval sequence. Stable question IDs remain useful for traceability.

## The strongest evidence for each gap

**1. One coherent traffic world: the parts must describe the same traffic.**

VSL's task statement fixes the initial lane population, common footprint, empty terminal/history and absence of later arrivals. Its five global assumption groups explain how the preparation region, terminal, point service and recovery history connect. Its accepted assumption audit explicitly checks their compatibility within the stated operating domain.

Urban already fixes continuous mass, structural routes, per-lane order and complete accounting. M2 also supplies useful physical partition and eligibility contracts. The remaining gap is their completion for the shared-lane/bay model: the accepted impact record explicitly leaves lane intent, realized access, storage, ordered service **and their update order** for later definition. Consequently, a full urban specification still needs to establish which initial histories are admissible and when a discharge can affect subsequent admission/receiving. This explains UR-G1/G2 and the propagation transcription in C1; it does not reopen the established continuous-mass backbone.

For initialization, the standard requires a declared start for the scenarios actually used. It does not require a general nonempty-state initializer: VSL itself specifies a restricted initial family. M1 deferred direct nonempty physical-link initialization, while urban V4 names initial-queue variation. Loading from an empty physical network may supply those queues. The review should first connect that construction to the required cases, adding direct prescribed starts only if a demonstrated need remains. Otherwise a general initialization extension would be unnecessary scope. The [first traffic question](../../temp_content/research_readiness/traffic_principles.md) explains how traffic location/readiness and a fixed control-start state affect the service comparison.

Evidence comparison:

[VSL concrete task and global assumptions, §2](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L44)

[VSL accepted compatibility audit](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_global_assumptions_findings_and_checkpoint.md)

[Urban accepted handoff of the coupled bay rules, P4](../../synthesis/project_impact_matrix.md#L19)

**2. Rules that determine evolution: a dependency is not yet a traffic law.**

VSL's forced-merging section defines a concrete service-work function, a condition ensuring the relevant root is unique, and a table selecting service for the free/queued combinations. A reader can determine the modeled service once the admitted state and parameters are supplied.

Urban's formal V2 section explicitly calls its receiving/admission equations schematic. V3 then names an ordered-access operator and lists its inputs, without defining the access law. P8 separately confirms that exact FIFO versus within-bin relaxation remains a modeling choice. Naming those dependencies therefore does not determine admitted or discharged mass.

For a concrete example, a bay with four vacant vehicle-equivalent places may still be inaccessible to a turner behind through traffic. The stored totals establish room; they do not establish reachability. The model needs the rule that decides whether the turner can reach the opening, how service removes the obstruction, and which ordered mass remains. UR-G3 settles the retained-order/method contract; C2 and C3 supply the access and coupled service/state laws. **This is the most direct evidence that the remaining work includes methodology, beyond rewriting the report.** Numerical calibration cannot choose that rule implicitly.

Evidence comparison:

[VSL concrete service law and branch table, §3.3](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L161)

[Urban schematic receiving and ordered access, §6](../../synthesis/experiment_formulation_formal.tex#L156)

[Accepted P8 qualification of production FIFO](../../synthesis/project_impact_matrix.md#L33)

**3. A concrete, fair comparison: the rival must be defined before its limitation is claimed.**

VSL states what the aggregate-information and lane-resolved predictors know, permits inference from admitted histories, and gives a compact peer that reconstructs the same initial state and dynamics from one additional statistic. It also separates the information comparison from the equal-information optimizer comparison.

Urban already accepts a strong baseline ladder and fairness rules. Feedback 5 and its clarification allow original time-series access through each rival's declared macro conversion or estimator, rather than forcing one fixed aggregation before model access. Native B1/B2 models may use subsets, but their failure alone does not establish an information limit. An indistinguishability claim depends on the complete retained record for the representation being tested; equality under one projection does not rule out another legitimate macro summary. C4 still makes the rivals and their observation schedules concrete, without weakening them or forcing their dynamics to match B3.

C6 adds an urban-specific consequence: its accepted external tests require independent references and one common effective-service-to-evaluator mapping. This is how the common-intervention standard applies to urban. It is not a claim that VSL has already supplied an urban-style SUMO mapping.

Evidence comparison:

[VSL predictor information and compact peer, §4](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L260)

[Urban principal B1/B2 choices still required](../../synthesis/literature_adoption_matrix.md#L34)

[Urban common external intervention obligation, P10](../../synthesis/project_impact_matrix.md#L25)

**4. Complete sensitivity: differentiate the actual selected model.**

VSL shows the derivative of its particular service root, tracks the influence of recovery history and changing events, and connects corrected departures to complete TST. These terms correspond to laws already defined in that model.

Urban's general state-sensitivity recursion and variant-specific causal paths are sound and useful. Feedback 5 clarifies the explanation: begin with current discharge/next-state response at one step, then compose those state effects into complete TST. An undefined access/receiving law still has no local derivative to insert into that calculation. G5's causal principle is agreed; C5 supplies actual selected-law responses and the time account, with the numerical horizon/endpoint choice still open. The required property is model-specific completeness. Urban need not adopt VSL's event formulas or history construction.

Evidence comparison:

[VSL service, history/event and complete-objective sensitivity, §5](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L270)

[Urban general recursion and its stated purpose, §5](../../synthesis/experiment_formulation_formal.tex#L109)

[Urban record explicitly identifying unresolved access equations/Jacobians](../../synthesis/project_impact_matrix.md#L37)

**5. Understandable attribution: show what the equations mean and whose work they contain.**

VSL introduces the traffic mechanism before the formulas. Beside its pre-choke transfer equation, for example, it credits the conservative-source and receiving/priority ingredients while identifying the particular minimum and interaction length as defined in the study. Its coverage map tracks that distinction equation by equation.

Urban already has an adoption vocabulary and a useful component/source matrix. Feedback 5 agrees both adjacent causal/source explanation and a complete source map. Exact credit beside each **selected defining equation** still requires the actual law and source or derivation. An unselected access rule cannot yet receive accurate equation-level credit. C7 therefore accompanies model discussion; some of this gap is editorial, while the missing-law portion depends on category 2.

Evidence comparison:

[VSL adjacent source/adaptation credit, §3.1](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.tex#L121)

[VSL equation-by-equation coverage map](../../../differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_compact_report_source_and_coverage_map.md)

[Urban existing adoption classes and required evidence](../../synthesis/literature_adoption_matrix.md#L18)

## How the topics form one scientific explanation

The selected overall-assumptions-first approach keeps the traffic world and shared meanings visible while discussing concrete mechanisms. A claim about a rival needs its laws and lawful observations; a derivative needs the actual traffic response; source credit accompanies each selected rule. These dependencies connect the topics without turning them into consecutive phases. The report brings the resulting coherent explanation together.

Thus the old review's task, action, objective, variants and evidence hierarchy remain the foundation. The main advance is to supply a complete, coherent and attributable model for that experiment, then explain it at the standard demonstrated by VSL. Extra empirical evidence, VSL-specific assumptions or a different urban research question are not prerequisites for this explanatory step.

[Live detailed question register](../../extraction/research_readiness/urban_open_question_register.md)

[Completeness criteria and topic guide](../../temp_content/research_readiness/review_plan.md)
