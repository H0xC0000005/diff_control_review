# Feedback 9: report-design discussion work and verification

Date: 2026-10-19. **Requested structure discussion delivered. The full
methods report and execution plan are not drafted or approved by this task.**

Read feedback 9 and answered its four questions: the proposed structure is
sound; make the physical/information contract explicit, distinguish equation
provenance from scientific status, retain the current model before its change
history, and keep the five sections with clear component/evidence logic.
The report fits Step 4's VSL methods/expert packet; selective urban alignment
and a separately reviewable execution proposal remain companion work.

[Detailed response and recommended structure](vsl_feedback9_report_structure_discussion.md)

## Files and authorized scope

Created three files in this directory:

- `vsl_feedback9_report_structure_discussion.md`
- `vsl_feedback9_work_report.md`
- `vsl_feedback9_validation.json`

Updated five review-package Markdown records:

- `README.md`
- `vsl_successor_00_opening_plan.md`
- `reporting/research_readiness/vsl_review_progress.md`
- `synthesis/research_readiness/vsl_successor_methods_outline.md`
- `reporting/research_readiness/vsl_successor_opening_dialogue.md`

Updated `temp_content/feedback/vsl_refinement_feedback.md` only by changing
its feedback-9 heading to `### 9 (answered)`, as that file expressly permits.
The validation check compares this exact transformation with its pre-edit
copy; no user feedback text is rewritten.

The user asks to discuss report writing first. Treated that as a bounded
Step 4 report-design discussion and kept the structure provisional. The
recorded formal Step 3 closure status is unchanged. Philipp and Wang's
feedback is recorded as reported by the user; no independent expert review,
validation or outreach is claimed. No model/claim/evidence criterion changes.

## Inspection, commands and checks

Read repository instructions/context, the active feedback, accepted Step 4
roadmap, current AS1–AS3 findings/protocol, and the archived H1, W-F and MP6
source/adaptation records. Those records support the proposal's illustrative
provenance distinctions. No new paper was viewed, source model adopted or
complete equation-by-equation manuscript audit claimed. The proposal uses
prose and equation roles, with no new mathematical derivation; Markdown is
appropriate for this structure discussion and no new PDF is needed here.

Commands used `cat`, `sed`, `rg`, `git status --short`, `apply_patch` and
read-only Python. A fresh SHA-256 snapshot at `/tmp/vsl_feedback9_before.json`
protects 444 existing files. The exact pre-edit feedback is retained at
`/tmp/vsl_feedback9_feedback_before.md` for the allowed-token check.
Document synchronization:

```bash
python3 /tmp/vsl_feedback9_sync.py
```

Final document/preservation verification:

```bash
python3 /tmp/vsl_feedback9_checks.py
git status --short
```

Checks cover the exact existing/new file sets, all other protected hashes,
local links and headings, the exact feedback token change, response coverage,
proposed rather than approved status, source/assumption/result distinctions
and unchanged root Git status. No scientific calculation, unit test, traffic
experiment, numerical gradient, installation or simulator work was required
or performed.

An initial wording assertion expected “does not claim novelty” while the
proposal explains the same boundary as a “separate novelty claim.” Corrected
that text assertion; the provenance rule and scientific scope are unchanged.

[Document and preservation results](vsl_feedback9_validation.json)

## Status and next allowed action

The feedback-9 response and concrete writing proposal are complete. Discuss
or refine this proposed structure before explicitly opening the full report
writing pass. This completes the user's requested discussion deliverable;
it does not complete Step 4 or freeze an execution plan. No new methodological
choice is forced. Physical admission and numerical usefulness remain
unestablished, SUMO optional, implementation/experiments unopened and the
ramp/urban lines closed. All previous mathematics, PDFs, source extractions,
results, build logs and validation records are preserved.
