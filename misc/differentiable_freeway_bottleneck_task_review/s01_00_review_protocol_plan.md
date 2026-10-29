# S01.00 — Differentiable freeway bottleneck task review — N1 protocol plan

Sprint: [S01](00_review_sequence.md#s01) · Role: 00 plan · Predecessor: pre-review handoff · Gate: N1 user gate.

Date: 2026-09-16  
Status: **Approved 2026-09-16; N1 executed; candidate A subsequently accepted
after gate clarifications; N2 protocol drafting only**

## 1. Decision purpose

N1 is a bounded, task-first framing sprint for traffic control around an
exogenous temporary or permanent freeway lane-capacity reduction. Its decision
is whether one candidate warrants a later full review—not which simulator to
build.

N1 will:

- compare F1 speed harmonization/advisory control and F2 coordinated ramp
  metering as the two initial primary candidates;
- treat F4 post-reopening recovery as a scenario dimension of either candidate;
- retain F3 joint control and F5 cooperative lane-change/merge control only as
  expansion or boundary candidates;
- identify the strongest credible lower-resolution baseline for each primary
  candidate;
- ask whether a demonstrated decision-relevant failure requires additional
  retained information;
- test whether a credible derivative-correctness and independent
  gradient-usefulness study can be formulated; and
- recommend selecting one candidate, refining and repeating N1, or halting the
  freeway branch.

Macro, multiclass/cohort, mesoscopic, hybrid, microscopic, and negative or
infeasible outcomes are equally admissible. Model candidates will be described
by retained information and behavior, not by a resolution label alone.

### Non-goals

N1 will not:

- implement a simulator, controller, optimizer, experiment, or formal task;
- choose or optimize closure location, affected lanes, or closure/reopening
  time;
- perform a full systematic review, novelty proof, calibration campaign, or
  site reconstruction;
- preselect F3 or F5, or broaden into generic incident management, routing,
  reinforcement learning, or network-wide CAV control;
- require compatibility with the current urban simulator, code base,
  mesoscopic definition, paper, or milestone sequence;
- alter project plans, milestones, source, tests, configuration, the closed
  pre-review, or the closed ramp-metering review; or
- authorize any work after the first user gate.

## 2. Research questions

The sprint operationalizes the inherited CQ1--CQ7 backbone as follows.

| ID | N1 question | Required output |
|---|---|---|
| N1-RQ1 | What disturbance, continuous action, feasible set, horizon, objective, constraints, demand regimes, and recovery phase define each candidate? | A bounded task statement for F1 and F2, with F4 variants where relevant |
| N1-RQ2 | What is the strongest credible task-specific lower-resolution model and controller/optimizer baseline? | A source-backed baseline family, not a deliberately weak comparator |
| N1-RQ3 | In what controlled scenario, if any, does that baseline lose information that can change feasible actions, action rankings, or downstream outcomes? | An explicit failure mechanism and counterevidence; absence is a valid result |
| N1-RQ4 | What minimum additional retained state or behavior could close the demonstrated gap? | A smallest-state hypothesis, alternatives, and an isolation/ablation strategy |
| N1-RQ5 | Can derivatives of the candidate model and control parameterization be defined and checked credibly? | A derivative contract, event/active-set limits, and finite-difference or equivalent reference check |
| N1-RQ6 | Can gradient directions or rankings be tested in a richer, independent evaluator under matched actions and objectives? | A plausible evaluator and transfer test distinct from internal optimization success |
| N1-RQ7 | Is the prospective fidelity gain worth the modeling, calibration, computation, validation, and evidence burden, and is the contribution distinct from direct predecessors? | A bounded value/burden and novelty-risk judgment |

N1-RQ1 and N1-RQ2 must be answered before interpreting richer-state evidence.
N1-RQ3 must identify an actual or well-supported decision-relevant gap before
N1-RQ4 can justify added state. N1-RQ5 and N1-RQ6 are independent gates: a
correct derivative does not establish a useful control direction.

## 3. Candidate comparison and decision rules

The comparison will use an evidence table rather than a weighted score. Each
candidate receives `supported`, `qualified`, `unsupported`, or `unresolved` on
the following criteria:

1. **Operational definition:** the action, disturbance, horizon, population,
   objective, constraints, and temporary/permanent and recovery cases are clear.
2. **Strong baseline:** a credible aggregate, multiclass, cohort-memory,
   feedback, MPC, adjoint, or direct-optimization comparator exists.
3. **Resolution-sensitive gap:** omitted information can plausibly change a
   feasible action, action ranking, or relevant outcome under a controlled
   contrast.
4. **Minimum-state isolation:** the proposed gain can be attributed to a
   smallest added state or behavior rather than an inseparable bundle.
5. **Derivative correctness:** a numerical or analytic derivative-validation
   contract exists, with nonsmooth/event conditions declared.
6. **Gradient usefulness:** the same feasible perturbations or rankings can be
   evaluated in a richer independent model without changing the objective or
   population accounting.
7. **Operational and scientific value:** the task is consequential and offers a
   distinguishable question beyond established lower-resolution control work.
8. **Evidence and execution feasibility:** source access, calibration, software,
   data, runtime, and evaluator demands appear bounded enough for a later review.
9. **Interpretability of outcomes:** positive, equivalence, and negative results
   would each support a clear conclusion.

A candidate is recommendable only if Criteria 1--6 are at least qualified and
no stop condition in Section 9 is triggered. High detail or high novelty
potential cannot compensate for a missing baseline, derivative contract, or
independent usefulness test. F1 and F2 will be compared separately; F3 will not
be used to rescue either candidate by combining them.

## 4. Search strategy

### 4.1 Sources

Searches will begin with the inherited package and closed-review evidence in
Section 7. New discovery will use, as appropriate:

- TRID and official FHWA/transport-agency guidance for operational definitions,
  field constraints, work zones/incidents, ramp storage, fairness, and model
  resolution;
- Crossref, OpenAlex, Google Scholar, and Semantic Scholar for discovery,
  metadata, and backward/forward citation tracing;
- publisher and author-repository records in IEEE Xplore, ScienceDirect,
  Springer, TRR/SAGE, and relevant university repositories;
- arXiv for recent differentiable simulation, traffic-control optimization,
  CAV/mixed-traffic, and prepublication work, with publication status checked;
  and
- primary software/model documentation only when evaluator capabilities or
  reproducibility claims depend on it.

Primary studies and authoritative guidance will support substantive findings.
Reviews may map terminology and citation networks but will not replace primary
method evidence. Searches cover classic predecessors without a start-date
cutoff and emphasize work from 2020 through the search date; recent arXiv work
will be searched explicitly, but recency will not override evidence quality.
English-language records are the working scope. A clearly decision-critical
non-English source will be logged as a gap rather than silently excluded.

### 4.2 Query families

Queries will combine the lane-reduction anchor with these bounded families:

| Family | Illustrative concepts |
|---|---|
| Bottleneck physics and recovery | lane drop/closure, work zone, incident, capacity drop, queue dissipation, hysteresis, reopening/recovery |
| F1 aggregate control | variable speed limit, speed harmonization, mainstream flow control, lane-drop bottleneck, link-queue/CTM/METANET, optimal control/MPC |
| F1 richer response | advisory speed, compliance, mixed traffic, CAV moving actuator, lane-specific speed control, acceleration/response delay, lane-change interaction |
| F2 control | coordinated ramp metering, nonrecurrent bottleneck, incident/work-zone metering, finite ramp storage, queue override, arterial spillback, equity/fairness |
| Resolution contrasts | macroscopic, multiclass, cohort/packet, lane-resolved, mesoscopic, hybrid/multiresolution, microscopic; retained class/lane/order/speed/gap state |
| Derivatives and optimization | differentiable simulation, automatic differentiation, discrete adjoint, sensitivity, nonsmooth/piecewise gradient, smoothing, direct optimization |
| Independent evaluation | cross-fidelity, microsimulation, hybrid simulation, perturbation ranking, controller transfer, held-out scenario |
| Counterevidence | macro sufficiency, feedback/ALINEA, convex/monotone/structured control, weak or failed VSL, compliance limits, calibration burden |

At least one query in each candidate will seek negative results and strong
simpler alternatives. Citation chasing stops when each decision-critical claim
has direct evidence or an explicit gap, not after an arbitrary paper quota.

## 5. Screening and evidence labels

### Inclusion

Include a record when it contributes directly to at least one N1 question by:

- defining F1 or F2 around a lane reduction, capacity-drop bottleneck, temporary
  restriction, or recovery period;
- establishing a strong lower-resolution control/model baseline;
- identifying a resolution-sensitive mechanism or a credible counterexample;
- specifying derivative/sensitivity construction or validation;
- enabling matched richer-model evaluation; or
- documenting operational constraints such as ramp storage, compliance,
  fairness, safety, or queue clearance.

Adjacent studies without the exact disturbance may be retained when their
method is directly transferable and the transfer is labeled as an inference.

### Exclusion

Exclude from the active evidence matrix:

- pure traffic prediction, detection, or state estimation without a relevant
  control or resolution implication;
- control studies whose action, objective, baseline, or traffic model cannot be
  determined beyond a title/abstract lead;
- trajectory, routing, lane-closure scheduling, or discrete maneuver
  optimization that changes the task instead of informing F1/F2 boundaries;
- generic “mesoscopic” applications that do not state what information or
  behavior is retained;
- uncheckable secondary claims, duplicate versions without substantive
  differences, and promotional software descriptions; and
- F3/F5 evidence unless it clarifies an explicit boundary or a stop condition
  for F1/F2.

Excluded records remain in the screening log with a reason. They are not
treated as evidence of absence.

### Claim-level evidence strength

| Label | Meaning | Permitted use |
|---|---|---|
| E3 — decision-grade | Relevant full primary text or authoritative official source inspected at the method/equation/result location | Supports task selection, baseline, mechanism, derivative, or evaluator judgments |
| E2 — supporting | Relevant full review/documentation or sufficiently detailed primary material inspected, but indirect or incomplete for the exact task | Supports context or a qualified inference; cannot alone decide a fatal gate |
| E1 — discovery-only | Metadata, abstract, indexed excerpt, citation lead, or inaccessible record | Candidate discovery and gap logging only |
| E0 — unverified | Claim encountered without a reliable inspectable source | No substantive use |

Each extracted claim will record the evidence label, exact source/version and
location, direct statement versus reviewer inference, and access limitation.
Contradictory evidence is retained. Publication venue or citation count does not
substitute for claim-level relevance.

## 6. Execution phases and artifacts

The user approved the full proposal on 2026-09-16 and authorized N1-1 through
N1-3, with a mandatory stop at the first decision gate or an earlier paper-
access request.

| Phase | Work | Planned artifacts | Exit |
|---|---|---|---|
| N1-0 — protocol | Reuse audit and executable plan | `s01_00_review_protocol_plan.md` | Approved 2026-09-16 |
| N1-1 — discovery and screening | Reuse-map first; bounded queries; deduplication; title/abstract and targeted full-text screening | `search/query_log.csv`, `search/coverage_map.md`, `screening/records.csv`, `screening/decisions.csv`, `archive/manifest.csv` | Continue only within approved protocol; stop for Section 9 or access batch |
| N1-2 — extraction and comparison | Claim-level extraction for F1/F2, baselines, minimum-state hypotheses, derivatives, and evaluators | `extraction/task_evidence_matrix.csv`, `extraction/claim_source_map.md`, `synthesis/s01/candidate_task_matrix.md`, `synthesis/s01/minimum_source_map.md`, `synthesis/s01/explicit_exclusions.md` | No task promotion; prepare gate only |
| N1-3 — first decision gate | Synthesize the bounded choice and uncertainties | `reporting/s01/s01_30_n1_user_gate.md` | Stop for user selection, N1 refinement, or halt |

The package will also use `archive/full_text/`, `archive/metadata/`, and
`archive/user_supplied/` for new material only. `README.md` may be added during
execution to state package status and navigation. Files will be created when
their phase opens rather than as empty placeholders.

The first user gate will ask the user to review exactly one primary decision
packet, `reporting/s01/s01_30_n1_user_gate.md`, containing:

1. a compact F1/F2 task matrix, with F4 and F3/F5 roles explicit;
2. a minimum source map showing the decision-grade evidence and remaining gaps;
3. an explicit exclusion list and scope-boundary effects;
4. fatal-stop results and uncertainties; and
5. one recommendation: select one candidate for a later full review, refine and
   rerun a bounded part of N1, or halt the freeway branch.

The matrices in `synthesis/` and logs/extractions are audit attachments, not
additional decision documents. N1-3 does not authorize a full review,
implementation, project synchronization, or candidate development.

## 7. Reuse of existing evidence

Before any new query, execution will inventory and map:

- the closed pre-review handoff, terminology scan, and email-response record;
- the motivating email trace;
- the closed ramp-metering review's closure record and evidence debate;
- its archive manifest and `feedback20_sources.md`; and
- archived RM0024 (first-order discrete-adjoint coordinated ramp metering),
  RM0025 (multiclass network discrete adjoint), and the bounded RM0026 record
  (smoothed-CTM ramp metering), plus other directly relevant IDs.

Existing files remain frozen in their original packages. The new package will
record cross-package ID, path, version/access state, prior claim boundary, and
the narrower or different N1 use. It will not duplicate full text or silently
upgrade abstract/metadata evidence. A prior conclusion is reusable only within
its original scope; the closed compatibility-framed rejection of ramp metering
does not decide this task-first review.

New queries will first be checked against the reuse map by DOI, title, and
source ID. A repeated query is allowed only to obtain a missing decision-grade
version, update a time-sensitive record, or answer a genuinely new N1 claim; the
reason will be logged.

## 8. Admission of one new candidate

N1 may admit at most one literature-supported candidate beyond F1/F2. It must:

1. use the same exogenous lane-capacity-reduction anchor;
2. define a materially distinct continuous control decision rather than rename
   F1, F2, F3, or F5;
3. have at least E2 evidence for operational relevance, a credible lower-
   resolution baseline, and a plausible derivative/usefulness contract;
4. fit N1-RQ1--N1-RQ7 without opening a new search community; and
5. either replace a weaker primary candidate at the gate or remain a boundary
   finding—never increase the active primary set beyond two.

If these conditions are not met, the lead is logged for future work and
excluded from N1. Admission changes no task selection until the first user gate.

## 9. Stop conditions

Stop work on a candidate and report the evidence when any of the following is
established or remains decision-critical after the bounded search:

- **Macro sufficiency:** a strong task-specific aggregate or multiclass model
  represents the relevant action rankings and outcomes, and no supported
  resolution-sensitive failure or minimum added state is found.
- **Excessive entanglement:** the candidate depends on an inseparable bundle of
  lane-changing, acceleration, safety-gap, compliance, route response, or other
  mechanisms, so N1 cannot attribute value to a minimum resolution increase.
- **Infeasible gradient validation:** no credible derivative contract can be
  defined around its discrete events/active sets, or no matched finite-
  difference/reference check and independent action-transfer test is plausible.
- **Insufficient novelty:** direct predecessors already answer the same
  resolution-and-gradient-usefulness question, or the remaining contribution is
  only implementation of established control at a new site.
- **Unacceptable evidence cost:** deciding the candidate would require an
  unbounded literature program, repeated inaccessible-paper requests, major
  proprietary calibration/data acquisition, or evaluator construction that
  cannot be justified before a task is selected.

A stop condition is a valid N1 result, not a reason to weaken the baseline or
change the question. If both primary candidates stop, N1 recommends halting the
freeway branch unless the single-candidate admission rule has already produced
a qualified replacement. A material conflict with this protocol or the fixed
task-first principles stops the sprint for user direction.

## 10. One-batch institutional-access procedure

During N1-1/N1-2, inaccessible papers remain E1 until screening shows that full
text is decision-critical and no open manuscript, author copy, preprint,
official report, or adequate direct alternative exists. Requests will be
consolidated into one file:

`reporting/institutional_access_batch_1.md`

For each item it will list source ID, title, authors/year, DOI/URL, candidate and
N1 question, why E3 evidence is necessary, alternatives already checked, and
the requested version/pages. The user will be asked once to place lawfully
obtained files in `archive/user_supplied/`; no credentials or proxy access will
be requested.

The sprint pauses after that request. There will be no paper-by-paper requests
and no second N1 batch. If requested material is unavailable, the affected claim
remains unresolved and the candidate is qualified, stopped for unacceptable
evidence cost, or excluded—never strengthened by assumption.

## 11. Approval boundary

The 2026-09-16 approval authorized N1-1 through N1-3 and the associated
new-package search, archive, screening, extraction, and synthesis files. It did
not authorize simulator development, task implementation, a full post-N1
review, changes outside this package, or action beyond the first decision gate.

N1 reached `reporting/s01/s01_30_n1_user_gate.md`. No inaccessible paper proved critical to
N1's selection, so its access batch was not opened. The user subsequently
selected candidate A after clarifications and authorized drafting the N2
protocol. This does not authorize N2 execution, implementation, or project
synchronization. Inaccessible predecessors must be reassessed at N2 depth.
