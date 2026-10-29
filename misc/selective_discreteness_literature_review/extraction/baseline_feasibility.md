# R6 baseline-feasibility assessment

Date: 2026-09-07  
Scope: approved nearest-predecessor set

“Executable” means that a usable implementation is identifiable; it does not mean that its task, physics, or numerical budget is already matched to this project. Final baseline requirements remain an R8 synthesis decision.

| Record | Feasible comparison role | Matching requirements | Main value | Principal obstacle | R6 recommendation |
|---|---|---|---|---|---|
| R0003 Wright partial FIFO | equation/reference implementation | same node demands, supplies, turns, priorities, and lane-derived restriction intervals | tests exact order against aggregate partial blockage | calibrating intervals fairly | required structured aggregate comparator |
| R0005 COS | equation/reference implementation | same cycle, stages, saturation flows, and boundary states | tests signal/node service independently of mesoscopic state | iterative COS operator differs from current baseline | use as service reference, not full external simulator |
| R0006 multilane node | equation/reference cases; faithful implementation potentially substantial | same lane permissions, sending flows, priorities, and receiving supply | strongest endogenous lane-allocation alternative | variational equilibrium and aggregate link receiving state | required equation/reference comparator; executable baseline if effort is proportionate |
| R0007 individual LTM | executable open implementation plus matched reference cases | same LTM parameters, demand, routes, time step, and node rules | isolates integer individual tracking versus divisible ordered mass | code/API and signal support may not align | required forward comparator; gradient comparison not applicable |
| R0008 turn-level queue | equation/reference implementation | same link geometry, turn demands, free-flow assumptions, signals, and spillback cases | tests whether movement queues suffice without exact order | extra time-varying-speed feature must be neutralized | required structured queue comparator |
| R0009 lane-group blockage | conceptual plus equation/reference cases | same lane groups, pocket lengths, demand, phases, and objective | tests functional value beyond established lane-group storage/blockage | legacy optimization and no ready matched implementation | required equation/behavior comparator; not necessarily full executable baseline |
| R0012 differentiable agent model | conceptual; reproduction only if source and task can be matched | same demand, objective, signal variables, smoothing scale, and optimizer budget | contrasts surrogate smoothing of discrete agent logic | different microscopic physics and smoothing choices | required conceptual differentiability comparator |
| R0013 differentiable hybrid | executable open implementation | matched small network, objective, signal controls, resolution region, and optimizer budget | compares selective semantics with micro/macro hybridization | different lane/vehicle physics and conversion machinery | candidate executable external baseline on a small case |
| R0014 differentiable LTM | executable open implementation | freeze routes or match route model; same LTM/node/signal physics and objective | strongest scalable differentiable macro baseline | toll/route-choice task differs; signal interface may need adaptation | required executable or faithfully reimplemented macro baseline |
| R0021 LIFT | executable case-study implementation plus equation cases | same FD, vehicle demand, signals, routes, and network | compares event/vehicle mesoscopic fidelity and cost | open code is limited to a case-study network; no gradients | required richer forward comparator where feasible |
| R0022 SUMO/LTM alternative | equation/reference cases | same signal corridor, bottleneck, FD, and demand | tests discrete-time LWR mesoscopic behavior and SUMO weaknesses | recent preprint; implementation maturity unclear | retain as equation and scenario comparator |
| R0025 Gao turning-lane queues | equation/reference cases | same lane capacities, turn demand, physical queue geometry, and FIFO domain | tests lane-level FIFO and physical queues without proposed ledger/grid | older hybrid solution procedure and limited scaling evidence | required behavior/reference comparator |
| R0027 LNCTM | equation/reference implementation | same commodities, split ratios, node topology, FD, and capacity assumptions | tests continuous commodity identity without realized order | optional hysteresis/capacity-drop features complicate matching | required commodity-state comparator |

## Feasible minimum ladder emerging from R6

1. **Matched homogeneous differentiable macro:** project macro baseline and/or R0014-compatible LTM behavior.
2. **Structured aggregate queue:** at least R0003-style partial FIFO or R0008-style turn queues; otherwise gains could be attributed merely to movement resolution.
3. **Lane/storage reference:** R0006, R0009, or R0025 equation/reference cases; otherwise lane blockage is not isolated from order.
4. **Identity/order mesoscopic reference:** R0007 and, where feasible, R0021; neither supplies gradients, but both test forward semantics and computational trade-offs.
5. **Differentiable rich-state comparator — deferred second choice:** R0013 may support a small hybrid ablation only after Question B defines a task that makes it meaningful. It is not part of the approved minimum ladder and cannot be the standalone experiment.

No single external paper supplies the whole baseline. A causal internal ablation ladder remains necessary, with external papers used according to the comparison role they can support faithfully.
