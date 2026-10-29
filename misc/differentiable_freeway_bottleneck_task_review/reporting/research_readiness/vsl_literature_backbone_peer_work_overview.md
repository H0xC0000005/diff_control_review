# The backbone viewed through its source works

2026-10-22. Explanation of the existing selected stack; no model change.
Reference numbers below match the current compact report.

**Final colleague-facing presentation, 2026-10-22.** The report now carries
the user's final title without a subtitle. Source colors and the source
hierarchy remain; full-word attribution replaces the B/A/D/S shorthand.
Internal review notes and links are removed from the PDF. Model equations
and the dependency account below are unchanged.

[Final report cleanup and checks](vsl_literature_backbone_colleague_finalization.md)

**Now incorporated in the report.** The user approves the inherited-dependency
account and requests a report revision. The live PDF now shows the hierarchy
explicitly; the preceding colored version is archived as v3. See the
[revision and checks](vsl_literature_backbone_review_hierarchy_work_report.md).

Feedback 15 subsequently clarifies the model presentation and separates
core assumptions within a three-page main-text budget. Its
[item-by-item answers and checks](vsl_feedback15_report_amendments.md)
describe the current PDF; the hierarchy and model equations are unchanged.

The global description is **Subraveti's lane-state and incentive framework,
using its Han congestion lineage and Han's VSL sending rule, with an adapted
movement component built from Carey and Wright principles.** Our task,
information comparison and complete-time sensitivity sit around that traffic
model. The source colors explain individual terms; this account explains
what each work contributes to the whole.

**Compact dependency wording, clarified 2026-10-22:** We use Subraveti's
lane framework as the backbone and follow its use of Han's approach for
congestion-dependent sending and receiving, completing and adapting that
formulation for the VSL lane-drop task. Han is an inherited modeling
dependency within that backbone's lineage. The full specification still
owns our congestion-mode interpretation, Han 2017 VSL extension and shared
receiving mapping; this wording does not attribute that exact variant to
Subraveti. The movement component remains a Carey-led adaptation with
Wright as supporting allocation credit.

## The module boundary: desire and available service versus realized movement

2026-10-23. The user asks explicitly which modules Subraveti plus Han and
Carey formulate, and which traffic behaviors each defines. The useful
division in the current task is:

**Subraveti plus Han describes the traffic state, what traffic wants to do
and how much service is available. The Carey-led adaptation determines
which movements actually occur under those conditions.**

This is the division we adopt from the works, not a claim that the original
papers are disjoint ready-made modules. Subraveti's original paper also
specifies realized flows; we replace that particular component. Carey
also presents a multilane CTM, but we use selected movement principles
rather than importing a second complete traffic model.

| Source within the current stack | Module contribution | Traffic behavior it defines |
|---|---|---|
| **Subraveti, with thesis clarification** | Lane-cell state and lane-change incentives. | Traffic is stored separately by lane and road section. Perceived crowding, distance-to-end urgency, keep-right and cooperation determine the desired lateral proportions. Thus E can seek A early, and continuing traffic can seek a less crowded adjacent lane or make room when the incentive conditions apply. A desired movement is not yet an accepted flow. |
| **Han, within the inherited congestion lineage and its VSL extension** | Sending and receiving limits. | Sending limits how much current traffic may leave. Receiving limits how much a target lane can accept. Congestion can lower the discharge ceiling and downstream occupancy restricts room. Advice caps sending directly; later density changes alter receiving and congestion. These laws define available service, not who wins a competition for it. |
| **Carey-led movement adaptation, with Wright supporting sharing** | Realized transport and competition for shared receiving. | A lane-changing movement advances into the next section of the adjacent lane. Competing requests share one receiving allowance. An unsuccessful attempt may continue straight if room remains; otherwise traffic waits. Applying these rules throughout the grid determines early merging as well as terminal competition. |

The module connection is therefore: **lane densities produce desires and
service limits; those inputs produce accepted movements; conservation
updates the densities.** Han does not set the lane-change preference, and
the preference does not set the fixed receiving priority. Neither source
block supplies an extra TST penalty: traffic movements and waiting generate
the time that the objective counts.

### What the Carey-led module commits the current task to

Its traffic meaning is broader than forced merging at the choke. Before
the end, a failed E-to-A attempt need not stop E if E still has forward
space. At the end, E has no straight outlet and must use A service or wait.
During either interaction, competing streams cannot jointly exceed the
same target's receiving allowance. Fixed equal priorities are capped by
each request, with unused entitlement returned to other contenders.

