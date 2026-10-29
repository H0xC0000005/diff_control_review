# N2 protocol proposal — F1 evidence review to the next scientific choice

**Archive status: Historical superseded draft; not current execution authority.**
Preserved on 2026-09-17 during package consolidation. The original drafting
status/text below is retained. Use the [approved N2 protocol](../../s02_00_n2_review_protocol_plan.md)
for its completed review pass, not this draft.

Status: **Proposed; execution awaits user approval**  
Prepared: 2026-09-16 (session date)  
Basis: candidate A selected after N1 findings/gate discussion, including the
Gap 7 restriction, focused Gap 8 novelty target, and matched-action correction.

Evidence basis:
[`N1 findings report`](../../reporting/s01/s01_20_n1_findings_report.md)
and [`accepted N1 gate`](../../reporting/s01/s01_30_n1_user_gate.md).

## 1. Authorization and intended stopping point

The user has approved candidate A: narrowed infrastructure speed-advisory
control upstream of an exogenous freeway lane-capacity reduction. The current
task authorizes **drafting this protocol**, recording that decision, and
synchronizing its documentation—not conducting the post-N1 review.

On approval, this protocol authorizes only the first, decision-focused segment
of the full F1 review, called N2 here. It ends at **N2-UG1**, where the user must
decide whether the evidence supports a distinctive, feasible minimum-information
study and which working study scope deserves detailed P2-P4 planning. There is
also an earlier consolidated paper-access gate or an early scientific stop if
decisive disqualifying evidence appears.

The findings-dependent choice cannot be closed from N1: the literature supports
aggregate VSL control, compliance effects, and lane/merge interactions, but N1
did not establish a matched aggregate-model ranking failure or deeply exclude
direct predecessors. We must examine those claims before committing to model
architecture, exact equations, or experimental construction.

**Two gates are distinct:** approve this executable review protocol now; decide
the scientific route at N2-UG1 after its findings. Neither gate automatically
authorizes implementation.

## 2. Fixed inputs, working hypotheses, and non-goals

### Accepted inputs

- Task-first, model-second; the urban simulator, state representation, code,
  and paper organization are not constraints on the freeway answer.
- Primary action: continuous infrastructure speed advice by upstream spatial
  zone and update interval. Advice is not direct vehicle-specific CAV actuation.
- Closure location, affected lanes, geometry, and closure/reopening schedule are
  exogenous structural/scenario inputs. Low, near-capacity, and high demand are
  relevant regimes; temporary closures require F4 post-reopening recovery.
- **Primary matched actions:** B0, B1, and B2 receive the same link-level advice
  schedule and feasible action set. A lane-group model applies that shared
  advice to its lanes. Lane-specific advice is not part of this primary contrast
  or an automatically authorized N2 extension.
- Shared population, demand, objective accounting, and horizon; do not hide
  residual queue or move delay outside the evaluation population/window.
- One candidate contribution: the minimum retained information needed for
  useful cross-fidelity speed-advisory sensitivities, including conditions of
  simpler-model sufficiency. Component assembly is not automatically novel.
- Avoid control-dependent discrete probability shifts and hybrid transitions
  requiring event-time/saltation corrections by default. An indispensable
  exception requires evidence against adequate continuous/deterministic
  alternatives, separate user approval, and dedicated fidelity/approximation
  and estimator bias-variance work where applicable.

### Working hypotheses, not selected implementations

- B0: strong homogeneous link-aggregate traffic/model-control baseline.
- B1: continuous aggregate mass by fixed exogenous compliance/response cohort.
- B2: continuous lane-group cohort mass with endogenous, deterministic,
  mass-conserving lateral transfer; lane-change commands are not actions.
- An independent microscopic evaluator can assess matched perturbations/rankings.

B0 is a **baseline family**, not permission to use an artificially weak
single-queue model when spatial propagation or continuous speed dynamics are
necessary. Inspect link-queue, LWR/CTM/LTM, and METANET predecessors for actual
task adequacy. If a credible stronger aggregate baseline changes the working
ladder's meaning, report the smallest amendment at the user gate; do not bury it
in an adapter or select a weak comparator to preserve apparent novelty.

Continuous cohort/lane traffic mass is not inherently a categorical sampling
distribution. Fixed seeds also do not remove sensitivity from control-dependent
choice probabilities. These distinctions apply to the differentiable candidate;
paired exogenous scenarios in a richer evaluator remain admissible.

