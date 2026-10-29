# Allocation can complete the traffic budgets; the meaning of a lane-change request is the next choice

**Later decision, 2026-10-21: LF1 is selected and closed.** The user approves
the recommended attempt-and-forward candidate and continuation. The original
assessment below is retained; its open-gate wording describes delivery before
that selection. The selected equations and their limitations are unchanged.
The subsequent LF2 choice is also closed with H selected; the joined
qualification is now delivered at JQ1. The earlier source/flow proofs remain
unchanged and are not empirical certificates.

[Current joined-candidate findings](vsl_joined_candidate_findings_and_checkpoint.md)

[LF1 decision and exact scope](vsl_allocator_selection.md)

[Current findings and LF2](vsl_congestion_join_findings_and_gate.md)

Original assessment, 2026-10-21. **The bounded allocator assessment is complete;
the decision was open at delivery.** The user
authorized allocation-first review after feedback 14. This pass reads primary
methods, constructs a conservative completion candidate and identifies the
behavioral decision needed to continue qualification. It provides no new
reason to backtrack the principal lane backbone.

## The main finding in traffic terms

The missing component does not need to invent new traffic states. Each lane
cell already tells us how much traffic can leave and how much traffic a
receiving cell can accept. The allocator must share these quantities once,
across all permitted movements. Ten available units cannot become seven
units going left plus seven going right. Several arriving streams cannot
each claim the same receiving space.

**A compact rule can meet those requirements.** I constructed an explicit
candidate for three lanes: form requests that share each donor's budget;
share each destination's receiving space; then let unsuccessful lane-change
attempts continue in their present lane when space remains. The mathematical
note proves nonnegative flows, common sending/receiving limits, conservation
and storage bounds under its stated CTM input conditions. This is an
analytical construction, not a traffic run or evidence of calibrated realism.

The literature supplies its ingredients, but does not supply this exact
joined three-lane law. Carey et al. provide diagonal lane-changing transport,
receiving competition and forward movement after realized lane changes.
Their worked algorithms cover two lanes with one changing direction.
Wright et al. provide explicit priority allocation and a complete general
junction alternative. Neither paper establishes that our new join inherits
all its source's properties. [1], [2]

**The important choice is now behavioral:** does a desired lane change mean
“try to move over, otherwise keep going,” or “this part of the traffic must
take that direction before it can advance”? Both can be made conservative.
They can produce very different queues and VSL sensitivities.

## Recommended candidate: attempts that can continue forward

Imagine traffic in E approaching the end of its lane. Before the lane end,
drivers may want to enter A but fail to find room. They can still advance
along E and try again farther downstream. At the actual lane end that escape
disappears: traffic must enter A or wait. This distinction keeps advance
preparation and compulsory merging within one movement network.

The proposed completion uses that idea as follows. Each movement advances
traffic by one physical cell, into either the same lane or an adjacent lane.
A lane change is therefore diagonal across a cell boundary. It is not a
same-cell lateral transfer followed by another forward transfer. All flows
use the old state and update stocks together, so incoming mass cannot move
a second cell in the same step.

The Subraveti incentives still generate the lateral requests. When the
requests toward two neighbors together exceed the donor budget, they share
that budget in their requested proportions. Otherwise those proportions
remain unchanged. The remaining request initially goes forward in the same
lane. Receiving space is shared with fixed priorities based on reference
lane capacities; an unsaturated stream relinquishes unused entitlement.
For identical lanes, sufficiently demanding contenders share equally.
These priorities do not use the displayed speed advice or the current
request size as an extra priority weight.

After that first allocation, unused donor traffic may take unused space in
the next cell of its own lane. There is no second lateral attempt within
the step. At the lane end E has only the permitted E-to-A movement, so its
unserved mass stays in the final E cell. There is no E-to-B jump, disappearing
traffic or completion merely because E reached the end.

**This is a concrete proposed allocator, with an admissibility proof.** It
adds no vehicle records, waiting-time state, recovery meter or route-history
ledger. It does change several assumptions inside one component: the
transport connections, joint normalization of requests, receiving priority
and treatment of failed attempts. One component substitution is therefore
not a claim that the methodological change is negligible.

**Pros.** It keeps a distinction between wishing to change lanes and actually
doing so, addresses both observed budget failures, and gives the permanent
lane end an explicit conservative boundary. It retains the lane-density and
incentive backbone instead of adding a separate forced-point model.

**Cons.** The three-lane extension and its two allocation passes are our
adaptation, not a published turnkey algorithm. It gives initial requests
precedence over later forward fallback; this can leave a better total-flow
assignment unrealized. It is deterministic for fixed inputs, but the budget
proof does not establish that refining the cells and time steps preserves
the same macroscopic traffic behavior. Nor does it establish every consistency
property required of a general road-junction model. The note gives a
counterexample to unrestricted total-flow maximization so this limitation is
visible before selection.

The elementary proposal uses no extra gap-headway multiplier beyond ordinary
receiving space. Subraveti's congestion/capacity-drop mechanism remains the
candidate source of additional service loss and still needs qualification
with VSL. Space competition by itself is not a claim that slow insertion and
subsequent recovery have been reproduced. We do not import the accepted
old point model's recovery law or its conclusions into this candidate.

## Strong simpler rival: committed movement fractions

The alternative treats each normalized directional request as a turning
fraction at a junction between cell rows. Traffic can use only its assigned
direction during that update. A published Wright-style allocator with fixed
reference-capacity priorities and full FIFO within each input lane gives a
complete junction rule. Here full FIFO means that blocking one assigned
direction also holds back the other directions from that same input lane.
It does not impose one queue across all three lanes. Fractions are recomputed
from the next state; this need not mean a permanent driver commitment. [2]

