# Why revise the primary merge-completion law?

Date: 2026-10-12. Status: **Discussion at VSL-R1-G1. Source-coupled revision
is the recommended direction for the current applied target; no replacement
law or state has been selected.**

**Current instruction.** The latest user correction requires the full modeling
problem inventory before defining B's remedy. The discussion below is retained
as history; its proposed immediate joint source-contract step is superseded.

[Current modeling problem inventory](vsl_r1_modeling_problem_inventory.md)

The user's conclusion is sound for the intended applied VSL task. The inspected
evidence provides no further physical justification for making S13's constant
physical-time completion rate its primary traffic law. Its mathematical
tractability explains why it was useful for the earlier conditional certificate.
That purpose does not establish its speed response in traffic.

## What the criticism establishes

The receiving examples identify conditions in which ending-lane mass and
elapsed time alone cannot determine completed merging. A crowded adjacent
lane can restrict transfers even when the farther continuing lane has room.
Realized completion then depends on consequential lane receiving information.
Lane-level aggregate quantities may cover this; individual vehicle dynamics
and a full spatial simulator do not follow automatically.

The result is a missing justification for the proposed applied regime, rather
than a proof that a constant rate is unrealistic in every regime. Different
lane conditions need not affect transfer when all relevant receiving limits
are inactive. But receiving slack alone does not show that the completion rate
remains unchanged when common speed changes. The sources do not jointly
establish these conditions across the proposed action range.

## Two different meanings of a fixed proportion

S13 fixes the completion rate per unit of remaining ending-lane mass and unit
elapsed time. The final fraction completing a merge is not fixed: it changes
with the time spent in preparation, and therefore with speed. This assumption
concerns realized completion, with upstream receiving taken to be sufficient.

A fixed desired share of a lane's sending demand is a different assumption.
Even if that share is constant, the sending amount and the target's available
receiving capacity can vary. Actual completed transfers can therefore vary
with lane conditions. A constant behavioral or priority parameter does not by
itself disregard supply/service limitations.

Carey's model explicitly distinguishes lane-change intentions from competition
for receiving space and specifies allocation rules when that space is scarce.
It also allows simple desire specifications. This supports retaining a simple
desire rule when justified, while allowing receiving to constrain realization;
it does not supply S13's speed-independent completion rate.

