# Downstream-task review and formulation protocol

Date: 2026-09-09  
Status: **Part I approved and closed 2026-09-14 through T7. The migrated sibling ramp-metering review also closed on 2026-09-15. No review gate remains.**

Part-II scope and execution addendum: `discussion/part_2_scope_decision_record.md` records feedback 18 and the transfer to the sibling package. The sibling review's `reporting/closure_record.md` now governs the final negative role decision.
Approval date: 2026-09-09  
Amended: 2026-09-10 (TSC-first priority, shared task/baseline contract, task parsimony, and two-part task output)  
Scope: downstream traffic/optimization task selection and scientific formulation for the selective-discreteness project

Execution override, 2026-09-14: the user approved T6 with V5 excluded from this review. This excludes its renamed corridor test I1 as well. T7 covers only the approved V0--V4 Part-I contract. Earlier prospective phase wording is protocol history; closure records are `discussion/t6_closure_record.md` and `reporting/closure_record.md`. At that time Part II was not closed by the T6 approval; it was subsequently reviewed and closed in the sibling package.

## 1. Purpose

This review will identify the smallest traffic-control task family that causally activates the route-order, lane-accessibility, finite-storage, and blockage mechanisms under study; define its objective and differentiation contract; determine fair baseline and richer-evaluation requirements; and translate the findings into explicit constraints and amendment candidates for the model and experimental roadmap without presupposing that selective discreteness is beneficial.

The review is not a search for an application after model construction. It is a methodological completion of the project: traffic validity, differentiability validity, and task/evidence validity will be treated as co-equal constraints.

## 2. Decisions already accepted as protocol inputs

The following are accepted inputs from the prior discussions and will not be reopened unless review evidence exposes a direct conflict:

1. The downstream-task review has a separate sibling workspace from the closed model-lineage review.
2. The task is a co-equal scientific pillar, not the sole authority over traffic semantics and not a merely advisory reference.
3. Project development is halted for this review. The review will close before any Milestone 2 work resumes, so no concurrent milestone/review synchronization rule is needed.
4. Exact implementation-dependent experiment details may be refined after the relevant Milestone 2 and 3 interfaces exist, but before the sensitivity and optimization studies are frozen.
5. Milestone 1 is retained by default. Discarding it would require evidence that the project question itself should abandon persistent order semantics and that the ledger materially obstructs the replacement architecture.
6. Milestone 2 is currently in Phase B. Its active decisions live in the temporary phase archive; project-wide files correctly retain the last closed state.
7. The completed model-lineage review is a read-only input. It established four necessary comparison roles: homogeneous differentiable macro, structured movement queue, lane/storage-aware aggregate, and identity/order mesoscopic forward reference.
8. Initial differentiation remains centered on continuous fixed-time green allocation under fixed phase topology unless the task review supplies compelling evidence for a methodological change.
9. Forward correctness, derivative correctness, internal optimization, and external decision usefulness are separate claims.
10. Fixed-time traffic-signal control is the first review priority. Continuous green allocation under fixed phase topology is the leading primary-task family, but the review must still determine whether the accepted output is high-level effective service allocation or a directly realizable signal plan.
11. Task semantics and baseline selection are co-designed. All models share one task contract; each baseline receives a realization specification rather than a different or easier task.
12. The preferred primary task is simple in the sense of minimal confounding, clear traffic meaning, and isolated causal mechanisms—not in the sense of being easy for the proposed model to optimize.
13. The review will produce both a near-executable primary green-allocation suite and a bounded conceptual map of later downstream tasks.

## 3. Review questions

### Q1 — Which task families are scientifically diagnostic?

Which traffic-control or optimization tasks make movement order, shared-lane blocking, finite turn-pocket storage, or realized lane accessibility causally relevant, rather than merely rewarding generic congestion reduction?

### Q2 — What derivative does each task require?

For every viable task, what are the continuous decision variable, objective/output, feasibility constraint, fixed scenario structure, gradient-carrying state path, structural nondifferentiated variables, and expected nonsmooth events?

### Q3 — Which objective is traffic-engineering meaningful and simulator-matchable?

