# RM7.90 — Method-first ramp task-formulation work report

Date: 2026-10-01. Status: **RM7-UG1 / RMT-R1 closed; Candidate A approved.**

## Work completed

- Recorded the user's rejection of RM6's implementation-anchored reopening.
- Withdrew RMA-R1 without accepting or rejecting any RM6 candidate.
- Reclassified historical ramp findings as evidence rather than current-project
  compatibility constraints.
- Reframed the branch around task selection before model-family selection.
- Audited three task families against operational coherence, strong baselines,
  candidate hidden information, isolation, gradient motivation and evaluator
  feasibility.
- Formulated the recommended local merge-opportunity task and stopped at the
  task-selection gate.

## Files created

- `rm7_00_method_first_task_formulation_review.md`
- `extraction/rm7_method_first_source_reuse_audit.md`
- `synthesis/rm7_candidate_task_matrix.md`
- `reporting/rm7_20_method_first_task_formulation_and_gate.md`
- `reporting/rm7_90_method_first_formulation_work_report.md`
- `reporting/rm7_current_handoff.md`
- `reporting/rm6_35_method_first_scope_correction.md`

## Files updated

- RM6 plan, findings, matrix and work report to mark their gate withdrawn;
- package README and handoff pointers; and
- the VSL S10 next-step plan and S13 closure pointer so that they identify RM7
  as the active ramp review and RM6 as withdrawn.

Historical RM0–RM5 conclusions and the final colleague report were not revised.

## Evidence and commands

Reused the archived ramp source corpus and the later freeway source audits.
Inspected records with `find`, `rg`, `sed`, `tail` and `ls`; edited only review
documentation; validated package-local links and Markdown/diff formatting. No
broad web search was needed for task selection. An approved successor must run a
fresh targeted predecessor review for the selected task.

Final validation checked 54 local Markdown targets with zero broken links,
confirmed all six RM7 deliverables are nonempty, parsed the unchanged 61-row VSL
document registry, and passed `git diff --check`.

No simulator, implementation, traffic run, optimization, automatic
differentiation, calibration, package installation or project-plan change
occurred.

## Assumptions and risks

“Method-first” is interpreted as independence from current implementation and
milestone progress, while preserving the research boundary of infrastructure
ramp metering and matched model comparisons. It does not pre-approve microscopic
physics, stochastic gradients or any representation.

The main risks are aggregate-plus-scalar sufficiency, inability to construct a
matched hidden-state pair, nonsmooth/stochastic gap behavior, confounding by
capacity-drop assumptions and insufficient novelty beyond mature aggregate ramp
control.

## Current status and next allowed action

The user approved Candidate A and retained Candidate C as a possible later
extension after positive local results and a separate decision. RM7 is closed.
The [approval/discussion record](../discussion/rm7_candidate_a_approval_and_extension_record.md)
records the later documentation pass and the
[design inventory](../synthesis/rm7_post_selection_design_inventory.md).
A bounded RM8 proposal may be drafted; execution and implementation remain
outside the current authorization.
