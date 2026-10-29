# Revised A1-C execution: work, checks and stopping point

Date: 2026-10-15. Method-first source/analytical review, not simulator work.

## Outcome and authority

Recorded the user's approval of revised A1-C after the unified-model
clarification, closing M2-A1 at direction scope. Resumed the approved
admission/discharge → shared recovery → joined qualification chain.

Formed a conditional one-budget work-allocation module with a proposed
fair-work convention; derived unique fixed-input flows and matched,
mismatched, intermediate and residual-service limits. Constructed an exact
queue-birth ambiguity diagnostic for one instantaneous speed completion.
Derived conditional storage/accounting and bounded-work/finite-loss
clearance criteria. These results do not supply a complete state/cost/
recovery law or an applied task certificate.

Stopped at **A1-C-S1, Type 2 G3**: equilibrium speeds with explicit causal
regime transitions (S-E, provisionally first) versus finite-rate aggregate
speed dynamics (S-V). Neither is selected. The diagnostic does not prove
that all first-order point models fail. The full approved chain and Step 3
remain in progress, not complete. No implementation milestone is opened.

[Traffic findings, model shape and direct option comparison](vsl_a1c_service_work_findings_and_gate.md)

## Files changed

Eight new review artifacts:

- `reporting/research_readiness/vsl_a1c_selection_and_scope.md`: user selection and precise approval boundary.
- `reporting/research_readiness/vsl_a1c_service_work_findings_and_gate.md`: plain findings, interpretation, limits and expanded state-closure gate.
- `extraction/research_readiness/vsl_a1c_source_and_adaptation_audit.md`: viewed-paper reference list, selected passages and screened alternatives.
- `synthesis/research_readiness/vsl_a1c_service_work_and_speed_closure.tex` and `.pdf`: five-page analytical audit.
- `reporting/research_readiness/vsl_a1c_service_work_build.log`: final LaTeX build log.
- `reporting/research_readiness/vsl_a1c_service_work_work_report.md`: this work record.
- `reporting/research_readiness/vsl_a1c_service_work_validation.json`: document/PDF/static-algebra checks, hashes and status.

Twelve existing review records updated: package `README.md`, successor
opening plan, methods outline, first-verification protocol, living core-model
candidates, C-P plan, review progress, Step 3 plan, M2 selection/scope,
opening dialogue and the latest-status notices of the earlier admission
gate and feedback-7 response. They distinguish the closed direction choice
from the new open state choice and preserve earlier delivery history.

The feedback inbox is unchanged. Earlier mathematical sources/PDFs, root
scientific context and preexisting user edits are preserved by hashes.
The review package is Git-ignored; its artifacts remain at the explicit
on-disk paths. Root `git status --short` shows the existing `AGENTS.md`,
`PLANS.md` and `memo.txt` edits, which this task did not change.

## Assumptions and limits

Keep conditional E slowing, continuous mass, finite terminal, H1 preparation/
early priority/cutoff, known initial state, primary ordinary-underload
domain, local choke-line completion and S-P→S-L. Retain strict/fixed-share,
aggregate/history, ending-statistic, P-E/M1 and equal-information search
references. No interior optimum or full-lane-state advantage is required.

Equal work is an explicit candidate fairness hypothesis. Unit admission
cost is not physical mass, and available work is not automatically a
composition-independent vehicle-flow ceiling. The actual state/cost/account
maps and attribution of current versus retained burden remain unqualified.

The exact normalized queue diagnostic tests a local, constant-offer speed
completion with recovery budget held fixed. It is not a complete P-H
history model, an H1-generated MP6 witness, a new primary scenario or a
general nonuniqueness result. Its role is to expose the omitted causal
state/transition rule. No epsilon queue, smoothing or timestep branch
selection is adopted to remove it.

## Commands, environment and sources

Used `rg`, `sed`, Python file reads and `git status --short` for instructions,
context, handoff, feedback/current authorities and predecessor equations.
Read primary source selections through web search/open/find; the source
audit records direct-access failures and abstract-only limits. No source
figure/data extraction or new SUMO API/runtime audit occurred.

Existing executables/packages were used: `/usr/bin/pdflatex` and
`/home/zpz/miniconda3/envs/differential_sim/bin/python` with existing `pypdf`
and `sympy`. No dependencies were installed. PDF raster tools were absent;
no raster visual inspection is claimed.

Build command:

```text
python3 /tmp/vsl_a1c_build.py
```

The script ran `pdflatex -interaction=nonstopmode -halt-on-error` twice with
`-output-directory=/tmp/vsl_a1c_latex` on the retained `.tex`, then copied
the PDF and final log to the artifact paths. The first build exposed two
text overflows; shortening prose/link labels corrected them. Final build
checks retain the mathematical content and require no overflow warnings.

Documentation synchronization:

```text
python3 /tmp/vsl_a1c_sync.py
```

Document/PDF/exact-algebra verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_a1c_checks.py
```

Scratch preservation records: `/tmp/vsl_a1c_before.json` and
`/tmp/vsl_a1c_preimages.json`. Durable hashes/results are in the validation
JSON; the scratch editing scripts are not needed to review the artifacts.

## Checks and scientific meaning

Checks cover local Markdown links/heading targets, direction/gate/stage
status, strict PDF parsing and page text, font types and final build warnings,
exact service-work allocations and symbolic share/polynomial/continuity/
clearance identities, plus unchanged hashes for 31 preexisting protected
root/feedback/mathematical files.

**Passed:** 16 Markdown files, 421 local links, 26 heading targets, ten
exact static allocation cases and seven symbolic identities. The five-page
PDF parses strictly, contains extractable text on every page and has no
final overflow/rerun warnings. All 31 protected-file hashes match. Package
versions, detailed results and hashes are retained in the linked JSON.

Static rational cases and symbolic expressions are analytical checks.
No traffic time stepping, simulator unit suite, rollout, calibration,
optimization, AD/finite-difference traffic run, installation or SUMO
execution occurred. Artifact and algebra checks do not establish empirical
validity, complete-law uniqueness or useful gradients.

[Verification results and hashes](vsl_a1c_service_work_validation.json)

## Remaining risk and next allowed action

Resolve A1-C-S1's physical state/evolution interpretation before qualifying
its exact equations. Then close admission/opportunity and state-to-work,
the single recovery update and overlap, full-law uniqueness/clearance and
the joint MP6/information/action/sensitivity/native evidence. Unknown
initial kinematics, spatial expansion or changed objective remains an
explicit return condition, not a local adapter.

The original three-part pass and Step 3 remain unfinished. Step 4,
implementation, installations, traffic experiments and the closed ramp
line remain unopened.
