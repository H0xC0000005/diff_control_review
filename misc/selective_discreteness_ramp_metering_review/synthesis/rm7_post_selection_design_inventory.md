# RM7 post-selection design inventory

Date: 2026-10-01. Status: **Task A and initial review approaches approved; evidence-dependent model adoption remains gated.**

Parent: [task-selection decision](../discussion/rm7_candidate_a_approval_and_extension_record.md).
This preserves the design candidates and their rationale. The user subsequently
approved open-loop G1.A and accepted the recommended review approaches; see the
[continuation decision](../discussion/rm7_open_loop_approval_and_rm8_opening.md).
The [RM8 protocol](../rm8_00_open_loop_local_merge_review_plan.md) transcribes the
accepted approach. RM8 closed with Candidate A approved. UG1.A is Default;
UG2.A was accepted, UG3.B explicitly amended its resource clause, and the current
gate is UG4’s observer contract.
Initial planning is closed; concrete equations and evidence are not assumed.

## Accepted inputs and scope

The user selected RMT-R1 Candidate A: one infrastructure-controlled on-ramp,
finite ramp storage, a multilane mainline and a local merge/acceleration region.
The action is bounded infrastructure metering. The comparison includes complete
affected-population accounting through common clearance, with all-stream total
system time/delay as the primary outcome. Ramp spillback, unserved demand and
merge feasibility/safety are guardrails.

The strong observer receives the complete declared road-total mainline and
ramp-queue history, known geometry, demands and future forcing. Lane/gap
decomposition is the candidate information omission. Neither its necessity nor a
particular representation has been accepted. Aggregate sufficiency is a valid
answer. Current project progress is not an admission constraint.

Candidate C is **Deferred: possible coordinated multi-ramp extension after
positive Candidate A results, subject to a separate user decision**. The exact
positive-evidence threshold should be agreed at local-result closure. A favorable
result inside an assumed richer model alone must not automatically promote C.
Candidate B remains an unselected alternative.

## Inventory, ownership and dependencies

All six questions are Type 2 review-global: they govern scientific meaning or
comparison fairness. The reviewer prepares evidence and alternatives; the user
owns methodological adoption. There are no implementation components or
component-local decisions in this discussion.

| ID | Question | Status and timing | Dependencies |
|---|---|---|---|
| RMD-G1 | What is the meter decision variable? | Closed: G1.A open-loop approved; exact action transcription is later work | Approved local task |
| RMD-G2 | Which merge mechanism and minimum state deserve formulation? | Closed review strategy A; family A approved at RM8-UG1; allocation A Default at RM9-UG1; UG2.A accepted with UG3.B separate-resource amendment; observer gate UG4 open | G1, G3 |
| RMD-G3 | What baseline and information-matching contract isolate the omission? | Closed review strategy A; precise observer/certificate remains evidence work | G1; informs G2 |
| RMD-G4 | Which operating regime makes the omission consequential? | Closed review strategy A grounded against B; numerical settings deferred | G2, G3 |
| RMD-G5 | What derivative meaning is valid for the surviving mechanism? | Closed review approach: evidence-dependent; no estimator adopted | G1–G4 |
| RMD-G6 | What evidence sequence and independent-reference contract are sufficient? | Closed: staged approach A; reference selection follows evidence | G1, G3; later G2–G5 |

Recommended discussion order: establish the provisional review approach for G1
and G6, map G3 baselines, assess G2 mechanisms jointly with G3, identify G4
regimes, then assess G5. Evidence may iterate across questions without silently
adopting a model. The RM8 proposal must specify its own evidence deliverables and
user stop points before execution.

## RMD-G1 — metering action

**Problem statement:** Is the first control object a metering-rate schedule,
parameters of a feedback controller, or rates repeatedly optimized in an MPC
loop?

Later clarification: A/B were two proposed optimization formulations, not an
exhaustive ramp-method taxonomy. MPC is added below as a distinct viable
candidate. Local/coordinated coverage and physical release pattern are separate
axes. See the [methods/PID background](rm7_g1_ramp_metering_methods_background.md).

**Assumed model-chain function:** The meter sets admissible ramp releases;
realized release may also be limited by ramp demand and safe receiving. Those
arrivals interact with mainline traffic, changing delays and subsequent state.

**Core gap:** Task selection allowed a continuous rate or fixed-shape release
schedule. It did not determine whether controller response to changing
observations belongs inside the sensitivity path. The comparison cannot give
one model a different action or additional feedback information by accident.

### Candidate A — common open-loop rate schedule

Use the same bounded time-dependent metering-rate schedule in each traffic
model. Start with a small family of local rate perturbations; choose temporal
resolution and operational meter mapping after reviewing sources.

