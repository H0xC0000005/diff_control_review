# S-E can describe causal queues; the first admission conflict needs a traffic interpretation

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

## The main finding: deciding how traffic waits is part of the model

The fixed choke does let us keep the traffic description small: two coupled
A/E waiting balances, the existing terminal travel/storage histories, and
one service/recovery account. S-E can then explain queue formation through
a real shortfall under a declared admission law, and clearance through the
waiting balance reaching zero. There is no need to locate extra queues.

The substantive issue exposed by the qualification is **which stream first
waits when E's maneuver makes the shared service insufficient**. A rule that
shares service work equally does not necessarily make E wait. If E's offer
fits its work share, that rule passes all E traffic and takes the shortfall
from A. A rule that first serves an unqueued A stream instead leaves E waiting.
These are distinct traffic interpretations even with the same total budget,
same state-dependent work law and same geometry.

For a simple accounting illustration, suppose the shared budget is 100 work
units, A offers 60 mass units and E offers 35, with initial E admission costing
1.2 work units per mass unit. Ordinary traffic would fit: its total is 95.
The declared maneuver work raises its requirement to 102.

| First-conflict interpretation | What happens in that same illustration | What the slowing would mean |
|---|---|---|
| **Immediate cooperation, S-E-W** | E's 42 work units fit its half-share. All 35 E pass; A receives 58 and begins waiting. | A yields service from the first conflict. E need not be the slow stream. |
| **Free-A priority followed by queued cooperation, S-E-P** | A first receives its 60. The remaining 40 work units admit at most about 33.3 E; E begins waiting. A qualified slower-entry rule can reduce E's rate further. | E initially has to fit the continuing stream's usable residual service. Later shared recovery can also make A wait. |

These are normalized static accounting examples, not measured traffic or
selected parameters. More importantly, the mathematical note repeats the
contrast using **the exact leading arrival state of the accepted H1/T1
family**, without inventing another external arrival scenario. Its strict
shortfalls support distinct local right-hand queue onsets under the stated
trial law and a continuous initially neutral recovery account.

Neither outcome is automatically impossible. Immediate yielding by A can
be natural cooperative behavior. Protecting free through flow while E waits
for usable service is also a reasonable elementary approximation. The source
evidence does not select one universally. We must make that interpretation
explicit before the shared account is completed.

## What concrete S-E model can now be formed

The candidate has an unqueued mode and a queued boundary mode for each
approach. An unqueued approach presents its eligible arrivals. A queued
approach presents its sending capacity. The selected node admits continuous
mass and the difference between arrivals and departures grows or drains the
waiting balance. Its regime follows the actual admission test and queue
history, with no numerical queue seed.

For a concrete constitutive test, I formed a work law with ordinary A passage
normalized to one. E uses a declared immediate maneuver amount plus an
additional cost when its boundary speed is lower than A's. The latter depends
also on actual A flow, so an absent A stream contributes no speed-mismatch
burden. The law can change both E's share and total usable discharge. A's
queue is not itself another imposed capacity penalty.

**This specific cost law is a proposed analytical family**, not an empirically
identified equation. Its immediate maneuver work can be zero, and its
one-sided speed effect is not asserted as a universal empirical law. Current
maneuver work and later recovery still need a defensible separation.

For the queued mode, the trial uses a congested first-order boundary relation
to obtain a representative speed from admitted flow. That gives a concrete
implicit service equation. A conservative bound on the strength of its
speed feedback makes that equation strictly increasing, proving a unique
feasible flow within each selected regime. The bound is a sufficient
mathematical domain, not a calibrated or approved traffic restriction.

The speed is a **boundary trace**, meaning the local state immediately
upstream of the service line. It is not average lane speed. Using it as the
representative insertion/recovery speed remains an explicit adaptation,
supported only conditionally by sources treating congested entry.

## What the transition checks establish

The rule now says: keep free passage whenever its actual admission test
permits it; activate waiting when that test has a strict shortfall; return
to an empty-approach test at true clearance. An alternative queued state
that could sustain itself is not enough to start a queue.

This excludes the arbitrary delayed queue births in the previous constant-
offer diagnostic: its free passage never encounters a shortfall. In the
new H1 example, by contrast, declared maneuver work produces a real shortfall
despite ordinary underload, so waiting begins without an external slowing
seed. Both results are conditional on their stated laws.

**What is not proved:** a unique solution through every simultaneous event,
grazing zero crossing or fully coupled recovery history. Unique flow inside
a regime is not whole-model uniqueness. The pass stops before silently
choosing an allocation and then claiming that stronger result.

I also checked the simpler alternative of sharing in proportion to each
lane's current demand. A direct graft of that rule onto T1's “empty demand
versus queued capacity” switch fails a consistency test in the same H1
example: an initial shortfall calls for a queue, but switching its demand
to queued capacity can immediately allocate more flow than that empty
queue possesses. None of the four proposed free/queued modes is compatible
with the required right-hand behavior in that example.

**That rejects this particular transcription, not demand-based merging as
a whole.** The native CTM rule and properly specified LTM node models remain
serious simpler rivals. The source literature explicitly distinguishes node
rules that remain consistent under the LTM boundary construction from those
that do not. Our two proposals also still need their own complete consistency
qualification; passing this local test does not confer a generic theorem.

