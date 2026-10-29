# R-E can start recovery loss causally; successive merges still need an overlap rule

**Current O-R qualification, 2026-10-15:** the user selects recent-mass
renewal, closing RE-O1. R-E and current-state S-E-P remain. The bounded
recovery candidate/analytical pass is complete at **OR-Q1**: physical
update/state, local causal coupling, derived positive service and clearance
bounds, and a regular full-cohort family with A delay and active retirement.
This does not establish realistic parameters, the whole original action
range, applied MP6 or useful gradients. The complete joined review and
Step 3 remain open; J4 follows review of this checkpoint. Earlier reports
retain delivery-time meaning. No implementation or traffic experiment.

[Selected renewal, analytical evidence and recovery checkpoint](vsl_or_recovery_qualification_and_checkpoint.md)

**Earlier report body:** RE-O1 below records its earlier delivery. The
user now selects O-R; the live result/checkpoint is OR-Q1 above.

Date: 2026-10-15. **R-E is user-selected; SEP-R1 is closed.** The review
has continued substantively. Its central finding is that choosing E as the
source does not yet decide whether successive E passages add separate
losses or renew one already affected stream. That difference can change
predicted capacity even with identical entry speeds. Stop at **RE-O1**
before choosing that physical overlap law.

## The traffic picture and what has been established

An E group waits at the lane end, enters slowly and temporarily reduces
the service shared with A. R-E gives that entry a recovery effect while A
follows the restriction. A's traffic still influences how much E can enter.
The service split responds to current traffic and the current budget; its
allocation has no separate historical preference.

The resumed analysis establishes four useful points for the trial law.

| Review question | Direct finding | Limit |
|---|---|---|
| **Can the admitted forced merge actually start the account?** | Yes. At the already established H1 fast-front example, E queues, its predicted entry is slow, and the shared budget immediately begins to fall. No external slowing seed is required. | This is a local reachable effect under the trial work/speed laws. A initially stays free; a consequential complete A-delay/MP6 case is not established. |
| **Does the additive account cause a finite-time service collapse?** | Starting neutral, its own admission feedback keeps the budget strictly positive at every finite time of any admissible causal solution. Fewer E admissions create less new loss as service falls. | This is a derived bound, not an imposed service floor. It does not prove a whole hybrid solution or validate profile addition physically. |
| **Do the selected allocation's strict queue switches have compatible directions?** | Yes. A strict shortfall gives positive growth for the newly active queue; a strict clearance admits the corresponding free offer. E clearance while A queues preserves cooperation. | These local checks do not prove global uniqueness, all grazing events or the absence of infinitely accumulating switches. |
| **What can a simpler model already reproduce?** | A state-dependent instantaneous work relation reproduces the additive model's stationary relation. If the initial free work already fits, H1's declining E offer leaves the whole task disturbance-free. | History must earn its role through transient behavior and independent usefulness. Neither an interior optimum nor a gradient advantage follows. |

The conservation, finite physical storage and complete local travel-time
interfaces survive admissible departures. The earlier finite integrated-loss
and conditional-clearance bounds remain. These results qualify parts of
the candidate; they do not complete the whole model.

## Why a second slow entry creates a real modeling question

Imagine another E portion enters before the first one's restriction has
finished recovering. There are two physical interpretations.

**Separate burdens:** each admitted portion leaves its own fading loss.
The account adds all remaining losses. More overlapping passages therefore
mean more lost service, even if each passage has the same speed.

**Renewal of the affected stream:** later E traffic refreshes the same
restricted stream. Older profiles gradually leave the representative
account as a reference amount of new E traffic passes. Loss can remain
low-speed for longer without adding every older restriction in full.

The reference point-insertion calculation evaluates recovery between
successive insertions. For repeated identical insertions, our capped
interval-mean deduction differs from adding each full recovery tail when
the next insertion arrives before recovery finishes. This is an analytical
screen of the overlap assumption, not evidence that every additive point
model fails. [Leclercq et al., Section 2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6).

The reference is prescribed-headway, homogeneous traffic. Neither the
source calculation nor our deduction supplies the complete transient
variable-speed law needed by this task. That extension must remain explicit.

## Two concrete R-E models, compared directly

Both candidates use the same isolated speed-dependent recovery profile,
the selected S-E-P sharing rule and one service output. They change only
how past E contributions combine. Their equations are in the mathematical
note; they are concrete constitutive families, not two procedural routes.

