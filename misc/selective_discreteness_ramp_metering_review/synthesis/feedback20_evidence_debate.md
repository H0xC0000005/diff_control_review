# The literature supports differentiable freeway control, but not B1-P as an orthogonal second task

Date: 2026-09-15  
Evidence cutoff: 2026-09-15  
Status: accepted in substance by feedback 21; RM4 closed against promotion; retained as the evidence basis for the approved colleague brief. RM5 and the review closed on 2026-09-15; see `../reporting/closure_record.md`.

## Executive conclusion

The feedback's central objection is supported. **B1-P should not be promoted as the project's parallel, orthogonal second downstream task.** It remains scientifically coherent as a deliberately elementary transfer test, but that is a smaller role: it asks whether order metadata survives an upstream-control/long-link/downstream-service chain. It does not isolate a second mesoscopic primitive or a second independent hypothesis beyond the ordered-access issue already central to the traffic-signal task.

Two qualifications are important.

First, the preceding audit did not require a large change to an already implemented milestone. It found that B1-P can avoid reopening M1 only by imposing non-overlapping input eligibility intervals, while its downstream service still depends on the unresolved M3 operator. The problem is therefore less "large implementation change already required" than **a narrow admissible construction plus unresolved shared-method dependence**. Ordinary overlapping flow or realistic multilane exit access would require the larger modeling changes that the feedback is concerned about.

Second, the statement that differentiable traffic-simulation work has only been evaluated on urban networks is true only for a narrow naming convention around recent end-to-end automatic-differentiation simulators. The adjacent optimal-control literature contains direct freeway examples. Reilly et al. compute a discrete-adjoint gradient through a Godunov-discretized first-order network and apply it to coordinated ramp metering on I-15. Gu et al. smooth CTM minimum operators to enable gradient-based ramp-metering MPC. Goatin et al. extend discrete-adjoint computation to multiclass networks with merges, diverges and buffers. Poole and Kotsialos use automatic differentiation for METANET freeway-model calibration. This correction, however, **weakens rather than strengthens B1-P as a distinct project task**: it shows that useful freeway gradients are already available with macroscopic models and without exact mesoscopic order.

The defensible disposition is therefore:

- reject B1-P as a primary parallel task with orthogonal hypothesis value;
- retain it, at most, as an optional post-M3 transfer/ablation fixture if testing long-range preservation of ordered metadata becomes useful;
- do not proceed to the planned RQ3–RQ5 task formulation now;
- do not infer that no freeway application could ever qualify. The bounded result is that the reviewed B1 family does not qualify under the current project contracts and desired role.

## 1. What mesoscopic ramp-metering studies add

"Mesoscopic" is not a single state definition. The reviewed literature uses the label for several materially different constructions, so the retained state—not the label—must be compared with this project.

| Literature family | Representative evidence | Added behavior relative to a coarse aggregate model | Why it matters for ramp metering | Relation to this project |
|---|---|---|---|---|
| Large-scale mesoscopic DTA | Lee et al. (RM0027); FHWA DTA guidance (RM0029) | Individual or packet route/departure-time progression, dynamic assignment, shorter update intervals and network-wide diversion | Captures both local and regional effects of control, including demand redistribution and corridor spillovers | Valuable, but dynamic route/departure choice is outside the fixed-route initial mainline. It does not establish exact within-queue order as necessary. |
| Stochastic/event-based mesoscopic operations | Wei (RM0028) | Stochastic event timing and vehicle operations on mainline, entrance and exit ramps; spatial-temporal state interactions | Provides a computational test bed between aggregate equations and car-following simulation | Its individual/stochastic semantics are not directly importable into deterministic continuous-mass differentiation. The inspected evidence does not isolate route order. |
| Lane-refined or vehicle-tracking mesoscopic tools | NCHRP/FHWA guidance (RM0029) | Individual vehicles or refined vehicle groups, simplified traffic-flow/car-following behavior, sometimes lane-by-lane queues; usually no detailed gap acceptance or lane-changing theory | Supports larger areas and longer periods than microsimulation while retaining route shifts and operational time resolution | This is closer in architectural spirit, but the principal benefit is scale plus route/temporal resolution, not the project's exact ordered local ledger. |
| Hybrid mesoscopic–microscopic evaluation | FHWA multi-resolution guidance; microscopic ramp studies in the existing corpus | Regional mesoscopic loading is coupled to microscopic junction/merge behavior where gaps, lane changes and driving interactions matter | Avoids paying microscopic cost everywhere while resolving operational merge details locally | This pattern is evidence that realistic ramp merges often need a different local physics stack; it does not show that a point-node ordered ledger substitutes for those dynamics. |

