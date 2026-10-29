# Why the downstream-task review is necessary and how it should guide the project

Date: 2026-09-09  
Status: intermediate methodological discussion; not a review protocol or project-plan amendment

## Context and current phase boundary

Milestone 2 is actively in Phase B and is resolving component-wise design questions. Its progress is correctly maintained in `temp_content/milestone_2_per_lane_interaction_zone/`; the project-wide status files continue to describe only the last closed milestone state until Milestone 2 reaches an appropriate closure or formalization gate. This is the intended workflow, not a status inconsistency.

The downstream-task discussion therefore arrives at a useful but delicate time. Milestone 2 has no frozen Phase-C plan and no implementation that would need to be discarded. Its proposal can still be checked against task-facing requirements without erasing accepted Milestone 1 work or silently rewriting current Phase B decisions.

## Bottom line

A downstream-task review is necessary because the scientific value of the proposed state representation depends on a task-specific gradient contract. The project already has a credible representation question and model lineage, but the phrases “useful gradient” and “signal optimization” are not yet sufficiently specific to determine which state resolution, objective, scenarios, baselines, or evaluator are required.

The review should occur before Milestone 2 Phase C, but it should not attempt to freeze every implementation and experiment detail now. It should establish a **task-facing scientific contract** that is strong enough to guide Milestones 2 and 3, while leaving engineering details that genuinely depend on completed interfaces to their later milestone plans.

The downstream task should become a **co-equal scientific pillar** alongside traffic-model validity and differentiability—not the sole authority over model design, and not a merely advisory reference point.

## 1. Why a downstream-task review is necessary

### Problem statement

The unresolved question is whether the project should continue building the proposed mesoscopic model and select an application afterward, or first review and define the task that will determine what model information and gradients are scientifically useful.

### Why implementation-first is risky here

Model-first development is not inherently unsound. It is reasonable when constructing a general-purpose simulator with well-established semantics and a broad user base. This project, however, makes a narrower claim: selectively retained route order and lane-local state are valuable because they improve downstream sensitivities. That claim cannot be evaluated independently of the downstream task.

Continuing implementation without a task contract creates five specific risks:

1. **Mechanism mismatch.** The selected task may rarely activate shared-lane blockage, finite turn-pocket storage, or order-dependent service. The model could be correct yet the experiment would be unable to reveal its intended value.
2. **Objective mismatch.** An objective dominated by uncongested travel time or total throughput may be insensitive to local ordering even when queues differ. Conversely, a narrowly crafted queue penalty may exaggerate the benefit without traffic-engineering relevance.
3. **Gradient ambiguity.** “Differentiate the simulator” does not identify the control variable, scalar outcome, feasibility constraint, fixed scenario structure, nonsmooth regimes, or external validation target.
4. **Baseline insufficiency.** The completed model review shows that a macro-only comparison cannot attribute benefit to exact order. The task must permit matched movement-queue and lane/storage alternatives as well.
5. **Architecture lock-in.** A completed lane grid and service interface can make later task formulation inherit convenient implementation choices rather than scientifically necessary state.

### Why the task cannot be frozen completely now

The opposite extreme—fully specifying a large final experiment before Milestones 2 and 3 are designed—also carries risk. Runtime, active-set behavior, controllable interfaces, and reference-simulator mapping cannot all be known before the relevant components exist. A premature detailed benchmark could force arbitrary tolerances or interfaces and confuse task relevance with engineering convenience.

The correct timing is layered:

- **Now, before Milestone 2 Phase C:** select the scientific task family, differentiated variable, objective family, causal phenomena, baseline roles, external-evaluation principle, and falsification logic.
- **During Milestones 2 and 3:** use those requirements to check state sufficiency, interfaces, diagnostics, and scenario support; do not tune the model to win a benchmark.
- **Before sensitivity and optimization experiments:** freeze exact equations, scenario distributions, optimizer budgets, evaluator mapping, and quantitative acceptance rules using the implemented and validated interfaces.

### Candidate development modes

#### Candidate A — continue model-first and choose the task after Milestone 3

The model is completed according to its current traffic semantics, and task selection occurs only when all intended behavior is available.

**Pros**

- avoids premature experiment constraints;
- preserves the simulator as a more general methodological object; and
- makes task feasibility easier to estimate from working code.

**Cons**

- cannot justify why the chosen state is the minimum needed for a useful derivative;
- risks building components whose scientific effect is not measurable in the eventual task;
- makes baseline and objective selection vulnerable to post hoc choice; and
- may require expensive interface redesign after Milestone 3.

**Scientific consequence:** acceptable for a simulator-engineering project, but weak for the present hypothesis-driven contribution.

