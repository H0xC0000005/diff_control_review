# VSL-B1 work record

Date: 2026-10-13. Task: the user-authorized bounded Option B qualification
against accepted MP1–MP6. Status: **Review delivered at VSL-B1-G1; proposed
local receiving/timing amendment awaits user disposition.** This is review
work, not a production milestone or an implementation pass.

## Result and boundary

Proposed a continuous mandatory-transfer model in which available demand,
adjacent receiving and competing same-lane traffic determine realized merging.
Carey is the provisional principal reduction reference; Subraveti remains a
separate lane-drop/density check. Neither whole source model nor a hybrid
equation set is adopted. The report is organized around the traffic model,
its interfaces with preparation/exit service and complete time, and MP6's
joint operating-domain burden.

Original conditional examples show that combined continuing mass can omit
adjacent receiving, initial symmetry can fail under selective transfer, and
equal final work/clearance can conceal different mean completion times.
These qualify interface risks; they do not establish new-model action
differences, a native full-history collision or useful external gradients.
The recommendation is B1-L: permit the smallest local receiving and within-
cohort chronology amendment for a bounded contract proposal. B1-R retains a
restricted sequential qualification route. Exact states/laws, common-speed
response and MP6's joint applied domain remain unapproved.

[Decision-facing model and gate report](vsl_b1_lane_change_model_and_gate.md)

## Files created and synchronized

Created six files in this review package:

- `reporting/research_readiness/vsl_b1_lane_change_model_and_gate.md`: plain
  traffic narrative, model/interface qualification, MP6 and expanded gate.
- `extraction/research_readiness/vsl_b1_source_and_interface_audit.md`: source
  locations, original/adapted distinctions, ownership and remaining contracts.
- `synthesis/research_readiness/vsl_b1_interface_examples.tex` and `.pdf`:
  editable mathematical diagnostics and their three-page rendering.
- `reporting/research_readiness/vsl_b1_work_report.md`: this work record.
- `reporting/research_readiness/vsl_b1_validation.json`: document/check evidence.

Updated eight existing files: package `README.md`,
`vsl_successor_00_opening_plan.md`, the short methods outline, living model
candidates, MP inventory, R1 findings/gate continuation notices, baseline/evidence
screen, and append-only opening dialogue. Their current checkpoint is B1's
interface choice. Accepted MP definitions and S13 results retain their meaning;
the outline's inherited equations remain an explicitly conditional reference.

Feedback files, closed S13/source records, prior PDFs/validation records,
urban/ramp closures, production code, root methodology/roadmap and existing
user edits are preserved. `misc/` was already ignored; no Git rule, staging
or forced tracking was changed.

## Assumptions and scientific risks

Review assumptions preserve the elementary companion role, fixed geometry,
finite cohort, one common bounded constant advice action, continuous mass,
complete-time objective and separate forward/derivative/usefulness claims.
No positive preparation benefit, information gap or optimizer advantage was
required. Proposed model restrictions and interface extensions remain proposals.
Within-cohort arrival/departure chronology is distinct from new streaming demand.

Unresolved risks are source-to-reduction validity; adjacent-state sufficiency;
compatible early/late receiving and spillback; lane-end holding/clearance;
common advice versus realized progress over the action range; source branch,
zero-state and combined-budget conventions; observable initial information;
native reachable history matching; and independently useful sensitivities.
If a small reduction fails, the elementary task role must be reconsidered,
rather than expanding automatically into a full spatial source model.

## Reads, commands and access

Read the finalized handoff first and followed its list through the latest
feedback-27 entry, ramp closure, accepted transition, S13 closure/sufficiency/
source audit and the closed urban task. Read repository `AGENTS.md`, relevant
`PROJECT_CONTEXT.md`/`PLANS.md`, the latest VSL feedback inbox and active review
records. No production milestone is opened; current Python APIs were not used
to constrain task design. A nested `AGENTS.md` search found no additional file
in the review areas.

Used `rg`, `sed`, `tail`, `cat`, `git status --short`, `apply_patch`, and
standard-library Python for document preservation and checking. Primary web
reads covered Carey, Wei, Roncoli and Zhang. Used the existing
`/home/zpz/miniconda3/envs/differential_sim/bin/python` with `pypdf` 6.15.0 to
extract selected FB0030 pages and inspect the new PDF. Python use was document
inspection and exact arithmetic, not traffic simulation.

Carey screenshots of PDF pages 11–12 returned web Internal Error; primary text
was accessible. No rendered source-equation or whole-algorithm certification
is claimed. Two incidental searches referenced a nonexistent `library/`
path or encountered unrelated private `/tmp` directories; neither affected
source access or required document checks. No methodological conclusion was
drawn from those search errors. No dependency was installed and no new full
text was archived.

Verified `/usr/bin/pdflatex`, pdfTeX 1.40.25 (TeX Live 2023/Debian). Built with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_b1_20261013_latex /home/zpz/repos/diff_minimal_meso/misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_b1_interface_examples.tex
```

Ran the build once, corrected two overfull text lines, and ran it again.
Final log has no overfull/underfull boxes or LaTeX warnings. Final PDF is three
pages, 123343 bytes, with text extracted on every page. Build auxiliaries/log
remain under `/tmp/vsl_b1_20261013_latex`; source and final PDF are in the package.
No raster/visual-render inspection is claimed.

Three synchronization patches initially failed exact-context checks and made
no changes. They were corrected using the inspected current text; no scientific
content or acceptance criterion was changed to accommodate a patch failure.

## Checks and next allowed action

**Document validation passed.** Of 751 pre-review files, 743 are unchanged
and eight are the allowed synchronization changes. Six review files were
created. All 150 checked local links resolve. Checks preserve accepted MP
definitions/ownership/closure options, R1 scientific findings/admission, A/C
candidate bodies and append-only dialogue; confirm current gate status and
expanded B1-R/B1-L pros/cons/dependencies; and verify the exact departure-example
arithmetic and three-page PDF/log.

The initial inventory comparison used a backup predating the previous user
acceptance notice. Corrected the reference to the actual pre-B1 content,
verified against its whole-file pre-review SHA-256. No accepted question was
edited and no preservation criterion weakened. Validation command:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_b1_20261013_validate.py
```

Preservation snapshot: `/tmp/vsl_b1_20261013_preservation_snapshot.json`.
Detailed temporary results: `/tmp/vsl_b1_20261013_checks.json`; final evidence
is retained in the package below.

[Document and arithmetic validation](vsl_b1_validation.json)

Scientific traffic, AD/FD and optimizer tests are not applicable to this
methodology review and were not run. No simulator code, environment,
dependencies or experiment results changed. Existing Git status remains
user modifications to `AGENTS.md`, `PLANS.md` and `memo.txt` only.

The authorized review step is complete. User disposition of VSL-B1-G1 is the
next allowed action because the proposed receiving/state/timing interface
changes scientific meaning. No further contract proposal or implementation
starts automatically.
