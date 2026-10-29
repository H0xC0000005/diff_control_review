# Withdrawn historical document — not an active plan

The user clarified on 2026-10-21 that this review is analytical and
methodological. The executable scope below was never approved or run and
is withdrawn. Original text is retained, with relative links rebased for
this archive.

Original SHA256: 4862fbb020c378a2c13e5eef03b85ecee6cb25700e38f794fdee3ff11c157112

---

# Joined VSL candidate: handoff for validation planning

**Subsequent authorized task, 2026-10-21.** The user requests execution-plan
preparation after clarifying the next gate. That proposal is now delivered
for approval at VJV-P; this completed handoff remains its scientific input.

[Current executable-plan gate](../../../../../misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_joined_candidate_execution_plan_gate.md)

2026-10-21. **Review handoff complete. Constructibility accepted as sufficient
for the present review; executable validation remains unperformed.**

The modeling question now has a bounded answer: one published lane-density
framework can support the intended lane-information task with the selected
Han traffic budgets and one conservative flow-allocation replacement. We
have a complete candidate to test. The next question is whether it behaves
correctly in execution and whether its hidden lane information and gradients
actually help choose speed advice. The user defers detailed understanding
until those checks are available. This accepts constructibility; it does
not freeze every declared default or accept numerical or physical validity.

**The traffic picture and the limited adaptation.** A finite cohort occupies
a three-lane approach. E is the ending lane; A is its adjacent continuing
lane; B is the farther continuing lane. Drivers can redistribute while
advancing. Failed lane-change attempts may continue forward in the current
lane; traffic at E's actual end must merge into A or wait. One common speed
advice is chosen at the initialized decision and held until completion.
Subraveti supplies the density/incentive backbone. Han supplies the sending,
receiving and VSL budget lineage already present in the source discussion.
The allocator composes Carey/Wright sharing principles into the explicitly
qualified three-lane rule. This composition is an adaptation with stated
limits, not a native turnkey implementation or a transferred calibration.

**Read these four records before preparing execution.**

1. [Readable findings](../../../../../misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_joined_candidate_findings_and_checkpoint.md):
   the causal argument and what has, and has not, been established.
2. [Complete model and analytical qualifications, PDF](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.pdf):
   pages 1–2 define the model; sections 5–7 give the diagnostic pair,
   complete accounting and derivative. The
   [adjacent LaTeX source](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_contract_and_qualification.tex)
   retains the equations.
3. [Global assumptions and source/adaptation boundaries](../../../../../misc/differentiable_freeway_bottleneck_task_review/extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md):
   JA1–JA7 distinguish selected contracts, declared defaults and hypotheses;
   linked audits identify the primary papers actually read.
4. [Existing comparison and derivative-evidence contract](../../../../../misc/differentiable_freeway_bottleneck_task_review/synthesis/research_readiness/vsl_joined_candidate_verification_contract.md):
   the prospective scientific requirements governing validation. This
   handoff carries them forward; it adds no traffic law or replacement plan.

**What transfers as the starting member.** LF1 (attempts with forward
fallback) and LF2/H (the full Han budget) are user-selected. The concrete
review defaults are ten 100 m rows, 6 s updates, common nominal free/backward
speeds of 60/20 km/h, jam density 150 veh/km/lane, maximum capacity drop
10%, and advice between 30 and 60 km/h. The whole cohort starts inside the
road independently of advice; there are no later arrivals. A/B have free
outlets at the lane-drop line, where crossing completes a trip. There is
no downstream recovery zone. Incentive/lookahead, vacuum and boundary
conventions are specified in the mathematical record. The execution plan
must identify the member it will instantiate and make any proposed changes
visible before results; defaults are not permission for silent retuning.

The review establishes conditional mass/storage admissibility, a genuine
same-observation service contrast, finite complete remaining population-time,
an exact residual value and a regular-branch derivative. It does not establish
different best advice, a need for full lane detail, numerical derivative
agreement, optimizer advantage or physical fidelity. The allocator need not
maximize unrestricted total flow. No old S13 or point-model certificate
automatically transfers to these new equations.

**Validation should answer three questions in this order.**

