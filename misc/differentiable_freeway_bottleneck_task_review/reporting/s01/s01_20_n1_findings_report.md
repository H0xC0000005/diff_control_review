# S01.20 — N1 scientific findings report

Sprint: [S01](../../00_review_sequence.md#s01) · Role: 20 findings / decision evidence · Predecessor: pre-review handoff · Gate: N1 user gate.

Date: 2026-09-16  
Status: **N1 candidate A accepted after clarifications; explanatory evidence
record; N2 protocol drafting authorized, review execution not yet authorized**

## 1. Executive interpretation

The literature does not support a broad claim that freeway bottleneck control
needs a mesoscopic or microscopic differentiable simulator. It supports a much
narrower, testable possibility:

> For infrastructure speed advice upstream of a fixed lane reduction, an
> aggregate model may represent the basic inflow-regulation mechanism, yet omit
> compliance composition and lane-specific merge pressure that could change the
> ranking of candidate speed-control actions in a richer traffic system.

This possibility is worth a full review because three evidence streams meet:

1. simple aggregate models already produce effective lane-drop VSL control, so
   there is a serious lower-resolution baseline rather than a straw man;
2. field and modeling studies show that compliance, vehicle composition,
   lane-specific sensing, and mandatory lane changes affect realized response;
   and
3. no reviewed study closes the complete chain from model resolution, through
   derivative correctness, to downstream usefulness of the resulting gradient
   in an independent richer evaluator.

The review therefore does **not** recommend “build a lane-level differentiable
simulator.” It recommends investigating whether a controlled progression from
homogeneous aggregate state to compliance classes and then lane groups changes
control rankings enough to justify the extra state.

Coordinated ramp metering did not reveal the same opening. Strong aggregate,
multiclass, feedback, adjoint, and nonlinear-model/MPC approaches already cover
the primary action and major operational constraints. N1 found no decision-
grade evidence that vehicle order or lane-scale state is the missing variable
for coordinated-meter decisions at the fixed lane reduction. That is a negative
finding about its fit to this research question, not about ramp metering's
operational value.

Throughout this report:

- **Established** means directly supported by inspected decision-grade sources.
- **Inference** means an N1 synthesis across those sources.
- **Proposed adaptation** is a model or experiment design for a possible later
  study; it is not a literature finding and is not approved for implementation.

## 2. What the literature establishes

### 2.1 The first-order aggregate mechanism is real and already strong

**Established.** Jin and Jin formulate VSL control at a lane-drop bottleneck in
both an LWR kinematic-wave model and a much simpler link-queue model. In their
capacity-drop setting, a constant open-loop speed limit does not reliably avoid
the stable congested state, while integral and proportional-integral feedback
can regulate density around the desired uncongested state. They report that the
controller developed in the link-queue model transfers to their LWR model. They
also find no performance gain from VSL when the modeled capacity drop is zero.
[FB0001](https://arxiv.org/abs/1310.2658)

This has two consequences for the review:

- the homogeneous link-aggregate model is a credible B0 baseline; and
- a study must verify and calibrate a capacity-drop mechanism rather than assume
  that every lane closure creates a controllable VSL benefit.

**Established.** Delle Monache, Piccoli, and Rossi pose speed limit as a bounded-
variation control in an LWR/Newell-Daganzo model, derive cost variations under
needle perturbations, and compare a gradient method with instantaneous and
random-exploration policies. Their case is a free-flow, single-road outflow-
tracking problem—not the proposed lane-closure task—but it establishes that
first-order VSL gradient optimization itself is prior art.
[FB0002](https://arxiv.org/abs/1603.04785)

**Inference.** Neither differentiability nor successful aggregate VSL control
is the contribution available here. Any later contribution must concern what
retained information is needed for gradients that remain useful outside the
model that generated them.

### 2.2 Compliance matters, but does not by itself require microscopic vehicles

**Established.** The macroscopic VSL literature can represent changes in free
speed, critical density, capacity, and incomplete compliance without tracking
individual vehicles. Frejo et al. explicitly construct such a macroscopic
model and discuss field calibration and compliance limitations.
[FB0003](https://doi.org/10.1016/j.ifacol.2018.07.056)

**Established.** In the Caltrans/PATH voluntary speed-advisory field experiment,
the morning evaluation reported higher vehicle miles traveled, lower vehicle
hours traveled, and higher effective throughput; the afternoon result was less
conclusive. The report also documents changing compliance and notes that actual
speeds could remain above the advice near the bottleneck. The study is valuable
operational evidence but is not a fixed lane-closure experiment and does not
isolate model resolution.
[FB0005](https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/final-reports/ca18-2447-finalreport-a11y.pdf)

**Established.** FHWA guidance treats work-zone VSL as an upstream speed-
harmonization measure, emphasizes whether signs are advisory or regulatory, and
recommends lane-specific speed and volume sensing. It also makes clear that sign
placement, update frequency, enforcement, and jurisdiction constrain the real
actuator.
[FB0011](https://ops.fhwa.dot.gov/publications/fhwahop21021/fhwahop21021.pdf)

**Inference.** The first extra information to test should be continuous mass by
compliance/response class, not individual identity. A homogeneous model can
mistake the displayed speed for the realized population response, while a
multiclass aggregate model can test this omission at much lower complexity than
a microscopic simulator.

### 2.3 Lane and lateral-transfer effects are the strongest candidate gap

**Established.** Guo et al. argue that mandatory lane changes near a lane drop
can limit or eliminate the benefit of VSL-only control. Their prediction model
is a lane- and class-resolved CTM with aggregate lane-change transfers; their
controller jointly chooses lane-specific speed limits and lane-change counts in
an MPC framework and evaluates the result in SUMO. This directly supports the
claim that lane distribution and lateral-transfer feasibility can matter. It
does not isolate their value for speed advice because lane-change commands are
also control variables, all vehicles are assumed to be CAVs, and optimization
uses a genetic algorithm rather than traffic-model derivatives.
[FB0004](https://doi.org/10.1109/ACCESS.2020.2981658)

**Established.** Ko et al. use a microscopic mixed-traffic setting for a highway
lane closure and separately train CAV speed-harmonization and merge-control
policies. Their results show that mobility, throughput, and fuel outcomes need
not favor the same action and that merge control can dominate parts of the
mobility result. Because the actuator is vehicle-specific CAV behavior and the
study bundles speed and merge control, it is boundary evidence rather than a
model for the proposed infrastructure-advisory task.
[FB0010](https://doi.org/10.1049/iet-its.2019.0709)

**Supporting only.** Seliman, Sadek, and He report a lane-group VSL study using
a macroscopic controller and microscopic evaluator, but N1 obtained only its
abstract/metadata. It is a highly relevant direct-predecessor lead for the next
review, not decision-grade support for superiority or novelty.
[FB0013](https://doi.org/10.1061/JTEPBS.0000395)

**Inference.** The evidence justifies testing lane-group state; it does not
justify assuming that lane-group state will improve gradients. It also does not
justify exact vehicle order, explicit gaps, or controlled lane-change maneuvers.
Aggregate lane mass, class composition, and lateral transfers are the smallest
currently defensible extension.

### 2.4 Advisory VSL, regulatory VSL, and direct CAV speed control are different tasks

**Established.** The reviewed studies span at least three actuators:

1. a posted or advisory infrastructure speed applied to a road segment;
2. a lane-specific speed command under connected/automated assumptions; and
3. direct vehicle-specific target speeds or moving actuators.

The second and third can assume much stronger observability and compliance than
the first. Recent work can represent CAV penetration and traffic-composition
uncertainty in a macroscopic extended LTM, showing again that “mixed traffic”
does not automatically require microscopic state.
[FB0007](https://arxiv.org/abs/2607.16615)

**Inference.** These actuator families cannot be pooled as evidence for one
control task. The proposed F1 task should remain infrastructure advice with
explicit response classes. Direct CAV commands may be a later boundary or
sensitivity study, not a substitute for compliance modeling.

### 2.5 Temporary closure recovery changes how outcomes must be measured

**Established.** The incident-management study archived as FB0006 simulates a
severe temporary blockage and finds that ramp-control effects during the active
incident can differ from effects after the blockage clears; an important part
of the benefit appears in faster recovery. This makes the post-reopening period
material to evaluation.

**Inference.** A controller must not receive credit merely for moving traffic
mass or delay beyond the chosen horizon. Temporary-closure cases need a common
post-reopening horizon, a queue-clearance criterion, and a terminal residual-
queue term or equivalent accounting.

### 2.6 Ramp metering already has a mature lower-resolution control stack

**Established.** The reused RM0024 study applies a discrete adjoint to a
first-order freeway network for coordinated ramp metering and checks gradients
against finite differences. RM0025 extends exact active-branch discrete-
adjoint reasoning to multiclass networks with merges, diverges, and buffers.
These are direct derivative baselines, not merely claims that the simulator is
differentiable.

**Established.** Recent alternatives include fairness-aware decentralized
ALINEA evaluated in calibrated SUMO and a data-driven nonlinear dynamics model
embedded in coordinated MPC and compared with ALINEA, PI-ALINEA, and DMD-MPC.
[FB0008](https://arxiv.org/abs/2601.06311),
[FB0009](https://arxiv.org/abs/2503.06767)

**Established.** FHWA guidance already frames finite ramp storage, queue
override, release-rate constraints, mainline objectives, and spillback as core
ramp-metering design concerns.
[FB0012](https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/5_1.htm)

**Inference.** F2 has strong aggregate and multiclass models, correct-gradient
methods, feedback baselines, and richer evaluators. N1 did not find evidence
that preserving vehicle order or lane state is the missing requirement for its
control decision. A new task could still be motivated by a specific storage,
fairness, or arterial-coupling question, but that would not yet be a selective-
discreteness result.

## 3. Important gaps not closed by the reviewed literature

### Gap 1 — No matched resolution ladder for one fixed speed-advisory task

The literature compares many models and controllers, but N1 found no study that
holds the disturbance, action space, objective, demand, horizon, and evaluator
fixed while adding information in this order:

- B0: homogeneous link aggregate;
- B1: link aggregate with compliance/response classes; and
- B2: lane groups with class mass and aggregate lateral transfer.

Without this controlled ladder, better performance by a richer method may come
from a different actuator, optimizer, calibration, objective, or controller—not
from the added state.

### Gap 2 — Forward fidelity is rarely separated from gradient usefulness

Existing work can show good traffic prediction, successful internal
optimization, or agreement between an analytic/adjoint gradient and finite
differences. Those answer different questions. N1 found no direct evidence that
the gradient from a richer lane/compliance model more reliably ranks feasible
speed-advisory perturbations when those same perturbations are replayed in an
independent microscopic traffic model.

This is the central unresolved question. A model could have lower forward error
yet produce no better control direction, or produce a useful local ranking even
with imperfect trajectory-level fidelity.

### Gap 3 — The actual B0 failure has not yet been demonstrated

Lane-changing and compliance are plausible mechanisms, but the review has not
yet produced a matched counterexample in which B0 chooses or ranks an action
incorrectly and B1 or B2 repairs the error. The next review must search for or
construct evidence for such a contrast before implementation is warranted.

Examples of candidate contrasts—not established results—include:

- equal total density but different compliant/noncompliant composition;
- equal total density but different lane occupancy upstream of the closure;
- the same displayed advice but different ability to complete mandatory merges;
- temporary reopening with equal current queue mass but different lane/class
  distribution and therefore different clearance response.

### Gap 4 — Compliance dynamics and calibration are underspecified

Field evidence shows that compliance can vary by time and location. The
literature does not give N1 a single accepted mapping from displayed advice to
class-specific realized speed, nor a settled rule for class transitions,
reaction delay, habituation, or enforcement. Treating compliance as a static
percentage may be enough for B1, but this must be tested rather than assumed.

### Gap 5 — Lane-transfer feasibility is often entangled with lane-change control

The clearest lane-resolved paper jointly optimizes VSL and lane-change counts.
That makes it difficult to determine whether lane state helps predict response
to speed advice or whether the gain comes from the added lane-change actuator.
A selected F1 study must keep lateral transfer as traffic behavior/state while
holding lane-change commands outside the action space.

### Gap 6 — Cross-fidelity fairness is not standardized

The aggregate model and microscopic evaluator must share population, demand,
closure schedule, controllable signs, objective accounting, and horizon. Their
fundamental diagrams, capacity drop, compliance response, and jam storage must
also be calibrated consistently enough that a ranking disagreement reflects
resolution rather than incompatible base traffic physics. The literature offers
ingredients but no ready-made fairness contract for this exact comparison.

### Gap 7 — Separate deterministic kinks from probability shifts and hybrid events

**User clarification recorded after the N1 gate:** the existing meso project
deliberately keeps traffic mass continuous and structural/scenario information
fixed during differentiation to avoid moving probability mass and saltation
problems. The freeway review should prioritize the same avoidance principle,
without assuming that its eventual equations must copy the urban stack.

Two distinct issues must not be conflated:

- **Deterministic piecewise-differentiable constraints:** continuous traffic mass
  is transferred through time-discrete sending/receiving, storage, and bounded-
  service operations. Changes in the active branch can create kinks. These need
  branch-aware derivative checks, but do not by themselves imply a stochastic
  probability-shift estimator or saltation correction.
- **Additional stochastic or hybrid sensitivity:** a control-dependent discrete
  choice changes the probability assigned to categorical outcomes; separately,
  a genuinely discontinuous hybrid transition can introduce sensitivity through
  its event time or reset. These are not ordinary constraint kinks. They can
  require extra gradient terms, approximations, and validation; stochastic
  estimators can additionally introduce structural bias-variance tradeoffs.

**Default restriction:** avoid the second category in the differentiable
candidate. Prefer fixed exogenous compliance cohorts, deterministic continuous
lateral mass fluxes, and fixed closure/reopening schedules. Continuous traffic
mass moving between lanes is not, by itself, probability mass shifting between
sampled outcomes. Fixed random seeds also do not make a control-dependent
categorical distribution parameter-independent.

If a candidate requires control-dependent discrete sampling or a hybrid
transition requiring event-time/saltation treatment, stop and explicitly reopen
the derivative contract. Such a process is admissible only after evidence shows
that no adequate continuous/deterministic alternative closes a decision-relevant
gap, followed by user approval of the smallest extension. Its work must include
dedicated gradient-fidelity tests under the relevant probability shifts or
event changes, and documented approximation error and estimator bias/variance
where applicable. It must not be hidden by fixed-seed comparisons, smoothing,
or checking only trajectories away from the affected transitions.

Capacity-drop formulations require particular scrutiny: a continuous kink and
a state-triggered discontinuous discharge jump have different derivative
contracts. N1 has not approved either a hybrid capacity reset or its gradient
treatment. The full B2 derivative contract remains open.

### Gap 8 — Novelty remains qualified

Lane-group VSL, multiclass CTM, microscopic evaluation, and VSL optimization all
exist. Their combination is not automatically novel either. The recommendation
has **one central candidate contribution**, not a portfolio of separate novelty
claims:

> Establish which minimum retained information, if any, changes useful
> infrastructure speed-advisory gradient/action rankings in a matched richer
> evaluator, and identify the conditions under which the simpler model suffices.

Compliance and lane groups are successive explanatory variables in that study.
Derivative checks, calibration, and recovery accounting make the evidence
credible; they are not independently claimed inventions. A new equation or
estimator is not a prerequisite and must not become a way to rescue weak
task-level novelty.

#### Priority within the recommended next full review

These are priorities for evidence review and protocol planning, not permission
to start experiments or a new implementation sequence.

| Priority | Question addressed | Related gaps | Role and stop implication |
|---|---|---|---|
| P0 — direct-predecessor veto | Has prior work already answered the substantive resolution-to-useful-sensitivity question? | Gap 8 | Inspect lane-group/multiclass VSL and gradient/cross-fidelity predecessors first. Different notation, one extra class, or a new site is not enough novelty. |
| P1 — decision gap and evaluator feasibility | Is there a supported B0 ranking-failure mechanism under the same speed-advisory actuator, and can it be judged fairly in an independent evaluator? | Gaps 3, 6; actuator boundary | Establish motivation and a plausible shared traffic/calibration contract before detailed architecture. If either cannot be justified, stop or refine the task. |
| P2 — isolate the minimum information | Can the gap be tested by B0 homogeneous aggregate, then B1 fixed compliance cohorts, then B2 lane groups/endogenous continuous lateral transfers? | Gaps 1, 4, 5 | Keep primary actions matched. Do not assume B2 is necessary; B0/B1 sufficiency is admissible. |
| P3 — derivative admissibility and correctness | Can each candidate use a declared deterministic continuous-mass derivative path with reliable reference checks? | Gap 7 | Apply the user's probability-shift/saltation avoidance restriction as an early admissibility screen, then specify checks for the chosen equations. |
| P4 — downstream usefulness evidence | What matched perturbation/ranking test establishes benefit outside the candidate model? | Gap 2, with Gap 6 | Freeze common actions, population, objective, recovery horizon, paired evaluator scenarios, and acceptance evidence. Internal descent alone cannot close this question. |

P0 and P1 are the first inexpensive kill gates. Evaluator/calibration feasibility
and the Gap 7 admissibility restriction are screened early, not postponed until
after model construction. P2-P4 specify one coherent evidence chain, and all
must be resolved sufficiently before implementation could be proposed.

#### Inside the recommendation but not standalone novelty claims

- Reusing or minimally adapting first-order propagation, capacity drop,
  multiclass response, and aggregate lane transfers.
- Numerical derivative verification and explicit deterministic kink handling.
- Common calibration, matched controls/objectives, and microscopic evaluation.
- F4 reopening recovery as a required test condition, not a new control family.
- Evidence for simpler-model sufficiency or equivalence in a declared domain.
  This can be informative, but publication-level novelty is not guaranteed by a
  negative result alone.

#### Outside the recommended next step

- Inventing new VSL/MPC optimization, car-following, lane-changing, or
  capacity-drop theory merely to obtain a method novelty claim.
- Developing stochastic categorical gradient estimators or saltation methods;
  these require a separately justified and approved exception under Gap 7.
- Direct vehicle-specific CAV control, F3 joint ramp/VSL control, F5 controlled
  merging/lane changes, route choice, or closure scheduling.
- Crash-risk theory, a new general microsimulator, field deployment, or a
  network-wide operational-control study.
- Any simulator/controller implementation or scientific experiment. The
  immediate task is now the N2 full-review protocol proposal after the user's
  selection of F1; execution still requires separate approval.

A full review must inspect direct predecessors such as FB0013 deeply enough to
decide whether the central question is substantively unanswered. N1 has not
established an absence claim or approved a novelty-bearing model design.

## 4. Modeling that can be adopted or adapted

The following is a proposed evidence-based modeling ladder, not an approved
implementation specification.

### 4.1 B0 — homogeneous link-aggregate capacity-drop model

**Adopt:** the first-order LWR/LTM/link-queue idea from FB0001: continuous mass,
sending/receiving constraints, finite storage, and a calibrated capacity-drop
mechanism at the lane reduction.

**Modify for this goal:** use a spatial discretization sufficient to represent
multiple upstream sign zones and propagation delay. Keep the closure location,
affected lane group, and closure/reopening schedule structural and fixed.

**Why B0 is essential:** it is cheap, interpretable, and already capable of
producing effective VSL control. A richer model earns its place only by beating
this strong baseline on the matched downstream ranking test.

**Do not assume:** that capacity drop always occurs or has one universal value.
Include a no-drop/equivalence case and calibrated activation/recovery cases.

### 4.2 B1 — aggregate compliance/response classes

**Adopt:** multiclass continuous mass and class-dependent speed/capacity response
from macroscopic compliance and mixed-traffic models.

**Modify for this goal:** classes should encode response to the same posted
advice—for example compliant, partially responsive, and effectively
nonresponsive mass—rather than routes or microscopic identities. The exact
number of classes should be the minimum supported by calibration or sensitivity
evidence.

**State retained:** total and class mass by longitudinal cell, with class-
specific realized-speed or fundamental-diagram response. Total sending,
receiving, and storage remain shared conservation constraints.

**Probability-shift avoidance:** first treat class membership and initial class
mass as fixed exogenous scenario inputs. A class fraction represents a
deterministic population share, not permission to sample a control-dependent
driver choice. Endogenous categorical compliance switching would require a
separate justification and gradient contract under Gap 7.

**Question isolated:** does knowing who will respond, while still mixing lanes,
change useful control rankings relative to B0?

### 4.3 B2 — lane-group multiclass aggregate model

**Adopt:** the lane-subcell and aggregate lateral-transfer idea used in
multilane/multiclass CTM work such as FB0004.

**Modify for this goal:** remove lane-change counts from the control vector.
Lateral transfers should be endogenous realized traffic behavior constrained by
available target-lane supply/storage and the need to leave the closing lane.
Speed advice remains the only control.

Prefer deterministic continuous mass-transfer equations. Do not implement this
as sampled lane choices or discrete merge outcomes whose probabilities move
with the speed control without reopening Gap 7.

**State retained:** continuous class mass by longitudinal cell and lane group,
plus only the aggregate quantities needed to compute longitudinal sending,
receiving, and feasible lateral transfers. A practical first split is
continuing/open lanes versus the closing lane or affected lane group.

**Question isolated:** after compliance is represented, does lane distribution
and merge feasibility add enough information to improve action rankings?

**Do not add by default:** exact vehicle sequence, individual gaps, integer
vehicles, or explicit maneuver decisions. If B2 fails, the failure must be
diagnosed before proposing one of those additions.

### 4.4 Control parameterization

**Adopt:** bounded piecewise-constant speed targets over time and upstream sign
zones, with physically/operationally justified update intervals.

**Accepted matched-action clarification:** B0, B1, and B2 share the same
link-level speed-advisory schedule and feasible action set in the primary
comparison. B2 applies that shared schedule to its lane groups. Lane-specific
actions are a separate, unapproved extension/ablation, because changing state
and action together prevents attribution to retained information.

**Constraints:** minimum/maximum display speed, bounded change between updates,
and possibly spatial consistency between adjacent signs. The accepted primary
task is infrastructure advice; transferring the study to regulatory limits
requires an explicit actuator/response-contract amendment, not an implicit
change of terminology.

**Quantization:** optimize a continuous relaxation for gradient testing, then
evaluate rounding to allowed sign values separately. Do not silently
differentiate through a discrete display choice.

### 4.5 Objective and horizon

**Primary common accounting:** total time spent or total delay over the same
population and horizon, with bottleneck outflow and queue-clearance time
reported separately.

**Temporary closures:** continue through reopening to a declared clearance
horizon; account for terminal residual queue if full clearance is not reached.

**Guardrails rather than hidden penalties:** speed variation, minimum commanded
speed, abrupt-control changes, emissions, or safety surrogates should be
reported or constrained explicitly. They should not be mixed into one weighted
objective without a separate decision about interpretation.

### 4.6 Derivative construction and correctness checks

**Adopt:** differentiate the actual time-discrete B0/B1/B2 update used for
optimization, either with reverse automatic differentiation or a discrete
adjoint. Declare closure topology, lane permissions, class definitions, and
scenario schedules nondifferentiated structural metadata.

**Checks:** use double-precision central directional finite differences on small
fixed cases away from known branch changes; record active sending/receiving,
capacity-drop, control-bound, and lateral-transfer branches. Test multiple step
sizes rather than one apparent match.

**At event boundaries:** report one-sided behavior, directional instability, or
an exclusion band. Do not add smoothing merely to make a gradient exist; any
smoothing changes the model and needs an explicit comparison with the original
nonsmooth dynamics.

These local checks concern the declared deterministic discrete model, not a
blanket solution for stochastic probability shifts or hybrid event-time/reset
sensitivities. Under Gap 7, those processes are avoided by default and require a
separately justified, user-approved extension and dedicated fidelity evidence.

### 4.7 Independent richer evaluator

**Adopt:** an independent microscopic platform such as SUMO with car-following,
lane-changing, vehicle/compliance classes, fixed closure schedule, and fixed
random seeds. FB0004 and FB0010 demonstrate that this evaluation family is
feasible.

**Modify for scientific separation:** the microscopic model should evaluate
actions, not supply gradients to B0/B1/B2. It should receive the exact same sign
schedule and objective accounting. The evaluator's stochastic replications must
be paired across candidate perturbations so noise does not masquerade as a
ranking reversal.

**Calibration hierarchy:** first align uncongested speed/flow, congestion wave
behavior, storage, bottleneck discharge/capacity drop, and recovery. Then align
compliance and lane distribution. Do not tune each candidate model separately
to favor its own control.

### 4.8 Strong baselines and ablations

At minimum, a later experiment would need:

- no control;
- the analytical/feedback I or PI VSL family motivated by FB0001;
- direct or derivative-free optimization on the same low-dimensional control
  parameterization, to separate gradient failure from objective difficulty;
- B0, B1, and B2 using matched optimization budgets; and
- state/action ablations that add compliance state before lane state and do not
  introduce lane-specific action at the same time unless separately labeled.

## 5. Modeling that should not be copied directly

- **Joint VSL and lane-change optimization from FB0004:** useful evidence and a
  useful lane-resolved state template, but it changes the action and assumes all
  CAVs. Copying it would prevent attribution to representation.
- **CAV DQN speed/merge control from FB0010:** useful as a richer behavior
  example, but it combines vehicle-specific control, reinforcement learning,
  and merge priority. It is not an infrastructure-advisory baseline.
- **A deliberately weak aggregate model:** B0 must include the task's calibrated
  capacity-drop and storage behavior. Otherwise a B2 advantage says little.
- **Microscopic state inside the differentiable candidate by default:** the
  richer simulator belongs first on the evaluation side. Adding gaps or vehicle
  order before B2 is falsified would abandon the minimum-information question.
- **A single internal optimization-success result:** a falling model objective
  establishes neither derivative correctness nor downstream usefulness.
- **Unreported smoothing, clipping, or control rounding:** each can change the
  physics, active set, or gradient and therefore requires explicit treatment.

## 6. The concrete scientific hypotheses now visible

The full review, if authorized, should try to reject these in order:

1. **H0/B0 sufficiency:** a calibrated homogeneous aggregate model ranks useful
   infrastructure speed-advisory perturbations as well as B1/B2 when evaluated
   microscopically.
2. **H1/compliance value:** if B0 fails, aggregate response classes explain and
   repair the material ranking failures without lane state.
3. **H2/lane-group value:** if B1 still fails, lane-group mass and feasible
   lateral transfer explain and repair the remaining failures.
4. **H3/no need for deeper discreteness:** exact vehicle order/gaps are not
   justified unless a repeatable B2 failure is tied specifically to their
   omission.

Possible outcomes are all meaningful:

- **B0 sufficient:** negative result for added resolution; use the simpler model.
- **B1 sufficient:** compliance heterogeneity matters, but lane resolution does
  not earn its cost.
- **B2 improves transfer:** lane-group state is the minimum supported addition.
- **None transfer reliably:** differentiable first-order control directions may
  not be useful for this task, or the evaluator/calibration contract is
  inadequate.

## 7. What the next full review must decide before implementation

1. Is there a decision-grade direct predecessor that already compares matched
   model resolutions and cross-fidelity gradient/action rankings?
2. Can at least one controlled B0 failure case be supported without bundling a
   new actuator?
3. What is the minimum defensible compliance-class model and calibration data?
4. What lane-group/lateral-transfer formulation preserves mass and remains
   differentiable enough for the declared derivative checks?
5. Can B0/B1/B2 and the microscopic evaluator be calibrated to a common traffic
   contract rather than separately tuned worlds?
6. What exact action parameterization allows fair state ablations?
7. What event-boundary policy and gradient acceptance tolerances are credible?
8. What empirical or simulation evidence would be strong enough to claim
   improved downstream gradient usefulness rather than site-specific tuning?

Question 7 must first screen out control-dependent categorical probability
shifts and hybrid transitions requiring saltation/event-time corrections. If
either proves indispensable, the review must document why continuous or
deterministic alternatives fail and request approval of the additional modeling
and gradient-fidelity work before proceeding.

Failure to answer Questions 1, 2, or 5 should stop the task before simulator
implementation. The present N1 evidence supports a full review of those
questions, not a presumption that B2 or any mesoscopic model will win.

**Current next-step boundary:** the user selected candidate A. The proposed
[`Historical N2 protocol proposal`](../../archive/planning/n2_phase_A_protocol_proposal.md)
reviews direct-predecessor novelty, strong-baseline decision gaps, and early
evaluator/Gap 7 feasibility, then stops at N2-UG1 for a scientific routing choice.
The questions above span the eventual full review; N2-UG1 does not approve their
detailed equations, calibration, or experiment contracts. N2 execution awaits
protocol approval.