Which objective can be defined with defensible units, horizon and terminal treatment and computed comparably by the proposed simulator, all differentiable baselines, and a richer evaluator?

### Q4 — Which scenarios expose the representation hypothesis fairly?

What network geometry, demand regime, route/order construction, signal setting, storage configuration, and held-out variation activate the target mechanisms without constructing a trivial win for the proposed model?

### Q5 — What baseline suite is required for the selected task?

How should the four accepted comparison roles be realized—as matched ablations, faithful equation implementations, executable external models, or forward references—under one shared task contract? For each baseline, what realization, unavailable state, permitted adaptation, gradient capability, and capability boundary must be recorded so that model resolution and optimizer effects are not confounded?

### Q6 — How should decision usefulness be evaluated?

What richer simulator or empirical reference, mapping protocol, perturbation/optimization test, stochastic treatment, and success/equivalence/negative-result rules can distinguish a correct internal derivative from a useful intervention?

### Q7 — What must change in the project plan?

Which active Milestone 2 questions, future Milestone 3 contracts, and later sensitivity/optimization/transfer milestones are compatible, need clarification, require amendment, or conflict with the selected task?

## 4. Scope

### In scope

- fixed-time signal-control tasks with continuous timing/service variables;
- isolated junctions, short arterials, or small networks where order, lane accessibility, storage, blockage, or spillback may affect service;
- differentiable traffic simulation and gradient-based signal optimization;
- mesoscopic or aggregate signal optimization that supplies useful task/objective/scenario precedents even without gradients;
- movement-, lane-, queue-, turn-pocket-, oversaturation-, and spillback-sensitive objectives and experiments;
- derivative validation, gradient-direction evaluation, full optimization, held-out testing, and cross-fidelity evaluation;
- matched ablation and baseline-design practice;
- objective definitions and traffic-engineering metrics that can be shared across simulators;
- deterministic tasks and fixed scenario-bank/sample-average formulations;
- negative-result and practical-equivalence design.

### Contextual only

- actuated or adaptive signal control, when it supplies a relevant traffic objective or scenario but changes the control topology;
- offset or cycle-length optimization, when it informs formulation but depends on within-cycle/lost-time effects outside the initial model;
- calibration, tolling, origin–destination estimation, trajectory optimization, and autonomous-driving tasks, when they clarify derivative or evaluation practice;
- reinforcement learning or derivative-free optimization, when used as a comparison protocol rather than the selected task family;
- microscopic and hybrid differentiable simulators, when they clarify gradient paths, evaluator roles, or task feasibility.

### Out of scope

- a general survey of all traffic optimization;
- dynamic route choice as the optimized variable in the initial task;
- categorical phase-sequence optimization;
- a controller-learning or reinforcement-learning review;
- full project-plan amendment or Milestone 2 implementation;
- selection of an objective solely because it already exists in code;
- benchmarking before the task and fairness contracts are approved;
- reopening fixed scientific invariants without explicit evidence and user approval.

## 5. Operational task and gradient contract

Each candidate task will be expressed as

```text
J_M(theta; xi) = Phi(S_M(theta; xi))
```

where `M` is the model/baseline, `theta` is the continuous decision variable, `xi` is fixed scenario structure, `S_M` is the simulated state trajectory, and `Phi` is the scalar traffic objective.

Every retained task must define:

1. `theta`: physical meaning, dimension, units, feasible set, and parameterization;
2. `J` or output vector: equation, units, horizon, and terminal/incomplete-trip treatment;
3. `xi`: demand, routes/order, topology, lane permissions, signals, randomness, and what remains fixed during differentiation;
4. gradient path: model states linking `theta` to `J`;
5. structural boundary: categorical or scenario values not differentiated;
6. nonsmoothness: active constraints, queue emptying, storage saturation, prefix changes, or signal events;
7. baseline compatibility: whether all relevant models can implement the same task;
8. validation: analytic/finite-difference, internal optimization, held-out, and richer-evaluator evidence;
9. decision claim: what positive, partial, equivalent, and negative results mean; and
10. feasibility: required components, software/data, calibration burden, and runtime.

