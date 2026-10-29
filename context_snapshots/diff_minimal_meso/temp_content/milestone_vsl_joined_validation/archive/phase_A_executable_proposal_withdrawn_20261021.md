# Withdrawn historical document — not an active plan

The user clarified on 2026-10-21 that this review is analytical and
methodological. The executable scope below was never approved or run and
is withdrawn. Original text is retained, with relative links rebased for
this archive.

Original SHA256: 8749f389cc25811da70409ff0f219f61ad08255a1da6af8463dfc637cc553e9e

---

# Joined VSL validation: executable-plan proposal

2026-10-21. **Phase A complete; proposed, awaiting user approval at VJV-P.**
This is a standalone VSL validation work package. It does not open or alter
urban Milestone 2. No implementation or scientific run is authorized by the
preparation of this document.

## The decision in plain language

We have established that the published lane model, selected Han budgets and
selected allocator can form a complete task. We now need to check whether
an implementation follows those equations, whether its full travel-time
derivative is correct, and whether the additional information or gradients
actually help choose speed advice. These are three different claims.

The proposal is to implement one small, separate evaluator and qualify it
in three components, each with an acceptance gate:

| Order and gate | What the work must establish | What happens at the gate |
|---|---|---|
| **VC1 / VJV-F: traffic and complete accounting** | Traffic follows the declared budgets, lane preferences and allocation; every unfinished unit's time is counted. | Present independent references, conservation/storage checks and complete-objective evidence; stop for acceptance. |
| **VC2 / VJV-S: sensitivities** | Derivatives of that same complete objective agree with independent numerical differences on regular traces; switches are exposed. | Present agreement, branch coverage and failures; stop for acceptance. |
| **VC3 / VJV-U: decisions** | Fair comparisons reveal whether lane information changes useful advice and how gradients compare with simpler search. | Present all outcomes, including null effects, and the limits of the supported claims; stop for review. |

**Approval at the current gate VJV-P** would select the concrete member,
interfaces, tests, numerical criteria and comparison settings below. It
would not mark any scientific check passed. After approval, freeze the
plan under `docs/milestones/milestone_vsl_joined_validation.md`; a subsequent
authorized implementation pass begins VC1 only. No additional traffic-law
choice is currently posed.

## Starting evidence and scope

The [complete model PDF](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf)
is the equation authority: sections 1–4 define the evaluator, section 5 the
information diagnostic, and sections 6–7 the exact residual objective and
regular-trace derivative. Its
[LaTeX source](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.tex)
and [assumption/source audit](../../../../../misc/differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)
remain unchanged. The existing
[verification contract](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_verification_contract.md)
governs comparison fairness. Subraveti supplies the density/incentive backbone;
Han supplies the selected budget/VSL lineage; the Carey/Wright-based allocator
is the explicit limited adaptation. Calibration, maximum-throughput properties
and source empirical results are not inherited.

**Member proposed for this validation.** Ten 100 m rows; lanes E, A, B; E ends
at the downstream line and A/B have free outlets. Six-second updates; nominal
free/backward speeds 60/20 km/h; jam density 150 veh/km/lane; maximum capacity
drop 0.1; route distance 750 m; lookahead weights 2:2:1. One constant common
advice between 30 and 60 km/h. All initial mass is inside the road and
independent of advice, with no later arrivals. Completion occurs across the
lane-drop line. Preserve every finite-domain, empty-donor, incentive-direction
and equality convention in the mathematical member. LF1 and LF2/H remain
selected; the values above become the first validation configuration only
after this plan is approved, not field calibration.

Excluded: urban LTM/ledger integration, a recovery meter or downstream zone,
continuing arrivals, feedback/history controllers, learned policies, a new
hidden-state family, new traffic rules, smoothing, surrogate gradients,
performance optimization and dependency installation. SUMO remains optional
future work. Neither positive information value nor an interior optimum is
an acceptance requirement.

**Verified repository and environment.** Current branch is
`m2_interaction_zone`, HEAD `48def0f2a3d22219a0629fdb570ccb5c94084e4f`;
pre-existing edits are `AGENTS.md`, `PLANS.md` and `memo.txt`. Urban Phase B
records also exist and remain outside this work. The accepted simulator
has no implementation of this candidate. Its
[gradient checker](../../../src/diff_minimal_meso/gradients.py) requires a
multi-phase simplex and its
[objective](../../../src/diff_minimal_meso/objectives.py) counts a finite urban
rollout; neither is a drop-in interface for scalar advice and the exact tail.

