# Feedback 2: explain the traffic choices in ordinary language

21 October 2026. The current proposal, overall plan and all 14 questions are rewritten. Each question now explains what traffic issue matters and what the user is deciding, then describes candidates through their core ideas, behavior and tradeoffs. The required problem/function/gap and labeled pros/cons/dependency template is removed. Examples carry the distinctions between arrival readiness, physical bay access, service timing and order approximation.

[Rewritten current proposal](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md)

[Rewritten overall plan](../../temp_content/research_readiness/phase_A_proposal.md)

[Complete conceptual question set](../../extraction/research_readiness/urban_open_question_register.md)

The user's instruction applies to later reports and question/candidate statements, so the old reporting block is replaced in [AGENTS.md](../../../../context_snapshots/diff_minimal_meso/AGENTS.md#L76). Precision is useful when it helps understanding; it is no longer a required checklist for the question statement. The edit preserves the surrounding repository instructions and unrelated pre-existing changes.

The current proposal is 1,750 words, compared with 3,271 before this rewrite. The wider plan is 1,132 words, compared with 2,714; the full inventory is also shorter. Detailed completion, ownership, stage and report-budget tables move to a [supporting map](../../extraction/research_readiness/urban_review_completion_and_work_map.md). The tables retain the earlier content and do not dictate the conversation.

The modeling choices retain their prior status. Loading from empty remains the provisional first approach for starting queues; direct nonempty initialization is optional. Fixed versus responsive lane intent remains separate from the missing physical-access law. Average versus timed service, exact versus relaxed order, and the passage-time modeling direction remain distinct. No scientific candidate is accepted by a reporting rewrite.

The active discussion remains Phase B, categories 1–2. The next action is review/discussion of the four traffic choices. The later comparison, sensitivity, implementation and experiment work has not started. Required queue-case coverage and concrete access/service laws remain unresolved.

## Files and record updates

Alongside the three rewritten documents and AGENTS.md, the readiness overview, logical-gap explanation, Phase B decision record and Phase B dialogue now point to the current approach. The feedback-1 response has a historical notice, and the earlier Question-1 report has its link corrected to the rewritten question. Historical scientific evidence and previous work reports otherwise remain intact. The only feedback-inbox change appends `(answered)` to the feedback-2 heading.

The new files are the supporting completion/work map, this report and the [verification record](urban_feedback2_validation.json). All changed files are listed in that record. The user request is interpreted as a persistent reporting instruction, not an authorization to change traffic behavior or implement a model.

## Inspection and verification

Inspection used `cat`, `sed`, `rg`, `wc -w` and `git status --short`, covering feedback 2, AGENTS.md, PROJECT_CONTEXT.md, PLANS.md, the current proposal/inventory, accepted baseline roles and the prior discussion records. Edits used `apply_patch` and Python standard-library text writes. No dependency, environment, simulator, test or scientific-result file was edited. There was no new source-equation adoption or literature search.

The pre-edit snapshot is `/tmp/urban_feedback2_before_20261021.json`. Verification checks local links and cited line bounds, continuity of the 14 IDs and their candidate sets, preservation of the technical tables, the narrow AGENTS.md edit and the feedback file's append-only rule:

    python3 /tmp/urban_feedback2_document_check_20261021.py
    git status --short

Results are recorded in the linked JSON. The traffic examples are explanatory illustrations, not numerical findings. No traffic, gradient, optimization or SUMO runs, package installations, production tests or PDF builds were performed for this prose revision.

The task-owned checks passed: 86 local links and line references resolve; all 14 question IDs and 29 candidate entries are retained; the six supporting tables are preserved verbatim; AGENTS.md differs only within the replaced reporting block; and the feedback inbox differs only by the permitted heading token. The 696-file snapshot records 11 declared existing-file edits, 684 unchanged files and one outside-task change. Three new documentation/verification files are declared.

The outside change is the separate VSL package's `reporting/research_readiness/vsl_successor_opening_dialogue.md`. This task did not write it or reverse that change. The original scientific authorities cited here, simulator files, PROJECT_CONTEXT.md, PLANS.md and memo.txt remain unchanged from the task snapshot. The pre-existing tracked changes are preserved.