### Not authorized in this segment

- Simulator/controller/optimizer implementation, coding a reference experiment,
  numerical traffic runs, parameter fitting, package installation, or detachment.
- Exact model selection, class counts, lane partitions, numerical tolerances,
  seeds, optimization budgets, scenario datasets, or an implementation plan.
- New VSL algorithms, microscopic behavior theory, stochastic estimators, or
  saltation methods merely to rescue novelty.
- Regulatory-VSL transfer as a new primary task, direct CAV commands, F2/F3/F5
  reopening, lane-specific actions, routing, closure scheduling, safety theory,
  field deployment, or network expansion.
- Modifying project/milestone files, source, tests, configs, environment, user
  feedback, original results, or closed review packages.

Boundary studies remain inspectable as prior art; exclusion from the task must
not be used to dismiss substantively overlapping results.

## 3. Questions, ownership, and discussion order

This is a scientific review, not component construction. There are no artificial
D_i/E_i coding checkpoints. The following global/local classification prevents
source transcription from silently deciding shared scientific contracts.

| ID | Class/status | Core question | Owner and dependencies |
|---|---|---|---|
| N2-G0 | Type 2; accepted input | What task, shared action, exclusions, and Gap 7 restrictions govern N2? | User-approved N1 boundary; input to every question |
| N2-G1 | Type 2; open | Is the substantive resolution-to-useful-sensitivity question already answered by direct predecessors? | Review synthesis; user decides consequence; depends on G0 |
| N2-G2 | Type 2; open | What strong-baseline information loss could change a feasible intervention or action ranking under this same action? | Review synthesis; depends on G0/G1 and C1-C3 |
| N2-G3 | Type 2; open | Can candidate models and an independent evaluator share a credible traffic, action, calibration, and accounting contract? | Review synthesis; depends on G0 and C1/C4 |
| N2-G4 | Type 2; open screen | Can proposed mechanisms plausibly avoid prohibited-by-default stochastic/hybrid sensitivities? | Review synthesis; restriction fixed by G0; evidence from C2/C3/C5 |
| N2-G5 | Type 2; pending findings | Retain the ladder, narrow its study scope, refine the decisive contrast, or halt/defer? | User at N2-UG1; depends on G1-G4 |
| N2-C1-Q1 | Type 1; extraction | What equations, state, control, capacity-drop/recovery assumptions, and checks do strong aggregate sources actually use? | Baseline source studies; informs G2/G3 |
| N2-C2-Q1 | Type 1; extraction | How do sources map advice to cohort response, and is membership fixed or endogenously switched/sampled? | Compliance source studies; informs G2/G4 |
| N2-C3-Q1 | Type 1; extraction | What lane state and lateral behavior are retained, and what changes in action or vehicle assumptions confound their reported gains? | Lane/merge source studies; informs G2/G4 |
| N2-C4-Q1 | Type 1; extraction | What inspectable model documentation, calibration data/parameters, and action interfaces support a richer evaluator? | Evaluator feasibility study; informs G3 |
| N2-C5-Q1 | Type 1; extraction | Which derivatives and event/probability assumptions are actually verified in predecessor models? | Derivative source studies; informs G4 and later P3 |

**Mixed splits:** class necessity is G2/G5, while source class/parameter
transcription is C2; lane-state-versus-actuator attribution is G0/G2, while
source transfer-law transcription is C3; cross-fidelity fairness is G3, while
capability/API transcription is C4; stochastic/hybrid admissibility is G0/G4,
while derivative-term extraction is C5. Local work cannot redefine a global
contract.

**Order:** confirm G0; prioritize G1 and initial G3/G4 fatal screens; inspect
component sources serially as needed to support G2-G4; synthesize G1-G4 together;
stop for G5. Proposed exact P2-P4 design choices remain open after this segment.
If a source exposes a conflict with G0, document and reopen that smallest input
with the user rather than adapting the task during extraction.

## 4. Review work and evidence obligations

### N2-R1 — predecessor review and early fatal screens (P0 first)

1. Audit inherited metadata, versions, full texts, and claim locations before
   new discovery. N1 E1/E2 records do not become E3 by citation or repetition.
2. Inspect nearest substantive prior art, especially lane-group VSL with a
   microscopic evaluator (FB0013), lane/multiclass CTM with joint control
   (FB0004), aggregate lane-drop VSL (FB0001), VSL variations/gradients
   (FB0002), macroscopic response/compliance (FB0003), and their citation
   neighborhoods. FB0007/FB0010/FB0014 are actuator-boundary comparisons.