The shared task contract also fixes, across the proposed model and all applicable baselines:

- the control variable and feasible set;
- the objective, units, horizon, and terminal treatment;
- topology, demand, routes, signal structure, scenario bank, and controller information;
- initialization, optimization/evaluation budget, and stopping rules; and
- interpretation of positive, equivalent, partial, and negative results.

Each baseline will have a realization specification stating how it implements that contract, what relevant state or mechanism it lacks, whether gradients are available, and which adaptations are allowed. An inability to express an essential task feature is reported as a capability boundary; it is not hidden by changing the task for that baseline.

The leading initial family is physical green allocation on a simplex with fixed phase topology, prioritized ahead of other downstream applications. This remains a candidate to examine and discuss, not an approved final task choice. The review must explicitly distinguish high-level effective service fractions from directly implementable signal timings; any realization claim requires the corresponding cycle, lost/clearance time, minimum-green, and phase-interval semantics.

## 6. Search strategy

### Evidence sources

Use a project-bounded, proportionate systematic mapping review with focused synthesis:

- arXiv as a first-class recent source;
- TRID and accessible scholarly web indexes;
- publisher and author repositories;
- backward and forward citation snowballing from nearest task papers;
- the existing personal paper archive as a high-priority seed source;
- the 37-study model-lineage corpus as a read-only seed and cross-reference source.

Institutional access requests, if needed, will be collected as one paper-level batch. The request will give title, authors, year, persistent identifier, relevance, and requested material. It will not ask the user to execute database-scale searches.

### Search families

The search will cover at least:

1. differentiable traffic simulation plus signal/control/green split;
2. gradient-based fixed-time traffic-signal optimization;
3. queue-, lane-, turn-pocket-, blockage-, spillback-, and oversaturation-sensitive signal control;
4. mesoscopic simulation used for signal optimization or evaluation;
5. sensitivity transfer, simulator mismatch, surrogate gradient, cross-fidelity, and high-fidelity evaluation;
6. total system time, delay, queue, throughput, incomplete-trip, and terminal-penalty objective formulations;
7. matched comparison, ablation, scenario-bank, held-out, and stochastic-evaluation practices.

Queries may be refined during the pilot to remove unrelated rail, communication-network, or autonomous-driving results. Material scope changes require a user gate; routine term refinement does not.

Coverage expansion is evidence-driven. If later discussion or screening identifies a missing sector relevant to the project questions, add it explicitly. Do not search adjacent fields merely for completeness after evidence shows that they do not inform the selected task, gradient contract, baselines, or evaluation.

### Archiving

Newly queried metadata, full texts, extracted local text, and query notes will be stored under:

```text
misc/selective_discreteness_downstream_task_review/archive/
```

Existing material in the completed model review will be referenced in place rather than duplicated. Every archived item will have a manifest entry recording source, access date, identifier, version, and relation to the review.

## 7. Eligibility rules

### Include as primary task evidence when a work

- studies road-traffic simulation, network loading, or traffic-signal control;
- defines or permits extraction of a decision variable and traffic outcome;
- supplies a task, scenario, optimization, sensitivity, or evaluation design relevant to at least one review question; and
- contains enough method detail to classify its model, objective, comparison, and validation role.

### Include as contextual evidence when a work

- offers a transferable derivative-validation, cross-fidelity, or experimental-design method but uses a different traffic task;
- establishes traffic-engineering importance of a target phenomenon without supplying a matched differentiable task; or
- is a review or guide used for coverage and terminology rather than primary method counting.

### Exclude when a work

- concerns non-road networks without a transferable methodological role;
- only predicts trajectories or behavior without a relevant traffic-control, objective, or evaluation contract;
- mentions optimization but supplies no extractable task formulation;
- is only an editorial, slide, abstract, or inaccessible fragment when a substantive claim depends on unavailable detail; or
- duplicates a later version of the same study without materially distinct methods or evidence.

Borderline exclusions with plausible task relevance will be retained for a user screening gate rather than silently removed.

## 8. Extraction and quality assessment

### Evidence matrix fields

For each included study, extract:

- bibliographic identity and publication status;
- traffic/task family and network scale;
- simulator/model resolution and traffic phenomena represented;
- control/decision variable and feasible set;
- objective equation or operational definition, units, horizon, and terminal treatment;
- deterministic/stochastic scenario design and sample split;
- derivative method and fixed structural assumptions;
- nonsmooth/discrete-event handling;
- derivative validation;
- optimization method, budget, initialization, stopping, and failures;
- baselines and matching conditions;
- compatibility with the shared task contract and model-specific baseline realization;
- whether the optimized signal quantity is an effective service target or a directly realizable timing plan;
- external simulator/data evaluation;
- performance, robustness, and cost measures;
- source code/data availability;
- task relevance to order, lane access, storage, blockage, and spillback;
- strongest transferable element;
- mismatch with the proposed project;
- reviewer inference and uncertainty; and
- task parsimony, semantic clarity, mechanism isolation, and baseline matchability.

### Quality dimensions

Assess credibility dimension by dimension rather than assigning one prestige score:

- task and objective clarity;
- model/task consistency;
- derivative-method transparency;
- comparison fairness;
- scenario adequacy;
- external or held-out validation;
- reproducibility/material availability; and
- maturity, including peer-review/preprint status.

A paper can be strong evidence for an objective definition but weak evidence for gradient usefulness. Such roles must remain separate.

## 9. Candidate-task synthesis and selection

### Candidate families

The synthesis will derive candidates from evidence rather than freeze them in advance. Fixed-time signal green allocation is searched and formulated first. Expected families to test include:

- isolated-junction green allocation with shared-lane/order effects;
- finite turn-pocket and oversaturation-aware green allocation;
- short arterial or interacting-junction green allocation with spillback;
- diagnostic gradient-direction perturbation without full optimization; and
- fixed scenario-bank signal optimization followed by richer-simulator evaluation.

These may become one primary task with supporting diagnostic layers rather than mutually exclusive experiments.

### Decision criteria

Each candidate will be judged on:

1. **Diagnosticity:** activates the representation mechanisms under study.
2. **Gradient interpretability:** supports an explicit, checkable derivative contract.
3. **Traffic-engineering relevance:** has a defensible control, objective, and constraints.
4. **Comparison fairness:** permits the complete differentiable baseline ladder.
5. **External evaluability:** can be reproduced and measured in a richer simulator.
6. **Falsifiability:** permits equivalence and negative conclusions.
7. **Model sufficiency:** requires no unapproved behavior outside the intended scope.
8. **Feasibility:** proportionate data, software, calibration, runtime, and implementation burden.
9. **Parsimony:** introduces no complexity unnecessary to the tested causal mechanism.
10. **Semantic clarity:** gives the control, state, and outcome direct traffic-engineering interpretations.
11. **Mechanism isolation:** separates aggregate propagation, finite storage, access/order blockage, and combined effects before drawing a composite claim.
12. **Baseline matchability:** permits one shared task contract and transparent model-specific realizations.

No weighted score will decide the task mechanically. The evidence table will expose trade-offs, and the recommendation will state which criteria are necessary, preferred, or tolerated.

### Veto conditions

A candidate cannot be the primary task if:

- it does not activate any order/access/storage mechanism;
- its objective cannot be computed comparably across models and evaluator;
- the differentiated variable is primarily categorical or outside approved scope;
- a fair structured movement and lane/storage comparison cannot be constructed;
- external evaluation changes the intervention or outcome being tested; or
- success can only be defined as improvement inside the proposed simulator.

## 10. Required review outputs

The package will contain:

```text
README.md
review_protocol_plan.md
inputs/model_review_handoff.md
discussion/decision_log.md
search/search_queries.md
search/search_log.csv
screening/candidate_records.csv
screening/screening_decisions.csv
extraction/task_evidence_codebook.md
extraction/task_evidence_matrix.csv
synthesis/task_taxonomy.md
synthesis/candidate_task_comparison.md
synthesis/task_selection_record.md
synthesis/primary_green_allocation_suite.md
synthesis/future_task_map.md
synthesis/baseline_realization_matrix.md
synthesis/experiment_formulation.md
synthesis/project_impact_matrix.md
reporting/closure_record.md
archive/manifest.csv
```