**Pros:** Separates traffic-model sensitivity from controller design; permits
identical interventions across representations; gives a direct causal path from
release to merge outcome.

**Cons:** Does not by itself validate feedback control; a continuous release
approximation may need an operational interpretation if the richer reference
uses individual releases.

**Dependencies/consequences:** All models must share the rate meaning, feasible
bounds, demand-limited release and terminal accounting. This is not approval of
a time step, signal-cycle approximation or saturation rule.

### Candidate B — common feedback-law parameterization

Optimize shared parameters of a metering rule. Specify its observation interface
and include the state-to-controller-to-release loop in the derivative contract.
Test extra controller observations as a separate comparison if needed.

Subvariants include integral ALINEA, PI-ALINEA or an explicitly specified full
PID. A provisional shared interface is declared aggregate occupancy/density
near the merge/bottleneck, ramp queue information and controller memory.
Sensor location, aggregation, target, bounds and queue handling remain open.

**Pros:** Directly addresses adaptive operation and robustness to disturbances;
may provide a compact controller parameter space.

**Cons:** Changes controller and traffic sensitivity together; unequal
observations can confound the representation effect; feedback derivatives and
queue overrides require additional semantics.

**Dependencies/consequences:** Requires a shared controller-information contract
and explicit handling of overrides before fair model comparisons.

### Candidate C — repeated model-based rate optimization / MPC

At every control update, estimate the current traffic state, forecast future
forcing, optimize a finite-horizon rate schedule, apply its first portion and
repeat with new observations. This is closed-loop operation, while its optimized
variables are future rates rather than gains of a fixed feedback law.

**Pros:** Direct link from predictions to actions; anticipates congestion and
handles declared constraints; provides a strong aggregate competitor and a
possible bridge toward later coordinated metering.

**Cons:** Forecasting, estimation and replanning introduce additional
attribution choices. Predicted-objective gradients with respect to rates are
distinct from derivatives through the repeated optimizer and closed-loop
execution.

**Dependencies/consequences:** Requires a common observer, forecast, objective,
feasible action and reference evaluation contract. It remains an unselected alternative; reviewing it as prior art does not adopt it.

### Release-pattern boundary

Single/multiple-vehicle or staggered release configurations are a separate
actuation axis. Optimizing detailed release timing at the same mean rate can
address a different gap-sensitive task. It is not silently included in A–C:
adoption would reopen the rate/fixed-shape release contract and require event
semantics to be reviewed.

**Accepted initial choice: A first.** Retain B as a later robustness or control
extension and include aggregate MPC in the predecessor/baseline review. C may
be adopted later if warranted. RMD-G1.C is an MPC formulation and is distinct
from RMT-R1 Candidate C, the deferred multi-ramp traffic task.

## RMD-G2 — merge mechanism and retained information

**Problem statement:** What physical mechanism links omitted local information
to effective merge service, and what is the smallest adequate retained state?

**Assumed model-chain function:** Metering changes ramp arrival pressure. Local
mainline and merge state determines feasible admission, lateral redistribution
or disruption of mainline service; these responses determine all-stream delay.

**Core gap:** Target-lane occupancy, receiving pressure, gap distribution,
acceleration and relaxation are hypotheses. Naming them does not establish their
necessity, sufficiency or a causal model. The VSL finite-receiving construction
is reusable evidence but is not the default ramp equation.

### Candidate A — compare a ladder of candidate mechanisms

Review strong aggregate dynamics, a compressed merge-pressure or similar
statistic, lane-group/local lane state, and finer gap/interaction state. Identify
which increments close an evidenced prediction or decision gap. Formulate the
smallest surviving family afterward.

**Pros:** Can answer the minimum-information question; allows compressed-state,
aggregate, mesoscopic or microscopic conclusions; avoids assuming that lanes or
vehicle identity are necessary.

**Cons:** Requires comparison across differing model assumptions; evidence may
not permit a unique minimum state or a common calibration.

**Dependencies/consequences:** G3 defines what each representation may observe.
Source-level physical justification and fair interventions are required before
any ladder increment becomes an adopted model.

### Candidate B — anchor on a published detailed merge model

Select an explicit gap/acceleration/lane-change model after source screening,
then remove or compress selected states in controlled ablations.

**Pros:** Starts from explicit local physics and an operational mechanism;
provides a concrete source for state definitions and possible ablations.

**Cons:** Necessity can become relative to one reference's assumptions; a complex
starting model can obscure a simpler sufficient mechanism.

**Dependencies/consequences:** Requires ablation validity, reference limitations
and comparator calibration to be reviewed. Its complexity cannot be justified
merely by its compatibility or incompatibility with project code.

