# Global assumptions: source, compatibility and claim-dependency audit

Date: 2026-10-19. **Approved bounded audit executed; GA-G1 delivered.**
This audits premises of the current standalone asymmetric task. No new paper,
traffic law, calibration, simulator or numerical experiment is introduced.
“Accounted for” below means traced and checked at methodological review
scope, not physically validated or machine-proved.

## Scientific authority and reading scope

The current task uses accepted AS1 independent initialization and retained
forward domain, accepted AS2 information/history semantics, and the delivered
AS3 action/sensitivity contract. The older feedback-8 core/forward equations
remain the mechanism reference, with AS1 replacing their initial A=B formula
and AS3 qualifying later action/gradient claims. Old S13 time-hazard/batch
service equations and advice-normalized trial work are historical references,
not current laws. Earlier source audits are reused at their recorded reading
limits; this pass does not claim fresh reading of the underlying papers.

| Source key | Exact material examined in this audit |
|---|---|
| **AS1** | [Independent forward contract](../../synthesis/research_readiness/vsl_as1_asymmetric_forward_contract.tex), Sections 1–6: initialization, `eq:domain`, `eq:workdomain`, preparation, point law, causal guards, whole-forward proof, exact admissible family and claim limits. |
| **AS2** | [Information/history contract](../../synthesis/research_readiness/vsl_as2_information_and_history.tex), Sections 1–5: roles, loader and `eq:loadbounds`, complete matched fields/counts, compact reconstruction and informative receiving histories. |
| **AS3** | [Action/sensitivity contract](../../synthesis/research_readiness/vsl_as3_asymmetric_actions_and_gradients.tex), Sections 1–6: fixed inputs, positive and common-action families, auxiliary-to-selected-law argument, complete regular derivative and evidence limits. |
| **CORE** | [Consolidated core](../../synthesis/research_readiness/vsl_feedback8_math_core.tex), current-model sections corresponding to Sections 2–8 in the compiled report: domain, H1, handoff, T1, work/marks, allocation/guards and recovery. Its initial symmetry is superseded by AS1. |
| **FWD** | [Consolidated forward proof](../../synthesis/research_readiness/vsl_feedback8_math_forward.tex), compiled Sections 9–12: cutoff comparison, local contraction, derived positive budget, event control, clearance and TST. Its old initial-information reconstruction is superseded by AS2. |
| **SRC** | [Component/source map](vsl_feedback8_model_stack_source_map.md), [H1 adaptation audit](vsl_h1_source_and_adaptation_audit.md), [W-F source/ownership audit](vsl_wf_forward_source_audit.md), [recovery/overlap source boundary](vsl_re_overlap_source_and_adaptation_audit.md) and [MP6 source limits](vsl_mp6_physical_source_audit.md). |
| **SCOPE** | [Current asymmetric verification contract](../../synthesis/research_readiness/vsl_asymmetric_standalone_verification_protocol.md), [Step 3 consistency audit](../../reporting/research_readiness/vsl_as3_step3_consistency_audit.md) and [future physical-admission contract](../../synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md). |

The reading covers the complete current AS1/AS2/AS3 notes and consolidated
CORE/FWD, plus the relevant O-R causal/history derivation and archived source
audits. Formal guarantees continue to have the scope of those arguments;
the static checks here do not replace their proofs.

## 1. Recovered global premises and definitions

These IDs match the short statement intended for the report. Multiple
scientific roles are kept separate even when the prose places them nearby.

