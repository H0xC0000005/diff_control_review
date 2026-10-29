# R5 full-text screening — user review gate

Date: 2026-09-07  
Status: Approved and closed by user on 2026-09-07

## Accounting

- R4 candidates entering full-text review: 31 (30 includes plus one uncertain).
- Full texts verified and assessed: 31.
- Included for R6 extraction: 31.
- Full-text exclusions: 0.
- Access failures: 0.
- R4 uncertainty resolved: 1.

The deliberately conservative R4 screen produced no full-text exclusion. This is plausible for a small corpus constructed through targeted discovery rather than a broad database dump; it should not be generalized into a claim that the search had perfect precision.

## Resolved uncertainty

R0022 is not a preprint or follow-on report of R0021. The author sets and implemented methods differ:

- R0021 (Ni, Kouvelas, Makridis) is the peer-reviewed event-based LIFT model, based on entry/exit events, backward-traveling spaces, and FIFO at congested intersections.
- R0022 (Ni, Akopian, Kouvelas, Makridis) is a later preprint evaluating SUMO-MESO and proposing a discrete-time LTM implementation with backward-traveling spaces.

They overlap scientifically and share three authors, but contain materially distinct methods/evidence. Both remain separate included records. Their precise lineage will be coded during R6 extraction.

## Proposed nearest-predecessor set for user confirmation

| Record | Why nearest |
|---|---|
| R0003 | aggregate multi-commodity partial FIFO |
| R0005 | continuous signal-stage/node semantics |
| R0006 | endogenous multilane allocation and movement FIFO |
| R0007 | individual identity and FIFO added to LTM |
| R0008 | turn-level queue state and spillback |
| R0009 | physical lane-group queues and blockage |
| R0012 | differentiable discrete agent simulation and signal optimization |
| R0013 | differentiable micro/macro hybridization |
| R0014 | differentiable LTM with continuous route-aware state |
| R0021 | event-based vehicle mesoscopic LIFT and backward spaces |
| R0022 | discrete-time mesoscopic LTM alternative to SUMO |
| R0025 | turning-lane physical queues and lane-level FIFO |
| R0027 | continuous multi-commodity Link-Node CTM |

R0005 is retained as nearest on the signal-service dimension even though it is not mesoscopic. R0021 and R0022 are promoted from their R4 roles because full text establishes that both occupy the LWR-consistent mesoscopic link-model neighborhood. R0017 remains `direct`, not `nearest`: it uses discrete single-vehicle packets with horizontal queues and explicitly says its principal contribution is embedding an existing mesoscopic model in a metaheuristic network-control procedure.

### Nearest-predecessor review cards

The following synopses paraphrase the papers' abstracts and full-text purpose; they are not quotations.

#### R0003 — Wright et al. (2017)

**Title:** *On node models for high-dimensional road networks*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.trb.2017.09.001`  
**Synopsis:** Extends macroscopic node models to many inputs, outputs, and commodities. It replaces strict link FIFO with a partial-FIFO mechanism expressed through mutual-restriction intervals derived from lane geometry and movement interactions. It remains aggregate rather than preserving realized vehicle or queue sequence.  
**Why proposed as nearest:** Strongest aggregate competitor for representing selective cross-movement blockage without explicit queue order.

#### R0005 — Yahyamozdarani and Tampère (2023)

**Title:** *The continuous signalized (COS) node model for dynamic traffic assignment*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.trb.2022.12.003`  
**Synopsis:** Formulates a cycle-averaged signalized node model that respects turning demand, link sending/receiving boundaries, signal stages, priorities, and holding-free behavior. It avoids second-by-second signal switching while retaining a theoretically consistent average transfer calculation.  
**Why proposed as nearest:** Closest continuous signal-service and node-boundary foundation, although it is not mesoscopic.

#### R0006 — Gong, Bliemer, and Raadsen (2025)

