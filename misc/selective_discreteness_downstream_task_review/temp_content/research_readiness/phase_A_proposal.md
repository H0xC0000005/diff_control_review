> Historical review record. The implementation-phase framing is retired following the user clarification of 26 October 2026. Current material: [review_plan.md](review_plan.md).

# Urban review plan: explain the traffic choices before the model details

Updated 23 October 2026 after feedback 4. All four broad principles are settled for this stage: loading from empty, responsive desired allocation, effective average service and exact order without deliberate local mixing. Logical assignment and physical zone entry are separated. Established waiting-lane commitments remain fixed by default; provisional retargeting is deferred. Concrete coupled laws remain to be proposed, especially under Q2/Q4.

The user has now opened the next review task: categories 3–5. Its focused proposal covers fair comparisons, complete sensitivity and scientific credit. The recommendations remain provisional. Q2/Q4 do not block this discussion or require another broad vote.

A useful urban model should explain why more left-turn service helps when turners can reach the bay, and why through service might help first when through traffic obstructs them. The established review already designed an experiment around that distinction. This continuation supplies the missing traffic explanation and model, then shows how to compare its predictions and sensitivities fairly.

[Current discussion: comparison, complete sensitivity and scientific credit](phase_B_categories_3_5_principle_proposal.md)

[Settled four traffic principles](phase_B_categories_1_2_principle_proposal.md)

[Feedback 3: response, critical corrections and current decisions](../../reporting/research_readiness/urban_feedback3_response.md)

[Feedback 4: four-question status and upstream waiting](../../reporting/research_readiness/urban_feedback4_response.md)

## What the old review establishes, and what still needs deciding

The accepted task uses one junction family, four effective-service groups and complete total system time: source waiting, travel and queueing are counted through completion. V0 checks the neutral case; V1 isolates order; V2 isolates storage; V3 combines access and order; V4 checks robustness across held-out situations. The simpler models and richer evaluators already have agreed roles. These are the foundation for the present review.

The remaining difficulty is that a description such as “access depends on order, bay room and lane state” does not say whether a particular turner gets into the bay. Likewise, giving movements capacity limits does not determine how a shared queue discharges. Different ways of filling those gaps can favor different service allocations. That is why this is partly a methodological review rather than only a report rewrite.

The VSL report provides the standard of explanation: its assumptions and traffic laws lead to a particular outcome that a reader can reconstruct. Urban should reach that level for its own model. It does not need VSL's traffic assumptions, its particular information comparison or a more general initializer. Numerical parameter calibration and evidence that gradients improve real decisions remain later tasks.

[Direct evidence for the five logical gaps](../../reporting/research_readiness/urban_vsl_standard_gap_explainer.md)

## The discussion follows the traffic logic

| Topic | What the reader should be able to understand and decide |
|---|---|
| **Traffic world and behavior, discussed together** | How the required queues arise, what lets a turner reach the bay, how service releases obstruction, and how much order must be preserved |
| **Fair comparison** | What simpler models can legitimately observe and infer, and what would count as a benefit from extra order information |
| **Control sensitivity** | How reallocating service affects everybody's complete trip time, including later blockage, spillback and clearance |
| **Explanation and scientific credit** | Which ideas come from existing traffic models, what this study changes, and how the full causal argument can be understood |

The first topic combines logical categories 1–2 because the traffic assumptions and behavior explain one another. Categories 3–5 can then have focused principle discussions. We can agree, for example, that a rival may infer traffic from its arrival history before choosing its full equation set. Whether it can distinguish a particular pair of queues depends on that eventual model.

For each topic, start with the short traffic question and compare candidates through what they assume and predict. Use an example when the distinction is hard to see. Once the main idea is agreed, work out details that follow from it. Bring back a choice if it would change the traffic explanation, the comparison or the meaning of a sensitivity. Precise definitions support that discussion where useful; they are no longer an entry requirement for understanding or considering a candidate.

This replaces the earlier mandatory question template. Reports will not require separate problem/function/gap sections or labeled lists of pros, cons and dependencies. Candidate explanations still make their strengths, limits and provisional recommendation clear in ordinary prose. The preference is recorded in AGENTS.md for subsequent reports and question statements.

## The settled traffic principles

The first proposal records four agreed directions:

1. **Starting queues:** use loading from empty for development and early validation; direct prescribed states are deferred.
2. **Access and lane choice:** develop responsive intended allocation followed by physical access; its perceived resistance, entry/commitment meaning and concrete law remain open.
3. **Service:** effective average service is selected for this stage; an active phase clock is deferred.
4. **Order:** defer local mixing and respect exact allocation/lane order. Logical assignment can finish while the assigned mass waits upstream; physical admission still follows eligibility and actual access.

