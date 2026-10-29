# T6 baseline realization and fairness matrix

Date: 2026-09-10  
Status: Approved at T6 on 2026-09-14 for V0–V4; V5/I1 excluded. Implementation choices and calibration remain subject to their stated future gates.

## Shared rule

Every model receives the same scenario, effective-service allocation, objective window, demand/routes, downstream supplies, and optimization/evaluation budget. A missing mechanism is reported as a capability boundary. It is not repaired by changing the task or providing privileged state.

## Literature and adoption overview

The baseline roles are not unsupported abstract categories. Their equation, algorithm, software, and validation anchors are summarized below and audited in detail in `literature_adoption_matrix.md`.

| Role | Principal anchors | Intended adoption route |
|---|---|---|
| B0 homogeneous macro | T0001 differentiable LTM; T0005 LTM-MPC; T0011 COS; T0012 continuum signal approximation | Retain project LTM/node backbone; transcribe signal/task equations and reuse AD/reference-test patterns |
| B1 structured queue/partial FIFO | T0015 turn-level queue transmission; T0014 partial-FIFO restrictions; T0007 signal turn queues; T0010 physical turn queues | Choose and faithfully transcribe one principal queue formulation; keep alternative restrictions explicit |
| B2 lane/storage aggregate | T0030 multilane equilibrium node; T0008 lane-group blockage; T0009 overflow; T0010 turning-lane storage | Transcribe lane-allocation algorithm and one explicitly sourced finite-storage augmentation |
| B3 selective order | T0017 order-tracking LTM; T0001/T0003 AD engineering; B0–B2 component sources | Project-owned documented composition; no single-paper or drop-in implementation claim |
| R1 ordered forward reference | T0017 individual tracking; T0016 LIFT; T0018 MESCOP; T0008 blockage | Independent bounded reproduction or reference fixture; never a gradient baseline |
| R2 microscopic evaluator | T0032 SUMO documentation; T0025 `sumoITScontrol`; T0022/T0027 evaluation protocols | Direct SUMO reuse through TraCI/libsumo plus project-owned scenario and metric wrapper |
| Optimizer comparison | T0024 TuRBO; T0002 gradient-guided SBO; T0022 multi-simulator optimization | Adopt optimizer/evaluation logic outside the traffic-model implementation |

The important engineering distinction is that **published equations are the primary adoption unit for B0–B2**, while **maintained software is directly reused for R2**. Public differentiable repositories are engineering references, not automatically compatible baseline implementations.

## Representation axis

| Role | Realization under shared task | State unavailable by design | Allowed adaptation | Gradient role | Expected variant boundary |
|---|---|---|---|---|---|
| B0 homogeneous differentiable macro | LTM links and aggregate node turning proportions; phase fractions scale movement capacities | Lane occupancy, finite bay, exact order/access | Match total capacity/storage where meaningful; no fitted blockage factor from test outcomes | Exact/piecewise AD baseline | Must match V0; expected to alias V1–V3 aggregate-matched pairs |
| B1 structured movement/partial-FIFO queue | Turn queues or movement classes plus declared partial-FIFO restrictions | Exact realized within-lane order and access path | Literature-faithful restriction parameters fixed without held-out tuning | Gradient if implementation supports it; otherwise forward ablation | Can explain movement queues and some V1 blockage, but may alias exact pairs |
| B2 lane/storage-aware aggregate | Explicit lanes/bay storage and aggregate movement composition or equilibrium allocation | Exact ordered prefix and realized accessibility history | Same geometry/permissions/storage; neutral aggregate allocation rule fixed before evaluation | Preferred differentiable ablation; forward-only if necessary | Should match V2 if storage suffices; V3 tests its residual limitation |
| B3 proposed selective-order model | Continuous mass plus exact ordered semantic metadata and realized lane accessibility | No microscopic car following/lane-change trajectories | Only approved model semantics; no scenario-specific correction | Primary exact/piecewise AD model | Tested across V0–V4 |
| R1 identity/order mesoscopic forward reference | Event/vehicle/packet order with physical lanes where compatible | Exact same continuous-mass derivative path | Calibrate common FD/capacity/storage; preserve its native order mechanism | Forward reference only | Checks V1–V3 causal ordering and service |
| R2 microscopic evaluator | SUMO network, routes, lanes, signals, and repeated seeds | Direct identity with continuum effective service | A single predeclared realization mapping; common scenario bank and objective | External forward evaluation only | Tests perturbation and optimized-action usefulness |

## Optimizer axis

Optimizer comparisons are run within a fixed model realization. They do not substitute for the representation ladder.

| Comparator | Same inputs required | Purpose |
|---|---|---|
| Model gradient | Same parameterization, initialization, objective calls, and stopping budget | Test benefit of available derivatives |
| Central finite difference | Same physical feasible directions; double precision in small cases | Validate local derivative correctness, not serve as the scalable optimizer |
| Derivative-free trust-region/BO or direct-search method | Same model, feasible set, initialization policy, and counted simulation budget | Determine whether optimization gains arise from gradients rather than extra evaluations |
| Random feasible perturbations | Same local radius and scenario bank | Calibrate whether a reported direction beats chance |

## Fairness rules

1. Do not tune a baseline's blockage parameter on held-out outcomes.
2. Report when a baseline cannot represent two aggregate-matched states distinctly.
3. Keep objective observations identical even if internal state differs.
4. Count simulator evaluations, derivative evaluations, wall time, and failures separately.
5. Compare representation quality first with fixed actions and perturbations; compare optimizers only afterward.
6. Use identical scenario IDs and fixed order/seed realizations for paired comparisons.
7. Evaluate every candidate action under the same richer-evaluator mapping.
8. Do not call R1 or R2 a gradient baseline.
9. Record the adoption class, exact source equation/code version, adaptation, and license for every implemented role as required by `literature_adoption_matrix.md`.

## Variant coverage

| Variant | Required roles |
|---|---|
| V0 | B0–B3; R1 optional conformance check |
| V1 | B0–B3 and R1; R2 for selected pairs |
| V2 | B0, B2, B3, R1; B1 when its equations support storage |
| V3 | B0–B3, R1, and R2 for selected pairs |
| V4 | B0–B3 and R2; R1 on a bounded diagnostic subset |

The conditional corridor test I1 receives its own baseline/evaluator coverage decision if it is later opened; it is not part of the T6 primary matrix.
