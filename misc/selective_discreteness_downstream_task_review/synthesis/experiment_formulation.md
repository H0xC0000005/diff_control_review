# T6 task-facing scientific contract

Date: 2026-09-10  
Status: Approved at T6 on 2026-09-14 for V0–V4. V5/I1 excluded; numerical defaults retain their stated status. The historical approval questions below are resolved by `../discussion/t6_closure_record.md`.

## Answer-first contract

The accepted task family allocates continuous effective signal service among four protected movement groups at a regular four-leg junction. The symmetric default assigns separate north–south and east–west through/right and protected-left service groups. The experiment asks whether selective order/access state changes forward outcomes and useful green-allocation sensitivities after finite storage, structured movement queues, and lane-aware aggregate alternatives are controlled.

The formal equations, units, derivative definition, objective, and result logic are rendered in `experiment_formulation_formal.pdf`; the editable source is retained beside it. Variant layouts and traffic allocation are defined in `primary_green_allocation_suite.md`. Baseline realization and fairness rules are defined in `baseline_realization_matrix.md`.

## What is fixed now

- effective-service rather than executable phase-timing semantics;
- fixed topology with four interpretable protected service groups;
- continuous vehicle-equivalent mass and fixed structural routes/order during differentiation;
- one rotationally symmetric four-leg controlled junction; a separate conditional two-node integration test remains outside the primary suite;
- a clearance-complete total-time/delay objective shared by every model and evaluator;
- variants V0–V4 and their causal ordering;
- representation and optimizer comparisons as separate axes;
- forward correctness, derivative correctness, internal optimization, and external usefulness as separate evidence claims; and
- equivalence and negative results as valid outcomes.

## Proposed defaults pending implementation evidence

These are working choices needed to make the experiment concrete. They are not yet fixed numerical or implementation requirements. Each should be checked against the completed simulator interfaces and small calibration runs before an executable experiment plan freezes it.

### D1 — valid green allocations through an internal simplex parameterization

The traffic-facing decision is the physical service fraction assigned to each of four fixed groups: north–south through/right, north–south protected left, east–west through/right, and east–west protected left. Those fractions must respect any minimum allocation and sum to one common available-service budget. The proposed optimizer therefore adjusts an internal dimensionless vector `z` of unrestricted scores, called logits. A softmax/simplex map transforms `z` into the physical vector `g`: minimum allocations are reserved first, and the remaining service is divided among the four groups. Adding the same constant to every logit does not change `g`, so an implementation may center `z` or fix one reference logit to remove this redundant internal coordinate.

This default prevents an optimizer step from proposing negative service or exceeding the common budget, while keeping the optimization path differentiable. Results must always be reported as physical phase fractions, not logits. A direct constrained optimizer may replace this parameterization if it gives a clearer or numerically better implementation without changing the physical feasible set.

### D2 — constant effective service followed by a common clearance period

During the declared control and demand-release interval, one effective-service allocation remains constant. After demand release ends, every model receives the same fixed clearance policy and continues until all admitted traffic and source-queued traffic has completed.

This creates a simple fixed-time allocation problem while avoiding a short horizon that rewards a model for leaving vehicles just outside the measured network or trapped at the terminal time. The eventual experiment plan must set a maximum clearance duration and treat failure to clear as a censored or failed run rather than silently truncating the objective. This default may be revised if calibration shows that a different model-common terminal treatment is more stable and equally measurable.

### D3 — total system time as the primary objective, with delay as its interpretation

The primary score accumulates all vehicle-equivalent mass still waiting at sources or physically present inside the modeled network over time. Network mass includes moving traffic as well as queued traffic. This area under the number-in-system curve equals the sum of source-to-destination elapsed times when every released trip completes; its units are vehicle-seconds. It is therefore total system time, not merely total queue time. Because the clearance rule requires every trip to finish, subtracting the same scenario's free-flow travel time produces total delay without changing the ranking or gradient with respect to green allocation.

