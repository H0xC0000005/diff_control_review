# Current downstream-task definition and roadmap status

Date: 2026-09-08  
Status of this document: read-only project-plan audit  
Sources inspected: `PROJECT_CONTEXT.md`, `PLANS.md`, and the approved Milestone 0 and Milestone 1 plans

## Bottom line

The project has a coherent **downstream experimental direction**, but it does not yet have a complete downstream task definition. The documents fix the initial control family as fixed-time signal green allocation and state that useful gradients must ultimately be judged in a richer simulator. They also define a three-stage scientific sequence: compare macro and mesoscopic sensitivities, optimize signals with validated gradients, and test transfer in a higher-fidelity reference model.

What remains open is the experiment-level contract: the exact traffic setting, objective, scenario distribution, full baseline set, optimization protocol, reference-simulator mapping, and quantitative success criteria. Consequently, the current plan is not ready to support a definitive downstream experiment without a separate task-selection and formulation pass.

## 1. What is already fixed or strongly established

### Scientific purpose

The project asks whether selectively retained movement order, lane accessibility, and finite storage produce more useful traffic-control sensitivities than an aggregate representation. The intended result is not merely a simulator with finite gradients; the gradients must support decisions in a richer traffic system.

The central causal setting is already well defined at a conceptual level:

- construct traffic cases with the same aggregate link demand, turning totals, and aggregate state;
- vary finite movement order or lane accessibility;
- observe whether the macroscopic model aliases cases that the mesoscopic model distinguishes;
- compare the resulting signal sensitivities; and
- determine in a richer simulator which sensitivity better predicts objective change.

This is a strong experimental principle because it isolates the information added by the mesoscopic representation.

### Initial control variable

The initial control is fixed-time signal service with fixed phase topology/order. Green split, or an equivalent continuous allocation of service among fixed phases, is the first optimization variable.

The following are deliberately outside the initial task:

- actuated phase-sequence control;
- reinforcement learning;
- endogenous route choice;
- explicit microscopic lane changing;
- network-wide offsets; and
- cycle-length optimization before startup or clearance lost time gives absolute cycle length a meaningful effect.

This restriction is scientifically sensible: it supplies a direct continuous path from control to movement service and avoids mixing the representation question with categorical control changes.

### Scenario and differentiation conventions

The initial simulator is deterministic. If scenarios are sampled later, route/order realizations remain exogenous and fixed while differentiating with respect to signal parameters. The documents call for fixed scenario banks or common random numbers when methods are compared.

The plan also distinguishes three claims that must not be conflated:

1. forward correctness and fidelity;
2. correctness of derivatives of the implemented model; and
3. usefulness of those derivatives for downstream decisions.

### External evaluation principle

A richer reference simulator, currently expected to be SUMO unless later evidence supports another choice, is intended to evaluate both small signal perturbations and final optimized plans. The intended claim is cross-fidelity usefulness, not simply lower loss inside the differentiable simulator.

## 2. What is implemented versus only planned

### Available foundation

Milestone 0 is closed and provides:

- continuous-mass LTM propagation;
- generic node transfer;
- restricted continuum fixed-time signal service;
- a diagnostic total-system-time objective; and
- stable-regime finite-difference and automatic-differentiation checks with respect to physical green split.

This is a gradient-validation foundation, not a completed signal-optimization task. Its total-system-time objective is explicitly temporary and diagnostic.

Milestone 1 is also closed. It provides persistent route identity and ordered continuous route-mass state while remaining behaviorally passive relative to the macroscopic flows. It explicitly does not test whether order changes signal service or improves gradients.

### Dependencies not yet available

The downstream task depends on behavior planned for the next two modeling milestones:

- a per-lane node-facing interaction zone with finite storage and conservative spillback coupling; and
- lane allocation, realized accessibility, and exact or explicitly bounded FIFO service.

Until these capabilities close, the central same-aggregate/different-order task cannot exercise the proposed causal mechanism completely.

### Provisional downstream sequence

The roadmap currently assigns downstream work to three provisional milestones:

| Planned stage | Present purpose | Current status |
|---|---|---|
| Sensitivity study | Test derivative correctness and determine when macro and mesoscopic gradients agree or diverge in matched cases. | Provisional; blocked by completion of lane/storage/FIFO behavior. |
| Fixed-time signal optimization | Use validated mesoscopic gradients for green-split optimization on deterministic cases or fixed scenario banks. | Provisional; objective and experiment contract remain open. |
| Cross-fidelity transfer | Evaluate gradient directions and optimized plans in a richer simulator, initially expected to be SUMO. | Provisional; reference mapping and acceptance criteria remain open. |

This sequencing is methodologically sound: derivative correctness precedes optimization, and internal optimization precedes claims about external usefulness.

## 3. What is still undefined

### Exact traffic task and experimental unit

