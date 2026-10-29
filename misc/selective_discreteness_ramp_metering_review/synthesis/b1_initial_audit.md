# B1 initial audit — admissions upstream of a restricted exit

Date: 2026-09-14. Interim evidence, not a final suitability verdict. Read the current action request in `../reporting/b1_access_request_batch_1.md`.

Superseded status: that access request has been satisfied. This interim record is preserved as history; current findings and discussion gate are in `b1_conclusion_checkpoint.md` and `../extraction/RM0016_full_text_audit.md`.

## Outcome of this pass

The user closed RM3's target-selection gate and confirmed B1 as the first review target. RM4 is opened with a **feasibility-first B1 subpass**; detailed formulation waits for discussion of its supported conclusion. This pass has established a closer literature basis and a concrete compatibility caveat, but has reached a decision-critical full-text gap before a defensible pro/against verdict.

B1 is not an invented traffic-control problem: literature explicitly discusses metering upstream of a constrained exit. However, that strengthens the need for a capable destination-aware comparator. It does not establish that selective order adds value. **Current disposition: insufficient evidence for project-specific promotion, not evidence of infeasibility.**

## 1. Source-backed admission mechanism

Michael J. Cassidy's **_Critique of a Freeway On-Ramp Metering Scheme and Broader Related Issues_ (2002, RM0017)** explicitly analyzes two merging streams upstream of a restricted exit. In §3, PDF pp.7–8, unequal exit-bound shares allow metering to change the composition reaching the diverge; depending on which stream is restricted, discharge can improve or worsen. Equal shares remove that particular composition-control mechanism under the stated idealization. The report also separates internal traffic improvements from total system delay. These are conditional aggregate arguments, not evidence that fine order is required. [Author report](https://escholarship.org/content/qt804724nd/qt804724nd.pdf).

The related **_Freeway On-Ramp Metering, Delay Savings, and Diverge Bottleneck_ (Cassidy, 2003, RM0015)** supplies the journal lineage; only its metadata/abstract was obtained. The 2002 report is inspected in its own right, not presumed identical to the journal version. This distinction and access records are archived.

This yields a useful B1 screening principle: different fixed source route populations can give one meter influence over the *admitted mixture* without changing anyone's route. One cannot simply assume that reducing the ramp rate helps. Route composition, downstream restriction and inclusion of ramp waiting determine the relevant comparison. Detailed demand construction is not frozen here.

The report's historical statements about the then-available evidence for merge capacity must not be treated as current universal claims; RM0014 supplies later isolated-merge observations. Our use of RM0017 is its diverge/composition argument.

## 2. The strongest newly identified comparator

**Zhang et al., _Destination-Aware Coordinated Ramp Metering for Preventing Off-Ramp Queue Spillover and Mainstream Congestion_ (2024; RM0016)** is directly relevant. Its author-institution abstract describes destination-aware traffic evolution, off-ramp queue constraints and predictive metering. Those features overlap with the proposed causal explanation for B1. Its full state, equations, spillover mechanism and comparison design must be inspected before deciding whether a finer local representation tests anything beyond that model. [Institutional record](https://research.polyu.edu.hk/en/publications/destination-aware-coordinated-ramp-metering-for-preventing-off-ra/).

This does not make B1 redundant automatically: the new paper may omit the relevant local information, use incompatible physics, or test a different control question. Conversely, an order-sensitive difference against a memoryless baseline would not suffice if a credible destination-aware model captures it. The one-paper access batch targets precisely this unresolved distinction. Its coordinated controller is not being imported into our one-meter scope.

## 3. Compatibility trace from the actual project

| Link in B1's causal chain | Inspected basis | Finding and limitation |
|---|---|---|
| Metered ramp release | `nodes.py`: restricted service and ordinary node paths; source/link accounting | A bounded release/service adapter is plausible. Structural `input_capacity_rate` is not the optimization variable; meter service must not be disguised as changing structural merge priorities. Units and finite-ramp/source ownership require later definition. |
| Continuous movement transfer and route progression | M0 node solver and M1 ledger operations | Existing basis for aggregate conservation and route bookkeeping, not a complete freeway access model. |
| Ordering of traffic entering the common link | M1 plan §3.4; `ledger.py::append_ordered_packages` | Whole packages are serialized by leading time and exact-tie input priority. The plan explicitly calls this a passive scaffold, **not physical lane-entry chronology**. |
| Long-link propagation | Accepted first-order LTM | Shared backbone remains the candidate. No need for independent speed is established by the composition argument. |
| Exit-pocket/shared-lane access and spillback | Active M2 neutral-domain restrictions; M3 planned service/storage ownership | Physical storage has a planned basis, but M2's principal service fixtures exclude shared-lane blocking and pocket behavior. M3 must resolve the local operator and its validity. |
| Objective and sensitivity | Existing fixed-structure differentiation and validation discipline | Full source/ramp/network accounting is required. No derivative correctness or richer-reference usefulness has been demonstrated for B1. |

The ordering caveat matters specifically because B1 introduces a merge upstream of the state whose ordering may affect service. If its claimed advantage comes from the whole-package tie convention, the experiment could measure an implementation convention instead of traffic behavior. The existing closure never promised otherwise; this is a compatibility dependency, not a discovered code defect.

Do not change the convention in this review. A physical interleaving claim would require reopening M1 G2 through an appropriately approved later lane-local decision, as the closed plan itself specifies. Alternatively, a carefully justified coarse arrival-history contrast might not need such a claim. That alternative must be tested conceptually against aggregate memory, not assumed as a workaround. No reopening is enacted now.

## 4. What must distinguish the representations?

Separate three information levels:

1. Fixed route identities and time-varying destination totals: give these to a route-aware comparator.
2. Local lane occupancy, finite physical storage and movement accessibility: match these in a capable lane/storage comparator when testing order specifically.
3. Residual sequence/rank information beyond those aggregates: only this contrast can isolate a finer-order contribution.

A conceptual pair may preserve each comparator's defined observable state while changing local sequence. But matching only whole-run totals is not enough if source time histories differ, and matching every exact route-labelled arrival would remove the variation under study. Explicitly define the information discarded by each comparator. Neither an artificial frozen-lane obstruction nor physical chronology inferred from M1's passive serialization is acceptable independent evidence.

Useful negative controls include a nonbinding exit, a composition-neutral admission case under the simplified assumptions, and neutralized local access/order. These are conceptual checks to consider, not newly approved numerical experiments or a claim that all such cases are universally identical.

## 5. Added value and remaining gate

B1 can potentially test whether retained information predicts a useful **upstream admission intervention at fixed downstream service**, unlike direct local service allocation in the closed TSC task. The aggregate composition mechanism is now concretely supported. What remains unproven is whether the selective representation contributes beyond destination-aware memory and credible lane/storage state, with a physically defensible merge-to-access mapping.

The next action is institutional full-text retrieval, not scientific approval of a positive or negative conclusion. After RM0016 is inspected, return to the three verdict axes: physical compatibility, hypothesis diagnosticity, and evidence feasibility. If a supported conclusion emerges, stop for the user's requested discussion; do not proceed automatically to detailed formulation, additional ramps, new physics or implementation.
