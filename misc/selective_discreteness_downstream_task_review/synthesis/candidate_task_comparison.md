# T5 candidate-task synthesis and comparison

Date: 2026-09-10  
Status: Part-I Candidate A selected; Part-II map returned for further review

## Answer-first recommendation

Select **Candidate A: fixed-topology continuous effective-service allocation at one junction, expressed as one diagnostic suite**, as the primary task family.

The suite should keep one control variable, objective family, feasible set, scenario representation, and comparison contract while adding traffic mechanisms in layers:

1. aggregate-equivalence;
2. finite turn-pocket storage;
3. aggregate-matched order/accessibility;
4. combined and held-out variation.

This is the smallest task that directly tests the project's selective-discreteness hypothesis without importing unapproved phase-switching semantics. Candidate B, directly realizable fixed-time timing, should be the first later realization task. Candidate C, a short arterial, should be the first spatial extension after the junction mechanism is established. Candidate D, gradient-direction perturbation, is a required diagnostic inside Candidate A rather than a competing primary task. Candidate E, multi-fidelity simulation optimization, is an evaluation/optimization architecture rather than the scientific task itself.

## Necessary selection criteria

A primary task must satisfy all six necessary conditions:

- activate storage and order/access mechanisms;
- use a continuous in-scope control;
- permit the same traffic objective across representations;
- permit homogeneous, movement-queue, lane/storage, and selective-order realizations;
- separate derivative correctness from decision usefulness; and
- admit negative or equivalence findings.

Parsimony, operational immediacy, network breadth, and empirical familiarity discriminate among otherwise viable candidates but do not override these conditions.

## Comparison table

| Candidate | Control/output meaning | Target mechanisms | Shared baseline contract | Richer evaluation | Scope burden | T5 disposition |
|---|---|---|---|---|---|---|
| A. Junction effective-service allocation | Continuous phase/movement service fractions over a fixed horizon; not claimed as executable intervals | Pocket storage, access, order, blockage | Strong across all four representation roles | Same service intervention in richer forward model; SUMO mapping is a later specification detail | Low–moderate | **Recommend as primary** |
| B. Junction realizable fixed-time timing | Executable green durations with cycle, minimum green, yellow/all-red, and fixed phase order | Same as A plus within-cycle timing | Possible, but requires every model to share added timing semantics | Direct SUMO phase program | Moderate–high and partly outside current semantics | First later realization task |
| C. Short-arterial green allocation | Effective service or timing at two or more interacting junctions | Downstream blockage and interjunction spillback | Feasible but coupling may obscure local mechanism attribution | Natural SUMO corridor evaluation | Moderate–high | First spatial extension |
| D. Gradient-direction perturbation | Small feasible changes to A's green vector | Sensitivity sign/direction near chosen states | Excellent | Evaluate identical perturbations externally | Low | Required diagnostic within A, not standalone primary |
| E. Fixed-bank multi-fidelity optimization | Optimization workflow combining project and richer simulators | Transfer and model discrepancy, not a new traffic mechanism | Depends on an already selected task | Built into method | High | Later evaluation architecture |

## Candidate A — continuous effective-service allocation at one junction

### Problem statement

Allocate a fixed amount of effective signal service among fixed phases or compatible movement groups. Compare how different traffic representations predict the objective and its sensitivity when lane storage and the accessibility of ordered movement mass alter realizable discharge.

### Assumed model-chain function

The green-allocation vector modifies node service capacities. Long-link aggregate propagation supplies arrivals; movement and lane representations determine which queued mass can reach and use that service; the objective is computed from the resulting traffic trajectory. Topology, routes, movement labels, phase order, and scenario order remain fixed during differentiation.

### Core specification still reserved for T6

T5 selects the family, not the exact equation. T6 must freeze parameterization, objective and units, horizon and terminal treatment, scenario geometry, constraint handling, baseline realization, gradient tests, richer-evaluator mapping, and result interpretation.

### Pros

- It is the minimum task that activates the proposed representation advantage.
- It matches the current continuous fixed-time service boundary and does not require categorical control.
- All representation baselines can receive the same control and objective.
- Aggregate-matched paired states can isolate information carried by order/accessibility.
- Hand cases, finite differences, optimization, and held-out evaluation can be layered without changing the task.
- A null result is meaningful: structured aggregate state may be sufficient.

### Cons

- Effective fractions are not directly deployable phase intervals.
- A richer simulator needs a declared mapping from service fractions to an evaluation intervention.
- One junction does not establish network-wide value or offset coordination.
- Care is needed to avoid designing paired states that trivially favor the proposed representation.

### Dependencies and scientific consequence

The task depends on the Milestone 2 lane/storage/order interface and a later signal-service component. Selecting it fixes the first claim at the service-allocation level; it does not authorize cycle, offset, clearance, or switching dynamics.

## Candidate B — directly realizable fixed-time timing at one junction

### Problem statement

Optimize executable phase durations under fixed sequence, cycle accounting, minimum greens, and yellow/all-red requirements.

### Assumed model-chain function

