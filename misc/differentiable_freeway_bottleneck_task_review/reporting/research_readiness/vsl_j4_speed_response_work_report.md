# J4 speed-response qualification: work and verification

Date: 2026-10-16. **Executed review opening; stopped at J4-W1, a new
Type 2 G3 decision. Step 3 remains open.**

## Result and authorization

The user reviewed OR-Q1 and authorized the remaining qualification. Carry
that recovery evidence forward with its conditional limits. The opening
audited the work law's advice response before full-domain/event and dependent
gradient/reference qualification. It found a direct advice effect under
inactive queued speed bounds and formed W-A/W-F as concrete alternatives.
W-F is provisionally recommended; no work expression is replaced.

The user's new speed-matching intuition was treated as a conditional
mechanism, not a universal empirical sign or a required control result.
Static tests hold current node inputs fixed; they do not claim a reachable
same-cohort policy comparison. Posted advice is assumed to set the existing
free-motion parameter, while any additional direct desired-speed influence
must be declared. Selecting that interpretation is precisely the open choice.

## Files changed

New artifacts:

- `reporting/research_readiness/vsl_j4_speed_response_findings_and_gate.md`
- `extraction/research_readiness/vsl_j4_speed_response_source_audit.md`
- `synthesis/research_readiness/vsl_j4_speed_response_audit.tex`
- `synthesis/research_readiness/vsl_j4_speed_response_audit.pdf`
- `reporting/research_readiness/vsl_j4_speed_response_build.log`
- `reporting/research_readiness/vsl_j4_speed_response_work_report.md`
- `reporting/research_readiness/vsl_j4_speed_response_validation.json`

Eleven existing Markdown records synchronized: package README, successor
opening plan, methods outline, living candidate/question inventory, review
progress, Step 3 review plan, first-verification protocol draft, C-P review
plan, O-R selection record, O-R checkpoint report and successor dialogue.
Earlier delivery-time claims, mathematical artifacts and question anchors
remain. The living inventory supplies W-A/W-F, explicit Pros/Cons,
classification, ownership, dependencies and the smallest reopen conditions.

The review package remains Git-ignored. Root user changes in `AGENTS.md`,
`PLANS.md` and `memo.txt` were already present and remain untouched. User
feedback, closed ramp/urban records, S13 and prior mathematics are protected.

## Commands and checks

Repository inspection used `pwd`, `rg --files --no-ignore`, `rg -n`,
`cat`, `sed`, `tail`, `nl -ba` and `git status --short`. No nested
`AGENTS.md` was found under the review, temporary or documentation folders.
Read the finalized handoff and its authorities, current review plans,
feedback entries, candidate formulas and existing source/baseline audits.
Primary web search/open/find rechecked the three references listed in the
source audit. Search-only leads are separated from substantive reading.

Exact symbolic/static verification, using installed SymPy:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_j4_speed_algebra.py
```

Seven symbolic identities and eight exact static checks passed. They cover
the two response derivatives, the queued direct-advice channel, candidate
response signs at the expression level, anchor equality, the exact free-A
root/work excess and sufficient-domain inequalities. No sampled traffic
trajectory, ODE solve or numerical gradient was computed. Symbolic checks
do not mechanically certify physical validity or full hybrid existence.

The local LaTeX command was verified at `/usr/bin/pdflatex`. Build:

```text
python3 /tmp/vsl_j4_speed_build.py
```

The script runs `pdflatex -interaction=nonstopmode -halt-on-error
-file-line-error` twice, using `/tmp/vsl_j4_speed_latex` for auxiliary files,
and copies the PDF/final log into the package. A slash-separated prose phrase
initially overflowed; ordinary prose reflow removed it without a mathematical
change. A bitmap default list bullet was replaced with the equivalent
vector math bullet after the font check identified it. The final five-page
PDF builds without overflow/underflow or rerun warnings and uses Type 1
fonts throughout. PDF parsing, text and font checks are recorded below. No raster
visual inspection is claimed; optional local raster renderers were absent.

Document synchronization used `python3 /tmp/vsl_j4_speed_sync.py`. The
preimage/protected-hash snapshot is `/tmp/vsl_j4_speed_before.json`.
Final verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_j4_speed_checks.py
```

The machine-readable record includes link/status/anchor checks, all 234
protected hashes, PDF properties, package versions and artifact hashes.
These are documentary/algebra checks, not traffic-model unit tests or
experiment evidence.

**Final result: passed.** Fourteen Markdown records, 480 local links and
29 heading targets checked; all 234 protected hashes match. Seven symbolic
identities and eight exact static checks passed. The PDF has five pages,
152,280 bytes and 40 Type 1 font resource references. The document check
also caught a missing gate label in the source list; it was added. The
generated validation record's link was resolved after its first creation.
No failed scientific criterion was waived or weakened.

## Scientific limits and next allowed action

W-F's fixed scales are a concrete constitutive proposal, not source-derived
gap dynamics or calibrated crossing speeds. The chosen interpretation still
needs all-original-action event/domain qualification, credible joint physical
scales, no double charging of maneuver/recovery, applied MP6 and the dependent
information/action/gradient/SUMO contracts. No interior optimum, full-lane-state
necessity or positive gradient-transfer result is established.

Next allowed action: decide J4-W1, then resume J4 under that explicit rule.
No selected H1/T1, allocation, renewal, observation, action range or objective
was amended. Step 4, implementation, dependency installation, traffic/ODE
rollouts, calibration, optimization, numerical derivative runs and SUMO
execution remain unopened. No processes are left running.

[Conceptual finding and choice](vsl_j4_speed_response_findings_and_gate.md)

[Mathematical support](../../synthesis/research_readiness/vsl_j4_speed_response_audit.pdf)

[Viewed-paper reference list](../../extraction/research_readiness/vsl_j4_speed_response_source_audit.md)

[Verification record](vsl_j4_speed_response_validation.json)