The exact three-lane realization remains an adaptation. We apply
proportional rationing to outgoing desires so that one origin cannot
promise the same traffic twice, define the allocation/forward-continuation
sequence, and impose the permanent E-end connection. Carey's worked
two-stream rules support the movement and sharing principles; they do not
alone provide this whole three-lane lane-drop model. Wright supports the
sharing formulation, without adding a second independent merge mechanism.

### One common traffic example

Imagine E approaching its end while A is busy and B has more room.
Subraveti's incentives determine E's desire to enter A and whether A
traffic wants to move toward B. Han's laws determine how much traffic
can leave each origin and how much A/B can accept. The Carey-led rule
determines which requests receive that space and what unserved traffic
can still do. The resulting movement changes the lane densities, which
changes the desires and limits at the next update. At the final E cell,
the lane-end geometry replaces discretionary E desire with a mandatory
A request; it does not grant E a higher receiving priority.

The cohort initialization, information rivals, complete-time objective
and sensitivity/validation design belong to the task formulation around
these traffic modules. Generic conservation is standard accounting.
Source colors credit the underlying rules; the exact assembled variant
and its qualifications remain explicit.

## What Subraveti originally does, and why replace that component?

2026-10-23. The user observes that Subraveti's own simulations necessarily
need service-allocation rules and asks what those rules are and why Carey
is needed. **Subraveti does provide a flow-realization rule. The reason for
replacement is difficulty safely transcribing its printed rule, not an
absence of a simulated traffic model.**

### The native rule: lateral transfer followed by adjusted forward flow

The original model treats lane changing as a transfer to the neighboring
cell at the same road position, followed by longitudinal flow. Its
calculation has three connected parts:

1. **Form lateral requests.** Multiply a cell's sending demand by its
   density/incentive-based desired lane-change fraction.
2. **Restrict lateral transfer using the adjacent lane.** A factor based
   on the target cell's receiving supply relative to capacity modifies the
   requested lateral flow. The intention is that available room limits
   the attempted transfer. The printed full-blockage branch has a separate
   ambiguity discussed in the source audit; neither central counterexample
   below relies on that branch.
3. **Recalculate forward service after accounting for lateral exchanges.**
   Add incoming and subtract outgoing lateral flow in the printed adjusted
   demand and supply quantities. Forward flow is then the minimum of the
   adjusted upstream demand and adjusted downstream supply. Conservation
   combines the lateral and forward transfers into the new lane densities.

Thus its allocation is embedded in a lateral-first/adjusted-forward
construction, rather than expressed as the current task's joint sharing
of all requests against one receiving budget. This ordering does not by
itself mean a formal right-of-way priority identical to our fixed weights.

The physical motivation is substantive: the paper argues that diagonal
transfer based only on the next cell's supply can misrepresent congested
wave propagation, and therefore makes the current adjacent cell matter in
the lateral stage. Changing the transfer interpretation is consequently a
behavioral adaptation, not a notation change.

**Source locations in the archived article:** PDF pp. 6–7 / printed
pp. 1761–1762 explain the transfer choice; PDF p. 10 / printed p. 1765,
Equations 13–17 specify requests and receiving restriction; PDF p. 11 /
printed p. 1766, Equations 20–22 specify the adjusted forward rule.

[Subraveti: archived primary article](../../archive/full_text/FB0030.pdf)

### Why direct reuse was not selected

The earlier review found two concrete accounting obstructions under
admissible positive densities, before adding VSL:

- **A lateral departure can make printed receiving negative.** Start with
  a congested cell that has little receiving space, then let substantial
  traffic change out into a free neighboring lane. That departure should
  release room. The printed adjusted-supply rule subtracts the departure
  from the receiving allowance and can make it negative. Taking the
  subsequent minimum then gives negative forward flow. This check uses
  only one lateral direction and avoids the disputed full-blockage and
  capacity-drop branches.
- **Two neighboring requests can spend the same traffic twice.** A busy
  middle lane can generate a strong request toward each less crowded
  neighbor. The pairwise fractions can sum to more than the donor's whole
  sending amount. The conservation equation contains both lateral
  directions, but the inspected rules do not specify joint normalization
  or a direction-selection rule to resolve that case. A literal summed
  simultaneous realization can therefore make residual forward demand
  negative. A hidden sequencing or selection convention could change this
  result, but cannot be assumed to be the source's rule without evidence.

