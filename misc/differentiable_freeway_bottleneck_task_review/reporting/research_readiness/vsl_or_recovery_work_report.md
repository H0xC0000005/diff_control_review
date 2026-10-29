# Selected renewal: bounded construction and analytical qualification

Date: 2026-10-15. Method-first VSL review; no simulator work.

## Outcome, authority and stopping boundary

The user explicitly directs proceeding with renewal after the sufficient-
state discussion. Recorded O-R as selected for qualification and closed
RE-O1. Used the concrete recent-mass formula previously presented, retaining
R-E and S-E-P. No stateless latest-batch map, numerical-step reset, extra
traffic state or new spatial model was substituted.

Completed the bounded J3 candidate-and-analytical-check pass. Derived the
physical injection/aging/retirement update, a functional perturbation bound
for the moving mass cutoff, and local causal coupling on valid node-regime
charts. Bounded admission, finite renewal mass and positive physical
acceleration give a derived uniform positive budget; finite-clearance and
complete TST/storage interfaces follow for admissible solutions.

Constructed a complete regular H1 cohort with initial E waiting, later A
delay under ordinary underload, genuinely nonzero old-profile retirement,
and finite clearance. Auxiliary zero recovery, zero mismatch and constant
arrivals are finite-prefix proof devices. Strict-event continuity removes
them: the final family has positive recovery/mismatch and finite geometry.
It covers a local advice neighborhood, not the entire original action range.
The construction may require long geometry and very slow recovery; its
existence does not supply applied MP6 or a chosen primary parameter set.

Stop at **OR-Q1**, the completed bounded recovery-result checkpoint. No new
model-option gate arose. The complete joined review and Step 3 are unfinished.
After review, the next allowed action is J4's joined original-action-range,
physical-provenance, applied MP6 and information/sensitivity/native qualification.
It is not begun here. Step 4, implementation and experiments stay unopened.

## Files changed

Eight new artifacts in the review package:

- `reporting/research_readiness/vsl_or_selection_and_scope.md`.
- `reporting/research_readiness/vsl_or_recovery_qualification_and_checkpoint.md`.
- `extraction/research_readiness/vsl_or_qualification_source_and_adaptation_audit.md`.
- `synthesis/research_readiness/vsl_or_recovery_qualification.tex` and `.pdf`.
- `reporting/research_readiness/vsl_or_recovery_build.log`.
- `reporting/research_readiness/vsl_or_recovery_work_report.md`.
- `reporting/research_readiness/vsl_or_recovery_validation.json`.

Twenty-two existing review records synchronized: README, successor opening,
methods outline, first-verification draft, living candidates, C-P plan,
progress, Step 3 plan, M2 scope, dialogue, earlier M2 admission, feedback-7,
A1-C scope/report, fixed-queue and S-E admission reports, earlier S-E-P
scope/recovery report, R-E scope/overlap report, MP problem inventory and
feedback-6 joined plan. Current notices point to O-R/OR-Q1. Living questions,
scope/progress and checkpoint status are revised; historical bodies retain
delivery-time meaning. Stable earlier question headings are retained.

All 110 preexisting root/feedback/mathematical/build/validation files in the
snapshot are protected. Existing root AGENTS.md/PLANS.md/memo.txt edits
predate this task. Feedback inboxes, root methodology/roadmap and production
files were not edited. Review files remain Git-ignored and saved durably
at their explicit paths.

## Assumptions and unresolved risks

Retain H1 preparation/priority/cutoff, T1 physical travel/storage, known
empty initial state/history, ordinary-underload primary domain, continuous
mass, independent unqueued B, singleton output, local choke completion
and model→SUMO S-P→SUMO S-L. Early-merged mass is ordinary terminal A.
Recent speed/age history is predicted internal state, not an added observer.

The proof is conditional on the declared work/trace/profile family and
its sufficient monotonicity domain. Equal-work congested cooperation,
flow-derived insertion speed, renewal mass, profile aging and retirement,
immediate-work/recovery separation and ideal advice response remain
physical adaptations. Retiring an older strong restriction can recover
service too quickly. No empirical parameter values are frozen by this pass.

The moving-cutoff estimate establishes local causal construction in valid
regimes. It does not prove every endogenous hybrid event sequence. The
complete-cohort argument closes one constructed regular sequence, with
local parameter/action persistence; it is not a whole-domain invariant-node
theorem. No numerical scheme, event epsilon, smoothing or artificial floor
is introduced. The uniform lower bound is a mathematical consequence of
the selected finite-mass recovery law.

The constructed positive A waiting area and nonzero retirement resolve a
mathematical possibility gap. They do not prove a realistic regime, action
advantage, interior optimum, information minimum or useful gradient. The
old constant-A protected limit still holds. Strong aggregate/history/scalar,
stationary-equivalent, fixed M1, O-S and search rivals remain; negative or
common-fastest outcomes are allowed. Applied MP6 retains its original
source-supported joint-domain meaning and remains unadmitted.

## Commands, source scope and environment

Read instructions, project context/roadmap, active feedback and prior laws/
plans/inventory using file reads, `rg`, `sed`, `tail` and `git status --short`.
No separate approved simulator milestone governs this method-only review.
No current VSL refinement tab overrides the interactive instruction; the
VSL inbox remains unchanged. No sub-agent or skill was used.

Primary web open rechecked Leclercq and Jin at their previously logged
scope; the new source audit distinguishes reused motivation from our own
proofs. No additional paper is claimed as newly read in full. No source
data/figure analysis or native algorithm execution.

Verified existing `/usr/bin/pdflatex`. Used installed `sympy` and `pypdf`
through `/home/zpz/miniconda3/envs/differential_sim/bin/python`. Installed
nothing. Document synchronization and build commands:

```text
python3 /tmp/vsl_or_recovery_sync.py
python3 /tmp/vsl_or_recovery_build.py
```

The build script runs `pdflatex -interaction=nonstopmode -halt-on-error`
twice into `/tmp/vsl_or_recovery_latex`, then copies the PDF/final log.
One long rational equation initially overflowed; splitting its layout
removed the overflow without changing its mathematics. The final PDF has
eight pages. Raster visual inspection is not claimed.

Verification command:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_or_recovery_checks.py
```

Preservation snapshots are `/tmp/vsl_or_qualification_preimages.json` and
`/tmp/vsl_or_qualification_before.json`. Durable hashes, results and package
versions are in the validation JSON. Scratch scripts perform document work,
exact inequalities and symbolic calculus; none runs traffic or an ODE solver.

## Checks and meaning

Checks cover current selection/checkpoint status, question ownership and
stable anchors, changed-document links, strict PDF parsing/text/fonts/build
warnings, symbolic profile/work/update and auxiliary-event identities,
exact positivity of a kernel budget-bound example, rational H1/auxiliary
inequality feasibility and all 110 protected hashes. Mathematical arguments
are retained for human review; these checks do not mechanically certify
the quantified causal/event proofs or their physical validity.

All passed: 26 Markdown records, 554 local links, 30 heading targets,
11 exact static checks, 12 symbolic identities and strict parsing of the
eight-page PDF. All PDF fonts are Type 1; no overflow or rerun warnings
remain. Package versions and hashes are retained in the validation JSON.

No simulator unit suite, traffic time stepping, ODE trajectory, experiment,
calibration, optimization, SUMO execution, numerical gradient, dependency
change or detached process was run. Exact rational values only verify
nonempty inequalities; they are not selected traffic parameters.

[Verification results and hashes](vsl_or_recovery_validation.json)

[Conceptual findings and completed-step checkpoint](vsl_or_recovery_qualification_and_checkpoint.md)
