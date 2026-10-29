# Feedback 21 — pre-closure questions and colleague-report structure

Date: 2026-09-15  
Decision status: RM4 scientific gate closed against promoting ramp metering as the parallel second task; RM5 report/closure sprint is stopped for outline approval

> Audience-contract update: the colleague-report outline and wording guidance in
> Section 2 below are superseded by
> `feedback22_colleague_report_amendment.md`. The evidence ledger in this file
> remains active. In particular, internal project consequences and reopen
> conditions may remain in the review archive but will not appear in the
> colleague-facing report.
>
> Closure update: the final objective-voice report was accepted and the review
> closed on 2026-09-15. See `../reporting/closure_record.md`. All approval language
> below is historical.

## Conclusion first

The new feedback accepts the substance of F20-A. The completed D1 audit should not be described as retroactively halted: its evidence remains valid and useful. What is now halted is the **B1-P promotion and RQ3–RQ5 formulation branch**. B1-P is deferred as a primary task and may be mentioned only as an optional later transfer/ablation fixture.

The proposed colleague-report structure is fundamentally sound. I recommend two amendments:

1. put the criteria that a parallel second task had to satisfy immediately after the conclusion, so the rejection is visibly derived from an agreed standard rather than personal preference; and
2. distinguish the low-cost aggregate correctness case from B1-P's more demanding transfer-test role. Calling both only “correctness validation” would erase the one limited value D1 actually found.

## 1. Five strongest reasons for and against

It is not defensible to claim that every “for” reason independently justifies adopting ramp metering as the second task. They independently justify **considering** or **retaining** it, but none overcomes the failed hypothesis-orthogonality gate. Distinctiveness is therefore prioritized for the positive case. Several negative reasons do independently defeat promotion under the approved criteria.

### Strongest reasons for retaining some ramp-metering role

#### F1 — Ramp metering is an established, consequential control problem

The task has strong traffic-engineering legitimacy, operational deployments, mature objectives and recognizable controller baselines. A successful experiment would be easy for a traffic-engineering audience to interpret.

**Decision force:** sufficient to justify the initial feasibility review and to keep an aggregate correctness example available; insufficient to establish selective-mesoscopic value.

#### F2 — Its elementary aggregate form fits the project backbone

A first-order freeway link, continuous ramp queue, supply–demand merge and continuous metering rate can be represented without microscopic car following or lane changing. This gives a low-cost reference case for conservation, control wiring and macro-limit equivalence.

**Decision force:** independently supports an optional correctness fixture, but not a primary task because it does not activate the project's distinctive state.

#### F3 — Upstream admission creates a different causal layout from local signal allocation

The meter acts upstream, traffic propagates along a link, and a downstream objective can respond later. This can test whether gradients and retained metadata survive a longer control-to-effect chain than the isolated signal task.

**Decision force:** independently supports a transfer/integration test if that evidence is later needed; it is causal-chain distinctness rather than representation-hypothesis orthogonality.

#### F4 — Freeway gradient computation has genuine scaling and MPC value

Reilly et al. demonstrate coordinated ramp-metering gradients through a first-order conservation-law model; Gu et al. formulate smooth CTM ramp-control MPC; related work uses adjoints or automatic differentiation for multiclass networks and freeway calibration. Many time-dependent meters and parameters make efficient gradients valuable.

**Decision force:** independently supports differentiable freeway control as a legitimate field, but it simultaneously establishes a strong macroscopic predecessor rather than a need for this project's mesoscopic order.

#### F5 — A bounded B1-P result could provide cross-context evidence

If M3 eventually supplies a trusted ordered-service operator, B1-P could test whether the same information remains useful after merge chronology and long-link propagation. Equivalence to aggregate/cohort models would also be an informative negative result.

**Decision force:** independently supports preserving the D1 design as an optional post-M3 ablation; it does not support treating it as an independent scientific pillar.

### Strongest reasons against promotion as the parallel second task

#### A1 — B1-P fails the required hypothesis-orthogonality criterion

Its decisive contrast is still exact versus relaxed route-labelled order at a service restriction, which is owned by M3 and already central to the traffic-signal task. Moving the control upstream and inserting a link changes the causal chain, not the retained-information hypothesis.

**Decision force:** independently sufficient to reject B1-P for the specifically requested role.

#### A2 — The native ramp-metering problem already has strong macroscopic models and gradient methods

Conventional ramp metering is naturally expressed using aggregate density, flow, ramp queues, supply, demand and metering rates. The literature contains strong feedback, optimal-control, LP/convex, MPC and adjoint approaches at this resolution. No reviewed evidence establishes that exact local order improves the resulting decisions or gradients over strong aggregate, composition-memory or time-cohort alternatives.

**Decision force:** independently sufficient to reject a claimed selective-mesoscopic contribution unless a specific aggregate failure class is first established.

#### A3 — Literature-supported mesoscopic ramp value does not match the project's retained state

Mesoscopic ramp studies mainly add dynamic route/departure response, stochastic event realization, vehicle or packet tracking, lane refinement and large-network evaluation. Dynamic route choice and stochastic integer vehicles are outside the initial project; route-aware aggregate models can cover some remaining effects. Exact cumulative-mass order is not established as the characteristic source of ramp-control improvement.

**Decision force:** independently defeats the required literature-affinity argument for the current task formulation.

