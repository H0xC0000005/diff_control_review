# Selective-discreteness downstream-task review

Current methodology refinement asks which lane/order information and traffic laws are needed for useful signal-service sensitivities. It uses scientific topics, a decision record and a discussion log. The implementation phase/checkpoint structure does not govern this review.

[Current review guide and discussion material](temp_content/research_readiness/review_plan.md)

[Agreed conclusions and remaining questions](temp_content/research_readiness/review_decisions.md)

## Closed task-selection record

Status: **Part I closed on 2026-09-14.** V5/I1 is excluded. The migrated ramp-metering review in `../selective_discreteness_ramp_metering_review/` also closed on 2026-09-15 against adoption as a parallel new task.

The ramp-specific discussions have moved, with redirects retained below. All new ramp-review work belongs in the sibling package; this package retains the closed TSC review and its history.

**Historical Part-II handoff:** `discussion/part_2_scope_decision_record.md` records the scope transferred to the now-closed sibling ramp-metering review.

**Historical discussion:** `discussion/part_2_ramp_metering_scope_discussion.md` records the alternatives that preceded migration. The final Part-I decision is in `reporting/closure_record.md`; the ramp-review decision is in the sibling package's `reporting/closure_record.md`.

No review gate remains. Read `reporting/closure_record.md`, then `synthesis/project_impact_matrix.md`. The T6 approval and scope override are recorded in `discussion/t6_closure_record.md`. Older approval requests below are historical artifacts superseded by those records.

Purpose: evaluate and select a literature-supported downstream traffic/optimization task, then translate it into a complete experimental formulation for the selective-discreteness simulator.

Final update: the impact classification is accepted with P8 delegated to M3, and Part I is formally closed. Start with `synthesis/milestone_impact_summary.md` for the short M2--M6 handoff, then consult the detailed impact matrix as needed. Project-documentation synchronization remains separate work.

This package is separate from the completed model-lineage and baseline review in `../selective_discreteness_literature_review/`. No project methodology or roadmap is changed merely by material recorded here.

Current artifact:

- `reporting/t6_user_review_guide.md` — historical T6 gate guide; now superseded by the T6 closure record.
- `review_protocol_plan.md` — approved executable downstream-task review and formulation protocol; Part-I execution is complete through the T6 work stage.
- `discussion/protocol_approval_record.md` — accepted interpretations, conflict check, and current execution gate.
- `discussion/email_trace_20260909_analysis.md` — analysis of the colleagues' task ideas, assessment of the user's reply, and implications for the future review.
- `discussion/personal_preferences_plan_response_20260910.md` — assessment and approved interpretation of the user's four task-review preferences.
- `archive/email_trace_20260909_named_sources_metadata.md` — bounded metadata verification for the three works named in that email trace; not a T1 search corpus.
- `status_audit/current_downstream_task_status.md` — read-only audit of what the present project documents already define, defer, or leave open about downstream tasks.
- `screening/t3_review_gate.md` — closed T3 gate with the full screening table, expanded discussed records, and accepted decisions.
- `reporting/t1_t3_progress.md` — durable progress, access, anomaly, and phase-status report.
- `discussion/t3_closure_record.md` — approved inclusion, taxonomy, codebook, and paper-specific T3 decisions.
- `full_text/institutional_access_request_T4.md` — fulfilled one-paper institutional-access request and supply audit trail.
- `reporting/t4_access_pause.md` — resolved T4 access-pause history.
- `extraction/task_evidence_matrix.csv` — structured T4 task, derivative, baseline, transfer, and quality extraction.
- `extraction/t4_evidence_audit.md` — human-readable T4 evidence audit and current approval gate.
- `reporting/t4_completion_report.md` — T4 work report, reconciliation results, commands, and phase boundary.
- `discussion/t4_closure_record.md` — user approval and accepted T4 synthesis inputs.
- `synthesis/candidate_task_comparison.md` — detailed T5 alternatives, evidence-based recommendation, diagnostic hierarchy, and current approval request.
- `synthesis/future_task_map.md` — bounded conceptual map of later tasks and their promotion conditions.
- `synthesis/task_selection_record.md` — provisional task selection and intentionally deferred T6 details.
- `reporting/t5_completion_report.md` — T5 work report and phase boundary.
- `discussion/t5_closure_record.md` — Candidate-A selection, unresolved Part-II status, and T6 boundary.
- `discussion/forward_sensitivity_recursion_explainer.tex` and `.pdf` — beginner-oriented chain-rule derivation, scalar example, and traffic interpretation of the T6 forward-sensitivity recursion.
- `synthesis/primary_green_allocation_suite.md` — explicit V0–V4 primary layouts, traffic allocation, mechanisms, intentions, dependency order, and conditional post-suite test I1.
- `synthesis/experiment_formulation.md` — T6 task-facing contract summary and approval questions.
- `synthesis/experiment_formulation_formal.tex` and `.pdf` — formal action, objective, derivative, scenario-pair, and result contracts.
- `synthesis/baseline_realization_matrix.md` — shared-task realizations, capability boundaries, optimizer separation, and fairness rules.
- `synthesis/literature_adoption_matrix.md` — paper-to-baseline equation, method, software, adaptation, licensing, and implementation-affinity audit.
- `reporting/t6_completion_report.md` — T6 evidence, checks, assumptions, and phase boundary.
- `discussion/gradient_contract_intermediate.tex` and `.pdf` — intermediate response defining the task-dependent gradient contract, baseline differentiability qualifications, toy examples, and implications for the review protocol.
- `discussion/review_necessity_and_plan_role.md` — methodological discussion of why the task review is needed, how it should govern model design, expected outcomes, and change-control thresholds for active and closed milestones.