**Accepted review strategy: A.** Use B where needed as
mechanism evidence or an independent-reference candidate. Do not adopt a state
family before the evidence pass.

## RMD-G3 — comparator and information matching

**Problem statement:** How can we establish that a decision difference comes
from information omitted by a strong aggregate observer?

**Assumed model-chain function:** Each model predicts outcomes of the same meter
intervention using declared state/history. The proposed richer state supplies
information unavailable to the aggregate observer.

**Core gap:** The history principle is accepted, but spatial/temporal
observation resolution, speed/class information, memory, initial conditions and
model-specific additional states are not transcribed. A scalar receiving state
may already resolve the effect; a short snapshot baseline would be inadequate.

### Candidate A — explicit observation contract and matched-history certificate

Inventory the strongest aggregate, multiclass, memory and compressed-state
competitors. Seek two feasible traffic histories with identical declared
aggregate observations and forcing but different hidden local states, then test
whether intervention ranking or useful perturbation differs. Assess whether an
added scalar or lane grouping removes the ambiguity.

**Pros:** Gives direct evidence of information insufficiency; separates history
identity from an arbitrary weak aggregate model; supports a minimum-state claim.

**Cons:** Exact history matching can be hard or impossible for some mechanisms;
observable speed or past discharge may reveal the supposed hidden state.

**Dependencies/consequences:** Observation resolution and physical realizability
must be explicit. Failure to find an exact pair is not a universal sufficiency
proof. G2 and G4 must honor this contract rather than conceal additional
differences.

### Candidate B — conditional predictive/intervention comparison

Use common observations and scenario families to compare forecasts and action
rankings, conditioning on aggregate information. Document any residual
observation mismatch and test whether it explains the claimed improvement.

**Pros:** More accessible with empirical or stochastic traffic; can test
practical added value when exact deterministic collisions are unavailable.

**Cons:** Supports a conditional predictive claim, not an exact deterministic
hidden-information certificate; calibration and unmatched histories can explain
apparent value.

**Dependencies/consequences:** Requires uncertainty and confound analysis.
Changing from exact-certificate to conditional evidence must be explicit, with
the resulting claim weakened accordingly.

**Accepted review target: A first.** Retain B as an
explicit alternative if sources justify it. Do not silently replace exact
identity with numerical closeness.

## RMD-G4 — scenario and control tradeoff

**Problem statement:** In which feasible traffic regime could local information
change the preferred metering action under complete accounting?

**Assumed model-chain function:** Holding ramp traffic incurs waiting; admitting
it can affect merge use, mainline service and future congestion. Their combined
effect determines whether a perturbation helps.

**Core gap:** Lane/gap heterogeneity alone may change forward traffic without
changing a useful decision. The review must exclude artificial benefit from
omitted ramp delay, end-of-horizon demand or an imposed capacity penalty.

### Candidate A — smallest mechanism-isolating traffic family

Seek a local merge family around relevant receiving or congestion boundaries,
with low-demand/equivalence controls and varied ramp/mainline demand or lane
distribution. Require the proposed action difference to survive all-stream
clearance accounting and plausible parameter variation.

**Pros:** Makes causal attribution and trivial-policy checks manageable;
identifies inactive as well as active regimes; supports a compact analytic task.

**Cons:** A constructed family can have limited empirical breadth; excessive
simplification may remove the effect or impose it through assumed service laws.

**Dependencies/consequences:** G2 supplies credible physical responses; G3
supplies matching constraints. Exact lane count, demand values and horizon are
later evidence-led choices.

### Candidate B — documented operational merge first

Use an observed site or a published empirical setting to anchor geometry,
demand, lane distribution and plausible congestion responses.

**Pros:** Offers operational grounding and physically plausible parameter
ranges; may reveal important mechanisms absent from a stylized task.

**Cons:** Data and calibration may be incomplete; several mechanisms and
nonstationary demand can complicate attribution and history matching.

**Dependencies/consequences:** Requires suitable primary evidence and a
reproducible observation/accounting contract. Field reconstruction is not
authorized.

**Accepted review approach: A, checked against B's evidence.** Keep the
all-stream objective and guardrails already accepted; use supporting throughput,
queue and service measurements to explain the mechanism rather than replace an
unfavorable primary result.

## RMD-G5 — derivative meaning

**Problem statement:** What derivative can the surviving mechanism support,
and how could its direction be useful for metering?

**Assumed model-chain function:** Meter parameters influence released traffic,
merge-state evolution, realized flows, queue trajectories and the objective.
Events or stochastic interactions may affect this path.