These are already established exact hand examples, not newly executed
traffic experiments. They show why unrestricted direct transcription was
not accepted. They do not prove that the authors' uninspected code produces
negative traffic, nor that a clarified or repaired native rule is impossible.
The selected later thesis material clarifies one receiving branch but did
not resolve both accounting issues. Merely adding Han's VSL sending cap
does not supply the missing joint allocation.

[Original equations, explicit assumptions and hand counterexamples](../../synthesis/research_readiness/vsl_lane_backbone_flow_checks.pdf)

[Source inspection scope and interpretation limits](../../extraction/research_readiness/vsl_lane_backbone_source_audit.md)

### What the Carey-led replacement buys, and what it does not establish

The needed capability is an explicit, physically admissible realization:
each origin's available traffic is used once, each destination's receiving
space is shared once, and unsuccessful lane changes have a stated outcome.
The selected Carey-led adaptation provides that through common donor and
receiver limits, fixed-priority capped sharing and forward continuation
where the original lane still has room. At E's end there is no forward
connection, so unmerged traffic waits. Under the declared input/CFL bounds,
the selected construction has a conservation and stock/storage proof.

Carey is the principal source for these movement/sharing principles, with
Wright supporting the sharing formulation. The exact three-lane
normalization, allocation sequence and lane-end closure remain our
adaptations. The choice also changes same-position lateral transfer into
diagonal movement, which can change congestion propagation. We have not
established that the adapted model is empirically more accurate or gives
better gradients than a clarified native implementation.

**Carey is not the only mathematically possible remedy.** An authoritative
native algorithm or a separately justified repair could support another
consistent realization. The current choice is a source-backed, explicitly
qualified replacement that preserves the lane-state/incentive backbone,
instead of silently changing signs, clipping negative values or assuming
unreported priorities. This explains the existing selection; it does not
reopen it or authorize a new repair/implementation pass.

[Selected component and admissibility proof](../../synthesis/research_readiness/vsl_allocator_contract_and_checks.pdf)

[Selected behavior and its stronger direct-reuse rival](vsl_allocator_findings_and_gate.md)

## How Carey determines lateral direction and proportions

2026-10-23. The user asks for the core logic behind Carey's lateral
movement directions and proportions. **The desired lane-change fraction
and the share of scarce receiving service are different quantities.**
Carey separates lane-change intention from its realization. The current
task uses Subraveti for the state-dependent intention and a Carey-led
adaptation for realization.

### In Carey's original study

**Direction follows the required exit lane.** Traffic enters with a
prespecified lane in which it wants to leave the road link. Traffic
currently in the other lane therefore needs to move toward that target.
The worked algorithms simplify this to two lanes and one changing
direction. The paper focuses on mandatory lane changes; it does not
implement a general density- or speed-based choice of whichever adjacent
lane currently looks best.

**The intended proportion follows a chosen lane-change timing/location
model.** Section 4 offers alternative ways to determine how much of the
remaining target-bound traffic wants to change now:

- All eligible traffic seeks the first available opportunity.
- Only a location-dependent fraction seeks a change, potentially rising
  toward the end. This can represent increasing urgency without making
  everyone seek the first opportunity.
- Entering traffic has different planned change locations. The model
  carries the unsatisfied demand of traffic whose planned location has
  been reached, bounded by the traffic actually present.

These are alternative behavioral assumptions supplied to the traffic
model. They do not constitute one universal formula inferring intentions
from congestion. The paper also discusses anticipation of harder merging
farther ahead, but explicitly does not present a formulation/result for
that anticipation case. A higher intended fraction remains a request,
not a guarantee of accepted movement.

**Realized movement follows receiving competition.** Traffic continuing
straight in the target lane and traffic entering laterally compete for
that lane's receiving space. If both demands fit, both can pass. If they
do not, Section 5 considers three sharing principles: give existing-lane
traffic priority, share in proportion to demand, or use prescribed
nonnegative shares. Service is capped by actual demand and unused
entitlement can be redistributed. The native model can also charge
lane-changing traffic more receiving space through a headway/gap factor.
Remaining traffic may continue in its original lane where space allows;
desired changes are not guaranteed to finish before the link ends.

Source locations in the inspected author manuscript: Section 3, PDF p. 6 /
printed p. 5, defines entry/exit-lane traffic types and the one-direction
simplification; Section 4, PDF pp. 7–9 / printed pp. 6–8, gives intention
models; Section 5, PDF pp. 9–13 / printed pp. 8–12, gives receiving,
headway and priority rules. The local reading copy remains
`/tmp/vsl_allocator_review/Carey_2013_author_manuscript.pdf`.

