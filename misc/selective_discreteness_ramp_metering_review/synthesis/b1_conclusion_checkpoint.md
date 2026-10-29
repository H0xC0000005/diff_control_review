# B1 evidence checkpoint — discussion required

Date: 2026-09-14. The requested full paper has been received and audited. RM3 remains closed; RM4 is stopped at this scientific/methodological checkpoint. No broader task or implementation has been opened.

## Conclusion first

**Do not promote the current B1 concept to a fully specified parallel validation task yet. Retain it as a conditional candidate for a narrowly defined local-access discussion.** This is a recommendation against immediate promotion, not a proof that B1 or ramp metering is infeasible.

The evidence supports B1 as a meaningful traffic-control question: upstream admission can affect downstream exit demand and blockage without changing routes. It does **not yet establish a project-compatible mesoscopic realization that tests something beyond route-aware aggregate memory and lane/storage state**. The closest newly audited paper does not close that gap: its mechanism uses different physics, and its printed queue equations have a reproducibility inconsistency.

We have reached the requested discussion point. More generic literature searching or silently rewriting the paper would not resolve the remaining model-choice question. There is no new paper request or dependency-installation request.

## 1. What the supplied paper changes

**Zhang et al., _Destination-Aware Coordinated Ramp Metering for Preventing Off-Ramp Queue Spillover and Mainstream Congestion_ (2024, RM0016)** is a close task reference but not a compatible ready-made baseline. Read the [full-text audit](../extraction/RM0016_full_text_audit.md) for page-level evidence and the [original PDF](../archive/user_supplied/RM0016_Zhang_et_al_destination_aware_ramp_metering.pdf).

- Its traffic state is destination-aware macroscopic density/flow and queues, plus independently evolving mean speed—not ordered lane-local mass.
- Its spillover mechanism changes effective lane count and fundamental-diagram parameters and enters a second-order speed update. Directly importing that mechanism would change the shared first-order project backbone.
- Its headline control comparison changes destination treatment, spillover dynamics, queue constraints and objective terms together. It does not isolate information resolution.
- Its more focused comparison shows that off-ramp-aware control with selected fixed split ratios can also work in the studied settings. This strengthens the required aggregate comparator without proving that aggregate models always suffice.
- The published recurrence caps off-ramp admission by remaining storage, preventing an initially feasible queue from exceeding storage, yet the reported spillover mechanism requires that exceedance. The [one-page mathematical check](RM0016_queue_consistency.pdf) documents the discrepancy. It needs clarification for literal adoption; we have not repaired it or attributed it to the authors' code.

An important correction to the pre-access discussion: RM0016 is **not evidence that the whole mechanism has already been reproduced by a first-order comparator**. It is evidence of a related aggregate-state control approach using second-order physics. Our matched first-order comparator would still need an explicit, justified construction.

## 2. B1 against the approved feasibility criteria

| Criterion | Finding | Decision consequence |
|---|---|---|
| Meaningful one-meter intervention | Cassidy's previously inspected two-stream/diverge argument gives a concrete composition-control mechanism; the new paper supplies related task lineage | Positive for relevance, not proof of selective-order value |
| Shared physical backbone | Aggregate admission/route conservation has a first-order basis; local exit-access realization remains M3-owned; RM0016's speed and regime laws cannot be copied | Conditional; no approved complete operator chain |
| Fair representation contrast | Route identity/composition and finite storage must be represented in strong baselines; benefit from simply adding those to a weak baseline would be confounded | No demonstrated residual local-information contrast yet |
| Physical credibility of order | M1's whole-package merge serialization explicitly is not physical lane-entry chronology | Cannot use bookkeeping order as independent forward evidence; physical replacement requires the specified later G2 reopening |
| Value beyond TSC | Upstream arrival control of fixed downstream service is a distinct intervention; local blockage itself overlaps TSC | Plausible incremental inference, but requires a defensible local-access mechanism rather than only more geometry |
| Reproducible comparison/evaluator | RM0016 is not a richer-reference gradient-transfer study and has a printed specification gap | Do not copy its result as a project acceptance target; evaluator contract remains open |

