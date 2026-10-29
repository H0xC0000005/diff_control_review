# VSL execution planning: Phase A dialogue and work record

2026-10-21. **Withdrawn.** The user clarifies that the task is analytical
and methodological. The executable proposal and VJV gates were never
approved or executed and are retired. The original planning record below
is historical; its interpretation of scope is corrected by the final entry.

[Active analytical review plan](../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_methodology_review_plan.md)

## User direction and interpretation

The review established constructibility and produced a validation handoff.
The user then requested brief next steps, asked for the next intended gate,
and was told that it is approval of an executable validation plan, followed
by a forward/accounting evidence gate. The user explicitly requested that
next step. This authorizes concrete plan preparation in the current task;
it does not authorize implementation or scientific runs. The prior review
handoff is complete and remains the scientific input, rather than a reason
to repeat another general review plan or require a new agent to be spawned.

Use a separate VSL work-package directory and the repository's A–C planning
and serial D/E component workflow, without assigning this task to urban
Milestone 2. The actual urban Phase B records already exist and are outside
this task. `AGENTS.md`, Phase A, explicitly says **“Stop after the proposal.
Do not implement.”** The user also explicitly agreed that this is the next
gate. This task therefore ends with the concrete proposal for approval.

## Inspection and resulting decisions

Read `AGENTS.md`, `PROJECT_CONTEXT.md`, `PLANS.md`, closed Milestone 0/1
responsibilities and current urban Phase B status. Inspect source, tests,
independent scalar references, configuration and diagnostic runners, especially
the existing FD, objective, rollout and simplex gradient interfaces. Read
the latest applicable VSL feedback and joined model, assumptions, hand cases,
proofs and evidence contract. No new primary-paper search or traffic-law
selection is required by this planning task.

Observed starting branch/commit:
`m2_interaction_zone`, `48def0f2a3d22219a0629fdb570ccb5c94084e4f`.
Pre-existing tracked edits remain `AGENTS.md`, `PLANS.md`, `memo.txt`.
Do not infer urban status solely from the older root roadmap: its actual
Phase B records say the global backbone is closed and local discussion is
active. This VSL proposal leaves both authorities and records untouched.

The accepted urban code is not this lane-density model. Reusing its LTM/node
solver would change the candidate. The existing gradient checker requires
at least two simplex coordinates with a zero-sum direction, and the urban
objective has no exact candidate-specific residual. Propose a small separate
package, retaining the repository's style, independent-reference discipline
and evidence conventions. Existing urban source and APIs are not modified.
Future implementation is proposed in an isolated checkout, with the review
authorities snapshotted and hashed, so the active urban checkout and user
edits are preserved. No branch or worktree is created by this task.

Two installed environments were probed read-only:

| Environment | Python / PyTorch / pytest | Role |
|---|---|---|
| `/home/zpz/miniconda3/envs/differential_sim/bin/python` | 3.11.9 / 2.5.1 / 9.1.0 | Available prior review environment; not proposed as the authoritative validation target. |
| `/home/zpz/miniconda3/envs/diff_minimal_meso/bin/python` | 3.12.13 / 2.5.1 / 9.0.3 | Existing accepted project environment, proposed for future execution. |

`torch.autograd.grad` and `torch.func.jvp` signatures were inspected; tensor
minimum documentation was read locally. Importability does not establish
operation-level derivative correctness, which remains future evidence.
Default dtype is float32, so the plan requires explicit CPU float64 tensors.
No GPU probe or GPU-to-CPU fallback, package installation or environment
change occurs. CPU is the proposed platform for the small reference suite.

## Proposal, assumptions and acceptance boundary

The plan specifies the whole bounded system before implementation: shared
member/defaults, units, tensor shapes, update order, independent references,
exact tail, finite-step resource guard, tolerances, native-switch diagnostics,
three serial components, commands, evidence records and reopen ownership.
Its overview makes the next gates readable without requiring all operational
detail. Global VG1–VG5 contracts precede local VC1-Q1–VC3-Q1 details; the
derivative/tracing and fairness/counter mixed issues are explicitly split.

The scientific source joins and LF1/LF2 remain unchanged. The declared
defaults are proposed for the first validation configuration, not treated
as already approved by constructibility acceptance. The residual index at
half the proved threshold is computational only; the exact future value
remains in every objective. The step guard reports incomplete evaluation
rather than truncating traffic. Numerical tolerances assess evidence and
do not clip states or change branches.

