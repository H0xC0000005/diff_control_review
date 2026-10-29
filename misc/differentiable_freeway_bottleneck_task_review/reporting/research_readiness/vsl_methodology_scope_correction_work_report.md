# Scope correction: work and preservation record

2026-10-21. **Executable proposal withdrawn; analytical review proposal
reworked. No review sprint, implementation or experiment is executed here.**

The user clarifies that the review is analytical and methodological. The
three conceptual checks remain appropriate, but a Python evaluator, numerical
tests and control experiments are outside the intended scope. The previous
interpretation expanded the task. Correct it explicitly; do not treat the
unapproved implementation proposal as an inherited user decision.

**What changed and why.** Replace the active implementation proposal with
a short retirement notice and archive its original. Revise the handoff
around analytical responsibilities, preserving the earlier version in the
same historical archive. Replace the execution-gate overview with a scope
correction. The VJV-P/F/S/U implementation gates, code/test plan, tolerances,
query budgets, run commands and experimental-configuration freeze are
withdrawn, not merely renamed.

The new plan retains VC1–VC3 as methodological questions in one bounded
review sprint: source/model joins; complete accounting and conditional
sensitivity; and task/RQ fit, simpler rivals and colleague justification.
Reuse the existing proofs and source studies; add focused reasoning only
for a real gap. Completion at JM1 requires a clear methodological conclusion,
not positive information value, optimizer success or numerical derivative
agreement. Stop earlier for a genuine new scientific choice. This task
revises the proposal only and does not perform that sprint.

**Files.** Add the following five records across the review and historical
planning folders:

- [Active analytical review plan](../../synthesis/research_readiness/vsl_joined_candidate_methodology_review_plan.md).
- This work report.
- [Document/preservation verification](vsl_methodology_scope_correction_validation.json).
- [Withdrawn executable proposal](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_vsl_joined_validation/archive/phase_A_executable_proposal_withdrawn_20261021.md).
- [Earlier handoff before scope correction](../../../../context_snapshots/diff_minimal_meso/temp_content/milestone_vsl_joined_validation/archive/validation_handoff_before_scope_correction_20261021.md).

Update nine existing documents: review README, progress, joined findings,
handoff, prospective numerical evidence contract, execution-gate overview,
successor dialogue, temporary Phase A proposal and temporary Phase A dialogue.
The handoff and gate overview are rewritten to the correct scope; the old
proposal path now directs readers to the replacement. Historical planning
reasoning is marked withdrawn and corrected rather than silently treated
as approval. The prospective empirical contract remains future research,
with its scientific requirements unchanged below the scope notice. The old
planning JSON remains a historical document-check result.

**Assumptions and limits preserved.** The selected LF1/LF2 traffic model,
common-FD/finite-cohort/free-exit assumptions, initial information diagnostic,
one-scalar sufficiency, exact residual and regular derivative retain their
previous meaning and limits. No source finding, equation, proof, PDF or
accepted report is changed. Illustrative values are not frozen as a run
configuration. There is no claim of positive optimal-action value, required
full lane detail, numerical gradient correctness or physical fidelity.
The accepted report/Step 4, separate historical gates, urban work and ramp
closure retain their status.

**Commands and document checks.** Use `cat`, `sed`, `tail`, `rg`,
`git status --short` and `apply_patch` to inspect and revise documents.
Python standard-library path, hashing, JSON and link-processing operations
snapshot files, preserve the two withdrawn originals and rebase their
relative archive links. These are document operations, not traffic tests;
no traffic evaluator or test Python file is created. One tool-orchestration
variable typo was corrected before the document outputs were inspected;
it made no file changes or scientific decision.

Snapshot: `/tmp/vsl_methodology_scope_correction/before.json`, covering 552
prior review-package files and 712 protected existing files in total,
including production source/tests/configs/runners, approved milestone plans,
urban Phase B, root authority and feedback. Verify with:

```bash
python3 /tmp/vsl_methodology_scope_correction/document_checks.py
git status --short
```

All document assertions pass: nine expected existing documents changed,
the other 703 protected files preserved, five expected records added and no
deletions. Of the prior review-package files, 545 are byte-preserved. Active
and archive Markdown links resolve; the archived bodies match the old
documents apart from the declared withdrawal header and link rebasing.
Existing scientific bodies below the corrected notices remain unchanged,
including the complete prospective numerical contract. The checker confirms
that proposed implementation/config/test/runner and frozen-plan paths were
not created. Equations, PDFs, source audits, accepted reports, user feedback
and production bytes remain unchanged.

No traffic trajectory, AD/JVP/FD calculation, optimizer, pytest suite,
training, dependency installation, environment probe, branch/worktree,
sub-agent or external message occurs in this correction. No mathematical
result is newly derived and no new PDF build is needed. Existing mathematics
remains in its linked PDF/LaTeX authority. No stochastic seed or scientific
run configuration applies to this documentary task.

**Status and next review work.** Proposal correction is complete; the bounded
analytical sprint has not begun. The next review action is VC1's source/model
interface audit, then VC2–VC3, ending at JM1 or an earlier methodological
choice. No execution milestone or implementation permission is pending
within this review. Future empirical evidence remains outside its closure
requirements.
