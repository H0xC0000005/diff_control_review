# Route B — bounded information-gap review plan

**Archive status: Historical superseded draft; not current execution authority.**
Preserved on 2026-09-17 during package consolidation. The original drafting
status/text below is retained. Use the [approved Route B protocol](../../s03_00_rb_review_protocol_plan.md)
for its closed review pass, not this draft.

Prepared: 2026-09-17. **Status: Proposed; awaiting plan approval.**
Route B itself was approved at N2-UG1. This document proposes its execution
scope; it is not an experiment, implementation or urban-milestone plan.

## 1. Backbone and intended endpoint

Review one question: **Does a strong aggregate model omit lane information
that could change useful gradients for shared upstream speed advice at a
freeway lane reduction? If so, what is the smallest credible next evidence step?**

Work order: reuse and precise-prior-art check → strong baseline/common contract
→ one reachable lane-occupancy contrast and candidate-information audit →
source-backed findings and the next user decision.

The initial omitted variable is occupancy of ending versus continuing lanes
near the mandatory merge. This is a hypothesis, not a demonstrated failure.
Fixed response classes, joint lane/class association and intra-lane order are
not required additions. Do not search for new mechanisms merely to save novelty.

The review stops at **RB-UG1: next-evidence go/no-go**, or earlier for a
decision-critical paper-access request, scope conflict or fatal finding.
It may conclude that numerical evidence is needed, but may not produce it.
There is no new upfront scientific choice for the user beyond approving this
bounded protocol. Evidence-dependent choices remain for RB-UG1.

## 2. Authority, verified starting point and exclusions

Inputs are the [accepted N1 task](../../reporting/s01/s01_30_n1_user_gate.md),
[completed N2 findings and Route B decision](../../reporting/s02/s02_20_n2_findings_and_gate.md),
[feedback23 clarification](../../reporting/s02/s02_35_feedback23_task_and_minimum_information_response.md)
and [amendment review](../../reporting/s02/s02_36_feedback23_amendment_novelty_and_component_necessity.md).
The approved N2 protocol remains the historical authority for its completed
segment; this proposal supersedes no accepted task boundary.

Verified existing evidence includes strong mean-response/speed-history
baselines, lane-group transfer models, aggregate speed adjoints and multi-lane
control. These are established components, not new contributions. The current
unproved issue is matched-action, externally useful sensitivity and information
sufficiency. Supplied Seliman2020 and Chen/Ahn2015 papers are already verified;
do not request them again. Some newer/abstract-only leads remain unverified at
method depth. Absence of a recorded answer is not worldwide novelty clearance.

Fixed boundaries for this review:

- Same continuous link-level infrastructure advice schedule and feasible actions
  across representations. A lane model receives the same advice on its lanes.
  Advice changes desired response; it does not command actual vehicle movement.
- Geometry, affected lanes, demand, routes, population and closure/reopening
  schedule are exogenous. Temporary closures include post-reopening clearance.
- Continuous traffic mass and deterministic candidate dynamics are preferred.
  Avoid control-dependent categorical probability shifts and hybrid resets
  requiring event-time/saltation treatment. Fixed seeds do not remove that issue.
- Strong aggregate response and necessary history belong in the baseline.
  Conservation, receiving/storage and objective accounting must remain valid
  in every proposed smaller representation.
- Separate forward fidelity, derivative correctness and independent gradient
  usefulness. Continuous mass or successful autodiff proves none by itself.
- Urban simulator compatibility, code reuse and one-paper organization are not
  task-admissibility constraints.

Excluded: simulator/controller/optimizer coding; traffic runs, calibration,
sampling or optimization; installation/environment changes; field/data
collection; selecting numeric parameters, tolerances or seeds; lane-specific
advice, commanded lane changes, direct CAV actuation, ramp-control expansion,
routing, closure optimization, safety certification or new gradient estimators.
No smoothing, surrogate derivative or repairs to source equations are approved.
No edits to mainline/milestone files, user feedback, closed reviews or old results.

This is documentary scientific review, not component construction. No new
dependency/API or tensor interface is proposed. The existing urban source/tests/
config were inspected only to confirm that they are not a freeway task contract;
their closed plans do not govern an independent freeway implementation.

## 3. Question ownership and order

The IDs below are audit labels; plain-language names are used in the report.
“Review-owned” means collect evidence and recommend, not approve a new method.