| ID and category | Actual premise or definition | Accepted location, rationale and source status | Dependence and important limit | Audit answer |
|---|---|---|---|---|
| **TD1: task definition** | Fixed 3-to-2 geometry, E/A/B roles, common finite footprint, uniform lane densities, independent lane loads, initially empty terminal/recovery and no later external inflow. | AS1 §1, `eq:initial`; §5 asymmetric family. Restricts the task to a controlled finite-cohort comparison. | Supports a simple arrival pulse and neutral initial memory. A/B equality is optional, not required. Unknown initial queues/history are outside this contract. | Accounted for; no new initialization assumption needed. |
| **TD2: action and fixed-data definition** | One bounded constant common advice; deterministic evolution; fixed initial state, prehistory, geometry and physical parameters as advice varies. | AS1 §1; AS3 §1; SCOPE. Gives a well-defined counterfactual action and derivative. | Changing a loading recipe or refitting physical coefficients with advice would change the task. No feedback/probing controller is implied. | Accounted for; state-dependent service does not mean state-dependent parameter refitting. |
| **TD3: objective definition** | Complete local population-time for every initial lane through choke exit, including all A/E waiting tails. | AS1 §4, `eq:tst`; FWD accounting section; AS3 §5.4. | Persistent effects burden unfinished followers; completed traffic has no extra own post-line travel. Initial uniform positions justify the mean-distance travel term. | Accounted for; complete accounting is not a half-clearance batch approximation. |
| **IC1: comparison definition** | Shared model/parameters and all permitted predecision channels/inference; central Level 2 omission is the realized A/B split at fixed E and continuing total. | AS2 §1 and §5; SCOPE information table. Defines the information being tested. | A derived true-state quantity revealing A, pair label or future reference trace is not a common input. Informative histories remain allowed. | Accounted for; no equal-split prior or universal concealment assumption. |
| **IC2: equal-information definition** | Compact peer receives one initial adjacent statistic in addition to Level 2 and predicts autonomously. | AS2 §4, `eq:compact`; AS1 forward uniqueness. It tests whether added representation is necessary once information is equal. | Sufficiency uses the common footprint and known initial terminal/recovery state; it does not prove a one-number dynamic-state closure. | Accounted for; equality is derived, not stipulated as an untested physical assumption. |
| **MA1: global representation** | Continuous mass, lane-specific aggregate preparation, homogeneous remaining body and first-order boundary/travel/storage ingredients. | AS1 §§1–2; CORE preparation/terminal sections; SRC H1 audit. Keeps adjacent receiving information without individual trajectories or an internal spatial grid. | Homogeneity is a chosen closure, preserved by its uniform free-motion/source equations when receiving accepts the handoff. It is not a general LTM reconstruction or full-wave merging solution. | Accounted for; approximation and conditional invariance are distinguished. |
| **MA2: global response hypothesis** | Advice changes unblocked motion and the selected FD family with fixed wave/jam parameters; work and recovery coefficients and their anchors are fixed. | AS1 `eq:fd` and `eq:workdomain`; CORE root section; SRC W-F audit. Removes a direct advice-only change in an unchanged local merge. | Ideal free response and the FD family are assumptions. Fully queued local service has no direct advice input at fixed represented state/budget. Applied compliance is not established. | Accounted for; current state mediation is compatible with the chosen response family. |
| **MA3: global interaction structure** | Early E-to-A transfer before a cutoff; early-merged mass becomes A; residual E traverses a finite no-lateral terminal and merges at the choke; B is separately served. | AS1 §§2–3, `eq:massprep`; CORE handoff and terminal sections. Separates preparation from forced service. | No separately retained early-merge recovery, other A/B exchange or explicit downstream interaction zone is modeled. Extra E work applies to residual terminal E, not origin identity. | Accounted for; the equations already determine this boundary. Making it explicit changes no law. |
| **MA4: global service hypothesis** | Equilibrium boundary marks, fixed mismatch work, free-A priority/queued-A cooperation and the selected causal transition conventions. | AS1 §3; CORE root/allocation sections; FWD event proof. Completes a single-valued point service and its queue transitions. | These are chosen constitutive rules. A may queue; cooperation also governs a queued A with free E when redistribution fits. Queue equality alone is not a birth. | Accounted for; no hidden priority timer, latch or universal free-A assumption. |
| **MA5: global recovery hypothesis** | Forced E alone deposits transient loss; finite recent mass is retained on a fixed physical normalization; aging and old-weight retirement update one shared budget. | AS1 `eq:recovery`; CORE recovery section; FWD local proof; SRC overlap audit. Supplies transient coupling while keeping point completion. | Fixed mass remains the denominator before fill. Retiring profile weight does not remove traffic. The reading is not sufficient state; current-work/recovery physical separation is unvalidated. | Accounted for; history dependence is explicit and no strongest-cap rule is substituted. |