The decision vector creates explicit within-cycle phase intervals. Traffic propagation must respond to on/off service timing rather than only average capacity scaling, and every baseline and evaluator must apply the same timing program.

### Core gap

The current project does not yet fix startup/clearance lost time, within-cycle switching behavior, or a realization mapping. The continuum-signal literature also warns that service averaging can diverge under spillback.

### Pros

- Strongest operational interpretation and direct SUMO transfer.
- Avoids ambiguity about whether an optimized action can be implemented.
- Can expose timing effects hidden by average service.

### Cons

- Adds scientific mechanisms not required to test selective order/accessibility.
- Makes cycle and clearance assumptions potentially dominate the local representation comparison.
- Raises nonsmooth event and baseline-matching burdens.
- Risks changing Milestone 2/3 scope before the simpler representation hypothesis is tested.

### Dependencies and scientific consequence

Requires an approved signal-realization contract. Promoting it now would change rather than merely instantiate the current model boundary.

## Candidate C — short-arterial green allocation

### Problem statement

Allocate signal service across a small sequence of interacting junctions so local lane blockage affects downstream discharge and upstream spillback.

### Assumed model-chain function

The task extends Candidate A with propagation and coupling between at least two controlled nodes. The same objective and feasible action meaning must be retained at every representation level.

### Core gap

The evidence supports arterial relevance, but does not show that network coupling is needed to identify the first-order benefit of exact local order rather than finite aggregate storage.

### Pros

- More representative of practical coordination and spillback.
- Exercises the intended local-refinement/long-link architecture.
- Supports strong richer-simulator cases.

### Cons

- Interjunction timing, propagation, and boundary demand can confound the local mechanism.
- Larger scenario and calibration burden.
- Failure is harder to diagnose than at one junction.

### Dependencies and scientific consequence

Best treated as the first extension after Candidate A establishes component-level causal behavior. It should reuse, not redefine, the accepted task contract.

## Candidate D — gradient-direction perturbation

### Problem statement

At fixed diagnostic states, compare predicted directional derivatives and evaluate identical small feasible green reallocations in each model and a richer evaluator.

### Pros

- Cleanly separates derivative direction from optimizer behavior.
- Low computational and implementation burden.
- Can expose incorrect signs even when objective values are close.

### Cons

- Does not by itself show useful optimization over a meaningful budget.
- Results can be local and event-boundary dependent.
- Without the enclosing task, the perturbation has no independent traffic purpose.

### Dependencies and scientific consequence

Include it as an evidence layer inside Candidate A before full optimization. Do not select it as a standalone project task.

## Candidate E — multi-fidelity optimization workflow

### Problem statement

Use the differentiable model to propose actions and a richer simulator to evaluate, correct, or select them over a fixed scenario bank.

### Pros

- Directly addresses model mismatch and external usefulness.
- Can exploit inexpensive gradients while retaining higher-fidelity evaluation.
- Supports robust held-out assessment.

### Cons

- Conflates optimizer architecture with representation value if introduced too early.
- Requires substantially more budget and tuning.
- Cannot define the traffic task until A, B, or C is selected.

### Dependencies and scientific consequence

Retain as a later optimization/evaluation design. T6 should require a simpler one-way richer-evaluator test first.

## Recommended diagnostic layers within Candidate A

| Layer | Fixed task | Mechanism changed | Required interpretation |
|---|---|---|---|
| A0 aggregate equivalence | Same service allocation and objective | Local storage/order inactive or homogenized | Models should agree within tolerance; disagreement is a conformance failure |
| A1 finite storage | Same task | Finite pocket/storage activated, order homogenized | Isolates whether storage-aware aggregate state is sufficient |
| A2 order/access | Same task and aggregate totals | Ordered route/movement arrangement changed | Tests added value of selective order beyond aggregate queues/storage |
| A3 combined held-out | Same task | Demand, initial queues, pocket length, and order varied | Tests robustness and prevents one constructed state from carrying the claim |

Each layer should include forward comparison, central finite-difference checks where differentiable, the Candidate-D perturbation test, and—only after those pass—matched-budget optimization.

## Effective-service versus realizable-timing decision

The primary T5 recommendation is explicitly **effective-service allocation**. The output is a continuous phase/movement service allocation under fixed topology, not an executable schedule. This boundary is scientifically honest and parsimonious.

Operational transfer remains required, but it must be labeled as evaluation through a documented realization mapping or deferred until Candidate B is opened. A positive result at the service layer cannot be reported as deployment-ready timing.

## T5 approval request

Approve or revise:

1. Candidate A as the primary task family at the effective-service layer;
2. A0–A3 as one diagnostic progression under a shared task, not separate tasks;
3. Candidate D as a mandatory diagnostic within A rather than the primary task;
4. Candidate B as the first later realization task and Candidate C as the first spatial extension;
5. Candidate E as a later evaluation architecture rather than a task family; and
6. the boundary of the later-task map in `future_task_map.md`.

Approval closes T5 and authorizes T6 to formulate the exact scientific task contract. It does not approve implementation or amend project documents.