#### A4 — The natural freeway mechanisms that make individual realization important require excluded physics

Gap acceptance, lane changing, merge safety, speed adaptation, heterogeneous driving and important capacity-drop mechanisms supply convincing nonaggregate freeway behavior. They generally require microscopic or substantially expanded mesoscopic dynamics that cannot be hidden in the current node solver. B1-P avoids the merge problem through non-overlapping eligibility intervals and moves order sensitivity to a deliberately elementary downstream diverge.

**Decision force:** independently defeats either compatibility or operational representativeness: the realistic task changes project physics, while the compatible task is contrived.

#### A5 — The remaining scientific value is too small for the methodological and engineering coupling cost

B1-P would require a special admissible scenario, exact order propagation, a downstream point-diverge operator, aggregate/cohort/refinement baselines, derivative checks and careful non-generalization. It also cannot be interpreted independently of the eventual M3 realization. This is bounded work, but it is disproportionate for a task that supplies only transfer evidence.

**Decision force:** not a universal scientific refutation by itself, but independently sufficient for project prioritization once the requested role is already unsupported.

## 2. Assessment and revision of the proposed report structure

The proposed structure contains the right ingredients. A slightly revised order will make the reasoning cleaner and prevent two possible misunderstandings.

### Recommended structure

1. **Overall conclusion and decision.** State that ramp metering is not recommended as the parallel second task; state the closest defensible residual roles; state that no project amendment follows.
2. **What the second task was required to establish.** Briefly define compatibility, distinct representation-hypothesis value, literature affinity and evidence feasibility. Explain that a different controller name or network type is not sufficient orthogonality.
3. **What the literature establishes.** Use three compact subsections:
   - native macroscopic ramp-control models and their strong controllers/optimizers;
   - mesoscopic ramp simulation and what its added resolution actually represents;
   - differentiable/gradient freeway control and what gradients contribute.
   Compare each family with the existing project architecture.
4. **The decisive for/against ledger.** Present the strongest positive case fairly, followed by the five negative reasons above. Make clear that A1–A4 fail the approved promotion criteria.
5. **Gap from the desired task to B1-P.** Use one compact table covering application distinctness, causal-chain distinctness, representation-hypothesis orthogonality, physical compatibility, representativeness, baseline separation and implementation dependence.
6. **Closest acceptable ramp-metering roles and their costs.** Separate:
   - **aggregate case A:** low-cost correctness/macro-limit check for ramp queue, metering action, merge conservation and gradients;
   - **B1-P:** optional post-M3 transfer/ablation check for order preservation across an upstream-control/long-link/downstream-service chain.
   Neither is a parallel scientific pillar. B1-P's cost is bounded but nontrivial, not simply “decent” without qualification.
7. **Project consequence and reopen conditions.** State that no milestone or project file changes; list the evidence that would be required to reconsider a freeway second task.
8. **Short conclusion.** Reaffirm that ramp metering is unsuitable for the intended role under the current scope, rather than universally unimportant.
9. **Short IEEE reference list.** Cite sources throughout the report and retain only the decision-bearing references.

### Why the amendments matter

- The decision criteria make the “against” conclusion auditable rather than rhetorical.
- The positive ledger shows that the colleague's suggestion was technically reasonable to investigate.
- Separating case A from B1-P avoids understating D1's transfer value or overstating case A's scientific value.
- Reopen conditions prevent the report from sounding like a universal theorem against freeway research.

## 3. Additional work needed for a proper closure

Beyond the reason inventory and report outline, only a small closure set is needed.

### C1 — Freeze a precise decision record

Record that ramp metering is rejected as the primary orthogonal second task, not rejected as a traffic-control problem. Record that case A and B1-P are optional fixtures with different roles, not planned experiments. Explicitly hang RQ3–RQ5 formulation.

### C2 — Preserve the strongest counterargument

The report should include the strongest positive case—established importance, aggregate compatibility, upstream/downstream gradient transfer and scalable adjoints—before explaining why it does not satisfy the project-specific gate. This is important because the idea came from a colleague and deserves a fair technical response.

### C3 — Audit the final claims and citations

Before rendering, verify that every literature-dependent claim uses a decision-bearing primary or authoritative source, derivative methods are not conflated, and “mesoscopic” is always tied to the state actually retained. Do not use absence from the bounded corpus as a novelty or impossibility proof.

### C4 — State project impact and reopen conditions

The closure should say explicitly that no project roadmap, milestone, implementation or task suite changes. Reconsideration would require either:

- evidence of a project-compatible freeway mechanism for which selective metadata changes forward outcomes or useful gradients beyond strong aggregate/cohort baselines; or
- explicit approval to add a new capability such as dynamic route choice, multiclass behavior, lane access/change, merge safety or capacity-drop dynamics.

### C5 — Produce and approve the final package

Draft one brief colleague-facing LaTeX report, render and inspect the PDF, archive the source/reference list and build command, then stop for final user approval. After approval, write the RM5 closure record and update only this review package's handoff/status files.

No further broad literature search or institutional-access request is presently necessary. A targeted lookup should occur only if drafting exposes a specific unsupported claim.

## Recommended next action

Approve this reason inventory and revised structure. Then open the RM5 report-writing pass, produce the LaTeX/PDF brief, and stop for user review before closing the overall review.
