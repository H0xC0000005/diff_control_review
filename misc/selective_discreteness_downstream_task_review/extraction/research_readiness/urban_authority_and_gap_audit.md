# Urban authority recovery and component/interaction completeness audit

Date: 2026-10-20. Scope: opening steps 0–1 only. This is a specification audit, not a new model, source-equation verification or scientific validation result.

The existing task can identify where order might matter. It cannot yet determine every discharge and bay-entry flow without an additional traffic rule. The useful next work is to close those few coupled laws while retaining the experiment that makes their value testable.

## 1. Recovered authority and reading depth

| Record | What was inspected and what it establishes | Authority limit |
|---|---|---|
| [Repository instructions](../../../../context_snapshots/diff_minimal_meso/AGENTS.md), [context](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md), [roadmap](../../../../context_snapshots/diff_minimal_meso/PLANS.md) | Continuous mass, first-order backbone, per-lane mass-rank refinement, fixed structural routes/permissions, conservative accounting and gated review | Root status is less current than active M2 Phase-B history; this audit does not synchronize it |
| [Initialization prompt](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/urban_report_refinement_start_prompt.txt), [handoff](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/urban_report_refinement_fresh_agent_handoff.md) | Current assignment, reading list, opening-only scope and stop | No future method is selected |
| [Selected order](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/urban_review_order_selection_and_handoff_ready.md), [P8 clarification](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/urban_p8_override_scope_clarification.md) | Global assumptions/interfaces first; P8 ownership and other methods may be reconsidered | Does not approve a replacement or waive other invariants |
| [Task feedback 16–17](../../../../context_snapshots/diff_minimal_meso/temp_content/feedback/baseline_novelty_audit_feedback.md), [reporting feedback 9–12](../../../../context_snapshots/diff_minimal_meso/temp_content/feedback/vsl_refinement_feedback.md) | V0–V4, explicit derivative-path request, Part-I closure and human-readable compact-methodology preferences | VSL-specific laws and exact page limit are not urban requirements |
| [T6 acceptance](../../discussion/t6_closure_record.md), [T7/Part-I closure](../../reporting/closure_record.md), [landing page](../../README.md) | T6/T7 accepted; Part I closed 2026-09-14; V5/I1 excluded | Older pending gates are historical |
| [Impact/ownership matrix](../../synthesis/project_impact_matrix.md), [milestone summary](../../synthesis/milestone_impact_summary.md) | P8 qualifies exact-FIFO production wording; P9/P10 establish urban external evidence/mapping obligations; M2 global/component distinction | Impact acceptance did not itself amend milestone plans or implement operators |
| [Task contract](../../synthesis/experiment_formulation.md), [formal source](../../synthesis/experiment_formulation_formal.tex), [formal PDF](../../synthesis/experiment_formulation_formal.pdf) | Action, feasible directions, complete TST, state recursion, variant paths and result logic; source read fully, five-page PDF text inspected | Prefix eligibility, bay receiving and ordered accessibility are explicitly schematic; proposal/exact-order wording must be interpreted through later decisions |
| [V0–V4 suite](../../synthesis/primary_green_allocation_suite.md) | Geometry, symmetry, matched pairs, causal roles, held-out strata and experiment order | Its older status ledger and I1 description do not supersede closure |
| [M0 approved plan](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_0_ltm_baseline.md) | Relevant timing/structure and restricted signal-node sections inspected | H1–H4 restrict where its signal branch applies; it is not a general mixed-lane service rule |
| [M1 approved plan](../../../../context_snapshots/diff_minimal_meso/docs/milestones/milestone_1_ordered_route_mass_ledger.md) | Scope and shared timing/extraction/order/merge/derivative contracts inspected | Passive quota extraction and deterministic merge order establish bookkeeping, not physical order-induced service; nonempty physical initialization was outside M1 |
| [M2 global revision](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md), [complete component register](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_component_question_register.md), [dialogue closure](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_2_per_lane_interaction_zone/phase_B_dialogue.md) | Closed G1–G6 recovered; all 19 local questions read; infrastructure, neutral domain and unresolved component ownership distinguished | No component recommendation is treated as approved. No later M2 Phase-C/M3 decision was located in inspected docs, active archives and urban records |
| [Baseline realization](../../synthesis/baseline_realization_matrix.md), [adoption matrix](../../synthesis/literature_adoption_matrix.md) | Accepted roles, capabilities, fairness, principal-source recommendations and adoption gates | A recommended source is not a selected complete equation set or a verified drop-in implementation |
| [Evidence codebook](../task_evidence_codebook.md), [31-row extraction](../task_evidence_matrix.csv), [T4 audit](../t4_evidence_audit.md), [archive manifest](../../archive/manifest.csv) | Recorded reading depth and task/method mismatch checked, especially T0007, T0014/T0015, T0030 and T0032 | This opening relies on those extraction records. It does not independently reread or verify their specific source equations, licenses or current software APIs |
| [Accepted VSL report](../../../differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_compact_methods_report.pdf), [coverage map](../../../differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_compact_report_source_and_coverage_map.md), [assumption findings](../../../differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_global_assumptions_findings_and_checkpoint.md) | Four-page PDF text/source and attribution/assumption presentation inspected | Presentation/specification example only; no urban/VSL unification or imported scalar/history/event law |