3. Separate three kinds of overlap: established building block; similar control
   task/evaluator; substantive prior answer to the central causal question.
   An exact B0/B1/B2 naming match is not required to invalidate novelty.
4. Perform initial evaluator/access/calibration and Gap 7 screens now. Do not
   wait until detailed architecture to discover an indispensable inaccessible
   dataset, direct-vehicle actuator, or stochastic/hybrid derivative requirement.

Output: source-backed predecessor overlap map and preliminary G1/G3/G4 findings.
If decisive disqualification is found, prepare an early N2-UG1 packet and stop;
do not mine unrelated mechanisms or new algorithms to rescue the task.

### N2-R2 — strong baseline, decision contrasts, and minimum-state feasibility

1. Establish what the strongest aggregate baselines represent, including
   propagation, realized speed response, storage, capacity drop, and recovery.
   Retain counterevidence: simpler feedback sufficiency, no-drop VSL ineffectiveness,
   aggregate multiclass sufficiency, or an unidentifiable compliance effect.
2. Extract contrasts that separate cohort composition, lane occupancy/merge
   pressure, and speed-response dynamics. Mark whether total aggregate state,
   advice, demand, population, and objective are genuinely matched.
3. Identify which omitted variable could alter actions/rankings rather than only
   trajectory detail. Do not infer ranking failure solely from better prediction,
   improved joint-control performance, or internal optimization success.
4. Build a small model-adoption register: source responsibility/I-O/state,
   equations/units at source locations, original assumptions, proposed minimal
   adaptation, confounding removed, conservation implications, and derivative
   hazards. This is an evidence register, not a frozen implementation interface.
5. Complete a feasibility screen for the common evaluator/traffic contract:
   advice realization, cohort mix, closure schedule, storage, bottleneck
   discharge/drop/recovery, metrics/horizon, parameter/data access, and source
   independence. Inspect installed APIs or official software docs only if a
   decision-grade feasibility claim depends on them; record versions. Do not
   install software or run a calibration/test campaign.
6. Screen candidate response, lateral-transfer, and capacity-drop laws for
   genuine discontinuous resets, event-time sensitivity, and moving categorical
   probabilities. Distinguish those from deterministic continuous-mass kinks.

**Strength of gap evidence, recorded separately from source access:** mechanism
only; controlled forward contrast; matched decision/action-ranking contrast;
verified model derivative; independent useful-sensitivity result. A full source
can be E3 for a mechanism yet provide no ranking evidence. A mechanism plus an
explicit reviewer-proposed contrast remains qualified, not a demonstrated gap.
Analytical arguments must state their assumptions and independent basis; no
new numerical experiment is permitted to upgrade evidence during N2.

Output: a gap/counterevidence register, provisional minimum-information map,
model-adoption register, evaluator screen, and admissibility screen.

### N2-R3 — substantive findings and N2-UG1

Produce one primary `reporting/s02/s02_20_n2_findings_and_gate.md`. It must explain the
actual scientific findings before asking for a choice:

- key predecessor methods and quantitative/qualitative results with relevance
  and limitations, not just procedural pass labels;
- which purported gaps are closed, survive, or remain unknown;
- strongest aggregate/multiclass counterevidence and what it rules out;
- original source model chain versus each proposed adaptation;
- attribution of a possible failure to compliance, lane state, speed dynamics,
  changed action, or incompatible calibration;
- novelty overlap, matched-action and recovery accounting, and Gap 7 findings;
- minimum remaining evidence cost and an interpretable next-study scope;
- recommended choice, genuine alternatives, dependencies, and exact work that
  would require a new plan if chosen.

The review must not claim to have proven minimum state or external gradient
usefulness merely by synthesizing papers. A decisive result may instead be that
only a well-grounded diagnostic hypothesis survives.

## 5. Search, screening, source access, and archive discipline

### Reuse and discovery

Reuse N1 records and cross-package full texts in place. Verify DOI/title/version
and claim boundary; do not duplicate or rewrite closed archives. Prioritize
FB0001-FB0005, FB0010-FB0014, and SEO2026 for F1; RM0024/RM0025 supply general
discrete-derivative lineage, not task-level F1 novelty evidence. N1's summary
query log is context; N2 logs exact executed queries and retrieval details.