Lee et al. give the clearest modern ramp-specific mesoscopic example. They integrate DTALite-style mesoscopic DTA with a traffic-responsive ramp-metering strategy to assess local and network-wide impacts over a large Maryland network, emphasizing minute-by-minute demand–supply interaction. The distinctive gain is **network scale and dynamic assignment**, not fine FIFO order at one merge or exit.

Wei's earlier study uses a stochastic, event-based mesoscopic simulator covering mainline, entrance-ramp and exit-ramp vehicle operations to evaluate a spatiotemporal neural ramp controller. It supports the existence of mesoscopic ramp-control test beds, but the controller contribution and the simulation-resolution contribution are coupled; the published abstract/indexed sections do not demonstrate that exact queue rank is the reason for the control result.

The practitioner guidance is consistent with that division of labor. FHWA describes mesoscopic/DTA models as useful for regional dynamic diversion and route shifts, while microscopic models resolve detailed junction control, lane changing and gap acceptance. The NCHRP evidence describes mesoscopic models as representing individual vehicles with simplified flow or car-following rules, often without lane-changing and gap-acceptance theories, and stresses their larger geographic/temporal scope.

### Answer to concern 1

The main mesoscopic contributions in ramp-metering work are:

1. dynamic route and departure-time response to control;
2. individual or packet progression with finer event/time resolution;
3. stochastic demand/vehicle realization;
4. lane-refined queues in some tools;
5. scalable corridor or regional evaluation, often inside a multiresolution workflow.

These are important relative to coarse macroscopic analysis when diversion, heterogeneity, variability or spatially distributed impacts are decision-relevant. **The reviewed works do not identify exact downstream route-mass order as a standard or dominant mesoscopic requirement for ramp metering.** Most of the clearest mesoscopic advantage lies in route choice and scale, which the project's fixed-route initial mainline deliberately does not model. The local phenomena that make ramp operations strongly non-aggregate—gap acceptance, lane changing, merge safety and some capacity-drop mechanisms—usually fall on the microscopic or hybrid side and cannot be compressed into the current generic node solver without a new modeling claim.

## 2. Differentiable and gradient-based ramp metering already exists

The literature should be separated by derivative contract rather than by whether authors use the modern phrase "differentiable simulation."

| Derivative construction | Representative work | Direct ramp task? | Main contribution | Consequence for this review |
|---|---|---:|---|---|
| Exact discrete adjoint of the numerical first-order model | Reilly et al. (RM0024) | Yes | Efficient gradients for many time-dependent controls; linear memory/computational scaling under the stated sparse network structure; coordinated I-15 application and MPC study | Direct predecessor for differentiable macroscopic ramp control; a strong baseline, not support for selective order |
| Smoothed CTM optimal control | Gu et al. (RM0026) | Yes | Smooth approximation of CTM minimum operators, convergence analysis toward the primal CTM optimum, and online MPC solution | Shows gradient-based ramp control is already viable, while also illustrating that smoothing changes the numerical/forward contract and must be compared carefully |
| Piecewise discrete adjoint for multiclass network flow | Goatin et al. (RM0025) | Ramp metering is an available priority-control interpretation; numerical example is broader network control | Exact gradient of the discretized objective away from branch boundaries, multiclass merges/diverges/buffers, efficiency with many controls | Extends the aggregate/multiclass gradient baseline; it still uses class proportions/aggregate junction rules rather than exact local order |
| Automatic differentiation for freeway-model calibration | Poole and Kotsialos (RM0030) | No; freeway calibration | AD through METANET for parameter estimation and Jacobian-based sensitivity insight | Establishes a freeway-specific AD use beyond control, but again at macroscopic resolution |
| End-to-end reverse-mode AD traffic simulator | Seo (cross-package T0001/R0014) | Ramp metering is future-applicability only; demonstration is pricing | One computation graph for simulation, route choice, calibration/optimization applications; avoids manual adjoint maintenance | Engineering motivation for AD, not direct evidence for B1-P or a completed ramp-metering experiment |

