# When would retaining order make a service recommendation more credible?

Prepared 23 October 2026; updated after feedback 5 and its clarification. **Closed by the user on 26 October 2026:** “Comparison, sensitivity and scientific credit: agreement on principles.” This document records those agreed principles and their remaining concrete questions. Q1–Q4 remain settled.

[Newly opened concrete traffic-model discussion](coupled_lane_access_and_service_discussion.md)

[Feedback 5: response, qualifications and mathematical explanation](../../reporting/research_readiness/urban_feedback5_response.md)

A left-turn bay has room, but through traffic may obstruct its entrance. An order-aware model might recommend extra through service to release the turners. Before calling that recommendation an improvement, we need to know whether a simpler model could already explain the obstruction, whether the gradient counts the later consequences, and which traffic rules support the explanation. These are the next three discussion topics.

We carry forward loading from empty, responsive desired allocation, average service and exact incoming/realized lane order without deliberate local mixing. Valid waiting-lane commitments remain fixed by default. Q2 and Q4 do not block this discussion and need no further principle vote. Their concrete allocation/access/service laws will be proposed later.

[Settled traffic principles and their specification limits](review_decisions.md)

## What is missing from the established review?

The old review already specifies a good experiment. The intended VSL-like standard additionally lets the reader reconstruct what each predictor knows, what its sensitivity includes and where its defining rules come from. The gaps below concern that definition, rather than new evidence of a performance advantage.

| Topic | Established urban review | Definition still needed, and why it affects the method |
|---|---|---|
| Fair comparison | Baseline roles, shared tasks and aggregate-matched order pairs | The actual observations and histories available to each rival. Matching current totals does not establish that a rival cannot distinguish the pair; its history may reveal the difference. |
| Complete sensitivity | Complete total system time and a general derivative chain | The selected laws' response through later admission, spillback, source waiting and clearance. A derivative of an incomplete time account can favor a different allocation. |
| Explanation and credit | Literature anchors and adoption classes | The exact borrowed law, adaptation or project-defined rule beside each model component. A citation to a family of models cannot supply an unspecified access law or justify its derivative. |

The strongest direct comparisons are concrete. VSL explicitly permits history-based inference, whereas urban still needs its principal movement-queue and lane/storage realizations. VSL derives sensitivities of its selected service law, whereas urban's access operator is still schematic. VSL separates borrowed ingredients from study-defined terms beside an equation, whereas urban's adoption map still calls for that equation-level record. These differences explain the work needed; they do not require importing VSL's assumptions or methods.

[Direct evidence and decision scope](../../extraction/research_readiness/urban_categories345_evidence_notes.md)

## What can the simpler models legitimately know?

The user chooses a limit-based comparison principle in feedback 5 and clarifies its data boundary: rivals may access the original series and apply their own declared conversion into macro state. The source's fine resolution does not determine the receiving model's resolution. Allow physically defined lane/bay masses, queue measures, speeds and model-derived aggregate effects; native rivals may use subsets. The model's conversion, retained state/memory, resolution and observation schedule need explaining.

**Candidate A — judge each comparison against the rival's actual information.** Give every rival its declared, source-faithful observations and history inference. Establish which pairs it really sees identically, and compare its predictions with the order-aware model and richer references. A pair may be informative against one rival and distinguishable by another. This supports strong comparisons, but the conclusion must explain which representation or information difference it has isolated.

**Candidate B — seek one pair that every simpler rival sees identically.** Keep all their permitted observations and histories equal while varying the relevant order/access detail. If such a physically realizable pair exists and richer traffic responds differently, it gives a particularly clear information test. With strong history-aware rivals, constructing it may be difficult or impossible. Restricting their legitimate inputs merely to obtain it would undermine the test.

**Candidate C — use a common maximum aggregate information boundary (agreed).** Permit original fine-grained time-series access through each model's declared macro aggregation or state estimator. The retained representation and its dynamics determine what the model preserves; do not force one fixed projection before the model applies its own method. Successful aggregate reconstruction or estimation is admissible and weakens the need for full packet-order retention in that regime. Native models may use subsets. Failure of a few chosen models is not a proof that every admitted macro representation fails.