Use the existing `/home/zpz/miniconda3/envs/diff_minimal_meso/bin/python`:
Python 3.12.13, PyTorch 2.5.1, pytest 9.0.3, verified by import/introspection.
`torch.autograd.grad` and `torch.func.jvp` are present; operation-level
correctness remains to be tested. The process default dtype is float32:
construct all validation tensors explicitly as CPU float64. Small deterministic
reference cases use CPU by design, not as a fallback from a failed GPU probe.
No environment change or installation is needed. Inspect again before execution
and record changes rather than assuming this snapshot is permanent.

Before implementation, use an isolated VSL checkout/branch based on the
recorded HEAD, preserving the current urban checkout and all user edits.
Proposed implementation paths and commands below are relative to that
checkout's repository root. Retain a read-only snapshot of the required
review authorities there and record both checkout paths and authority hashes
in the evidence. This planning pass creates no branch or worktree.

## Shared interface and numerical contract

Use a separate `src/vsl_joined_validation/` package. Do not change existing
`src/diff_minimal_meso/` behavior or import its node/rollout laws as this
candidate. Retain textbook units from the mathematical member: km, h,
vehicle equivalents; convert reported seconds and veh/h explicitly. This
standalone interface does not change the urban SI-unit convention.

| Value | Shape/type | Meaning |
|---|---|---|
| `stock`, `initial_stock` | float64 `[10,3]` | Vehicle-equivalent mass; initial stock is independent of advice. |
| `advice_kmh` | float64 scalar `[]` | Only control input differentiated in this package. |
| Densities / density lookahead | float64 `[10,3]` | Veh/km/lane, derived from physical stock and row length. |
| Sending/receiving amounts | float64 `[10,3]` | Shared donor/target budgets per update; rates are explicitly converted by the time step. |
| Desires, requests, flows | float64 `[10,3,3]` | Row, origin lane, target lane; desires are dimensionless, requests/flows are mass. |
| Completions | float64 `[2]` per update | Exit mass into A/B outlets; no downstream stock is created. |
| Objective / derivative | scalar float64 | Veh-equivalent hours / veh-equivalent hours per km/h. |
| Geometry, permissions, mode/active-set records | fixed Python metadata or CPU bool/index tensors | Not differentiated; diagnostic records do not replace physical state. |

One update evaluates all densities, H budgets and preferences from old stock;
masks nonexistent destinations; forms normalized joint donor requests; applies
one exact capped-sharing allocation per target; applies one same-lane fallback;
then updates all stocks and exits simultaneously. No arriving traffic is
reused in that update. Terminal E has only E-to-A and no forward fallback.
The same target receives one common budget for all contenders.

Implement equal-priority capped sharing by finitely removing requests already
below their equal entitlement, then dividing the remaining budget among the
remaining contenders. At most three donors participate; no approximate root
finder is needed. Keep selected arithmetic in tensors. Comparisons may choose
active branches; `.item()`, `detach`, NumPy or tensor reconstruction may not
break the selected arithmetic path. Skip undefined ratios for exactly empty
donors; do not add density epsilons.

For ordinary evaluation, stop the simulated prefix at the first total stock
at or below **1.875 veh**, half the proved 3.75 veh threshold, and add the
**exact** remaining value from section 7. This is a convenient index inside
the proved regime, not discarded traffic or a modified objective. An empty
initial state uses the exact zero residual. A **10,000-step resource guard**
raises an incomplete-evaluation failure; it must never return a truncated
objective. For a derivative check, fix the baseline prefix index and require
all perturbed states at that index to remain strictly below 3.75 veh.

Proposed acceptance tolerances are fixed before execution:

| Check | Numerical rule |
|---|---|
| Local reference values, rates and flows | Absolute tolerance `1e-12` plus relative tolerance `1e-10`, in each stated unit. |
| Stock, sending/receiving and storage inequalities | Maximum violation `1e-12` veh per step; record raw minimum/excess, without clipping. |
| Whole-cohort cumulative mass balance | Absolute residual at most `1e-9` veh. |
| Complete objective, independent reference and residual-index invariance | Absolute tolerance `1e-10` veh·h plus relative tolerance `1e-9`. |
| Reverse derivative versus JVP | Absolute tolerance `1e-10` plus relative tolerance `1e-10`. |
| AD versus independent central difference | Absolute tolerance `1e-8` plus relative tolerance `1e-6`; at least three consecutive decreasing eligible perturbations must agree. |

