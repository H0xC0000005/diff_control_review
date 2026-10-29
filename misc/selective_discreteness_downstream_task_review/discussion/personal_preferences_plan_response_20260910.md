# Response to downstream-review plan preferences

Date: 2026-09-10  
Status: approved and incorporated into the review protocol on 2026-09-10

## Overall assessment

All four preferences are methodologically compatible with the approved review. They improve its prioritization and intended outputs without changing the project's scientific invariants. I recommend accepting them with two safeguards:

1. baselines and the proposed model must share one task contract rather than receiving different task definitions; and
2. traffic-signal control should be the prioritized domain, but its value should be established through the target traffic mechanism and evidence—not by relying on the broad statement that traffic-signal control is difficult.

The fourth preference materially refines the review deliverables. It should therefore be incorporated as an explicit protocol amendment only after user approval of the interpretation below. T1 remains unopened in the meantime.

## 1. Specify baselines together with the task

**Decision:** admit, with a terminology correction.

The concern is valid: a task cannot be considered executable until the comparison roles are realizable under it. Task formulation and baseline realization should therefore be co-designed and approved at the same gate.

However, there should not be a separate “baseline task formulation” if that means changing the scientific task for each baseline. The review should define one **shared task contract**:

- control variable and feasible set;
- objective, units, horizon, and terminal treatment;
- topology, demand, routes, signal structure, and scenario bank;
- initialization and information available to the controller;
- optimization/evaluation budget and stopping rules; and
- positive, equivalent, partial, and negative-result interpretations.

Each baseline then receives a **realization specification** describing how that same contract is represented in the baseline, what state it lacks, whether gradients are available, and what adaptations are allowed. If a baseline cannot express an essential part of the shared task, this is recorded as a capability boundary; it is not repaired by silently giving the baseline a different objective or easier scenario.

This makes baseline feasibility a task-selection criterion rather than a post-hoc implementation detail. It also prevents two common confounds:

- attributing an advantage to model resolution when the models optimized different objectives; and
- attributing an advantage to gradients when the optimizers received different variables, information, or budgets.

**Recommended protocol effect:** strengthen Q5 and the task-contract gate so that every retained primary task includes a baseline realization matrix and fairness audit before selection.

## 2. Prioritize traffic-signal-control tasks and green allocation

**Decision:** admit as a review priority, not yet as a frozen final task.

Prioritizing traffic-signal control is well justified for this project because:

- signal service directly activates the downstream interaction region where lane access, movement order, storage, and blockage can alter realized discharge;
- continuous fixed-time green allocation offers a clear initial derivative input under fixed phase topology;
- the email-trace literature supplies established LTM-based control tasks and a hierarchy between network service targets and implementable signals; and
- the user's prior traffic-simulation experience reduces task-interpretation and implementation risk.

The statement that traffic-signal control is generally difficult is not, by itself, a contribution argument. A defensible project claim must identify the particular difficulty addressed: aggregate models may hide lane-specific storage/access/order states that change the effect of a green allocation, while richer discrete models may not supply the desired derivative path.

Green allocation should therefore become the **leading primary-task family searched and formulated first**. It remains subject to review evidence concerning its physical parameterization, objective, baseline matching, nonsmooth events, and translation to implementable control. Fixed phase topology remains the initial boundary; categorical phase order, actuated control, and controller learning are not pulled into the primary task.

**Recommended protocol effect:** change the priority order, not the eligibility boundary. Search and synthesis begin with fixed-time green allocation for lane/storage-sensitive signal control, while retaining the existing gate before final task selection.

## 3. Prefer simple, semantic, traffic-engineering-sound tasks

**Decision:** admit and turn the preference into explicit selection criteria.

Here, “simple” should mean **minimal confounding while preserving the causal mechanism**, not merely easy to optimize or easy for the proposed model to win. A preferred task should:

- have a physical traffic interpretation independent of the proposed implementation;
- use a control variable that a traffic engineer can interpret;
- define an objective in meaningful units and treat unfinished traffic explicitly;
- activate one declared mechanism at a time before combining mechanisms;
- permit hand/reference cases and matched baseline realization;
- avoid unnecessary route-choice, stochastic-controller, or phase-sequence complexity; and
- remain rich enough that lane/order/storage semantics can genuinely change the result.

A small isolated junction or short approach with a finite turn pocket is therefore preferable to a large network as the first verification setting, provided the geometry is not a contrived one-case demonstration. Complexity should then increase through declared variants and held-out cases.

