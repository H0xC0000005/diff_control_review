# Proposed migration manifest and entry-point patch — draft

Status: **Proposal only; do not execute without explicit user approval**  
Prepared: **2026-09-15**

## 1. Proposed repository additions

After content approval, create this new supplementary directory:

`temp_content/milestone_2_per_lane_interaction_zone/supplements/`

Add two new files, with the word `_draft` removed from their names and draft
status replaced by an approved supplementary status:

| Staged draft | Proposed repository file |
|---|---|
| `milestone_2_review_findings_supplement_draft.md` | `supplements/downstream_task_review_methodology_handoff.md` |
| `milestone_2_component_crosswalk_draft.md` | `supplements/downstream_task_review_component_crosswalk.md` |

These would be new files. They would not overwrite any existing proposal,
dialogue, revision, question-register, project-context, roadmap, source, test, or
configuration file.

The staging `README.md` and this migration manifest are review-process files and
are not proposed for migration.

## 2. Only proposed edit to an existing Milestone 2 file

The sole existing-file change would add an entry point to
`temp_content/milestone_2_per_lane_interaction_zone/phase_B_revision.md`. The
proposed insertion is after `## Next Phase B activity` and its existing
paragraph:

```markdown
## Supplementary review-methodology handoff

Accepted downstream-task and task-scope review findings relevant to the remaining
component discussion are summarized in:

- `supplements/downstream_task_review_methodology_handoff.md`; and
- `supplements/downstream_task_review_component_crosswalk.md`.

These files are supplementary evidence and methodology guidance only. They do
not alter G1--G6, decide or close a component-local question, approve Phase C,
authorize implementation, or advance the milestone status.
```

This insertion provides discoverability only. It does not rewrite the existing
status, global decisions, dependency result, or next activity.

## 3. Files explicitly excluded from amendment

No change is proposed to:

- `AGENTS.md`;
- `PROJECT_CONTEXT.md`;
- `PLANS.md`;
- `phase_A_proposal.md` or `phase_A_dialogue.md`;
- `phase_B_dialogue.md` or `phase_B_chitchat_answers.md`;
- `phase_B_component_question_register.md`;
- `phase_B_component_2_1_questions.md`;
- any approved milestone plan;
- production source, tests, configurations, dependencies, or reports; or
- either closed review package.

If a future development pass decides that an active candidate or decision record
must change, that change must occur through the normal Phase B dialogue and
approval workflow. It is not part of this review synchronization.

## 4. Proposed approval and execution sequence

1. User reviews and approves or revises the two draft contents and this manifest.
2. In a separate authorized task, copy the approved texts into the two new
   supplementary repository files.
3. Apply only the link-only entry-point insertion shown above to
   `phase_B_revision.md`.
4. Verify links, status wording, and a path-limited Git diff.
5. Stop and report the exact diff. Do not advance Milestone 2 phases or edit
   component candidates.
6. Stage, commit, and push only if the user's approval explicitly includes those
   Git operations and the target branch/remote are confirmed.

## 5. Acceptance checks for the future migration

- The two repository supplements are byte-for-byte equivalent in substance to
  the user-approved drafts apart from approved status/path edits.
- The only modified pre-existing file is `phase_B_revision.md`, and its diff is
  link-only plus the non-authority disclaimer.
- `PROJECT_CONTEXT.md`, `PLANS.md`, all active component question files, source,
  tests, and configs have no new diff from this operation.
- The active status still reads “Milestone-global backbone closed;
  component-local discussion active.”
- No review statement is represented as implementation evidence or as closure of
  an open Milestone 2 decision.
- No Git push occurs without explicit approval.
