# R9 closure record: selective-discreteness literature review

Date: 2026-09-07  
Status: Closed  
Scope: Question A—literature gap, model lineage, and baseline credibility

## 1. Closure decision

R8 was approved by the user without a disputed conclusion. R9 found no unresolved factual correction, screening dispute, access failure, or protocol deviation that prevents closure. The review package is therefore frozen as the evidence base for a later colleague-facing report and a separate audit of the current project plan.

This closure does not change simulator methodology, approve an experiment, open Question B, or establish a first-of-kind publication claim.

## 2. Assumption foundation

The synthesis relies on the following assumptions. Each is either conventional in traffic modeling/review practice or an explicit reasonable rule adopted for this audit.

### A1 — Models are compared by implemented capability, not labels

Terms such as “mesoscopic” cover individual vehicles, packets, events, and queue models. Comparing state variables and update rules is more reliable than treating the label as a technical definition. This is supported by the heterogeneous mesoscopic implementations in de Souza, LIFT, DTALite, MESCOP, TRAFFMED, and Son's hybrid model.

### A2 — Continuous traffic quantity and discrete semantic structure are separable concepts

A model may carry continuous mass while route, movement, topology, or lane permissions remain categorical metadata. Multi-commodity LTM/CTM and general node models establish this separation. It is therefore reasonable to ask whether semantic distinctions can persist without integerizing every vehicle transfer.

### A3 — Commodity identity is not realized queue order

Knowing totals by route or movement does not in general identify their sequence. Partial-FIFO intervals, movement FIFO, and lane-level FIFO are aggregate service assumptions unless the state explicitly retains a realized sequence or individual/event order. This distinction is necessary to compare Wright, Gong–Bliemer–Raadsen, LNCTM, de Souza, and LIFT fairly.

### A4 — Traffic capability must be defined phenomenon by phenomenon

There is no absolute “true mesoscopic capability” scalar. The review therefore evaluates route identity, order, movement/lane resolution, finite storage, accessibility, spillback, signal representation, and stochastic behavior separately. A project can preserve the targeted subset while deliberately omitting microscopic car following or lane-changing behavior.

### A5 — Differentiability mechanisms are not interchangeable

Analytic smooth equations, reverse-mode AD through piecewise operations, AD through smoothed discrete logic, and derivatives of a learned surrogate have different forward and backward contracts. Osorio et al., Seo, Andelfinger, Son, and Song et al. justify keeping these categories separate.

### A6 — Derivative correctness and decision usefulness are different claims

Finite-difference or analytic agreement tests the derivative of the implemented model. Internal objective reduction tests whether that model can optimize itself. Neither alone shows that the direction improves a richer simulator or real system. This distinction is standard model-validation logic and is reinforced by the aggregation/prediction sensitivity evidence of Poelman et al.

### A7 — Fair baseline comparisons control alternative explanations

Models must share demands, traffic parameters, control variables, objectives, and budgets wherever possible. If a complete implementation cannot be matched without changing scientific meaning, an equation/reference or conceptual comparison is more credible than a raw performance ranking.

### A8 — Literature absence is corpus-bounded

Failure to retrieve an equivalent model supports an open intersection only within the documented search. It does not prove universal priority. Accordingly, no unrestricted “first” claim follows from this review.

### A9 — The project's contribution may be architectural and empirical

A scientific contribution need not consist of individually unprecedented components. A nontrivial integration can be useful if it occupies a justified design point and controlled experiments establish consequences that existing combinations do not. Conversely, integration alone is insufficient without evidence of incremental value.

## 3. Evidence-to-deduction chain

### D1 — Aggregate propagation and differentiability are inherited

- **Assumptions used:** A1, A2, A5.
- **Evidence:** Yperman and Tampère establish the continuous LTM/node foundation; Osorio–Flötteröd–Bierlaire establish smooth stochastic differentiable DNL; Seo supplies modern reverse-AD LTM; Song et al. supply a differentiable surrogate DNL.
- **Deduction:** The project cannot claim continuous LTM, differentiable DNL, or scalable traffic gradients as standalone novelty.

### D2 — Lane, movement, storage, blockage, and spillback components are inherited or adapted

- **Assumptions used:** A1, A4.
- **Evidence:** Wright partial FIFO; Gong–Bliemer–Raadsen lane allocation; Wei turn queues; Liu–Chang lane groups; Gao turning-lane physical queues; Wong–Lee finite lane overflow; Shiomi multilane equilibrium.
- **Deduction:** These traffic capabilities justify the project's target phenomena but cannot individually carry novelty claims.

### D3 — Exact identity/order in LWR-consistent mesoscopic models is established through discrete vehicles or events