**Recommended protocol effect:** add parsimony, semantic clarity, mechanism isolation, and baseline matchability to the task-ranking rubric. These criteria complement—not replace—traffic relevance and external validity.

## 4. Split task proposal into a concrete primary suite and broader task map

**Decision:** admit, with a sharper boundary between an experiment suite and future task families.

The proposed two-part structure is useful, but the first part should not be described as merely an example. It should be the review's principal candidate output and, if approved at the later gate, the first executable experimental task contract.

### Part I — near-executable primary green-allocation suite

The review should produce one shared signal-control contract plus a small progression of causally related variants:

1. **Matched aggregate reference:** fixed-time green allocation where the local lane/order mechanism is inactive or homogenized. Purpose: establish macro-limit equivalence and verify that any later difference is not caused by an unmatched task.
2. **Finite turn-pocket storage:** introduce a dedicated pocket whose capacity and demand can activate spillback. Purpose: test whether explicit local storage changes predicted service and control sensitivity.
3. **Access/order-sensitive blockage:** use paired states or arrivals with matched aggregate totals but different movement order or realized pocket access. Purpose: isolate the additional information supplied by selective discreteness.
4. **Combined/held-out cases:** vary demand, pocket length, ordering, and initial queue state without changing the task definition. Purpose: test robustness and prevent a single constructed scenario from carrying the claim.

For each variant, the review should specify:

- intersection geometry and lane permissions;
- fixed and varied scenario quantities;
- green-allocation variable and feasibility constraints;
- objective and terminal treatment;
- mechanism intended to be activated;
- expected indistinguishability or divergence among baseline roles;
- forward, gradient, optimization, and richer-evaluator evidence;
- failure/negative-result interpretation; and
- which project components are required.

The suite should distinguish **effective service allocation** from **directly implementable signal timing**. The first task may legitimately remain at the service-allocation layer, but its claim must say so. A realization experiment requires cycle, clearance/lost time, minimum-green, and phase-interval rules and should not be implied without those elements.

### Part II — broader downstream task map

The review should also identify a bounded set of later task families, including tasks adjacent to or beyond green allocation. These are conceptual candidates rather than near-executable experiment plans. Each should receive:

- traffic purpose and decision variable;
- required derivative and model capabilities;
- relationship to the selective-discreteness hypothesis;
- additional scientific or engineering dependencies;
- plausible baselines and evaluator;
- reason it is later than the primary suite; and
- evidence that would justify promotion to a future executable review.

This part should remain project-bounded. It is not a survey of every possible differentiable-simulation application and should not pre-authorize dynamic route choice, categorical phase design, actuated control, reinforcement learning, or other currently deferred scopes.

## Recommended amendment to the review workflow

If approved, the protocol should be amended as follows:

1. **T1–T4:** retain the approved search, screening, and extraction process, but rank fixed-time signal green allocation and finite turn-pocket blockage first.
2. **T4 extraction:** add shared-task compatibility, baseline realization, control-layer semantics, and parsimony fields.
3. **T5 task-family gate:** select both (a) the primary green-allocation experiment family and (b) a bounded conceptual map of later tasks.
4. **T6 task-contract gate:** require a near-executable Part-I suite, including its baseline realization/fairness matrix. Part II remains conceptual and cannot authorize implementation.
5. **T7 impact audit:** classify project implications from the approved Part-I contract; treat Part II only as future-facing risk and opportunity context.

The later T5 and T6 gates remain intact. Prioritization does not prejudge their decisions.

## Conflicts and residual questions

No critical conflict exists with the approved protocol. The changes refine priority, selection criteria, and deliverable structure. They do not change the accepted project-bounded search philosophy or authorize implementation.

One distinction should remain open for the review rather than be settled now:

> Is the primary output a high-level continuous effective-service allocation, or a directly realizable fixed-time signal plan?

The former is smaller and matches the current simulator boundary; the latter is operationally stronger but requires additional timing and feasibility semantics. The review should compare them explicitly and close the choice at the task-contract gate.

## Current status

The user accepted all four preferences with the stated safeguards on 2026-09-10. The two-part output, TSC-first ordering, shared task/baseline contract, and explicit task-selection criteria have been incorporated into `review_protocol_plan.md`. T1 has not started. The next action is an explicit user instruction to begin it.