C is the organizing principle. A describes concrete comparisons; B is a possible information-limit witness for a declared retained record. If identical records correspond to reference responses differing by more than twice the allowed absolute error, a predictor of only that record cannot meet the margin for both. Equality under one projection does not establish that condition for every model-defined conversion of the original series. We have not constructed a universal witness. Successful reconstruction must count rather than be prohibited.

Responsive lane allocation adds a related distinction. Match the exogenous traffic, geometry, permissions and declared behavioral assumptions where they are shared. Do not force equal realized allocation shares or lane occupancy when those are outputs of the dynamics being tested. Nor should a simpler rival receive B3's exact lane/admission ledger as an extra input. Its own allocation capability must be represented faithfully.

A one-step replay, macro-state updates from an observation series, and prediction without later updates are all legitimate setups. Describe the data schedule and the capability each test measures; running without updates is not a general requirement for an admissible macro rival. For a counterfactual allocation, distinguish observations supplied to the model from outcomes it predicts and state what is held fixed in the response calculation. Aggregate blockage capability already exists; its exact order-sensitive and useful-gradient sufficiency remains the test. B3 itself is not ground truth.

This principle preserves the accepted baseline ladder: homogeneous macro, movement queues, lane/storage aggregate, and selective order. A simpler model explaining the bay effect is a valid sufficiency result. Every comparison still uses the same physical service action, population and complete objective. Independent ordered references remain forward checks; the richer evaluator needs one common service-realization mapping. External perturbation evidence still precedes full optimization, and optimizer comparisons remain a separate question.

The agreed principle is **UR-G4**. Each model's actual conversion/retained memory, observation schedule and error margin, principal B1/B2 laws, matched cases and reference/evaluator realizations remain concrete questions, **UR-C4-Q1/Q2 and UR-C6-Q1**. Source-faithful subset-using rivals remain valid. Retaining an ordered ledger inside a preprocessor must be disclosed; transient fine-data access and a successful macro summary are allowed.

## How does one step's service response become complete TST sensitivity?

Feedback 5 agrees the local-first approach. Start with a fixed beginning-of-step state: how does a feasible reallocation of service change current discharge and the next state? A reachable queue may use more service fully; an inaccessible bay or binding downstream receiving may make the immediate response zero. A larger service share for one group is compensated elsewhere in the fixed budget. Absolute cycle length remains outside the task.

Next ask how a changed previous-step state affects the present response. Extra through service may remove obstruction, change later bay access and alter upstream/source waiting. Composing the local state responses gives the complete TST derivative for the fixed allocation. This is a sequence of whole-system states, without requiring packet-path differentiation. Summing local discharge slopes while resetting future states would miss the main causal effect.

The current TST charge uses beginning-of-step source plus network mass under the inherited left-interval convention. Its direct control partial can therefore be zero with the starting state fixed, even though discharge and the next state respond. Later time charges carry the effect. Discharge/queue/state sensitivities explain the local mechanism; complete TST remains the primary control objective.

The following candidates concern the complete time account. They are compatible with the agreed local-to-system principle, rather than competing explanations of it.

**Candidate A — use one horizon long enough for complete clearance.** Continue every compared trajectory to a common end time, with an empty system contributing zero afterward. This works with the existing fixed-step calculation and avoids making a changing stopping counter part of the derivative. It is valid only in a neighborhood where the base allocation and relevant feasible perturbations all clear before that horizon. A long horizon by itself does not establish that condition.

**Candidate B — evaluate to each trajectory's completion and derive the response consistently.** Account for the complete trip times, or an equivalent event-based calculation, without storing an unnecessary empty tail. This can describe the same objective as A. Its difficulty is handling changes in completion time and active traffic events; automatic differentiation through an integer stopping decision is not sufficient.

The earlier recommendation of **A wherever its clearance condition holds** remains conditional. Feedback 5 selects neither horizon treatment. Nonclearing runs remain failed/censored, with remaining traffic reported rather than given a silently truncated low cost. No positive mass cutoff is introduced.

