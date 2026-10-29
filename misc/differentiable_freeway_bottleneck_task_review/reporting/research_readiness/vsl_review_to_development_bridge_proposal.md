# Preparing the VSL review for development

2026-10-29. **Big-picture proposal, not an implementation plan or repository
creation decision.** Colleague discussion is continuing. The user wants
to prepare for the likely VSL direction without prematurely settling that
discussion, and asks how to hand the review to a development agent and
whether a standalone paper warrants a new repository.

**Recommendation: prepare a small, portable research handoff against an
explicit provisional model version, and use a fresh VSL repository for
the eventual development.** This separates scientific meaning from
software planning and avoids carrying the urban simulator's assumptions
into a different traffic model. No new model component is proposed here.

## What should bridge the review and development

The short reports explain the traffic picture to colleagues. A developer
also needs the exact mathematical choices behind that picture, a clear
source of authority and known reference outcomes. Most of this already
exists; the missing work is selection and consolidation, not another broad
literature review or an executable reference simulator.

Keep the initial reading package to three parts:

| Part | What the review should provide | What it enables |
|---|---|---|
| **Research brief** | The VSL question, one constant advice, finite cohort, lane-information comparisons, full-time objective, assumptions, source roles and claim limits. Identify what is selected in the review, what remains under colleague discussion and which numerical settings are illustrative. | The developer understands what research the software must support and does not treat an expected positive result as an assumption. |
| **Complete model specification** | One designated definition of lane-cell state, desires, sending/receiving, shared allocation, update order, boundaries, empty-cell and mode/tie conventions, completion, exact residual accounting and regular-branch sensitivity. Reuse the current full specification and make any clarifications explicit. | The developer can translate the model without reconstructing it from a long dialogue or silently choosing a different traffic law. |
| **Reference and evidence note** | Existing hand examples and expected flows, conservation/storage identities, the exact residual/free-flow results, observer/optimizer fairness and the evidence still needed. Include source/adaptation provenance and a short record of unresolved or provisional points. | These provide anchors for the developer's tests and research validation, without presenting unrun checks as results. |

These can link to deeper literature extracts, but those extracts should
not become a large mandatory reading list. The old task-first formulation
is historical comparison material, not an alternative source of current
equations. The module map must be unambiguous: Subraveti supplies lane
state/desires, Han supplies congestion/VSL budgets, and a Carey-led
adaptation realizes movements. The exact three-lane composition remains
ours, with its existing limitations.

The development agent proposes software architecture, APIs, environment,
module order, numerical checks/tolerances, automation and its implementation
plan within the agreed scientific contract. Execution and consequential
scientific choices retain the user's approval requirements. The review
owns the scientific meaning and records what is known.
An engineering question that changes traffic physics, objective,
observations, action timing or the meaning of a comparison returns to the
user for discussion rather than being resolved inside implementation glue.

## Preparing while colleague discussion continues

A dated **provisional baseline** is sufficient for preparation. It should
identify exactly which documents define it, label the outstanding colleague
questions, and keep illustrative parameter values distinct from scientific
assumptions. It must not be described as final consensus or as a validated
simulator. Later changes should be recorded as changes to that version,
with the affected implementation/evidence identified.

This allows a development agent to assess and plan against a concrete
candidate before final colleague agreement. Any speculative coding or runs
would need their own explicit authorization and a stated provisional scope;
this discussion does not authorize them. A separate model copy for
preparation also avoids rewriting the review whenever code progresses.

The handoff should highlight the principal remaining research uncertainty:
different service under hidden A/B loading does not yet prove different
best advice or useful gradients. After development is authorized, early
evidence should distinguish forward conformance, derivative correctness
and decision value before a large optimization effort. Scalar speed search
and maximum advice are important simple references. The established
free-flow zero-information case is a legitimate reference outcome, not
something to remove to force a favorable result. Exact configurations,
budgets and acceptance procedures belong in the developer's plan.
These are future evidence questions, not reasons to repeat the completed
review or block preparation of the handoff.

## Why a separate repository is preferable here

A separate paper alone would not require a separate repository. Here the
stronger reason is an independently defined model and evidence program.
The current mainline explicitly requires LTM long-link propagation and
ordered FIFO metadata near signals. The VSL candidate uses lane-cell
propagation, density/incentive-based lateral movement and one speed advice.
It should not inherit the existing urban milestones or simulator interfaces.

