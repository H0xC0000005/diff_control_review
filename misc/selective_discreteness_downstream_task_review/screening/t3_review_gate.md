# T3 screening and taxonomy approval gate

Status: approved and closed on 2026-09-10  
Date: 2026-09-10  
Completed phases: T1 search pilot and seed handoff; T2 discovery and corpus construction; T3 screening and taxonomy pilot

## Decision summary

The pilot supports the approved TSC-first direction without requiring a methodology change. The 38-record candidate corpus contains:

| Provisional decision | Count | Meaning |
|---|---:|---|
| Include as primary task evidence | 20 | Directly informs the primary task, mechanism, baseline, control realization, or evaluator contract |
| Include as contextual evidence | 8 | Informs a supporting method or later task but does not define the primary experiment |
| Borderline for T4 value check | 3 | Plausibly useful, but retained only if marginal evidence justifies extraction cost |
| Exclude | 7 | Does not materially inform the fixed-time signal/blockage task contract |

The proposed taxonomy separates effective service from realizable signal timing, separates representation value from optimizer value, and treats aggregate equivalence, finite storage, access/order, and held-out combinations as layers of one primary task suite.

## Full screening table

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0001 | *End-to-end differentiable network traffic simulation with dynamic route choice* | Primary | Differentiable aggregate LTM baseline; toll rather than signal task |
| T0002 | *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization* | Primary | Direct AD signal-timing and optimizer comparison |
| T0003 | *Differentiable Hybrid Traffic Simulation* | Primary | Richer differentiable/hybrid signal precedent |
| T0004 | *Differentiable Modeling of Traffic Signals for Gradient-based Parameter Optimization in Microscopic Traffic Simulations* | Exclude | Smoothed microscopic differentiability conflicts with project target; stronger task precedents exist |
| T0005 | *Linear MPC-Based Urban Traffic Control Using the Link Transmission Model* | Primary | LTM-MPC task and computation baseline |
| T0006 | *A Hierarchical Control Framework for Coordination of Intersection Signal Timings in All Traffic Regimes* | Primary | High-level reference versus executable switching |
| T0007 | *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics* | Primary | Recent LTM/turn-queue control intersection |
| T0008 | *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage* | Primary | Direct lane-blockage signal task |
| T0009 | *Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow* | Primary | Short-lane overflow task and CTM verification |
| T0010 | *A Node Model Capturing Turning Lane Capacity and Physical Queuing for the Dynamic Network Loading Problem* | Primary | Physical turning-lane reference |
| T0011 | *The continuous signalized (COS) node model for dynamic traffic assignment* | Primary | Signal-stage/node semantics |
| T0012 | *On the continuum approximation of the on-and-off signal control on dynamic traffic networks* | Primary | Validity limits of averaged signal service |
| T0013 | *Continuum signalized junction model for dynamic traffic networks: Offset, spillback, and multiple signal phases* | Contextual | Later multiphase/offset realization scope |
| T0014 | *On node models for high-dimensional road networks* | Primary | Partial-FIFO structured aggregate baseline |
| T0015 | *A link-based flow model with turn-level queue transmission and time-varying free-flow speed for urban road networks* | Primary | Turn-queue baseline |
| T0016 | *Simulating link-level interrupted flow traffic dynamics and the comparison between different models for urban road networks* | Primary | Richer mesoscopic evaluator/reference |
| T0017 | *A mesoscopic link-transmission-model able to track individual vehicles* | Primary | Identity/order forward reference |
| T0018 | *MESCOP: A Mesoscopic Traffic Simulation Model to Evaluate and Optimize Signal Control Plans* | Primary | Mesoscopic signal-plan precedent |
| T0019 | *Network Traffic Control Based on a Mesoscopic Dynamic Flow Model* | Contextual | Per-intersection method only; network control excluded |
| T0020 | *Optimization of Actuated Traffic Signal Plans Using a Mesoscopic Traffic Simulation* | Exclude | Actuated wrapper; reusable MESCOP formulation already covered by T0018 |
| T0021 | *Structure-free model-based predictive signal control: A sensitivity analysis on a corridor with spillback* | Contextual | Spillback control and sensitivity context |
| T0022 | *Simulation-Based Optimization: Achieving Computational Efficiency Through the Use of Multiple Simulators* | Primary | Multi-fidelity signal optimization and external evaluation |
| T0023 | *Urban transportation emissions mitigation: Coupling high-resolution vehicular emissions and traffic models for traffic signal optimization* | Contextual | Differentiable low-fidelity structure plus microscopic evaluator |
| T0024 | *Optimizing green splits in high-dimensional traffic signal control with trust region Bayesian optimization* | Primary | Black-box green-split optimizer comparator |
| T0025 | *sumoITScontrol: Traffic Controller Collection for SUMO Traffic Simulations* | Contextual | Replicated SUMO controller evaluation |
| T0026 | *The use of common random numbers to reduce the variance in network simulation of traffic* | **Borderline** | Retain only if marginal fairness value justifies added complexity |
| T0027 | *Reliable simulation-optimization of traffic lights in a real-world city* | Contextual | Scenario uncertainty and reliable optimization |
| T0028 | *Multi-intersection Traffic Optimisation: A Benchmark Dataset and a Strong Baseline* | **Borderline** | Held-out benchmark ideas dominated by adaptive/RL scope |
| T0029 | *Dynamic network loading: A stochastic differentiable model that derives link state distributions* | Contextual | Early differentiable DNL, no direct signal task |
| T0030 | *Extended macroscopic node model for multilane traffic* | Primary | Lane-aware aggregate comparator |
| T0031 | *With spatial queueing, the P0 responsive traffic signal control policy may fail to maximise network capacity even if queue storage capacities are very large* | Contextual | Shows that spatial queueing changes control conclusions |
| T0032 | *SUMO Traffic Lights documentation* | Primary technical source | Authoritative evaluator signal realization |
| T0033 | *OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections* | Exclude | Gridlock detection/clearing intervention, not simple spillback-process analysis |
| T0034 | *Second-order macroscopic modelling of stop-and-go traffic under fixed and feedback-based signal control* | **Borderline** | Congestion-regime context but different dynamics/task |
| T0035 | *Traffic-Aware Autonomous Driving with Differentiable Traffic Simulation* | Exclude | Autonomous-driving decision rather than signal task |
| T0036 | *Gradient-based Trajectory Optimization with Parallelized Differentiable Traffic Simulation* | Exclude | Trajectory decision rather than signal task |
| T0037 | *A Deep Reinforcement Learning Approach for Traffic Signal Control Optimization* | Exclude | Generic categorical/adaptive RL outside primary scope |
| T0038 | *IoT-Simulated Digital Twin with AI Traffic Signal Control for Real-Time Traffic Optimization in SUMO* | Exclude | Different AI/digital-twin purpose and disproportionate adaptation cost |

