# Review sequence and reading guide

For the big picture before individual reports, read the
[semantic recap through the S10 methodology closure](01_review_recap_through_s06.md).

Current status: **S13 is closed with M2C-A; later study extensions remain
separately gated.** Start with the
[S10 closure](reporting/s10/s10_99_vsl_methodology_review_closure.md),
[S12 closure](reporting/s12/s12_99_advice_merge_service_sprint_closure.md) and
[S13 findings](reporting/s13/s13_20_m2_certificate_findings_and_gate.md),
[study-sufficiency audit](reporting/s13/s13_35_study_sufficiency_and_extension_audit.md)
and [S13 closure](reporting/s13/s13_99_m2_certificate_sprint_closure.md).
No installation, harness implementation or traffic experiment has occurred.
The current scope/decision correction is recorded in the
[living dialogue](reporting/s04/s04_80_rb_diagnostic_phase_A_dialogue.md).
This index does not itself approve an experiment, model contract or changed
finding. Everything remains in this same review pack.

## Naming and relationships

Primary plans/reports use `sNN_RR_<existing_semantic_name>.md`.
`sNN` is the stable review-sprint identity, in continuation order; `RR` is the
document's role/read-order slot, **not** its creation date, revision number or
scientific priority. The semantic suffix and existing gate/source/question IDs
are retained. A findings-plus-gate document occupies20, not duplicate20/30 files.

| Role slot | Document function |
|---|---|
| 00 | Approved/proposed plan; read before executing that sprint. |
| 10 | Paper-access request, if any; may be resolved historical material. |
| 19 | Optional brief plain-language companion; read before the full findings. |
| 20 | Main findings; first scientific reading after execution. |
| 30 | Separate user decision gate, when not combined with findings. |
| 35–36 | Feedback clarification/amendment supplementing the findings/gate. |
| 80 | Dialogue and decisions; supporting history, not a new findings report. |
| 90 | Work/check report; verification and reproducibility support. |
| 99 | Explicit user closure and next-sprint handoff, when recorded separately. |

The usual reading path is **20 → 30 (if separate) → 35/36 (if needed) → 99**;
00 supplies scope/authority,80 supplies discussion,90 supplies the audit trail.
Absent role slots are intentional. Do not create empty reports to fill them.
S05–S08 have explicit user closure. S09's provider audit is retained only as an
audit record; its empirical continuation is outside the corrected scope. S10 and
the complete methodology review are closed. S11, S12 and S13 are also closed.
S13's methodology-only certificate was accepted as M2C-A; no implementation or
empirical VSL continuation is authorized. The separately opened ramp-metering
task-admission review is maintained in its own
[package](../selective_discreteness_ramp_metering_review/README.md).

Source PDFs/FB IDs, claim/query registers, technical annexes and mathematical
attachments keep their existing evidence-oriented names. They are linked from
their owning sprint rather than being renumbered as new reports. Archived drafts
remain archived, not promoted to current plans. Living dialogue files keep their
origin sprint ID even when they document continuation into a later sprint.

## Sprint backbone