Total system time is proposed because it counts source waiting, internal queues, spillback, and incomplete progress consistently across representations. Delay is reported alongside it because it is easier to interpret operationally. Queue length, throughput, blocked mass, and bay occupancy remain mechanism diagnostics rather than alternative primary objectives. This choice should be reconsidered only if the richer evaluator cannot reproduce the same population and time accounting reliably.

### D4 — three demand regimes defined relative to common capacity

Each layout is tested under undersaturated, near-capacity, and oversaturated demand. These labels will not be assigned from arbitrary absolute flow values. They will be calibrated against the same physical saturation-flow, storage, and downstream-supply assumptions used across the compared models.

The three regimes have different purposes: undersaturation checks ordinary agreement, near-capacity cases expose sensitivity to allocation and ordering, and oversaturation activates persistent queues, bay overflow, and spillback. Exact flow ranges remain open until the physical interfaces exist because premature numbers could accidentally make a nominal regime behave differently across models. Calibration may adjust the ranges, but it may not delete a difficult regime merely because results are unfavorable.

### D5 — keep aggregate-matched order pairs together when splitting scenarios

V1 and V3 use paired scenarios with identical aggregate demand, movement totals, geometry, initial aggregate occupancy, and downstream supply but different movement order or realized accessibility. Both members of such a pair must be assigned together to the development/tuning set or together to the held-out set.

This prevents the optimizer or experiment designer from seeing one ordering and then being evaluated on its deliberately paired counterpart, which would leak scenario structure and exaggerate generalization. Held-out splitting should therefore operate on pair or scenario-family IDs rather than individual runs. The exact split proportions remain open, but the no-pair-splitting rule is expected to remain unless later evidence shows a stronger grouping unit is required.

### D6 — SUMO as a replicated richer forward evaluator

SUMO is the proposed external evaluator because it can represent explicit lanes, turning bays, route-specific vehicles, queueing, and executable signal programs. Each selected scenario/action is evaluated under several predeclared microscopic random seeds, using the same seeds for every compared action within that scenario.

SUMO does not provide the reference gradient. It tests whether directions or allocations proposed by the differentiable models cause the predicted objective change in a richer traffic realization. Before use, T6's effective-service fractions need one documented, common mapping to a SUMO phase program, and network geometry, demand, storage, capacities, and measurement windows must be reconciled. SUMO may be replaced only if another evaluator supports the same mechanisms and a more credible common intervention mapping.

### D7 — calibrate numerical values only after interfaces exist, then freeze them

Exact link and bay lengths, demand rates, horizon and clearance cap, perturbation size, finite-difference step, seed count, numerical tolerances, optimizer settings, and evaluation budgets are intentionally not guessed in this review. Small reference and calibration runs should first identify physically meaningful regimes, stable derivative neighborhoods, and feasible computational costs.

This is a timing decision, not permission for post-hoc tuning. The later implementation or experiment plan must record the calibration method, freeze the resulting values before confirmatory or held-out evaluation, and preserve failed or negative regimes. Any calibrated value that changes task semantics—rather than merely instantiating this contract—must return to the appropriate user gate.

## Evidence sequence

1. Verify geometry, mass conservation, service constraints, and V0 macro equivalence.
2. Validate model derivatives against central finite differences on stable active-set signatures.
3. Compare feasible directional predictions across B0–B3 and selected richer references.
4. Evaluate identical small service reallocations in the richer evaluator.
5. Only then run matched-budget optimization within each representation.
6. Evaluate final actions on held-out scenarios and richer-simulator seeds.

## Formal gradient meaning

For every primary variant, the scalar function `f` is clearance-complete total system time and the scientific input `x` is the physical four-group effective-service allocation `g`. Thus `df/dx` means the change in vehicle-seconds caused by a marginal feasible reallocation of physical service. The optional `z` is only an internal logit coordinate used to generate valid `g`; it is not `x`. Cross-model gradients are compared after mapping back to physical service fractions or as feasible directional derivatives.