Relative comparisons use the larger absolute compared value. Tolerances
evaluate evidence; they never change a flow, state or branch. If tiny raw
negative values make a subsequent ratio invalid, stop and diagnose arithmetic;
do not introduce clipping to continue. A criterion needing amendment returns
to the gate with the failed evidence.

## VC1: complete forward evaluator and accounting

**Files and interface.** Create `records.py`, `model.py`, `objectives.py` and
`__init__.py` in the new package. Small immutable records define parameters,
stock and results; pure functions in `model.py` expose budgets, preferences,
allocation and `step(stock, advice, parameters)`. `objectives.py` composes
steps and the exact tail, returning objective, prefix index, terminal stock,
completions and diagnostics. Retain the initial left-interval stock in each
step's population-time, as in the equation authority.

Add a test-package `__init__.py`, `tests/vsl_joined_validation/reference_scalar.py` and
`test_forward.py`. The scalar reference uses Python arithmetic/Fractions for
exact static cases, ordinary scalar loops for trajectories, and an independent
enumeration of capped-sharing active sets. It may read the same declared
configuration, but must not import production traffic helpers or use AD.

Create `configs/vsl_joined_validation/review_member.json` as the single
configuration for member values, cases, advice grids, tolerances and budgets.
Add `scripts/run_vsl_joined_validation.py` with an explicit `--stage` selector;
there is no automatic run-all mode. VC1 implements the forward stage only.

**Mandatory evidence.**

- H bounds at vacuum, critical/jam density and a deterministic 5-by-5 density
  grid using 0, 18.75, 37.5, 93.75 and 150 veh/km/lane on each axis,
  including the previously qualified upstream-150/current-40/next-39.9
  or 40.1 case. Selected H serves 2025 veh/h on both sides at advice 60.
- Native incentive branches, route activation, the finite E lookahead,
  vacant donors, nominal-critical-density equality and outlet masks.
- Existing allocator hand cases: overbooking resolves to `(2,5,3)`; an
  unsuccessful pre-end attempt can use all ten units forward; terminal E
  cannot do so; constrained sharing gives `(4,4)` and `(1,7)`. Reproduce the
  admitted 15-versus-feasible-20 throughput limitation rather than "repairing"
  it. These remain allocator inputs, not claimed reachable density cases.
- The actual X/Z initialization: penultimate densities 37.5 in all lanes;
  final E 120, A/B 60/90 or 90/60; earlier rows empty. At advice 60 reproduce
  E service 877.5/1072.5 veh/h, exits 4005/4350 veh/h and next total mass
  31.575/31 veh. Initial total mass is 38.25 veh in both.
- Complete trajectories at advice 30, 45 and 60 for: empty road; one vehicle
  equivalent in final E; 0.1 veh in every first-row lane and none elsewhere;
  a jam-initialized road; row 9 E containing 2 veh with final A at jam and
  all other cells empty; X; and Z. Require conservation, permissions,
  storage/budget bounds, independent-reference agreement and valid exact
  tails. These are deterministic mathematical fixtures, not calibrated cases.
- Compare complete objectives at the selected residual index and 1 and 10
  updates later. Check the small-cohort residence-time reference directly.
  Save stock/flow/completion traces for manual inspection. No exact finite
  emptying or old no-queue-reformation result is required.

**Gate VJV-F.** Every mandatory correctness check passes within the declared
tolerances, or is reported failed/incomplete. Present a readable account of
the traffic behavior and a per-criterion evidence table, then stop. Passing
does not establish real-traffic fidelity. Do not begin VC2 before acceptance.

## VC2: complete-objective sensitivities

**Files and interface.** Add `sensitivity.py` and `test_sensitivity.py`; extend
the runner with the gradients stage. Tensor-only scalar wrappers construct
fixed records internally for `torch.func.jvp`; no custom tensor registration
or differentiation through metadata is needed. Reverse AD, JVP and the
section-7 three-term decomposition must describe the same fixed-prefix,
exact-residual objective. The reference finite difference evaluates the
independent scalar implementation, not only a second production call.

