# T4 full-text evidence and quality audit

Date: 2026-09-10  
Status: approved and closed on 2026-09-10

## Completion accounting

- T3 retained or conditional records assessed: 31/31.
- Final T4 extraction set: 30 records.
- Primary records: 20.
- Contextual records: 10, including two approved low-cost borderline promotions.
- Rejected at T4 value check: T0026.
- Strong evidence quality: 21 records.
- Adequate evidence quality: 9 records.
- Decision-critical unresolved access failures: 0.

T0007 was supplied by the user and extracted locally with page boundaries. Other full texts were read from open publisher, author, institutional, arXiv, official-documentation, or previously archived sources. T0031 remains abstract/repository-level, but its retained claim is narrow and contextual; it does not control task selection.

## Main evidence findings

### 1. Continuous green variables do not imply differentiable simulation

The corpus contains several continuous green-allocation tasks, but their computational mechanisms differ:

- T0001–T0003 provide automatic-differentiation precedents.
- T0005–T0007 formulate signal decisions through linear, quadratic, or nonlinear optimization but do not differentiate the simulator end to end.
- T0022 and T0023 use differentiable analytical low-fidelity structure to guide expensive simulation, which is not the same as a gradient of the high-fidelity simulator.
- T0024 is a derivative-free Bayesian-optimization baseline over fixed-topology green splits.

These categories must remain separate in T5. “Continuous decision variable,” “gradient-based optimizer,” and “differentiable simulator” are not interchangeable labels.

### 2. The nearest task predecessor stops at aggregate turn queues

T0007 is the closest task precedent found. Its network layer optimizes segment-level effective green fractions over an LTM prediction horizon, while its local layer allocates turn-level effective green fractions using predicted turn-queue lengths. It assumes known turning rates, represents left-turn and through/right-turn queues as aggregate cumulative counts and lengths, and evaluates control using a separate CTM system model.

It does not produce executable on/off phase intervals, store exact movement order, or test whether a computed lane/pocket allocation is reachable through ordered arrivals. Consequently, it substantially narrows the project's task novelty but does not cover the selective-discreteness question.

### 3. Finite storage is established; order-dependent accessibility is the sharper test

T0008–T0010 establish lane-group blockage, short-lane overflow constraints, and physical turning-lane queues. T0014, T0015, and T0030 establish partial FIFO, movement queues, and aggregate lane allocation. A primary experiment that merely demonstrates finite storage or turn queues would therefore be weak.

The stronger diagnostic is whether two states with matched aggregate link/movement totals but different realized order/accessibility yield different service, blockage, gradients, or optimized green allocation. The literature supplies the surrounding baselines, but the exact paired-state experiment remains to be formulated at T5/T6.

### 4. Effective service and executable timing remain genuinely different tasks

T0005 and T0007 optimize effective green fractions. T0006 explicitly supplies a lower layer that converts network reference outflows into green/red switching. T0009 and official SUMO documentation expose cycle, duration, clearance, and storage-feasibility requirements.

The evidence therefore does not justify silently calling a service fraction an implementable signal plan. The T5 shortlist should state the claim level explicitly; direct realizability may be a supporting transfer test or later task if it introduces unapproved within-cycle semantics.

### 5. A fair experiment needs two orthogonal comparisons

- **Representation axis:** homogeneous LTM → movement/partial-FIFO queue → lane/storage-aware aggregate → selective order/access model → richer forward evaluator.
- **Optimizer axis:** exact model gradient versus derivative-free or estimated-gradient optimization under the same model, variables, objective, initialization, and budget.

T0002 and T0024 help define the optimizer comparison. T0014, T0015, T0030, T0017, and T0016 define the representation comparison. Combining the axes into one comparison would not reveal whether gains came from the model or the optimizer.

### 6. External usefulness needs held-out, matched interventions

T0022 supports using low- and high-fidelity simulators within one optimization/evaluation design. T0027 supports multiple demand scenarios rather than one nominal case. T0025 and T0028 support replicated or held-out simulator evaluation, while T0032 defines executable SUMO phase programs.

No retained work directly proves that a selective mesoscopic gradient yields a better signal decision in a separately specified richer evaluator. The planned usefulness test remains necessary and should report negative or equivalent outcomes.

## Record-level audit table