[Primary LTM discussion, section 6](https://arxiv.org/pdf/1405.7080)

## Gate S-E-A2: how does free A participate in the first conflict?

**Problem statement.** Should an unqueued A stream first claim its offered
service, with cooperative allocation beginning once A is queued, or should
the two streams cooperate from their first service conflict?

**Function in the model chain.** This is the terminal admission allocator
inside component 6/G3. It converts the common account and approach demands
into actual A/E departures. Those departures determine boundary speeds and
the influences that later update the same account. It does not change H1's
early allocator, the number of queues or the completion line.

**Core gap.** Revised A1-C and S-E approve a traffic-conditioned direction,
not an exact fairness rule. The earlier equal-work module was explicitly
proposed. The reachable H1 contrast now shows why adopting it as a routine
convention would select meaningful traffic behavior. The source evidence
supports relevant allocation templates, not a unique lane-drop prescription.

### S-E-P: serve free A first, cooperate once A is queued

Keep A's current arrivals moving while they fit the shared available work.
E uses the remaining usable work, subject to its actual entry cost and
sending. E can therefore wait and enter slowly while A is still free.
If subsequent shared service loss makes A unable to pass its offer, A queues.
Once A is queued, use the cooperative allocation template; with both streams
waiting, both can receive service whenever the budget is positive.

The main addition is a **conditional traffic-priority rule at the point**.
It is not the rejected strict A-first server: queued A cannot automatically
exclude E. The cooperative template and state-to-work coefficients remain
to be qualified after this direction choice.

- **Pros:** gives a direct elementary interpretation of E waiting beside
  free A; retains own-lane priority as a regime limit and congested cooperation
  as another. It needs no extra continuous state, spatial cells or gap phase.
  It can expose slow E entry to the selected recovery mechanism while retaining
  a route to A delay through the shared account.
- **Cons:** protecting free A is a substantive approximation. Natural forced
  yielding may slow A before a sustained A queue exists. Switching priority
  at queue activation introduces event and hysteresis semantics; these still
  need complete-law qualification. Residual work is not a measured gap process.
- **Dependencies/consequences:** Type 2 G3 allocation choice, followed by
  exact transition/overlap proof and the same MP6 checks. It does not guarantee
  A eventually queues, an interior optimum or an information advantage.

### S-E-W: cooperative work sharing from the first conflict

Retain the proposed fair-work rule throughout. Each ready stream can use its
work share; unused work goes to the other. A may start waiting while E's
whole offered flow passes. If both wait, state-dependent admission costs
still determine their mass shares and total service.

The mental model is that through traffic can yield service immediately to
accommodate E. If that makes A pass slowly while E passes freely, later
recovery must examine A's actual passage. An E-only recovery calculation
would not cover that initial slow stream. This does not justify automatically
charging every queued A unit a second capacity penalty.

- **Pros:** one allocation principle across regimes; permits immediate
  cooperative yielding and avoids a special protection rule for free A.
  It is a serious simple rival, with feasible conservative fixed-regime
  flows. E need not be forced to slow in every traffic state.
- **Cons:** equal division of work is still a behavioral assumption. In
  the joined example it transfers the initial delay to A, so it cannot use
  an E-only slowing narrative to explain that event. The source evidence
  for congested sharing does not establish the same rule for free approaches.
- **Dependencies/consequences:** Type 2 G3 allocation choice; the account
  must qualify the resulting A/E recovery sources and attribution. Neither
  additional A loss nor an altered initial-information channel is approved.

**Subsequent user selection: S-E-P**, retaining S-E-W as an unselected
strong comparison. The priority-direction gate is closed; exact fairness,
work/speed and recovery law are not frozen. It is the smaller interpretation change from the existing
own-lane receiving logic while allowing both queued streams service. P keeps
that interpretation with the existing states; W has the simpler uniform
allocation rule. There is no empirical proof here that free A is always
protected. **S-E-P is selected at priority-direction scope.** S-E itself
remains selected; S-V stays an unselected return route.

## What this establishes for the remaining stack and MP6

| Question | Direct answer and core finding |
|---|---|
| **Can a compact S-E admission model be written?** | Yes. Existing waiting balances plus explicit admission/clearance guards and a qualified equilibrium boundary equation suffice for the local candidate. No extra queue geometry is needed. |
| **Does it remove the old arbitrary queue-birth ambiguity?** | It excludes that diagnostic's untriggered births. Fixed-regime uniqueness and strict local onsets are checked; whole coupled uniqueness remains open. |
| **What now controls the recovery account?** | The actual departures and their justified speeds. Allocation can make E or A the initially slow stream. The exact one-account recovery/overlap rule is still unfinished. |
| **Does it fit H1/T1 and MP6?** | The contrast occurs at a reachable H1 front, with ordinary underload and the retained all-action finite-storage bound. This is a local analytical admission result; complete-cohort causal clearance and applied MP6 still need the finished account and event law. |
| **What follows for information and gradients?** | No new positive certificate. A uniquely autonomous final law may preserve the ending-scalar reconstruction. State-dependent work and event timing must enter sensitivities; useful gradients and native validation remain unproved. |

The original admission/discharge → shared recovery → joined qualification
pass and Step 3 remain **in progress**. This bounded S-E review was delivered
at S-E-A2; the user then selected P and the continuation now stops at SEP-R1.
The old PDF is preserved as the pre-selection evidence record. No recovery law, A penalty, fairness coefficient,
parameter set, demand amendment or numerical regularization is adopted.
The local objective, S-P→S-L ladder, stronger aggregate/history/scalar/search
rivals, closed S13 certificate and closed ramp line retain their meanings.

[Mathematical candidate, unique-regime proof and exact H1 comparison](../../synthesis/research_readiness/vsl_se_admission_and_transition_audit.pdf)

[References actually inspected, source support and adaptation limits](../../extraction/research_readiness/vsl_se_admission_source_and_adaptation_audit.md)

[Work, changes and verification](vsl_se_admission_work_report.md)
