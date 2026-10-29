# T5 bounded future-task map

Date: 2026-09-10  
Status: not approved; further literature review and discussion required

The user found the present classes insufficiently promising because each carries substantial limitations. The table is retained as a provisional inventory, not an accepted future-task hierarchy. It must be revisited with additional task-specific literature before any class is recommended or promoted. This unresolved Part-II work does not block T6 formulation of the separately accepted Part-I Candidate A.

This map records credible later uses without enlarging the current project. None is authorized for implementation, and none is part of the recommended primary task.

| Priority | Later task | Traffic purpose and decision | Added derivative/model requirement | Relation to selective discreteness | Plausible baseline/evaluator | Reason deferred | Promotion evidence |
|---|---|---|---|---|---|---|---|
| 1 | Realizable fixed-time signal timing | Choose executable phase durations under fixed sequence | Within-cycle switching, cycle accounting, minimum green, yellow/all-red, lost time | Tests whether order/access gradients survive physical timing realization | Continuum/on-off signal models; SUMO | Adds unapproved signal semantics | Candidate A succeeds or reveals a realization-sensitive gap; common mapping is validated |
| 2 | Short arterial coordination | Allocate service/timing across interacting junctions | Multiple local zones, link travel time, spillback coupling, possibly offsets | Tests whether local detail remains useful with aggregate long-link propagation | LTM-MPC, lane-blockage models, SUMO corridor | Network coupling can obscure the first causal test | Junction suite passes; paired corridor scenarios show a nontrivial coupling question |
| 3 | Robust fixed-bank signal optimization | Optimize expected or risk-sensitive performance over demand/order scenarios | Batched scenarios, declared uncertainty distribution, robust objective | Tests whether benefit persists beyond one ordering | Scenario-based traffic-light optimization; replicated SUMO | Requires a stable primary objective and runtime budget | Held-out A3 results show material scenario variation |
| 4 | Multi-fidelity signal optimization | Use mesoscopic gradients with selective richer-simulator calls | Trust-region/discrepancy method and matched evaluation budget | Tests practical use under model mismatch | Multi-simulator optimization, TuRBO, SUMO | Optimizer architecture would confound the initial representation test | One-way transfer evidence establishes informative gradients and manageable mismatch |
| 5 | Continuous parameters of actuated control | Tune thresholds, extensions, or gaps with topology fixed | Event-dependent controller state and differentiated continuous controller parameters | Local queues/order may affect activation and service | Actuated-control simulation, SUMO | Changes controller semantics and nonsmoothness substantially | Fixed-time task closes; a specific parameter has a defensible derivative contract |
| 6 | Offset optimization | Coordinate phase offsets along an arterial | Explicit cycles and within-cycle timing | Local blockage may change progression value | Continuum signal models, SUMO | Meaningless without an approved timing model | Realizable timing and corridor layers are validated |
| 7 | Cycle-length optimization | Select cycle duration with green allocation | Lost/startup/clearance effects so cycle length has physical consequence | Indirect; representation may alter congestion response | Signal-design models, SUMO | Current invariant says cycle is not meaningful without within-cycle effects | Lost-time model is approved and empirically supported |
| 8 | Calibration or demand estimation | Infer continuous traffic/demand parameters from observations | Observation model, identifiability, data and loss specification | Can test whether selective state improves inference | Differentiable DNL, trajectory/count data | Does not directly test downstream control usefulness | Control program closes or a data-backed identification need emerges |
| 9 | Pricing or network design | Optimize tolls or continuous capacity/design surrogates | Route response or design-response semantics | Local blockage may alter network sensitivities | Differentiable LTM, richer assignment/simulation | Pulls in dynamic behavior and broader scope | Separate review shows local selective detail is decision-critical for that intervention |

## Explicitly outside this map's promotion authority

- categorical phase-sequence design;
- dynamic or stochastic route choice as an optimized variable;
- explicit microscopic lane changing or car following;
- reinforcement-learning policy selection;
- autonomous-driving control; and
- unrestricted network-wide lane expansion.

These topics require separate scientific justification and ordinary project change control. Their appearance in literature does not make them planned downstream tasks.