## Primary-anchor synopsis

These records determine why the proposed inclusion boundary is not just a generic signal-control survey:

- *End-to-end differentiable network traffic simulation with dynamic route choice* makes aggregate LTM/INM/DUO differentiable almost everywhere and demonstrates reverse-mode AD for large-scale toll optimization. It anchors the macro differentiable baseline but does not solve lane-specific signal blockage.^1
- *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization* directly compares AD-driven and gradient-free signal-timing optimization, while obtaining gradients by smoothing discrete agent logic. It anchors optimizer benefits and a contrasting differentiation strategy.^2
- *Linear MPC-Based Urban Traffic Control Using the Link Transmission Model* uses LTM propagation and spillback in a computationally efficient signal MPC formulation. It anchors the established aggregate signal task.^3
- *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics* combines network-level effective green fractions with a turn-queue lower level. It directly motivates the distinction between a service target and an implementable controller.^4
- *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage* models physical lane-group queues and their interactions under signal control. It is the clearest established task precedent for finite pocket/lane blockage.^5
- *Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow* constrains red, green, and cycle settings using physical lane storage and verifies them with a CTM implementation. It anchors short-lane overflow and feasibility.^6
- *Simulation-Based Optimization: Achieving Computational Efficiency Through the Use of Multiple Simulators* combines low- and high-accuracy simulators for signal optimization. It anchors cross-fidelity decision usefulness rather than internal-gradient evidence alone.^7
- Official SUMO signal documentation defines executable static phase durations, yellow/all-red phases, and program interfaces. It is a technical source for the richer-evaluator realization contract, not scientific evidence for the model hypothesis.^8

