# Selected W-F: forward qualification work and verification

Date: 2026-10-16. **J4-W1 closed with W-F; forward review delivered at
WF-Q1. Step 3 remains open.**

## Result, authorization and assumptions

The user selected the concrete W-F work expression and required advice to
act through local traffic state. Recorded that decision and executed the
next joined forward-domain check. The coefficient is fixed in physical
units; the upper-advice anchor fixes those units once. The local state
includes the previously selected O-R recovery memory, not just current
queues. No initial observation, geometry, demand scope, priority, recovery
source or objective boundary is changed.

The analytical argument covers the entire original constant-advice interval
under the retained sufficient H1/T1, ordinary-underload, root-monotonicity,
positive-recovery and storage conditions. It combines the monotone H1 pulse,
one E waiting episode, positive separation of repeated A events, previous
within-regime O-R causality and a common clearance bound. This is a proof
about the declared conditional model, not empirical traffic validation or
a theorem about arbitrary boundary histories/general network junctions.

It also establishes full-domain compact initial-information reconstruction,
retains the earlier A-delay/active-renewal witness at the reference advice,
and records the no-extra-work negative control and local activation-flux
gap. No control or gradient advantage is inferred.

## Files changed

Eight new artifacts:

- `reporting/research_readiness/vsl_wf_selection_and_scope.md`
- `reporting/research_readiness/vsl_wf_forward_qualification_and_checkpoint.md`
- `extraction/research_readiness/vsl_wf_forward_source_audit.md`
- `synthesis/research_readiness/vsl_wf_forward_qualification.tex`
- `synthesis/research_readiness/vsl_wf_forward_qualification.pdf`
- `reporting/research_readiness/vsl_wf_forward_build.log`
- `reporting/research_readiness/vsl_wf_forward_work_report.md`
- `reporting/research_readiness/vsl_wf_forward_validation.json`

Fourteen existing Markdown records synchronized: package README, successor
opening plan, progress, Step 3 plan, C-P plan, O-R selection/checkpoint,
successor dialogue, previous W-A/W-F gate report, feedback-6 joined plan,
MP1–MP6 inventory, living model/question inventory, methods outline and
first-verification protocol draft. Closed gate IDs and prior mathematical
artifacts are retained. Earlier report bodies are labeled delivery history.

The package is Git-ignored. The pre-existing user edits in root `AGENTS.md`,
`PLANS.md` and `memo.txt` remain unchanged. The preservation snapshot covers
238 other root/feedback/closed-task/previous review artifacts. No production
simulator file, source test, environment or dependency was modified.

## Commands and validation

Read-only inspection used `git status --short`, `rg --files --no-ignore`,
`rg -n`, `cat` and `sed`. Read repository context, handoff/current review
authorities, feedback entries and the accepted/selected model records.
No implementation milestone was opened. Primary web open/find rechecked
Carey, Jin–Gan–Lebacque and Leclercq as listed in the viewed-reference audit;
no new full-paper or empirical replication is claimed.

Snapshot: `/tmp/vsl_wf_forward_before.json`.
Document synchronization command: `python3 /tmp/vsl_wf_forward_sync.py`.
The first attempt stopped before any write because its paragraph matcher
lacked multiline matching; the matcher was corrected and synchronization
completed. A later patch with mismatched context made no changes and was
reapplied against the inspected text. Neither issue changed model semantics.

Supporting exact algebra:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_wf_forward_algebra.py
```

Nine symbolic identities and ten exact static checks passed. They cover the
work-root derivative, fixed-state advice exclusion, free-A speed response,
critical-front flux gap, recovery primitive, H1 receiving-branch sign and
illustrative budget/event bounds. The first rational check accidentally used
Python floating division; inputs were changed to exact rationals, preserving
the expected assertions. These are not traffic simulations or numerical
gradient checks. The quantified event/continuation proof still requires
human mathematical review; the symbolic script does not certify it.

Verified installed LaTeX at `/usr/bin/pdflatex`. Build:

```text
python3 /tmp/vsl_wf_forward_build.py
```

The script runs `pdflatex -interaction=nonstopmode -halt-on-error
-file-line-error` twice into `/tmp/vsl_wf_forward_latex`, then copies the
PDF and final log. A justified narrow table cell initially produced an
underfull line; ragged-right cell formatting removed it. The final PDF has
six pages and a clean build log. PDF text/font/parse checks are recorded in
the validation JSON; raster visual inspection is not claimed. Installed
SymPy and pypdf were used without installation or environment changes.

Final document/PDF/status/preservation verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_wf_forward_checks.py
```

**Final checks passed:** 18 Markdown records, 550 local links and 30 heading
targets; all 238 protected hashes match. Nine symbolic identities and ten
exact static checks passed. Strict PDF parsing confirms six pages, 175,606
bytes and 49 Type 1 font resource references, with no build warnings.
No scientific acceptance criterion was weakened. The analytic proof remains
available for human review rather than described as mechanically certified.

## Remaining risks, status and next allowed action

This pass completes the planned conditional forward block at WF-Q1, an
evidence checkpoint without a new model-choice request. It does not close
physical MP6 or Step 3. Crossing-speed identification, the interaction
coefficient, renewal/recovery scales, old-profile retirement and possible
double charging of immediate work versus recovery remain physical hypotheses.
Queue activation can change local flux abruptly; full-objective derivative
behavior must be assessed separately. The theorem does not establish an
interior optimum, full-lane-state necessity or useful external gradients.

After this checkpoint's review, the next allowed work is joint physical-domain
and applied-MP6 qualification, then dependent information/action/sensitivity
and SUMO correspondence under the original evidence ladder. Step 4 remains
unopened. No traffic experiment, ODE trajectory, numerical derivative,
calibration, optimization, SUMO execution or detached process occurred.

[Plain findings and checkpoint](vsl_wf_forward_qualification_and_checkpoint.md)

[Selected decision](vsl_wf_selection_and_scope.md)

[Mathematical support](../../synthesis/research_readiness/vsl_wf_forward_qualification.pdf)

[Reference list](../../extraction/research_readiness/vsl_wf_forward_source_audit.md)

[Machine-readable checks](vsl_wf_forward_validation.json)
