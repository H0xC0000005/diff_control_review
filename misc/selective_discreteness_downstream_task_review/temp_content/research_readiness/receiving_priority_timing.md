# Receiving priorities: share among currently ready heads

**Agreed, 27 October 2026.** The user selects option 2: receiving priorities act among the heads currently ready and able to discharge. This closes the focused timing definition under UR-G2/UR-C3-Q1. Green weights across legs, equal sharing within a leg, feasible caps and reuse remain agreed.

When a lane exposes a new movement, that movement joins the current competition. Earlier discharge stays as served; later sharing does not compensate for it to restore proportional whole-interval totals. The set of competitors changes with actual head order, travel readiness and physical receiving.

The user's reason is that both alternatives already need a solver aware of discharge order. Current-head sharing therefore requires no additional kind of order tracking, while its realized discharge directly reflects that order. Whole-interval fairness can offset part of that effect by compensating a later-ready movement. This is a modeling reason for selecting option 2, rather than a claim that option 1 violates order or conservation.

## The traffic case

Two inbound lanes feed one downstream link. Its entrance can accept 0.5 continuous mass per second throughout a one-second interval; storage does not bind. Each relevant movement has an average service rate of 1 mass per second, so downstream receiving is the tighter bound. This is an isolated hand example, not a proposed timestep, experiment setting or direct nonempty initialization procedure.

- **Lane A** is ready to enter that link from the start.
- **Lane B** first serves 0.6 mass toward a different, unrestricted exit. It therefore becomes ready to enter the common link only after 0.6 seconds.
- The two movements into the common link have equal green weights. Each lane has sufficient remaining demand.

Both following rules preserve exact lane order, the selected elapsed-rate service and the physical receiving limit. Both use all 0.5 of the common link's receiving supply. Neither introduces actual on/off phases.

| Meaning of green-weighted sharing | Lane A enters common link | Lane B enters common link | What happens |
|---|---:|---:|---|
| Balance completed interval totals — unselected | 0.3 | 0.2 | B can use at most 0.2 after becoming ready. Cap its nominal equal share at that amount and redistribute the rest to A. A uses the first 0.6 seconds; B uses the last 0.4 seconds. |
| **Share among current ready heads — selected** | **0.4** | **0.1** | A uses the link alone for the first 0.6 seconds, receiving 0.3. Once B becomes ready, they split the remaining 0.2 equally. |

The first rule seeks fairness in whole-interval amounts. After B becomes ready, A waits despite being able to move because A has already received its final share. It is not the rejected fixed-reservation rule: feasible caps are applied, unused nominal shares are redistributed, and no receiving supply is wasted here.

The second seeks fairness among current competitors. Earlier receiving used by A is not charged against its later share. This follows the time-local interpretation of reachable heads, but its final amounts need not be proportional to green when the heads become ready at different times.

## Why the distinction matters

The two results leave different residual traffic in the inbound lanes. Their local response to a small green transfer can differ too: one completion is locally unchanged in this case, whereas the other transfers discharge between the two lanes. The PDF gives the arithmetic and the range over which that comparison holds.

This example does **not** establish different total TST: common-link inflow and total discharge are identical here. It established why the time basis needed a decision: the two meanings leave different lane/route states and sensitivities, which feed later propagation and complete TST. The selected model now takes the current-head result, 0.4/0.1, in this case.

## Status and continuation

**No question remains in this focused choice.** The updated mathematical draft states capped green-weighted sharing across currently competing legs, then capped equal sharing among their ready lanes. Shares are recomputed when the ready set or physical bounds change. Earlier served mass is not a later priority debit.

The full model still needs the physical receiving/eligibility histories and conservative admission transaction joined to this sharing law, followed by their complete sensitivity. Those are continuing definition work in the accepted syllabus. This approval does not by itself approve new simulator code or experiments, and it reopens no earlier broad question.

[First unified draft and derivative details — PDF](../../reporting/research_readiness/urban_unified_methodology_draft.pdf)

[Agreed receiving principle and original context](coupled_lane_access_and_service_discussion.md)