## Expanded records discussed at the gate

### T0004 — *Differentiable Modeling of Traffic Signals for Gradient-based Parameter Optimization in Microscopic Traffic Simulations*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0004 | *Differentiable Modeling of Traffic Signals for Gradient-based Parameter Optimization in Microscopic Traffic Simulations* | Exclude | Smoothed microscopic differentiability conflicts with project target; stronger task precedents exist |

**Abstract-level synopsis:** The thesis builds a smoothed differentiable microscopic intersection around a car-following model and timed signal logic, then uses AD gradients to optimize valid signal timings. Across 100 randomly generated traffic-load scenarios, the reported solution approaches the global optimum in a simple setting.

**Why retain:** It is unusually close to the proposed decision variable and gives a single-intersection task formulation.

**Why borderline:** It is a bachelor thesis, the full text is restricted, and stronger peer-reviewed differentiable-signal evidence already exists in T0002 and T0003.

**Final decision:** Exclude. Its microscopic differentiation strategy depends on smoothing/approximation, which is contrary to the project's targeted gradient semantics, and its signal-task role is covered by stronger sources.

### T0026 — *The use of common random numbers to reduce the variance in network simulation of traffic*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0026 | *The use of common random numbers to reduce the variance in network simulation of traffic* | **Borderline** | Retain only if marginal fairness value justifies added complexity |

**Abstract-level synopsis:** The paper applies common random numbers to traffic-network simulation comparisons to reduce output variance and improve precision when alternatives are evaluated under stochastic traffic conditions.

**Potential value:** It may support paired microscopic-evaluator comparisons under matched random realizations.

**Why borderline:** The initial task may use deterministic scenarios or fixed scenario banks, making a formal CRN method unnecessary. Adding it by default would reduce simplicity without changing the main task contract.

**Final decision:** Downgrade to borderline. During T4, retain it only if stochastic SUMO evaluation makes paired random-number control materially useful; otherwise reject it without further extraction.

### T0028 — *Multi-intersection Traffic Optimisation: A Benchmark Dataset and a Strong Baseline*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0028 | *Multi-intersection Traffic Optimisation: A Benchmark Dataset and a Strong Baseline* | **Borderline** | Held-out benchmark ideas dominated by adaptive/RL scope |

**Abstract-level synopsis:** The work introduces traffic-signal benchmark data and a baseline evaluated on synthetic and real maps and demand through SUMO. Its emphasis is learning-based multi-intersection control and generalization.

**Why retain:** It may contribute scenario splits, benchmark discipline, and held-out evaluation practice.

**Why borderline:** Its adaptive/RL control semantics do not match fixed-time continuous green allocation, and T0025 offers more directly reusable controller-evaluation guidance.

**Final decision:** Include contextually for evaluation design only; do not treat it as a task or model baseline.

### T0033 — *OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0033 | *OverFlowLight: Real-Time Gridlock Prevention and Traffic Signal Optimization for Urban Intersections* | Exclude | Gridlock detection/clearing intervention, not simple spillback-process analysis |

**Abstract-level synopsis:** This recent preprint combines rapid rule-based overflow intervention with longer-horizon controller back ends, including RL, to prevent gridlock at urban intersections.

**Why retain:** The overflow-prevention framing may clarify traffic outcomes and adverse-event metrics for the future task map.

**Why borderline:** The controller is hybrid, adaptive, and categorical; it neither tests the selective-discreteness representation nor supplies the primary continuous gradient contract.

**Final decision:** Exclude. Narrow verification shows that it detects overflow using sensing and inserts dedicated clearing phases across a deployed gridlock-control framework. It does not provide the simple-intersection spillback-process analysis sought here.

### T0034 — *Second-order macroscopic modelling of stop-and-go traffic under fixed and feedback-based signal control*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0034 | *Second-order macroscopic modelling of stop-and-go traffic under fixed and feedback-based signal control* | **Borderline** | Congestion-regime context but different dynamics/task |

**Abstract-level synopsis:** The paper embeds fixed and feedback signal logic in a second-order macroscopic model and studies stability and performance across free-flow, transitional, and heavy-congestion regimes. Adaptive control helps in intermediate regimes but not persistent oversaturation.

**Why retain:** It supports regime-aware scenario construction and cautions against assuming control benefits under every demand level.

