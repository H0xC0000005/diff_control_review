# After the last merge, can slow through traffic renew the service loss?

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

**Earlier report body:** the text below records the preceding source-choice
gate. R-E is now selected; RE-O1 in the current report is the live decision.

Date: 2026-10-15. **S-E-P is user-selected; the admission-priority gate is
closed.** Its continuation checks clearance behavior and forms two explicit
recovery laws. The new question concerns whether slow A departures create
fresh impairment after E has already caused a restriction. This pass stops
at that physical source choice, **SEP-R1**. The whole model is not frozen.

## The traffic question that now matters

Imagine E has merged slowly and reduced the service shared with A. Some A
traffic has accumulated and is still moving slowly after the last E has
crossed the line. There are two different explanations for what happens next.

One explanation treats the A stream as **following a restriction already
represented in the account**. The account recovers from the E disturbances;
A consumes whatever service is currently available and its remaining queue
then drains. The other explanation says those slow A departures **create
fresh acceleration burdens of their own**, so they can extend the recovery
tail. Both are compact, causal models of one shared service account. They
make different physical commitments, rather than simply retaining different
amounts of bookkeeping.

The selected priority rule does not decide between them. Nor does the fact
that A is queued prove that its departure creates another independent loss.
This is the next scientific choice before completing the account.

## What is settled about S-E-P

A's offered traffic takes priority while A remains unqueued and its offer
fits the shared budget. E uses the feasible remainder. If A also queues,
the cooperative branch serves both streams.

There is one useful clarification of “until both are queued”: **when E's
queue clears before A's, the proposed S-E-P rule keeps the cooperative
branch until A clears**. It serves E's current arrivals and returns unused
work to A. It does not restore strict A priority every time E briefly has
zero backlog. The exact clearance check shows why the latter toggle can
require the same empty E queue to grow and immediately disappear, with no
consistent nonnegative continuation.

This preserves the S-E-P option as proposed and selected. No additional
latch, queue floor, smoothing or numerical event convention is introduced.
The actual fairness formula, current-work coefficients and representative
speed law remain subject to qualification.

[Recorded S-E-P selection and precise scope](vsl_sep_selection_and_scope.md)

## Current traffic determines the split; recovery determines available service

The user's clarification is consistent with R-E: the allocation rule uses
current A/E conditions and the currently available shared budget. Both
queued streams cooperate; free A has the selected priority when its offer
fits. No additional preference depends on which stream queued first, how
long cooperation has lasted, or a remembered allocation mode. The earlier
wording “keeps the cooperative branch until A clears” refers to A's current
queued condition, not a latch that survives after that condition disappears.
At an exact queue boundary, the causal shortfall/clearance rules still
need to give a consistent continuation; this clarification does not complete
that proof.

R-E addresses a different question: which actual departures add new loss
to the shared recovery account? Its answer is E admissions, with profiles
conditioned on their predicted speeds. Earlier E disturbances can still
reduce the budget now, even when the visible A/E queues match another
case. Given the same current traffic inputs and budget, the trial node
must give the same current allocation; its future budget may still depend
on the account's retained recovery profiles. This is not a claim that the
single budget reading alone is sufficient state for future evolution.

R-AE can use exactly the same current-state allocation rule. It differs
only by also letting sufficiently slow A departures add recovery profiles.
Thus the clarification supports the shared allocation interpretation but
does not select either recovery source law or require a memoryless total
service model. SEP-R1 remains open.

## Why asymmetric disturbance is a reasonable simplification

The user's intuition gives R-E a reasonable elementary interpretation:
A continues along its own lane, whereas E must enter that lane. Ordinary
A passage uses the baseline service; E's additional maneuver can consume
extra work and leave a recovery disturbance affecting both streams. When
both queue, closer speeds can reduce the mismatch burden while E still
has a lateral maneuver. Cooperation therefore need not give identical
per-unit service costs. Exact costs and shares remain trial laws.

The interaction remains coupled: A's current traffic consumes shared service
and affects E admission, while admitted E can impair later A service. The
asymmetry concerns an **additional disturbance source**, not an assertion
that A has no effect on E. R-E further assumes ordinary slow A release
needs no independent new recovery profile beyond the restriction already
represented. A weaker A burden alone does not prove that this additional
source is exactly zero; that omission is the explicit minimal approximation.

The inspected model of Leclercq et al. provides a related precedent: slow
insertions are bounded-acceleration moving restrictions, while mainstream
followers use a first-order traffic model, including when both approaches
are congested. Its introduction and model assumptions were rechecked for
this clarification. It does not validate our aggregate profile overlap or
establish universal absence of ordinary queue-discharge recovery effects.

