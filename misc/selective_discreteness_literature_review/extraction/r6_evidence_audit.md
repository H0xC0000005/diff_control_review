# Post-R6 evidence-audit gate

Date: 2026-09-07  
Status: Approved and closed by user on 2026-09-07

## Completion accounting

- Included studies extracted: 31/31.
- Approved nearest predecessors extracted: 13/13.
- Other primary studies: 17.
- Secondary systematic reviews: 1, kept outside primary-method counts.
- Method credibility: 16 `strong`, 15 `adequate`, 0 excluded for weak quality.
- Unresolved access failures: 0.
- Material bibliographic corrections: R0013 recorded as a peer-reviewed ACM TOG/SIGGRAPH Asia 2022 article, DOI `10.1145/3550454.3555492`.

The ten-paper pilot passed without changing the eligibility boundary or behavioral categories. The codebook is frozen for this corpus.

## Evidence pattern requiring user review

| Evidence dimension | R6 observation | Interpretation boundary |
|---|---|---|
| Continuous traffic quantity | 16 studies | Continuous mass itself is established. |
| Exact realized order | 12 studies | It is concentrated in individual/event/hybrid models, not evidence for the proposed continuous ordered-mass construction. |
| Aggregate or parameterized FIFO | 16 studies | Aggregate models already offer substantial FIFO, partial-FIFO, movement, and lane functionality. |
| Reverse-mode AD | 4 studies | Differentiable traffic simulation is established, but across materially different macro, hybrid, and microscopic states. |
| Smoothed/surrogate differentiable agents | 1 primary study | Supports the claimed trade-off as one design point, not a universal statement about microscopic differentiation. |
| Microscopic forward comparison | 6 studies, including combined LWR evidence | Forward cross-fidelity validation exists in the literature. |
| External gradient/control-transfer validation | 0 studies as operationally defined here | No extracted study evaluates gradient-directed controls in a separately specified richer simulator; absence remains corpus-bounded. |

No extracted record combines continuous mass, exact realized semantic order, lane-local finite storage/accessibility, reverse-mode derivatives, and external gradient-usefulness evidence. This supports an open intersection for later synthesis, but R6 does not convert corpus absence into a “first” claim.

## Nearest-predecessor extraction audit

| Record | Quantity / order | Differentiation | Main relation | Credibility |
|---|---|---|---|---|
| R0003 | continuous; parameterized partial FIFO | none | aggregate restriction alternative | strong |
| R0005 | continuous; aggregate FIFO | none | continuous signal-node operator | strong |
| R0006 | continuous; movement FIFO | none | endogenous lane allocation | strong |
| R0007 | integer vehicles; exact realized order | none | identity-preserving LTM | strong |
| R0008 | continuous; turn-level aggregate FIFO | none | movement queues and spillback | strong |
| R0009 | continuous; lane-group aggregate queues | black-box optimization | lane storage and blockage | strong |
| R0012 | individual agents; exact order | smoothed/surrogate AD | differentiable agent logic | strong |
| R0013 | mixed hybrid; exact micro order | reverse AD | differentiable micro/macro conversion | strong |
| R0014 | continuous; aggregate FIFO | reverse AD | differentiable route-aware LTM | adequate; recent preprint |
| R0021 | integer/event vehicles; exact order | none | LIFT spillback and micro validation | strong |
| R0022 | integer vehicles; exact order | none | discrete-time mesoscopic LTM | adequate; recent preprint |
| R0025 | continuous; lane-level FIFO | none | physical turning-lane queues | adequate |
| R0027 | continuous commodities; parameterized partial FIFO | none | Link-Node CTM commodity state | adequate; preprint |

### Nearest-predecessor titles and abstract summaries

The abstracts below are concise paraphrases for review convenience, not quotations.

#### R0003

**Title:** *On node models for high-dimensional road networks*  
**Abstract:** Develops a general macroscopic node framework for networks with many inputs, outputs, and commodities. It introduces partial FIFO through mutual-restriction intervals that represent how queues for one movement obstruct others, permitting behavior between strict link FIFO and no FIFO.
**R6 coding:** Quantity/order — continuous mass; parameterized partial FIFO. Differentiation — none. Main relation — aggregate restriction alternative. Credibility — strong.

#### R0005

**Title:** *The continuous signalized (COS) node model for dynamic traffic assignment*  
**Abstract:** Formulates a cycle-averaged signalized node model that consistently combines turning demand, link sending and receiving constraints, stages, priorities, and holding-free flow. Numerical cases compare COS with other continuous signal formulations and expose violations that COS is designed to avoid.
**R6 coding:** Quantity/order — continuous mass; aggregate FIFO. Differentiation — none. Main relation — continuous signal-node operator. Credibility — strong.

#### R0006

