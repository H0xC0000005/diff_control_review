# Question 1 clarification: required starts versus an initialization extension

Date: 2026-10-21. Status: **Phase B discussion; UR-G1 remains open.**

Question 1 now separates the need to define the urban experiment's initial queues from the optional capability to prescribe nonempty physical-link states directly. M1 excluded/deferred that capability within its scope; it did not reject it scientifically. The VSL-like standard requires a reproducible admitted start, which can be restricted. It does not require general nonempty initialization.

The causal explanation compares equal approach counts with different travel readiness: traffic at the stop line can use service immediately, while newly entered traffic must first arrive. A mismatch changes discharge, TST and allocation sensitivity and could be mistaken for an order-representation effect. The text also distinguishes a fixed preparation from candidate-dependent queue formation, which would change the accepted fixed-initial-state sensitivity experiment.

## Files changed

- [First proposal, Question 1](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md#L18): narrower problem, explicit scope clarification, causal example, optional direct-preload candidate and revised recommendation.
- [Detailed register, UR-G1](../../extraction/research_readiness/urban_open_question_register.md): synchronized candidate meanings and recommendation; stable ownership/dependencies retained.
- [Logical gap explanation](urban_vsl_standard_gap_explainer.md): initialization completeness distinguished from an added capability.
- [Phase B dialogue](../../temp_content/research_readiness/phase_B_dialogue.md): user concern, correction and rationale archived.
- [Readiness overview](urban_readiness_overview.md): current clarification summarized.
- This work report and [document verification](urban_question1_clarification_validation.json).

## Assumptions and recommendation status

The user asks for clarification, not approval of a new initialization method. The earlier unaccepted recommendation blurred a shared consistency condition with Candidate A's optional extension. The revised provisional recommendation checks whether declared loading from the existing empty start supplies the required queue cases first, considering direct preload only for a demonstrated unmet need. Both candidates require consistent histories. Required V4 coverage has not yet been established for either construction.

The accepted initial state remains independent of the candidate allocation. Preparation-time accounting must be made explicit within the existing complete-TST contract. No checkpoint/restart interface, general initializer or source equation is assumed implemented. Other scientific options and accepted milestone plans are unchanged.

## Inspection, commands and checks

Inspected the latest urban feedback inbox, current proposal/register/decision records, initialization provisions of M0/M1, urban initial-state and derivative definitions, V4 initial-queue scope and VSL's restricted initial world. Commands used `sed`, `rg`, `cat`, `nl -ba` and `git status --short`. Edits used `apply_patch`. Python standard-library hashing captured the pre-edit snapshot at `/tmp/urban_question1_before_20261021.json`; the verification command checks local document links and preservation against it:

    python3 /tmp/urban_question1_document_check_20261021.py
    git status --short

Verification results are recorded in the linked JSON. Checks cover changed-document links and cited line bounds, stable global/local question IDs, the declared file-change scope and unchanged cited authorities/feedback. No scientific tests, traffic runs, gradient checks, optimization, package installation or PDF build are needed for this prose clarification, and none were run.

Result: **passed**. All 62 local links/line references resolve, the 14 question IDs are retained, and the 693-file snapshot shows exactly the five declared existing-file edits, with no outside changes or missing files. Cited authorities, feedback, simulator files and the pre-existing tracked modifications to `AGENTS.md`, `PLANS.md` and `memo.txt` are preserved.

## Remaining issue and next allowed action

The construction and accounting for the required urban initial-queue strata remain to be agreed. The next allowed action is discussion/revision of Question 1 and its provisional recommendation. No scientific candidate is marked approved, no global contract is closed and no implementation is opened.