- **Assumptions used:** A1–A4.
- **Evidence:** de Souza integerizes LTM transfers for individual tracking; LIFT and the SUMO LTM alternative use vehicle/event-oriented representations with FIFO and backward-space spillback; packet simulators preserve discrete entities.
- **Deduction:** Identity-preserving or FIFO mesoscopic LTM is not new. The narrower proposed adaptation is persistent exact semantics with divisible mass.

### D4 — Differentiable rich-state traffic simulation is established

- **Assumptions used:** A1, A5.
- **Evidence:** Andelfinger differentiates smoothed agent logic; Son et al. differentiate a micro/macro hybrid with conversion; differentiable IDM papers optimize individual trajectories or traffic-aware driving.
- **Deduction:** “First differentiable mesoscopic/hybrid traffic simulator” and “first differentiable traffic signal optimization” are unsafe. The relevant distinction is the state and derivative contract used.

### D5 — The rank-bin/ledger construction remains potentially distinct, not proven novel

- **Assumptions used:** A2–A4, A8, A9.
- **Evidence:** The corpus contains continuous commodities without exact order, exact individual/event order without divisible transfer mass, and aggregate lane/movement queues without an aligned exact semantic ledger. No extracted work matches the complete aligned rank-bin/ledger construction.
- **Deduction:** The construction is potentially novel under a narrow operational definition. Corpus absence cannot establish priority, and experiments must show that it is more than an implementation convenience.

### D6 — The primary empirical threat is equivalence with structured aggregate state

- **Assumptions used:** A3, A4, A7, A9.
- **Evidence:** Partial-FIFO, turn-queue, lane-equilibrium, lane-group blockage, and finite-storage models already recover many intended behaviors without exact sequence.
- **Deduction:** A macro-only baseline is inadequate. The approved comparison ladder must test whether movement/lane/storage aggregates explain any gain before attributing it to exact semantic order.

### D7 — The minimum comparison logic contains four required explanatory rungs

- **Assumptions used:** A7.
- **Evidence:** `baseline_map.md` and `baseline_feasibility.md` trace each rung to retrieved methods.
- **Deduction:** The review recommends homogeneous differentiable macro; structured aggregate queue; lane/storage-aware aggregate; and identity/order mesoscopic forward reference. The differentiable hybrid comparison is deferred until Question B supplies a fair task.

### D8 — Gradient usefulness remains an empirical question

- **Assumptions used:** A5, A6, A9.
- **Evidence:** Several studies validate derivatives or improve internal objectives, and several compare forward traffic outputs with microscopic simulation. No extracted study supplies the complete externally evaluated gradient-direction test defined by this review.
- **Deduction:** The project's strongest prospective contribution is a controlled demonstration that selective mesoscopic state improves externally evaluated decisions. A negative result—structured aggregate state performs equally well—is scientifically valid.

## 4. Final claim boundary

### Supported now

- The project is built from mature traffic-model and differentiation lineages.
- There is a credible open intersection around divisible mass plus persistent exact semantics and localized lane/storage state.
- A four-rung comparison ladder is required to attribute any benefit.

### Supported only as a hypothesis to test

- The selective-discreteness stack preserves the targeted mesoscopic behavior with acceptable cost.
- Exact semantic order adds useful information beyond movement/lane aggregate queues.
- Its gradients improve externally evaluated traffic decisions.

### Not supported

- Any broad first-of-kind claim.
- Novelty of the individual traffic components.
- An absolute promise of no capability loss or perfect gradient fidelity.
- Usefulness inferred from differentiability or in-simulator optimization alone.

## 5. Frozen review outputs

- Protocol: `review_protocol_plan.md`
- Search and screening: `search/`, `screening/`, and `full_text/`
- Evidence extraction: `extraction/evidence_matrix.csv`
- Citation expansion: `snowballing/r7_report.md` and `snowballing/snowball_log.csv`
- Taxonomy: `synthesis/model_taxonomy.md`
- Baseline logic: `synthesis/baseline_map.md`
- Novelty judgment: `synthesis/novelty_gap_report.md`
- Final narrative: `reporting/review_report.md`
- Limitations and counts: `reporting/limitations.md` and `reporting/prisma_counts.csv`

## 6. Deferred follow-on work

1. Prepare a colleague-facing report that explains this evidence chain at presentation/report depth rather than protocol depth.
2. Audit the current project context, roadmap, and approved milestone plans against the closed review conclusions.
3. Run the separate Question B sprint for downstream task selection and formulation.
4. Recheck preprint publication status and recent arXiv additions before any manuscript submission.

These follow-ons require separate user instructions. They are not implicitly authorized by closing R9.