**Title:** *Extended macroscopic node model for multilane traffic*  
**Abstract:** Introduces a lane-based macroscopic node model and an equilibrium procedure for allocating movement sending flows across permitted approach lanes. The formulation relaxes link FIFO to movement FIFO and captures multilane junction effects without explicitly expanding every lane choice into a separate route.
**R6 coding:** Quantity/order — continuous mass; movement FIFO. Differentiation — none. Main relation — endogenous lane allocation. Credibility — strong.

#### R0007

**Title:** *A mesoscopic link-transmission-model able to track individual vehicles*  
**Abstract:** Modifies LTM link and node transfers so traffic moves in integer vehicle units, enabling persistent individual tracking while retaining the macroscopic LTM backbone. It bounds the deviation from continuous LTM and evaluates merges, diverges, lane drops, larger networks, and parameter transferability.
**R6 coding:** Quantity/order — integer vehicles; exact realized order. Differentiation — none. Main relation — identity-preserving LTM. Credibility — strong.

#### R0008

**Title:** *A link-based flow model with turn-level queue transmission and time-varying free-flow speed for urban road networks*  
**Abstract:** Adds queue-inflow and turn-level queue states to conventional link-based flow modeling so movement-specific queues and spillback can be represented. Intersection and network experiments compare its predictions with a homogeneous link model and microscopic simulation.
**R6 coding:** Quantity/order — continuous mass; turn-level aggregate FIFO. Differentiation — none. Main relation — movement queues and spillback. Credibility — strong.

#### R0009

**Title:** *An arterial signal optimization model for intersections experiencing queue spillback and lane blockage*  
**Abstract:** Models arterial queue evolution by lane group, including shared-lane interactions, turn-pocket blockage, finite geometry, and spillback between lane groups and intersections. The model is embedded in a genetic-algorithm signal-timing procedure and compared with established signal software.
**R6 coding:** Quantity/order — continuous mass; lane-group aggregate queues. Differentiation — black-box optimization. Main relation — lane storage and blockage. Credibility — strong.

#### R0012

**Title:** *Differentiable Agent-Based Simulation for Gradient-Guided Simulation-Based Optimization*  
**Abstract:** Replaces discrete elements of time-driven agent simulations, such as conditional branches, with smooth differentiable counterparts. Traffic and epidemic examples evaluate fidelity, computational overhead, gradient checks, and gradient-based optimization relative to derivative-free methods.
**R6 coding:** Quantity/order — individual agents; exact forward order. Differentiation — smoothed/surrogate AD. Main relation — differentiable agent logic. Credibility — strong.

#### R0013

**Title:** *Differentiable Hybrid Traffic Simulation*  
**Abstract:** Combines differentiable macroscopic and microscopic traffic models in one simulator and introduces a differentiable conversion component between their state representations. It demonstrates inverse and traffic-control optimization and compares macro, micro, and hybrid configurations.
**R6 coding:** Quantity/order — mixed hybrid state; exact order in the microscopic region. Differentiation — reverse-mode AD. Main relation — differentiable micro/macro conversion. Credibility — strong.

#### R0014

**Title:** *End-to-end differentiable network traffic simulation with dynamic route choice*  
**Abstract:** Implements LTM, general node operations, and dynamic route choice as an end-to-end differentiable JAX computation using piecewise-linear operations. A large Chicago network toll experiment demonstrates reverse-mode gradients with many decision variables.
**R6 coding:** Quantity/order — continuous mass; aggregate FIFO. Differentiation — reverse-mode AD. Main relation — differentiable route-aware LTM. Credibility — adequate; recent preprint.

#### R0021

**Title:** *Simulating link-level interrupted flow traffic dynamics and the comparison between different models for urban road networks*  
**Abstract:** Proposes the event-based LIFT mesoscopic model, which transmits vehicle entry and exit events, tracks backward-traveling spaces for spillback, and applies FIFO at congested intersections. Signalized-network experiments compare it with alternative models and microscopic simulation.
**R6 coding:** Quantity/order — integer/event vehicles; exact order. Differentiation — none. Main relation — LIFT spillback and microscopic validation. Credibility — strong.

#### R0022

**Title:** *Revisiting mesoscopic traffic flow simulation in SUMO: Limitations, analysis, and an alternative*  
**Abstract:** Identifies queue-development and backward-space limitations in SUMO's existing mesoscopic traffic model. It proposes a discrete-time LTM alternative and compares congestion onset, recovery, density, and spillback behavior with kinematic-wave expectations and SUMO microscopic simulation.
**R6 coding:** Quantity/order — integer vehicles; exact order. Differentiation — none. Main relation — discrete-time mesoscopic LTM. Credibility — adequate; recent preprint.

#### R0025