## 2. Local closures and source-applicability boundaries

Local equations instantiate the global hypotheses. They are not additional
borrowed global theorems. “Supported” here reports the archived source audit,
not a new source assessment or an empirical qualification.

| ID / component | Selected local completion and interface | Source status and justification | Compatibility finding and limit |
|---|---|---|---|
| **LC1 / preparation** | Own-A demand first, residual receiving versus donor offer, paired E/A source divided by a fixed physical interaction length. Inputs are current densities, selected motion and common parameters; outputs are transfer and conserved lane totals. | CORE H1; AS1 §2; SRC H1. Receiving-work/own-lane ingredients have source lineage. Same-location homogeneous exchange and opportunity scaling are adaptations. | Compatible with MA1–MA3 under protected free preparation. Donor decay is per traveled progress; extra elapsed time alone does not create more attempts. The length/penalty scale is not empirically identified. |
| **LC2 / terminal** | Boundary entries become eligible after minimum travel; physical stock and eligible waiting are distinct; vacancy/storage constrain entrance. | CORE terminal; AS1 §2. LTM-style cumulative travel/vacancy ingredients, with selected finite-cohort restrictions. | Compatible with H1 because the admitted storage bound prevents entrance blocking. No infinite point buffer, exact queue-position trajectory or general junction-invariance theorem follows. |
| **LC3 / point service** | Free and queued representative marks, monotone implicit E work root, four retained mode branches and shortfall/actual-zero/free-continuation rules. | CORE root/allocation; AS1 §3. Fixed work and particular sharing/marks are study-defined adaptations; Carey supports ingredients, not this joined node. | Root uniqueness and feasible flows follow under OD4 below. Queued marks summarize a boundary relation, not independent acceleration states or observed individual entry speeds. |
| **LC4 / isolated recovery profile** | A speed-marked, capped transient service-loss profile derived/adapted from an isolated insertion expression; its age is physical time. | CORE recovery; SRC MP6/overlap. Leclercq lineage is restricted; the boundary-equivalent speed is not the inserted vehicle trajectory. | Shared FD units and the selected mark make the formula internally consistent. Transferring the isolated source interpretation to variable interacting entries is a modeling hypothesis. |
| **LC5 / overlap and renewal** | Normalize retained profile losses by the fixed one-vehicle-equivalent mass, integrate at most the latest such E mass, and retain their time/mark information. | CORE recovery, `eq:renewal`; FWD local proof; SRC overlap. Defined overlap/retirement closure, not the source's complete interacting-event algorithm. | Causal history integration and current service can be joined locally; no exogenous future receiving is needed. Old strong loss can retire after new fast entry. Its physical adequacy and separation from immediate work remain MP6 limits. |

Two apparent assumptions are therefore not to be added: that the one budget
reading is Markov state, or that queued mark relations reproduce microscopic
speed recovery. Neither is required or established by the current model.

## 3. Common operating domain and joint compatibility

Use AS1's exact Section 1 inequalities, not a new numerical admission rule.
The following is their traffic meaning and proof role.

