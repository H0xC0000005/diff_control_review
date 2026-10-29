# CP-D2 option explanation: readability revision

Date: 2026-10-15. User-requested presentation correction only.

Reframed the decision around the traffic question: what determines the strength
and duration of the restriction left by a completed merge? The rewritten
report explains each direction's modeling philosophy and old/new change,
compares both through one E-burst/A-following example, and separates assumptions,
known behaviour, unresolved behaviour and scientific consequences.

Option 1 is the exact conditional model with a common recovery profile and
additive overlapping losses. Option 2 requires those relationships to be
supported from traffic conditions before accepting the primary law; its exact
model is not formed, and evidence could still justify a fixed response.
This distinction clarifies the existing options without selecting a new law.

## Files changed

- [AGENTS.md](../../../../context_snapshots/diff_minimal_meso/AGENTS.md): reinforced the existing global reporting
  preference with the user's 2026-10-15 decision-readability clarification.
  Preserved the preexisting edits; added only that preference block.
- [Findings and gate report](vsl_ph_recovery_work_findings_and_gate.md):
  rewrote the option section with conceptual explanations and direct comparison.
- [Living candidate inventory](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md):
  aligned the option descriptions and specification limits.
- [Dialogue](vsl_successor_opening_dialogue.md): archived the user's feedback,
  the presentation correction and unchanged decision status.
- This report and [documentary verification](vsl_ph_options_readability_validation.json).

## Scope, assumptions and remaining decision

Interpreted the request as reworking the explanation and recording its global
purpose. It does not approve either CP-D2 option, require a new traffic model,
or reopen an accepted endpoint/observation contract. No mathematical file,
source paper, numerical parameter or existing scientific result was changed.
The fixed prototype/additive-overlap limitations remain explicit.

CP-D1 stays closed with P-H. CP-D2 remains open; the provisional recommendation
is still Option 1 as a conditional elementary task. Step 3 remains open.
The next allowed action is the user's decision on the explained modeling
standard; no dependent review or implementation has begun.

## Commands and checks

Used read-only `cat`, `sed`, `rg`, `git status --short` and Python standard-library
hashing, followed by documentary `apply_patch`. No external source search,
LaTeX build or repeated mathematical test was needed because the mathematical
artifacts were unchanged.

```text
python3 /tmp/vsl_ph_options_readability_checks.py
```

The check verifies local links/heading anchors, current option/status wording,
unchanged mathematical and user-feedback hashes, and exact preservation of
the previous AGENTS.md content outside the added preference block. Its metadata
records counts and hashes. These are documentary checks, not traffic validation.
No simulator, installation, traffic experiment or gradient computation ran.

Final checks passed for five Markdown files, 133 local links and 20 heading
anchors. The P-H and accepted H1/T1 mathematical source/PDF hashes and the
user-feedback hash are unchanged. Removing only the added preference block
reproduces the pre-task AGENTS.md hash, confirming preservation of existing
instructions and user edits.