1. **Does execution represent the declared traffic and count the whole
   cohort?** Check the budgets, shared allocation, fallback and simultaneous
   update against independent hand/reference cases before trajectory-level
   claims. Cover empty donors, saturated receiving, competing lateral
   requests, blocked attempts, E's compulsory merge, free outlets and the
   native mode boundaries. Require mass conservation, nonnegative stocks,
   storage/permission compliance and common donor/receiver budgets. Reproduce
   the prescribed diagnostic: penultimate densities are 37.5 in every lane;
   final E is 120 and final A/B are 60/90 or 90/60, with earlier rows empty.
   At advice 60, E service is 877.5 versus 1072.5 veh/h and total exit is
   4005 versus 4350 veh/h. These are exact static review references. Validate
   complete population-time using the exact low-mass residual; choosing a
   later index within that regime must give the same full objective within
   the declared numerical tolerance. Exact finite-time emptying is not a
   requirement, and deleting small residual stocks is not equivalent.

2. **Is the sensitivity of that complete objective correct?** On regular
   branch traces, compare the defined analytical/AD derivative with an
   independently evaluated complete-objective finite difference in double
   precision. Include finite-trajectory sensitivity, residual-state
   sensitivity and the residual's direct dependence on advice. Declare
   perturbation sequences, tolerances and branch-margin diagnostics before
   accepting agreement, and demonstrate a stable interval as perturbations
   decrease. Hold a valid residual index locally. At genuine switches report
   one-sided or finite-change behavior and possible jumps; do not force a
   smooth two-sided interpretation. Structural zeros need exact handling.
   Smoothing, density epsilons and the old continuous-time saltation rule
   cannot be added as implementation repairs to this fixed-step evaluator.

3. **Do the extra information and gradients improve decisions?** Use the
   same plant, cohort, action timing/bounds and complete objective throughout.
   Compare rowwise aggregate traffic; E plus rowwise A+B; that reduced state
   plus the last A-cell density; and separate lane densities. Match road
   locations and allow every observer to know the model and hidden-state
   distribution. The one-statistic observer identifies the diagnostic pair
   completely and is mandatory. Separate information value from optimizer
   performance: compare shared reduced-information advice with
   state-conditioned advice, then compare gradient use with bounded scalar
   search under equal information and declared budgets. Include maximum
   advice/no-control. Report actual feasible perturbation rankings and full
   objectives, search resolution and remaining optimization uncertainty;
   finite search is not a certificate of the global optimum. Zero action
   information value or no advantage over search is an admissible finding.

The diagnostic's hidden mode can become visible in later aggregate flow.
Its decision is made before that flow exists. Pre-decision histories or
repeated advice require a newly matched information/timing contract; a
snapshot cannot establish absolute unobservability. Likewise, a different
aggregate simulator tests a model change as well as an information change.

**Where the next responsibility begins and when it stops.** The separate
implementation/validation agent should first inspect the repository and
prepare the executable plan under its applicable approval workflow: concrete
component responsibilities, independent references, configurations, numerical
tolerances, commands, output records and acceptance checks. This handoff is
the scientific input to that plan, not implementation authorization and not
an opening of the repository's urban Milestone 2. Numerical and configuration
details belong there. There is no new unresolved modeling choice that must
be decided before that planning can start.

If a check fails, distinguish a transcription defect from a defect in the
declared method. Fix conformance errors within the authorized execution
plan. Stop and reopen the smallest affected scientific contract if the law,
state, boundaries, information/timing, objective or derivative must change;
do not hide such a change in clipping, tolerances or adapters. A null research
effect calls for an honest result, not automatic redesign to manufacture a
positive finding. Physical calibration and richer-simulator evidence remain
separate; SUMO is an optional later variation, not required for this handoff.

The review agent stops with this document and its preservation checks. The
accepted compact report and original Step 4 closure remain intact; separate
historical acceptance entries are not silently closed. Ramp construction
remains closed and urban revision is outside this transfer. No simulator,
dependency installation, traffic/gradient experiment, agent launch or external
message is part of this handoff.

[Handoff work record and document checks](../../../../../misc/differentiable_freeway_bottleneck_task_review/reporting/research_readiness/vsl_joined_candidate_validation_handoff_work_report.md)
