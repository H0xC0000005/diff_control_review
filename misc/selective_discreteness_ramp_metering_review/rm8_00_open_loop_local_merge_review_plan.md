# RM8.00 — Open-loop local ramp merge predecessor and mechanism review

Date: 2026-10-01. Status: **Closed 2026-10-01 with RM8-UG1.A approved.**
Parent: [RM7 closure and continuation decision](discussion/rm7_open_loop_approval_and_rm8_opening.md).

## Authorization and purpose

The user approved RMD-G1.A, accepted the recommended initial approaches as
resolving the hanging planning decisions, and instructed continuation to the
next discussion point. This protocol makes that approved review approach
concrete. It does not introduce a new action, accounting choice or model
adoption requiring renewed approval.

The purpose is to determine which local merge mechanism/model family, if any,
deserves detailed task formulation for the minimum-information question.
The next discussion point is evidence-dependent: **RM8-UG1 model-family/
formulation admission**. No implementation or traffic experiment is authorized.

## Accepted planning contracts

- RMT-R1.A: one finite-storage controlled on-ramp, multilane mainline and local
  merge/acceleration region; method-first, independent of project progress.
- RMD-G1.A: common bounded open-loop metering-rate schedule or rate
  perturbation family; no gain optimization or MPC execution as the primary task.
- RMD-G2: inspect a minimum-information ladder before choosing a representation.
  Published detailed models supply evidence and candidate references.
- RMD-G3: strong declared road-total mainline and ramp history plus shared
  geometry, demand and future forcing; exact matched-history construction is the
  first analytic target. Approximate/conditional evidence requires an explicit
  claim change, not silent substitution.
- RMD-G4: smallest mechanism-isolating local traffic family, grounded against
  operational evidence; complete all-stream delay/time through common clearance.
- RMD-G5: establish forward decision relevance before adopting derivative
  semantics. Prefer deterministic/piecewise-smooth sensitivity if supported;
  evidence-dependent stochastic/event methods are not pre-approved.
- RMD-G6: staged evidence review. Gradient correctness and one-step independent
  usefulness are distinct targets; full optimization/feedback performance is
  later work.
- RMT-R1.C multi-ramp task remains a possible extension after positive local
  results and a separate user decision.
- Aggregate sufficiency, scalar-state sufficiency, an incomplete gradient path
  or a supported negative result are valid findings.

Planning decisions are closed for this pass. Evidence questions remain open:
neither lane necessity nor a hidden-history pair is assumed.

## Questions, classification and ownership

| ID | Type / owner | Evidence question | Dependencies |
|---|---|---|---|
| RM8-G0 | Type 2, accepted user input | What action, observation, accounting and scope contracts govern the review? | RM7 continuation decision |
| RM8-G1 | Type 2, synthesis; user decides consequence | What has direct local-ramp prior art already established? | G0; source studies |
| RM8-G2 | Type 2, synthesis | Which mechanism plausibly hides consequential information beyond aggregate/history/compact state? | G0/G1 |
| RM8-G3 | Type 2, synthesis | Can matched rates and complete outcomes isolate the information effect fairly? | G0/G2 |
| RM8-G4 | Type 2, synthesis | What derivative-correctness and one-step-usefulness evidence exists or is missing? | G0/G2/G3 |
| RM8-G5 | Type 2, user at RM8-UG1 | Which family should enter detailed analytic task formulation, or should this branch halt/refine? | G1–G4 |
| RM8-E1 | Type 1, source extraction | Actual macro states, queue/merge rules and derivative assumptions | Fixed G0; informs G1/G2/G4 |
| RM8-E2 | Type 1, source extraction | Empirical isolated-merge mechanisms and tested meter interventions | Fixed G0; informs G2/G3 |
| RM8-E3 | Type 1, source extraction | Lane/group/gap laws, action confounds, conservation and events | Fixed G0; informs G2–G4 |
| RM8-E4 | Type 1, source extraction | Independent-reference capabilities and calibration/evidence limits | Fixed G0; informs G3/G4 |

These local owners are literature-extraction responsibilities, not coding
components or delegated agents. Source details cannot change G0. The mixed
issues split into source transcription E1–E4 and shared adoption/fairness G1–G5.

Order: confirm G0, inspect baseline and empirical predecessors, inspect richer
families and counterevidence, then synthesize G1–G4 and stop for G5.

## Work sequence

### R1 — source reuse, operational mechanism and direct predecessors

Reuse RM0002/3/4/11/14/24/25 and related freeway FB0030/S12 records in place.
Recheck critical texts before promoting historical access levels. Search
author/publisher/agency sources for isolated-merge metering, lane redistribution,
receiving/acceleration effects and strong aggregate alternatives. Follow the
closest empirical/theoretical predecessors rather than searching general
traffic optimization indefinitely.