#### Candidate B — let one selected downstream task become the primary authority over all model design

Every component and state variable is retained only when immediately necessary for the selected benchmark.

**Pros**

- produces a focused and economical system;
- makes the experiment and implementation tightly aligned; and
- discourages unnecessary modeling scope.

**Cons**

- encourages benchmark-specific overfitting;
- may weaken established traffic semantics merely to simplify one task;
- can turn a representation study into a one-scenario optimization method; and
- provides little robustness if the selected task proves uninformative.

**Scientific consequence:** the task could silently override conservation, physical storage, or exact-order semantics, which is unacceptable without an explicit methodological change.

#### Candidate C — use the downstream task as a co-equal pillar

Traffic semantics determine what constitutes a valid simulator; the derivative contract determines what must remain differentiable; the downstream task determines which valid and differentiable capabilities are scientifically necessary and how their value is tested.

**Pros**

- aligns the model with a falsifiable contribution without letting the benchmark define traffic truth;
- exposes unnecessary or missing components before implementation;
- supports fair baseline construction and negative results; and
- preserves a clear separation among forward validity, derivative validity, and decision usefulness.

**Cons**

- requires explicit reconciliation when task convenience conflicts with model semantics;
- adds a review gate before Milestone 2 can freeze; and
- some experiment details must still be revisited after implementation.

**Scientific consequence:** the model is neither task-agnostic nor task-overfit. It is deliberately sufficient for a defined class of signal-relevant phenomena.

### Recommendation

Adopt Candidate C. The review is better than continuing the current model-first sequence because it closes the causal and derivative contracts before the lane-local architecture is frozen, while respecting already accepted traffic invariants. It is also safer than making a single benchmark the sole design authority.

## 2. How the review should affect project and milestone plans

### Three-pillar authority model

The project should treat the following as co-equal constraints:

1. **Traffic-model validity:** conservation, LWR/LTM consistency, physical storage, feasible node flows, route semantics, and causal spillback.
2. **Differentiability validity:** a declared continuous input, traceable gradient path, fixed structural conditioning, and honest treatment of active-set boundaries.
3. **Task and evidence validity:** a traffic-engineering-relevant objective, scenarios that activate the studied phenomena, fair baselines, and an external decision-usefulness test.

No pillar may silently override another. A task cannot justify unphysical flow; a traffic component is not required merely because it is realistic if it cannot affect the chosen task; and differentiability cannot justify smoothing or simplifying away the phenomenon being tested.

### Expected effect on Milestone 2

Milestone 2 should not be discarded pre-emptively. Its per-lane interaction zone is plausibly required by the existing target phenomena, and Phase B is precisely the stage at which task-facing requirements can still influence its design.

Before Phase C, the downstream review should determine whether Milestone 2 must support:

- which lane/pocket geometries and shared-lane configurations;
- which state observations are required to construct the objective and evaluator mapping;
- which scenario initialization and demand-order inputs are needed;
- which aggregate ablations can be produced without duplicating a simulator;
- whether the local-zone extent and rank resolution can represent the selected causal cases; and
- which outputs must remain comparable with a richer simulator.

If the review conflicts with a component-local choice, revise the relevant Phase B question and record the reason. If it conflicts with a closed Milestone 2 global contract, explicitly reopen the smallest affected global decision. Because Milestone 2 has not reached Phase C or implementation, “redoing” it would normally mean revising its proposal and question closures, not discarding code.

### Expected effect on Milestone 3

Milestone 3 is more directly task-dependent because it defines the behavior that turns lane/order state into realized flow. The review should constrain:

- the required lane-allocation versus accessibility behavior;
- whether exact FIFO is essential for the selected primary task or mainly a reference operator;
- the service and storage active boundaries that must be diagnosable;
- the aggregate movement and lane/storage ablations;
- the signal parameterization exposed to optimization; and
- the forward outputs needed for cross-fidelity matching.

The task should guide which established lane-allocation rule is minimally sufficient. It should not license a rule that violates the accepted separation between desired intent and physically realizable occupancy.

### Expected effect on later experimental milestones

The current sensitivity–optimization–cross-fidelity sequence is sound and should be retained unless the review finds that the primary task cannot support it. The plans will likely need amendment in three respects:

1. expand the comparison from macro versus meso to macro, structured movement queue, lane/storage aggregate, and selective-discreteness gradients, plus a forward-only individual/event reference;
2. replace the temporary diagnostic objective with the selected task objective and metric contract; and
3. define external evaluation, equivalence, cost, and negative-result criteria before scientific runs.

### Should Milestone 1 ever be discarded?