| ID | Title | T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|---|---|
| T0001 | *End-to-end differentiable network traffic simulation with dynamic route choice* | Primary macro-gradient baseline | Toll task; no signal | Piecewise reverse AD | Adequate—preprint |
| T0002 | *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization* | Differentiable-agent contrast | Realized static timing | Smoothed/surrogate AD | Strong |
| T0003 | *Differentiable Hybrid Traffic Simulation* | Differentiable hybrid contrast | Signal/control tasks | Reverse AD | Strong |
| T0005 | *Linear MPC-Based Urban Traffic Control Using the Link Transmission Model* | Established LTM-MPC task | Effective green/service | Analytical optimization, not simulator AD | Strong |
| T0006 | *A Hierarchical Control Framework for Coordination of Intersection Signal Timings in All Traffic Regimes* | Signal-realization reference | Reference outflow to switching | Analytical optimization | Strong |
| T0007 | *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics* | Nearest task/turn-queue baseline | Segment/turn effective fractions | QP/NLP, not simulator AD | Strong |
| T0008 | *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage* | Lane-blockage task baseline | Realized arterial timing | Black-box optimization | Strong |
| T0009 | *Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow* | Lane-storage feasibility | Cycle/red/green plus markings | MILP/analytical model | Adequate |
| T0010 | *A Node Model Capturing Turning Lane Capacity and Physical Queuing for the Dynamic Network Loading Problem* | Turning-lane reference | Signals as service inputs | None | Adequate |
| T0011 | *The continuous signalized (COS) node model for dynamic traffic assignment* | Signal-node reference | Cycle-averaged service | None | Strong |
| T0012 | *On the continuum approximation of the on-and-off signal control on dynamic traffic networks* | Averaging-validity reference | Effective service versus on/off | Analytical sensitivity | Strong |
| T0013 | *Continuum signalized junction model for dynamic traffic networks: Offset, spillback, and multiple signal phases* | Later realization context | Multiphase/offset continuum signal | Analytical sensitivity | Strong |
| T0014 | *On node models for high-dimensional road networks* | Structured aggregate baseline | No optimized signal task | None | Strong |
| T0015 | *A link-based flow model with turn-level queue transmission and time-varying free-flow speed for urban road networks* | Turn-queue baseline | On/off signal scenarios | None | Strong |
| T0016 | *Simulating link-level interrupted flow traffic dynamics and the comparison between different models for urban road networks* | Richer mesoscopic evaluator | On/off signal scenarios | None | Strong |
| T0017 | *A mesoscopic link-transmission-model able to track individual vehicles* | Identity/order reference | No signal task | None | Strong |
| T0018 | *MESCOP: A Mesoscopic Traffic Simulation Model to Evaluate and Optimize Signal Control Plans* | Per-intersection meso task | Complex actuated plans | Black-box optimization | Adequate |
| T0019 | *Network Traffic Control Based on a Mesoscopic Dynamic Flow Model* | Per-intersection method only | Green durations; network coordination excluded | Metaheuristic | Adequate |
| T0021 | *Structure-free model-based predictive signal control: A sensitivity analysis on a corridor with spillback* | Aggregation-sensitivity context | Predictive signal control | Not simulator AD | Strong |
| T0022 | *Simulation-Based Optimization: Achieving Computational Efficiency Through the Use of Multiple Simulators* | Cross-fidelity optimization | Continuous signal plan | Analytical low-fidelity sensitivity | Strong |
| T0023 | *Urban transportation emissions mitigation: Coupling high-resolution vehicular emissions and traffic models for traffic signal optimization* | Structured metamodel context | Real-valued signal plan | Analytical surrogate sensitivity | Strong |
| T0024 | *Optimizing green splits in high-dimensional traffic signal control with trust region Bayesian optimization* | Black-box optimizer baseline | Fixed-topology green split | None | Strong |
| T0025 | *sumoITScontrol: Traffic Controller Collection for SUMO Traffic Simulations* | Evaluator protocol | Adaptive/controller-specific | None | Adequate—preprint |
| T0026 | *The use of common random numbers to reduce the variance in network simulation of traffic* | Rejected at T4 | Stochastic policy comparison | None | Adequate but low marginal value |
| T0027 | *Reliable simulation-optimization of traffic lights in a real-world city* | Scenario-reliability context | City traffic-light programs | None | Strong |
| T0028 | *Multi-intersection Traffic Optimisation: A Benchmark Dataset and a Strong Baseline* | Held-out benchmark context | Adaptive policies | None | Adequate—scope mismatch |
| T0029 | *Dynamic network loading: A stochastic differentiable model that derives link state distributions* | Differentiable DNL context | No signal task | Analytical derivative | Strong |
| T0030 | *Extended macroscopic node model for multilane traffic* | Lane-allocation baseline | No optimized signal task | None | Strong |
| T0031 | *With spatial queueing, the P0 responsive traffic signal control policy may fail to maximise network capacity even if queue storage capacities are very large* | Spatial-queue control context | Responsive P0 policy | Analytical counterexample | Adequate—narrow abstract-level use |
| T0032 | *SUMO Traffic Lights documentation* | Evaluator technical contract | Executable phase durations | None | Strong technical authority |
| T0034 | *Second-order macroscopic modelling of stop-and-go traffic under fixed and feedback-based signal control* | Congestion-regime context | Fixed/feedback signals | Analytical sensitivity | Adequate—different model/task |

