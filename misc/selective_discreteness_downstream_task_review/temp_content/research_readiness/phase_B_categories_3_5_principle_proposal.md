> Historical review record. The implementation-phase framing is retired following the user clarification of 26 October 2026. Current material: [comparison_sensitivity_and_credit_proposal.md](comparison_sensitivity_and_credit_proposal.md).

# When would retaining order make a service recommendation more credible?

23 October 2026. Phase B discussion proposal for logical categories 3–5. Recommendations below are provisional. The four traffic principles from the preceding discussion remain settled for the present stage.

A left-turn bay has room, but through traffic may obstruct its entrance. An order-aware model might recommend extra through service to release the turners. Before calling that recommendation an improvement, we need to know whether a simpler model could already explain the obstruction, whether the gradient counts the later consequences, and which traffic rules support the explanation. These are the next three discussion topics.

We carry forward loading from empty, responsive desired allocation, average service and exact incoming/realized lane order without deliberate local mixing. Valid waiting-lane commitments remain fixed by default. Q2 and Q4 do not block this discussion and need no further principle vote. Their concrete allocation/access/service laws will be proposed later.

[Settled traffic principles and their specification limits](phase_B_revision.md)

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

Consider two queues with the same left/through totals but different order. If they were formed by different movement-specific arrival histories, a turn-queue model observing those histories may distinguish them. Equal totals alone would therefore be insufficient evidence that exact order supplied otherwise unavailable information. Loading from empty makes this check especially relevant: the preparation history may contain part of the information we intended to vary.

**Candidate A — judge each comparison against the rival's actual information.** Give every rival its declared, source-faithful observations and history inference. Establish which pairs it really sees identically, and compare its predictions with the order-aware model and richer references. A pair may be informative against one rival and distinguishable by another. This supports strong comparisons, but the conclusion must explain which representation or information difference it has isolated.

**Candidate B — seek one pair that every simpler rival sees identically.** Keep all their permitted observations and histories equal while varying the relevant order/access detail. If such a physically realizable pair exists and richer traffic responds differently, it gives a particularly clear information test. With strong history-aware rivals, constructing it may be difficult or impossible. Restricting their legitimate inputs merely to obtain it would undermine the test.

I recommend **A as the general contract, with B as a stronger diagnostic where available**. Failure to find a universal pair would limit the information claim; it would not automatically end the broader comparison of traffic predictions and useful service directions. If a rival's lawful history reconstructs the relevant order, acknowledge that fact and examine what its dynamics preserve or use. Do not claim hidden information merely because its current state is aggregate.

Responsive lane allocation adds a related distinction. Match the exogenous traffic, geometry, permissions and declared behavioral assumptions where they are shared. Do not force equal realized allocation shares or lane occupancy when those are outputs of the dynamics being tested. Nor should a simpler rival receive B3's exact lane/admission ledger as an extra input. Its own allocation capability must be represented faithfully.

This principle preserves the accepted baseline ladder: homogeneous macro, movement queues, lane/storage aggregate, and selective order. A simpler model explaining the bay effect is a valid sufficiency result. Every comparison still uses the same physical service action, population and complete objective. Independent ordered references remain forward checks; the richer evaluator needs one common service-realization mapping. External perturbation evidence still precedes full optimization, and optimizer comparisons remain a separate question.

The decision here is the information/fairness principle, **UR-G4**. Choosing the principal B1/B2 equations, proving that a particular pair is matched, and specifying the independent/evaluator realizations remain later component work, **UR-C4-Q1/Q2 and UR-C6-Q1**. No baseline is selected by this recommendation.

## Does the sensitivity count the consequences after control ends?

More service can empty a bay earlier, admit upstream traffic sooner and reduce source waiting later. Stopping the time account when demand release ends could miss much of that benefit. Conversely, keeping traffic outside the modeled network must not make a plan look good. The accepted objective already counts every released unit through completion; the remaining issue is how the derivative preserves that meaning.

**Candidate A — use one horizon long enough for complete clearance.** Continue every compared trajectory to a common end time, with an empty system contributing zero afterward. This works with the existing fixed-step calculation and avoids making a changing stopping counter part of the derivative. It is valid only in a neighborhood where the base allocation and relevant feasible perturbations all clear before that horizon. A long horizon by itself does not establish that condition.

