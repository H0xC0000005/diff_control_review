# Feedback 5: shared service meter response and gate revision

Date: 2026-10-15. Methodological discussion and documentary revision only.

## Outcome

Answered the user's mental-model question. One shared effective service
ceiling is sound and already compatible with the exact P-H candidate.
Traffic-dependent updates align more closely with the earlier Option 2.
Separated capacity from actual flow, current service use from future loss,
an additional A-discharge mechanism from queue-induced slowness, and one
reading from one sufficient recovery state.

Refined the options as M1 (unchanged exact representative E response) and
M2 (qualification of a discharge/speed-dependent shared-meter update).
The revised provisional recommendation is to qualify M2 with M1 as reference.
This is a proposal responding to the clarified physical target, not selection
of M2, an approved A capacity penalty or a completed new traffic law.

## Files changed

- [Feedback 5 response and comparison](vsl_feedback5_shared_service_meter_response.md): new decision-facing answer.
- [Live findings/gate](vsl_ph_recovery_work_findings_and_gate.md) and
  [candidate inventory](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md):
  replaced the old recommendation explicitly; identified one shared interface
  and unresolved update/state semantics.
- [Progress](vsl_review_progress.md), [Step 3 plan](vsl_step3_comparison_review_plan.md)
  and [dependent protocol](../../synthesis/research_readiness/vsl_step3_first_verification_protocol_draft.md):
  synchronized ownership/status and confined the exact proofs to M1.
- [Viewed-reference audit](../../extraction/research_readiness/vsl_ph_source_and_adaptation_audit.md):
  appended the three selected primary-source rechecks and access limits.
- [Dialogue](vsl_successor_opening_dialogue.md): archived the feedback,
  interpretation, proposal change and unchanged closed contracts.
- `README.md`, `vsl_successor_00_opening_plan.md` and
  `synthesis/research_readiness/vsl_successor_methods_outline.md`: current
  entry notices; earlier notices retain delivery-time status.
- `temp_content/feedback/vsl_refinement_feedback.md`: appended only
  `(answered)` to heading 5, as the inbox permits.
- This report and [verification metadata](vsl_feedback5_validation.json).

No mathematical source/PDF, production code, root instruction or roadmap
file was edited. Existing Git-visible AGENTS.md/PLANS.md/memo.txt changes
remain untouched in this task. The review package is saved on disk under
its existing Git-ignored path.

## Assumptions, limits and gate

Interpreted the meter as available shared service under sufficient demand,
not realized throughput. Preserved the declared undisturbed budget rather
than silently replacing it with an advice-dependent FD maximum. Treated
the user proposal as a question and invitation to refine candidates, not
as acceptance of an unspecified equation or broader modeling stack.

Boundary speed prediction, sufficient recovery memory, overlap and any
additional A influence remain open. An A queue alone does not establish
a second loss. No one-state reduction, universal queue-discharge penalty,
reference-speed oracle or new parameter is adopted. Existing exact M1
proofs and MP6/scalar findings do not prove an unspecified M2.

CP-D1 and S3-M1/S3-M2 remain closed. **CP-D2 remains open** with the revised
provisional M2 qualification recommendation. The terminal amendment and
Step 3 are not closed. Next allowed action: the user's choice on the clarified
update direction, then only the authorised bounded law qualification. No
dependent review, Step 4, simulator development or traffic experiment began.

## Commands and verification

Used read-only `cat`, `sed`, `rg`, `git status --short`, Python standard-library
hashing, and primary-source web open/find. Edited review documents with
`apply_patch` and a bounded Python replacement of the live gate section.
Updated the old gate-anchor link after renaming the heading. No LaTeX build
or mathematical test was needed because equations and PDFs were unchanged.

```text
python3 /tmp/vsl_feedback5_checks.py
```

The check covers local targets/anchors, current status/recommendation
consistency, before/after mathematical hashes and exact preservation of
feedback outside the permitted heading token. Its output is documentary
verification, not traffic validation. No dependency, numerical rollout,
calibration, AD/FD computation, optimisation or native SUMO run was executed.