| Organization | Consequence for this work |
|---|---|
| **Fresh VSL repository — recommended** | Gives the task its own scientific context, instructions, dependencies, tests, evidence and eventual paper release. Requires maintaining those documents separately and making any reused utilities explicit. |
| **Isolated VSL subproject in the current repository** | Keeps everything together, but needs a user-approved scope separating it from parent scientific rules, roadmap, dependencies and outputs. It is more attractive if substantial shared code is demonstrated; that need has not been established here. |

A Git branch or worktree can isolate edits but does not by itself separate
the inherited scientific contract. A fresh repository should therefore
start with a VSL-specific charter and guidance, rather than a wholesale
copy of the existing root instructions, milestones or simulator. General
engineering practices can be retained. Code reuse should be justified
file by file; a shared simulator library is not needed as a starting premise.
Opening a development-agent session at the new repository root would keep
its working context clear, while this review archive remains the source
of the earlier discussion.

## Repository hygiene that matters at the transfer

**A concrete current issue: the review package is not in Git.** Inspection
finds zero tracked files under this review directory. Both the full model
source and colleague report are excluded by the `misc` rule on line 4 of
the root `.gitignore`. A clone or source commit alone would not deliver
the research specification.

The transfer should therefore be a self-contained snapshot of selected
project-owned specification/notes, with a manifest recording original
paths, dates and content hashes. Track the canonical VSL specification,
decisions and source metadata in the new repository. Keep the original
archive in place; do not move it or depend on absolute links into this
workspace or `/tmp`. Bibliographic records and source URLs provide paper
provenance without copying the entire paper archive.

The new repository should have its own scientific context and agent
instructions, a deliberately chosen environment and dependency record,
clear separation of source/tests from generated results, and a convention
for identifying model versions in later evidence. An initially private
standalone repository is a reasonable default; ownership and hosting can
be chosen separately. No repository is created, pushed or published by
this proposal.

## Proposed immediate action and current conclusions

The next useful review deliverable is the **portable provisional handoff
and a short new-repository charter**, assembled from the existing material.
It would give a fresh development agent a concise starting point for its
own implementation plan. It would not prescribe that plan, freeze the
experimental configuration, run a simulator or turn pending colleague
agreement into approval.

The existing model choices and evidence limits remain unchanged. The
handoff/new-repository approach is a recommendation for discussion, not
a recorded user decision. Repository name/location/ownership, the scope
of any authorized speculative development and final colleague conclusions
remain to be settled. There is no need to reopen a traffic component
merely to prepare the proposed handoff.

## Evidence and work record

Read the current research context/roadmap, the completed analytical findings,
the old review-only handoff, full model assumptions and prospective evidence
contract. Inspect tracked paths with `git ls-files` and check exclusions
with `git check-ignore -v`. Save file hashes in
`/tmp/vsl_review_bridge_20261029/before.json` before editing.

[Current model and analytical qualification](../../synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)

[Assumptions and source/adaptation details](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)

[Analytical conclusions and unproved outcomes](vsl_methodology_review_findings_and_gate.md)

[Prospective comparison and derivative evidence](../../synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)

[Current simulator scientific context](../../../../context_snapshots/diff_minimal_meso/PROJECT_CONTEXT.md)

[Root exclusions](../../../../context_snapshots/diff_minimal_meso/.gitignore)

Add only this proposal, its README link and a topic discussion-log entry.
Check local links and preservation of prior files with Python; retain the
output in `/tmp/vsl_review_bridge_20261029/validation.json`. The command is:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_review_bridge_20261029/document_checks.py
git status --short
```

No repository initialization/migration, simulator code, environment change,
dependency installation, numerical traffic test or experiment is performed.
The current topic is the review-to-development bridge; agreed model
conclusions stand and the organizational recommendations remain proposed.

Document checks pass: 174 local links resolve, only the README and topic
discussion log change among existing files, and 611 other snapshotted
files remain byte-identical. The new file is this proposal. Read-only Git
checks confirm zero tracked review files and the `misc` exclusion for the
model specification. All existing models, reports and root guidance are
preserved.