The negative recommendation is about **readiness of the current candidate**, not the desired sign of a future experiment. A task with a credible contrast remains valuable if it finds aggregate sufficiency. We do not require proof that the mesoscopic model will win before approving an experiment. We do require that the contrast, intervention and reference have a coherent traffic meaning.

## 3. The unresolved core is now local and concrete

The next substantive question is not whether to add more ramps. It is:

**At B1's fixed downstream exit, which physically credible lane-access or finite-storage behavior depends on information that the agreed aggregate comparator lacks, and how does metering influence that information without relying on arbitrary merge serialization?**

Possible content includes a finite exit-access region whose blocked occupancy affects through service. But route labels alone do not determine realized access; fixing lanes unrealistically would manufacture an effect. M3 must own the eventual service rule and any within-bin relaxation. If the mechanism instead needs distributed weaving, it requires the separate compatibility discussion already agreed.

A source-based second-order model can be useful as contextual evidence without being a matched representation baseline. Replacing its speed evolution with LTM and its overflow law with a local-zone model would be a methodological adaptation to justify, not a mechanical simplification of the paper.

## 4. User discussion: smallest next decision

**Problem statement:** should B1 receive one bounded local-access design discussion, be deferred, or be pursued through a broader common-physics review?

**Assumed model-chain function:** meter service changes admitted route-mass histories; the merge and LTM propagate them; a fixed downstream exit's lane/storage/access rule determines service and total time. Only the admission is optimized.

**Core gap:** the project-compatible access rule and credible order/information contrast are not yet specified. The supplied paper cannot provide them unchanged. This is not resolvable by selecting a different numerical parameter or changing a source equation without approval.

### D1 — one bounded local-access design discussion (recommended)

Keep one meter and one exit. Discuss a physically justified M3-compatible local-access construction, its comparator information and evaluator interpretation. First try a contrast that does not require physical sub-package interleaving; if none can be justified, report that rather than inventing one. Explicitly assess any need to reopen M1 G2. No implementation or detailed optimizer settings.

**Pros:** addresses the precise unresolved scientific question; preserves the approved minimal geometry and common backbone; allows a reasoned negative conclusion without speculative expansion.

**Cons:** needs methodological judgment, not just further paper extraction; may find only aggregate effects or TSC-redundant access behavior; may still expose an order-contract change.

**Dependencies:** user approval of this next discussion scope; M3 remains the implementation decision owner. Any change to closed contracts must be separately approved. The discussion need not wait for M3 implementation, but cannot preempt its approval workflow.

### D2 — defer B1 as a parallel validation task


Retain its task lineage and this compatibility record. Revisit when an approved local-access design or new evidence supplies a credible contrast. Do not add the plain aggregate case merely as a benchmark.

**Pros:** avoids application-driven model expansion and redundant experiments; leaves effort focused on the closed TSC task anchor.

**Cons:** does not determine whether a viable in-scope B1 construction exists; could defer a useful indirect-control test.

**Dependencies:** explicit user decision to defer; not a declaration of universal infeasibility or permission to close the whole review automatically.

### D3 — separately review common TSC/freeway physics

Assess whether a shared architecture should represent freeway lateral/speed effects more broadly, including the implications of second-order or distributed lane dynamics. Clarification of RM0016's recurrence would be needed only if pursuing its exact adoption/reproduction.

**Pros:** could support physically richer freeway mechanisms and a stronger transfer question.

**Cons:** substantially exceeds the current narrow representation study and may change the contribution, accepted dependencies and comparison fairness.

**Dependencies:** explicit new scope approval; no change follows from the current review. Not recommended before D1 establishes whether it is necessary.

**Recommendation:** D1, not immediate formulation or implementation. This recommendation is provisional. Stop here for the user's discussion as requested; do not silently open D1, D2 or D3.

## 5. Work and artifact guide

Read this file first. The full-text audit is supporting detail; the one-page PDF is only the queue-specification proof. Earlier access requests and interim reports are historical, not current gates.

Original RM0016 preserved and checksummed; source index and access status updated. Used installed PDF extraction, Poppler rendering and LaTeX; no dependencies added, no project code/plans/feedback changed, no simulation or optimization run. The source inconsistency was verified visually and algebraically, not silently fixed. The work record and build/check results are appended to `../reporting/b1_initial_pass_work_record.md`.