**Core gap:** No equations, event treatment or derivative estimator has been
selected. A differentiable forward approximation is insufficient evidence of a
correct or useful derivative.

### Candidate A — deterministic or piecewise-smooth sensitivity first

For a defensible deterministic model, identify continuous dependencies and
active-event boundaries. Plan independent derivative checks in stable regimes,
with explicit boundary diagnostics and reference evaluation of small control
perturbations.

**Pros:** Gives an interpretable path and local correctness tests; can distinguish
physical sensitivity from numerical smoothing.

**Cons:** May fail to describe stochastic gap behavior or event changes;
piecewise derivatives need not predict finite operational interventions.

**Dependencies/consequences:** Requires G1–G4 to support the deterministic model.
Smoothing, clipping or freezing events cannot be adopted merely to obtain a
gradient.

### Candidate B — expected-outcome/event-aware sensitivity

If essential merge behavior is stochastic or discontinuous, review derivatives
of expected outcomes or justified event-aware estimators. State the probability
model, control coupling and estimator limitations.

**Pros:** Can represent variable gap and driver interactions; avoids claiming a
pathwise derivative where the relevant quantity is an expectation.

**Cons:** Adds variance, sampling and probability assumptions; existing
literature may not establish a usable estimator or its transfer value.

**Dependencies/consequences:** Requires a justified stochastic/event model and
distinct derivative-validation evidence. It is a methodological change to adopt,
not an automatic fallback.

**Accepted review approach: decide derivative adoption after the mechanism audit.** Prefer A if
the physical evidence supports it; do not force it onto inherently stochastic
behavior. Report a supported forward task without a completed gradient path if
that is the evidence boundary.

## RMD-G6 — evidence sequence and independent reference

**Problem statement:** What must the next review establish, and when should an
independent richer reference be selected?

**Assumed model-chain function:** Source evidence supports a mechanism; matched
task/model comparisons test consequential information; derivative checks test
mathematical sensitivity; independent intervention tests assess usefulness.

**Core gap:** Existing archives do not establish this complete chain for the
selected local ramp task. A theoretical certificate, published empirical
mechanism and a software model are different evidence products.

### Candidate A — staged review with separate claims

Draft RM8 around targeted predecessor/mechanism review, strong comparators and
candidate reference requirements. Then, if warranted and approved, formulate the
matched information-to-decision task and derivative/evaluation plan. Identify
documented reference families now; choose software and any execution later.

**Pros:** Exposes the weakest link early; distinguishes method feasibility from
validation; allows literature and static analysis to resolve a review question
without executing a simulator.

**Cons:** Requires later stages to complete the research plan; a forward-positive
result can still end with an unresolved gradient or reference gap.

**Dependencies/consequences:** The next proposal must state bounded deliverables,
coverage and stop rules. Reference choice follows the required phenomenon; no
SUMO installation or run follows from task approval.

### Candidate B — review the complete modeling and evaluation chain together

Draft a broader review seeking one published model/reference combination that
already supports local information, metering actions, derivatives and independent
validation.

**Pros:** May reveal a coherent research pipeline quickly; exposes interface and
transfer requirements together.

**Cons:** Sparse full-chain literature can cause a promising mechanism to be
dismissed prematurely; a ready-made pipeline may anchor model choice before the
minimum-information question is resolved.

**Dependencies/consequences:** Requires a wider scope and explicit separation of
published evidence from proposed bridges. It still authorizes review only.

**Accepted review approach: A.** RM8 should inventory every link, but its main
output should be mechanism/predecessor and comparator findings. Later adoption
and construction remain user-gated.

## Reopen and extension conditions

- If complete aggregate history identifies the proposed hidden state, revisit
  G2/G3's information claim; do not weaken the observer.
- If the preferred action changes only because delay or residual traffic was
  excluded, repair G4's scenario construction while preserving accepted
  accounting; otherwise report no supported action distinction.
- If evidence requires stochastic/event physics, revisit G5 before adopting
  smoothing or a derivative estimator.
- If the mechanism requires another actuator or several controlled ramps to
  exist, reopen task selection; Candidate C is not authorized by that finding.
- At Candidate A closure, separately assess physical support, added information,
  decision relevance, gradient feasibility and independent-reference readiness.
  Only then discuss whether the result justifies a Candidate C proposal.

## Current allowed action

Initial planning decisions and RM8 family admission are closed. UG3.B resource
adoption is recorded; read the
[active RM9 observer gate](../reporting/rm9_50_separate_resource_findings_and_observer_gate.md).
Discuss UG4 before adopting speed/observation semantics. No simulator,
implementation, experiment or multi-ramp extension is open.