**Candidate B — evaluate to each trajectory's completion and derive the response consistently.** Account for the complete trip times, or an equivalent event-based calculation, without storing an unnecessary empty tail. This can describe the same objective as A. Its difficulty is handling changes in completion time and active traffic events; automatic differentiation through an integer stopping decision is not sufficient.

I recommend **A wherever its clearance condition holds**, retaining B for a demonstrated need rather than opening a second calculation now. Nonclearing runs remain failed/censored evaluations, with their remaining traffic reported. They cannot be ranked using a silently truncated low cost. No small positive mass cutoff is introduced by this proposal.

The existing D2 default keeps the candidate allocation constant during the control/inflow window, then uses a common fixed clearance policy. I read that fixed continuation as independent of the candidate allocation: the candidate no longer changes clearance service directly, but it changes the traffic state entering clearance. That effect must continue through the calculation. Extending the candidate allocation throughout clearance would change the duration of the intervention and must be stated explicitly rather than slipped into a stopping rule. D2 retains its default status; the numerical clearance policy and cap remain to be instantiated later.

The required causal explanation follows service through responsive continuous allocation shares, admitted and discharged mass, residual lane order, storage, upstream receiving and every unit of source/network time. Fixed route/lane labels do not mean freezing these continuous responses. The preparation remains independent of the candidate allocation as already agreed.

This is a conditional local sensitivity: the active constraints and ordered traffic fronts must support the stated derivative. Their changes remain visible in forward reporting and require separate boundary treatment. A correct internal derivative and a direction that helps richer traffic remain distinct claims. Neither average service nor responsive allocation guarantees either one.

The decision here is the complete-response principle and conditional horizon treatment, **UR-G5**. The actual derivative of the coupled traffic laws, **UR-C5-Q1**, follows their specification. Accepting this principle would not complete the still-missing access/service derivatives.

## How should the report make its scientific origin clear?

Suppose a published model motivates lane preferences, while this study adds a rule for how assigned mass waits upstream and reaches a short bay. The reader needs to see where the borrowed idea ends and the added traffic assumption begins. Otherwise a source citation can give an unselected or newly constructed rule an appearance of established authority.

**Candidate A — maintain a complete equation/source map.** For every defining law, record the exact source and location, what was retained or adapted, and what was defined or derived here. This makes missing credit and missing laws easy to find, but a separate map alone does not explain the traffic mechanism to the reader.

**Candidate B — explain source and adaptation beside each component.** Introduce what the rule is trying to represent, how it changes the traffic, and which part comes from prior work. This makes the main report understandable, but scattered explanations need a consolidated index to show complete coverage.

I recommend **using both: contextual explanation in the report, backed by one complete source map**. They serve different reading needs and are compatible. Label the complete model as a documented composition of ingredients, without implying that a single paper supplies it or that project ownership alone proves novelty. A project-defined rule still needs a traffic justification and later validation.

The requirement for clear attribution is already established. This is a proposed way to satisfy it, rather than a new global traffic-model choice. The existing component-local question **UR-C7-Q1** supplies the detailed source records as laws are selected; there is no new Type 2 question or separate scientific gate for the report layout.

## Decisions collected for this discussion

| Topic | Proposed answer | What remains for the concrete model and evidence stages |
|---|---|---|
| Fair comparison | Allow each rival its legitimate observations/inference; use rival-specific matching. Seek a universally indistinguishable pair where feasible, without requiring one for every comparison. | Principal rival equations and capabilities, realizable matched pairs, independent references and common external intervention. |
| Complete sensitivity | Retain complete TST under the existing control/clearance default; use a common sufficiently long horizon where local clearance holds. | Selected-law derivatives, their regularity, numerical horizon/cap and derivative checks, richer-evaluator usefulness. |
| Explanation and credit | Put causal explanation and source/adaptation credit beside the model, supported by a complete source map. | Exact equation-level sources and derivations once the laws are selected. |

These are the written choices for review; my recommended answers are stated alongside them. The examples are conceptual, not executed fixtures or evidence that the order-aware model wins.

The present task stops at this proposal. Once these principles are reviewed, consolidate them with Q1–Q4 into the shared urban contracts before dependent components close. The later coupled proposal will specify allocation, physical access and service. Revisit a settled principle only if that work reveals a genuine conflict or a materially different traffic assumption. No simulator implementation or numerical experiment is opened here.

[Full question inventory and ownership](../../extraction/research_readiness/urban_open_question_register.md)

[Work record and document checks](../../reporting/research_readiness/urban_categories345_work_report.md)
