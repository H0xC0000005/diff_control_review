# Feedback 4 — conceptual B2 option comparison

Date: 2026-10-13. Status: **Presentation revision complete at VSL-B2-G1;
receiver/motion route unselected.**

## What changed and why

The user found the B2-A/B2-B gate logically plausible but too procedural to
make each option's modeling philosophy and main change easy to grasp. The
repository-wide review guidance in `AGENTS.md` now requires option proposals
to lead with the shared traffic problem, core idea, explicit old/new modeling
change and direct comparison before work steps. This preference applies to
later review branches as well.

The decision-facing B2 report now asks whether the target lane can be
represented by one evolving occupied stock or whether a short region must
remember where traffic is. Its direct table compares the routes' purpose,
S13 delta, expressive difference, risk and conditions for use. The checked
same-current-receiving/different-stock example supports the need to represent
occupied space. A separate, explicitly conceptual equal-stock/different-queue-
location example explains the possible value of spatial state without claiming
to prove it necessary. The living candidate record has the same distinction,
pros, cons, dependencies and provisional recommendation. README navigation and
the phase dialogue point to the reworked gate.

[Reworked decision-facing gate](vsl_b2_joined_service_findings_and_gate.md)

[Synchronized living candidates](../../synthesis/research_readiness/vsl_feedback1_core_model_candidates.md)

## Scope, checks and remaining decision

Changed files: repository `AGENTS.md`; review-package `README.md`, B2 gate
report, living candidate record, phase dialogue and this work report; and
the feedback-4 heading's answered marker. The feedback prose, source audit,
mathematical note, approved P1 contract, S13 result and earlier candidate
directions are preserved. Existing unrelated edits to `AGENTS.md`,
`PLANS.md` and `memo.txt` were left intact.

Assumption: feedback 4 requests clearer presentation of the existing two
routes, not a new choice or a fresh source/evidence pass. No new scientific
claim, receiver state, motion law, information witness or MP6 applied regime
was adopted.

Commands/tools used: `sed`, `rg`, `tail`, `find`, `git status --short`,
`git diff -- AGENTS.md`, `apply_patch` and standard-library Python document
checks. No simulator code, dependency installation, traffic experiment,
production test or literature search was run. The document checks verify
protected-file hashes, targeted changes against before-copies, append-only
dialogue, the feedback marker and local links. Tests of traffic behavior are
not applicable to this prose-only revision.

Document checks passed: 217 protected files are unchanged; the feedback inbox
diff is exactly the answered heading with its original missing final newline
preserved; the dialogue is append-only; `AGENTS.md` differs from its
before-copy only by the new preference block; prior gate context and
candidate sections outside the B2 alternatives are intact; and 118 local
links across the edited review documents resolve.

The unresolved scientific choice remains whether a compact autonomous
receiver-stock/motion closure can cover the admitted elementary VSL domain.
If it fails on a concrete service or timing dependency, the small spatial
route remains open. Status remains **VSL-B2-G1**. The next allowed action is a
bounded qualification of the chosen route after the gate decision; this work
does not begin it.
