# Ramp metering background for RMD-G1

Date: 2026-10-01. Status: explanatory background; model/control adoption remains open.
Parent: [post-selection design inventory](rm7_post_selection_design_inventory.md).

## 1. What ramp metering controls

A ramp meter regulates admission from an on-ramp to a freeway. For this review,
the proposed actuator is its commanded release rate, subject to ramp demand,
meter bounds and physical merge feasibility. It does not directly prescribe
mainline vehicle speeds, routes or lane changes.

Operational objectives can differ: limiting congestion, managing ramp queues,
smoothing admission and improving safety. Our approved local task evaluates
all-stream time/delay through common clearance; safety/feasibility and spillback
are guardrails. A controller that regulates mainline conditions is not, solely
for that reason, optimal for that complete objective.

Agency taxonomy separates time-based versus traffic-responsive operation, local
versus coordinated coverage, and release configuration. These are different
axes, rather than one mutually exclusive algorithm list.
[FHWA primer, §§1.8–1.10](https://ops.fhwa.dot.gov/publications/fhwahop14020/sec1.htm).

## 2. Established method families and their roles

The source-backed lineage includes:

- Pre-timed/time-of-day plans and local or system-wide traffic-responsive
  control. HERO is a coordinated strategy built around ALINEA.
  [FHWA primer](https://ops.fhwa.dot.gov/publications/fhwahop14020/sec1.htm).
- Demand/capacity rules, multi-input fuzzy control, queue management and
  single/multiple-vehicle or staggered releases.
  [FHWA handbook, §§5.3.3–5.3.6](https://ops.fhwa.dot.gov/publications/ramp_mgmt_handbook/manual/manual/5_1.htm).
- ALINEA's local feedback lineage: downstream detector occupancy regulates
  admissions.
  [Original ALINEA paper](https://onlinepubs.trb.org/Onlinepubs/trr/1991/1320/1320-008.pdf).
  A density-based implementation explicitly uses integral action and saturation.
  [Schmitt et al., §5.1, eq.13](https://arxiv.org/pdf/1611.06766).
- PI-ALINEA addresses feedback from a distant downstream bottleneck; its results
  are conditional on the studied geometry and tuning.
  [Authors' institutional abstract](https://sndbx.library.tuc.gr/view/49548?locale=el&show=full).
- Model-based optimal control and MPC: Reilly et al. optimize metering with a
  discrete adjoint and separately assess a repeated state-estimation/replanning
  loop.
  [Reilly et al., §§5.2–5.3](https://jackdreilly.github.io/papers/adjoint.pdf).

This is an orientation to established families, not a deployment-prevalence
ranking or an exhaustive review. Learned policies and robust/adaptive
optimization are additional research families, but they need not define the
initial local task. A learned policy is still a mapping from observations to
meter commands; its use does not by itself establish a different physical
actuator or information requirement.

## 3. The original two formulations and the missing third

The following are reviewer-proposed task definitions, not equations adopted
from one paper.

### RMD-G1.A — optimize a common open-loop rate schedule

Choose a bounded metering-rate value for each declared control interval over a
horizon, or a small set of coefficients defining that schedule. Given initial
information and declared demand/forcing, predict all-stream outcomes and find
useful schedule perturbations.

The selected schedule is then applied without being recomputed from subsequent
mainline observations. A separate queue override or online rate update would
make the implemented scheme hybrid/closed-loop and must be declared.

The gradient target is the all-stream objective's sensitivity to schedule
values/coefficient changes. The path passes through demand-limited release,
merge response, mainline/ramp queues and terminal accounting.

A pre-timed plan is a baseline implementation of scheduled control. Optimizing
the schedule under a matched scenario is a research formulation; it should not
be confused with choosing a historical fixed-time plan without optimization.

**Pros for the current review:** Identical interventions across models; direct
isolation of prediction and sensitivity errors; few controller-specific
assumptions.

**Cons:** A favorable open-loop distinction does not establish feedback benefit
or disturbance robustness. Forecast information and feasible release mappings
must be matched. If individual release timing is decisive, a continuous rate
alone may be an inadequate action description.

### RMD-G1.B — optimize a common feedback policy's parameters

Choose a controller family and a declared observation interface. At each update,
the controller maps measurements and internal memory to a bounded meter command.
Optimize its gains, targets or other declared parameters over shared scenarios.

For an ALINEA/PI-style controller, a provisional common interface is:

1. one declared mainline occupancy or density measurement in the merge/
   bottleneck region;
2. ramp queue length or a queue-detector proxy for storage management;
3. previous commanded/realized release and the controller's integral memory;
4. identical update timing and, if needed, identical filtering/delay assumptions.

This is a proposed comparator interface, not a frozen sensor layout. It is also
not the full strong aggregate observer: the baseline review must include models
with richer aggregate spatial/history information and forecasting where
appropriate.

Field detector occupancy means the fraction of a measurement interval during
which the detector is occupied. It is not the same quantity as the fraction of
vehicles occupying a lane. Occupancy-to-density conversion requires a declared
measurement model; a simulator's density cannot simply be relabeled as measured
occupancy. Keeping that distinction prevents accidental addition of lane
information or a mismatched feedback sensor.

The controller's regulation signal is the difference between its target and the
chosen measured mainline variable. In the proposed sign convention, excessive
mainline occupancy/density calls for reducing release; available ramp storage
can impose pressure to increase release. Feasibility can limit what is actually
released. How these objectives interact is part of the future controller
contract, not a justification to invent a queue-override law now.

The derivative target is sensitivity to controller parameters. It includes the
repeated loop: release changes traffic, traffic changes later observations, and
the policy changes later release.

**Pros:** Operationally interpretable; tests whether a traffic model can tune a
usable controller; allows explicit disturbance-response testing.

**Cons:** Controller architecture, measurements and tuning can confound traffic
representation. A small gain vector gives limited evidence for gradient scaling.
An integral/PI law can correct aggregate errors without representing the proposed
hidden state; that is an important sufficiency possibility.

### RMD-G1.C — repeated model-based rate optimization / MPC

At each update, estimate the current state from declared observations, forecast
future demand, optimize a finite-horizon rate schedule, apply only its first
portion, and repeat with new observations.

Operationally this is feedback. Its optimized variables are usually future
rates, however, rather than gains of a fixed PID/ALINEA policy. It therefore
combines properties of A and B and must be a distinct G1 candidate.

An MPC controller may use a PID/ALINEA controller at a lower level or share a
queue-management layer; labels alone do not determine its information or
derivative contract.

**Pros:** Direct connection between traffic prediction and control; explicit
constraints and anticipation; a strong aggregate competitor and a natural later
bridge to coordinated Candidate C.

**Cons:** Forecasts, state estimation and reoptimization can explain gains
independently of local resolution. Sensitivity of a predicted objective to a
planned rate sequence is different from sensitivity through the repeated
optimizer/closed-loop execution.

**Dependencies:** Shared observations/forecasts, feasible actions, objectives and
budget conventions must be explicit. Adoption requires a later decision;
recognizing MPC as established prior art does not open it as the active task.

## 4. PID and the proposed feedback signals

Yes: a PID controller that maps measured congestion error into a ramp release
command belongs to RMD-G1.B. For this task, the natural first candidate output is
mainline occupancy/density in the relevant merge or bottleneck region. A queue
controller is another possible feedback loop, with a different regulated output.

In ordinary control terminology:

- Proportional action reacts to the current error.
- Integral action accumulates persistent error.
- Derivative action reacts to how quickly the error changes.

Basic ALINEA is an integral controller. PI-ALINEA adds proportional action. A
full PID includes derivative action; it should not be called ALINEA without
specifying the change. Derivative action, measurement noise/filtering, delay,
bounds and integral windup require an explicit design if full PID is chosen.

A colleague's PID suggestion is therefore a coherent controller-family
candidate. It does not identify a complete ramp task until the measured output,
sensor location, target, gains, sampling, bounds, queue handling and objective
are specified. It also does not establish that all three PID terms are needed.

Provisional recommendation: use the published integral/PI lineage for the
initial feedback comparator, and consider full PID if evidence supports a
distinct benefit. No superiority claim is made.

## 5. Variants: reviewer assessment for the hidden-information question

The pros/cons below are reviewer inferences about this review's purpose.

| Variant | For the current question | Against / limitation | Proposed role |
|---|---|---|---|
| Fixed-time plan | Simple common intervention and reference | A weak plan cannot substantiate information necessity | Basic baseline |
| Demand/capacity rule | Direct aggregate receiving comparator | Capacity estimation and reactive observation may mask or confound the mechanism | Strong simpler-model family to inspect |
| Integral/PI/PID feedback | Tests correction from aggregate measurements; operationally interpretable | Gains, target and sensing can dominate; few parameters do not motivate scalable gradients | Feedback comparator / later tuning task |
| Multi-input rule/fuzzy policy | Tests whether several coarse signals already suffice | Controller flexibility adds attribution problems; derivative treatment may be awkward | Comparator if directly relevant |
| Open-loop rate optimization | Cleanest identical-action sensitivity comparison | No automatic feedback-robustness claim | Recommended initial analytic task |
| MPC | Strong predictive macro alternative; credible rate-gradient use | Forecast/estimation/replanning differences can mimic a resolution benefit | Required predecessor/baseline review; possible later control task |
| Coordinated multi-ramp control | Tests spatial coupling and larger gradient dimension | Storage allocation, fairness and forecasting obscure local mechanism | Deferred task Candidate C |
| Fine release timing / platoon pattern | Could expose temporal merge opportunity at equal mean rate | Changes the actuator resolution and may require event/stochastic analysis | Explicit boundary variant; reopen action contract before adoption |
| Learned policy | Can test flexible information use | Policy learning, training and generalization add another research question | Optional future comparator; not the first target |

Coordinated geography can use scheduled, feedback or MPC control. Release pattern
is another independent axis. A scalar rate and a release sequence need not encode
the same action. Fine timing must not be quietly introduced to force gap-state
value into a rate-control task.

## 6. What aggregate feedback can and cannot settle

If two scenarios have identical declared observation histories and identical
controller memory, a deterministic common feedback law issues the same current
command. Future observations may diverge and the controller can then react.
Thus feedback is not permanently blind merely because the present state is
ambiguous.

The relevant comparison is whether extra information improves anticipation,
action ranking or all-stream outcomes beyond what strong aggregate feedback or
MPC can recover. Giving one controller lane/gap observations while keeping the
other on coarse totals is a sensor-plus-model intervention. It must be separate
from comparing traffic models under a common controller-information interface.

There are therefore two research axes:

1. better traffic-model prediction/sensitivity under a common action and
   observation contract; and
2. better policy decisions because extra observations are supplied.

Our first task should isolate the first axis. A positive result does not
automatically establish the second. PID's integral memory is itself a reason to
use a strong history-aware aggregate baseline rather than a snapshot observer.

## 7. Provisional position after this clarification

Retain A as the initial task: local rate perturbations/schedule optimization,
with common feasible actions, demand and complete accounting. Review integral/
PI feedback and aggregate MPC as substantial competitors, not merely no-control
or pre-timed plans.

Add RMD-G1.C explicitly to the living inventory. Keep full PID as a B subvariant
and fine release patterns as a scope boundary requiring discussion. The physical
task A and deferred coordinated task C selected at RMT-R1 are unchanged.

This clarification is not the RM8 predecessor/mechanism review. It supplies G1
background and corrects the candidate inventory before a bounded RM8 proposal.


## Subsequent user choice

The user approved open-loop rate optimization to prioritize gradient correctness
and independent one-step usefulness. PID/feedback and MPC remain background and
unselected primary-task alternatives. See the
[continuation record](../discussion/rm7_open_loop_approval_and_rm8_opening.md).