Read-only implementation checks covered the existing node/signal API, objective accounting and relevant test definitions/configuration. In particular, [continuum_service](../../../../context_snapshots/diff_minimal_meso/src/diff_minimal_meso/signals.py#L100) rejects different exposure among one input's positive-turn movements; [the node implementation](../../../../context_snapshots/diff_minimal_meso/src/diff_minimal_meso/nodes.py#L235) declares the restricted H1–H4 branch; [existing tests](../../../../context_snapshots/diff_minimal_meso/tests/test_nodes.py#L277) check receiving-share feasibility. The [objective](../../../../context_snapshots/diff_minimal_meso/src/diff_minimal_meso/objectives.py#L23) uses source availability and pre-update physical occupancy. These are inspection findings; no tests or simulator were run.

## 2. What is accepted, recovered, newly undecided or deferred

Classification: **A** = accepted and ready to explain; **R** = supplied by a later existing authority, with its scope retained; **N** = requires a new methodological decision/specification; **E** = implementation, calibration or empirical evidence outside this pass. A component can contain several classes; the entries below keep their claims separate.

| ID | Class | Finding | Record and consequence |
|---|---|---|---|
| A01 | A | V0–V4 task, symmetric core and held-out asymmetry | T6/closure; retain roles and later V0-first execution order |
| A02 | A | Four-group physical effective-service allocation and feasible directions | Formal §§2,4; internal logits are optional/default optimization coordinates |
| A03 | A | Clearance-complete TST counts source waiting and moving/queued mass once | T6/formal §3; no short-horizon queue-only replacement |
| A04 | A | Baseline/evidence roles and separate representation/optimizer axes | Baseline matrix and P9/P10; equivalence and negative results remain valid |
| R01 | R | Exact within-bin production FIFO is not selected | Accepted P8; current instruction permits reconsideration and alternatives |
| R02 | R | Geometry-authoritative upstream/local-zone split and storage independent of bin resolution | M2 G1/G3; exact ledger remains authority, grid a cached view |
| R03 | R | Conservative fixed-commitment ingress, explicit eligibility and no same-step admission/discharge | M2 G2; its passive no-cross-lane-blockage policy is replaceable later, infrastructure is retained |
| R04 | R | Neutral full-length movement-exclusive fixtures; matched split-domain comparator; stable-signature differentiation | M2 G4–G6; these do not close short-bay/shared-lane behavior |
| N01 | N | Full urban initialization, histories and population ownership | Gap 1; UR-G1 and C1-Q1 |
| N02 | N | Average service opportunity and compatible movement/shared-lane/node interface | Gap 2; UR-G2 and C3-Q1 |
| N03 | N | Coupled admission/discharge/receiving clock and resource allocation | Gap 3; UR-G2 and C1/C2/C3 |
| N04 | N | Order resolution and a concrete production access/service family | Gap 4; UR-G3 and C2/C3 |
| N05 | N | Lane intent, physical bay reachability and admission | Gap 5; UR-G3 and C2-Q1 |
| N06 | N | Principal faithful B1 and B2 equations | Gap 6; UR-G4 and C4-Q1/Q2 |
| N07 | N | Rival observation/history/inference and pair-matching maps | Gap 7; UR-G4 |
| N08 | N | Local and joined sensitivity, including complete clearance | Gap 8; UR-G5 and C5-Q1 |
| N09 | N | Equation-level source/adaptation credit | Gap 9; component owners and C7-Q1 |
| N10 | N | Independent R1 coverage and common R2 realization/accounting method | Gap 10; UR-G4 and C6-Q1 |
| N11 | N | Whole-model consistency and neutral/coupled reference specification | Gap 11; S6 after all component closures |
| E01 | E | Numerical lengths, rates, time step, finite-difference scales, seeds, optimizer/budget settings and tolerances | D1–D7 retain status; calibrate under later approved execution plans and freeze before confirmatory work |
| E02 | E | Implemented conservation/reference/AD evidence, runtime, external perturbation, optimization and held-out transfer | Evidence sequence retained; this audit provides none of these results |

The D1–D7 labels do not make every related scientific requirement optional. D1's logit map is a default; physical feasible allocations remain the shared action. D2's constant-allocation/control-window and clearance-policy details retain their default status while complete accounting is retained. D3's explanatory discussion sits under defaults, but T6 expressly accepts clearance-complete TST as the task score. D4's exact regime ranges remain to calibrate. D5's paired grouping/no-leakage rule is retained, with split proportions open. D6 makes SUMO the proposed evaluator; it does not make the accepted richer-evaluator perturbation stage optional. D7 leaves numerical instantiation to later planning and requires freezing it before confirmatory evaluation.

### Physical interfaces that the missing laws must complete

| Component | Authoritative state and inputs | Required output/interface | Present limit |
|---|---|---|---|
| Population/source | Released route mass, source order and generation history; initial population | Source waiting, admitted mass and actual entry chronology | Complete urban initial-history domain still open |
| Upstream LTM | Cumulative boundary histories, physical FD/storage and downstream restriction | Sending/receiving in mass per interval; updated counts | Accepted equations available; local/bay coupling must preserve the clock |
| Per-lane zone | Ordered route references/positions, continuous mass and eligibility; cached lane/bin/movement grid | Conserved lane mass, physical storage/room, service-ready offers | M2 neutral infrastructure recovered; no short-bay access law |
| Intent and access | Fixed permissions/geometry, admitted intent information, actual queue/order state and room | Reachable admission and explicitly retained rejected mass | Desired allocation and physical reachability cannot be conflated |
| Node/service | Eligible movement mass, physical allocation, lane/shared-output resources and receiving | Feasible movement discharge, route removal/residual/timing plan | Mixed-lane opportunity and solution-selection rules are missing |
| Accounting/objective | Disjoint source, upstream, zone, downstream and completed population | Complete TST in vehicle-equivalent seconds and mechanism diagnostics | Ledger/grid/cumulative views must not be counted as extra traffic |
| Rivals/references | Each role's declared native state and permitted history; common physical task | Forward outcomes and only justified gradient roles | B1/B2 laws and common external mapping remain unselected |

The later specification must name field cardinalities, units and structural versus continuous status, including lane/run/bin/movement dimensions where used. Rate inputs are vehicle-equivalent mass per second; interval transfers and storage are mass; eligibility and passage times are seconds. A chosen tensor layout or numerical solver is not supplied as a substitute for these scientific interfaces. Float64 gradient checks remain the inherited evidence default.

### Equation provenance recovery versus verification still needed

| Defining object | Exact current internal location | Credit recovered from that record | Remaining attribution work |
|---|---|---|---|
| LTM history queries, sending/receiving and count update | M0 §6, “Exact history query and equations” | Yperman (2007) cumulative/interpolation lineage; separate scalar oracle and recorded UNsim reference version | Verify exact primary-text locations when publishing the compact source map; do not attribute the entire composition to a software comparator |
| Ordinary oriented-capacity node | M0 §8.1 | Tampère et al. (2011) Branch-T/ORCA transcription | Preserve its distinction from signalized service and lane/access extensions |
| Exposure/service arithmetic and restricted signal node | M0 §§8.2,9 | Han continuum-service lineage with explicitly approved H1–H4 restrictions | Reconcile with the adoption matrix's COS/task anchors: the existing restricted branch is not automatically the complete COS node or Tampère's signalized model |
| Continuous route references, actual-crossing affine timing, exact split/merge | M1 §3 | Project-approved continuous-mass metadata composition | Separate that composition from T0017's integer identity/order precedent; inspect source claims only at their actual depth |
| Physical allocation, TST and generic sensitivity recursion | Formal urban §§2–5 | Accepted task definition/accounting and chain-rule contract | Mark study-defined task choices and mathematical deductions; task-precedent papers do not author all these equations |
| Prefix eligibility, bay receiving and ordered access | Formal urban §6 | Explicitly schematic contracts | Select/derive laws before assigning equation-level credit or derivatives |
| B1/B2 traffic equations | Adoption matrix, B1/B2 sections | Recommended source families and declared adaptation gates | Inspect and select exact equations/algorithms; recommendations are not equation identity |
| Effective-service-to-executable-evaluator mapping | D6 and P10 | Required project-owned mapping supported by technical documentation | Specify the mapping and its physical mismatch; software documentation is not a validation of equivalent service |

This table credits what the inspected internal authorities actually say. It is not a fresh verification of the cited primary formulas or current software versions.

## 3. Component and interaction gaps

### Gap 1 — the initial population must describe a possible traffic state

**Why it matters.** A nonempty bay or feeder queue needs matching aggregate history, route mass, lane occupancy and eligibility times. Otherwise one model can start with service-ready traffic while another must wait for travel, or the objective can omit preloaded mass. M1's empty physical-link start is a deliberate limited scope; T6's initial-state and V4 queue variation do not automatically inherit that restriction.

**Standard/source.** U2/U4/U5; formal §1, M1 §§2–3 and M2 G1/G2. Later records recover timing and ownership, but do not complete general urban initialization.

**Proposed review/owner.** UR-G1 fixes admitted initial and arrival histories, population accounting origin, structural/continuous state and source-time convention. C1-Q1 transcribes them. Specify whether any pre-control warm-up is independent of the candidate action; do not differentiate an initial state that the task holds fixed.

**Dependencies/closure.** Before access, objective and derivatives. Close with an initial/history compatibility sheet and one mass traced from release or initial residence through completion, including an explicit account of initially present mass. No numerical preload generator is needed for this opening.

### Gap 2 — effective average service is not a complete ordered-service law

**Why it matters.** In a shared lane, left traffic and through traffic compete through their sequence. Positive average service for both does not itself specify a red/green event or which opportunity occurs first. The older red-ineligible/green-eligible example needs a declared eligibility interpretation under this continuum action. Independently limiting each movement by its own service cap also does not settle shared-lane or common-output feasibility.

**Standard/source.** U3/U4; formal §§2,6; suite V1; M0 §8.2 and the inspected signal API. M0 requires homogeneous exposure across an input's positive-turn movements. Left and through groups generally have different allocations, so treating a mixed lane as that same homogeneous input is not automatically valid. This does not invalidate the accepted task; it shows why a new declared service interface is needed.

**Proposed review/owner.** UR-G2 states what a service opportunity means at the model's time scale, how movement/input/lane resource groups relate, and which restricted M0 cases remain reusable. UR-G3 determines the permissible order policy; C3-Q1 specifies the actual solver. Do not invent an executable phase schedule or hide shared-lane relaxation in an adapter.

**Dependencies/closure.** G1 first; then global service/interface closure before C3. Require a left-first/through-first shared example under the same physical allocation, explicit unused-service treatment, simultaneous resource/receiving feasibility, and a V0 specialization consistent with the inherited restricted domain.

### Gap 3 — storage, service and upstream restriction need one clock

**Why it matters.** Whether a discharge opens room for admission in the same interval changes bay occupancy, blockage and gradients. A queue cannot disappear at the U/Z boundary or jump backward instantaneously because an implementation rearranges update calls. Newly admitted mass must not also traverse its zone in the same step under the inherited contract.

**Standard/source.** U3/U4; M0 scheduler, M1 actual-crossing eligibility, M2 G2/G4, formal V2/V3. M2's neutral timing is recovered; the coupled bay transaction is still unspecified.

**Proposed review/owner.** UR-G2 freezes the shared pre/post-state, service-eligibility, travel-delay and vacancy-credit conventions, including allocation of common receiving supply. C1/C2/C3 implement the mathematical transcription in their specifications, not code. Geometry-derived storage and flow capacity have distinct units; neither can be inferred from bin count or time-step length.

**Dependencies/closure.** G1/G2 and all affected components. Require one joined interval trace identifying every accepted/rejected flow, physical owner and applicable history, followed by the delayed upstream receiving response. Exclude unexplained fixed-point loops; if a simultaneous solve is selected, specify its existence/selection and sensitivity contract globally.

### Gap 4 — retained order and service resolution remain a choice

**Why it matters.** An exact ordered prefix, a homogeneous mass bin and a different continuous ordered-flow closure can let different traffic pass under the same allocation. That changes what the research tests and the meaning of a useful gradient. Fine mass bins do not by themselves prove a small objective or derivative error.

**Standard/source.** U3/U7/U8; P8, current override scope, M2 exact/policy-neutral seam and M3 roadmap questions. No later chosen production policy was found.

**Proposed review/owner.** UR-G3 reviews the minimal exact, bounded-bin and other justified method directions, and proposes bringing methodological closure here while leaving implementation to future milestones. C2/C3 can then write concrete laws. The [register](urban_open_question_register.md) marks which candidates are only directions and compares old/new behavior and consequences.

**Dependencies/closure.** G1/G2 first; G4/G5 consume the result. Require a selected concrete model, retained/relaxed information statement, route/residual/timing reconciliation and appropriate forward/reference/resolution/gradient obligations. An override record must state precisely which part of P8 is superseded. Current exact infrastructure and scientific invariants remain unchanged until an explicit compatible decision/amendment.

### Gap 5 — intent, room and reachability are different things

**Why it matters.** A left turner can want a bay with available room and still be trapped behind through traffic. Conversely, applying an arbitrary global prefix restriction could overblock traffic in independently accessible lanes. Cumulative traffic rank describes order; it does not locate the bay opening in meters or determine where the physical queue tail lies.

**Standard/source.** U2–U4; context lane/access invariants, formal schematic access operator, M2 G2/G4. The neutral scan may pass blocked commitments for independent lanes; it is not an ordered bay-opening law.

**Proposed review/owner.** UR-G3 settles what state can determine intent and realized access and whether intent is authored or solved. C2-Q1 supplies an explicit geometry/queue/rank-to-access closure, storage-limited admission and retained rejection. A literature equilibrium idea for desired allocation does not itself solve realized accessibility. No microscopic lane-change trajectory is required or authorized.

**Dependencies/closure.** G1–G3, C1, coupled C3. Require the same bay with room under reachable and obstructed ordering, a full-bay case and an unobstructed limit. The rule must state where any spatial inference comes from, rather than identifying a mass bin with a road cell.

### Gap 6 — strong B1/B2 labels need selected formulations

**Why it matters.** A weak improvised aggregate model can manufacture selective-order benefit; a hybrid assembled from several papers can introduce undeclared information or physics. The accepted role ladder intentionally leaves exact equation choices open.

**Standard/source.** U6/U7; baseline/adoption matrices and recorded T4 extraction. T0015 is a recommended turn-queue anchor, with T0014 a distinct partial-FIFO alternative; the extraction records on/off and additional-feature differences. T0030 is the recommended lane-allocation anchor, but finite-storage augmentation is explicitly still to be chosen.

**Proposed review/owner.** UR-G4 freezes capabilities. C4-Q1/Q2 each select one principal realization, inspect exact primary equations, document time/service/storage adaptations, and identify hand or published reference cases. Do not force AD where the chosen native law lacks a justified derivative; preserve a forward-only role if necessary.

**Dependencies/closure.** G2/G4 and coupled bay interface. Require principal-source equation/algorithm/version, every adaptation, lawful observations, neutral limits and reference specifications. Numeric reproduction belongs to later implementation/evidence, but a missing mathematical baseline cannot be deferred past the compact methodology report.

### Gap 7 — equal aggregate totals do not settle every rival's information

**Why it matters.** Two queues with equal totals may expose different movement arrival histories, lane histories or previous service. A turn-queue or lane-aware rival may infer more than a homogeneous model. Declaring all aggregate rivals blind merely because they lack a ledger would overstate the information result.

**Standard/source.** U7; formal §7 and baseline fairness. Urban has its own observation/capability contract; it need not inherit VSL's scalar information ladder.

**Proposed review/owner.** UR-G4 gives each B0–B3 input, initialization, permitted history and inference map. Check pairs at the actual declared information level; distinguish known source order from predicted realized accessibility, and do not supply future evaluator states. If an allowed history distinguishes a pair, report that capability, refine the diagnostic pair lawfully or narrow the claim.

**Dependencies/closure.** G1–G3; C4 realizations must obey it. Require a projection/checklist for each rival and each claimed matched pair, provenance of B3's order/access inputs, pair-grouped split rules and no test-outcome tuning. Matching offered information does not require forcing different models' future endogenous trajectories to agree.

### Gap 8 — the chain rule is only complete after the traffic laws

**Why it matters.** A service change can empty a bay, expose a turner, change later receiving and source waiting, and change the clearance tail. Differentiating only direct discharge misses those paths. Treating the order skeleton as structural also does not mean freezing all future head/exhaustion decisions while perturbing the action.

**Standard/source.** U5/U8; formal §§4–6, M2 G6 and P11. The existing recursion says what must connect; it does not supply derivatives of undefined operators.

**Proposed review/owner.** UR-G5 closes the derivative domain, metadata and boundary conventions. C5-Q1 derives local and joined sensitivities for selected laws, including eligibility timing, residual mass, storage/access feedback, any solved equilibrium and the common clearance policy. Clarify a fixed comparison horizon beyond local clearance or another justified complete-tail treatment; do not differentiate an arbitrary stopping counter as though it were smooth.

**Dependencies/closure.** Selected traffic and baseline laws. Require an operator-by-operator dependency map, active-signature list, V0–V3 specialization and V4 fixed-bank averaging. Censored/nonclearing runs and boundary cases remain reported. Float64 AD/JVP/central differences and richer intervention usefulness are future separate evidence, not opening results.

### Gap 9 — a source ID is not equation-level credit

**Why it matters.** Readers must distinguish established ingredients, necessary adaptations and project-defined closures. T0017's integer identity tracking is not a source for an exact continuous-mass derivative; an AD engineering precedent does not author the urban access law.

**Standard/source.** U6; adoption matrix's eight gates, extraction access-depth fields and VSL attribution example.

**Proposed review/owner.** Each component owns its source inspection; C7-Q1 consolidates an equation/source map. Record source version, equation/page/algorithm, native assumptions, adoption class, changed terms and the owner of any derivation. Give credit beside the defining equation in the later report. Treat metadata/abstract/task relevance as such, not as a verified law.

**Dependencies/closure.** Selected laws. Require complete coverage of all defining model/task/sensitivity equations, with primary text checked at the needed depth. No new equation is attributed to a paper by this audit.

### Gap 10 — independent references and the external intervention need definitions

**Why it matters.** R1 must be able to disagree with production code. R2 must evaluate the same service change, population and completion accounting for every model, despite microscopic vehicles and executable signals. Direct software availability does not make continuum service equivalent to signal timing under blockage.

**Standard/source.** U7/U9; R1/R2 baseline roles, D6, P9/P10. External perturbation remains required before full optimization; its evaluator and exact numerical settings retain their recorded decision status.

**Proposed review/owner.** UR-G4 states common mapping/accounting obligations; C6-Q1 defines bounded independent order/storage references and a conceptual effective-service-to-program law, held fixed across methods. Specify route/departure realization and source-wait measures without integerizing the mainline model. Document mismatch and admissible claims. Numeric cycle/clearance values, seeds and actual API/version checks are later execution choices.

**Dependencies/closure.** Action/clock, selected laws, objective and observations. Require an auditable mapping/measurement sheet, independent reference coverage and failure logic before S6/S7. If a credible common mapping cannot be specified, record the unresolved methodological block; do not import VSL's optional-external-evidence amendment.

### Gap 11 — complete components can still disagree when composed

**Why it matters.** A correct storage update can use the wrong admitted flow, a correct access rule can use already-updated occupancy, and a correct TST sum can count ledger and grid copies twice. A model report must describe one consistent system.

**Standard/source.** U4/U9; approved component/integration workflow and selected global-first order.

**Proposed review/owner.** S6 owns the whole-model audit after all global/component specifications close. Compare the final state/interface/units/clock definitions with accepted globals and every V0–V4 causal purpose, rival capability and derivative edge.

**Dependencies/closure.** S2–S5. Require worked neutral, order-only, storage-only and combined-access traces; symmetry and conservation/resource arguments; complete sensitivity and provenance coverage. These are later specification/reference checks, not a new two-node V5/I1 task or a numerical experiment in this opening. A conflict reopens its smallest owner and affected evidence.

## 4. Sensitivity coverage to preserve in later review

| Variant | Required traffic/sensitivity chain | Current missing closure |
|---|---|---|
| V0 | Allocation → movement service → feasible aggregate discharge → later source/network time | Match the actual restricted signal/resource domain and physical split-domain comparator |
| V1 | V0 plus order-conditioned service → residual head/continuous masses → future discharge | Service-opportunity/order law, branch signatures and reconciliation |
| V2 | Bay discharge → occupancy/room → admission → feeder restriction and delayed upstream receiving → time | Explicit receiving/storage/service clock and a declared order-neutral/nonbinding-access construction |
| V3 | V2 plus realized reachability → admitted/residual ordered mass → future access/service | Concrete geometry/queue/order-conditioned access law; chosen retained/relaxed resolution |
| V4 | Fixed scenario-bank average of applicable complete paths; held-out scenarios excluded from training feedback | Freeze split units/strata later; no new local traffic equation |

Each arrow is a required dependency, not a claimed nonzero derivative in every regime. Inactive constraints may remove a sensitivity legitimately. New topology, active-prefix changes and event boundaries require explicit qualifications; they are not reasons to add unapproved smoothing.

## 5. Audit conclusion

The accepted task and much of the infrastructure are ready to write. The principal remaining work is methodological: a coherent average-service/order/access/storage system, faithful B1/B2 realizations, fair information and external mapping contracts, then their full conditional sensitivity. Calibration cannot fill these laws. Conversely, the absence of numerical evidence does not prevent specifying them.

The [proposal](../../temp_content/research_readiness/phase_A_proposal.md) stages that work globally first and stops this opening at its plan gate. The [question register](urban_open_question_register.md) records alternatives and exact decision ownership without selecting a production law.
