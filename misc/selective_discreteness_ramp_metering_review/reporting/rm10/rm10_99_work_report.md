# RM10 work report

Date: 2026-10-05. **Authorized A-only source/analytic review completed to scoped
negative task admission; user acceptance pending.** No C review or task opening.

Subsequent status: [user acceptance closes RM10](rm10_99_user_closure.md).
The execution report below retains its creation-time checkpoint. Current work
is the separate [post-A planning check](../../rm11_00_post_a_direction_check_proposal.md).

## Files changed

All changes are within `misc/selective_discreteness_ramp_metering_review/`.

- New `reporting/rm9_99_scoped_closure.md`: UG5.A predecessor closure.
- New `rm10_00_recovery_acceleration_review_plan.md`: approved scope, ownership,
  execution order and final disposition.
- New `search/rm10_query_log.csv` and `screening/rm10_records.csv`: sixteen
  queries and sixteen version/access-qualified source records.
- New `extraction/rm10/primary_source_audit.md`: selected methods, provenance,
  source/task transfer and access limits.
- New `synthesis/rm10/information_and_action_audit.md`: strongest aggregate rivals,
  residual local-state family, complete history/action audit and conclusion.
- New `synthesis/rm10/rm10_information_tst_and_gradient_audit.tex` and `.pdf`:
  four-page main mathematics retained together.
- New `reporting/rm10/rm10_70_findings_and_conclusion.md`, `current_handoff.md`
  and this work report: complete result and current checkpoint.
- New `discussion/rm10/review_dialogue.md`: interpreted approval, decisions,
  methodological boundaries and artifact build.
- Updated `README.md`, `rm9_00_compact_local_merge_formulation_review.md`,
  `reporting/rm9_current_handoff.md`,
  `synthesis/rm9/rm9_formulation_contract_inventory.md` and
  `discussion/rm9_review_dialogue.md`: synchronize closure/successor status;
  preserve dated historical evidence and PDFs.

No production source/test/config, feedback inbox, project roadmap/context or
existing result was changed. Root `AGENTS.md` and `PLANS.md` had pre-existing
modifications; they were inspected and left intact. No binary source papers
were redistributed and no agent delegation occurred.

## Assumptions and claims

Review envelope: single ramp, bounded common rate schedules, default two mainline
lanes, public shared forcing/parameters, exact aggregate mass/flow/speed/ramp
history, finite storage and all-stream TST through common clearance. Actual
non-equilibrium speed support requires declaration; no new sensor is adopted.
No private random realizations, weakened history, favorable symmetry or task C
geometry is used as a rescue assumption. Compatibility with project progress is
not an admission filter.

The complete-state and observed homogeneous-state deductions are conditional
mathematical statements. Source capacity approximation is not exact closure.
The residual distribution/leader finding is insufficient evidence for positive
task admission, not universal impossibility. Formula identities are review
derivations, not validated simulator gradients or empirical control benefits.

## Commands and evidence work

Read-only `pwd`, `rg --files`, `rg -n`, `cat`, `head` and `tail` inspected repository
context, handover, current review contracts, feedback headings and source records.
`git status --short` confirmed the pre-existing tracked modifications. Sixteen
web queries are recorded verbatim in `search/rm10_query_log.csv`; primary
open/find operations inspected the selected locations in the source audit.
Direct-access failures are retained as access limitations, not scientific failures.

`apply_patch` wrote the methodology records. A standard-library `python3` script
created CSVs with the `csv` writer and copied the completed PDF beside its TeX.
CSV/link checks also used standard-library Python. No installed environment was
modified. LaTeX toolchain probes used `command -v latexmk pdflatex`.

Exact PDF build:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm10_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm10/rm10_information_tst_and_gradient_audit.tex
```

Validation used `/home/zpz/miniconda3/envs/differential_sim/bin/python`:
Python 3.11.9, installed pypdf for page/text inspection and SymPy 1.14.0 for
symbolic algebra. Initial layout overflows were corrected; final build succeeds
with no overfull boxes or undefined commands. Font-cache generation used TeX's
normal `/tmp` fallback; no install or behavior-changing workaround was needed.

## Verification results

| Check | Result |
|---|---|
| LaTeX compilation | Passed; four pages, `.tex` retained beside PDF |
| PDF extraction/section coverage | Passed; all four pages have substantial extractable text and intended section starts |
| Final log layout checks | No overfull boxes or undefined commands |
| Symbolic demand-law endpoints | Public modified-demand branch gives jam demand at jam density and capacity at critical density |
| Symbolic complete-population TST coefficients | Direct expansion/differentiation agrees with the derived exit coefficient for horizons S=2–14; algebra only, no traffic experiment |
| CSV shape/ID integrity | Passed; sixteen rows each; six query columns/seven source columns; unique IDs |
| Local navigation/artifact links | Passed after all deliverables were written |
| Scope/claim consistency | Conditional sufficiency distinguished from unsupported rich-family admission; no new law or C work |

Raster PDF inspection was unavailable: `pdftoppm`, `mutool` and `gs` are absent.
Compilation, log and extracted-text checks were performed; no visual-rendering
claim is made. No traffic model test, numerical finite difference, controller
optimization, SUMO or richer-reference experiment was performed or required to
complete this methodology-review conclusion.

## Risks, status and next allowed action

The source frontier is bounded; several leads remain abstract/indexed or prior
extraction only. No universal hidden-state impossibility is claimed. The physical
family can still motivate another task, but a genuine history/action certificate
would be required to reopen a positive admission claim. A new non-equilibrium
task also needs explicit sensing, initialization, finite-storage semantics and
event-sensitive derivatives before any experiment could validate it.

RM9 is closed with its scoped result. RM10 G1/G2/E1–E4 are complete; G3 yields
negative admission; G4 supplies the conditional general path. G5 is user review
and acceptance of this completed result. No further A work is pending under the
current bounded plan. C remains an alternative and was not involved. The next
allowed action is discussion/acceptance of this result and a subsequent explicit
direction, without automatically launching C or project development.