**Title:** *Extended macroscopic node model for multilane traffic*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.trb.2025.103208`  
**Synopsis:** Introduces a lane-based macroscopic node formulation and an equilibrium allocation of sending flows across approach lanes. It relaxes link FIFO to movement-based FIFO and represents lane permissions without expanding every lane choice into a separate network route. The link receiving state remains aggregate.  
**Why proposed as nearest:** Strongest lane-aware aggregate alternative to explicit local lane occupancy and accessibility state.

#### R0007 — de Souza et al. (2025)

**Title:** *A mesoscopic link-transmission-model able to track individual vehicles*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.simpat.2025.103088`  
**Synopsis:** Modifies continuous LTM link and node transfers so flow moves in discrete vehicle units, permitting persistent individual tracking while preserving LTM traffic behavior. It proves a deviation bound relative to the continuous counterpart and tests lane-drop, merge, diverge, network, calibration, and transferability cases.  
**Why proposed as nearest:** Closest LTM precedent for adding exact persistent identity and FIFO, with integer vehicle transfers as the crucial contrast.

#### R0008 — Wei et al. (2025)

**Title:** *A link-based flow model with turn-level queue transmission and time-varying free-flow speed for urban road networks*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.trc.2024.104937`  
**Synopsis:** Adds a queue-inflow boundary and turn-level queue states to a link-based traffic model, allowing queue length and spillback to vary by movement under signals and changing free-flow speed. It compares the model with a conventional homogeneous link model and microscopic simulation.  
**Why proposed as nearest:** Direct competitor for the claim that movement-resolved local state is needed beyond aggregate link totals.

#### R0009 — Liu and Chang (2011)

**Title:** *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage*  
**Status:** Peer-reviewed journal article; DOI `10.1016/j.trc.2010.04.005`  
**Synopsis:** Models physical queue evolution by lane group, including shared-lane interactions, blockage, spillback across lane groups and neighboring intersections, and finite geometric constraints. It embeds these equations in arterial signal optimization using a genetic algorithm.  
**Why proposed as nearest:** Established lane-group blockage and storage-aware control model that may reproduce much of the proposed stack's functional behavior without exact order.

#### R0012 — Andelfinger (2021)

**Title:** *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization*  
**Status:** Peer-reviewed conference paper; DOI `10.1145/3437959.3459261`  
**Synopsis:** Makes an agent-based simulator differentiable by replacing or smoothing discrete program constructs and demonstrates gradient-guided optimization, including a traffic-signal example. It illustrates both the feasibility and approximation cost of differentiating individual-agent logic.  
**Why proposed as nearest:** Closest differentiable discrete-agent signal-optimization precedent and a contrast to keeping categorical structure outside the mass derivative path.

#### R0013 — Son et al. (2022)

**Title:** *Differentiable Hybrid Traffic Simulation*  
**Status:** Peer-reviewed ACM Transactions on Graphics/SIGGRAPH Asia article; DOI `10.1145/3550454.3555492`; author version arXiv `2210.08046`  
**Synopsis:** Combines differentiable macroscopic and microscopic traffic models with mechanisms for converting state between resolutions. It demonstrates gradient-based traffic applications, including signal control, while explicitly representing a micro/macro hybrid rather than selective semantic detail within a continuous-mass LTM.  
**Why proposed as nearest:** Closest differentiable multiresolution traffic architecture.

#### R0014 — Seo (2026)

**Title:** *End-to-end differentiable network traffic simulation with dynamic route choice*  
**Status:** Preprint; arXiv `2604.11380`  
**Synopsis:** Organizes LTM network loading, node operations, and dynamic route choice into an end-to-end differentiable computation and demonstrates large-network gradient optimization. Its state is continuous and route-aware, but it does not target realized local lane occupancy or exact within-queue order.  
**Why proposed as nearest:** Strongest differentiable aggregate LTM baseline and direct challenge to novelty claims based only on differentiable LTM or continuous route commodities.

#### R0021 — Ni, Kouvelas, and Makridis (2026)

**Title:** *Simulating link-level interrupted flow traffic dynamics and the comparison between different models for urban road networks*  
**Status:** Peer-reviewed open-access journal article; DOI `10.1016/j.simpat.2026.103252`  
**Synopsis:** Proposes the event-based LIFT mesoscopic model, transmitting vehicle entry and exit events, tracking backward-traveling spaces for spillback, and applying FIFO at congested intersections. It compares macroscopic and mesoscopic alternatives against microscopic simulation for interrupted urban flow.  
**Why proposed as nearest:** LWR-consistent, vehicle/event-based mesoscopic competitor with FIFO, spillback, and microscopic reference validation.

#### R0022 — Ni et al. (2026)

**Title:** *Revisiting mesoscopic traffic flow simulation in SUMO: Limitations, analysis, and an alternative*  
**Status:** Preprint; arXiv `2606.09282`  
**Synopsis:** Diagnoses unrealistic congestion onset and recovery in SUMO's existing mesoscopic model and proposes a discrete-time LTM alternative with explicit backward-traveling spaces. It tests signalized and bottleneck cases against kinematic-wave theory and SUMO microscopic simulation.  
**Why proposed as nearest:** A second, distinct LWR-based mesoscopic design that directly connects discrete vehicle-oriented simulation, spillback, and a richer reference model.

#### R0025 — Gao (2012)

**Title:** *A Node Model Capturing Turning Lane Capacity and Physical Queuing for the Dynamic Network Loading Problem*  
**Status:** Peer-reviewed open-access journal article; DOI `10.1155/2012/542459`  
**Synopsis:** Develops a dynamic node model with directional queues in turning lanes, lane-level FIFO, physical queue length, and a running-versus-queuing link decomposition. It integrates the node with dynamic network loading and tests it on a sample network.  
**Why proposed as nearest:** Early explicit precedent for physical turning-lane queues and lane-level FIFO—the phenomena the local mesoscopic zone is intended to recover.

#### R0027 — Wright et al. (2015)

**Title:** *A new model for multi-commodity macroscopic modeling of complex traffic networks*  
**Status:** Preprint; arXiv `1509.04995`  
**Synopsis:** Introduces the Link-Node CTM, a continuous multi-commodity network model with a general multi-input/multi-output node, capacity drop and hysteresis options, and local assignment of unknown split ratios. Commodities retain categorical distinctions but not exact realized queue sequence.  
**Why proposed as nearest:** Strong continuous-mass precedent for persistent commodity semantics and complex junction transfers.

## Borderline inclusions for user confirmation

| Record | Proposed treatment | Reason |
|---|---|---|
| R0018 | contextual include | actuated-signal task and MESCOP application; not fixed-time differentiation |
| R0019 | contextual include | controller/prediction sensitivity rather than simulator differentiation |
| R0020 | contextual include | queue-growth control algorithm; simulator is an evaluator rather than the contribution |
| R0023 | contextual include | calibration task; useful for validation practice but not signal control |
| R0024 | contextual secondary include | systematic review supports coverage and taxonomy; exclude from primary-method counts |
| R0029 | contextual include | microscopic differentiable IDM used for traffic-aware autonomous driving |
| R0030 | contextual include | differentiable IDM for trajectory tasks rather than network signal control |

These records will receive light extraction in R6 and will not be presented as nearest model baselines. Retaining them prevents the synthesis from falsely narrowing “differentiable traffic simulation” or “mesoscopic optimization” to the project's chosen task.

### Borderline/contextual review cards

#### R0018 — Toledo, Balasha, and Keblawi (2020)

**Title:** *Optimization of Actuated Traffic Signal Plans Using a Mesoscopic Traffic Simulation*  
**Status:** Peer-reviewed journal article; DOI `10.1061/JTEPBS.0000363`  
**Synopsis:** Couples MESCOP, an individual-vehicle mesoscopic intersection simulator, with a genetic algorithm to optimize complex actuated plans involving vehicle and pedestrian detection and transit priority.  
**Reason for contextual treatment:** Strong evidence that mesoscopic signal-plan optimization is established, but the task and derivative method differ from fixed-time differentiable control.

#### R0019 — Poelman et al. (2023)

**Title:** *Structure-free model-based predictive signal control: A sensitivity analysis on a corridor with spillback*  
**Status:** Peer-reviewed open-access journal article; DOI `10.1016/j.trc.2023.104174`  
**Synopsis:** Studies how prediction aggregation and bias affect a structure-free predictive signal controller in a microscopic corridor with spillback. It finds meaningful control-performance losses from prediction errors and motivates more vehicle-resolved predictions.  
**Reason for contextual treatment:** Relevant evidence about decision sensitivity and aggregation, but not a differentiable simulator or fixed-phase-topology method.

#### R0020 — Jang, Kim, and Jang (2015)

**Title:** *Traffic Signal Optimization for Oversaturated Urban Networks: Queue Growth Equalization*  
**Status:** Peer-reviewed journal article; DOI `10.1109/TITS.2015.2398896`  
**Synopsis:** Optimizes signal phase ratios to equalize queue-growth rates and delay spillback in oversaturated networks. Optimized plans are evaluated in CORSIM and compared with TRANSYT-7F.  
**Reason for contextual treatment:** Useful queue/storage-aware signal-task comparator; the main contribution is a control heuristic rather than simulator representation or differentiation.

#### R0023 — 2025 calibration preprint

**Title:** *Automatic Calibration of Mesoscopic Traffic Simulation Using Vehicle Trajectory Data*  
**Status:** Preprint; arXiv `2501.10934`  
**Synopsis:** Uses vehicle-trajectory observations to calibrate a mesoscopic traffic simulation automatically, providing evidence about parameter estimation, trajectory-based validation, and the practical identifiability of a mesoscopic model.  
**Reason for contextual treatment:** Relevant to validation and inverse use, but not to the fixed-time signal-gradient gap.

#### R0024 — Gong, Raadsen, and Bliemer (2025)

**Title:** *A systematic review of node models for macroscopic network loading of traffic flows*  
**Status:** Peer-reviewed open-access review; DOI `10.1016/j.trb.2025.103273`  
**Synopsis:** Systematically reviews 48 macroscopic node-model studies, classifying their general principles, FIFO domains, allocation rules, operational features, and extensions. Its search used four scholarly databases and citation snowballing.  
**Reason for contextual treatment:** Important coverage and taxonomy evidence, but it is secondary literature and should not be counted as a primary implemented method.

#### R0029 — Zheng, Son, and Lin (2022)

**Title:** *Traffic-Aware Autonomous Driving with Differentiable Traffic Simulation*  
**Status:** Preprint; arXiv `2210.03772`  
**Synopsis:** Uses a differentiable microscopic traffic simulation to supervise autonomous-vehicle speed control toward traffic-flow and energy benefits for nearby vehicles.  
**Reason for contextual treatment:** Demonstrates another use of differentiable traffic dynamics, but focuses on autonomous-driving behavior rather than network loading or signal control.

#### R0030 — Son et al. (2024)

**Title:** *Gradient-based Trajectory Optimization with Parallelized Differentiable Traffic Simulation*  
**Status:** Preprint; arXiv `2412.16750`  
**Synopsis:** Implements a highly parallel differentiable Intelligent Driver Model and optimizes model parameters or trajectories for filtering, reconstruction, and prediction on vehicle-trajectory datasets.  
**Reason for contextual treatment:** Relevant differentiation and scalability evidence, but microscopic car-following trajectory tasks are outside the proposed model's central traffic-state and signal-control comparison.

## Requested user decision

Please confirm or correct:

1. the 13-record nearest-predecessor set;
2. retention of the seven borderline records as contextual evidence;
3. proceeding with all 31 records to R6 extraction, with the secondary review excluded from primary-method counts.

No project methodology or milestone file is changed by this decision.

## Closure decision

The user approved the 13-record nearest-predecessor set and agreed to retain all seven borderline records as contextual evidence. The statement that there was no absolute reason to exclude the borderline group, together with approval of that group, is interpreted as approval to advance the complete 31-record corpus to R6. The systematic node-model review remains secondary evidence and is excluded from primary-method counts.

R5 is closed. No screening decision was changed by the feedback.