| Sprint | Question / function | Predecessor and selected continuation | Main reading / gate | Status |
|---|---|---|---|---|
| [S01](#s01) | Which freeway task warrants review? | Independent pre-review handoff. | [Findings](reporting/s01/s01_20_n1_findings_report.md), [N1 gate](reporting/s01/s01_30_n1_user_gate.md). | Completed; narrowed F1/Candidate A accepted. |
| [S02](#s02) | What do strong predecessors establish; which evidence route next? | S01 accepted F1 scope. | [Findings/N2-UG1](reporting/s02/s02_20_n2_findings_and_gate.md). | Completed; Route B approved. |
| [S03](#s03) | Does the contrast/common-control evidence support proceeding? | S02 selected Route B. | [Findings/RB-UG1](reporting/s03/s03_20_rb_findings_and_gate.md). | Closed; Option A diagnostic planning approved. |
| [S04](#s04) | Is the diagnostic's information-to-decision methodology defensible? | S03 selected separately gated diagnostic planning, in this pack. | [Findings/DG-MUG1](reporting/s04/s04_20_rb_diagnostic_methodology_findings_and_gate.md). | Closed; Candidate A analytical construction approved. |
| [S05](#s05) | Can an admissible matched-history traffic case require different useful common advice? | S04 selected exact information-loss construction. | [Findings/DG-AC1](reporting/s05/s05_20_rb_certificate_findings_and_gate.md), [closure](reporting/s05/s05_99_rb_certificate_sprint_closure.md). | Closed with partial results; reference-first documentary continuation selected. |
| [S06](#s06) | What richer-reference mechanisms bridge the advice/information link; is the proposed preparation defensible? | S05 closure and approved documentary scope. | [Findings/S06-UG1](reporting/s06/s06_20_reference_bridge_findings_and_gate.md), [closure](reporting/s06/s06_99_reference_bridge_sprint_closure.md). | Closed; Candidate A near-drop preparation review selected. |
| [S07](#s07) | Can a reachable near-drop preparation avoid obvious insertion/history confounding? | S06 closure / DG-R3 Candidate A. | [Findings/S07-UG1](reporting/s07/s07_20_reachable_preparation_findings_and_gate.md), [closure](reporting/s07/s07_99_reachable_preparation_sprint_closure.md). | Closed; localized Candidate A selected. |
| [S08](#s08) | How should the exact-prefix feasibility experiment be bounded? | S07 closure / DG-R4 Candidate A. | [Findings/S08-UG1](reporting/s08/s08_20_exact_prefix_planning_findings_and_gate.md), [closure](reporting/s08/s08_99_exact_prefix_planning_sprint_closure.md). | Closed; full dual-step Candidate A selected. |
| [S09](#s09) | Clarify whether post-S08 work is empirical execution or methodology review. | S08 closure / DG-R5 Candidate A. | [Scope correction](reporting/s09/s09_35_scope_correction_and_methodology_alternatives.md). | Empirical route withdrawn; methodology-only alternatives documented. |
| [S10](#s10) | Is the future protocol sufficient for its bounded claims, and should methodology review close? | S09 scope correction / M1. | [Findings/S10-UG1](reporting/s10/s10_20_protocol_sufficiency_findings_and_gate.md), [closure](reporting/s10/s10_99_vsl_methodology_review_closure.md). | Closed; DG-R7 Candidate A approved. |
| [S11](#s11) | Can exogenous lane reopening create a defensible hidden-state-to-useful-VSL-decision path? | S10 closure / approved post-closure Option 3 ordering. | [Findings/S11-UG1](reporting/s11/s11_20_temporary_closure_recovery_admission_findings_and_gate.md), [closure](reporting/s11/s11_99_temporary_closure_recovery_sprint_closure.md). | Closed; G4-A approved, TCR-E accepted. |
| [S12](#s12) | Can a conservative analytical advice–merge–service class escape the S05 obstruction without favorable coefficients? | S11 TCR-E closure / approved Step 2 Candidate B branch. | [Findings/S12-UG1](reporting/s12/s12_20_advice_merge_service_findings_and_gate.md), [closure](reporting/s12/s12_99_advice_merge_service_sprint_closure.md). | Closed; G4-A approved and AMR-A accepted. |
| [S13](#s13) | Can admitted M2 yield an exact strong-history useful-action certificate, and what gradient path follows? | S12 G4-A/AMR-A closure; inserted before ramp metering. | [Findings/S13-UG1](reporting/s13/s13_20_m2_certificate_findings_and_gate.md), [closure](reporting/s13/s13_99_m2_certificate_sprint_closure.md). | Closed; M2C-A accepted. |

These are review continuations, not development milestones or mandatory urban
Phase A–F cycles. N1/N2/Route B remain the historical names; S01–S06 make their
sequence legible without changing those meanings. Selected options at different
gates are local to their own gate, not one universal “Candidate A.”

<a id="s01"></a>
## S01

Task framing (historical N1), from the independent pre-review handoff.

- [00 Protocol plan](s01_00_review_protocol_plan.md).
- [20 Scientific findings](reporting/s01/s01_20_n1_findings_report.md).
- [30 Accepted user gate](reporting/s01/s01_30_n1_user_gate.md).
- [80 Gate clarification/decision dialogue](reporting/s01/s01_80_n1_gate_dialogue.md).

Handoff: accepted narrowed F1 opens S02 review planning, not simulator construction.

<a id="s02"></a>
## S02

Predecessor and route review (historical N2), following accepted S01 scope.

- [00 Approved protocol](s02_00_n2_review_protocol_plan.md).
- [10 Resolved institutional paper batch](reporting/s02/s02_10_n2_institutional_access_batch_1.md).
- [20 Findings and N2-UG1](reporting/s02/s02_20_n2_findings_and_gate.md).
- [35 Feedback23 task/minimum-information response](reporting/s02/s02_35_feedback23_task_and_minimum_information_response.md).
- [36 Feedback23 novelty/necessity amendment](reporting/s02/s02_36_feedback23_amendment_novelty_and_component_necessity.md).
- [80 Living dialogue](reporting/s02/s02_80_n2_phase_A_dialogue.md), also covering S03 planning.
- [90 Work/check report](reporting/s02/s02_90_n2_work_report.md).

Handoff: Route B selection leads to S03's bounded contrast review. The
[original proposal](archive/planning/n2_phase_A_protocol_proposal.md) is superseded.

<a id="s03"></a>
## S03

Route B contrast/common-contract review, following S02's Route B decision.

- [00 Approved protocol](s03_00_rb_review_protocol_plan.md).
- [10 Resolved paper request](reporting/s03/s03_10_rb_access_request_1.md).
- [20 Findings and RB-UG1](reporting/s03/s03_20_rb_findings_and_gate.md).
- [90 Work/check report](reporting/s03/s03_90_rb_work_report.md).
- [99 Sprint closure and diagnostic-planning handoff](reporting/s03/s03_99_rb_sprint_closure.md).

Handoff: Option A authorizes S04 planning, not an experiment. Planning history
is in S02's living dialogue; the [original draft](archive/planning/route_B_review_plan.md)
is superseded. [Common contract](synthesis/s03/rb_common_contract.md) and
[contrast/information audit](synthesis/s03/rb_contrast_and_information_audit.md) are annexes.

<a id="s04"></a>
## S04

Diagnostic planning and methodology review, following S03 closure. The user
clarified methodology-only scope; numerical settings remain prospective.

- [00 Approved continuation proposal](s04_00_rb_diagnostic_phase_A_proposal.md).
- [20 Methodology findings and DG-MUG1](reporting/s04/s04_20_rb_diagnostic_methodology_findings_and_gate.md).
- [80 Living dialogue](reporting/s04/s04_80_rb_diagnostic_phase_A_dialogue.md), also recording S05 execution.
- [90 Planning/consolidation/work record](reporting/s04/s04_90_rb_diagnostic_planning_work_report.md).
- [99 Methodology closure and analytical-study boundary](reporting/s04/s04_99_rb_diagnostic_methodology_closure.md).

Annexes: [technical contract](synthesis/s04/rb_diagnostic_technical_contract.md) and
[living decision inventory](synthesis/s04/rb_diagnostic_question_inventory.md).
Handoff: DG-MUG1 Candidate A selects S05's exact information-loss analytical
study, not the distinct observer-quality route or numerical implementation.

<a id="s05"></a>
## S05

Analytical construction, following S04 Candidate A approval and explicit
execution. Its authorized work boundary is S04's99 closure/handoff, so no
duplicate00 plan is manufactured.

- [19 Brief semantic explanation](reporting/s05/s05_19_certificate_semantic_summary.md).
- [20 Findings and DG-AC1 scope/selection](reporting/s05/s05_20_rb_certificate_findings_and_gate.md).
- [Mathematical analysis PDF](synthesis/s05/rb_certificate_analysis.pdf) and
  [LaTeX source](synthesis/s05/rb_certificate_analysis.tex).
- [Source/construction audit](extraction/rb_certificate_source_audit.md).
- [90 Work/check report](reporting/s05/s05_90_rb_certificate_work_report.md).
- [99 User closure and reference-first documentary handoff](reporting/s05/s05_99_rb_certificate_sprint_closure.md).

Handoff: DG-R2 records the selected reference-first direction and documentary-only
boundary. Explicit user closure opens S06; empirical A remains deferred.

<a id="s06"></a>
## S06

Reference-first documentary bridge review, following S05 closure. This is actual
source/methodology review, not merely the preceding administrative scope correction.

- [00 Approved execution protocol](s06_00_reference_first_bridge_review_plan.md).
- [19 Two-page colleague-facing progress handout](reporting/s06/s06_19_colleague_progress_handout.pdf)
  and [editable LaTeX source](reporting/s06/s06_19_colleague_progress_handout.tex).
- [20 Brief findings and preparation-contract gate](reporting/s06/s06_20_reference_bridge_findings_and_gate.md).
- [Source/mechanism audit](extraction/s06_reference_mechanism_source_audit.md).
- [Query log](search/s06_reference_bridge_query_log.csv) and [access log](search/s06_reference_bridge_access_log.csv).
- [90 Work/check report](reporting/s06/s06_90_reference_bridge_work_report.md).

Gate: DG-R3 selected Candidate A after the reachability screen and mechanism/
history audit. The user then [closed S06](reporting/s06/s06_99_reference_bridge_sprint_closure.md)
and opened S07. No S06 finding itself revised a preparation setting.

<a id="s07"></a>
## S07

Reachable near-drop preparation review, following S06 Candidate A.

- [00 Approved execution protocol](s07_00_reachable_near_drop_preparation_review_plan.md).
- [Analysis PDF](synthesis/s07/s07_reachable_preparation_analysis.pdf) and
  [LaTeX source](synthesis/s07/s07_reachable_preparation_analysis.tex).
- [20 Findings and preparation-contract gate](reporting/s07/s07_20_reachable_preparation_findings_and_gate.md).
- [Source/method audit](extraction/s07_reachable_preparation_source_audit.md).
- [Query log](search/s07_reachable_preparation_query_log.csv) and
  [access log](search/s07_reachable_preparation_access_log.csv).
- [90 Work/check report](reporting/s07/s07_90_reachable_preparation_work_report.md).

Gate: DG-R4 chooses a localized one-block balanced contrast, a broader balanced
multi-block window, a pre-registered failure-specific A-to-B ladder, or deferral.
The user selected A and [closed S07](reporting/s07/s07_99_reachable_preparation_sprint_closure.md).
Candidate B requires later manual mutual agreement; automatic fallback is not active.

<a id="s08"></a>
## S08

Exact-prefix feasibility planning, following the localized S07 preparation.

- [00 Approved planning protocol](s08_00_exact_prefix_feasibility_planning_review.md).
- [Exact preparation/observation/execution contract](synthesis/s08/s08_exact_prefix_feasibility_contract.md).
- [20 Findings and execution-scope gate](reporting/s08/s08_20_exact_prefix_planning_findings_and_gate.md).
- [90 Work/check report](reporting/s08/s08_90_exact_prefix_planning_work_report.md).
- [99 User closure and exact-prefix execution handoff](reporting/s08/s08_99_exact_prefix_planning_sprint_closure.md).

Gate: DG-R5 selected full dual-step prefix screening. The next continuation must
separately authorize provider/readiness work and the bounded prefix run. No
provider check, implementation or traffic run is authorized by S08 completion.

<a id="s09"></a>
## S09

Exact-prefix readiness and execution review, following S08 Candidate A.

- [00 Approved execution protocol and reached stop](s09_00_exact_prefix_readiness_execution_review.md).
- [Provider inventory](extraction/s09_provider_inventory.json).
- [20 Superseded readiness findings/provider gate](reporting/s09/s09_20_exact_prefix_readiness_findings_and_gate.md).
- [35 Current scope correction and methodology alternatives](reporting/s09/s09_35_scope_correction_and_methodology_alternatives.md).
- [90 Work/check report](reporting/s09/s09_90_exact_prefix_readiness_work_report.md).

The read-only provider audit is historical. DG-R6 provisioning is withdrawn;
the current review does not install or execute SUMO. Static methodological audit,
an explicit analytical construction/obstruction, and a bounded static source-code
audit are the available review-only continuations.

<a id="s10"></a>
## S10

Static future-protocol sufficiency review, following the S09 scope correction.

- [00 Methodology-only protocol](s10_00_future_protocol_sufficiency_review.md).
- [19 Colleague-facing methodology report](reporting/s10/s10_19_vsl_methodology_colleague_report.pdf)
  and [LaTeX source](reporting/s10/s10_19_vsl_methodology_colleague_report.tex).
- [Claim–evidence sufficiency matrix](synthesis/s10/s10_claim_evidence_sufficiency_matrix.md).
- [Post-closure freeway review option portfolio](synthesis/s10/s10_post_closure_freeway_review_options.md).
- [Approved post-closure next-step ordering](synthesis/s10/s10_post_closure_next_step_plan.md).
- [20 Findings and methodology closure gate](reporting/s10/s10_20_protocol_sufficiency_findings_and_gate.md).
- [90 Work/check report](reporting/s10/s10_90_protocol_sufficiency_work_report.md).
- [99 Review closure and recovery map](reporting/s10/s10_99_vsl_methodology_review_closure.md).

Gate result: DG-R7 Candidate A closed the review with conditional findings and
approved the successor ordering. S11 executed the first branch and subsequently
closed with TCR-E; no provider check or traffic execution occurred.

<a id="s11"></a>
## S11

Temporary-closure recovery task-admission review, following the S10 closure and
approved post-closure ordering.

- [00 Approved methodology-only review plan](s11_00_temporary_closure_recovery_admission_review.md).
- [Source audit](extraction/s11_temporary_closure_recovery_source_audit.md).
- [Admission and metric matrix](synthesis/s11/s11_temporary_closure_recovery_admission_matrix.md).
- [20 Findings and deferred G4 gate](reporting/s11/s11_20_temporary_closure_recovery_admission_findings_and_gate.md).
- [90 Work/check report](reporting/s11/s11_90_temporary_closure_recovery_work_report.md).
- [99 User closure and analytical handoff](reporting/s11/s11_99_temporary_closure_recovery_sprint_closure.md).

Gate result: G4-A was approved and the bounded TCR-E result accepted. Option 3
closed at task admission. The user authorized opening the planned analytical
Candidate B branch as S12, subject to a separate plan gate.

<a id="s12"></a>
## S12

Lightweight analytical advice–merge–service admission review, following the S11
closure and approved Step 2 ordering.

- [00 Approved methodology/model-admission plan](s12_00_analytical_advice_merge_service_admission_review.md).
- [Source audit](extraction/s12_advice_merge_service_source_audit.md).
- [Mechanism-admission matrix](synthesis/s12/s12_mechanism_admission_matrix.md).
- [20 Findings and deferred G4 gate](reporting/s12/s12_20_advice_merge_service_findings_and_gate.md).
- [80 Admission-rationale clarification](reporting/s12/s12_80_advice_merge_service_dialogue.md).
- [90 Work/check report](reporting/s12/s12_90_advice_merge_service_work_report.md).
- [99 User closure and targeted M2 handoff](reporting/s12/s12_99_advice_merge_service_sprint_closure.md).
- [Query log](search/s12_advice_merge_service_query_log.csv) and
  [access log](search/s12_advice_merge_service_access_log.csv).

Gate result: G4-A was approved and AMR-A accepted. One conservative finite-
receiving/mandatory-transfer family is admitted for separately gated analytical
testing. S12 is closed; no equation contract or certificate is implied.

<a id="s13"></a>
## S13

Targeted M2 analytical contract and certificate review, inserted before the
planned ramp-metering review after S12 closure.

- [00 Approved analytical contract/certificate plan](s13_00_m2_analytical_contract_certificate_review.md).
- [Source-to-equation audit](extraction/s13_m2_source_to_equation_audit.md).
- [Model contract PDF](synthesis/s13/s13_m2_model_contract.pdf) and
  [LaTeX source](synthesis/s13/s13_m2_model_contract.tex).
- [Certificate PDF](synthesis/s13/s13_m2_certificate_analysis.pdf) and
  [LaTeX source](synthesis/s13/s13_m2_certificate_analysis.tex).
- [20 Findings and certificate-disposition gate](reporting/s13/s13_20_m2_certificate_findings_and_gate.md).
- [35 Study-sufficiency and extension audit](reporting/s13/s13_35_study_sufficiency_and_extension_audit.md).
- [80 Contract dialogue](reporting/s13/s13_80_m2_contract_dialogue.md).
- [90 Work/check report](reporting/s13/s13_90_m2_certificate_work_report.md).
- [99 User closure and research-readiness boundary](reporting/s13/s13_99_m2_certificate_sprint_closure.md).

Gate result: M2C-R1 Candidate A was accepted. The audit classifies M2C-A as a
study kernel and the closure defines four prospective review stages toward a
research-ready task. The VSL continuation is deferred. A separately authorized
ramp-metering task-admission review is active in its own package; no VSL
implementation, empirical validation or later gradient work has started.

## Migration and maintenance

Primary reports are grouped by owning sprint under [`reporting/`](reporting),
and analytical/contract artifacts are grouped the same way under
[`synthesis/`](synthesis). Their directory READMEs define placement rules.
Filenames retain sprint/role prefixes, and root `sNN_00_...` plans remain beside
this sequence guide for fast access.

The [document registry](review_document_registry.csv) maps migrated and current
primary documents and records parent/gate relationships; newly created sprint
documents have an empty previous-path field.
Old filenames are not duplicate live documents or symlink aliases;
earlier console links to those old paths must be replaced by links from this index.
Package-local links and filename references were synchronized. Scientific content,
decision status and source archives were not revised by the rename.

For future approved continuations, assign the next sprint ID when a genuinely
new bounded review starts; record its parent decision and scope here. Revisions
inside a sprint retain its ID. Read/maintain this index and each current gate
together; adding an index row is not execution or closure authorization.
Mechanical checks and change accounting are in the
[navigation work report](reporting/shared/pack_navigation_work_report.md).
