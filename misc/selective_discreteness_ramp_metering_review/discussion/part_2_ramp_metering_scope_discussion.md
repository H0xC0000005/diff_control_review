# Feedback 17: Part-I closure and proposed ramp-metering feasibility study

Date: 2026-09-14
Migration note: moved to the dedicated ramp-metering review on 2026-09-14. Earlier references to execution inside the downstream-task package are superseded by this package's review_protocol_plan.md. Original decision text below is retained as history.
Status: Initial scope discussion; its three choices are now resolved by feedback 18. See `part_2_scope_decision_record.md` for accepted interpretations and opening readiness. Candidate descriptions below are retained as discussion history.

## Is the proposed change clear?

Yes. Replace the broad future-task map with a focused feasibility study of freeway ramp metering as a potential second, parallel scientific task. “Parallel” means a second application alongside green allocation; it does not authorize concurrent development, require acceptance of ramp metering, or imply that both tasks must enter the same implementation milestone.

The study should answer three separate questions: can an in-scope simulator represent the necessary ramp/merge physics credibly; does this task distinguish the selective-discreteness hypothesis from simpler aggregate alternatives; and, if both are supported, what minimal action, objective, scenarios, gradient path and comparison contract would make a defensible experiment? A task can be feasible to implement yet weak evidence for the representation hypothesis. That distinction is central to this review.

The direction is sufficiently clear to discuss a replacement plan. Three choices below should be resolved before freezing and executing it. The recommendations are provisional.

## Q1 — How much model change may feasibility assume?

**Problem statement.** Must the second task fit the established architecture, or may its feasibility depend on a materially expanded traffic model?

**Assumed model-chain function.** Ramp control would influence admitted ramp flow, merge discharge and downstream/upstream states, and ultimately the measured objective. The study must identify which operators and states are required along that chain. It must distinguish closed components, planned but unresolved M3 functionality, and genuinely new capabilities.

**Core gap.** The feedback raises lane changing and speed as possible necessities. Neither necessity nor dispensability has been established here. Explicit trajectories/lane changes, aggregate merge allocation, equilibrium speed derived from density, and independently evolving speed state are different modeling commitments and must be distinguished from source equations rather than from terminology alone.

**Candidate A — strict compatibility with bounded adaptations (recommended).** Evaluate feasibility using the established continuous-mass, aggregate propagation/local refinement architecture and the approved decision boundaries. Permit candidate merge/boundary adapters to be proposed, with their ownership, literature basis and required approval stated. Do not assume unresolved M3 behavior already exists. Treat any essential new microscopic lane-changing or independent speed-dynamics requirement as conditional/out-of-scope feasibility, not as an automatically accepted dependency.

- **Pros:** answers the user's scope concern directly; protects closed components; makes the implementation burden inspectable.
- **Cons:** may reject attractive tasks that a broader simulator could handle; compatibility still needs operator-level evidence.
- **Dependency/consequence:** a feasible finding permits later planning, not implementation or reopening a closed component.

**Candidate B — include an explicit model-extension option.** Alongside compatibility, design the smallest extended simulator necessary if the present architecture is insufficient, including new state, equations, derivatives and validation requirements.

- **Pros:** explains what would make a rejected task possible; can reveal a worthwhile architectural extension.
- **Cons:** increases review scope and may become a simulator redesign; weakens the premise of a readily parallel second task.
- **Dependency/consequence:** extension-dependent feasibility needs separate project-level approval; its cost cannot be hidden in a merge adapter.

**Provisional recommendation:** A, while recording the minimum missing capability for rejected candidates without developing a full extension plan.

## Q2 — What qualifies ramp metering as a successful second task?

**Problem statement.** Is general gradient-based ramp control sufficient, or must the task test the incremental value of selectively retained information?

**Assumed model-chain function.** Baselines and the proposed model receive the same control, demand, objective and physical setting. Their state differences must explain any differences in predicted service or useful control directions.

**Core gap.** A well-established control problem, simple mathematics, real-world relevance or strong conventional controllers would not alone establish its diagnostic value for this project's representation hypothesis. “Shorter gradient path” also needs a defined comparison: fewer action variables, fewer local dependencies and less temporal sensitivity accumulation are not interchangeable.

**Candidate A — require diagnostic value for selective discreteness (recommended).** Recommend ramp metering as a parallel validation task only if evidence supports an in-scope mechanism for which retained local information can matter beyond a credible aggregate merge/storage baseline. Allow sufficiency or negative results; do not assume selective detail must win. Return distinct verdicts for physical feasibility and scientific diagnosticity.