| ID | Class/status | Question | Owner; dependencies |
|---|---|---|---|
| RB-G0 | Type 2; fixed input | What task/actions and Gap7 restrictions apply? | Accepted user boundary; all work |
| RB-G1 | Type 2; evidence-open | Does prior work already answer the precise information-to-useful-gradient claim? | Review synthesis; G0 |
| RB-G2 | Type 2; evidence-open | What strong baseline and common advice/accounting/evaluator contract are defensible? | Review synthesis; G0; local baseline/evaluator extraction |
| RB-G3 | Type 2; hypothesis-open | Is a reachable omitted-lane-information contrast meaningful beyond that baseline? | Review synthesis; G1/G2; lane extraction |
| RB-G4 | Type 2; screen-open | What added information is plausible, admissible and fairly attributable? | Review synthesis; G2/G3; derivative extraction |
| RB-G5 | Type 2; deferred decision | Proceed to which smallest next evidence activity, narrow, or halt/defer? | User at RB-UG1; G1–G4 |
| RB-C1-Q1 | Type 1; extraction | What aggregate state/history/response and results do baseline sources actually retain? | Baseline study; informs G2 |
| RB-C2-Q1 | Type 1; extraction | What occupancy, lane-end incentives and constrained transfer do lane sources use? | Lane study; informs G3/G4 |
| RB-C3-Q1 | Type 1; extraction | What action/data/accounting capabilities does a richer evaluator document? | Evaluator study; informs G2 |
| RB-C4-Q1 | Type 1; extraction | What switches, denominators and derivative targets/checks do sources contain? | Derivative study; informs G4 |

Mixed questions are split: global information necessity is G3/G4, source
transcription is C1/C2; global comparison fairness is G2, software capability
transcription is C3; admissibility is G0/G4, equation hazards are C4.
Global-first means confirm G0 and the shared question/fairness obligations before
serial source studies; local findings inform open global conclusions but cannot
silently close or alter them. Close G1–G4 at finding/recommendation level before G5.
A contradiction reopens the smallest affected contract explicitly; changing G0
requires an immediate user stop, not an extraction convention.

## 4. Authorized review work after approval

### Step 1 — reuse, exact overlap and strong-baseline contract

Reuse existing source studies/claim locations before discovery. Audit the closest
claim, not a literal model-name match: does lane-resolved information alter
speed-action directions/rankings under otherwise comparable conditions?

Prioritize existing Seliman2020 lane-drop evaluation; Roncoli2014/2015
multi-lane control; Goatin2016 speed adjoints; mean-response and speed-history
sources; and the relevant derivative/AD lineage. Read full methods only where
the decision depends on them. Classify overlap as building block, same task,
or substantive prior answer. Changed actuators/objectives may prevent causal
attribution, but do not automatically make overlapping work irrelevant.

Produce one common-contract note covering:

- Baseline retained spatial mass/density, mean speed/response, queues/storage
  and history; which evidence justifies each item and credible alternatives.
- Shared advice zones/update intervals, feasibility and response mapping;
  distinguish desired response from actual car-following motion.
- Matched population, demand, geometry, disturbance and initialization; aggregate
  projection and information/history visible to each candidate.
- Objective recommendation and full accounting: include upstream waiting,
  pending/unfinished traffic and recovery; no arrived-only or truncated advantage.
  Retain original source metrics. Do not invent policy weights.
- Independent evaluator and lawful parameter/data support: what is documented,
  what remains untested, and whether a synthetic-reference claim or empirical
  claim is supportable. Synthetic micro results are not field truth.
- Calibration versus held-out action evaluation, comparable action/search budget,
  grid/response/discharge confounds and a common failure-accounting policy.

This note recommends a contract for later approval; it freezes no equations or
calibration settings. Do not certify advice fidelity from native speed-limit
software capability alone. Verify official versioned documentation/source if
a capability claim matters; no installation or simulation probe is authorized.

### Step 2 — one contrast and an information/admissibility map

Specify one primary contrast, in prose or a compact diagram:

1. Candidate reduced information and the exact history/window retained.
2. Two physically reachable traffic conditions sharing that information but
   differing in ending/continuing-lane occupancy.
3. What demand, population, parameters, geometry and future disturbance are held
   fixed, and what distinct preparation/past conditions produce the hidden state.
   Do not claim complete matched histories unless they can actually coexist.
4. The causal chain: omitted occupancy → constrained merge/receiving behavior →
   advice-dependent traffic response → possible delay/action-ranking difference.
5. Same feasible advice perturbations and independent observable outcome.
6. What would falsify the hypothesis: aggregate/history response explains it,
   only forward trajectories differ, action ranking is unchanged, or matching
   fails without another uncontrolled mechanism.