The existing D2 default keeps the candidate allocation constant during the control/inflow window, then uses a common fixed clearance policy. I read that fixed continuation as independent of the candidate allocation: the candidate no longer changes clearance service directly, but it changes the traffic state entering clearance. That effect must continue through the calculation. Extending the candidate allocation throughout clearance would change the duration of the intervention and must be stated explicitly rather than slipped into a stopping rule. D2 retains its default status; the numerical clearance policy and cap remain to be instantiated later.

The local laws must carry continuous responses through allocation shares, admissions/discharges, residual order, storage and receiving. Fixed labels do not freeze these responses; preparation remains independent of the candidate allocation. The mathematical companion distinguishes the current direct response, the response inherited from last step and the complete fixed-allocation response.

[Local-to-system sensitivity and the aggregate-information limit](../../reporting/research_readiness/urban_feedback5_information_and_sensitivity.pdf)

This is a conditional local sensitivity: the active constraints and ordered traffic fronts must support the stated derivative. Their changes remain visible in forward reporting and require separate boundary treatment. A correct internal derivative and a direction that helps richer traffic remain distinct claims. Neither average service nor responsive allocation guarantees either one.

The local-to-system principle **UR-G5** is agreed. Exact selected-law responses, **UR-C5-Q1**, still need deriving, and the numerical horizon/endpoint treatment remains open. These do not require another broad sensitivity-principle vote now.

## How should the report make its scientific origin clear?

Suppose a published model motivates lane preferences, while this study adds a rule for how assigned mass waits upstream and reaches a short bay. The reader needs to see where the borrowed idea ends and the added traffic assumption begins. Otherwise a source citation can give an unselected or newly constructed rule an appearance of established authority.

**Candidate A — maintain a complete equation/source map.** For every defining law, record the exact source and location, what was retained or adapted, and what was defined or derived here. This makes missing credit and missing laws easy to find, but a separate map alone does not explain the traffic mechanism to the reader.

**Candidate B — explain source and adaptation beside each component.** Introduce what the rule is trying to represent, how it changes the traffic, and which part comes from prior work. This makes the main report understandable, but scattered explanations need a consolidated index to show complete coverage.

The user agrees to **using both: contextual explanation in the report, backed by one complete source map**. They serve different reading needs and are compatible. Label the complete model as a documented composition of ingredients, without implying that a single paper supplies it or that project ownership alone proves novelty. A project-defined rule still needs a traffic justification and later validation.

This presentation approach is agreed under **UR-C7-Q1**. Exact source/adaptation records still follow the selected laws. The VSL report remains an explanatory example; presentation agreement supplies no missing traffic rule.

## Agreed principles and remaining concrete questions

| Topic | Agreed principle | What remains to specify or establish |
|---|---|---|
| Fair comparison | Original time-series access through declared model-defined macro conversion; individual native rivals may use subsets and successful macro reconstruction counts. | Actual conversion/retained representation, observation schedule, margins, rival capabilities/cases, independent references and common external intervention. |
| Complete sensitivity | One-step discharge/next-state response first; compose those effects over time into complete TST sensitivity. | Selected-law derivatives, regularity, numerical horizon/endpoint treatment and checks, richer-evaluator usefulness. |
| Explanation and credit | Adjacent causal/source explanation plus one complete source map. | Exact equation-level sources and derivations once the laws are selected. |

Feedback 5 settles these principles, with the qualifications explained in the response. The examples are conceptual, not executed fixtures or evidence that the order-aware model wins.

Relate these agreed principles to Q1–Q4 as the traffic model, rivals and sensitivity become concrete. A derivative needs its law; an information-limit claim needs its complete observation definition and evidence. These scientific dependencies do not create implementation phases or component-closure gates. Revisit a settled principle only for a genuine conflict or materially different traffic assumption. Simulator implementation and numerical experiments remain separate work.

[Full question inventory and ownership](../../extraction/research_readiness/urban_open_question_register.md)

[Original preparation record and document checks, 23 October](../../reporting/research_readiness/urban_categories345_work_report.md)

[Current topic guide](review_plan.md)