The documents do not yet select whether the principal experiment is one isolated junction, an arterial fragment, a small interacting network, or a progression from small causal fixtures to a network experiment. Network geometry, demand regimes, horizon, initialization, oversaturation conditions, and the number of controlled junctions are not fixed.

### Final optimization objective

The roadmap mentions queue, waiting, throughput, and related traffic metrics, but does not choose a primary scalar objective or define:

- its exact equation and units;
- terminal-queue treatment;
- source queues and incomplete trips;
- relative weights if several terms are combined;
- evaluation horizon and warm-up; or
- whether the simulator and richer evaluator can compute genuinely matched quantities.

The existing total-system-time implementation cannot silently become the final objective merely because it is available.

### Task-generating scenario family

The project lists useful causal motifs—different movement order under equal totals, shared-lane head-of-line blockage, turn-pocket overflow, and upstream spillback—but does not specify how these become a representative experiment distribution. Missing choices include parameter ranges, demand/order generation, fixed versus sampled cases, training/optimization versus held-out evaluation splits, and how often the targeted mesoscopic effects must be active.

### Complete baseline contract

The current project documents emphasize a matched homogeneous macroscopic baseline. The completed model-lineage review shows that this is necessary but insufficient. A credible experiment must also control for:

1. structured aggregate movement queues or partial-FIFO restrictions; and
2. lane/storage-aware aggregate state without exact realized sequence.

Individual/event mesoscopic LTM can then serve as a forward reference rather than a gradient baseline. This four-level logic is not yet incorporated into `PROJECT_CONTEXT.md` or the Milestones 4–6 roadmap.

This is an **incompleteness, not yet a methodological contradiction**. The roadmap predates the closed review and uses “at minimum” language in several places, so the missing baselines can be added through an approved planning amendment before the sensitivity study. Nevertheless, proceeding with macro versus full meso alone would no longer be scientifically adequate because any gain could arise from movement resolution or lane/storage state rather than exact order.

### Optimization and fairness protocol

The roadmap requires identical objective definitions and optimizer/update budgets where possible, but does not fix the optimizer, control parameterization, feasibility mapping, initialization policy, stopping rule, hyperparameter-tuning allowance, failure handling, or whether comparisons use one-step directions, full optimization, or both.

### Cross-fidelity mapping

SUMO is an expected reference, not an approved and calibrated evaluator. The following remain unspecified:

- network and lane-geometry translation;
- demand, route, signal, saturation-flow, storage, and fundamental-diagram matching;
- treatment of continuum versus on/off signal service;
- stochastic seeds and replication count;
- warm-up and measurement windows;
- common objective construction; and
- separation of representation error, stochastic variance, and optimization artifacts.

### Quantitative success and negative-result criteria

The plan correctly permits a negative result, but it does not define how much directional agreement, externally evaluated improvement, runtime/memory cost, or robustness is enough to support or reject the selective-discreteness hypothesis. It also does not define equivalence or practical-indifference criteria under which the simpler aggregate model should be preferred.

## 4. Consistency assessment

The existing plan is internally coherent in the following respects:

- fixed-time green allocation matches the available continuum signal derivative path;
- deterministic causal cases fit the fixed structural route/order differentiation contract;
- the sensitivity–optimization–transfer sequence respects the validation hierarchy; and
- a richer evaluator is required before claiming gradient usefulness.

The main weaknesses are definition gaps rather than contradictions:

- the final objective is not selected;
- candidate task families have not been compared using literature evidence;
- the scenario distribution and experimental unit are not selected;
- the baseline plan is now narrower than the completed literature review supports;
- the reference-evaluator contract is only aspirational; and
- success, equivalence, and negative-result thresholds are not quantitative.

One wording risk should be corrected during later task formulation: the project sometimes contrasts only a “matched homogeneous macro” gradient with the mesoscopic gradient. After the model-lineage review, this is no longer enough to attribute value specifically to exact order. The structured movement and lane/storage aggregate alternatives must appear in the explanatory comparison design.

## 5. Status conclusion

The downstream direction is **conceptually defined but experimentally under-specified**.

- **Fixed or established:** fixed phase topology, green split as the initial control, continuous service path, deterministic-first scenarios, same-aggregate/different-order causal logic, separate derivative and usefulness validation, and richer-simulator evaluation.
- **Provisional:** the sensitivity study, signal-optimization study, SUMO transfer study, scenario-bank use, measurements, and staged milestone allocation.
- **Open:** the exact task, primary objective, experimental network, scenario distribution, complete baseline suite, optimizer protocol, reference mapping, and quantitative acceptance rules.
- **Unavailable today:** the lane-local storage/accessibility and order-conditioned service capabilities needed to run the complete task.

The appropriate next step is to formulate and approve a downstream-task review protocol. That review should compare candidate task families and extract their objective, control, scenario, baseline, and evaluator conventions before any roadmap or methodology document is amended.