Reilly et al. are the decisive correction to the urban-only premise. Their work is functionally a differentiable first-order freeway simulator for a specific optimal-control contract, even though the derivative is manually derived as a discrete adjoint rather than generated by PyTorch/JAX. They show why gradients can matter: finite differences require a forward run per perturbed control, whereas an adjoint exploits the time-sparse computation to obtain the gradient efficiently for coordinated, time-varying meters. Their I-15 experiment reports improvement over ALINEA under reasonable input noise, but also reports that the model-based adjoint loses usefulness when boundary data become severely noisy. That is a useful warning: derivative efficiency does not remove model/forecast dependence.

Gu et al. address a different obstacle. CTM minimum operators are nonsmooth, so they replace them with smooth approximations and solve a sequence of online ramp-control problems. This is directly relevant to the project's methodological stance: a smoother optimization problem can be valuable, but the smoothing is part of the scientific contract, not a neutral implementation detail. It cannot be counted as evidence that exact piecewise gradients and smoothed gradients are interchangeable.

Goatin et al. show in 2026 that a discretize-then-optimize adjoint can handle multiclass conservation laws, merge/diverge coupling and congestion buffers. Their paper states that applying the adjoint to the actual discretized equations gives the exact gradient of the numerical objective on the active piecewise branch. The paper is adjacent rather than a direct B1-P predecessor: it uses class aggregate states and its numerical demonstration is not the proposed ramp/downstream-order experiment.

### Answer to concern 2

The major contribution of differentiability in ramp metering is primarily **computational and integrative**, not a new traffic behavior:

- gradient cost can scale much better than finite differences as the number of time-dependent meters or parameters grows;
- gradient-based MPC and coordinated control become more plausible in real time;
- the same sensitivity machinery can support calibration, parameter identification and control;
- end-to-end AD reduces the manual derivative work and error risk when the forward model changes;
- sensitivity paths expose which upstream controls influence downstream objectives.

None of these benefits by itself establishes a need for mesoscopic order. They are already demonstrated on first- or second-order macroscopic freeway models. To support this project, a ramp task would need to show not merely that gradients help, but that **the gradient produced using selectively retained mesoscopic information is materially more useful than gradients from strong aggregate and cohort-memory models**.

## 3. Is there a strong freeway-specific reason for differentiable simulation?

There is a legitimate freeway case, but it is conditional.

### The positive case

Freeway corridors can have many meters, long time horizons, interacting queues and nonlocal bottlenecks. A reverse/adjoint gradient is well matched to many time-indexed controls and one scalar system objective. Reilly et al. demonstrate this computational motivation directly. Freeways also have mature conservation-law models, so the forward dynamics can be cheaper and more structurally differentiable than microscopic vehicle systems. Calibration of many spatial parameters, as in the METANET AD work, is another credible use. Joint optimization of meters, speed limits, tolls or learned control policies can further increase the number of decision variables.

### The limiting case

The same maturity makes the novelty bar high. For standard first-order ramp-metering objectives, strong alternatives already include local feedback controllers, monotonic best-effort laws, linear/convex reformulations under declared assumptions, MPC, and discrete adjoints. RM0002 reports that a distributed nonpredictive controller satisfies its sufficient optimality conditions on most tested real-data cases and that violations produced a negligible apparent gap; RM0001 develops efficient near-global ACTM plans. These are not universal proofs that macro control is sufficient, but they mean a new differentiable simulator must beat more than finite differences or no control.

For one ramp and a small control vector, the scaling benefit of reverse-mode differentiation is modest. A finite-difference check, ALINEA-style feedback, direct search or a structured aggregate optimizer may already be adequate. The freeway case becomes strongest with many coordinated controls or joint calibration/control—but those settings validate scalable differentiation more directly than they validate selective mesoscopic order.

### Answer to concern 3

It is not correct to conclude that differentiable freeway control lacks precedent or motivation. The stronger conclusion is more specific:

> A differentiable freeway simulator is well motivated for high-dimensional coordination, MPC and calibration, but a **selectively mesoscopic** differentiable freeway task needs an additional representation-sensitive mechanism. Existing macroscopic gradient/control results make generic ramp metering an insufficient second-task justification.