All four broad choices are settled at the principle level. Q2 and Q4 especially need a concrete coupled allocation/waiting/access/service model. UR-G3-Q1 preserves fixed commitment as the default, with provisional retargeting deferred and the earlier physical scan/prefix cases kept as access possibilities rather than a universal scheduler vote. Detailed equations should not be presented as reopening all four broad choices; genuinely non-equivalent traffic laws still return for discussion.

The user's proposed lane-specific upstream queues are initially logical records of mass still in the aggregate upstream link, counted there once rather than as new physical buffers. Eligible reachable packets can enter partially; their size is not an all-or-nothing restriction. Positive room does not establish access, and no small positive admission cutoff is selected. Reusing an already valid desired lane is a shortcut, while inventing a target because traffic is far upstream would change the model.

The default transcription chooses desired shares responsively, preserves a valid commitment while mass waits, and admits physically when feasible. This retains the inherited no-reassignment rule instead of adding another mandatory principle question. Revisable targets remain a distinct deferred alternative. The concrete allocation point and ownership must be reconciled with the existing seam before a coupled law is adopted. Average service avoids an extra phase-timing model; it does not mean phase-duration sensitivities are inherently zero.

The earlier context discussed equilibrium ideas but did not select a zone-entry equilibrium. M2's existing single-lane precommitment interface also does not already implement responsive balancing. Decide where intended allocation becomes actual lane commitment, preserving eligibility, conservation and causal receiving; explicitly reconsider the smallest affected contract if that meaning changes. No resident-traffic reassignment or interface adapter is inferred from the principle.

## How the remaining work follows those decisions

The current categories 3–5 proposal asks how to judge a rival's legitimate information, preserve complete control-to-clearance sensitivity and explain scientific sources. UR-G4/G5 are the remaining global-principle discussion; the report-credit approach supports the existing UR-C7-Q1 and adds no global traffic question. Review these recommendations and consolidate the shared contracts before dependent components close. Particular rival laws, matched-pair realizability and model-specific derivatives cannot be closed by principle agreement alone.

After the shared traffic choices are understood and agreed, specify how traffic reaches the junction and how access, storage and service work together. Keep the coupled bay problem together: a discharge creates room, that room can admit more traffic, and an obstruction can prevent that admission. These interactions cannot be decided as unrelated local conveniences.

Then make the simpler comparisons concrete. Select one principal movement-queue model and one principal lane/storage model, allow their legitimate information and inference, and explain which queue pairs each can distinguish. Design the independent causal checks and the common way of realizing an allocation in the richer evaluator. Urban's existing requirement for external perturbation checks before full optimization is retained.

Derive the sensitivity of the chosen model, following service changes through access, residual queues, upstream restriction, source waiting and the final clearance. The calculation must describe the actual laws. An internally decreasing objective is not evidence that the direction improves richer traffic behavior.

Finally, check the joined explanation against neutral and coupled examples and write the compact methodology report. Collect scientific source credit while each law is chosen, so the final report can say clearly which pieces are borrowed, adapted or defined here. A model description, numerical correctness and demonstrated decision usefulness remain distinct achievements.

The [full question set](../../extraction/research_readiness/urban_open_question_register.md) uses the same conceptual style. Its supporting tables retain the shared-versus-local ownership and dependencies. Shared scientific choices still close before dependent component details; the conversation itself is organized by category. The [supporting completion/work map](../../extraction/research_readiness/urban_review_completion_and_work_map.md) retains the detailed completion criteria, stage outputs and provisional report budget.

## Scope of this revision

Continuous traffic mass, structural routes and permissions, per-lane local refinement, physical storage and conservation remain the model's basis. The urban Part-I task remains accepted. The earlier handoff of service/order selection to M3 may be reconsidered as authorized. Exact allocation processing and deferral of mixing are now recorded; no concrete replacement access/service law or strict-prefix admission policy is selected. V5/I1 and the ramp line remain outside this review.

This revision opens the authorized categories 3–5 discussion and carries forward the four-question settlement. It does not implement or validate a simulator. The default and deferred commitment alternative remain as recorded; no repeated Q2/Q4 principle vote or interactive prompt is added. This task stops at its discussion proposal. The agreed directions guide the concrete model proposal when authorized; dependent component and experiment work is not started here.

[Current decisions and dialogue](phase_B_revision.md)

[Recovered authority and source evidence](../../extraction/research_readiness/urban_authority_and_gap_audit.md)

[Feedback 2 work record](../../reporting/research_readiness/urban_feedback2_work_report.md)
