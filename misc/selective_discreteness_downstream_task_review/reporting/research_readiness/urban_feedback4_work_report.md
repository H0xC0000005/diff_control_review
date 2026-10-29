# Feedback 4: settled principles and a clearer upstream waiting model

23 October 2026. The response records effective average service as accepted and answers the status question directly: all four broad principles are settled for this stage. Q2/Q4 still need a concrete coupled allocation/waiting/access model; that is specification work, not another broad option vote.

[Response to feedback 4](urban_feedback4_response.md)

[Updated principle proposal](../../temp_content/research_readiness/phase_B_categories_1_2_principle_proposal.md)

The response accepts partial physical entry of continuous packets, separates logical lane assignment from actual zone entry and treats pending lane queues as records of mass still in the aggregate upstream link. A valid established lane commitment stays fixed by default, preserving the inherited no-reassignment rule. Provisional retargeting is recorded as a deferred alternative. The first draft unnecessarily made that an extra required principle choice; the final records preserve the existing default instead.

The response also corrects two consequential implications. A phase-based model can have nonzero duration sensitivities through changing switching times. Positive room or capacity alone does not establish physical access/eligibility, and no small positive admission deadband is adopted. Reusing an already valid desired target does not itself define a new allocation rule.

## Files and decisions

Updated the current principle proposal, full question inventory, Phase B decision/dialogue, overall plan, supporting completion/ownership map, readiness overview and logical-gap explanation. The prior feedback-3 response has a current-navigation notice. The feedback inbox changes only by the permitted heading token. The response, [evidence notes](../../extraction/research_readiness/urban_feedback4_evidence_notes.md), this report and the [verification record](urban_feedback4_validation.json) are new files.

The inventory retains all 15 stable IDs and their classifications. Under UR-G3-Q1, the older physical admission candidates A/B remain, while C/D describe a separate waiting-target axis: fixed commitment as default versus provisional retargeting deferred. C1's dependency on that global ownership/commitment contract is now explicit. No concrete solver, physical access law, new cutoff, additional physical buffer or replacement of M2's ingress contract is approved.

The user feedback is interpreted in the context of the existing fixed-commitment rule and reporting preference. Fixing a valid commitment is not a new claim that the responsive allocator is already implemented or that its interface is fully specified. If the concrete model exposes a conflict, the smallest affected contract must be reconsidered explicitly.

## Inspection and checks

Inspected the latest feedback and live review records, PROJECT_CONTEXT.md, PLANS.md, approved M1 partial-split/timing semantics, M2's closed ingress/geometry/differentiation contracts and the accepted urban average-service/TST definition. Commands used `cat`, `sed`, `rg`, `head` and `git status --short`; edits used `apply_patch` and Python standard-library text writes. The bounded web check used the official abstract/metadata of arXiv:1204.1910v3 as support for the phase-sensitivity correction. No full-paper method qualification or source-equation adoption is claimed.

The pre-edit snapshot is `/tmp/urban_feedback4_before_20261023.json`. The check command is:

    python3 /tmp/urban_feedback4_document_check_20261023.py
    git status --short

The linked verification records local links and cited line bounds, stable question IDs/classification, preservation of prior candidate entries plus the new C/D variants, the scope of the C1 dependency refinement, feedback token-only handling and preservation of scientific authorities and simulator files. The packet arithmetic and signal examples are explanatory, not new experimental findings. No production tests, environment changes, package installations, traffic/gradient/optimization/SUMO runs or PDF builds were performed.

Task-owned checks passed: 115 local links and line references resolve; all 15 IDs/classifications are retained, with the C/D variants bringing the inventory to 33 candidate entries. C1's new global dependency agrees with the supporting ownership map, while the completion, stage and report-budget tables remain unchanged. The feedback inbox differs only by the heading token. Root instructions/context/roadmap, the M2 archive, approved plans and simulator files are preserved.

The 745-file snapshot records ten declared existing-file edits, 733 unchanged files and two outside-task changes in the separate VSL package: its `README.md` and `reporting/research_readiness/vsl_successor_opening_dialogue.md`. Four new documentation/verification files are declared. This task did not edit or reverse the outside changes, and the pre-existing tracked modifications remain intact.

## Status and next allowed action

Phase B, categories 1–2. The four principle directions are settled; detailed global interfaces, allocation cost/solution, bay-access law, coupled service and complete sensitivity are not yet frozen. The next allowed action is review/consolidation of this principle record and continuation of the remaining global discussions when requested. The later authorized coupled proposal preserves the commitment default and reports genuine amendments before formal component closure. No implementation or later milestone is opened.