This creates a genuine tension for the current project. The freeway mechanisms that most clearly defeat macro aggregation—safe merge gaps, lane changes, lane-specific access, heterogeneous driver interactions and some capacity-drop dynamics—are precisely the mechanisms the current node/LTM architecture does not support. The mechanisms it does support cleanly are the ones for which strong aggregate controllers and adjoints already exist.

## 4. Debate: the strongest case for and against B1-P

### Strongest case for keeping it

B1-P is not merely the signal task with freeway names. The control acts upstream, long-link propagation intervenes, and downstream service remains fixed. It therefore tests a real model-chain question: can route/order metadata survive merge chronology and propagation well enough to change a useful upstream metering sensitivity? A positive, equivalent or negative result would all be interpretable if the aggregate-cohort baseline ladder is retained. The point-diverge itself also has literature precedent, and the non-overlap restriction prevents an invented chronology from being mistaken for physical overlapping merge order.

This makes B1-P a credible **transfer stress test**. It could be valuable after M3 to ensure that the selected ledger/order realization composes with LTM propagation and remote control.

### Strongest case against promotion

The desired second task is supposed to test a distinct and reasonably orthogonal project hypothesis. B1-P does not meet that bar:

| Desired property | B1-P evidence | Gap |
|---|---|---|
| A distinct selectively retained mesoscopic behavior | Uses the same exact-versus-relaxed ordered-service primitive owned by M3 | New causal placement, not new information/hypothesis |
| Ordinary traffic relevance without contrived admissibility | Requires non-overlapping mainline/ramp eligibility intervals to avoid an unsupported total merge chronology | Mechanism is clean only on a narrow, deliberately scheduled subset |
| Compatibility without new physics | Narrow form is compatible; overlapping or realistic multilane form is not | Generalization reopens merge chronology and/or adds lane dynamics |
| Literature affinity to mesoscopic ramp-metering value | Literature emphasizes DTA, route/departure response, stochasticity, scale and sometimes lane refinement | Exact downstream rank is not established as the characteristic mesoscopic ramp mechanism |
| Clear advantage over macro baselines | Macro CTM/LWR/METANET controllers, adjoints, cohort FIFO and composition-memory models are strong | Selective order may add no decision value after time/cohort refinement |
| Independent failure interpretation | Failure may reflect the same M3 ordered-access realization or its compression as the signal task | Weak orthogonality at the evidence level |
| Distinct differentiability contribution | Upstream/downstream gradient path is different, but macroscopic ramp gradients already exist | Demonstrates reuse of differentiation, not why selective discreteness is needed |

The point-diverge was selected because the immediate merge case lacked order-sensitive value within scope. The non-overlap rule was then added because simultaneous continuous inputs lack a source-backed unique physical total order. These are scientifically honest restrictions, but together they show that the candidate was **constructed around two incompatibilities** rather than recovered as a natural, literature-established mesoscopic ramp task.

### Answer to concern 4

**B1-P is not acceptable as the primary parallel second task with distinct, orthogonal hypothesis value.** It is acceptable only in the weaker role of an optional transfer/ablation fixture.

The precise gap is:

1. **Application orthogonality:** present. The action is ramp admission rather than green allocation, and the controlled location is separated from the constrained service location.
2. **Causal-chain orthogonality:** partial. It adds merge chronology and long-link propagation before ordered service.
3. **Representation-hypothesis orthogonality:** absent. The decisive retained information is still route-labelled order at a service restriction—the M3/TSC question.
4. **Operational representativeness:** weak. The restriction that makes chronology valid excludes ordinary overlapping continuous arrivals; realistic lane access would add unsupported physics.
5. **Literature-native mesoscopic justification:** weak. The established mesoscopic benefits for ramp evaluation predominantly concern dynamic assignment, route/departure response, stochastic realization and geographic scale.
6. **Incremental project value:** bounded. It can test composition of already selected components, but it cannot independently justify the selective-discreteness program.

## 5. Important distinctions and possible misunderstandings

### Mesoscopic is not synonymous with ordered FIFO rank

Many mesoscopic simulators track individual vehicles or packets mainly to support route choice and event timing. Others use lane-level groups or simplified car-following. The project's continuous mass plus selected semantic metadata is a specific mesoscopic hypothesis, not a default property of every model called mesoscopic. A literature paper's use of a mesoscopic tool therefore does not automatically support the ledger/order representation.