Discarding Milestone 1 requires a much higher threshold than revising Milestone 2. Milestone 1 is closed, conservative, behaviorally passive, and establishes route identity/order without changing aggregate flows. It can serve as exact-order infrastructure and an ablation even if a selected task ultimately shows that exact order adds no decision value.

Discarding it would be justified only if the review supports all of the following:

1. the project's primary scientific question is explicitly changed so that persistent route/order semantics are no longer under study;
2. every selected task can be formulated credibly with aggregate movement or lane state;
3. retaining the ledger materially obstructs the new architecture rather than merely adding dormant metadata cost; and
4. the benefit of removal exceeds the loss of an already validated exact-order reference and requires an approved methodological amendment.

That would amount to changing the identity of the project, not merely improving its experiment. Nothing in the current evidence justifies it. The prudent default is to retain Milestone 1 and allow the downstream experiments to determine whether its information is useful.

### Change-control recommendation

The review should produce an **impact matrix**, not directly edit project plans. For every accepted task requirement, the matrix should identify:

- affected project invariant or hypothesis;
- affected milestone/global or component-local decision;
- status: compatible, clarification needed, amendment needed, or scope conflict;
- smallest required change;
- dependent questions and validation evidence; and
- whether the change must occur before Milestone 2 Phase C, before Milestone 3 Phase C, or before the experimental milestones.

Only after the user approves the review closure and impact matrix should `PROJECT_CONTEXT.md`, `PLANS.md`, or milestone plans be amended.

## 3. The purpose and expected outcomes of the review

### Recommended purpose statement

> Identify the smallest traffic-control task family that causally activates the route-order, lane-accessibility, finite-storage, and blockage mechanisms under study; define its objective and differentiation contract; determine the fair baseline and richer-evaluation requirements; and translate those findings into explicit constraints and amendment candidates for the model and experimental roadmap without presupposing that selective discreteness is beneficial.

This purpose is stronger than “find an application.” It makes the task review part of the method: the review defines what evidence can establish, narrow, or refute the proposed contribution.

### Required outcomes

The review should not close until it produces the following:

1. **Task-family taxonomy.** Candidate traffic/optimization tasks classified by control variable, objective, traffic phenomenon, spatial scale, derivative method, and evaluation practice.
2. **Primary task recommendation.** One main task family with explicit rationale, plus only those supporting diagnostic tasks needed to establish causal mechanisms or derivative correctness.
3. **Gradient contract.** The decision variable, objective, scenario conditioning, feasibility constraints, gradient path, nondifferentiable structure, and derivative interpretation.
4. **Objective contract.** Exact metric semantics, units, horizon, source and terminal queues, incomplete-trip treatment, and compatibility with all simulators.
5. **Scenario contract.** Network/geometry class, demand regimes, route/order construction, deterministic versus sampled treatment, and optimization/evaluation splits.
6. **Baseline contract.** Differentiable homogeneous, movement-queue, lane/storage, and full selective-discreteness models, plus the role of forward-only individual/event references.
7. **External-evaluation contract.** Reference simulator or evidence source, parameter and signal mapping, seeds/replications, and comparable outputs.
8. **Decision rules.** What full support, partial support, equivalence, failure, or a scientifically useful negative result means.
9. **Feasibility assessment.** Component dependencies, data/software needs, computational burden, and risks of task-specific overfitting.
10. **Project-impact matrix.** Exact implications for Milestone 2 Phase B/C, Milestone 3, and later experimental plans, with smallest amendment proposals.

### What the review should not do

The review should not:

- assume the proposed model must outperform aggregate alternatives;
- select a task solely because current code already supports it;
- broaden into every application of differentiable traffic simulation;
- reopen closed traffic invariants without evidence;
- prescribe low-level APIs that depend on unimplemented components;
- use an objective that cannot be measured comparably in the richer evaluator; or
- amend project-wide files before the task conclusions and impact matrix are approved.

### Closure criterion

The review is successful when a reader can answer, without referring to implementation convenience:

- what decision is being optimized;
- what traffic outcome defines success;
- why the chosen scenarios require the information under study;
- which simpler models could explain the same result;
- what derivative each model supplies;
- how those directions are evaluated fairly; and
- how every task requirement changes, confirms, or leaves unchanged the model roadmap.

## Final recommendation

Pause the closure of Milestone 2 Phase B long enough to complete and approve the downstream-task review's task-facing contract. Do not discard Milestone 2 or reopen Milestone 1 by default. Use the review to audit current Milestone 2 questions before Phase C, revise only the smallest conflicting decisions, and preserve the current traffic semantics unless the selected task exposes a documented scope conflict.

This sequencing turns downstream-task definition into a genuine methodological input while avoiding both extremes: a model completed before its scientific test is defined, and a simulator overfit to one prematurely frozen benchmark.
