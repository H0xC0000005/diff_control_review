# RM9 allocator-default continuation work report

Date: 2026-10-01. Status: **RM9-UG1.A closed as Default; RM9 open at RM9-UG2.**

## Result and authorized scope

Recorded the user's allocation approval without a redundant confirmation,
transcribed the positive-priority two-input node, proved offer/receiving bounds
and work conservation, and derived ordinary local sensitivities away from ties.
Explained meter release, ramp propagation, local offer, physical allocation,
subsequent queues and complete departure accounting with hand calculations.

Continued the lane-law review: diagnosed isolated combined-incentive coefficient
and zero-receiving branch issues, checked shared-flow/actuator boundaries, and
made the next restricted conservative adaptation concrete before presenting
RM9-UG2. The alternative retains the fuller cooperation family for source-level
resolution. Neither local-physics alternative is adopted. No full-history/action
or verified/useful whole-chain gradient certificate has been established.

## Assumptions and risks

- The user said Default: allocation A is Default, not Fixed. Priorities remain
  structural and common across comparisons; illustrative 2:1 is not calibration.
- One-receiver work conservation is not arbitrary multilane donor/FIFO validity.
  Spare supply requires physical eligibility; ramp permission is not downstream
  entry when travel/storage intervenes.
- Unchanged complete final departures imply unchanged all-stream system time.
  Local merge throughput is not necessarily the accounting-boundary exit.
- Source range/branch diagnostics are isolated algebraic checks, not a proof
  that every complete published trajectory violates conservation.
- Candidate A's bounded discretionary within-cell transfer and sequential
  recomputation are an explicit reviewer adaptation. Its conservation proof is
  conditional on finite lane storage, step bounds, unique paired transfers and
  conservative ramp/boundary balances. Residual original donor/receiver budgets
  are carried into Stage 2 to prevent double capacity allocation. It is not field-validated physics and
  may produce no hidden-state or useful-metering distinction.
- The observer retains all admitted density/flow/speed/count and ramp history;
  no symmetry, mixing, extra actuator, capacity-drop penalty or stochastic
  derivative estimator was adopted to manufacture a positive result.
- The 2015 Part I lead is metadata only; missing full methods do not imply
  unavailable physics. The inspected 2014 optimizer is not its full substitute.

## Files created

- `discussion/rm9_allocator_a_approval_and_continuation.md`
- `reporting/rm9_30_allocator_contract_and_control_chain.md`
- `extraction/rm9_joint_flow_readiness_audit.md`
- `synthesis/rm9/rm9_priority_allocator_and_control_effects.tex`
- `synthesis/rm9/rm9_priority_allocator_and_control_effects.pdf`
- `reporting/rm9_95_allocator_continuation_work_report.md`

## Existing files updated

- `rm9_00_compact_local_merge_formulation_review.md`
- `reporting/rm9_current_handoff.md`
- `reporting/rm9_20_findings_and_gate.md` (gate disposition/history retained)
- `synthesis/rm9/rm9_formulation_contract_inventory.md`
- `discussion/rm9_review_dialogue.md`
- `extraction/rm9_source_and_claim_audit.md` (resolved family, unchanged limits)
- `search/rm9_query_log.csv`
- `screening/rm9_records.csv`
- `README.md`
- `synthesis/rm7_post_selection_design_inventory.md` (active status only)
- `reporting/rm7_current_handoff.md` (superseding pointer)
- `reporting/rm8_current_handoff.md` (superseding pointer)
- `reporting/rm8_20_findings_and_gate.md` (superseding pointer)
- `discussion/rm8_review_dialogue.md` (superseding pointer)
- `../differentiable_freeway_bottleneck_task_review/reporting/s13/s13_99_m2_certificate_sprint_closure.md` (navigation only)
- `../differentiable_freeway_bottleneck_task_review/synthesis/s10/s10_post_closure_next_step_plan.md` (current navigation/authorization only)

Root AGENTS.md and PLANS.md had pre-existing user changes and were not edited.
No production source, tests, environment, dependency, project context, feedback
inbox, old PDF/full-text archive or approved implementation plan changed. Review
artifacts are in the existing ignored misc tree; git status alone does not list
them. The prior RM9.90 report describes the first pass, not current UG1 status.

## Sources and commands

Primary PDFs were inspected/rechecked for RM0018, FB0030 and FB0034; existing
RM0002 and RM8-P01 supplied conditional background only. Added a separately
marked metadata lead RM9-L01; preserved existing source IDs/archives. Seven new
exact executed queries (Q05–Q11) are appended. Publisher/repository access did
not yield 2015 Part I full methods; no abstract-based equation admission.

Read-only inspection used `rg`, `cat`, `head`, `sed`, `command -v`,
`git status --short`, primary-source web search/open and local pypdf extraction.
Document writes/status synchronization used standard-library temporary scripts:

```
python /tmp/rm9_continue.py
python /tmp/rm9_sync.py
python /tmp/rm9_report.py
python /tmp/rm9_budget_fix.py
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm9_allocator_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm9/rm9_priority_allocator_and_control_effects.tex
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/rm9_continuation_validate.py
```

Build uses installed pdfTeX 1.40.25 / TeX Live 2023 and latexmk 4.83, without
installation. PDF copied beside editable TeX; auxiliaries stay in /tmp. Validation
uses Python 3.11.9/pypdf 6.15.0. No numerical traffic, autograd/finite-difference,
optimization or SUMO test run; hand arithmetic and symbolic reasoning only.

## Verification and current gate

Document verification covers links, CSV uniqueness/evidence labels, PDF pages/
text/checksum, LaTeX errors/overflow/undefined references and status coherence.
No raster visual inspection was performed. Mathematical checks are direct proof
review, not an independent empirical gradient-usefulness result.

UG1 is closed with A approved as Default. The continuation reaches UG2 because
local transfer/coupling changes physics. The next allowed action is discussion
and adoption of that concrete candidate or further source resolution, followed
by the same bounded review; no successor, implementation or experiment begins.
G1/G2 remain incomplete, G3/G4 unestablished. RM8 and VSL S13 closures, VSL
colleague-discussion deferral and multi-ramp deferral remain intact.

## Final proposal consistency correction

Before delivery, the global/local budget audit found that recomputing only
post-lateral state limits would allow the two proposed stages to reuse one
capacity budget. Revised the unapproved candidate to retain residual original
donor and receiver budgets as well as post-transfer state limits. The PDF now
proves the shared bounds explicitly. This corrects the proposal before adoption;
it does not change the user's Default allocator or a closed traffic law.

## Final validation result

Passed with zero errors: 18 changed Markdown documents, 108 local links,
7 unique source/lead records, 11 unique query records, seven scoped new claims,
and a 5-page PDF. Final LaTeX log has no overflow, underfull boxes, undefined
references or compilation errors. Scope: six new artifacts and sixteen existing
documentation/CSV updates. No production or scientific experiment tests ran.

PDF SHA-256: `5c572965ff85079191741437f36e96baf5ec88fc1a0b1e91fd02db8dc77cf613`.
