# Review context

This repository maintains literature, methodology and task-definition
reviews for differentiable traffic-control research. The urban and freeway
tasks are separate lines. Common questions concern how traffic information,
representation and sensitivities support control decisions; neither line
is required to reproduce the other's traffic laws.

Feedback 18 confirms the literature-backed VSL stack as the development
target after the group meeting. It is a continuous-mass lane-cell model using the
Subraveti lane-density/incentive backbone, inherited Han congestion/VSL
budgets and one Carey-led movement adaptation with Wright supporting sharing.
Its full-time objective and regular-branch sensitivity are analytically
qualified under declared assumptions. Numerical gradient usefulness,
physical fidelity and a positive optimal-advice information gap are not established.

Feedback 17 authorizes migration of all `misc` reviews and creation of the
separate [VSL repository](https://github.com/H0xC0000005/diff_freeway_vsl). It authorizes bootstrap/handoff,
not simulator code, dependencies, experiments or an implementation plan.
The earlier hold pending model choice is superseded by feedback 18.
The user next authorizes the bounded review-side plan: select a published
rival, define the comparison, formulate the elementary verification and
consolidate the handoff. Stop at the next gate or a methodological choice.
This does not authorize development implementation or traffic experiments.

Reviews here follow scientific topics, evidence, alternatives, decisions
and discussion logs. They do not inherit implementation milestone gates.
Detailed historical urban implementation context is data in
`context_snapshots/diff_minimal_meso/`, not the active charter of this repository.

Use [REVIEW_INDEX.md](REVIEW_INDEX.md) and the applicable collection's
current overview. Preserve source support/adaptation boundaries and
distinguish selected decisions, defaults, hypotheses and open questions.

## Repository visibility

The user explicitly requests a public diff_control_review repository and a
private diff_freeway_vsl repository on 2026-10-29. This supersedes the initial
private-by-default hosting choice, without changing review or development scope.

## Current VSL review topic

The user confirms that aggregate A is not required for early verification
and authorizes the private handoff alignment. That bounded transition is
complete. The local private entry, scope/timing addendum, evidence note and
portable first-verification specification now carry the selected model and
matched B-first target. This completes the current review-side B preparation.

[Handoff alignment outcome and next action](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_first_handoff_alignment.md)

[Accepted first-verification specification](misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_b_pair_elementary_verification_specification.md)

One common continuous constant-advice controller is tuned separately for
each initialized case. B0 receives complete costs; B-gradient additionally
receives our qualified complete simulator derivative. The plant, controller,
action and complete TST match. Costs also carry consequences of lane detail.
This is per-case planning, not a learned aggregate-observation policy.

The private wrappers now replace provisional model-choice text and qualify
the older observation-only information comparison. All twenty original
mathematical/source exports and the initial provenance files remain unchanged;
the entire implementation-workflow suffix is byte-preserved. A new alignment
manifest records source/export hashes and local navigation.

The next development task is Phase A for the first implementation/system
proposal, under the existing private workflow. Architecture, numerical
settings, executable checks and sequencing belong there. No plan, simulator,
experiment, dependency install, commit or push is produced in this pass.

A remains explicitly deferred under the user's source-core/algorithm-
backbone/intended-behavior requirements. Simpler established alternatives
remain open; Zhang is not fixed as A and no new source survey occurs.
Delle Monache remains excluded. Broader information/representation studies,
shared-policy training, runtime control and SUMO/physical validation are
separate later tasks, not current handoff blockers.

Numerical derivative correctness/usefulness, a positive advice-information
gap and physical fidelity remain unproved. No gradient win, interior optimum
or different X/Z best advice is required. The source observations/bounds
remain valid under their original conditional timing, not as claims about
the current per-case query optimizer. Original urban roots and user feedback
are preserved.