## Expanded primary records

The synopses below are paraphrases for review convenience. Each repeats the corresponding audit row so the title, T4 role, derivative interpretation, and quality remain visible during detailed reading.

### T0001 — *End-to-end differentiable network traffic simulation with dynamic route choice*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Primary macro-gradient baseline | Toll task; no signal | Piecewise reverse AD | Adequate—preprint |

**Abstract synopsis:** Implements LTM, a fixed-length incremental node procedure, and dynamic route choice in JAX using piecewise operations and reverse-mode AD. Small cases inspect derivatives and a large Chicago case optimizes time-dependent congestion tolls.

**T4 interpretation:** Strong evidence that aggregate LTM differentiation itself is established. It does not test signal control, lane-local storage, or realized order.

### T0002 — *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Differentiable-agent contrast | Realized static timing | Smoothed/surrogate AD | Strong |

**Abstract synopsis:** Replaces branches and other discrete agent-program elements with smooth counterparts, then compares fidelity, overhead, and gradient-based versus gradient-free optimization. Its traffic example includes high-dimensional static signal timing.

**T4 interpretation:** It supports the value of gradients in signal optimization but embodies the approximation strategy the present project seeks to avoid.

### T0003 — *Differentiable Hybrid Traffic Simulation*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Differentiable hybrid contrast | Signal/control tasks | Reverse AD | Strong |

**Abstract synopsis:** Couples differentiable macroscopic and microscopic traffic regions through a differentiable conversion component and demonstrates inverse and control optimization. Experiments compare macro, micro, and hybrid configurations.

**T4 interpretation:** It is a credible richer differentiable architecture, but its micro/macro conversion and microscopic local dynamics differ from one continuous ordered-mass path.

### T0005 — *Linear MPC-Based Urban Traffic Control Using the Link Transmission Model*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Established LTM-MPC task | Effective green/service | Analytical optimization, not simulator AD | Strong |

**Abstract synopsis:** Formulates linear MPC around LTM dynamics so both forward propagation and backward spillback waves influence signal control. It evaluates total time spent and computation time against store-and-forward and CTM-based strategies.

**T4 interpretation:** It anchors the aggregate signal-control task. Solving its analytical optimization problem is not evidence of an end-to-end simulator gradient.

### T0006 — *A Hierarchical Control Framework for Coordination of Intersection Signal Timings in All Traffic Regimes*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Signal-realization reference | Reference outflow to switching | Analytical optimization | Strong |

**Abstract synopsis:** A network MPC layer supplies desired average link-outflow trajectories, and a lower layer maps them to green/red switching at intersections across traffic regimes.

**T4 interpretation:** It demonstrates why an effective service target and an implementable phase program are distinct scientific outputs.

### T0007 — *Hierarchical Predictive Control of Network Traffic Signals Using Link Transmission Model With Queue Dynamics*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Nearest task/turn-queue baseline | Segment/turn effective fractions | QP/NLP, not simulator AD | Strong |

**Abstract synopsis:** Uses a network LTM-QP layer to optimize segment-level effective green fractions for travel-time/throughput performance and signal stability. Distributed local NLP controllers allocate turn-level fractions from aggregate queue lengths and track the network references; arterial and grid cases compare against aggregate MPC and max pressure.

**T4 interpretation:** This is the nearest task predecessor. It lacks exact order, lane-access reachability, executable phase intervals, derivative validation, and richer-simulator gradient transfer.

### T0008 — *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Lane-blockage task baseline | Realized arterial timing | Black-box optimization | Strong |

**Abstract synopsis:** Evolves physical queues by lane group and captures shared-lane interference, turn-pocket blockage, and interintersection spillback. Signal timing is optimized for travel time or throughput under congested regimes.