| | **O-S: sum the active burdens** | **O-R: renew through recent E mass** |
|---|---|---|
| **Core assumption** | Every admitted mass portion leaves an additional independent loss profile. | A recent reference amount of E mass represents the currently affected stream; older profiles retire from that representation as new mass enters. |
| **Retained information** | All E admission/speed history whose profiles have not expired. | The same history, restricted further to its most recent reference amount of admitted E mass. |
| **Second slow portion before recovery ends** | Its loss adds to the earlier still-active loss. | It contributes while gradually replacing older profile weight. Repetition can prolong the episode without accumulating all previous burdens. |
| **Repeated identical passage** | Gives the full-profile loss per mean headway. | Gives the interval-mean loss in the capped homogeneous fixed-headway point reference. |
| **Sparse passage after full recovery** | Agrees with O-R in the corresponding stationary reference. | Agrees with O-S; the distinction concerns overlapping recovery. |
| **After E finishes** | Existing loss decreases and expires within the maximum recovery duration. | The retained recent profiles also decrease and expire within that duration. |
| **Additional assumption to defend** | Distinct loss profiles add rather than representing the same unavailable service again. | A recent-mass average is an adequate transient renewal description; its physical renewal mass and retirement of older restrictions are justified. |

For O-R, the reference mass is continuous vehicle-equivalent mass, not an
integer vehicle counter or a packet size. Retiring a recovery profile
does not remove any traffic. All physical mass and waiting remain in the
unchanged T1 balances. Its role as a renewal scale is a physical assumption;
it cannot be treated as a harmless numerical resolution setting.

One consequence of O-R needs particular care: later fast E traffic can
retire part of an older slow profile before that profile would expire by
acceleration alone. That can represent renewal of an average affected
stream, but may release service too quickly if an older slow leader still
controls it. O-R is not an exact variable-speed moving-bottleneck solver.

## Renewal, sufficient current state and the case for addition

The user's follow-up intuition favors a useful physical principle: when
the continuing effect of an old restriction is already represented in
current traffic, it should not be charged again as another independent
burden. A model can update from its current state without reprocessing the
entire past, provided that state contains everything still relevant. This
is often called a Markov description. It is stateful: past effects persist
through the current state, rather than through an additional history input.

However, being admitted under an earlier service limit does not by itself
make the latest A/E queues, speeds and discharge a sufficient description
of that earlier restriction. Those quantities can reflect the restriction
without revealing its remaining recovery duration. In a conceptual example,
two approaches serve the same light demand with no queue. One still has an
older slow merged group recovering downstream, while the other has already
recovered. Their present observed flow can match while available service
for a following portion differs. This is an illustration of capacity versus
actual flow, not a new H1 reachability certificate or task scenario.

The relevant test is whether any older influence can still change future
service after the proposed current state is held fixed. If yes, that state
omits something. A compact current recovery state might supply it; no
spatial expansion or detailed per-vehicle record follows automatically.
The existing source studies interactions of waves and earlier recovery
effects; it does not establish that the last discharge alone is sufficient.
[Leclercq et al., Section 3.1](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6).

**O-R as written retains recent discharge/speed history.** It renews profile
weight over a physical reference amount of admitted E mass and continues
aging the retained profiles. It is compatible with the renewal philosophy,
but is not an instantaneous current-A/E-only formula, a latest-batch reset,
or a replacement on every numerical update. Physical renewal must remain
independent of the numerical time step. A strictly current-state-only law
without that recent history is a separate, as-yet-unformulated direction;
it must specify sufficient recovery state and a causal update before it can
replace either concrete candidate. This discussion does not rename it O-R.

O-S has conditional grounds that differ from merely keeping old constraints:

| Situation | Why addition can be defensible | What must be established here |
|---|---|---|
| **Earlier effects have expired before the next disturbance** | The profiles do not overlap, so their sum never charges the same recovery episode simultaneously. | This supports the separated-passage limit, not dense overlapping traffic. |
| **Different passages create distinct lost service work** | Separate maneuver-related time or service opportunities can add when they are genuinely different burdens. | Their loss partition must avoid counting the same restriction, or current maneuver work, twice. Continued influence alone does not prove additivity. |
| **Small disturbances around a declared operating state** | A linear response approximation can superpose marginal effects while neglecting higher-order interactions. | The kernel, operating range and approximation error need evidence. Our full isolated profile is not automatically a validated marginal-response kernel. |

These are modeling justifications to test, not new empirical findings for
O-S. Several capacity ceilings acting on the same stream would instead
require the tightest ceiling to be respected; summing their full losses
does not follow. Retaining an older active influence and adding every
older loss are different claims. The user's argument favors renewal of
one affected stream without by itself proving that all older influence is
captured by the latest upstream state or discharge.

