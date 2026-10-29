# Part-II scope decisions and readiness

Date: 2026-09-14
Migration note: moved to the dedicated ramp-metering review on 2026-09-14. Earlier references to execution inside the downstream-task package are superseded by this package's review_protocol_plan.md. Original decision text below is retained as history.
Source: feedback item 18 and the user's request to document the decision and assess readiness.
Status: Scope choices resolved; ready for explicit opening of Part II. Research execution has not started.

## Accepted interpretation

**Q1 — strict compatibility.** Preserve the simulator's backbone, continuous-mass semantics, closed component contracts and structural differentiation boundary. Investigate task-specific node/merge service dynamics as the candidate adaptation location. The feedback does not establish that a different solver is necessary, sufficient, or already authorized for implementation. Each candidate must identify changed equations, interfaces, state and evidence obligations. If feasibility requires a backbone change or other scientific expansion, stop and propose a separate common-compatibility review covering both TSC and ramp control. Do not assume such an extension in a positive feasibility verdict.

The user's phrase “m4(node solver)” is interpreted by function. The current `PLANS.md` identifies Component 0.4 as the accepted generic node solver, M3 as lane/allocation/storage/service design, and M4 as sensitivity analysis. No renumbering or permission to reopen Component 0.4 is inferred. The study must distinguish a task-specific operator using existing interfaces from a change to an accepted shared solver contract.

**Q2 — scientific diagnosticity.** A parallel task must test the selective-discreteness hypothesis or provide interpretable empirical evidence about its sufficiency. Generic optimization success or benchmark performance is insufficient. Simpler aggregate models matching the selective model can be a scientifically useful negative/sufficiency result if the comparison actually tests a justified mechanism; trivial agreement in a mechanism-free setting is insufficient to motivate the task.

**Q3 — minimum justified scope.** Begin with a single controlled on-ramp and local merge. Additional domain length, boundary conditions, lane/storage structure or interacting elements may be considered when required to expose a stated blockage/spillback or other diagnostic mechanism. For each increase record: the missing mechanism, why the simpler case cannot test it, the smallest additional structure, literature support, extra model dependencies and baseline/evaluator matching consequences. Scenario complexity may grow within strict compatibility; it cannot override Q1. Coordinated control or a materially different task family remains a scope-change gate.

## Readiness assessment

The purpose, compatibility limit, promotion criterion and complexity rule are now sufficiently explicit. No critical user scope choice remains before opening a focused feasibility review. Whether lane changes, an independent speed state, different merge dynamics or more complex geometry are necessary are research questions, not decisions the user must guess beforehand. The claim that TSC and ramp control may need incompatible backbones is likewise a concern to test, not an accepted literature conclusion.

Part I remains closed; V5/I1 and the old broad future-task map remain excluded. This decision replaces the old Part-II direction without reopening the green-allocation suite. Exact service-order resolution remains owned by M3 as agreed in P8.

## Execution sequence when opened

Apply the existing protocol's source archiving, evidence-quality assessment, batched access requests and separation between review and implementation to this replacement scope:

1. Inventory archived ramp/merge/control references and run a focused search pilot. Search controller lineage, aggregate versus lane-resolved merge models, ramp queue/spillback, speed-state requirements, and diagnostic comparison/evaluation designs. Verify the colleague's controller terminology and real-site claims from primary sources.
2. Screen the relevant corpus and extract equations or explicit method descriptions needed to distinguish physical feasibility from diagnostic value. Record uncertainty and missing full text. Stop for one batched institutional-access request if decision-critical evidence is inaccessible.
3. Produce a compatibility matrix against closed components and planned functionality, a literature-supported necessity/feasibility verdict, and a minimum scenario/control shortlist. **First planned scientific user checkpoint:** approve or revise that verdict and shortlist before detailed conditional task formulation. Stop earlier for a required architecture/scope change.
4. Only after that checkpoint, formulate a warranted candidate's action, objective, state/gradient dependencies, baseline/controller roles, evaluator and remaining implementation gates. If no diagnostic compatible candidate is supported, prepare a reasoned rejection/conditional finding instead of forcing a task.
5. Present the Part-II conclusion and project implications for user closure. Do not change project documents or implement the task as part of this study.

Use a distinct `part_2_ramp_metering/` area inside this package for execution records and artifacts, with newly obtained material in the package archive and references to existing sources rather than repeated downloads. No new literature search was performed for this decision record.

Next allowed action: explicit opening of Part II, proceeding through steps 1–3 to the first scientific checkpoint unless access or scope anomalies require an earlier stop.