**T4 interpretation:** It already covers much of the functional blockage outcome. The proposed project must distinguish exact order/access semantics and gradient fidelity rather than claim first modeling of lane blockage.

### T0009 — *Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Lane-storage feasibility | Cycle/red/green plus markings | MILP/analytical model | Adequate |

**Abstract synopsis:** Adds physical lane-length constraints to lane-based signal design so effective red, green, and cycle settings avoid short-lane overflow. Hong Kong cases are checked using TRANSYT's CTM implementation.

**T4 interpretation:** It establishes that physically attainable queue storage must constrain signal plans, but its mixed-integer lane markings and aggregate queues do not match the proposed derivative path.

### T0010 — *A Node Model Capturing Turning Lane Capacity and Physical Queuing for the Dynamic Network Loading Problem*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Turning-lane reference | Signals as service inputs | None | Adequate |

**Abstract synopsis:** Splits links into running and queuing portions and tracks directional turning-lane queues with physical length and lane-level FIFO inside dynamic network loading.

**T4 interpretation:** It supplies a physical turning-lane reference but no optimization or differentiability evidence.

### T0011 — *The continuous signalized (COS) node model for dynamic traffic assignment*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Signal-node reference | Cycle-averaged service | None | Strong |

**Abstract synopsis:** Defines a traffic-consistent continuous signalized node operator combining stages, priorities, sending/receiving limits, turning fractions, and holding-free behavior.

**T4 interpretation:** It is a strong service-equation reference but remains aggregate and does not select a downstream objective.

### T0012 — *On the continuum approximation of the on-and-off signal control on dynamic traffic networks*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Averaging-validity reference | Effective service versus on/off | Analytical sensitivity | Strong |

**Abstract synopsis:** Establishes conditions and error behavior for replacing binary signals with continuous capacity scaling. Approximation quality depends on cycle length and can weaken under sustained or transient spillback.

**T4 interpretation:** It supports continuous green service with explicit limits; it does not justify an unconditional equivalence claim in the very blockage regimes of interest.

### T0014 — *On node models for high-dimensional road networks*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Structured aggregate baseline | No optimized signal task | None | Strong |

**Abstract synopsis:** Extends macroscopic node models using mutual-restriction intervals so congestion in one movement can partially obstruct others rather than impose strict link FIFO.

**T4 interpretation:** It is the key parameterized aggregate alternative that must be controlled before attributing gains to exact order.

### T0015 — *A link-based flow model with turn-level queue transmission and time-varying free-flow speed for urban road networks*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Turn-queue baseline | On/off signal scenarios | None | Strong |

**Abstract synopsis:** Introduces cumulative queue inflow and turn-level queue states into a link-based model and compares its signalized-network predictions with homogeneous models and microscopic simulation.

**T4 interpretation:** It tests whether movement queues alone explain the desired benefit, without exact ordered metadata.

### T0016 — *Simulating link-level interrupted flow traffic dynamics and the comparison between different models for urban road networks*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Richer mesoscopic evaluator | On/off signal scenarios | None | Strong |

**Abstract synopsis:** The event-based LIFT model propagates entry/exit events and backward spaces, applies FIFO at congested intersections, and is compared with microscopic simulation and analytical traffic behavior.

**T4 interpretation:** It is a strong forward reference for interrupted flow and spillback, but it supplies neither gradients nor the same continuous-mass semantics.

### T0017 — *A mesoscopic link-transmission-model able to track individual vehicles*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Identity/order reference | No signal task | None | Strong |

**Abstract synopsis:** Integerizes LTM transfers so individual vehicles and their order persist while bounding deviation from continuous LTM. It evaluates network and field cases.

**T4 interpretation:** It is the closest identity/order forward reference, but integer transfer events are incompatible with the desired exact continuous gradient path.

### T0018 — *MESCOP: A Mesoscopic Traffic Simulation Model to Evaluate and Optimize Signal Control Plans*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Per-intersection meso task | Complex actuated plans | Black-box optimization | Adequate |

**Abstract synopsis:** Builds an event/packet mesoscopic simulator for evaluating complex signal plans at much lower cost than microscopic simulation and demonstrates signal-plan optimization applications.

**T4 interpretation:** It establishes mesoscopic TSC maturity. Only its per-intersection task/method content transfers; actuated and broader network logic remain outside scope.

### T0022 — *Simulation-Based Optimization: Achieving Computational Efficiency Through the Use of Multiple Simulators*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Cross-fidelity optimization | Continuous signal plan | Analytical low-fidelity sensitivity | Strong |