The common propagation chain is physical service allocation → movement capacity → realized movement discharge → next traffic state → source and network occupancy over time → total system time. The formal PDF specifies the state-sensitivity recursion and each added variant path:

- V0: direct movement service and aggregate state;
- V1: continuous ordered-prefix eligibility and residual head state;
- V2: bay discharge, occupancy, available storage, admission, and spillback;
- V3: V2 plus exact order-conditioned realized accessibility; and
- V4: a fixed scenario-bank average of the applicable V1–V3 gradients.

Structural order, route/movement labels, permissions, topology, and branch choices are not differentiated. Continuous masses within a fixed prefix/active-set signature are differentiated. Event-boundary cases are reported separately rather than smoothed or assigned an invented derivative.

## Literature trace for the contract

- T0005 and T0007 support LTM-based effective-green allocation and total-time objectives, while T0007 supplies the nearest aggregate turn-queue predecessor.
- T0011–T0013 delimit continuum service from executable on/off timing, particularly under spillback.
- T0008–T0010 support lane-group blockage, finite short-lane storage, and physical turn queues.
- T0014, T0015, and T0030 motivate structured movement/partial-FIFO and lane-aware aggregate baselines.
- T0017 supplies an identity/order forward reference; T0001–T0003 supply differentiable-simulation contrasts.
- T0022, T0024, T0027, T0028, and T0032 support optimizer separation, scenario variation, held-out evaluation, and richer-simulator realization.

These sources support the surrounding task and comparison architecture. They do not establish in advance that selective order will be beneficial.

## Claim and failure logic

- **Forward claim:** the representation predicts traffic quantities under the declared task; it says nothing yet about gradients.
- **Derivative claim:** AD agrees with stable-regime directional finite differences; it says nothing yet about external usefulness.
- **Selective-information claim:** V3 aggregate-matched pairs differ in the richer reference and are distinguished more faithfully by B3 than B0–B2.
- **Optimization claim:** within a fixed model and budget, its gradients improve its own objective more reliably than matched derivative-free search.
- **Usefulness claim:** B3 directions or final actions improve or predict change in the richer evaluator more reliably than comparison representations.
- **Equivalence result:** if B2 matches B3 and the richer evaluator within declared uncertainty, lane/storage aggregate state is sufficient in that regime.
- **Negative result:** if B3 derivatives are correct internally but do not transfer, differentiability is valid but the representation/task combination has not shown downstream value.

## Explicit nonclaims

The contract does not establish deployable signal timing, network-wide coordination, route-choice response, actuated control, stochastic policy learning, microscopic trajectory fidelity, or universal advantage of exact order.

## T6 approval questions

1. Confirm V0–V4 as the complete primary variant set with the intentions and dependency order stated in `primary_green_allocation_suite.md` and the formal gradient paths stated in the PDF.
2. Confirm the detailed realization of the user-selected rotationally symmetric four-leg, four-service-group default and its symmetric traffic-allocation conventions.
3. Confirm that the former V5 is removed from the primary suite and retained only as conditional post-suite integration/network test I1.
4. Approve effective-service semantics and the clearance-complete total-time/delay objective contract.
5. Approve the baseline realization matrix, its literature/adoption anchors in `literature_adoption_matrix.md`, and the separation of representation versus optimizer comparisons.
6. Approve the staged forward/derivative/perturbation/optimization/external-usefulness evidence sequence.
7. Approve leaving numerical geometry, demand, horizon, seed-count, tolerance, optimizer, and budget values as defaults to calibrate and freeze in their implementation/experiment plans.

Approval closes T6 for Part I and authorizes T7 to audit its project impact. It does not resolve the unapproved Part-II future-task map, amend project files, or authorize implementation.
