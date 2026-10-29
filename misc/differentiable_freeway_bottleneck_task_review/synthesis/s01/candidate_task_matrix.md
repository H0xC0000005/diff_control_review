# Candidate task matrix

Decision update: **candidate A selected after N1 discussion**. This matrix
records the accepted working scope, not approved model equations or experiments.

| Criterion | F1 — speed advisory/VSL | F2 — coordinated ramp metering |
|---|---|---|
| Operational definition | **Supported.** Continuous, bounded speed targets upstream of a fixed exogenous lane reduction. | **Supported.** Continuous metering rates with ramp storage, queue override, and fairness constraints. |
| Strong baseline | **Supported.** B0 homogeneous link aggregate; B1 aggregate multiclass/compliance. | **Supported.** ALINEA/fair feedback, first-order and multiclass adjoints, nonlinear MPC. |
| Resolution-sensitive gap | **Qualified.** Lane/lateral interaction can matter, but matched control-ranking failure is not yet proven. | **Unsupported.** No supported lane/order omission that changes rankings was found. |
| Minimum-state isolation | **Qualified.** Sequential B0 → B1 → B2 lane-group multiclass ladder. | **Unsupported.** No justified state beyond aggregate/multiclass/storage/fairness. |
| Derivative correctness | **Qualified.** Discretize B0–B2; compare autograd/adjoint directional derivatives with central differences away from events. | **Supported.** Direct discrete-adjoint predecessors. |
| Gradient usefulness | **Qualified.** Same continuous perturbations/rankings can be replayed in a fixed-seed microscopic evaluator. | **Qualified but unmotivated.** Technically feasible; lacks a resolution hypothesis. |
| Value and novelty | **Qualified.** Only resolution-dependent cross-fidelity gradient usefulness is plausibly distinct. | **Unsupported for this question.** Generic differentiable ramp optimization is established. |
| Evidence/execution feasibility | **Supported.** Open primary sources and open microsimulation route exist; calibration burden remains. | **Supported.** Extensive methods and evaluators exist. |
| Outcome interpretation | **Supported.** B0 equivalence, B1 sufficiency, B2 benefit, or no transfer are all informative. | **Supported.** Negative result is clear: no selective-discreteness case. |
| Stop result | No stop yet; novelty and minimum-state proof remain full-review gates. | **Macro-sufficiency and insufficient-novelty stops triggered.** |

## Narrowed F1 task carried to the gate

**Single novelty target:** minimum retained information needed for useful
cross-fidelity speed-advisory sensitivities, including conditions of simpler-
model sufficiency. Novel VSL algorithms, new compliance/lane-change theory, and
new gradient estimators are not separate promised contributions. The recommended
full-review priorities are predecessor veto and decision-gap/evaluator
feasibility first, then the state ladder, deterministic derivative contract, and
matched usefulness evidence. See Gap 8 in the findings report for boundaries;
no full-review execution or implementation is authorized by this clarification.

- **Disturbance:** fixed temporary or permanent lane closure/lane-drop topology;
  closure and reopening times are structural scenario inputs.
- **Action:** the same piecewise-constant continuous link-level advice schedule
  and feasible bounds/update limits across B0/B1/B2. B2 applies the shared advice
  to its lane groups. Lane-specific actions are a separate, unapproved extension,
  not part of the primary state-resolution comparison. Sign/display quantization
  is a later sensitivity, not differentiated.
- **Population:** human advisory compliance classes are primary. Direct
  vehicle-specific CAV commands are a distinct actuator and excluded.
- **Baseline ladder:** B0 link-aggregate homogeneous capacity drop; B1
  link-aggregate multiclass/compliance; B2 lane-group multiclass with aggregate
  lateral transfer. Exact vehicle order, gaps, and microscopic maneuvers are not
  retained unless later evidence explicitly reopens the minimum-state choice.
- **Objective/evaluation:** common population and horizon; total time/delay,
  bottleneck outflow, and queue clearance, with speed variation/safety proxies
  and residual terminal queue reported as metrics or guardrails.
- **F4:** temporary-closure cases continue after reopening until clearance or a
  declared horizon, so a controller cannot win by moving delay outside the
  evaluation window.
- **Gradient contract:** check differentiated B0–B2 discretizations against
  central finite differences away from branch/event boundaries; evaluate the
  same feasible perturbations and action rankings in a calibrated, fixed-seed
  microscopic car-following/lane-changing model.
- **User clarification — avoid additional probability/hybrid sensitivity:**
  prioritize deterministic continuous traffic-mass equations, fixed exogenous
  compliance cohorts, and fixed closure schedules. Ordinary active-constraint
  kinks are distinct from control-dependent probability redistribution across
  discrete outcomes and hybrid event-time/reset sensitivity requiring saltation
  or comparable corrections. If either additional mechanism is
  indispensable, reopen the derivative contract, establish why adequate
  continuous/deterministic alternatives are unavailable, and obtain approval
  for dedicated gradient-fidelity and approximation/bias-variance evidence.
  Fixed evaluator seeds are not a substitute for this contract.
