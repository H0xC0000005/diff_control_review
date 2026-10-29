# Feedback 3: corrected traffic reasoning and revised recommendations

22 October 2026. The response updates the main recommendation to responsive lane allocation, records loading from empty for development/early validation and defers local mixing. It corrects the threshold-only fixed-lane gradient claim, distinguishes redistribution from lossless merging, and explains why realized shared-lane order can still matter.

[Response, including the collected follow-up questions](urban_feedback3_response.md)

[Updated principle proposal](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md)

The user's follow-up clarifies that incoming package order governs the allocation sequence while actual admissions and downstream conditions determine lane occupation. The response records that distinction. It does not infer either erased lane order or a strict global admission prefix. The newly explicit shared question UR-G3-Q1 compares independent physical access with one strict feeder queue. The phase-rate interpretation and blocked-front policy remain open in the written response.

The user also requests that follow-up questions be collected in the material rather than asked through interactive console prompts. That preference is saved in AGENTS.md. No scientific answer is inferred from dismissal of the console prompts, and no further interactive prompts are used.

## Changed files

Updated existing files:

- [AGENTS.md](../../../../context_snapshots/diff_minimal_meso/AGENTS.md): one reporting-preference paragraph concerning written follow-up questions.
- [Principle proposal](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md): current decisions, corrected rationale and the allocation-order clarification.
- [Question inventory](../../extraction/research_readiness/urban_open_question_register.md): changed recommendations/statuses, continuous-share sensitivity note and new global subquestion UR-G3-Q1.
- [Overall plan](../../temp_content/research_readiness/phase_A_proposal.md), [supporting work map](../../extraction/research_readiness/urban_review_completion_and_work_map.md), [overview](urban_readiness_overview.md) and [logical-gap explanation](urban_vsl_standard_gap_explainer.md): synchronized direction, ownership and navigation.
- [Phase B decision record](../../temp_content/research_readiness/phase_B_revision.md) and [dialogue](../../temp_content/research_readiness/phase_B_dialogue.md): scoped decisions, corrections, unresolved interpretations and follow-up format.
- The user feedback inbox: only the permitted `(answered)` token on the feedback-3 heading.

Added the response, [evidence notes](../../extraction/research_readiness/urban_feedback3_evidence_notes.md), this report and the [verification record](urban_feedback3_validation.json).

## Evidence and interpretation limits

Inspected PROJECT_CONTEXT.md, PLANS.md, M1 initialization/merge semantics, M2's closed G2/G4/G6 contracts, the accepted urban phase-service/objective and P4/P8 records, the baseline/adoption matrices and prior discussion. A bounded web check of the already identified T0030 primary publisher text establishes its source scope; the evidence notes distinguish that from selecting a complete zone-entry operator. Direct publisher opening returned HTTP 403; indexed primary-publisher text was available. No full-PDF inspection, new source-equation adoption or numerical validation is claimed.

Q1 acceptance is limited to current development and early validation. The user's responsive-allocation preference updates the recommendation without approving a particular equilibrium or bypassing corrections. The rate principle does not select a phase clock. Deferring local mixing does not prove it infeasible. Existing realized lane order is retained, while the exact allocation admission rule remains open. Responsive allocation must be placed explicitly relative to M2 commitment; no inherited scientific contract is silently changed.

## Commands and checks

Inspection used `cat`, `sed`, `rg`, `head`, `git status --short` and the web search/open tools. Edits used `apply_patch` and Python standard-library text writes. The pre-edit snapshot is `/tmp/urban_feedback3_before_20261022.json`.

    python3 /tmp/urban_feedback3_document_check_20261022.py
    git status --short

The verification record checks local links and line bounds, the retained 14 IDs plus the new shared subquestion, unchanged candidate sets for existing questions, scope of the dependency addition, the narrow AGENTS.md edit and the feedback inbox's token-only change. It also checks preservation of original scientific authorities and simulator files. Traffic examples are causal illustrations. No production tests, traffic/gradient/optimization/SUMO runs, installations or PDF builds were performed for this prose discussion.

Task-owned checks passed: 109 local links/line references resolve; the original 14 IDs and their candidate sets remain, with UR-G3-Q1 bringing the inventory to 15 questions and 31 candidate entries. Its Type 2 classification and explicit dependencies in comparison/access/service records agree with the supporting map. AGENTS.md differs only by the written-follow-up preference, and the feedback inbox differs only by the permitted heading token.

The 717-file snapshot records ten declared existing-file edits, 706 unchanged files and one outside-task change: the separate VSL package's `reporting/research_readiness/vsl_successor_opening_dialogue.md`. Four new documentation/verification files are declared. This task did not edit or reverse the outside change. The cited scientific records, M2 decision archive, simulator files, PROJECT_CONTEXT.md, PLANS.md and memo.txt remain unchanged from the task snapshot; pre-existing tracked modifications are preserved.

## Current status and next allowed action

Phase B, categories 1–2 remains active. Preparation/accounting details, the allocation resistance/information and solution, physical access, commitment compatibility and coupled service law remain unresolved. The next action is written discussion of the two collected questions and corrected modeling direction. No component implementation or later experiment stage is opened.
