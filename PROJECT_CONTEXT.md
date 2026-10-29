# Review context

This repository maintains literature, methodology and task-definition
reviews for differentiable traffic-control research. The urban and freeway
tasks are separate lines. Common questions concern how traffic information,
representation and sensitivities support control decisions; neither line
is required to reproduce the other's traffic laws.

The selected VSL candidate is a continuous-mass lane-cell model using the
Subraveti lane-density/incentive backbone, inherited Han congestion/VSL
budgets and one Carey-led movement adaptation with Wright supporting sharing.
Its full-time objective and regular-branch sensitivity are analytically
qualified under declared assumptions. Numerical gradient usefulness,
physical fidelity and a positive optimal-advice information gap are not established.

Feedback 17 authorizes migration of all `misc` reviews and creation of the
separate [VSL repository](https://github.com/H0xC0000005/diff_freeway_vsl). It authorizes bootstrap/handoff,
not simulator code, dependencies, experiments or an implementation plan.
The VSL development agent begins with Phase A under that repository's rules.

Reviews here follow scientific topics, evidence, alternatives, decisions
and discussion logs. They do not inherit implementation milestone gates.
Detailed historical urban implementation context is data in
`context_snapshots/diff_minimal_meso/`, not the active charter of this repository.

Use [REVIEW_INDEX.md](REVIEW_INDEX.md) and the applicable collection's
current overview. Preserve source support/adaptation boundaries and
distinguish selected decisions, defaults, hypotheses and open questions.
