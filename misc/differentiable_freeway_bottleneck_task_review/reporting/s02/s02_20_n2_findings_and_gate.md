# S02.20 — N2 findings and user gate N2-UG1

Sprint: [S02](../../00_review_sequence.md#s02) · Role: 20 findings / decision evidence · Predecessor: S01 · Gate: N2-UG1.

Date: 2026-09-16; decision update 2026-09-17.
**N2-R1/R2/R3 delivered; N2-UG1 Route B approved; follow-on plan approved.**
Route B review has reached its [next-evidence gate RB-UG1](../s03/s03_20_rb_findings_and_gate.md).
Its one-paper access request is resolved; the user closed that sprint and approved
Option A diagnostic planning. No diagnostic execution or model construction is approved.
[Route B closure](../s03/s03_99_rb_sprint_closure.md).
Candidate A and the approved review protocol remain accepted. No experiment,
calibration, model selection or implementation is authorized by this report.
The discussion below preserves pre-decision recommendations and hypotheses;
the route approval in section8 supersedes their pending-route status only.

## 1. Bottom line

The literature leaves a plausible minimum-information question, but does not
yet justify committing to the compliance-first B0 → B1 → B2 ladder. My
provisional recommendation is **Route B: a bounded contrast/contract refinement**
before detailed model design. Start with a credible response-aware aggregate
baseline and a fair advice/evaluator contract; require motivation for one
omitted-information contrast before planning richer models.

This is not a finding that richer state is unnecessary. The missing evidence is
whether losing response composition or lane occupancy changes the ranking of
feasible speed-advice interventions, rather than merely reducing prediction
accuracy. Current evidence supports mechanisms and forward modeling much more
strongly than that decision claim.

## 2. Supplied files verified

Both filenames identify the requested final published papers. All pages parse
and contain extractable text; neither PDF is encrypted. FB0021 includes Appendix A.
Title, authors, DOI and journal identity match the access request. This verifies
document identity/readability and supplied completeness, not publisher-byte
authenticity against an unavailable publisher checksum.

| File | Pages / bytes | SHA256 |
|---|---|---|
| [FB0013](../../archive/user_supplied/FB0013.pdf) | 15 / 2,341,929 | `e47da1bb385685bd9529a3e9671423cb3c8791b4d9fbf5c283698a8053b76e3f` |
| [FB0021](../../archive/user_supplied/FB0021.pdf) | 21 / 2,852,395 | `6ad00928a6a2516afae34cdb58971cea49f7cef4cc885651ff06467d5f790ee5` |

Batch 1 is resolved. Both papers were inspected through their results and
conclusions, not just their abstracts. No second paper-access request is pending.

## 3. Key predecessor findings

### Lane-group VSL: the closest paper is not a state-resolution ladder

FB0013 first optimizes a homogeneous METANET schedule, then seeds and
reoptimizes PSO within VISSIM. Its lane-group case principally adds lane-group
speed actions; another case also bans rightward lane changing. It does not
compare aggregate versus lane-group METANET under identical actions.

Table 2 reports stops per vehicle of 9.43 without control, 8.46 for the METANET
schedule, 5.00 for link-wide VISSIM reoptimization and 4.81 for lane-group
VISSIM reoptimization. The advertised 48.99% improvement is against no control;
lane-group versus reoptimized link-wide control differs by 3.8%. Moreover,
METANET minimizes density discrepancy whereas VISSIM minimizes stops subject
to constraints. Thus its macro-to-micro improvement cannot establish a
state-information-only failure. The strong link-wide result is important
counterevidence to assuming lane-specific control is necessary.
[Source](https://doi.org/10.1061/JTEPBS.0000395),
[full audit and locations](../../extraction/n2_source_studies/FB0013.md).

### Severe temporary bottlenecks: recovery and analytical sensitivity already exist

FB0021 develops aggregate kinematic-wave speed control for incident/work-zone
bottlenecks. It explicitly restores capacity when the event ends and computes
delay through complete queue clearance. Its analytical sensitivities identify
competing queue-clearing and discharge benefits; capacity overestimation can
reactivate congestion. These are substantial predecessors for recovery and
sensitivity, not microscopic gradient-transfer validation. Its moving speed-
activation fronts and idealized response are not our fixed-zone advisory
implementation. We should reuse its accounting/reference logic, not claim
reopening accounting or speed sensitivity alone as novelty.
[Source](https://doi.org/10.1016/j.trc.2014.10.015),
[full audit](../../extraction/n2_source_studies/FB0021.md).

### A strong aggregate model can already represent imperfect response

FB0026, the fuller 2019 extension of FB0003, calibrates a homogeneous METANET
response model to A12 field data. It varies advice/limit-induced free-flow
speed, critical density and capacity with a scalar noncompliance parameter;
it does not require fixed driver classes. Its uncongested VSL comparison
reports mean relative speed errors of 12.84%, 30.08% and 9.29% for the three
response formulations. These are forward response-law results, not action-
ranking or gradient comparisons. They rule out treating full instantaneous
obedience as a credible universal B0.
[Source](https://doi.org/10.1016/j.trc.2019.01.001),
[audit](../../extraction/n2_source_studies/FB0026.md).

FB0022 also retains differing speeds by link entry-time history. That is another
aggregate capability, not proof of immutable response-cohort necessity. Its
SUMO forward checks and constant-limit field drop checks do not jointly
establish our advisory/closure/gradient contract.
[Source](https://onlinelibrary.wiley.com/doi/10.1111/mice.13492).

### Compliance matters, but does not select B1 automatically

The advisory field report FB0005 uses an aggregate speed-discrepancy compliance
metric, distinct from the nominal compliant-driver fractions in its simulations.
Neither directly identifies B1 membership and response laws. Observed response
changes with traffic context and experience.
[Source](https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/final-reports/ca18-2447-finalreport-a11y.pdf).

Newly checked FB0033 (July 2026) provides a concrete SUMO work-zone calibration
strategy: fit car following, lane changing and individual speed-factor
mean/spread. Table 10's two/three-layer speed RMSEs are 23.66/5.68 and
25.22/6.71 km/h over three seeds. This strengthens forward evaluator feasibility,
but it uses a fixed 60 km/h limit at one site, not changing advice or candidate
gradients. Calibration and evaluation use the same dataset, with no independent
validation set; underlying data are by request. Exogenous driver heterogeneity in an
evaluator is not a control-dependent categorical probability-shift model.
[Publisher record](https://www.mdpi.com/2076-3417/16/14/7091),
[method audit](../../extraction/n2_source_studies/response_lane_derivative_frontier.md).

### Endogenous lane models are available, but need selective adaptation

FB0024 supplies density-imbalance lane-group transfer for on-ramp traffic.
FB0030 adds mandatory lane-end/route incentives, downstream lookahead and
receiving limits in a per-lane CTM, with field lane-density checks. These are
better starting points for endogenous merge pressure than commanded lane-
change volumes. Their forward benefits do not prove shared-advice ranking
benefits; the complete published schemes also require boundary/continuity and
conservation audits before differentiable use.
[FB0024](https://doi.org/10.1061/JTEPBS.0000481),
[FB0030](https://doi.org/10.1080/21680566.2019.1700846),
[audit](../../extraction/n2_source_studies/FB0030.md).

FB0004 and FB0020 remain important boundary predecessors: they combine richer
state with lane-specific/CAV/lane-change/ramp actions. Their gains must not be
attributed to retaining state under our unchanged link-level advice action.

## 4. Which gaps survive?

| Status | Finding |
|---|---|
| Already addressed | Aggregate speed control, imperfect mean response, lane-level traffic models, macro–micro reoptimization, analytical speed sensitivity, and reopening-tail delay accounting. |
| Qualified research opportunity | Minimum information needed for useful independent advisory sensitivities under the same actions and population; simpler-model sufficiency boundaries. No direct answer adopted from the inspected predecessors. |
| Not demonstrated | Strong B0 ranking failure caused specifically by lost response composition or lane occupancy; B1 necessity before B2; gradient usefulness outside the candidate model. |
| Feasibility gap | Common dynamic advice-response calibration and closure/discharge/recovery contract with a richer evaluator. Documentary capability exists; faithful implementation and held-out validation remain untested. |
| Modeling gap | Cohort identification, lane/cohort coupling, exact conservative transfer, and branch-safe continuous capacity/discharge dynamics. Existing components help but do not supply an approved complete model. |

Potential novelty is therefore concentrated, not scattered: **information
retention → matched intervention ranking → useful independent sensitivity**.
Response, lane and recovery mechanisms are supporting ingredients or controls,
not separate novelty projects. New VSL algorithms, CAV actuation, lane-specific
actions, stochastic estimators, saltation methods, routing and safety theory
remain outside the recommendation.

Search checked all required families and nearest-source citation neighborhoods.
The final targeted pass added no new decision category after the recent
calibration paper was inspected. This supports only a bounded statement about
inspected evidence, not proof of worldwide absence. Abstract-only/unreconciled
leads remain explicit unknowns, not novelty evidence.
[Coverage](../../search/n2_coverage_map.md),
[gap/counterevidence register](../../synthesis/s02/n2_gap_register.md).

## 5. Model priority, Gap 7 and evaluator implications

First priority is a strong mean-response/history-aware B0 and common action,
population and recovery accounting—not constructing B1. Second is establishing
one decision-relevant omitted-information contrast. Only then choose fixed
response cohorts, lane refinement or neither. Response and lane information
are two axes; the compliance-first ladder is a working hypothesis that may
need refinement at this gate, not a fixed scientific invariant.

Deterministic continuous response and lateral-flow structures are plausible.
No evidence makes control-dependent class sampling or hybrid reset/saltation
methods indispensable. However, published threshold, empty-state and capacity-
mode laws cannot be certified by saying 'continuous mass.' No smoothing,
exception or silent repair is approved.
[Adoption register](../../synthesis/s02/n2_model_adoption_register.md),
[Gap 7 screen](../../synthesis/s02/n2_admissibility_screen.md).

SUMO is a plausible evaluator, but native variable speed signs change lane
limits rather than directly representing voluntary advice. A faithful shared
driver-response mapping needs a later API/behavior audit. SUMO is not on this
session's PATH and traci/sumolib are absent from the selected environment;
nothing was installed. The outcome can initially be a synthetic-reference
claim, not field validity by implication. Pending insertion delay, unfinished
traffic and post-reopening queues must be counted.
[Evaluator contract screen](../../synthesis/s02/n2_evaluator_contract_screen.md).

## 6. N2-UG1: substantive user choice

**Problem statement.** Does F1 warrant further minimum-information study, and
should the next work commit to a ladder, narrow the question, refine evidence
first, or defer?

**Assumed model-chain function.** Shared infrastructure advice affects realized
driver response and continuous traffic dynamics; candidate sensitivities should
rank interventions usefully in an independently implemented richer evaluator,
including the recovery tail. N2 has not constructed or validated this chain.

**Core gap.** Mechanism/forward evidence does not identify which omitted variable
causes a matched decision failure. Choosing cohorts first could add unnecessary
complexity; selecting a weak B0 or changing actuators could manufacture benefit.
The common response/calibration contract is plausible, not ready to freeze.

### Route B — bounded contrast/contract refinement (route approved 2026-09-17)

Prepare a separate short plan for two linked outputs: a credible homogeneous
baseline/common advice-and-recovery contract, and one supported omitted-
information diagnostic hypothesis. Provisionally prioritize ending/continuing-
lane occupancy under mandatory-merge pressure; joint response composition is
conditional, not a required first refinement. Check closest predecessor coverage
of that precise information/gradient claim. This is go/no-go evidence development,
not selection of final equations or a promised novel simulator. Reuse existing
response/transfer/reference models, not develop new behavior theory. Resolve
what can be resolved by source/contract review; if numerical evidence is needed,
present a separately approved small diagnostic experiment plan before any run.

**Pros:** targets the actual uncertainty; limits construction burden; preserves
strong simpler counterevidence and the user's preference for simpler modeling.
Tests a potentially substantive retained-information contribution rather than
repackaging established lane control or aggregate autodiff.

**Cons:** an extra stage may conclude no viable study; faithful advisory response
and lawful calibration materials may still be unavailable. It does not promise
a successful novelty or gradient result.
The hypothesis may already be answered by prior work, or disappear against a
strong response/history-aware aggregate baseline; the initial lane priority is
itself provisional.

**Dependencies/cost/stop:** G0 unchanged; refine G2/G3 before detailed P2–P4.
Cost now is a bounded source/contract synthesis, not three simulators or a
calibration campaign. Require an explicit observable omitted-information
contrast and accessible fair validation basis. Stop for user review when those
exist—or when a critical access/contract gap prevents them. Do not extend the
search into a new task or rescue novelty with new mechanisms.

### Route A1 — retain the compliance-first working ladder

Plan detailed B0/B1 review first; B2 conditional on a justified lane mechanism.
B0 must already represent mean response and necessary dynamics; classes are
fixed exogenous metadata with continuous mass, not sampled actions.

**Pros:** coherent nested study; response heterogeneity has empirical motivation;
can measure when the simpler model suffices without needing B2 to win.

**Cons:** existing evidence does not establish persistent classes as the first
missing information; identification and coupled calibration could dominate cost.
The full ladder cannot currently be defended as necessary.

**Dependencies:** new detailed design/review plan; explicit hypothesis status
and early stop if mean response explains the effect. No automatic three-model
implementation. Viable as a user-selected exploratory commitment, less supported
than Route B at present.

### Route A2 — narrow to a strong-aggregate sufficiency question

Focus on when calibrated aggregate speed-response dynamics suffice for advisory
decisions during restriction/recovery, with one justified richer reference
contrast rather than a preset full ladder.

**Pros:** smaller scope; directly respects strong aggregate counterevidence;
negative/equivalence outcomes can be scientifically meaningful.

**Cons:** the domain and decision acceptance logic still need specification;
without a genuine challenging contrast it risks reproducing established
aggregate success rather than answering a distinctive question.

**Dependencies:** approve the narrowed question and plan its sufficiency/failure
domain. Similar common-contract burden remains; cannot conclude equivalence
from the absence of richer-model evidence.

### Route C — halt or defer F1

Defer this extension because the surviving decision gap is insufficiently
motivated relative to calibration/access/construction cost; retain the review
as a reusable evidence map.

**Pros:** avoids unnecessary complexity and novelty rescue; no implementation
or new access obligations.

**Cons:** leaves a plausible matched-sensitivity opportunity untested. The
current review does not prove it already answered or impossible.

**Dependencies:** record deferral as an evidence/cost judgment, not a proof of
aggregate sufficiency or global novelty overlap.

**Recommendation:** Route B. It keeps the next step finite and allows the
findings—not the ladder's initial ordering—to determine the necessary model
complexity. The user approved this route on 2026-09-17; its separate execution
plan remains to be drafted and approved.

## 7. Feedback 23 clarification — 2026-09-17

The gate needs a concrete task–information hypothesis, not only a gap verdict.
[Detailed response](s02_35_feedback23_task_and_minimum_information_response.md).
The accepted control task stays shared link-level speed advice upstream of a
fixed lane reduction; B2 is a model label, not a distinct actuator/task.

Two candidate contrasts are now explicit: (1) different ending/continuing-lane
occupancy under matched aggregate retained states, creating different feasible
merge pressure; (2) different lane–fixed-response-group association under
matched marginals, where feasible, potentially requiring joint information.
Both are reviewer hypotheses, not demonstrated advice-ranking failures.

Route B remains provisionally recommended, now with a more concrete initial
priority: refine the simpler lane merge-pressure contrast/common contract,
without requiring fixed response groups first. Joint lane/group information
is conditional. This changes no accepted G0 input or frozen protocol; any
lane-only intermediate would refine working G2/G5 hypotheses with explicit
later approval, not silently replace the originally described B2 model.

Candidate retained information is lane-resolved local spatial occupancy,
receiving room, fixed continuation/adjacency and constrained deterministic
transfer, plus the strong baseline's needed speed-response/history. Exact
minimum state and native differentiated closure are not proved. Such a
candidate can also be described as multi-lane macroscopic; the scientific
question is information and gradient usefulness, not a naming distinction.

The user gate chooses the phenomenon/hypothesis worth investigating and the
acceptable bounded next scope. It does not ask the user to declare the missing
empirical necessity result. Candidate formulations/admissibility arguments
belong to current discussion; frozen equations/partitions and quantitative
minimum-state or independent-usefulness proof belong to later planned work.
No route, model refinement or experiment has been approved by this clarification.

### Feedback23 amendment: novelty and necessity (2026-09-17)

The brief supplementary review establishes predecessors for continuous
multi-lane speed/lateral control, aggregate speed-control adjoints and
METANET automatic-differentiation calibration. Neither lane-aware control
nor native aggregate autodiff is sufficient standalone novelty.

Route B's provisional rationale is now explicitly a bounded go/no-go test
of control-gradient information sufficiency, not a promise of a novel
simulator. Prioritize one reachable lane-occupancy contrast against a strong
response/history-aware aggregate baseline with identical shared advice,
then a closest-predecessor check of that precise claim. Conditional response
groups and intra-lane order must earn their additional complexity; neither
is established necessary. An independent-reference advice-ranking distinction
and valid component ablation are needed, not merely improved forward fit.

Possible contributions are a task/domain-specific sufficiency/failure map,
gradient-aware retained-information selection and a compact deterministic
validated realization. All remain conditional. If prior work settles the
precise question or the strong aggregate baseline suffices, narrow/revise or
defer. Smoothing in an adjoint predecessor does not authorize smoothing here.
The user's task-plausibility agreement is not route/equation approval.
See [full amendment response](s02_36_feedback23_amendment_novelty_and_component_necessity.md).

## 8. Handoff

The user approved Route B on 2026-09-17, closing the N2-UG1 route decision.
G0 is unchanged; G1–G4 retain their documented findings/remaining gaps.
Local extraction has not selected global
equations, partitions, calibration targets or tolerances. No paper request,
scientific run or later P2–P4 work is active.

The [historical Route B review/refinement proposal](../../archive/planning/route_B_review_plan.md)
was drafted and subsequently approved on 2026-09-17.
Its [frozen protocol](../../s03_00_rb_review_protocol_plan.md) governs the follow-on pass,
now completed through [RB-UG1](../s03/s03_20_rb_findings_and_gate.md) after resolving its
[one-paper request](../s03/s03_10_rb_access_request_1.md).
The user selected diagnostic planning and closed the Route B review sprint.
Next action is the separate proposal, not a numerical run. Route approval is not approval of
exact equations, experiments or implementation. [Work/check record](s02_90_n2_work_report.md).
