# RM8 work report

Date: 2026-10-01. Status: evidence pass complete to RM8-UG1; user disposition pending.

## Work completed and result

Recorded approval of common open-loop rates and the recommended initial review
approaches. Drafted/transcribed the bounded RM8 protocol, executed its literature
and static-method audit, produced source/claim ledgers and synchronized status
pointers. The reviewed mechanism supports a conditional compact-local-state
admission candidate. Strong aggregate history/memory/scalar sufficiency remains
unresolved; no useful-gradient result is claimed.

RM8-UG1 presents three distinct candidates with problem, chain, gap, pros, cons
and dependencies. A recommends an analytic local-state review with early
history/scalar filters; B prioritizes aggregate closure; C reopens toward fine
gap timing. None is approved yet. No successor review was opened.

## Assumptions and scientific limits

- Latest interactive approval governs the review approach. 'Decisions resolved'
  closes initial planning, not evidence-dependent model adoption.
- Method-first review is independent of implementation compatibility. Historical
  negative decisions retain their earlier parallel-task scope.
- Review-only scope remains in force. Separate derivative correctness and
  independent one-step usefulness; do not infer either from a forward mechanism.
- Exact declared-history identity remains the first analytic target. A scalar
  may encode exactly the same group contrast; no full-lane necessity is assumed.
- Some leads are abstract/section-index only. No equations or decisive theorem
  were adopted from inaccessible text. Coverage is bounded, not exhaustive.
- RMT-R1.C multi-ramp stays deferred. VSL S13 closure and deferral are unchanged;
  two VSL files received navigation/status updates only.

## Files created

- `rm8_00_open_loop_local_merge_review_plan.md`
- `discussion/rm7_open_loop_approval_and_rm8_opening.md`
- `archive/metadata/rm8_source_access_record.md`
- `discussion/rm8_review_dialogue.md`
- `extraction/rm8_claims.csv`
- `reporting/rm8_20_findings_and_gate.md`
- `reporting/rm8_current_handoff.md`
- `screening/rm8_records.csv`
- `search/rm8_coverage_map.md`
- `search/rm8_query_log.csv`
- `synthesis/rm8_predecessor_and_information_map.md`
- `synthesis/rm8_task_gradient_reference_screen.md`
- `extraction/rm8_source_studies/aggregate_and_gradient_alternatives.md`
- `extraction/rm8_source_studies/continuous_lane_family.md`
- `extraction/rm8_source_studies/gap_timing_and_scope_boundaries.md`
- `extraction/rm8_source_studies/isolated_merge_and_hybrid.md`
- `reporting/rm8_90_work_report.md` (this report)

## Existing files updated

- `README.md`
- `reporting/rm7_current_handoff.md`
- `reporting/current_handoff.md`
- `synthesis/rm7_post_selection_design_inventory.md`
- `rm7_00_method_first_task_formulation_review.md`
- `discussion/rm7_g1_methods_clarification_record.md`
- `synthesis/rm7_g1_ramp_metering_methods_background.md`
- `../differentiable_freeway_bottleneck_task_review/synthesis/s10/s10_post_closure_next_step_plan.md`
- `../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md`

Historical source archives, feedback inboxes, project context, roadmap, source,
configuration, tests and environment files were not edited. Existing user-owned
changes to root AGENTS.md and PLANS.md were left intact.

## Tools, commands and validation

Primary-source browsing: search/open/find; 14 exact executed query entries in
`search/rm8_query_log.csv`, 17 source records and 17 linked claims. Public primary
PDFs were read through browsing; existing full texts were read locally without
redownload/overwrite. Metadata/access records distinguish inspected versions.

Filesystem inspection used `rg --files`, `rg -n`, `cat`, `head`, `tail`, `sed` and
`git status --short`. Local PDF extraction used pypdf via
`/home/zpz/miniconda3/envs/differential_sim/bin/python` (Python 3.11.9,
pypdf 6.15.0). Default Python lacks the required PDF reader; no package installed.
Document writes used standard-library Python and temporary scripts:

```
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/write_rm8_review.py
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/update_rm8_status.py
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/validate_rm8_review.py
```

Validation checks CSV shape/unique IDs, claim-to-source references, relative
local links and active status pointers. Final results are recorded below.
No traffic simulation, finite-difference/autograd experiment, optimizer, SUMO
installation/run or production test was performed. No equations/derivations
were newly presented; the artifacts are prose method audits with source locations,
so no mathematical PDF was necessary.

## Current status and next allowed action

RM7 planning decisions closed. RM8 evidence complete to user gate, not user-closed.
Discuss RM8-UG1 model-family admission. If A is selected, prepare the bounded
analytic formulation review plan before adopting laws. Scientific risks remain:
history identifiability, valid conservative reduction, real rate intervention
meaning, complete-accounting action benefit, nonsmooth sensitivities and independent
reference fidelity. No claim or gate was weakened to obtain a positive result.

## Final document-validation result

Passed: 76 local links; 17 unique source records; 17 valid claim/source references; 14 unique query records; CSV schemas and active handoff statuses. Zero validation errors. Scope: 17 new review files and 9 existing documentation updates.