- **Pros:** directly answers the user's stated validation purpose; avoids choosing a task solely because it is tractable.
- **Cons:** may conclude that ramp metering is a useful control benchmark but unsuitable as a second representation test; mechanism evidence may be limited.
- **Dependency/consequence:** baseline capability and scenario matching must be defined with the mechanism, before optimization is proposed.

**Candidate B — accept a general control/engineering benchmark.** Accept a compatible ramp-control task that validates optimization, throughput/time accounting or software reuse even if aggregate models retain all decision-relevant information.

- **Pros:** can supply a simpler development or sanity-check task; useful even without an order-sensitive regime.
- **Cons:** does not independently validate the selective-discreteness hypothesis; risks overstating the second task's scientific contribution.
- **Dependency/consequence:** must be labeled an engineering/control benchmark and excluded from evidence claiming incremental representation value.

**Provisional recommendation:** A as the promotion criterion; B may be reported as a secondary verdict, not silently substituted for the requested scientific task.

## Q3 — How broad and concrete should the feasibility study be?

**Problem statement.** Should the review stop at a minimal local ramp/merge formulation or cover coordinated freeway control and mandatory real-site reconstruction?

**Assumed model-chain function.** A candidate needs a control parameterization, merge and ramp-queue representation, demand/supply boundaries, objective/population accounting, comparison controllers/models, and an evaluator. Spatial/control scope determines how many coupled states and additional assumptions this introduces.

**Core gap.** “Ramp control” does not fix single versus multiple ramps, open-loop metering rates versus feedback-policy parameters, or synthetic versus real-site evidence. These should not all become mandatory scope by implication.

**Candidate A — single-ramp feasibility first, conditional formulation (recommended).** Prioritize one controlled on-ramp and its merge with enough upstream/downstream domain to capture the selected mechanism. Review open-loop metering allocation and conventional feedback as alternatives, then recommend the smallest justified action definition from evidence. Search for accessible documented sites/data, including US examples, but require a credible minimal scenario and evaluator rather than a full site reconstruction. Produce a formulation outline only if feasibility and diagnosticity warrant one; otherwise provide rejection reasons and missing capabilities.

- **Pros:** bounds confounding and effort; preserves freedom to select the control semantics from literature; can produce a clear yes/conditional/no result.
- **Cons:** cannot establish coordinated-network value or field effectiveness; documented site data may not resolve local behavior/calibration.
- **Dependency/consequence:** exact numerical calibration and executable experiment design remain a later gate, as in Part I.

**Candidate B — coordinated corridor and real-site reproduction as required outputs.** Include multiple controlled ramps and interaction between them; make a reconstructible empirical case a feasibility condition.

- **Pros:** tests broader operational relevance and spatial coupling; provides a more concrete eventual deployment context.
- **Cons:** adds coordination, data access and calibration burdens before local compatibility is known; may obscure why selective information matters.
- **Dependency/consequence:** substantially expands search and formulation scope; requires explicit approval of the additional network/control and data work.

**Provisional recommendation:** A. Real-site availability is an evidence/feasibility dimension, not a promise of field validation. The study should not equate the availability of a road layout with sufficient calibration data.

## How the stated arguments enter the evidence review

The five colleague arguments become evidence questions: established task/controller lineage; documented real cases and accessible data; the conditions under which conventional feedback works; actual derivative/state-chain complexity; and which merge, lane, ramp-queue or spillback mechanisms survive aggregate modeling. Controller terminology, including PID versus other feedback structures, must be verified from the cited sources.

The user's three reservations become feasibility checks: unfamiliarity implies a concise introductory account; lane-changing necessity requires comparison of aggregate merge and explicit lane-change formulations; speed necessity requires separating derived observables from additional dynamic state. These are not settled by this planning response. No new literature search has been performed for this scope discussion.

## Proposed next step after these choices

With A/A/A accepted, draft a replacement Part-II protocol with a focused literature/equation review, component compatibility matrix, baseline/controller/evaluator evidence, and a yes/conditional/no decision. Keep the accepted Part-I record immutable except for clearly labeled handoff/status records. Reuse archived sources before querying new ones; archive new metadata and full text within this review package. Retain batched institutional-access requests and stop gates for scope changes, the evidence-based feasibility verdict, and any proposed task formulation requiring approval.

No project plan, milestone decision or implementation is changed by this discussion. The three decisions above are the remaining critical scope choices; exact controller family, speed representation and merge equations should be findings of the review, not prerequisites guessed by the user.
