# Formula provenance in the urban reports

28 October 2026. This inventory covers the unchanged 23 main and 35 companion equation labels in the clean reports. Source relationships remain explicit beside the formulas. The clean edition removes revision colors and private review/implementation wording; all previous versions remain preserved.

“Reused” identifies an inherited project transcription or representation. “Adapted/inspired” identifies a literature idea while distinguishing the present equation. “Defined here” identifies a closure, geometry or convention chosen for this task; it is not a claim of worldwide methodological novelty. “Derived” identifies algebra or calculus applied to stated model assumptions. A formula can have more than one of these relationships.

[Main report](../../reporting/research_readiness/urban_compact_methods_report_clean.pdf)

[Companion](../../reporting/research_readiness/urban_methodology_specification_clean.pdf)

## Exact project sources and literature scope

The [M0 technical specification](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_0_ltm_baseline.md) supplies the verified triangular-FD/LTM discrete domain, histories, sending/receiving, conservative bookkeeping and population-time quadrature. The [M1 specification](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md) supplies continuous route mass and actual-admission affine timing. The [M2 representation record](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md) supplies the fixed cumulative-mass bins and ledger-authoritative reconstructed grid; its implementation status is not changed here.

The [component provenance record](urban_feedback12_component_provenance.md) preserves the literature reading depth: Gong motivates lane equilibrium; Han motivates average signal service; Tampere supplies node feasibility/conservation requirements; Daganzo supplies cell-based lineage; de Souza supplies the identity-tracking precedent. Their complete algorithms/theorems are not silently imported. Wei, Gong and Liu–Chang also identify comparison directions rather than equations of the ordered model. Official SUMO documentation supplies the reference interface and trip-output meanings. This pass makes the recorded relationships explicit; it does not claim a new full-paper reproduction.

## Companion equations

| Label | Relationship | Exact role/source |
|---|---|---|
| eq:action | Adapted interpretation; task-defined bound | Han et al. motivate average signal service; the fixed four-group simplex and physical-cap minimum instantiate this task. |
| eq:geometry | Project task definition | The representative two-feeder/three-terminal graph and fixed permissions define the physical scenario. |
| eq:history | Reused project discretization | The M0 affine reconstruction of stored cumulative boundaries is retained; this is not a new urban wave law. |
| eq:sending | Reused LTM transcription | The verified M0 discrete transcription of Yperman supplies the sending/eligibility law; only the section graph changes. |
| eq:receiving | Reused LTM transcription | The same M0/Yperman lineage supplies delayed-space receiving on each physical section. |
| eq:grid | Project representation; derived overlap | M1/M2 supply continuous ordered mass and fixed rank bins. Interval intersection derives omega/M/n. CTM supplies cell-based inspiration, not these equations. |
| eq:allocation | Inspired idea; project-defined objective; derived solution | Gong et al. motivate lane equilibrium. The queue-mass quadratic cost and constrained per-packet entry problem are specified here; their capped solution is derived here. |
| eq:allocation-update | Derived resource identities | Subtract actual admitted amounts from packet/sending/receiving budgets and add them to perceived receiving loads in the allocation law. |
| eq:physical-access | Project-defined access predicate | The declared topology and exact realized-lane FIFO determine whether an older resident blocks the legal outgoing path. |
| eq:receiving-rate | Project-defined average convention | The selected constant-rate convention converts the timestep LTM receiving allowance into a rate by dividing by timestep length. |
| eq:leg-sharing | Project-defined priority rule | Green-weighted capped grants are this model's rule. Tampere et al. supply feasibility/conservation requirements, not this priority equation. |
| eq:lane-sharing | Project-defined priority rule | Equal uncapped lane rates within a granted leg are selected for this model; capped portions are reused among current heads. |
| eq:head-time | Derived from model stopping constraints | The earliest head clearance, sending exhaustion or timestep end determines how long the current-head rates apply. |
| eq:service-amount | Derived transfer identity | Sum rate times duration for the tracked lane/movement stream over the timestep intervals. |
| eq:head-example | Derived application of the service law | Apply the service-amount sum to a left head followed by through traffic, with nonbinding physical/receiving bounds. |
| eq:head-example-derivative | Derived by calculus | Differentiate the preceding diagnostic along a feasible left/through green transfer; this is not a borrowed paper equation or empirical evidence. |
| eq:state-update | Reused conservative bookkeeping | M0/M1 cumulative-count and paired-transfer bookkeeping preserves each physical mass and route ownership. |
| eq:entry-time | Derived from reused timing construction | M1 uniform boundary reconstruction plus actual admitted mass rank gives the front/tail entry endpoints. |
| eq:storage-bound | Derived implication | The inherited sending/receiving bounds and paired state update imply the storage range under the existing timestep domain. |
| eq:mass-identity | Derived conservation identity | Sum all paired updates from empty loading, including source waiting, release and sink exit, also route by route. |
| eq:allocation-derivative | Derived by calculus | Differentiate the allocation minimum, lane rule and total mass constraint on fixed active categories. |
| eq:allocation-level-derivative | Derived algebraic solution | Substitute the lane derivative cases into their total mass balance and solve for the common filling-level derivative. |
| eq:scan-derivative | Derived by calculus | Differentiate the resource updates in eq:allocation-update, retaining sequential responses. |
| eq:sharing-derivative | Derived by calculus | Differentiate the fixed-category leg-sharing law and its total rate balance. |
| eq:sharing-level-derivative | Derived algebraic solution | Substitute capped/free leg responses into their total rate balance and solve for the multiplier derivative. |
| eq:service-derivative | Derived by the product rule | Differentiate the service-amount sum, retaining both rate and duration channels. |
| eq:duration-derivative | Derived by selected-branch calculus | Differentiate the selected head-time branch, including head clearance, sending exhaustion and the remaining timestep. |
| eq:grid-derivative | Derived representation calculus | Differentiate cumulative packet boundaries and their fixed-bin overlaps in eq:grid; structural metadata remain fixed. |
| eq:eligibility-derivative | Derived from uniform readiness and calculus | Uniform readiness defines the displayed interior fraction; quotient/product rules give its fraction and ready-mass responses. |
| eq:entry-derivative | Derived by the quotient rule | Differentiate the front endpoint of eq:entry-time at fixed timestep boundaries; the tail uses the same construction. |
| eq:ltm-derivative | Derived by selected-branch calculus | Differentiate inherited sending/receiving with sensitive stored counts and fixed query times/interpolation weights. |
| eq:tst | Reused project objective quadrature | M0 supplies source-plus-road population time, applied here to all disjoint sections and complete released demand. |
| eq:state-sensitivity | Derived by the chain rule | Differentiate the project-defined composed timestep map and sum the derivatives of its stated population-time charges. |
| eq:exit-objective | Derived conservation rewrite and calculus | Combine mass conservation with the population-time objective, then differentiate with fixed demand, timestep and common horizon. |
| eq:reference-action | Derived task-to-reference conversion | The fixed usable cycle-time budget and green-fraction definition give the conversion. SUMO documentation supplies program encoding and output meanings, not this budget algebra. |

