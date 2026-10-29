# Physical MP6 review: work, assumptions and verification

Date: 2026-10-16. **MP6-Q1: planned physical/source and identifiability review
delivered. Applied MP6 and Step 3 remain open; Step 4 is unopened.**

## Result and authorization

The user reviewed the forward checkpoint, clarified that E non-requeueing
is conditional, received the remaining three-block recap and directed
proceeding. This pass completes the physical/source block and stops at its
evidence checkpoint. It does not open implementation or numerical evidence.
There is no new model alternative requiring a choice.

The central result is a joint physical admission contract: distinguish actual
crossing-speed marks, immediate maneuver work and retained recovery, rather
than infer a correct decomposition from total TST. A queued A-only tail can
expose residual recovery; distinct mixed-service covariates can constrain
remaining maneuver cost conditionally. The source's square-root boundary
quantity is not a vehicle-speed trajectory. Preparation-scale confounding,
stationary headway limits and smallest reopen conditions are explicit.

This is mathematical/source analysis and future evidence specification,
not a supported numerical regime or passed empirical admission. No theory-only
primary, new speed state, spatial cells, A recovery source, adjustable renewal
window, changed initial observation or widened objective is selected.

## Files changed

Eight new review artifacts:

- `reporting/research_readiness/vsl_mp6_physical_findings_and_checkpoint.md`
- `synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md`
- `extraction/research_readiness/vsl_mp6_physical_source_audit.md`
- `synthesis/research_readiness/vsl_mp6_physical_identifiability.tex`
- `synthesis/research_readiness/vsl_mp6_physical_identifiability.pdf`
- `reporting/research_readiness/vsl_mp6_physical_build.log`
- `reporting/research_readiness/vsl_mp6_physical_work_report.md`
- `reporting/research_readiness/vsl_mp6_physical_validation.json`

Eleven existing Markdown records synchronized: package README, successor
opening plan, progress, Step 3 plan, C-P qualification plan, feedback-6 joined
plan, MP1–MP6 inventory, living model/question inventory, methods outline,
first-verification draft and successor dialogue. Current notices supersede
older delivery-time statuses; prior mathematics and sources are preserved.
The living inventory records ownership and remaining admission without
changing MP definitions or closed choices.

The review package is Git-ignored. Pre-existing root edits in `AGENTS.md`,
`PLANS.md` and `memo.txt` remain unchanged. The fresh snapshot protects 337
root/feedback/closed-task/prior-review artifacts. No production code, tests,
environment file, existing result or user feedback was edited.

## Assumptions and limits

Retain the selected H1/T1/W-F/S-E-P/R-E/O-R model, fixed physical coefficient
and recent-mass normalization, original advice domain, known empty terminal/
memory, continuing symmetry, finite cohort and local complete-TST objective.
Conditional identities require binding service or the indicated informative
branch; they do not guarantee such observations exist in a native dataset.
The E non-requeue theorem additionally depends on the monotone H1 pulse,
selected marks/recovery and retained bounds. Finiteness alone is insufficient.
Native bursty requeueing is not an automatic evaluator failure.

The single-observation work/recovery ambiguity is an accounting example,
not a second admissible O-R history or a theorem of global non-identifiability.
Exact algebra does not certify statistical identification, physical mechanism
independence, an applied parameter range or control usefulness. The
acceleration parameter retains its physical interpretation; a boundary
transform is not silently used as measured vehicle speed. Informative
development evidence and outcome-blind numerical acceptance settings remain
requirements of a separately approved execution proposal.

## Commands and checks

Read-only inspection used `rg --files --no-ignore`, `rg -n`, `cat`, `sed`,
`tail`, `command -v pdflatex` and `git status --short`. Read repository context,
handoff/current review authorities, existing feedback and selected model/
source records. Primary web `find`/`open` rechecked selected passages of
Carey and Leclercq, plus official SUMO road-capacity documentation. The
viewed-reference list records their exact support and access limits.

Fresh preimages and preservation hashes:
`/tmp/vsl_mp6_physical_before.json`.

Document synchronization:

```text
python3 /tmp/vsl_mp6_physical_sync.py
```

An initial patch creating that scratch script failed validation because a
patch line lacked its prefix; no write occurred. The corrected patch and
synchronization completed. No scientific change or failed criterion was
hidden by that correction.

Supporting exact algebra:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_mp6_physical_algebra.py
```

Fifteen symbolic identities and nine exact rational static checks pass.
They cover the boundary-rate/profile derivatives and area, saturated-tail
accounting, work-coefficient rank and ambiguity, preparation branch/product
relations and stationary headway correspondence. A static branch check was
made explicit in its two receiving inequalities before final verification.
These are analytical formula checks, not simulated trajectories or numerical
gradient/finite-difference experiments.

Verified the installed `/usr/bin/pdflatex`. Build:

```text
python3 /tmp/vsl_mp6_physical_build.py
```

The script invokes `pdflatex -interaction=nonstopmode -halt-on-error
-file-line-error` twice into `/tmp/vsl_mp6_physical_latex`, then copies the
four-page PDF and final log. Strict PDF parsing, extracted page text and
font resources are checked; raster visual inspection is not claimed.
The final log has no overflow, underfull, LaTeX or package warnings.
Installed SymPy and pypdf were used without dependency changes.

Final document/status/preservation verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_mp6_physical_checks.py
```

Final quantitative results and artifact hashes are recorded in the linked
validation JSON. A first status check expected a differently worded native-
evaluator limitation; the checker was corrected to recognize the written
statement and normalize line wrapping. No model text or scientific criterion
was changed to satisfy it.

**Final checks passed:** 15 Markdown documents, 563 local links and 30
heading targets; all 337 protected hashes match. Fifteen symbolic identities
and nine exact static checks pass. Strict PDF parsing confirms four pages,
161,809 bytes and 38 Type 1 font resource references, with a clean build log.
These checks do not establish physical admission or control usefulness.
No traffic acceptance test was weakened or described as
passed. No ODE/traffic run, numerical derivative, calibration, optimization,
SUMO execution, installation or detached process occurred.

## Status and next allowed action

Stop at MP6-Q1 after completing this planned review block. Applied MP6 is
explicitly unresolved; the exact model remains selected for qualification.
Next review the information/action and full-objective gradient protocol,
then update the accepted model → S-P → S-L contract. Their final consistency
gate must distinguish a specified future admission process from passed
physical evidence. Step 3 remains open; Step 4 and implementation are unopened.

[Plain findings and checkpoint](vsl_mp6_physical_findings_and_checkpoint.md)

[Joint admission contract](../../synthesis/research_readiness/vsl_mp6_joint_physical_admission_contract.md)

[Mathematical note](../../synthesis/research_readiness/vsl_mp6_physical_identifiability.pdf)

[Viewed references](../../extraction/research_readiness/vsl_mp6_physical_source_audit.md)

[Machine-readable verification](vsl_mp6_physical_validation.json)