Discovery uses official agency guidance, primary publisher/author/university
repositories, research indexes for leads, and arXiv. Follow backward/forward
citations of the nearest predecessors; explicitly update recent arXiv and
published versions through the actual execution date. No start-date cutoff;
English is the working language, with decision-critical other-language sources
logged rather than silently excluded. Do not rely on future-dated work without
verifying availability/version/date.

Required query families, specialized as sources reveal terminology:

- lane-drop/closure VSL link-queue/LWR/CTM/METANET capacity drop feedback;
- speed-advisory compliance heterogeneous/multiclass response and calibration;
- lane-group/multilane speed advice, endogenous lateral flow, mandatory merges;
- VSL sensitivity/discrete adjoint/automatic differentiation/piecewise dynamics;
- macro-micro controller transfer, perturbation/action ranking, matched fidelity;
- temporary closure/reopening recovery and residual-queue accounting;
- simpler-model sufficiency, no VSL benefit, poor transfer, compliance limits,
  and baseline/calibration confounding;
- control-dependent categorical sampling, hybrid capacity transitions, and
  deterministic alternatives, solely to screen admissibility—not to develop a
  new estimator or broaden the task.

Include sources that address G1-G4 directly or a labeled transferable method.
Exclude generic prediction, undefined resolution labels, changed actuators as
direct primary-task evidence, and claims without inspectable support. Keep
boundary and excluded records in the log. Use research indexes/reviews for
discovery, but primary texts/official documentation for technical conclusions.

Search completion requires every decision-critical claim to have direct
support, explicit counterevidence, or a recorded unresolved gap; all required
query families and nearest-predecessor citation frontiers must be checked. One
additional targeted frontier pass must add no new substantive decision category
before a bounded absence statement is made. Log that stopping rationale. No
paper quota or weighted novelty score substitutes for coverage; if closure
requires an expanding new task/community, stop for the user rather than broaden.

### Claim extraction and evidence levels

Reuse E3/E2/E1/E0 meanings from N1. Each claim records source/version/access,
exact page/section/equation/figure, actuator, state/units, scenario/population,
objective/horizon, baseline fairness, derivative target/check, evaluator,
reported result, direct statement versus reviewer inference, and limitation.
Unsupported novelty absence or causal conclusions are never upgraded by source
count. Record contradictions and missing comparisons explicitly.

Archive lawfully accessible new texts with unique IDs, URLs, retrieval dates,
versions, filenames, and SHA256 hashes; append to the manifest without changing
old entries/files. Web-only full texts get stable metadata and method/result
locations, plus a lawful snapshot where practical. Store new audit products
with `n2_` names so N1 evidence is preserved.

### One institutional-access batch for this segment

Reassess FB0013 at N2 depth: being noncritical to N1 selection does **not** make
it noncritical to a direct-predecessor novelty decision. First check lawful open
published/manuscript/author versions and adequate direct alternatives. Critical
inaccessible records stay E1 until obtained.

If necessary, consolidate one request in
`reporting/s02/s02_10_n2_institutional_access_batch_1.md`: ID, citation/DOI, G question,
needed method/result locations, why alternatives are insufficient, and requested
version. Ask the user to place lawfully obtained papers in
`archive/user_supplied/`; never request credentials or circumvent access.
Pause at the request. This protocol permits no second access batch; newly
uncovered inaccessible dependencies remain gaps for N2-UG1 unless the user
explicitly approves a separate refinement. Do not reinterpret lack of access as
either novelty or macro sufficiency.

## 6. Outputs and verification

On protocol approval, freeze an approved copy in the active review package as
`s02_00_n2_review_protocol_plan.md`, preserving this Phase A proposal and dialogue.
This is a review protocol, not an approved `docs/milestones/` implementation plan.

Create artifacts only when their work opens:

- `search/n2_query_log.csv`, `search/n2_coverage_map.md`;
- `screening/n2_records.csv`, `screening/n2_decisions.csv`;
- `extraction/n2_claims.csv`, `extraction/n2_source_studies/<source_id>.md`;
- `synthesis/s02/n2_predecessor_overlap.md`, `synthesis/s02/n2_gap_register.md`;
- `synthesis/s02/n2_model_adoption_register.md`;
- `synthesis/s02/n2_evaluator_contract_screen.md`, `synthesis/s02/n2_admissibility_screen.md`;
- `reporting/s02/s02_20_n2_findings_and_gate.md` and a concise work/dialogue record;
- appended archive manifest/metadata and new texts where lawfully available.

