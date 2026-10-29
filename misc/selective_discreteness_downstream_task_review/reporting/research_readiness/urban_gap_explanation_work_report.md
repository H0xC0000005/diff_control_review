# Urban gap explanation: work record

Date: 2026-10-20. Status: explanatory response at the S0–S1 opening gate; no later stage started.

The added explanation supplies the missing connection between the VSL completion standard and the urban question inventory. It groups the work by five logical purposes and uses direct comparisons of the accepted documents to show why each gap exists. The old urban review's task and evidence contract remain accepted; the explanation identifies where model completion and presentation still need work.

## Files changed

- Added [the gap explanation](urban_vsl_standard_gap_explainer.md), this work record and [its static verification](urban_gap_explanation_validation.json).
- Added a reading link to [the overview](urban_readiness_overview.md) and [the proposal](../../temp_content/research_readiness/phase_A_proposal.md).
- Appended the request and response to [the dialogue](../../temp_content/research_readiness/phase_A_dialogue.md).

The detailed question register, authority/gap audit, rubric table, plan stages, candidate bodies and original urban/VSL scientific records were retained. The earlier opening work report/verification remain historical records of that pass; this pass has its own preservation snapshot and verification.

## Assumptions and scope

The user's positive assessment is read as feedback on the opening, followed by an explicit request for explanation. It is not treated as an instruction to choose a new law, execute S2 or draft the final methodology report. The five categories explain why the questions exist; Type 1/Type 2 still governs ownership and A/R/N/E still describes work status. C6's external mapping requirement comes from the urban contract, so the comparison does not falsely claim that VSL already supplies that deliverable.

No new source equations or mathematical derivation were introduced. The comparisons concern the completeness of inspected documentary specifications. The prose/table explanation needs no new formula-heavy PDF. The existing LaTeX/PDF sources were used as evidence, without changing or rebuilding them.

## Commands and checks

Read-only commands used git status --short, cat, rg -n, sed and nl -ba to revisit the current opening documents, accepted VSL report source/coverage/assumption audit, formal urban source, adoption matrix, P4/P8/P10 impact decisions and M2 global revision. Existing feedback headings were checked; the interactive request is the active feedback and is archived in the dialogue. No feedback file was edited and no external literature search was needed.

Edits used apply_patch. Python standard-library hashes captured 815 existing files before editing at /tmp/urban_gap_bridge_before_20261020.json. The check command is:

    python3 /tmp/urban_gap_explanation_checks_20261020.py
    git status --short

Static checks passed: all 14 question IDs have an explicit place in the explanation, the substantive IDs each have one primary table assignment, all five categories contain a source comparison, local links and cited source line targets resolve, and the detailed register/audit are byte-identical. One source-line link was corrected from a blank line to its section heading during checking. The rubric/stage sections are unchanged. Of the 815 existing files, only the three declared navigation/dialogue files changed; the remaining 812 are unchanged. The three added artifacts are all documentation/verification. The durable verification gives exact counts, changed paths and hashes.

No simulator code, dependency, traffic run, gradient check, optimization or SUMO execution was involved. The working branch remains m2_interaction_zone. Ordinary git status still contains only the pre-existing AGENTS.md, PLANS.md and memo.txt modifications; these package artifacts remain ignored under existing rules.

## Remaining status

The prior unresolved methodological questions remain open. This response makes their connection to the standard explicit and does not settle their candidates. Review of the opening standard/inventory/plan can continue; S2 global-contract review requires its own opening. No implementation or subsequent scientific review stage began.