**Abstract synopsis:** Combines high-accuracy expensive and low-accuracy efficient traffic simulators, choosing evaluations adaptively using an analytical approximation. Signal-control studies span small and city networks.

**T4 interpretation:** It supports a richer-evaluator design but does not validate gradients exported directly from the proposed simulator.

### T0024 — *Optimizing green splits in high-dimensional traffic signal control with trust region Bayesian optimization*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Black-box optimizer baseline | Fixed-topology green split | None | Strong |

**Abstract synopsis:** Optimizes phase green splits with phase topology, sequence, cycle, and offsets fixed. Trust-region Bayesian optimization is compared with BO, genetic algorithms, and random sampling on real networks up to 233 dimensions.

**T4 interpretation:** It is a well-matched derivative-free optimizer comparator but does not isolate lane/order blockage or provide simulator gradients.

### T0030 — *Extended macroscopic node model for multilane traffic*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Lane-allocation baseline | No optimized signal task | None | Strong |

**Abstract synopsis:** Allocates movements across permitted lanes through an equilibrium procedure and obtains movement-level FIFO without expanding every lane into a separate network link.

**T4 interpretation:** It is the strongest aggregate lane-allocation alternative; exact order and physically realized accessibility through arrivals remain absent.

### T0032 — *SUMO Traffic Lights documentation*

| T4 role | Signal/task meaning | Derivative category | Quality |
|---|---|---|---|
| Evaluator technical contract | Executable phase durations | None | Strong technical authority |

**Abstract synopsis:** Official documentation defines static and actuated signal programs, phase-state durations, yellow/all-red treatment, and external control interfaces.

**T4 interpretation:** It defines how an intervention can be realized in SUMO. It is not evidence that any traffic-model or gradient claim is scientifically valid.

## Contextual and borderline resolutions

- **T0013 retained:** necessary to qualify continuum signal use when offsets/multiple phases or spillback matter.
- **T0019 retained narrowly:** only its per-intersection green-time and mesoscopic queue method is extracted; network-control claims are out of scope.
- **T0021 retained:** aggregation sensitivity is relevant to decision transfer even though no simulator gradient is studied.
- **T0023 retained:** supplies a concrete analytical-low/high-fidelity distinction; emissions objectives are not carried into the primary task.
- **T0025 retained:** provides recent replicated SUMO evaluation practice; its adaptive controllers are not candidate task baselines.
- **T0026 rejected:** fixed scenario banks and recorded seeds can provide the necessary pairing initially. A separate formal CRN method offers too little marginal value for the added complexity.
- **T0027 retained:** multiple plausible demand scenarios and reliability across them transfer directly to held-out task design.
- **T0028 retained contextually:** only benchmark split/generalization practices transfer; RL task semantics do not.
- **T0029 retained:** early differentiable aggregate DNL context prevents overly narrow historical claims.
- **T0031 retained narrowly:** supports only the proposition that spatial queue representation can change control conclusions.
- **T0034 retained at low cost:** supplies traffic-regime variation and a negative-control lesson; its second-order dynamics are not a model baseline.

## Quality and interpretation boundaries

1. Preprints are retained where recent differentiable-simulation or evaluation practice is important, with maturity stated explicitly.
2. T0031's abstract-level evidence is used only for its explicit theoretical counterexample; no equation or broader result is inferred.
3. A paper's task relevance does not make its model a fair executable baseline.
4. Internal simulator optimization is not cross-fidelity usefulness evidence.
5. Aggregate turn queues, lane equilibrium, partial FIFO, exact individual order, and continuous ordered mass are distinct representations.
6. Continuous effective green fractions are not called executable timings unless cycle and clearance semantics are supplied.

## T4 approval record

The user approved this audit on 2026-09-10. The following five items are retained as the approved decision basis:

1. the extraction distinction among simulator AD, analytical optimization/sensitivity, structured metamodel guidance, and derivative-free optimization;
2. the coding and interpretation of the 20 primary records, especially T0007 as the nearest task predecessor;
3. rejection of T0026 and the narrow contextual use of T0019, T0028, T0031, and T0034;
4. the evidence-derived baseline/task implications: finite storage and turn queues are established, while order-dependent physical accessibility is the sharper diagnostic; and
5. the six quality/interpretation boundaries above.

This approval closed T4 and authorized T5 candidate-task synthesis. It did not select a task or amend the project.
