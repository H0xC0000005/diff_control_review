# Selected S-E-P: recovery continuation, checks and stopping point

Date: 2026-10-15. Method-first scientific review; no simulator work.

## Outcome and approval boundary

Recorded the user's S-E-P selection and rationale, closing S-E-A2 at
priority-direction scope. Continued the approved admission/discharge →
shared recovery → joined qualification chain. Exact cooperative fairness,
work/speed laws, profile overlap and parameters remain unapproved.

Preserved S-E-P as proposed: cooperation remains while A is queued,
including when E clears first. Interpreted the user's “until both are
queued” as build-up language, not a separately approved literal toggle.
An exact local clearance diagnostic shows that such a toggle has no
nonnegative absolutely continuous continuation; the selected proposal
serves E's current offer and gives spare work to A. No new latch, queue
floor, smoothing or implementation fallback was introduced.

Formed a speed-marked version of the earlier isolated recovery profile,
with finite-support, integrated-work and Lipschitz bounds. Specified R-E
(E-origin new loss, A follows) and R-AE (additional loss profiles from slow
A departures) in one shared account. Derived their local fixed-mode causal
construction, A-only-tail renewal identity, finite integrated service-loss
and conditional finite-clearance bounds. Neither is the old fixed-speed M1
reference or a source-native overlap theorem.

Derived a limiting case: with constant underloaded A offers and neutral
history, the selected priority and either trial source law can throttle E
before A queues. This does not decide changing H1 arrivals, require an
external slowing seed or amend the primary domain. A consequential primary
A-impact/MP6 case and whole hybrid existence/uniqueness remain unproved.

Stopped at **SEP-R1, Type 2 G3**, the physical recovery-source attribution.
Recommend R-E first as the minimal primary candidate; R-AE is a concrete
alternative with a stronger renewal assumption. Neither is selected.
S-E-P, S-E, M2/P-H, H1/T1 and local completion retain their meanings.
The full three-part pass and Step 3 are unfinished. Next allowed action:
user source-law decision, then dependent overlap/event/primary-MP6 review.

## Files changed

Eight new review artifacts:

- `reporting/research_readiness/vsl_sep_selection_and_scope.md`: selected priority, clearance interpretation and approval limits.
- `reporting/research_readiness/vsl_sep_recovery_findings_and_gate.md`: conceptual model comparison, direct results and expanded source-law gate.
- `extraction/research_readiness/vsl_sep_recovery_source_and_adaptation_audit.md`: viewed-paper references, access limits and adaptation boundary.
- `synthesis/research_readiness/vsl_sep_recovery_and_clearance_audit.tex` and `.pdf`: five-page analytical explanation and proofs.
- `reporting/research_readiness/vsl_sep_recovery_build.log`: final build log.
- `reporting/research_readiness/vsl_sep_recovery_work_report.md`: this record.
- `reporting/research_readiness/vsl_sep_recovery_validation.json`: document/PDF/static algebra checks, versions and preservation hashes.

Sixteen existing review records synchronized: README, successor opening
plan, methods outline, first-verification protocol, living candidates,
C-P plan, progress, Step 3 plan, M2 scope, dialogue, earlier admission and
feedback-7 latest notices, A1-C scope/report, fixed-queue response and S-E
admission report. They now distinguish selected S-E-P from unselected R-E/
R-AE. Previous math and validation reports retain delivery-time identity.

Protected all 102 preexisting root/feedback/mathematical/build/validation
files in the snapshot. Root AGENTS.md contains the user's latest reporting
clarification and is not edited here. The root AGENTS.md/PLANS.md/memo.txt
changes predate this task. Review files remain Git-ignored and durable at
their explicit disk paths. User feedback inboxes are unchanged.

## Assumptions and unresolved risks

Retain continuous mass, fixed geometry, H1 preparation/priority/cutoff,
T1 travel/storage, the known empty initial state, primary ordinary underload,
two potentially active A/E balances, independent unqueued B, one shared
account, local choke completion and S-P→S-L. Early-merged mass is ordinary
A in the terminal, not a second compulsory E merge.

Both recovery laws are explicit mathematical hypotheses using the same
proposed speed marks and additive profile overlap. Their physical validity,
current-work/recovery separation and any A renewal independence are not
proved. Fixed-mode causal construction and finite-loss clearance bounds
do not establish a full hybrid solution. No source proof or M1 uniqueness
is transferred; no parameter is selected for an interior optimum or positive
gradient result. Strong simpler rivals and a negative/common-action outcome
remain valid.

## Commands, environment and source access

Used `rg`, `sed`, Python file reads and `git status --short` to inspect
latest instructions/feedback, selected option, prior exact work/kernel laws,
review plan, living inventory and stage status. The global feedback file
has no separate active VSL review tab; current interactive direction and
the VSL inbox govern. Used primary web open/find/search for the papers
and sections in the source audit. Jin/Laval's publisher direct access
failed; only primary search-returned abstract/introduction is used, with
that limit recorded. No full native algorithm was newly qualified.

Verified existing `/usr/bin/pdflatex`. Used
`/home/zpz/miniconda3/envs/differential_sim/bin/python` with installed
`sympy` and `pypdf`; installed nothing.

Build command:

```text
python3 /tmp/vsl_sep_recovery_build.py
```

The script runs `pdflatex -interaction=nonstopmode -halt-on-error` twice,
with `/tmp/vsl_sep_recovery_latex` as output directory, then copies the PDF
and final log to the review. One long equation overflowed initially;
splitting its layout removed the overflow without changing its mathematics.
The final PDF has five pages, extractable text, vector fonts and no final
overflow/rerun warnings. No raster visual inspection is claimed.

Synchronization command:

```text
python3 /tmp/vsl_sep_recovery_sync.py
```

Document/PDF/exact algebra verification:

```text
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_sep_recovery_checks.py
```

Preservation snapshots: `/tmp/vsl_sep_recovery_before.json` and
`/tmp/vsl_sep_recovery_preimages.json`. Durable hashes/results are retained
in the validation JSON. Scratch scripts do document work and exact local
algebra; none is a simulator or traffic runner.

## Checks and scientific meaning

Checks cover local links/heading targets, selected priority versus open
source-law status, candidate specification/proof limits, strict PDF parsing,
page text/fonts/build warnings, rational queue-clearance and tail-source
identities, symbolic profile/derivative/work/barrier/clearance identities,
and all 102 protected-file hashes. All passed: 20 Markdown documents,
490 local links, 26 heading targets, five exact static checks, 12 symbolic
identities and strict parsing of the five-page PDF. The final PDF has only
Type 1 fonts and no overflow or rerun warnings. Results and package versions
are linked.

No traffic time stepping, rollout, experiment, calibration, optimization,
numerical gradient, SUMO execution, dependency change or production unit
suite was run. Static algebra and documentary checks do not establish
empirical fidelity, complete primary MP6 or useful gradients.

[Verification results and hashes](vsl_sep_recovery_validation.json)

[Main report and source-law gate](vsl_sep_recovery_findings_and_gate.md)