The final `experiment_formulation.md` must define the primary task, supporting diagnostics, gradient contract, objective, scenario family, baseline contracts, external evaluation, fairness rules, and interpretation logic. It will distinguish task-level requirements fixed now from implementation details to be frozen later.

`primary_green_allocation_suite.md` will be the near-executable Part-I output. It will define one shared signal-control contract and a progression covering: (1) a matched aggregate or homogenized reference, (2) finite turn-pocket storage, (3) access/order-sensitive blockage using aggregate-matched paired states where supported, and (4) combined and held-out variations. Each variant will state its geometry, fixed and varied quantities, intended mechanism, expected baseline agreement or divergence, required evidence, failure interpretation, and required project components.

`baseline_realization_matrix.md` will map every model role to the shared task contract, unavailable state, allowed adaptations, gradient role, and capability boundary. It will explicitly keep representation comparisons separate from optimizer comparisons.

`future_task_map.md` will be the bounded conceptual Part-II output. For each later task family it will record the traffic purpose, decision variable, derivative and model requirements, relation to the selective-discreteness hypothesis, dependencies, plausible baselines/evaluator, reason for deferral, and evidence needed before promotion to an executable review. It will not authorize implementation or broaden the project into deferred scopes.

The `project_impact_matrix.md` will classify every implication as:

- compatible/no change;
- clarification in the active phase archive;
- component-local question revision;
- milestone-global decision reopening;
- later roadmap amendment; or
- project-scope conflict requiring explicit user decision.

The review will propose changes but will not edit `PROJECT_CONTEXT.md`, `PLANS.md`, or an approved milestone plan without a separate explicit instruction.

## 11. Execution phases and user gates

### T0 — protocol approval

Deliverable: this plan, revised through discussion.

**User gate T0:** approve scope, review questions, search sources, selection criteria, outputs, and milestone timing. No search execution before approval.

### T1 — search pilot and seed handoff

Create `inputs/model_review_handoff.md`, initial queries, and a small pilot spanning differentiable signal control, traffic-engineering queue/storage control, mesoscopic optimization, and external gradient evaluation. Search and synthesis prioritize fixed-time green allocation and finite turn-pocket blockage before broader task families.

Stop only for a material scope anomaly. Routine query refinement proceeds under the approved protocol.

### T2 — discovery and corpus construction

Run the refined accessible-source searches, deduplicate versions, classify source provenance, and identify inaccessible high-priority papers.

If institutional access is necessary, write one batched request and stop so the user can supply the papers.

### T3 — screening and taxonomy pilot

Screen titles/abstracts and pilot the task taxonomy and extraction codebook on representative candidate families.

**User gate T3:** approve inclusion boundary, borderline records, and any material revision to the task/gradient categories.

### T4 — full-text extraction and quality assessment

Extract all included studies, audit nearest task precedents and a sample of contextual records, and record evidence limitations. Code shared-task compatibility, baseline realization, effective-service versus realizable-timing semantics, parsimony, and mechanism isolation.

**User gate T4:** approve the coded nearest-task evidence and confirm that no critical objective, derivative, baseline, or evaluator field is being misinterpreted.

### T5 — candidate-task synthesis and shortlist

Produce the task taxonomy and candidate comparison. Recommend (a) a primary green-allocation experiment family with diagnostic layers and (b) a bounded conceptual map of later tasks. The primary recommendation must preserve one shared task contract across baseline roles and state whether it remains at the effective-service layer or includes realizable timing.

**User gate T5:** select or revise the primary task family, supporting diagnostics, and boundary of the later-task map. No project-plan amendment follows automatically.

### T6 — scientific task formulation

Write the full task, gradient, objective, scenario, baseline, evaluator, fairness, and result-interpretation contracts. Produce the near-executable primary green-allocation suite and its baseline realization/fairness matrix. Keep the later-task map conceptual. Mark every detail as fixed now, default pending implementation evidence, open, or deferred.

**User gate T6:** approve the task-facing scientific contract.