| ID | Sufficient bound / premise | What it secures | Finding and excluded interpretation |
|---|---|---|---|
| **OD1** | Positive speed interval and physical length/wave/jam/recovery scales, nonnegative work coefficients, preparation penalty at least one. | Well-defined clocks, finite capacities, nonnegative work and aging profiles. | Reused exactly. Zero-recovery auxiliary limits are not the admitted complete model. |
| **OD2** | Initial free densities and ordinary E+A underload below a receiving ceiling feasible even at the lowest advice. | Free homogeneous preparation for every advice and bounded monotone A/E arrival pulse. | Reused with actual independent E+A state. Primary queuing is caused by extra forced work/recovery, not ordinary demand overload. |
| **OD3** | Separate far-lane service bound and conservative total cohort mass below one terminal lane's jam storage. | No B eligible waiting and a strictly positive vacancy margin for each terminal entrance. | The strong total-mass bound is sufficient, not necessary. It avoids feedback that would invalidate H1; it does not model arbitrary spillback. |
| **OD4** | Fixed W-F coefficient/anchor and the existing strict root-monotonicity margin. | One feasible service root, bounded work and regime-local regularity. | Reused exactly; no new clipping, service floor or coefficient renormalization. |
| **OD5** | Neutral account and selected profile, finite E rate, positive recovery and retained causal guards. | A derived positive budget, causal local history construction, finite event continuation and clearance. | Positivity, event separation and clearance are deductions of these ingredients, not inserted root assumptions. Transverse events are not needed for this forward result. |

**Nonempty common domain.** AS1 §5 gives a continuous fixed-E/fixed-A+B
split family with shared geometry/coefficients and positive margins throughout
the advice interval. The new exact static checks re-evaluate its endpoint
and common bounds using rational arithmetic, including the actual total
three-lane mass and both different initial receiving branches. Monotonicity
of the triangular capacity/critical-density family and affine split bounds
justify checking the worst endpoints; no time integration is performed.
AS2's rational loading specialization also fits that forward family.

**Compatibility of the feedback loop.** H1 supplies lane-specific entries;
finite travel supplies eligibility; selected point service supplies E flow
and mark; their retained history updates actual budget. The isolated
profile and rank cutoff enter through causal integrals. FWD's cutoff
comparison and local contraction, root uniqueness and event argument are
the accepted joined proof, extended by AS1. This is not an extra assumption
that a chosen numerical fixed-point iteration converges.

**Compatibility is conditional, not applied validity.** Immediate work
uses the remaining budget after recovery. Treating integrated recovery loss
as another maneuver multiplier would duplicate accounting. The existing
formula does not do that, but whether its two terms separate physical
effects correctly still requires joined MP6 evidence. Likewise, a profile
with good isolated lineage does not prove its use with equilibrium marks
and recent-mass retirement is a realistic many-entry model.

## 4. Conditions and direct conclusions for each claim

The core domain is shared. The extra conditions below are attached only to
the relevant result, not intersected into a purported universal task regime.