**Why borderline:** It does not study lane-specific storage/order, uses a different second-order backbone, and does not supply the proposed optimization comparison.

**Final decision:** Include contextually for scenario regimes only if T4 extraction cost remains low.

### T0038 — *IoT-Simulated Digital Twin with AI Traffic Signal Control for Real-Time Traffic Optimization in SUMO*

| ID | Title | Decision | Task-facing role |
|---|---|---|---|
| T0038 | *IoT-Simulated Digital Twin with AI Traffic Signal Control for Real-Time Traffic Optimization in SUMO* | Exclude | Different AI/digital-twin purpose and disproportionate adaptation cost |

**Abstract-level synopsis:** The work constructs a site-specific SUMO model using sensor and geometry information and compares an adaptive AI controller with fixed-time and actuated baselines using mobility and emissions measures.

**Why retain:** It illustrates a calibrated richer-evaluator workflow and identical-geometry baseline comparisons.

**Why borderline:** The adaptive AI and digital-twin contribution is outside scope, and official SUMO documentation plus multi-fidelity studies provide stronger methodological anchors.

**Final decision:** Exclude. Its AI/digital-twin purpose, controller semantics, and evaluation adoption cost are not justified by a distinctive contribution to this review.

## Proposed exclusion boundary

Exclude a work from full extraction when its only connection is generic traffic-signal control, policy-gradient learning, autonomous-driving optimization, or differentiable trajectory optimization. Include it contextually only if it supplies a transferable field needed by the protocol: control realization, objective semantics, stochastic fairness, held-out evaluation, richer-simulator mapping, or a bounded later-task dependency.

This boundary avoids an exhaustive TSC review while preserving evidence that can change the selected task or evaluation contract.

## Access status before T4

No access problem prevents T3 decisions. T0007 is decision-important and currently represented by a publisher abstract; T0004 is restricted but not decision-critical. Before T4, open author/repository versions will be sought. If any decision-critical full text remains inaccessible, one batch request will be prepared as required by the protocol.

## T3 closure decisions

The user approved the project-bounded inclusion boundary, task taxonomy, and extraction codebook on 2026-09-10. Paper-specific refinements were applied as follows:

- T0004, T0020, T0033, and T0038 are excluded.
- T0019 is retained only for per-intersection TSC method evidence; its network-control scope is excluded.
- T0026 is downgraded to borderline and will be rejected during T4 unless stochastic evaluator design makes its marginal value worth the complexity.
- T0028 remains contextual for evaluation design, and T0034 remains optional contextual evidence for congestion-regime construction.
- All unmentioned screening decisions are approved.

No decision remains open at T3. The gate is closed and T4 is authorized but has not begun. Final task selection remains at T5.

## Sources

1. T. Seo, “[End-to-end differentiable network traffic simulation with dynamic route choice](https://arxiv.org/abs/2604.11380),” arXiv:2604.11380, 2026.
2. P. Andelfinger, “[Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization](https://arxiv.org/abs/2103.12476),” ACM SIGSIM-PADS, 2021.
3. G. S. van de Weg et al., “[Linear MPC-Based Urban Traffic Control Using the Link Transmission Model](https://trid.trb.org/View/1744667),” *IEEE Transactions on Intelligent Transportation Systems*, 2020.
4. G. S. van de Weg et al., “[Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics](https://ieeexplore.ieee.org/document/11010837),” *IEEE Transactions on Intelligent Transportation Systems*, 2025.
5. Y. Liu and G.-L. Chang, “[An arterial signal optimization model for intersections experiencing queue spillback and lane blockage](https://doi.org/10.1016/j.trc.2010.04.005),” *Transportation Research Part C*, 2011.
6. C. K. Wong and C. K. Lee, “[Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow](https://www.mdpi.com/2227-7390/8/8/1368),” *Mathematics*, 2020.
7. C. Osorio and K. K. Selvam, “[Simulation-Based Optimization: Achieving Computational Efficiency Through the Use of Multiple Simulators](https://pubsonline.informs.org/doi/10.1287/trsc.2016.0673),” *Transportation Science*, 2017.
8. Eclipse SUMO, “[Traffic Lights](https://eclipse.dev/sumo/docs/Simulation/Traffic_Lights.html),” official documentation, accessed 2026-09-10.