Distinguish existing model/control building blocks from a prior answer to
matched hidden-information necessity and independently useful gradients.

### R2 — minimum-state and fair-task screen

Inspect aggregate supply/demand, capacity-drop memory, second-order speed and
compressed merge statistics before treating lane detail as necessary.
Inspect lane-continuous and hybrid/local-gap families without importing their
extra actuators. Extract whether metering alone can affect the stated mechanism.

Assess whether strong aggregate history could reveal the proposed hidden state.
Seek source-backed candidate pairs or an analytic route to constructing them;
do not claim a collision from different lane configurations alone.
Count ramp waiting, residual demand and mainline outcomes. Distinguish temporary
flow recovery from net complete-population benefit.

### R3 — derivatives and independent-reference requirements

Separate verified model derivatives from control improvement in the same model,
and both from independent one-step direction/ranking usefulness.
Inspect active receiving constraints, hysteresis, mode switches, acceleration,
events and stochastic gaps. Do not smooth or freeze them to obtain a gradient.

Screen reference requirements using literature/docs only. Do not install or run
SUMO or another simulator. No new numerical experiment is required to close
this review segment.

### R4 — findings and substantive gate

Prepare traceable evidence, counterevidence and a model-family admission packet.
Recommendations must state the source model, proposed adaptation, unresolved
matched-history/decision/gradient gaps and smallest next review work.
Stop before adopting equations, an exact scenario or a derivative estimator.

## Search and evidence discipline

Use primary technical sources and official operational/software documentation.
Index pages/abstracts screen leads; decision-critical model claims require method
locations or remain qualified. Preserve source versions and historical files.

Query families:
- isolated merge ramp metering capacity recovery, shoulder-lane queues, lateral
  spreading and all-stream accounting;
- aggregate CTM/ACTM/METANET merge/capacity-drop models, memory and consistency;
- lane-specific ramp models and autonomous redistribution under meter-only action;
- hybrid acceleration/gap merge models and rate-versus-release timing;
- ramp adjoints/sensitivities and matched independent gradient-direction tests;
- nearest-source citation frontier and recent publications.

Log executed queries and access, include counterevidence and actuator boundary
papers, and state limitations of bounded coverage. No paper quota or absence
claim based on failed retrieval. Stop if a decisive missing full text requires
user supply after lawful alternatives are checked; batch requests.

## Outputs

- rm8_00_open_loop_local_merge_review_plan.md
- search/rm8_query_log.csv and rm8_coverage_map.md
- screening/rm8_records.csv
- extraction/rm8_claims.csv and rm8_source_studies/
- synthesis/rm8_predecessor_and_information_map.md
- synthesis/rm8_task_gradient_reference_screen.md
- reporting/rm8_20_findings_and_gate.md
- reporting/rm8_90_work_report.md and rm8_current_handoff.md
- discussion/rm8_review_dialogue.md

Archive metadata/access links for newly inspected public texts; reuse existing
full texts rather than overwrite them. A source already assigned an RM/FB ID
keeps it; newly screened sources use RM8-P IDs in the RM8 record namespace.

## Acceptance and stop conditions

The pass is complete at a substantive gate when core source claims are traceable,
strong simpler alternatives are represented, possible hidden-state mechanisms
are separated from proven necessity, action/accounting fairness is assessed,
and derivative correctness/usefulness gaps are explicit.

Stop earlier for a material action/accounting change, evidence that only a
different task can expose the effect, indispensable unsupported stochastic/event
semantics, decision-critical inaccessible methods, or an expanding scope.
Current-code incompatibility is not a stop.

Validation is document/source consistency, identifiers, CSV schemas, relative
links and status pointers. No implementation milestone, production code,
configuration, environment or user feedback edits.


## Execution disposition — 2026-10-01

R1–R4 completed to the planned RM8-UG1 gate. Read the
[findings](reporting/rm8_20_findings_and_gate.md), [work report](reporting/rm8_90_work_report.md)
and [current handoff](reporting/rm8_current_handoff.md). The evidence pass is
finished, but RM8 user closure/model admission is pending. No successor opened.

## User closure — 2026-10-01

Candidate A approved; RM8 closed at conditional family admission. Earlier
pending-gate language in execution records is historical. Read the
[closure](reporting/rm8_99_predecessor_review_closure.md) and
[RM9 handoff](reporting/rm9_current_handoff.md). The user authorized the
bounded analytic review, now stopped at its first methodological allocation gate.