**Title:** *A Node Model Capturing Turning Lane Capacity and Physical Queuing for the Dynamic Network Loading Problem*  
**Abstract:** Develops a dynamic node model with directional turning-lane queues, physical queue length, and FIFO applied at lane rather than link level. The formulation divides links into running and queuing portions and integrates the resulting node behavior into dynamic network loading.
**R6 coding:** Quantity/order — continuous mass; lane-level FIFO. Differentiation — none. Main relation — physical turning-lane queues. Credibility — adequate.

#### R0027

**Title:** *A new model for multi-commodity macroscopic modeling of complex traffic networks*  
**Abstract:** Proposes the Link-Node CTM for continuous multi-commodity traffic on complex networks. It combines a multi-input/multi-output commodity-aware node model with optional capacity-drop and hysteresis behavior and a local procedure for assigning unknown commodity split ratios.
**R6 coding:** Quantity/order — continuous commodities; parameterized partial FIFO. Differentiation — none. Main relation — Link-Node CTM commodity state. Credibility — adequate; preprint.

## Representative non-nearest sample for human verification

The protocol asks the human reviewer to check a sample beyond the nearest set. The proposed five-record sample spans inherited, mature mesoscopic, finite-storage, packet-control, and secondary-review evidence:

| Record | R6 role | Main relation | Credibility |
|---|---|---|---|
| R0002 | direct | generic node foundation | strong |
| R0010 | direct | queue-based mesoscopic DTA | adequate |
| R0016 | direct | finite-lane overflow signal optimization | adequate |
| R0017 | direct | discrete packets, horizontal queues, and metaheuristic network control | adequate |
| R0024 | contextual secondary | systematic node-model coverage and taxonomy; excluded from primary-method counts | strong |

### Non-nearest sample titles and abstract summaries

#### R0002

**Title:** *A generic class of first order node models for dynamic macroscopic simulation of traffic flows*  
**Abstract:** Defines requirements for consistent first-order macroscopic node models and presents a general formulation combining demands, supplies, turning fractions, priorities, and supply-constraint interaction rules. It derives efficient node instances for unsignalized and signalized intersections.
**R6 coding:** Role — direct. Main relation — generic node foundation. Credibility — strong.

#### R0010

**Title:** *DTALite: A queue-based mesoscopic traffic simulator for fast model evaluation and calibration*  
**Abstract:** Presents an open queue-based mesoscopic dynamic traffic assignment system designed for computationally efficient network loading, evaluation, and calibration. It combines route-aware traffic propagation with practical network-analysis workflows.
**R6 coding:** Role — direct. Main relation — queue-based mesoscopic dynamic traffic assignment. Credibility — adequate.

#### R0016

**Title:** *Lane-Based Traffic Signal Simulation and Optimization for Preventing Overflow*  
**Abstract:** Incorporates physical lane-length capacity and short-lane overflow into a lane-based traffic-signal formulation. Numerical studies use the resulting queue dynamics to optimize fixed-time signals while preventing storage violations and blockage.
**R6 coding:** Role — direct. Main relation — finite-lane overflow signal optimization. Credibility — adequate.

#### R0017

**Title:** *Network Traffic Control Based on a Mesoscopic Dynamic Flow Model*  
**Abstract:** Embeds the TRAFFMED discrete-packet mesoscopic model, including horizontal queues and spillback, within a two-stage network-control method. Genetic algorithms optimize junction green times and hill climbing coordinates offsets, with results compared against benchmark tools.
**R6 coding:** Role — direct. Main relation — discrete single-vehicle packets, horizontal queues, and metaheuristic network signal control. Credibility — adequate.

#### R0024

**Title:** *A systematic review of node models for macroscopic network loading of traffic flows*  
**Abstract:** Reviews macroscopic network-loading node models identified through four scholarly databases and citation snowballing. It organizes 48 primary studies using six general principles and five extension categories and identifies continuing node-model research gaps.
**R6 coding:** Role — contextual secondary. Main relation — systematic node-model coverage and taxonomy; excluded from primary-method counts. Credibility — strong.

## Quality cautions retained for synthesis

- Seven records are preprints; their priority relevance is retained while peer-review status remains explicit.
- `adequate` does not mean unreliable. It usually reflects preprint maturity, limited replication material, stylized validation, or difficulty producing a scientifically matched executable baseline.
- AD through a fixed piecewise program, AD through smoothed discrete logic, analytic signal sensitivity, and black-box optimization are not pooled as one gradient category.
- Micro-simulator agreement is forward validation, not proof that a simulator's gradients transfer.
- Several external models contain extra physics or different controls; raw outcome rankings would be unfair without the matching conditions in `baseline_feasibility.md`.

## What approval item 4 means

Item 4 asks whether the extracted papers have been assigned sensible **comparison roles**, and whether the evidence supports carrying a particular **minimum comparison ladder** forward into R7–R8. It does **not** ask you to approve an implementation plan or commit to reproducing every paper.