Its strongest justification is that one physical lane cannot always pass
around traffic waiting to move over. An early queue may therefore be a
meaningful approximation to committed lane-changing traffic. It also offers
a more direct reuse of a published general allocation algorithm.

**Pros.** A single established junction algorithm handles multiple donors,
multiple destinations, priorities and supply restrictions together. Its
blocking assumption is explicit and can represent strong within-lane
obstruction without extra state.

**Cons.** It changes the meaning of the Subraveti requests into movement
commitments. Traffic can queue upstream solely because it cannot change
lanes even though its own next cell has room. Relaxing FIFO alone does not
return the denied lane-change quota to forward traffic. The source's
junction results also do not certify our incentive mapping, VSL join,
capacity-drop branches or complete task.

## The same example separates them

Consider ten service-eligible units in E, before the lane end. Half request
A and half initially request the next E cell. A currently has no receiving
space; the next E cell can take all ten. There are no other contenders.
These are allocator input quantities, not a claimed full task trajectory.

| Rule | What happens to the ten units? | Traffic meaning |
|---|---|---|
| **Attempts with forward fallback, recommended** | All ten advance along E; none enters A. | A failed attempt does not itself stop travel in the continuing lane. |
| **Committed fractions with full FIFO** | None advances. | Traffic waiting for its assigned lane change blocks the shared input lane. |
| Committed fractions with FIFO removed, for clarification | Five advance along E; five wait. | Removing blocking still leaves a fixed unserved directional quota. |

At the actual lane end, E has no forward destination. Both main candidates
then retain unmerged E mass and make E compete with A for A's receiving
space. The third row is an explanation of why “relax FIFO” is not a complete
substitute for the recommended behavior, not a third proposed review branch.

Another simple check addresses the previous two-neighbor problem. Ten units
generating requests of seven toward each neighbor first become requests of
five and five. If the targets accept two and five, the donor has three left.
In the recommended model these three can continue forward if its own next
cell has room. The total remains ten throughout.

## Where this puts the whole VSL stack

| Part of the model/task | Current finding and remaining obligation |
|---|---|
| **State and lane incentives** | Keep Subraveti's continuous per-lane cell densities and lookahead/structural incentives as the principal candidate. A/B asymmetry remains meaningful; it is not assumed to yield a useful control advantage. |
| **Flow realization** | A concrete conservative completion now exists on paper. It replaces the problematic adjusted-flow equations, rather than clipping their outputs or silently reversing a sign. Its adoption and behavioral alternative are the present choice. |
| **Physical timing and lane end** | Both candidates propose fixed cells and one-cell forward/diagonal transfers. The permanent lane end removes E's forward connection. These are explicit adaptations, not a claim of exact native equivalence. |
| **VSL and congestion loss** | Han's sending restriction remains the actuation lead. The exact join with Subraveti's capacity-drop branches, sending bounds and branch thresholds must be checked after the allocator choice. Neither a second recovery mechanism nor an interior optimum is presumed. |
| **Information and rivals** | Compare lane-resolved information with E plus aggregated A/B on the same plant and action/accounting rules. The new flow law requires a fresh witness and observability check; old information and gradient certificates do not transfer. A link-only rival and direct action search remain relevant. |
| **Objective and complete accounting** | Count all unfinished mass, including final E stock and any upstream holding stock. A coherent full population-time/tail contract remains to be established; no arbitrary fixed-horizon disappearance or exact finite-clearance claim is admitted here. |
| **Sensitivity and decision evidence** | The proposed allocator is piecewise smooth on fixed positive-demand active sets. Whole-model derivatives, mode boundaries and gradient usefulness remain unqualified. No AD or traffic experiment was run. |

Thus this pass supplies a viable **forward-allocation component**, not a
completed replacement task. The old negative adjusted receiving cannot occur
in this component because flows are allocated against nonnegative budgets
directly. Stock/storage validity additionally requires admissible CTM budgets
and a fixed grid satisfying the stated time-step bounds. Those conditions
must also hold for the eventual VSL/capacity-drop join.

## Decision and stopping point

**LF1 is Type 2, user-owned.** Its concrete question is whether to continue
with the proposed attempt-and-forward completion or the published
fixed-fraction/FIFO junction route. This changes queue formation and the
meaning of lane-change intention, so it cannot be settled as a numerical
repair. The transport, priority, normalization and boundary assumptions above
belong to the candidate contract and are not approved merely by this review.

**Provisional recommendation: continue qualification with attempts and forward
fallback.** It gives lane-changing wishes their less restrictive opportunity
meaning, while making compulsory waiting arise at the actual lane end. The
tradeoff is a transparent small adaptation rather than direct inheritance of
a complete general-junction algorithm. Its lack of a maximal-throughput
guarantee is a real limitation, not a reason already established to reject it.
Choose committed fractions instead if early within-lane blocking is part of
the intended elementary task. No literature result makes one universally
correct for this scenario.

The allocator fit assessment ends here. After selection, qualify the chosen
flow law with the native congestion/VSL rules, then complete information,
accounting and derivative checks under that law. Source transcription is
component-local only where it leaves this contract unchanged; a new conflict
reopens the affected LF1 assumption. No further review stage, simulator code,
dependency installation or traffic experiment is started in this pass.
The accepted report and closed VSL Step 4 remain unchanged.

[Mathematical candidate, proof and hand cases, PDF](../../synthesis/research_readiness/vsl_allocator_contract_and_checks.pdf)

[LaTeX source](../../synthesis/research_readiness/vsl_allocator_contract_and_checks.tex)

[References actually viewed, source scope and adaptation boundaries](../../extraction/research_readiness/vsl_allocator_sources_and_adaptations.md)

[Work record and checks](vsl_allocator_work_report.md)
