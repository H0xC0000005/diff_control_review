# Minimal feasibility finding — RM3

Date: 2026-09-14
Status: Provisional evidence synthesis at the user checkpoint. Detailed formulation has not started.

## Recommendation

**Do not yet promote ramp metering to the second scientific task.** A first-order aggregate ramp-control task is a credible modeling possibility, so explicit microscopic lane changes and an independent speed state are not universal prerequisites. However, this minimal pass has not established a compatible scenario in which the project's selectively retained order/access information is scientifically diagnostic beyond strong aggregate lane/storage alternatives. This is an insufficient-evidence finding on diagnosticity, not proof that ramp metering is unsuitable in all forms.

| Decision axis | Finding |
|---|---|
| Physical/model compatibility | Plausible for aggregate ramp flow, queues and merge supply; exact project adapter remains unverified |
| Scientific diagnosticity | Not established for the minimal single-ramp/common-destination case |
| Evidence feasibility | Useful open primary sources and operational examples exist; site calibration and intervention matching remain unresolved |
| Promotion to detailed formulation | Not recommended yet; request a decision on the narrow missing-mechanism question |

## Ramp-control primer

A ramp meter regulates the rate at which waiting ramp traffic enters a freeway. Holding vehicles can change where congestion forms and which traffic receives limited capacity. A fair system objective must account for the held traffic as well as freeway traffic. A local feedback rule adjusts releases from nearby measured conditions; an open-loop plan prescribes releases over time. These choices create different derivative paths: optimizing feedback parameters includes the dependence of future controls on earlier traffic states.

## Evidence that changes the discussion

**Aggregate modeling and conventional feedback.** Schmitt, Ramesh and Lygeros define a first-order CTM with density and ramp-queue states, metering bounds and a total-time objective (§2). Their ramp model assumes that freeway congestion does not prevent commanded ramp admissions. Their ALINEA implementation uses integral feedback (§5.1); the optimality discussion is conditional on model properties. This rebuts a universal need for microscopic lane changes or an independent speed state, while also showing why the assumptions cannot be imported into a ramp-spillback experiment unchanged. [RM0002 full paper](https://arxiv.org/pdf/1611.06766).

**Richer freeway mechanisms have additional costs.** Cao, Nilsson and Coogan explicitly add binary congestion memory for capacity-drop hysteresis (§II.B). That is a new dynamic assumption relative to the project's fixed triangular backbone; ordinary supply restriction is not sufficient evidence that hysteresis has been represented. [RM0003](https://arxiv.org/pdf/2106.10347).

**Lane detail is possible at an aggregate level, but is not free.** Nagalur Subraveti et al. use lane-specific CTM, lateral incentive flows and a capacity-drop extension (§2.1). They also give ramp entry priority that avoids mainline spillback onto the ramp. This is a useful boundary example, not a project-compatible implementation of ordered local accessibility. [RM0004](https://onlinelibrary.wiley.com/doi/10.1155/2021/8638523).

**A common architecture is possible in principle.** Official POLARIS documentation describes an LTM-derived mesoscopic model with both merge and traffic-signal nodes. Its integer vehicles and priority-token transfers make it an architectural precedent, not an admissible continuous-mass derivative baseline. [RM0007](https://polaris.egs.anl.gov/polaris/theory/traffic_flow/models/mesoscopic_model.html).

**Real deployments support relevance, not automatic reproducibility.** FHWA documents Twin Cities meter operation and subsequent queue-management changes. This establishes operational relevance, but does not supply this project with a calibrated, isolated test of local order. [RM0005](https://ops.fhwa.dot.gov/bn/resources/case_studies/minnstp_mn.htm).

## Responses to the colleague's reasons and the user's concerns

| Statement | Assessment |
|---|---|
| Ramp metering is established | Supported; establishment alone does not establish diagnostic value for this simulator |
| American examples can be imported | Documented cases exist; simulation-ready geometry, demand and local behavior calibration were not verified |
| PID-type control already works well | Refine the claim: inspected evidence supports integral ALINEA and conditional near-optimality; not every PID controller in every regime |
| Formulation/gradient path is simpler than TSC | Possible for a chosen scalar action; not demonstrated as a general fact. Feedback and dynamic horizons can still create long state-dependency chains |
| Multi-lane blockage/spillback makes the task relevant | Plausible motivation; must identify which mechanism is represented and why aggregate lane/storage state is insufficient |
| Limited personal experience makes it unsuitable | Not a scientific veto; an introductory source/model account can reduce this cost |
| Lane changes are necessarily required | Too broad for aggregate control tasks; their necessity remains credible for particular lane-sensitive mechanisms |
| Explicit speed must be modeled | Distinguish fixed speed parameters or derived observables from independently evolving speed. The inspected first-order task provides a counterexample to universal necessity |

## Why diagnosticity remains the limiting issue

The following is reviewer reasoning, not a theorem attributed to a source. In a minimal merge where all traffic has the same downstream movement and identical service eligibility, permuting route labels within an incoming FIFO stream need not change aggregate attainable discharge. A continuous ledger can preserve those labels without making them behaviorally relevant. Ramp queue storage can matter, yet a storage-aware aggregate baseline may already retain it.

This does not rule out more informative ramp cases. It means that the presence of queues or a merge does not, by itself, identify a selective-information experiment. A proposed positive case must name the distinct eligibility/access condition, how retained state determines it, the credible aggregate competitor, and an independent expected contrast. Otherwise differences could be caused by a chosen capacity-drop law, merge priority, boundary accounting or lane-changing model rather than selective discreteness.

A local finite acceleration/merge zone with lane access is a possible direction to examine. It is not yet supported as a complete in-scope operator/experiment by this pass. Adding a nearby exit or lane-specific route restriction might create distinguishable movements, but it also adds scenario and access assumptions; it must be justified rather than quietly introduced to reproduce the TSC case on a freeway.

## What this pass did not do

Six focused queries and bounded source follow-up produced eight tracked records, with method sections inspected for the core and boundary sources. This is sufficient for the qualified gate finding, not a comprehensive literature verdict. No model equivalence test, gradient run, simulation-ready data audit or broad discovery campaign was performed. No current paper demonstrates the full project-specific compatibility/diagnosticity chain in the evidence inspected here.

See `candidate_shortlist.md` for the user choices and `compatibility_matrix.md` for component implications. The next decision is whether to authorize a narrowly targeted attempt to resolve diagnosticity or close/defer on the present evidence. Detailed task formulation should wait.