[Inspected primary author manuscript](https://eprints.whiterose.ac.uk/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

### In the current task

| Decision | Current rule and ownership |
|---|---|
| **Which lateral directions can be considered?** | Lane adjacency and the permanent lane end define permissions. Before the end E/A and A/B are adjacent; no direct E/B jump exists. |
| **How much traffic wants each permitted direction?** | Subraveti's perceived-density contrast and route/keep-right/cooperation incentives determine desired proportions. Carey's original target-lane cohorts and location profiles are not substituted for those incentives. |
| **How do one origin's requests fit its traffic?** | Our Carey-supported proportional-normalization adaptation prevents two lateral requests from jointly exceeding one sending amount. The remainder initially requests straight movement. This is distinct from receiver-side priority. |
| **Which requests get through a receiver?** | The selected Carey-led adaptation uses fixed equal reference priorities, capped requests and unused-share redistribution. It uses ordinary receiving space without a separate extra merging-headway factor. Equal priority concerns streams entering one destination, not equal splitting toward an origin's two neighbors. |
| **What happens to unsuccessful attempts?** | They may use remaining forward space in the same lane. There is no second lateral allocation to another neighbor within that step. At final E, all sending requests A service and unserved traffic waits because E has no forward outlet. The permanent-end closure is our adaptation. |

For an E-to-A attempt, Subraveti determines the request, Han determines
the available sending/receiving, and the Carey-led allocator determines
how much crosses alongside A's own traffic and any other contender.
Stronger urgency can increase the request; it does not increase its fixed
priority. Actual lateral proportions can therefore vary with traffic and
space even though the reference priorities are constant.

This clarification changes no selected rule, preference, direction or
scientific status. It does not import Carey's native intention profiles,
cohort/FIFO state or additional headway multiplier into the current task.

## Where the peer works enter

**Subraveti's article [3] is the principal lane backbone.** It supplies the
physical picture: successive road sections retain traffic separately in
each lane. Lane-change desires depend on perceived density differences,
the need to leave an ending lane, and keep-right/cooperation incentives.
This directly supports asking whether E and combined A+B traffic conceal
an important A/B difference. The same author's thesis [7] clarifies the
2:2:1 downstream lookahead; it is a specification source within this
framework, rather than an additional traffic module. We retain the lane
states and preference forms. We replace the native coupling of same-cell
lateral and adjusted-forward flows. Thus adopting this backbone does not
mean reproducing its full original dynamics or calibration.

**Han 2016 [4] and Han 2017 [5] supply the congestion and VSL rules.** They
determine how much traffic can leave a section and how much the next section
can receive, including density-dependent discharge and congestion-wave
constraints. The 2016 congestion model is already a cited ancestor of
Subraveti's model. The 2017 work provides the explicit nominal cap and
speed-advice restriction on sending. We use this source lineage to specify
the budgets completely, then apply one target-lane receiving budget to all
arrivals. That shared-lane interface is our adaptation. We do not import
Han's full predictive controller. Advice changes sending directly and later
receiving through traffic-state changes.

**Carey [6] supplies the movement interpretation for the replacement.** A
lane-changing unit advances into the next section of the neighboring lane.
A desired change may fail for lack of receiving space; away from the lane
end, residual traffic may still advance in its original lane. This gives
the replacement its attempt-and-forward meaning. Carey supports diagonal
transport, receiving competition and forward fallback. We adapt those
principles; we do not reproduce its cohort/FIFO representation or treat its
worked two-lane algorithms as a complete three-lane, permanent-lane-end
solution.

**Wright [8] supplies a direct sharing formulation inside that same replacement.**
When several requests compete for one target's receiving budget, positive
fixed priorities assign shares, requests cap what each donor receives, and
unused entitlement is redistributed. Our member uses equal priorities.
For example, queued E and continuing A can compete for the same A outlet;
if A requests less than its entitlement, E can use the remainder. This is
a local allocation kernel adapted from the source, rather than the full
Wright general junction model. It does not imply a fixed realized merge
fraction or transfer the general model's guarantees. Carey also supplies
priority sharing and unused-share redistribution through R3/A3. These
source roles overlap; Wright is not needed to introduce a second physical
merging effect that Carey lacks.

Carey and Wright therefore contribute to **one composed movement module**:
Carey explains where attempted traffic can go, while Wright supports how
competing requests share receiving. Our joint normalization, first
allocation followed by one straight fallback, and final-E merge-or-wait
connection complete that module. These are substantive adaptation choices,
not merely notation or mass bookkeeping. The changed transfer topology can
change congestion propagation.

## Why the full Han budget, and could one movement source suffice?

**Subraveti explicitly adopts Han's congestion approach.** The article's
capacity-drop section, printed pp. 1765–1766, says that Han's approach is
used in its model, then gives a short formulation and refers to Han for
details. Its reported numerical study includes simulation, calibration
and validation of that lane model. This supports reported author use of
a Han-based component, rather than merely our proposal to combine the
works. Subraveti does define traffic budgets; the reason for selecting
the full source formulation was not a lack of receiving capability or
an inability to represent A/B differences. Its short summary also
states a mode condition: use the modified demand/supply while density falls
from a cell to its successor, and ordinary CTM otherwise. Applying that
sentence literally to sending can switch off a congestion ceiling when
the next cell becomes just slightly denser. The earlier hand example showed
a service increase even though the downstream density increased. We did
not establish whether that is the authors' intended implementation.

The selected full Han formulation supplies the congestion/recovery details
and retains the congestion ceiling without that extra sending switch.
Han 2017 also supplies the explicit speed-advice restriction. This is an
openly selected completion of the existing source lineage, with a meaningful
behavioral difference from the literal mode-gated alternative. It is not
just another citation for identical equations.

The author-level support has a precise limit. It establishes Han 2016 as
part of Subraveti's model ancestry and reported numerical model. It does
not establish that the authors implemented our exact ungated H completion,
the Han 2017 advice rule, or the shared-target mapping into our replacement
allocator. No inspected author code or clarification resolves that identity.
“Continuing Subraveti's Han-based congestion formulation” is supported;
“our exact assembled variant was certified by Subraveti” is not established.

A fully specified Subraveti-based completion remains possible in principle;
the review did not prove that its mode-gated budget cannot answer the research
question. It was not selected because the unexplained sending switch and
additional lane-end convention would become assumptions to justify. Returning
to it would change the approved budget and require revisiting dependent
analytical findings. Keeping the selected Han equations while removing their
source credit would not reduce model complexity. The separate printed
adjusted-flow problems that motivated the movement replacement are not a
blanket refutation of Subraveti's underlying budget model.

**Carey and Wright are not both mathematically indispensable.** Carey R3/A3
already lets competing streams share receiving with chosen nonnegative
fractions, caps service by available demand and returns unused entitlement
to the other stream. In its two-stream, unit-headway case, equal fractions
have the equal-priority capped-sharing meaning used here. Wright gives a
direct formulation for multiple contenders and a wider junction context;
it was useful in constructing and crediting the kernel, but does not add a
separate forced-merge state or penalty.

For intuition, give a receiving lane ten service units. Two sufficiently
demanding streams with equal entitlement receive five each. If one requests
only two, the other may receive eight. Carey's R3/A3 already expresses this
logic. The three-lane extension, joint donor normalization, allocation/fallback
sequence and permanent E end still need our explicit definitions. Thus a
Carey-led adaptation is a feasible way to describe the component without
treating Wright as an independent dynamics module; it is not a claim that
Carey's unchanged two-lane algorithm supplies the whole stack.

For the terminal shared-service problem alone, a Wright-style multi-input,
single-output merge can also work once lane budgets and connections are
given. It does not by itself specify the upstream diagonal transport and
the ability to continue straight after a failed lane-change attempt. Those
rules would need separate justification. Using the previously considered
full junction rule with committed fractions would change that behavior,
rather than merely reduce source count. Carey is therefore the more natural
single principal movement reference for the selected attempt-and-forward
semantics, with Wright retaining credit for the sharing formulation actually
used. Neither observation changes the selected equations or source history.

That makes the user's proposed source hierarchy reasonable: **a movement
component adapted primarily from Carey, with Wright supporting the allocation
formulation.** Supporting does not mean weaker-quality evidence; it means
no additional independent traffic mechanism is imported from that work.
The mathematical need is a consistent sharing rule, and Carey's R3/A3
already provides the two-stream principle.

However, not every remaining adaptation is merely scenario-specific.
Removing E's straight continuation at the lane end follows the geometry.
Choosing how a donor divides excessive requests toward two neighbors,
giving first-pass requests precedence over forward fallback, and dropping
cohort/FIFO state are behavior/model choices. They fit the selected
elementary task and have the existing conditional analytical checks, but
are not uniquely imposed by the road geometry or certified as Carey's
unchanged dynamics. Using Carey as the principal source simplifies the
architectural account; those choices still need to be stated and owned.

## What remains ours, and what this says about simplicity

We define the finite initialized cohort, free completion outlets, constant
common advice and observers that conceal or reveal the A/B split. We also
derive the exact remaining-time objective and its complete regular-branch
sensitivity. Conservation and chain-rule calculus are standard; their
application and the task-specific residual are documented here. These
choices are part of the task's justification burden even though they are
not additional traffic-model families. All member assumptions in the
existing contract still apply.

The eight bibliography entries have different roles: [1] Jin--Jin and [2]
Wei--Han--Wang are comparison models, not ingredients. The remaining six
sources fall into four groups: Subraveti article/thesis, Han 2016/2017,
Carey, and Wright. Source grouping makes the architecture clearer, but
does not by itself prove simplicity.

The useful complexity judgment is therefore: **one principal lane model
and its congestion/VSL lineage, one composed movement replacement, and our
research-task/accounting definitions.** This is a more concentrated model
design than the many colors suggest. It is still more adaptation than an
unchanged published model plus one unchanged published component. The
movement replacement is the main new traffic-behavior burden; the shared
budget mapping and task assumptions also need explicit justification.
The analytical review supports a complete, admissible construction under
its assumptions. It does not prove that this is the globally smallest
construction, inherit the source models' empirical fidelity, or establish
positive information/gradient benefit.

## Supporting records and work record

[Current report and numbered references](../../synthesis/research_readiness/vsl_literature_backbone_review_report.pdf)

[Source and interface audit](../../extraction/research_readiness/vsl_methodology_review_source_and_interface_audit.md)

[Carey/Wright adaptation boundaries](../../extraction/research_readiness/vsl_allocator_sources_and_adaptations.md)

[Han lineage and budget mapping](../../extraction/research_readiness/vsl_congestion_join_sources_and_adaptations.md)

[Selected member assumptions and source details](../../extraction/research_readiness/vsl_joined_candidate_sources_and_assumptions.md)

This note and the successor dialogue are the only files edited in this
response. Reuse the existing source audits; no new paper reading is claimed.
Inspect with `rg`, `cat` and `sed`; write with `apply_patch`; check local
links with Python file tools and report hashes with `sha256sum`; inspect
`git status --short`. No traffic, gradient or optimization experiment is
performed. The current PDF/LaTeX remain byte-identical. Analytical review
status and the pending report/JM1 acceptance remain unchanged. The next
allowed action is bounded discussion or a requested presentation revision.

**Dependency clarification follow-up, 2026-10-22.** Reuse the Han/LF2 and
allocator/LF1 findings and selection records. Reread the already available
Carey manuscript text around R3/A3 and forward progression to verify the
overlap above; no new full-paper reading or literature search is claimed.
Update this explanation and the successor dialogue only. Check their local
links and unchanged current report hashes. This clarification does not
replace either selected component, reopen a closed gate or start a new
review/implementation pass. Any actual return to a different budget or
movement law remains a separate methodological decision.

**Author-adoption and movement-hierarchy follow-up, 2026-10-22.** Targeted
primary rereading confirms Subraveti's explicit Han adoption and reported
numerical use, while retaining the exact-variant limitation. Synchronize
the Han and allocator source records with this clarification and append
the successor dialogue. These four Markdown files are the only edits in
this response. Check their local links and unchanged report hashes; retain
all selected equations and gates. No author-code verification, new full-paper
review, experiment, dependency installation or implementation is claimed.

**Compact-wording follow-up, 2026-10-22.** Record the user's proposed
inherited-dependency interpretation above, using “completing and adapting”
to include substantive interpretation choices as well as task-specific
interfaces. Update this note and the successor dialogue only with
`apply_patch`, and inspect the inserted text with `rg`. No model or report
file changes; the existing review/acceptance status is preserved.

**Report revision follow-up, 2026-10-22.** The user authorizes incorporating
the agreed hierarchy in the PDF. Update the report and navigation, retain
formula/source colors and supporting credit, and archive the preceding
version. The selected equations and scientific decisions remain unchanged.
The linked hierarchy work record contains the files, build and checks.