Check CSV schemas/IDs, relative links, source locations and version references,
manifest hashes, claim-to-source traceability, and G0/global-local consistency.
Inspect consequential reported numbers against source tables/text. If substantial
mathematics is needed for the human-facing explanation, verify LaTeX and render
a linked PDF with retained source under repository conventions; do not omit
the mathematics or put a complex derivation only in chat.

No code tests or scientific runs are acceptance requirements for this review
segment. Source inspection and document/audit consistency are its checks.

## 7. Next scientific choice: N2-UG1

### Problem statement and model-chain function

Does F1 still warrant a minimum-information study after deep predecessor and
strong-baseline review, and what scope should proceed to detailed evidence/model
planning? The intended eventual chain is shared infrastructure advice → candidate
continuous-mass traffic dynamics → checked derivatives → matched independent
action evaluation. N2 selects no implementation of that chain.

### Core gap to be resolved

The decision depends on review findings about substantive novelty, supported
ranking-failure mechanisms, minimum plausible added information, shared evaluator
feasibility, and compliance with Gap 7. These cannot be inferred safely from
N1's mechanism-level support. Exact class/lane equations, calibration tolerances,
and gradient-usefulness tests remain later design decisions.

### Candidate routes for the findings packet

Present only evidence-viable routes at the gate, in expanded problem/function/
gap/candidates format; preserve rejected routes and reasons in the audit.

**Route A1 — retain the compliance-first working ladder for detailed P2-P4 review.**
Applicable if a distinctive decision gap and viable evaluator/admissibility
contract survive. Plan B0/B1 first, with B2 conditional on the lane mechanism.
**Pros:** isolates information and preserves a strong simpler comparator.
**Cons:** model-level and external ranking benefit remain unproved; calibration
may dominate burden. **Dependencies:** a new detailed review/task-design plan;
no inference that all three implementations must be built or B2 will win.

**Route A2 — narrow to a smaller or sufficiency-focused study.**
Applicable if findings favor B0/B1 or a meaningful unresolved boundary of simple-
model sufficiency rather than the full ladder. **Pros:** less complexity and a
sharper causal question. **Cons:** negative/equivalence work needs a substantive
domain/contribution, not merely an absence of richer benefit. **Dependencies:**
explicit user approval of the narrowed scientific question and acceptance logic;
do not relabel an already-established result as novelty.

**Route B — bounded evidence/contrast refinement before detailed design.**
Applicable if an unresolved mechanism has a concrete, finite missing evidence
contract but cannot yet justify A1/A2. **Pros:** avoids premature construction and
can target the decisive ambiguity. **Cons:** may end in no viable task or incur
extra access/calibration burden. **Dependencies:** specify the missing claim,
smallest evidence activity, cost, and stop condition; any diagnostic experiment
requires a separately approved experiment plan, not N2 authorization.

**Route C — halt or defer F1.**
Applicable if prior work covers the substantive contribution, no meaningful
decision gap survives the strong baseline, or feasible fair validation requires
unjustified mechanisms/access. **Pros:** avoids novelty rescue and unbounded
modeling. **Cons:** leaves qualified opportunities untested. **Dependencies:**
record whether this is overlap, absence of motivation, or insufficient evidence;
do not conflate lack of access with proof that richer information is unnecessary.

No outcome-dependent recommendation is fixed now. The protocol recommends
evidence-first routing and stopping at this gate. If Gap 7 requires an exception
or G0 must change, stop for that explicit user choice rather than continuing
under any route by implication.

## 8. Completion/stop criteria and current handoff

This segment succeeds when N2-UG1 has a substantive source-backed findings
packet, traceable evidence/counterevidence, clear remaining gaps, and a justified
route recommendation. A well-supported halt/defer is a successful review result.

Stop earlier for decisive novelty overlap, unsupported decision motivation after
bounded coverage, changed-actuator entanglement, infeasible fair evaluation,
indispensable prohibited-by-default sensitivity, critical access request, or
scope conflict. Write the diagnosis and smallest viable routes; do not weaken
criteria, silently add mechanisms, or begin later P2-P4 design.

**Current status:** candidate A selected; N2 protocol proposed. Approving this
protocol would authorize N2-R1 through N2-R3 until N2-UG1 or an earlier stop.
The current drafting task ends here for protocol approval. No new literature
search, model experiment, or implementation was performed during drafting.