[Primary merge-model precedent, introduction and Section 2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

This supports the rationale for R-E as a minimal source approximation.
The user asked whether that rationale is sound; no source-law choice or
new qualification pass is recorded from this question alone. SEP-R1 remains
open, with the same current-state sharing rule available to both candidates.

## The common recovery model that can now be written

The continuation turns the earlier isolated acceleration calculation into
a **speed-marked recovery profile**: an admitted unit of mass leaves a
temporary loss profile whose strength and duration depend on its predicted
departure-speed mark. A sufficiently fast passage leaves no profile; a
slower one leaves a stronger, longer profile. The profile recovers over a
physical acceleration and backward-propagation time, not a numerical step.

Continuous admitted mass contributes to one aggregate loss history. The
remaining shared budget is the ordinary ceiling minus that aggregate loss,
with zero service possible while the loss exhausts the ceiling. Each
candidate produces one budget, rather than independent constraints attached
to every departed unit. The account can retain sufficient history without
representing microscopic vehicles or a spatial recovery reach.

This is a **concrete constitutive family**, with equations, units and bounds
in the mathematical note. It is not yet an empirically established model.
In particular, adding the profiles assumes a particular form of overlap;
identifying the point's representative departure speed with a first-order
boundary trace is still an adaptation. The same physical burden must not be
charged once as current maneuver work and again as retained recovery.

The immediate E cost and speed feedback remain the prior trial work family.
The new comparison changes **which admitted streams deposit new recovery
profiles**, keeping those other assumptions the same.

## Two concrete versions, compared through the same A tail

| | E-origin recovery, **R-E** | Renewal by both slow streams, **R-AE** |
|---|---|---|
| **What creates new impairment?** | Admitted E mass, with a profile determined by its predicted current speed. | The same E source, plus admitted A mass whose predicted speed is low enough to produce a nonzero profile. |
| **What does a slow A departure mean?** | It uses the restricted service already represented. It is not separately counted as a new disturbance. | It creates a new recovery burden even if the original reason for slowing was an earlier E passage. |
| **What happens after the last E admission?** | No new profiles enter the account. Existing loss decreases and vanishes within the maximum profile duration. A may still have a queue to drain. | Slow A admissions can continue depositing profiles. Total service can recover more slowly, depending on the balance between new deposits and recovery. |
| **Does A information matter?** | Yes. A's offered flow and boundary state affect E admission, its speed mark and subsequent loss, as well as A's own service. | Yes, through those same interactions and through A's additional direct recovery source. |
| **Is this the old fixed-speed M1 model?** | No. The E speed mark and resulting profile are predicted from current traffic, rather than fixed in advance. | No. Both streams can contribute variable profiles. |
| **What extra assumption is made?** | The represented E disturbances suffice for follower recovery at this level of abstraction. | Each sufficiently slow A passage renews impairment; its profile is additional to existing loss. |

The difference is quantitatively consequential even in an A-only tail.
Under the trial first-order speed identification, an A discharge using a
reduced budget deposits positive new loss in R-AE. R-E has no such deposit.
The mathematical note gives an exact local example and the derivative
difference. It does not claim a universal ordering of the two full,
endogenously changing traffic trajectories.

## The new evidence, and its practical limits

The speed-marked profiles have a finite maximum duration and a bounded
integrated loss. Continuous mass conservation therefore bounds the **total
future service work that can be lost** under either explicit source law.
For any admissible causal solution, that fills the previously unspecified
finite-loss assumption in the sufficient clearance bound. Neither model
needs an artificial positive service floor to obtain that conditional result.

Within a fixed traffic regime, the prior monotone discharge equation and
the new profile bounds give a local causal construction of the coupled
history and service. **This does not establish unique evolution through all
queue switches**, or prove that the speed/overlap assumptions match traffic.
Whole-model existence and event consistency remain open.

A second finding limits the claim we may make. With **constant underloaded
A arrivals**, empty A and neutral initial history, these smooth admission-
driven laws can throttle E before the shared budget falls below A's
protected offer. A then remains free, although E may wait and lower the
available service. Adding the R-AE source does not create the first A queue
in that limiting case, because free A does not yet contribute a slow profile.

This is a conditional negative case, not a requirement for an external
disturbance or ordinary overload. H1 actually generates changing A arrivals,
so the constant-rate result does not decide the primary task. It does mean
that a consequential A-delay/MP6 example must still be demonstrated for the
finished joined model. The priority and account cannot simply be assumed to
produce every desired traffic effect.

## The scientific choice and provisional recommendation

**Problem statement.** Should ordinary slow A departures merely follow the
already represented restriction, or should they deposit fresh recovery loss
of their own?

**Function in the chain.** The affected part is the source/update law of
the single shared account, after actual admission and speed prediction.
Its output restricts subsequent A/E departures. It therefore changes the
duration of congestion, complete local travel time and control sensitivity.

**Core gap.** A low representative A speed does not by itself identify
whether that passage creates a new restriction or is already a consequence
of the current one. Conservation and the fixed queue geometry do not supply
that attribution. A smaller per-lane flow can also reflect how service is
shared; it does not by itself measure an individual crossing speed. The
trial first-order speed mark is an additional assumption. Treating all slow followers as independent sources may
overcount; treating none as new sources may omit genuine acceleration effects.
This is a Type 2 G3 physical closure, not a transcription detail.

### R-E: E initiates disturbance; A follows and drains

Use the speed-marked E history as the source of new loss. A changes that
history through the coupled admission rule, and is delayed whenever the
remaining shared service is insufficient. Its own slow departures do not
independently renew the account. After the last E source, recovery has a
finite expiration even if an A backlog remains.

- **Pros:** a direct continuation of the insertion-led moving-bottleneck
  interpretation, with the smaller source assumption. It avoids automatically
  charging a follower a second time for the same disturbance. It has a
  specified finite-memory law and conditional clearance bound, while retaining
  traffic-dependent interaction with A.
- **Cons:** it deliberately omits independent renewal by ordinary A traffic.
  If a real queued A stream continues to generate acceleration losses beyond
  the represented E recovery, this model can recover service too quickly.
  E-profile overlap and representative insertion speed still need evidence.
- **Dependencies/consequences:** the exact E profile, current-work/recovery
  partition and full hybrid law still require qualification. It does not
  prove A impact in the primary H1 family or a positive control result.

### R-AE: slow A departures also renew the disturbance

Use the same concrete E law and add speed-marked A contributions to the
same aggregate loss. A passage contributes only when its speed mark gives
a nonzero profile. It can therefore extend the account's recovery tail after
all E admissions have ended. This makes slow follower discharge an active
part of the mechanism.

- **Pros:** directly represents the possibility that slow A releases have
  their own continuing acceleration burden. It remains a compact point model
  with one account, continuous mass and a finite-loss bound. The conditional
  nature of the speed profile avoids a penalty triggered merely by queue
  presence.
- **Cons:** the additional-profile assumption is stronger than the isolated
  insertion calculation. The trial A speed is a boundary trace, not independent
  evidence of a new physical bottleneck. Additive profiles can count inherited
  restriction again; a finite mathematical bound does not validate that
  attribution or its magnitude.
- **Dependencies/consequences:** the source attribution and overlap must be
  defended, including the A-only tail and its native-reference correspondence.
  Extra A renewal does not by itself solve the first-A-queue limiting result.
  No new spatial state or initial observation is approved by discussing it.

**Provisional recommendation: qualify R-E first as the minimal primary
candidate**, keeping R-AE as a serious recovery alternative. The reason is
that the directly reused mechanism treats E insertions as new restrictions
and ordinary A traffic as followers; a separate A renewal law needs additional
support. This is not a conclusion that A recovery is negligible in nature.
**Neither recovery source law is selected.** Both are concrete candidates
with outstanding physical and global-event qualification; the choice is
about their traffic assumptions, not “accept now” versus “review later.”

The inspected merge source separates inserted moving restrictions from
kinematic-wave followers and explicitly studies interactions between their
effects. A broader bounded-acceleration source also shows that the relation
between acceleration and extra capacity loss depends on the traffic setup.
Neither supplies these two aggregate source laws as ready-made results.

[Viewed primary references and exact access/adaptation limits](../../extraction/research_readiness/vsl_sep_recovery_source_and_adaptation_audit.md)

## Review position and stopping status

| Part of the approved review | Direct answer now available | Still required |
|---|---|---|
| **Admission and actual discharge** | S-E-P is selected. The E-clearance case preserves cooperation while A remains queued; the literal two-positive-queue toggle is inconsistent in an exact diagnostic. | Exact cooperative fairness, work/speed provenance and global event consistency. |
| **One shared recovery** | Two explicit speed-marked source laws can be written. Both retain finite predicted history and one service output; their A-only tails differ. | SEP-R1 source choice, physical attribution/overlap and the finished coupled law. |
| **Joined qualification and MP6** | Each explicit law supplies a finite integrated-loss bound and conditional finite clearance. Storage and local TST interfaces remain. The constant-A protected limit is identified. | Whole-law existence/uniqueness, a consequential reachable primary case, and independent information/action/gradient/native evidence. |

**S-E-A2 is closed with S-E-P. SEP-R1 is the current open gate.** The
three-part review and Step 3 remain in progress. The constant-rate finding
is a limitation to carry into qualification; it does not overturn the whole
compact stage or silently reopen the selected priority.

H1/cutoff, the primary ordinary-underload domain, finite storage, initial
information, independent unqueued B, local completion and S-P→S-L remain.
M1/P-E, immediate cooperation, strong aggregate/history/ending-statistic and
search rivals remain available. No full-lane-state necessity, interior optimum
or positive gradient result is required. No simulator, installation or traffic
experiment occurred. Stop here before selecting the new physical source law.

[Mathematical laws, clearance check and limiting-case proof](../../synthesis/research_readiness/vsl_sep_recovery_and_clearance_audit.pdf)

[Work, changes and verification](vsl_sep_recovery_work_report.md)
