# S04.00 — Route B diagnostic continuation — Phase A proposal

Sprint: [S04](00_review_sequence.md#s04) · Role: 00 plan · Predecessor: S03 / diagnostic planning · Gate: DG-MUG1.

Prepared: 2026-09-17. **Status: Methodology review closed; DG-MUG1 Candidate A approved.**
Approved: 2026-09-17 by explicit user approval of the Phase A proposal.
Execution clarification: user explicitly limited this continuation to methodology
and excluded server/toolchain configuration. Numerical designs below remain
prospective; no simulation, implementation or installation is authorized.
[Current findings and substantive user gate](reporting/s04/s04_20_rb_diagnostic_methodology_findings_and_gate.md).
Subsequent authorized Candidate A construction is completed at
[DG-AC1](reporting/s05/s05_20_rb_certificate_findings_and_gate.md); numerical settings below
remain unchanged and no implementation/traffic run has been authorized.
The [Route B sprint is closed](reporting/s03/s03_99_rb_sprint_closure.md);
the user approved this separately gated plan as the next stage in the
same freeway package. Continuation position: RB-UG1 → approved diagnostic plan.
“Phase A” is a retained document label, not a requirement to repeat the urban
development lifecycle. The review is closed; diagnostic settings are approved.

## 1. Mainline

Accepted conditional direction: identify when a strong aggregate response/history
model loses information that changes useful common-speed-advice decisions, then
test the smallest conservative refinement and its independently useful gradients.

**This pass reviews the argument/design for the first link only.** It neither
constructs a simulator nor supplies a reachable-pair or gradient validation result.

Proposed sequence:

| Pass | Question and evidence | Stop |
|---|---|---|
| Reference methodology | Are common desired-speed response, endogenous driving and all-demand accounting defensible? | Methodological incompatibility, not server configuration. |
| Preparation/matching methodology | Do sources/arguments establish reachable different configurations with the declared equal aggregate/history channel? | Stop if the evidence supports a different information/model claim instead of certifying the intended pair. |
| Shared-action diagnostic design | Would complete acceptable sets/common-action regret identify useful decision differences without overstating gradients? | Documentary findings/user gate; no invented scores or automatic construction. |

An unsuccessful match search is a bounded setup result, not refutation of the
information hypothesis. A positive action result is finite-menu, synthetic
evidence, not continuous-space optimality, minimum state or useful gradients.

## 2. Recommended scope

Use a synthetic, headless SUMO reference with a permanent three-to-two physical
lane reduction and homogeneous passenger traffic. Different preparation lane
allocations are exogenous initial conditions, not ongoing control.
Native car-following and lane changing determine subsequent movement.

The three-to-two choice retains the continuing-lane balance mechanism identified
in the review. It is not a claim that two-to-one cannot work. Temporary closure/
reopening is outside this first diagnostic; recovery remains mandatory for any
later temporary-closure claim. No additional merge mechanism is invented.

A single upstream advice zone receives one common continuous-valued advice on
every lane. The proposed synthetic response changes desired free speed, not
actual motion or legal road limits. Its gain is fixed within each context.
Use unchanged advice and symmetric early/late pulse probes; the probe menu
samples a continuous feasible space rather than rounding the control variable.

Keep demand, routes, driver parameters, geometry and future lane entry pattern
identical within each matched pair. Record different preparation conditions.
No CAV commands, ramps, routing, lane-change commands, stochastic response
classes, order ledger, safety objective or incident optimization.

## 3. Strong aggregate information without a new macro implementation

For this reference-first test, freeze a lane-blind information envelope covering
spatial counts/density, mean speed, source waiting, cumulative boundary/internal
flows, full available predecision observation/advice history and known response/
geometry/future demand. It supplies more observational history than a current-
state-only macro baseline. Include connector traffic and empty-cell masks.

The controller is not told past per-vehicle lane assignments or microscopic
leader/gap topology. Those are hidden preparation metadata, not aggregate
observations. The exact information channel is specified in the
[technical contract](synthesis/s04/rb_diagnostic_technical_contract.md).

Identical declared inputs prevent a deterministic controller using only those
inputs from choosing different initial open-loop actions. This can establish an
information collision without coding METANET or a lane simulator. It does NOT
benchmark Frejo/Wei model gradients or prove all possible aggregate observers
fail. Grid/history/extra-observable audits limit that interpretation.

Primary matching requires exact equality of the serialized numerical inputs;
near equality is reported separately. Never round observations, shorten memory,
overwrite a rollout state or pick a weaker baseline to create a positive case.
If exact matching fails, approximate matching requires a newly agreed residual/
observer error contract before action-outcome testing.

## 4. Reviewed prospective numerical evidence obligations

The design settings, preparation bank, probe menu, run caps, state units/shapes,
accounting and pass/failure thresholds are in the technical contract, not copied
from source studies as if calibrated facts.

Select pairs using predecision matching and occupancy only, before inspecting
postdecision action outcomes. Replay from original inputs for every action.
Keep development checks separate from frozen evaluation/robustness contexts.
There is no field calibration claim or parameter tuning to obtain a benefit.

Score all-population time spent from intended departure through completion;
audit both an independent presence ledger and trip records. Incomplete or
teleported traffic cannot obtain a lower arrived-only score.

Assess the best acceptable action sets and forced common-action regret.
A reversal between two inferior actions is not enough if a third action is
acceptable in both states. Different speeds/queues alone do not pass.

Robustness changes reference time step, aggregate spatial grid and fixed response/
following/demand contexts. Recheck matching in each context. Report no-benefit,
failed preparation and invalid runs rather than quietly selecting successes.

## 5. Boundaries and user gates

User approval accepts the recommended scientific choices and annex settings.
No additional upfront scientific choice or artificial development-phase gate
was required at approval. The executed methodology review now introduces the
evidence-dependent DG-R1 claim choice at DG-MUG1. The
[question inventory](synthesis/s04/rb_diagnostic_question_inventory.md) classifies global contracts and local
details, with global-first closure and reopen conditions.

A separately authorized numerical experiment could later test the design.
The present execution is methodology only: no harness, installation, calibration
or traffic runs. Treat server workability as outside this review under the user's
clarification; do not make a provider/version check a review prerequisite.
Scientific response/model assumptions remain reviewable independently of tooling.

Prospective numerical evidence gate: exact matching is unavailable, hidden occupancy
vanishes, or only artifact-contaminated preparations survive. Present the
measured residuals and strongest counterexample, then ask whether to plan a
bounded near-match study, revise the scenario, or defer. No automatic expansion.

If valid exact matching were demonstrated in a future numerical pass, finish the
predeclared shared-action diagnostic.
At its final gate:

- Robust decision distinction: consider a separate conservative refinement plan,
  including internal derivatives and independent gradient-guided improvement.
- Common acceptable advice: report bounded evidence against needing the hidden
  detail for this probe/domain; assess whether a substantive sufficiency study exists.
- Ambiguous/matching/robustness failure: revise or defer without a positive claim.

## 6. Artifacts and handoff

This approved package-root plan and its approved annexes are the authority for
this independent diagnostic continuation. Keep the existing filename for stable
references; no urban milestone, PLANS.md amendment or extra development-phase
plan is created. Earlier approved review protocols remain historical authorities
for their completed passes, not authorizations for this diagnostic's execution.
The continuation stays within misc/differentiable_freeway_bottleneck_task_review/:
future reference/harness/config/input files under experiments/rb_diagnostic/,
matching/action tables under extraction/ with rb_diagnostic_ prefixes, and
findings/work/user-gate reports under reporting/ with the same prefix.
This editable proposal stays at the package root; its dialogue stays under
reporting/, per the user's explicit package-location clarification.
No existing source/test/config or archived review evidence is modified.

Planned records: one immutable experiment JSON, generated network/vehicle inputs,
engine/version manifest, validation report, preparation/matching register,
per-action results, failure ledger and one primary findings/user-gate report.
No elaborate publication infrastructure or detached execution is needed.

Current acceptance: planning inspection, document/ID/link checks and unchanged
protected-file/archive checks only. No experiment result is asserted.
Current pass: methodological comparison/source audit delivered and closed; no
empirical match, measured residual or action benefit asserted. User selected
Candidate A: next allowed activity is the methodology-only information-loss
certificate study, with [recorded boundary](reporting/s04/s04_99_rb_diagnostic_methodology_closure.md).
Exact-first remains the default; no relaxed matching adopted. Next sprint not started.