| Claim | Required core and additional conditions | Direct conclusion actually supported | What is not supported |
|---|---|---|---|
| **CL1 / conservation and complete forward** | TD1–TD3, MA1–MA5, LC1–LC5, OD1–OD5, fixed initial state. AS1 §§2–4 and FWD. | The accepted conditional forward argument covers every advice through finite clearance, respects total mass/storage and yields complete TST. | General overload/inflow/initial-history cases, empirical accuracy or smoothness at every action. |
| **CL2 / E queue structure** | CL1 plus its derived monotone pulse, zero new loss for free E and the selected clearance/priority law. AS1 §4; FWD event section. | E has at most one waiting episode in this domain. | A finite cohort by itself preventing later queue re-formation. |
| **CL3 / matched-history ambiguity** | IC1 and AS2 §2's explicit common-past loading/receiving conditions, same E/continuing total and distinct admitted A/B split. | The stated full aggregate and even richer E/continuing predecision records can be identical while adjacent receiving differs. | Every history concealing A, noisy field unobservability, different optimal actions or learning difficulty. |
| **CL4 / informative history and compact sufficiency** | IC1–IC2 and AS2 §§4–5; strict receiving-active measured E decline for that inference case; neutral known initial history for compact reconstruction. | Lawful informative histories may identify A; one extra initial adjacent statistic otherwise reconstructs the full initial state and matches Level 3's law/defined derivative. | Forced equal-split ignorance or necessity of full lane detail, discrete identities, integer mass or order. |
| **CL5 / conditional finite-action value** | CL1, IC1, the fixed-E AS3 reference/loading, its sufficiently large shared work choice, then sufficiently weak positive mismatch and fast finite recovery. Auxiliary fixed-work proof and uniform selected-law value bound are both needed. | Opposite utility of a finite slowdown and positive common-action regret exist within a nonempty selected-law range; A remains free in this certificate. | A calibrated/moderate-work default, a joint strong-A-delay witness, opposite actual infinitesimal slopes or AD advantage. |
| **CL6 / common-action outcomes** | CL1 and the AS3 common-fastest free-work interval, or the appropriate neutral limit. | The same fastest action can be optimal despite hidden lane information and positive E/mismatch parameters. | Missing information always harming control or a required interior optimum. |
| **CL7 / coupled A delay and active retirement** | The archived dedicated H1/O-R witness, restored to positive mechanisms and retained at W-F's anchor. | The selected mechanism can delay A and exercise retirement in its own analytical member. | That witness sharing CL5's preferred-action/physical range. |
| **CL8 / ordinary complete sensitivity** | Fixed true data/parameters, CL1, and AS3 §5's local smooth branches, finite isolated transverse event list, regular cutoffs with positive old rate where the inverse chart is used, and fixed horizon beyond clearance. | A local event/history-aware derivative reference includes preparation, all arrival clocks, service/marks, source timing, old-weight retirement and complete TST. | Universal ordinary differentiability, gradient closeness from value closeness, numerical AD correctness or useful finite steps. |
| **CL9 / evidence and comparison claims** | SCOPE's staged forward/gradient/usefulness checks, equal-information compact and scalar peers, honest nonregular reporting and predeclared cases/resources. | Defines how later numerical usefulness, extraction or optimizer claims must be tested. | Any executed numerical, learning, applied-physical or external-transfer success in this audit. |

Nonregular cases remain forward-admitted and require honest side/finite-change
reporting. No ordinary derivative is assumed merely to enable gradient
training. No policy-improvement outcome, interior optimum, representation
advantage or favorable parameter selection is included as a root assumption.

## 5. Correction log and audit disposition

**One live-document inconsistency was corrected without changing the model.**
The future MP6 joint physical-admission contract still listed “continuing
symmetry” in its storage/workload bullet. AS1 already supersedes that
restriction. Its current scope now explicitly uses independent initial
E/A/B loads and actual three-lane mass. Historical source/proof records
remain untouched; their old symmetry is read under the authority map above.

The initial MA groups otherwise needed explicit qualifications, not new
equations: ideal free advice response, no separate early-merge recovery,
representative rather than measured queued speeds, fixed prefill normalization,
retained history rather than scalar dynamic state, and restricted point/local
completion rather than spatial downstream-wave resolution. All follow from
the accepted laws and have been included in the short statement.

**GA-Q1, GA-Q2 and GA-Q3 are complete at the approved review scope; GA-L1
transcription is complete.** Each essential model/claim premise at the
declared granularity is accounted for. No unresolved logical contradiction,
circular positive-outcome assumption or new scientific choice was identified.
This is a review-level consistency finding, not a proof-assistant certificate
or empirical justification of every closure.

The audited set is suitable for the current conditional standalone report.
Joined physical admission, numerical gradient/usefulness and richer transfer
remain open evidence, with SUMO optional. A future change to those scientific
claims must reopen its affected contract. The audit stops at GA-G1; it does
not start full report writing or alter original Step 3's formal closure status.

[Short assumption statement](../../synthesis/research_readiness/vsl_global_assumptions_statement.md)

[Plain findings and checkpoint](../../reporting/research_readiness/vsl_global_assumptions_findings_and_checkpoint.md)

[New exact static checks](../../reporting/research_readiness/vsl_global_assumptions_static_checks.py)

[Static results](../../reporting/research_readiness/vsl_global_assumptions_static_results.json)