Research checks remain on the equal-probability X/Z pair. They include the
exactly sufficient compact observation, maximum advice, bounded scalar
search and a transparent gradient baseline. The common coarse action grid
defines a finite-set information comparison; refinements and continuous-action
uncertainty are reported separately. Oracle-work accounting and actual run
costs are distinct. No benefit, interior optimum or full-lane necessity is
assumed. Broader hidden-state families, learned controllers, SUMO and physical
calibration are outside this executable proposal.

## Files and commands

Added:

- [Executable proposal](phase_A_proposal.md).
- This dialogue/work record.
- [Static planning verification](phase_A_validation.json).
- [Readable plan-gate overview](../../../../misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_joined_candidate_execution_plan_gate.md)
  in the review package.

Updated six current review/navigation records: package README; progress;
joined findings; completed validation handoff; prospective verification
contract; successor dialogue. Updates are new status/link notices and a
dialogue append. Earlier scientific content, equations, PDFs, feedback and
results are preserved.

Inspection used `pwd`, `rg`, `cat`, `sed`, `tail`, `git status --short`,
`git branch --show-current` and `git rev-parse HEAD`. Python probes used
`platform`, `importlib.metadata`, `inspect`, `torch` and JSON solely to
report installed versions and signatures. Two read commands initially
used an incorrect runner spelling or directory; the actual runner and
repository paths were subsequently inspected. Neither failure concerns a
dependency or scientific behavior. Editing used `apply_patch`.

Before-edit snapshot:
`/tmp/vsl_execution_plan_review/before.json` — 551 prior review-package
files and 708 protected existing files in total, including source, tests,
configs, scripts, approved milestone plans, urban Phase B records, root
authority and feedback. Static verification command:

```bash
python3 /tmp/vsl_execution_plan_review/checks.py
git status --short
```

All document assertions pass: six existing review notices changed, the
other 545 prior review-package files and all other protected existing files
preserved; four expected files added across review/planning; no deletions;
all relative links in touched Markdown resolve; scientific evidence bodies
and source/PDF hashes remain unchanged; planned implementation paths do not
exist. The proposal contains the component gates, interface/units, reference
coverage, numerical tolerances, comparison budgets, ownership taxonomy and
future commands. The checker verifies documents and hashes, not traffic.

No pytest suite, simulator, trajectory, numerical FD, AD/JVP calculation,
optimization or dependency installation was executed. Future commands in
the proposal refer to files that will be created only after approval; they
are not claimed to have run. No new formulas require a new mathematical PDF;
the unchanged six-page equation authority remains linked. No stochastic seed
or scientific run configuration applies to this documentary task.

## Status, risks and next allowed action

Phase A is complete at **VJV-P**, awaiting approval. No new modeling fork was
discovered. Risks remain actual implementation conformance, regular-trace
coverage, numerical gradient correctness, possibly zero information/action
benefit, no optimizer advantage and unproved physical fidelity. These are
future evidence obligations, not documentary pass results.

After approval, record the accepted plan under
`docs/milestones/milestone_vsl_joined_validation.md` and preserve the accepted
global contracts before any component work. A subsequent authorized pass is
VC1 D/E only, ending at **VJV-F** for user acceptance. Do not begin VC2, rewrite
the accepted VSL report, close historical pending gates, amend urban work or
resume the closed ramp line. No agent is spawned and no external message is sent.

## User correction: this remains a methodological review

The user explicitly rejects implementation/experimentation as the next
review activity. The conceptual traffic/accounting, sensitivity and task-fit
checks are appropriate, but their evidence must be analytical and
methodological. The earlier interpretation of “carry out the next step” as
authorization to prepare an executable study expanded the intended scope.
It is corrected rather than treated as an approved implementation decision.

Withdraw the proposal, its VJV gates, file plan, tolerances, run commands,
query budgets and experimental-configuration freeze. Preserve the original
unapproved proposal in the archive; replace its active path with a retirement
notice. The active plan belongs in the review package and uses VC1–VC3 as
review questions in one bounded sprint ending at JM1 or a new methodological
choice. Reuse existing source studies and proofs; do not require positive
control results. No code or numerical experiment was created or run from
the withdrawn plan. The previous JSON check is a historical document check,
not a current plan approval or scientific validation.

[Scope correction and preservation record](../../../../misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_methodology_scope_correction_work_report.md)