A reachable matched pair may not exist for the strongest baseline. Record that
as a finding; do not weaken its information set to manufacture one. If ranking
reversal is not supported, distinguish weaker sensitivity/decision evidence
from a reversal. A different derivative magnitude alone does not demonstrate
a need for different control.

For each candidate information item, identify its function, source basis,
simpler substitute, valid conservative removal/compression comparison, causal
benefit claimed and evidence still needed. Distinguish a physical constraint
from an independently required extra state. Initial items are lane occupancy,
receiving room and deterministic constrained transfer, alongside the strong
baseline's speed response/history. Response classes and intra-lane order remain
conditional; do not develop a second contrast or new behavioral model here.

Audit source equations for paired conservation, donor/receiver budgets,
empty-state limits, continuous flux kinks versus genuine jumps/resets and
control-dependent sampling. Reference exact source locations; no silent fixes.
Internal numerical derivative checks and external perturbation usefulness are
listed as later evidence obligations, not performed or claimed here.

### Step 3 — substantive findings and stop

Combine overlap, common contract, contrast and information audit in one primary
findings/gate report. Explain what prior results establish, what gap survives,
what strongest counterevidence limits it, and the cheapest missing evidence.
Report each conclusion as established, supported hypothesis, unresolved or
disqualified, with source/evidence limits.

The report must tell the user what the science says before presenting choices.
A plausible testable hypothesis is a legitimate review output, but not proof
of minimum state, native-gradient fidelity, necessity or external usefulness.

## 5. Bounded search, evidence and paper access

This planning task executes no new search. After approval, search only gaps
left by reuse, using primary publisher/author/institutional sources and official
software documentation; indexes/reviews are discovery leads. Check recent
arXiv/publication versions through the execution date; no arbitrary start-year
cutoff. English is the working language; log critical other-language leads.

Required targeted families:

- Lane drop/closure + shared speed advice/VSL + lane distribution/merge pressure.
- Aggregate mean-speed response/history + advice sensitivity/control sufficiency.
- Multi-lane control + matched actions + omitted information/state aggregation.
- Speed-control adjoint/autodiff + internal derivative versus independent transfer.
- Macro/micro action ranking/perturbation + calibration/grid/actuator confounds.
- Temporary reopening/recovery and objective accounting, only unresolved details.

Follow closest-predecessor backward/forward citations where they could answer
the precise claim. Include negative/sufficiency/no-benefit results.
Changed-actuator and stochastic/hybrid studies remain labeled boundary evidence,
not justification to expand the task.

Log exact executed queries, dates, versions, inclusion/exclusion and claim
locations. Reuse N1 evidence levels: E3 inspected decision-relevant full primary
method/result or authoritative official source; E2 qualified supporting material;
E1 abstract/metadata/indexed excerpt; E0 unverified. Separately label scientific
strength: mechanism, controlled forward difference, matched decision difference,
verified internal derivative, independent useful sensitivity. Access is not
scientific strength; full text does not turn prediction into decision evidence.

Completion requires coverage of the six families and relevant nearest-predecessor
frontiers, with each gate-critical claim supported, contradicted or explicitly
unresolved. One final targeted frontier pass should add no new decision category.
Record the stopping rationale; no paper quota or global “first” claim.
If closure requires a new task/community or additional mechanisms, return to
the user rather than extending the review indefinitely.

Proposed access rule for this new segment: check lawful open versions and direct
alternatives first; consolidate **at most one decision-critical institutional
paper request**, then stop immediately. The completed N2 access batch is not
reopened. Request lists citation/DOI, required version/locations, why it changes
the decision and why alternatives are insufficient, with suggested filenames
under the active archive. Verify user-supplied identity/completeness/hash before
resuming an approved review. No credentials or access circumvention.
Later inaccessible dependencies become explicit gate gaps; a second request
requires renewed user authorization. Calibration data access is separately
reported, never inferred from paper access.

## 6. Artifacts and acceptance checks

Editable proposal: this file and the existing phase dialogue. On explicit plan
approval, freeze a copy as
`misc/differentiable_freeway_bottleneck_task_review/s03_00_rb_review_protocol_plan.md`.
No `docs/milestones/` implementation plan is created.

Create review outputs only when execution opens, inside the active package:

- `synthesis/s03/rb_common_contract.md` — baseline/action/evaluator/accounting note.
- `synthesis/s03/rb_contrast_and_information_audit.md` — one contrast, candidate
  information/valid-ablation map and derivative hazards.