## Main equations

The main formula below inherits the same provenance as its companion counterpart, with the head-time derivative showing the head-clearance branch only.

| Main label | Relationship | Companion/source |
|---|---|---|
| eq:compact-domain | Derived FD identity; reused numerical domain | Triangular FD and timestep domain in the M0 transcription; inline domain in the companion. |
| eq:compact-sending | Reused LTM transcription | eq:sending |
| eq:compact-receiving | Reused LTM transcription | eq:receiving |
| eq:compact-allocation | Inspired idea; project-defined objective; derived solution | eq:allocation |
| eq:compact-action | Adapted interpretation; task-defined bound | eq:action |
| eq:compact-leg-sharing | Project-defined priority rule | eq:leg-sharing |
| eq:compact-lane-sharing | Project-defined priority rule | eq:lane-sharing |
| eq:compact-head-time | Derived from model stopping constraints | eq:head-time |
| eq:compact-service-amount | Derived transfer identity | eq:service-amount |
| eq:compact-update | Reused conservative bookkeeping | eq:state-update |
| eq:compact-entry | Derived from reused timing construction | eq:entry-time |
| eq:compact-grid | Project representation; derived overlap | eq:grid |
| eq:compact-tst | Reused project objective quadrature | eq:tst |
| eq:compact-chain | Derived by the chain rule | eq:state-sensitivity |
| eq:compact-sharing-derivative | Derived by calculus | eq:sharing-derivative |
| eq:compact-sharing-level-derivative | Derived algebraic solution | eq:sharing-level-derivative |
| eq:compact-service-derivative | Derived by the product rule | eq:service-derivative |
| eq:compact-head-time-derivative | Derived by selected-branch calculus | eq:duration-derivative |
| eq:compact-grid-derivative | Derived representation calculus | eq:grid-derivative |
| eq:compact-allocation-derivative | Derived by calculus | eq:allocation-derivative |
| eq:compact-allocation-level-derivative | Derived algebraic solution | eq:allocation-level-derivative |
| eq:compact-entry-derivative | Derived by the quotient rule | eq:entry-derivative |
| eq:compact-objective-derivative | Derived conservation rewrite and calculus | eq:exit-objective |

All derivative expressions retain their fixed-category/selected-branch conditions. No source attribution establishes numerical gradient accuracy, traffic fidelity or downstream control usefulness; those are the distinct validation questions already defined by the study.