O-R remains the leading concrete qualification candidate, with the explicit
recent-history and older-profile-retirement limitations above. The follow-up
is an intuition check, not approval of O-R or of a stateless replacement.
RE-O1 stays open; no new review pass or mathematical law is executed here.

## The decision, its tradeoff and provisional recommendation

**Problem statement.** Do successive E admissions create independent
additive loss burdens, or refresh a shared affected stream represented
by recent admitted mass?

**Function in the chain.** This is the overlap/update rule inside the
single recovery account, after actual admission and speed prediction.
It changes the budget supplied to the same A/E allocator and therefore
the predicted delay and VSL sensitivity. It is Type 2 G3.

**Core gap.** An isolated recovery profile specifies one restriction's
strength and duration. It does not specify the interaction of repeated
restrictions. Source attribution to E and finite mathematical bounds do
not determine that interaction. The reference comparison exposes a
consequential difference precisely where recovery overlaps.

### O-S: independent fading burdens

Keep the trial mass-weighted sum of all unexpired profiles. Each E portion
adds loss; only the profiles' physical aging removes it.

- **Pros:** the simpler existing aggregate law; no older restriction is
  retired merely because faster E later passes. It has a fixed-mode causal
  construction, a finite-loss/clearance bound and the new finite-time
  positive-budget result. The history can affect subsequent A service.
- **Cons:** full-profile addition is stronger than the isolated physical
  deduction. In the overlapping homogeneous reference it predicts more
  loss than interval renewal. Independence and the division between current
  maneuver work and retained loss need their own evidence.
- **Dependencies/consequences:** qualify it as a phenomenological additive
  law, not as the source's native repeated-insertion model. Its transient
  node, parameter provenance and primary MP6 still require qualification.

### O-R: recent-mass renewal

Average the same profiles over at most the most recent reference amount
of admitted E mass. New admitted portions enter that average; the oldest
weight retires. The account still has one output and uses predicted history.

- **Pros:** represents one stream being refreshed rather than repeatedly
  charging its entire old restriction. It matches the stated capped
  homogeneous point reference's interval mean, adds no spatial field or
  traffic queue, and retains bounded loss, finite recovery memory and a
  conditional clearance bound.
- **Cons:** extending that stationary reference to changing speeds is a
  new physical closure. It can retire an older strong restriction too
  quickly. The renewal mass has physical meaning, and the new cutoff needs
  its own causal/event proof. The additive law's uniqueness evidence does
  not transfer automatically.
- **Dependencies/consequences:** define and defend the recent-mass
  interpretation, especially a slow-to-fast E sequence. Continue to count
  all actual traffic and keep the current maneuver/recovery partition
  explicit. This changes the recovery formula, not H1, geometry or sharing.

**Provisional recommendation: qualify O-R first as the point-renewal
candidate, keeping O-S as the transparent additive rival.** Its attraction
is the explicit treatment of overlapping restrictions and the closer
homogeneous point-reference correspondence. Its transient retirement
assumption remains a real cost of that choice. Neither overlap law is
selected, and the recommendation does not assert that renewal is already
empirically valid or globally well posed.

## Where this leaves the planned review

| Approved joined question | Position after this pass |
|---|---|
| **J1–J2: entry, discharge and state** | S-E-P is selected; strict transition directions and a local reachable loss onset are checked under the trial work/trace family. Exact fairness, speed provenance and full event qualification remain. |
| **J3: one shared account** | R-E source attribution is now closed. Its overlap qualification reaches RE-O1 with two concrete formulas. This part is not complete. |
| **J4: joined task, MP6 and evidence** | Conservation/storage/TST and conditional clearance remain; a stationary-equivalent simple rival and an exact benign reduction are explicit. Consequential complete H1 A-delay/MP6, information/action and gradient/native evidence remain open. |

This is substantive continuation within the same compact terminal component.
**The full joined review and Step 3 are still in progress.** The finding
does not overturn the elementary stage, reopen E versus A source attribution,
or justify CTM, a new spatial zone or a broader primary demand domain.
The smallest new decision is RE-O1. Stop before selecting its formula.

[R-E approval and precise scope](vsl_re_selection_and_scope.md)

[Equations, transition checks, overlap comparison and proof limits](../../synthesis/research_readiness/vsl_re_overlap_and_boundary_audit.pdf)

[Viewed references and adaptation limits](../../extraction/research_readiness/vsl_re_overlap_source_and_adaptation_audit.md)

[Files, commands and verification](vsl_re_overlap_work_report.md)