- `reporting/s03/s03_20_rb_findings_and_gate.md` — primary science explanation/decision packet.
- `reporting/s03/s03_90_rb_work_report.md` — commands, changes, checks and remaining risks.
- `search/rb_query_log.csv` and `search/rb_access_log.csv`; one
  `extraction/rb_evidence_register.csv` for new/reused sources and claims.
  Schema: claim ID; source ID/title/DOI/version; access/E-level; source location;
  question ID; actuator; retained state/units/history; scenario/population;
  objective/horizon; baseline/evaluator; result; scientific-strength label;
  source statement versus reviewer inference; limitations; reused study path.
  Add source studies only when substantial new inspection warrants them.
- Optional `reporting/s03/s03_10_rb_access_request_1.md` only if triggered.
  Append new lawful texts/metadata/checksums to the existing archive; preserve
  old files and manifest entries. Reuse old texts in place, including closed
  ramp-review sources without modifying that package.

Acceptance is documentary, not a positive-result requirement:

1. Traceable closest-predecessor overlap and strong counterevidence.
2. Explicit common-contract recommendations and unresolved feasibility limits.
3. One reachable contrast specification, or a reason it fails; honest evidence
   grade and remaining numerical needs.
4. Candidate information/constraint/ablation map with Gap7 audit; no unsupported
   minimum-state or AD-ready assertion.
5. Clear next decision, costs/dependencies and early-stop diagnosis where needed.
6. CSV widths/unique IDs, question/source/study joins, local links, source-location
   and version checks; new archive hashes and unchanged reused-file hashes.

Use standard-library read-only checks; no new dependencies or code tests.
If substantial mathematics becomes essential, verify local LaTeX and supply
PDF plus retained source under repository conventions. Source units are retained
and conversions recorded; numerical shapes/dtypes/update schedules belong to
a later implementation plan, not this review.

## 7. RB-UG1 — next evidence decision

**Problem:** Is the information-gap claim sufficiently distinct, testable and
affordable to pursue, and what is the smallest next approved activity?

**Model-chain function:** shared advice → candidate traffic response →
checked model derivative → independently evaluated action direction/outcome.
This review motivates/contracts that chain; it does not construct it.

**Core gap:** literature may supply only mechanism/forward support. Reachability,
external advice-ranking differences and necessary extra state cannot be
declared empirically established from synthesis alone.

Present only findings-viable choices, preserving genuine alternatives:

### A. Proceed with a bounded diagnostic, or detailed design if already justified

If the gap is distinct and the contract/contrast is credible but ranking evidence
is missing, propose a separately approved diagnostic experiment plan. It must
later specify scenarios, reachable preparation, shared perturbations, evaluator,
calibration/held-out separation, derivative checks, precision/seeds/budgets and
acceptance/failure criteria. Do not run it from this review approval.
If direct decision-grade evidence already supplies the missing result, explain
why detailed model/evidence planning is the smaller next step instead.

**Pros:** tests the actual uncertainty before broad construction; can justify
a minimal refinement rather than a whole ladder.
**Cons:** may reject the hypothesis; evaluator setup/calibration may dominate.
**Dependencies:** lawful reproducible support and a fair baseline; new plan and
user approval. No automatic approval of lane/classes/order.

### B. Narrow to a substantive aggregate-sufficiency study

If a strong simpler representation resolves the proposed distinction but an
important unresolved domain boundary remains, present a bounded sufficiency
question and proposed evidence/contribution, not a relabeled lack of benefit.

**Pros:** less complexity; answers the resolution question honestly.
**Cons:** may overlap existing knowledge; meaningful domain-specific evidence
can still be expensive.
**Dependencies:** distinct scope and later evidence plan explicitly approved
by the user; not an automatic substitute for the lane hypothesis.

### C. Halt or defer

Use when overlap settles the question, no credible contrast survives, fair
evaluation is inaccessible, or sufficient evidence would require unjustified
scope/Gap7 changes. Distinguish refutation from insufficient evidence/access.

**Pros:** avoids unnecessary construction and novelty rescue.
**Cons:** a qualified opportunity can remain untested.
**Dependencies:** archive the reasons and exact unresolved claim; no mainline
project change or task expansion follows automatically.

**Recommendation at this planning stage:** execute this bounded review once
approved; no outcome route is preselected. At RB-UG1 recommend the smallest
evidence-justified option, or stop earlier with findings and costs. Any task
boundary, policy tradeoff or Gap7 exception requiring new authority triggers an
immediate explicit user gate. Review execution does not continue beyond it.