### T7 — project-impact audit and review closure

Audit the accepted contract against active Milestone 2 Phase B decisions, provisional Milestone 3 scope, and later experimental milestones. Produce the impact matrix and closure record.

**User gate T7:** approve the impact classification and close the review. Any actual project or milestone amendment requires a separately authorized pass.

## 12. Timing relative to project work

Project development is halted while this review is discussed and executed. Milestone 2 will not progress concurrently, so the earlier proposal to synchronize T6/T7 with its Phase-B/Phase-C boundary is dismissed as unnecessary. The complete review, including T7 impact classification and closure, will finish before project work resumes. Resumption and any resulting milestone action require a separate explicit user instruction.

The following should be fixed before Milestone 2 Phase C where they affect its architecture:

- target traffic phenomena and geometry class;
- required input order/scenario representation;
- required lane/storage observables;
- baseline/ablation seams;
- evaluator-facing outputs; and
- macro-limit/equivalence requirements.

The following may remain defaults until Milestone 3 or the experimental plans, provided they do not alter Milestone 2 scientific meaning:

- exact optimizer and learning-rate schedule;
- final scenario counts and seeds;
- quantitative performance thresholds;
- reference-simulator calibration values;
- runtime budgets; and
- presentation/reporting details.

If later implementation evidence conflicts with the task contract, reopen the smallest affected task or milestone decision explicitly. Do not compensate through an undocumented adapter or change the objective to fit the available code.

## 13. Anomaly and stop conditions

Stop and request user direction if:

- evidence favors a task requiring categorical phase sequence, endogenous route choice, microscopic car following, or another scope change;
- no candidate permits fair structured movement and lane/storage baselines;
- the objective cannot be matched with the richer evaluator;
- a nearest task predecessor appears to cover the proposed complete contribution;
- institutional access blocks a decision-critical paper after the batched request;
- T6 conflicts with a fixed scientific invariant or closed Milestone 1 contract;
- the review would require discarding Milestone 1 rather than retaining it as exact-order infrastructure/reference; or
- task relevance can only be achieved by weakening conservation, storage, route/order, or derivative-validation requirements.

The method may be refined without a new gate when changes only improve search recall/precision, deduplication, metadata correction, or presentation and do not change the review questions, eligibility boundary, selection criteria, or scientific interpretation.

## 14. Reproducibility and effort boundary

The review will preserve search, screening, extraction, and decision records sufficient for auditability. It will not build software or a database solely for review reproducibility. Existing scripts or simple local checks may be used for deduplication and consistency, but documentation quality takes priority over packaging machinery.

Randomized sampling, if used for reviewer spot checks, will record the seed. All retrieved versions, access dates, and identifiers will be logged.

## 15. Approval decisions and remaining discussion boundary

The user approved this protocol in principle on 2026-09-09 with the following interpretations:

1. The earlier Milestone 2 synchronization question is dismissed because project development is halted for the review. The review closes before development resumes.
2. The review is project-bounded and proportionate, not exhaustive across simulation and optimization literature.
3. The search families and objective/evaluation coverage are accepted. Missing relevant sectors may be added when identified; adjacent fields are not searched only for coverage.
4. The T3, T4, T5, T6, and T7 human gates are accepted.
5. Green split was initially a preferred starting candidate; the 2026-09-10 amendment now makes fixed-time TSC and continuous green allocation the first review priority while preserving the T5/T6 selection gates.
6. All work remains inside this review package. Existing project documents, milestone archives, code, and plans are not changed unless the user separately and explicitly requests it.
7. One shared task contract governs all applicable models. Baselines receive realization and capability specifications rather than different task definitions.
8. Task selection explicitly favors traffic-engineering meaning, parsimony, causal-mechanism isolation, and baseline matchability.
9. The task output is split into a near-executable primary green-allocation suite and a bounded conceptual map of later tasks.

No critical conflict follows from these decisions or the approved 2026-09-10 amendment. Execution has reached the T5 user gate. T6 may begin only after explicit approval or revision of the T5 selection. The plan does not authorize Milestone 2 work, implementation, or amendment of project documents.