[Carey et al., primary manuscript §§4–5](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

Subraveti's lateral demand is a share of sending demand and is subsequently
subject to receiving restrictions. This further separates a demand fraction
from an unconditional completion rate. The earlier source branch and gradient
cautions remain; no whole-model adoption is implied.

[Selected source equations and limitations](../../extraction/research_readiness/vsl_r1_primary_source_join_audit.md)

## The strongest case for keeping a constant rate

A possible physical approximation would restrict the task to a narrow operating
range where merge opportunities per unit elapsed time change little with common
speed and target receiving remains sufficient. This is a hypothesis to justify,
not a result supplied by the inspected sources. Matching the merged amount at
one speed would also be insufficient for the gradient task: the response to
changing speed is the consequential quantity.

There is an established analytical reason to preserve the S13 result. Its law
provides a complete conditional example, exact sensitivities and a sufficient
initial merge scalar. Those results remain valid and can serve as historical
or optional mathematical checks. A revised primary model need not retain this
law or recover its positive benefit. Keeping the closed S13 record does not
require keeping Candidate A as the active applied model.

[Accepted S13 adaptation and evidence boundaries](../../extraction/s13_m2_source_to_equation_audit.md)

## Consequence for the gate

For the current applied-usefulness goal, **Candidate B is the recommended
direction**: qualify a bounded source-coupled relation between desired merging,
available sending, adjacent receiving, completed transfers and departures.
Retain the smallest continuous state that relation actually requires, and
account for costs both upstream and at the exit. A source-consistent relation
may still include constant parameters; they cannot substitute for determining
actual feasible transfer.

This is a revision of the primary traffic mechanism, not permission to add a
fuller simulator. The speed response and receiving/service assumptions must
be qualified together. Adding an ad hoc receiving cap to the old law would
not alone establish its physical meaning. If the sourced response removes the
extra-time benefit or makes aggregate information sufficient, that is an
admissible finding. No law should be chosen to force a positive gradient result.

The user's present message expresses a preference for revision and asks for
counterarguments. It is recorded as support for that direction in the
discussion. The exact replacement and its required G3 amendment remain
unselected; no further derivation, implementation or experiment is opened.

[Current gate and full candidate consequences](vsl_r1_core_mechanism_findings_and_gate.md)

## Clarified scope of Candidate B

The user welcomes B's direction and asks whether it mainly compares alternative
speed-dependent merging laws or needs amendment in light of the discussion.
**B should qualify one coherent, elementary traffic mechanism linking speed,
available sending, desired merging, adjacent receiving and completed exit.**
The speed response is the first exposed gap; replacing the constant rate with
a speed-dependent function alone would leave other consequential assumptions
unresolved. This sharpens B's existing joint scope rather than opening a larger
traffic-model program.

Consider two preparations with the same common speed, ending-lane mass and
combined continuing mass. The adjacent continuing lane is crowded in one and
has spare receiving in the other. When that receiving is restrictive, a rule
using only speed and ending mass gives the same completion prediction for both,
although their immediate merge opportunities differ. This is why the needed
lane information and the receiving relationship must be qualified together.

The bounded scope has four connected parts:

1. **Speed and sending.** State how the common advice maps to realized motion,
   traversal time and the traffic available to move. Qualify the operating
   regime in which that mapping holds. An ideal realized-speed assumption is
   conditional; new congested-response dynamics are not adopted implicitly.
2. **Desired and completed merging.** Identify what determines desired lateral
   demand, what the adjacent target can receive while serving its own traffic,
   and how the chosen source allocates competing demands. Retain the smallest
   continuous state needed for actual completion; constant desire or priority
   parameters may remain if their use is justified.
3. **Departures and full cost.** Account consistently for early interaction
   costs, unfinished merging at the exit and departure timing. Reconsider the
   nonbinding early receiving, shared continuing resource and batch service
   assumptions wherever the source requires it. Preserve complete traffic-time
   accounting, including the cost of slowing everybody.
4. **Information and useful sensitivity.** Determine the compact state and
   fair aggregate rival from the qualified mechanism. S13's one-scalar
   sufficiency is established for S13; it is not automatically inherited by a
   revised model. A useful response, zero preparation benefit or aggregate
   sufficiency is an admissible outcome.

Use one principal source and make every adaptation explicit. Qualifying a
neighboring alternative may later test robustness, but a broad survey of rate
functions is not the immediate task. The next bounded proposal would identify
the principal source, operating regime, minimum state and complete transfer/
departure contract, and expose any remaining choice before admission. This
discussion neither selects that contract nor starts its derivation.

The present recheck did **not** establish a specific synchronized-flow service
law or a universal direction of the speed effect. The inspected sources and
diagnostic justify examining the coupled response; no additional synchronized-
flow theory, compliance dynamics or microscopic gap model is implied here.

The amendment stays within VQ3-P/T/S. Common bounded speed remains the action,
traffic mass remains continuous, and the task remains a small lane-drop
information/gradient verification. If a defensible contract requires substantial
spatial dynamics, extra control variables or a larger model family, return to
the elementary-role gate. The exact source, state and laws remain unresolved.

## Subsequent correction — identify the whole problem set first

The user asks to make all modeling problems identified by the completed review
explicit, instead of letting the latest speed/service discussion determine B's
scope. The earlier wording moved too quickly from findings to a prescribed
source-contract remedy. MP1–MP6 now separate transfer meaning and realization,
continuing-lane aggregation, early/late costs, departure chronology and joint
operating validity. Speed dependence belongs within that set.

B is a provisional direction for addressing the inventory as a whole. Some
assumptions may be justified and retained; some may require minimal revision;
others may remain conditional or unsupported. No particular source arrangement,
minimum state or repair sequence is chosen before inventory discussion. The
question artifact is the present deliverable and stop at VSL-R1-G1.

[Problem statements, ownership and possible closure outcomes](vsl_r1_modeling_problem_inventory.md)