### Differentiability is an interface, not a traffic mechanism

A simulator can provide useful gradients through a manual discrete adjoint, automatic differentiation, analytic sensitivity equations or a smoothed surrogate. These methods have different forward and backward contracts. Their common benefit is access to sensitivities; none determines which traffic state is physically necessary.

### A strong controller result is not a representation result

A ramp controller can improve travel time in a mesoscopic or microscopic simulator without proving that its performance required mesoscopic detail. To establish representation value, the same action, objective, demand, physical parameters and optimization budget must be compared across matched aggregate/cohort/exact-order models.

### Orthogonality must be judged at the hypothesis level

Traffic signals and ramp meters are different applications. That alone is insufficient. If both tasks turn on the same claim—ordered route mass changes attainable service at a restricted node—then they are two contexts for one hypothesis. A second application can improve external validity, but it is not an independent scientific pillar.

### The negative finding is bounded

This audit does not prove that no freeway task can ever provide orthogonal selective-discreteness value. It finds that the plausible alternatives divide into two groups:

- project-compatible effects that are already well represented by aggregate models or reuse the M3 order primitive; and
- strongly mesoscopic freeway effects that require route choice, stochastic vehicles, lane changing, gap acceptance, merge safety, multiclass dynamics or new capacity-drop physics.

Finding a new freeway candidate would therefore require a new task-family search and an explicit decision about which additional model capability may enter. It should not be treated as a routine refinement of B1-P.

## 6. Recommendation and recorded decision

The current D1 formulation recommendation is withdrawn. Do not open RQ3–RQ5 formulation under E1.

The recommendation was **E2 with preservation**:

- defer B1 as a primary parallel task;
- preserve `d1_point_diverge_verdict.md` as a historical mechanism audit rather than deleting it;
- preserve B1-P as an optional post-M3 transfer/ablation concept, not a promised experiment or milestone;
- close RM4 after user acceptance;
- if the user still wants a freeway-centered parallel task, open a separate candidate-discovery decision rather than stretching B1-P.

Feedback 21 accepted this conclusion: RM4 is now closed, the remaining B1-P formulation is halted, and RM5 is open only for the colleague brief and final review closure. No project file, milestone contract, implementation plan or simulator behavior is changed by the decision.

## Sources introduced or reclassified in this pass

- RM0024 — J. Reilly et al., “Adjoint-Based Optimization on a Network of Discretized Scalar Conservation Laws with Applications to Coordinated Ramp Metering,” *JOTA*, 2015, doi:10.1007/s10957-015-0749-1. Public manuscript archived.
- RM0025 — P. Goatin, A. Klar, and C. Mezquita-Nieto, “Discrete adjoint gradient computation for multiclass traffic flow models on road networks,” *Optimization and Engineering*, 2026, doi:10.1007/s11081-026-10122-4. Open version of record archived.
- RM0026 — C. Gu et al., “A Smoothing Method for Ramp Metering,” *IEEE T-ITS*, 2022, doi:10.1109/TITS.2021.3123815. Publisher/author-institution abstract and metadata inspected.
- RM0027 — M. Lee et al., “Analyzing Simulation-Based Active Traffic Management Impact on a Large-Scale Regional Network,” *TRR*, 2019, doi:10.1177/0361198119845650. Publisher abstract and references inspected.
- RM0028 — C.-H. Wei, “Analysis of artificial neural network models for freeway ramp metering control,” *Artificial Intelligence in Engineering*, 2001, doi:10.1016/S0954-1810(01)00019-X. Publisher-indexed abstract and method excerpts inspected.
- RM0029 — FHWA DTA guidance and NCHRP active-traffic-management evidence on model-resolution roles. Official pages/full report precursor inspected.
- RM0030 — A. Poole and A. Kotsialos, “Second order macroscopic traffic flow model validation using automatic differentiation with resilient backpropagation and particle swarm optimisation algorithms,” *TRC*, 2016, doi:10.1016/j.trc.2016.07.008. Author-repository text and bibliographic metadata inspected.

Detailed access and inference boundaries are recorded in `../archive/metadata/feedback20_sources.md`.