Check the small-cohort cases and X/Z at advice **35, 45, 55**. Scan central
perturbations **0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001 km/h**; check
bounds and the residual's strict regime. Record native modes, branch choices,
request caps, sharing sets, fallback constraints and raw comparison gaps
through the common prefix. Exact structural zeros and documented persistent
initial ties are distinguished from changing branches. A trace with differing
active formulas cannot be counted as a regular central-difference pass merely
because the numerical answer happens to agree.

Show the finite-prefix, residual-state and direct-speed contributions
separately; verify their sum and residual-index invariance. Include
one-sided/finite-change diagnostics at advice bounds and native incentive
mode boundaries. Such diagnostics are not required to have a two-sided
derivative. Do not add continuous-time saltation to the fixed-step evaluator.

**Gate VJV-S.** Require agreement on eligible small-cohort cases and at
least one interacting X/Z trace, with three adjacent passing perturbations
and reverse/JVP agreement. Report every planned case, including switches or
insufficient regular coverage. If no interacting trace qualifies, report the
coverage gap and stop; do not smooth the law, silently replace cases or
claim a general gradient pass. Other scientifically justified follow-up
sampling requires an explicit recorded extension. Stop for acceptance before VC3.

## VC3: information value and advice usefulness

**Files and interface.** Add `decisions.py`, `test_decisions.py` and the runner's
decisions stage. Use only the declared equal-probability X/Z pair. Observation
functions return row totals; E plus rowwise A+B; that state plus final A
density; or all lane densities. Scenario IDs are evidence keys, never policy
inputs. All observers know the model and prior. The first two observations
coincide across X/Z; the extra scalar identifies the pair exactly. Verify
that compact and full observers consequently use equivalent conditional
objectives. No learning algorithm or hidden-label input is needed.

Separate the shared expected objective from each mode-conditioned objective.
Report approximate best shared and conditional actions and values without
claiming that a finite search attains the mathematical infimum. On this
pair, the comparison cannot establish a need for all lane fields.
Use the common 61-point coarse grid below to report best-action information
value on that finite action set. Report subsequent refinements separately:
the finite-set result need not equal the continuous-action information value.
Do not interpret an optimizer's underperformance as an information effect.

Under each information setting include:

- Maximum advice 60 km/h.
- Scalar search over **61 uniformly spaced advice values from 30 to 60**,
  followed by ten equally spaced interior samples between the best coarse
  value and each existing adjacent coarse value: at most 20 new evaluations.
  Break exact objective ties by lower advice; report all coarse ties and
  refinement locations. This is a bounded strong reference, not a global
  optimality certificate for a discontinuous function.
- A gradient method starting at **45 km/h**: follow the derivative's descent
  sign, begin each iteration with a 2 km/h trial, enforce the advice bounds,
  and halve the trial on rejection up to five trials. Accept only a strict
  full-objective
  decrease, retain the best visited advice, and stop on zero derivative,
  unchanged feasible advice, no accepted trial or budget exhaustion. These
  are optimizer rules, not new traffic rules or an optimality certificate.

For each conditional objective use a budget of **81 sweep units**: one full
cohort objective evaluation costs one; value plus reverse derivative costs
two. A reduced expected-objective call costs two such cohort units; a full
policy has two separately budgeted conditional decisions. This matches the
declared oracle-work allowance across paired hypotheses. Count every trial
and backward sweep. Record actual forward steps and wall time as well:
sweep accounting does not assert identical runtime. No uncharged tuning,
cached hidden-state answer or extra restarts enter the comparison.

Also inspect feasible ±0.25 and ±1 km/h changes at 35, 45 and 55 under the
same information. Report derivative-predicted direction and actual complete
objective changes, distinguishing regular local changes from switch-crossing
steps. These diagnostics are separate from the optimizer budget. Re-evaluate
selected advice with the independent reference; report objective and action
gaps with numerical/search uncertainty. Zero information value, common-fastest
advice and search outperforming gradients are legitimate outcomes.

**Gate VJV-U.** Accept completed, reproducible and fair comparisons, not a
predetermined winner. Report what is supported about information, compact
representation and gradients separately. No within-model result is physical
validation or a SUMO transfer claim. Stop for user review and final disposition.

## Question ownership, approval order and reopen conditions