### Baseline-feasibility roles

The role describes the strongest fair way in which a paper could inform a later comparison:

- **Executable external baseline:** identifiable code or a sufficiently usable implementation may permit a matched run after aligning demand, traffic physics, controls, objectives, and computational budgets. R0013 and R0014 are candidates; R0007 and R0021 may support matched forward comparisons.
- **Equation/reference comparator:** the published equations or small cases can be reproduced to compare one behavior without rebuilding the complete original system. This is appropriate for partial FIFO, lane allocation, turn queues, lane blockage, or turning-lane FIFO in R0003, R0005, R0006, R0008, R0009, R0025, and R0027.
- **Conceptual comparator:** the paper establishes that a method or capability already exists, but an experimental head-to-head comparison would be misleading or disproportionate because its task, physics, or implementation differs materially. R0012 is likely to serve mainly this role.
- **Richer forward evaluator:** a more detailed simulator can evaluate whether candidate traffic states or controls behave plausibly outside the proposed simulator. R0021 may contribute here, although the project's eventual richer evaluator is a later project decision.

One paper can support more than one role. “Feasible” means scientifically plausible enough to retain for R8 baseline selection; it does not mean implementation cost and interfaces have already been approved.

### Minimum comparison ladder

The ladder is a set of **distinct explanatory alternatives** that a credible eventual experiment should address. Each rung prevents a different overly easy explanation for a positive result:

1. **Homogeneous differentiable macro:** asks whether the complete mesoscopic stack improves on the original low-state continuous model at all. This is primarily the project's internal macro baseline, informed by R0014.
2. **Structured aggregate queue:** asks whether movement totals or calibrated partial-FIFO restrictions already explain the gain, without exact realized order. R0003 or R0008 supplies the main literature basis.
3. **Lane/storage-aware aggregate:** asks whether explicit lane groups, lane allocation, or finite turning-lane storage explains the gain, again without the proposed ledger/grid combination. R0006, R0009, or R0025 supplies this rung.
4. **Identity/order mesoscopic forward model:** asks whether the proposed continuous ordered-mass construction reproduces behavior available from individual/event mesoscopic models, and at what cost. R0007 or R0021 supplies this reference; neither is expected to provide a gradient baseline.
5. **Differentiable richer-state model — deferred second choice:** where a fair small matched case is feasible, this could ask how selective semantic discreteness compares with differentiable micro/macro hybridization. R0013 is the candidate. The user did not approve this as part of the minimum ladder: it is contextual until Question B defines a task for which the comparison is meaningful, and it cannot stand alone as the project's experiment.

The word **minimum** does not mean that five external software systems must be implemented. It means that the final baseline design must cover these five alternative explanations using the smallest defensible mix of:

- internal ablations;
- equation/reference cases;
- executable external models; and
- clearly labeled conceptual comparisons.

For example, the structured-queue and lane/storage rungs might be implemented as internal ablations faithful to published equations rather than as complete reproductions of the original authors' software.

### What approving item 4 does and does not approve

Approval would mean:

- R6 has correctly identified the relevant comparison roles and confounding explanations;
- R7 snowballing and R8 synthesis should test and refine this ladder;
- the final review should not recommend a macro-only comparison if that would leave movement-queue or lane/storage alternatives uncontrolled.

Approval would **not** mean:

- approving any simulator implementation or milestone amendment;
- requiring all named papers to be reimplemented;
- freezing which exact paper represents each rung;
- approving Question B's downstream task;
- deciding that R0013 or another external model is technically fair before a later matching assessment.

Thus item 4 is an approval of the **logic used to select future baselines**, not approval of the future experiment itself. The detailed paper-by-paper feasibility assessment is in `baseline_feasibility.md`.

## R6 closure decision

The user approved the codebook, the nearest and non-nearest coding, and minimum ladder points 1–4. Point 5 was explicitly stashed as a second-choice hybrid ablation: it remains relevant literature and a possible later comparison, but is not a minimum experiment, cannot serve as a standalone task, and must wait for Question B's task definition before feasibility is reconsidered. This refinement does not change screening, extraction, or the nearest-predecessor classification.

R6 is closed and R7 may proceed.

## User approval requested

Please approve or correct these four items:

1. the frozen codebook and the distinctions among identity, order, quantity, storage, derivative construction, and external validation;
2. the extracted coding of the 13 nearest predecessors shown above;
3. the five-record non-nearest verification sample and the qualitative credibility judgments;
4. the baseline-feasibility roles and minimum comparison ladder points 1–4; point 5 is deferred as recorded in the closure decision.

Approval closes R6 and opens R7 citation snowballing. Any factual correction can be applied locally without reopening R5 unless it changes eligibility or nearest-predecessor status.
