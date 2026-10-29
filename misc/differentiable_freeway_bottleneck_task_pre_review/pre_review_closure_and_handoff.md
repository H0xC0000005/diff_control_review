# Pre-review closure and handoff — differentiable freeway bottleneck task

Date: 2026-09-16  
Status: **Closed; ready for a fresh-agent review opening**

## 1. Why this handoff exists

The current dialogue accumulated several literature reviews, project-document
audits, and Milestone 2 discussions. The new freeway work is semantically
different: it explores a possible parallel task without treating the existing
urban simulator as a fixed starting point. The user therefore chose to close
this pre-opening discussion and initialize the formal review with a fresh agent.

This file is the authoritative concise handoff. The new agent should not infer
review decisions from the older conversation when this record supplies them.

## 2. Decision that closed the pre-review

The user approved **N1 — a bounded task-framing sprint followed by a user gate**.

N1 will:

- use a freeway lane-capacity-reduction bottleneck as the operational anchor;
- define and compare candidate intervention/task formulations;
- examine their strongest lower-resolution baselines;
- identify what traffic information, if any, is necessary beyond those
  baselines;
- assess whether a credible derivative and gradient-usefulness experiment can
  be formulated; and
- stop before a full task/model review so the user can select one candidate,
  request refinement, or halt the branch.

N1 is approved as the next review mode. Its detailed executable protocol,
search boundaries, phase names, evidence codebook, artifacts, and gates have not
yet been drafted or approved.

## 3. Fixed methodological principles for the new review

### P1 — task first, model second

Start from the operational decision and research question. Determine the minimum
credible model afterward. The present simulator is neither an admissibility
constraint nor the default implementation.

### P2 — the common ground is the resolution question

The urban and freeway branches share this high-level question:

> What traffic resolution is necessary to produce credible and useful gradients
> for the selected control decision?

They do not have to share the same mesoscopic state, equations, simulator,
software, implementation, paper, or answer.

### P3 — do not assume mesoscopic value

Macro sufficiency, a hybrid requirement, a microscopic requirement, or an
infeasible task are all admissible conclusions. The review must not be designed
to prove that mesoscopic detail wins.

### P4 — name retained information, not only model level

“Mesoscopic” is ambiguous in freeway literature. Describe candidates using what
they retain: route/traveler identity, cohort/packet identity, class/compliance,
lane state, arrival order, speed/headway distribution, gap state, explicit
lane-change interaction, or another concrete quantity.

### P5 — lower-resolution baselines must be strong

The review must compare a richer candidate with the strongest credible
task-specific macro, multiclass, cohort-memory, feedback, MPC, adjoint, or other
baseline. It may not manufacture value by choosing an artificially weak macro
model.

### P6 — derivative correctness and gradient usefulness are separate

A differentiable or adjoint model is not valuable merely because it returns a
gradient. The review must foresee both a derivative-validation contract and an
independent test of whether the action direction/ranking is useful in a richer
reference.

### P7 — paper and code unity remain outcomes

Whether the freeway and urban branches become one paper, two papers, share
components, or diverge completely is decided after task/model evidence. It must
not constrain task selection.

### P8 — compatibility is a later secondary audit

If the selected freeway task requires acceleration, safety gaps, speed dynamics,
lane changes, or other absent mechanisms, that is a model requirement rather
than evidence against the task. Common-ground reuse and engineering cost are
assessed only after the task and minimum model are justified.

## 4. Operational anchor and provisional task candidates

The shared anchor is a **temporary or permanent freeway lane-capacity reduction**
caused by an incident, maintenance/work, or physical lane reduction. Low,
near-capacity, and high-demand regimes and post-event queue clearance are
important scenario dimensions.

The first formulation should treat closure location, affected lanes, and the
closure/reopening schedule as exogenous. Optimizing those structural events is a
separate discrete-decision branch.

| Candidate | Pre-review role | Main question |
|---|---|---|
| F1: speed harmonization or speed/advisory control | Primary first screen | Does lane/class/compliance or richer response state change useful speed-control gradients beyond a strong aggregate VSL/capacity-drop model? |
| F2: coordinated upstream ramp metering | Co-primary screen and strong comparison family | Does the lane-reduction setting create a representation-sensitive control problem beyond aggregate density, supply, ramp storage, and strong existing gradient/control methods? |
| F4: post-reopening recovery | Required scenario dimension if a temporary closure is selected | Does a queue persist, and should control remain active after physical capacity returns? |
| F3: joint metering and speed control | Expansion candidate | Do coupled actuators add a distinct question after F1 or F2 is independently justified? |
| F5: cooperative lane-change/merge-priority control | Boundary or separate-project candidate | Are explicit local maneuver/safety interactions the necessary resolution, and can they support a credible gradient contract? |