All entries below are **proposed for VJV-P**, not newly selected traffic laws.
Resolve VG1–VG5 together before dependent local work. Closed LF1/LF2 decisions
are inputs. A local transcription cannot amend a global contract.

| ID / class | Owner and dependency | Contract or local detail | Reopen when |
|---|---|---|---|
| **VG1 / Type 2** | User; before VC1 | Standalone scope, member/defaults, initialization, exit and action timing. | Execution needs different traffic, geometry, arrivals or control timing. |
| **VG2 / Type 2** | User; depends VG1 | Shared shapes/units, old-state update, exact complete objective and regular derivative meaning. | A local API, tail rule or branch repair changes those meanings. |
| **VG3 / Type 2** | User; depends VG2 | Independent references, numerical criteria and required coverage. | A criterion must be weakened, omitted or replaced. |
| **VG4 / Type 2** | User; depends VG1–VG3 | Observations/prior, scalar and compact rivals, optimizer budgets and null-result interpretation. | Concealment, information access or comparison fairness changes. |
| **VG5 / Type 2** | User; governs all | Serial component gates, environment/config provenance and immutable evidence. | Work needs new dependencies or a different acceptance/workflow boundary. |
| **VC1-Q1 / Type 1** | Implementer; VG2/VG3 | Exact capped-sharing algorithm, scalar-reference organization and trace serialization specified above. | Conflict with VG2 or reference independence: reopen that global contract. |
| **VC2-Q1 / Type 1** | Implementer; VG2/VG3, accepted VC1 | Scalar tensor wrappers and active-trace diagnostics. | Stable traces or full derivatives cannot be represented: reopen VG2/VG3. |
| **VC3-Q1 / Type 1** | Implementer; VG4/VG5, accepted VC2 | Observation/decision tables, sweep counters and deterministic report layout. | Hidden input or unaccounted computation changes VG4 fairness. |

This splits the mixed issues explicitly: scientific derivative/regularity
belongs to VG2/VG3 while tracing mechanics belong to VC2-Q1; scientific
comparison fairness belongs to VG4 while counters/serialization belong to
VC3-Q1. No additional unresolved component method is delegated silently.

## Commands, evidence and stop rule

The files/CLI below are **proposed future interfaces, not existing commands
that were run for this proposal**. Execute from the repository root only
after approval and authorization of the corresponding component.

```bash
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python -m pytest -q tests/vsl_joined_validation/test_forward.py
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python scripts/run_vsl_joined_validation.py --stage forward --config configs/vsl_joined_validation/review_member.json --output-root reports/vsl_joined_validation
```

After VJV-F acceptance:

```bash
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python -m pytest -q tests/vsl_joined_validation/test_sensitivity.py
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python scripts/run_vsl_joined_validation.py --stage gradients --config configs/vsl_joined_validation/review_member.json --output-root reports/vsl_joined_validation
```

After VJV-S acceptance:

```bash
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python -m pytest -q tests/vsl_joined_validation/test_decisions.py
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python scripts/run_vsl_joined_validation.py --stage decisions --config configs/vsl_joined_validation/review_member.json --output-root reports/vsl_joined_validation
PYTHONPATH=src /home/zpz/miniconda3/envs/diff_minimal_meso/bin/python -m pytest -q tests
```

The final command checks VSL integration and the existing suite together.
Broaden or repeat testing only for a failure, further change or unresolved
concern. Existing urban files are not modified by this plan.

Each stage creates a unique UTC-qualified output directory and refuses to
overwrite it. Retain full config and hash; code and mathematical-authority
hashes; git HEAD/dirty status; command; Python/PyTorch/pytest versions;
dtype/device; per-criterion JSON; CSV traces/decision tables; and a short
human-readable Markdown explanation. Preserve failure records and limits,
not just successful rows. All cases are deterministic; no stochastic seed
or sampling claim is applicable. Keep component work/evidence summaries in
this planning directory's `phase_D/` and `phase_E/` records. No detached or
overnight runner is part of the proposal.

Fix implementation-conformance defects within the approved component. If
evidence challenges the equations, information contract or acceptance rules,
document the failure and reopen the smallest affected VG contract before
changing behavior. Do not reinterpret an unfavorable research outcome as a
software failure. Stop at VJV-P now; the first future evidence gate is VJV-F.

[Planning work record and static checks](../phase_A_dialogue.md)