This list is provisional, not exhaustive. N1 may add a materially distinct
literature-supported candidate, but it should not broaden merely to catalog all
freeway control.

## 5. Shared research-question backbone

N1 should preserve the following backbone while simplifying it as needed in the
formal protocol:

| ID | Question |
|---|---|
| CQ1 | What operational decision, disturbance, feasible action, horizon, objective, and constraints define the task? |
| CQ2 | What is the strongest credible lower-resolution model/control baseline? |
| CQ3 | Where does that baseline lose decision-relevant information? |
| CQ4 | What minimum additional state closes the demonstrated gap? |
| CQ5 | Can the selected model's derivatives be defined and checked credibly? |
| CQ6 | Do those derivatives improve action directions/rankings in an independent richer evaluator? |
| CQ7 | Is the fidelity gain worth its modeling, calibration, computation, and validation burden? |

## 6. Terminology finding inherited by N1

The pre-opening quick scan found five broad freeway “mesoscopic” directions:

1. large-network individual-agent mesoscopic DTA with aggregate link movement;
2. vehicle/packet/platoon tracking over CTM/LTM or queue physics;
3. lane-aware, multiclass, simplified operational models;
4. kinetic/distributional traffic-flow models; and
5. hybrid or multiresolution models with local microscopic detail.

These directions retain different information and support different claims.
N1 must treat mesoscopic as a descriptive family, not as the target resolution.
See `freeway_mesoscopic_meaning_quick_scan.md` for the semantic map and sources.

## 7. Source reuse and provenance

### Read before searching

- `temp_content/feedback/email_trace_20260916.md` — the colleague exchange that
  motivates the new task-first review.
- This package's `feedback22_email_trace_response.md` — detailed candidate and
  methodological provenance.
- This package's `freeway_mesoscopic_meaning_quick_scan.md` — terminology scan
  and representative source links.
- `misc/selective_discreteness_ramp_metering_review/reporting/closure_record.md`
  — scope and bounded conclusion of the old ramp review.
- `misc/selective_discreteness_ramp_metering_review/synthesis/feedback20_evidence_debate.md`
  — existing freeway gradient, macro-control, and mesoscopic evidence.
- `misc/selective_discreteness_ramp_metering_review/archive/manifest.csv` and
  `archive/metadata/feedback20_sources.md` — already archived source inventory.

### Important reusable records

- RM0024: Reilly et al., discrete-adjoint coordinated ramp metering; full public
  manuscript archived.
- RM0025: Goatin et al., multiclass network discrete adjoint; full open version
  archived.
- RM0026: Gu et al., smoothed-CTM ramp metering; bounded metadata/method evidence.
- The quick scan links authoritative FHWA definitions/guidance, DTALite,
  POLARIS, Anisotropic Mesoscopic Simulation, traffic-flow taxonomy,
  gas-kinetic models, and hybrid meso-micro simulation.

The new review should reuse these files before querying the same sources. New
metadata and full texts should be archived in the new sibling package with an
access/evidence-level record. If institutional access becomes necessary, request
one batch from the user rather than repeated paper-by-paper interruptions.

## 8. What is closed and what remains open

### Closed here

- interpretation of the email trace;
- selection of N1 as the next review mode;
- task-first/model-second hierarchy;
- high priority of “do not assume mesoscopic value” and “do not force paper/code
  unity”;
- the common-ground statement as a resolution question only;
- correction that incompatibility with the current simulator is not a task-risk;
- a sufficient semantic scan of freeway uses of “mesoscopic”; and
- the provisional F1/F2/F4/F3/F5 roles.

### Open for the fresh agent and user

- the executable N1 review plan and its precise gate sequence;
- final N1 research questions and inclusion/exclusion rules;
- exact search sources, query families, date/language limits, and stopping rule;
- the evidence-quality and task-comparison codebook;
- whether F1, F2, or another candidate survives N1;
- the minimum model and richer evaluator for any surviving candidate; and
- whether a subsequent full review should open.

## 9. Explicit non-effects and prohibitions

- Do not modify `AGENTS.md`, `PROJECT_CONTEXT.md`, `PLANS.md`, milestone archives,
  source, tests, configs, or the accepted urban-task review.
- Do not reopen or rewrite the closed ramp review. Its conclusion answered a
  different compatibility-framed question and remains valid within that scope.
- Do not treat the current project as a required backbone or comparison target
  during task selection.
- Do not implement a simulator, controller, experiment, or project amendment.
- Do not decide in advance that the output must be one paper or share code.

## 10. Closure statement

The pre-opening discussion has fulfilled its purpose: it interpreted the
colleague feedback, selected the N1 approach, corrected the compatibility bias,
and supplied enough terminology and provenance for a fresh agent to design the
formal review without relying on the long dialogue. No unresolved issue prevents
the new agent from drafting the N1 protocol.
