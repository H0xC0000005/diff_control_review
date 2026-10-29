# Fixed merge weights work; the remaining question is access to a donor's spare sending

**Subsequent decision, 2026-10-09:** D2 explicitly approved and dependent
static boundary/whole-contract continuation performed. The current gate
is Q.J.F.R, the ordinary field carried into the next timestep. Earlier
D1/D2 proposals and certificates below retain their original evidence
scope; they are not an open sender choice.

[Current findings and field decision](d2_forward/findings_and_field_gate.md)


Date: 2026-10-08. **P.A is user-approved and its dependent review has proceeded.**
Queue growth does not increase a stream's priority inside the regular step.
Physical availability, receiving and already fulfilled requests can still
change actual service. The ramp's geometric share remains fixed; mainline
request weights refresh at the next original regular request clock. This
approval does not replace them with permanent geometric weights across steps.

There is a constructive positive. One joint traffic example now includes two
constrained receiving lanes, a through allowance used up before the clock,
the queue waves after that stop, a restriction crossing a section boundary,
and two new effects attached to the completed state. Its traffic, motion,
count labels and actual transfers all agree. This is a complete local
one-step certificate, not the whole task's forward/gradient qualification.

The review also exposes a different question. **Merge priority decides which
incoming stream gets receiving space. It does not, by itself, decide how one
donor's available sending is shared between its own two exits.** We should
settle that before adopting a general port update.

## What your approval means

Think of a merge with a fixed allocation arrangement. A growing queue can
make traffic ready at the entrance; it does not press harder on that arrangement
and earn extra priority. When a stream cannot use its share, unused receiving
can still go to another eligible stream. These are availability changes,
not queue-length priority bonuses.

P.A preserves the sampled request ratios as competition weights for the
current timestep. N.A's fixed ramp share, unused-share transfer and one common
receiving resource remain approved. T.A still limits integrated movement mass
without a held nominal request-rate ceiling. No PID, queue-responsive priority
or new geometric parameter is introduced.

## What the joint example achieves

A donor wants to send both through and lane-changing traffic. Its through
recipient has a slow effect and can accept 0.20 equivalents/s. Its lane-change
recipient has another effect; after the ramp receives its fixed share,
0.20 equivalents/s remains for two mainline requests. The sampled weights
award about 0.178 to the mainline through request and 0.022 to lane changing.

That branching donor's through allowance is only 0.075 equivalents, so it is used
up after 0.375 s. Through service then stops even though traffic remains on
the donor. Its lane-changing request keeps its original weight. A backward
queue wave catches the donor's moving rear, with no lost or reassigned mass.

The old effect in the through recipient reaches its section edge at 0.55 s.
It enters the next section and is relabeled in that section's own count
coordinates. Following traffic crosses with it at the receiving allowed by
its own queue. The record carries no extra population. A separate release
wave in the finite, closed-meter ramp also interacts with its discharge queue.

At the regular clock, the accepted ramp and lane-change counters each create
one effect at the lane-change recipient's entrance. They share the completed
count label, retain their distinct metadata, and add no traffic mass. Both
start by respecting the traffic already ahead. Total ending mass equals
initial mass plus the only external inflow exactly.

This demonstrates composition of the approved mechanisms on specified
fields and history inputs. It does not establish a reached metering policy,
clearance, full-horizon TST response or useful gradients. The one-step total
inventory alone cannot demonstrate controller benefit, since no traffic exits
the whole diagnostic domain during this step.

## The next question, in traffic terms

Suppose through movement is blocked, but lane changing is allowed. The donor
has unused ability to send and a still-unspent lane-change allowance.

- Should the original quarter lane-choice fraction also restrict lane-changing
  discharge to a quarter of the donor's sending capability?
- Or may the surviving request use the donor's available sending capability,
  stopping when its already approved mass allowance is used up?

Neither alternative gives a queue higher merge priority. Neither creates more
lane-changing demand or retries the sampled choice. They differ in the
**timing** of service for the same allowed movement mass.

A late-arrival example makes the consequence visible. Consider one 1-second
step with 0.45 equivalents initially on the donor. Its original 25% lane-choice
fraction allows **0.1125 equivalents of lane changing in total**. Traffic only
reaches the exit at 0.9 s, so discharge has just **0.1 s**. Through receiving is
blocked; lateral receiving is ample. The donor's physical sending capacity is
about **0.643 equivalents/s**.

- **D1 reserves a rate fraction:** lane changing is capped at 25% of that
  capacity, about 0.161 equivalents/s. In 0.1 s it serves **0.0161 equivalents**.
  The unusable through fraction does not increase that cap.
- **D2 pools physical sending:** the still-active lane-change request can use
  the full 0.643 equivalents/s until its original amount allowance is spent.
  In 0.1 s it serves **0.0643 equivalents**. It borrows unused sending capability,
  without borrowing the through movement's mass allowance.

Both results are below the same 0.1125-equivalent allowance. The question is
whether the original 25% also limits **instantaneous rate**, not whether more
traffic should be assigned to change lane. With an existing accepted-entry
counter of 0.94, D1 ends near 0.956 while D2 ends near 1.004. Only D2 crosses the
next E1 threshold and creates a new effect record at the regular update; that
record adds no traffic population. This shows different forward laws, not
evidence that either option produces better control.

[One-page explanation with short calculations](../../../synthesis/rm12/bp_r_stage3/donor_capacity_example_brief.pdf)

## Q.J.F.D — donor sending after competing exits become unusable

**Problem statement — Type 2 / user.** Does the original sampled choice
fraction also bound instantaneous oriented sending on the richer field, or
does it define the integrated mass allowance and competition weight only?

**Assumed model-chain function.** A shared sender must supply all its exits
without spending its physically available traffic twice. The accepted port
flows then update lane fields, exhaust movement allowances and feed E1.
P.A already governs receiving competition; D completes the sender-side meaning.

**Core gap.** The original finite-step IT recipe partitions desired advancing
mass. Its saturated sampled formula also has an oriented-rate form. That
formula alone does not prove that this becomes a physical per-movement rate
ceiling inside a nonuniform causal field. T.A rejected a held sampled rate,
but did not select every multi-exit availability rule. P.A fixes competition
weights, not this remaining cap. Earlier local P.A examples used a declared
source-oriented completion; that example was not approval of a general rule.

### D1 — retain source-oriented instantaneous capacity

While a movement is active, cap its potential service at the original choice
fraction times the donor's capacity, alongside shared physical sending,
receiving and the integrated allowance. Fulfilled/blocked exits are not
renormalized to give their orientation to another exit. Fixed original weights
allocate competition and qualified capped redistribution.

In plain language, D1 treats the sampled fraction as a persistent limit on
how quickly a movement can be performed, as well as how much mass requests
it. Blocking through movement need not make lane changing faster. This is
defensible if lane changing has its own rate restriction that the sampled
fraction represents. The source's direction-specific sampled sending recipe
explains why this is a candidate; it does not establish that interpretation
for our richer traffic field. A fraction describing how many want to change
lane does not, by itself, prove the same fraction of capacity is usable.
No additional gap-acceptance, lane-order or execution law is adopted here.

**Pros:** retains the source's disaggregated sending form and earlier local
wave-kernel lineage. Gives a clear directional service ceiling without a new
calibrated parameter. Exact early-stop and late-arrival fields exist.

**Cons:** adds an instantaneous movement restriction beyond its total mass
allowance; useful donor sending can remain idle with an active request.
The coarse source formula is evidence for this transcription, not independent
proof of a physical lane-change-capacity law in our richer field.
Thus D1 is a consistent declared candidate with a remaining physical
justification obligation, rather than an established necessary restriction.

**Dependencies/consequences:** retain this declared cap in the full node/wave
completion, including depleted modes. It is different from the rejected held
nominal rate based on sampled mass divided by the regular timestep.

### D2 — pool physical donor sending among its active mass requests

Keep every original movement allowance and weight. Allow active exits to use
the common physically available sending, subject to receiving and the donor's
joint sending limit. Do not impose an extra fraction-times-capacity ceiling.
Unused ability to send can be used by a surviving request without enlarging
its allowed mass. Reallocate only among still-active original requests.

**Pros:** follows T.A's amount-first meaning and avoids an additional
instantaneous restriction. The derived static allocator bounds total donor
service and total receiving jointly; early-stop and late-arrival fields exist.

**Cons:** changes interior service timing from the source-oriented completion;
transfers can become more concentrated. Source-native finite IT is not thereby
proved temporally equivalent, and full joined qualification must use this
explicit adaptation rather than the older constant-flow certificate.

**Dependencies/consequences:** qualify the chosen shared-node/wave completion
with original quotas, atomic exhaustion and E1. No new lane choice, FIFO rule,
rate-control variable, geometric parameter or early birth is authorized.

**Provisional recommendation: D2.** Your amount-first approval favors using
physically available sending without adding another limit whose physical
necessity is unestablished. D1 remains a viable source-oriented transcription,
not a refuted traffic model. This separate decision is about one sender's
capacity; the approved P.A merge priorities are not reopened.

## Evidence, limits and next allowed work

Primary source reading distinguishes interval movement amounts, node
priorities and exact boundary-wave consistency. We derive two finite static
port constructions with joint donor/recipient constraints and simultaneous
ties; their allocation parameter is not elapsed traffic time. They are
reviewer constructions, not imported generic FIFO or throughput theorems.
The joint local field example and both donor diagnostics are exact analytical
certificates. Numerical checks evaluate their formulas, not traffic rollouts.

[Source movement recipe](https://doi.org/10.1016/j.trb.2005.04.003)

[Fixed-priority node family and its scope](https://arxiv.org/pdf/1601.01054)

[Boundary-wave framework and its distinct FIFO theorem](https://arxiv.org/pdf/1204.6727)

P.A and T.A are closed. Stop at D before selecting a general sender completion.
After D, qualify remaining encounter/coincidence/node-crossing modes and
repeated reset under that selected common field, then return at full Q/J.F
adoption. The present joint example does not prove all those modes. A1/A2/C
field realizations remain unselected; Stage 3/67 open; Stage 4 unopened.

[Mathematical explanation and exact joint example](../../../synthesis/rm12/bp_r_stage3/fixed_share_completion_math.pdf)

[Technical qualification and question ownership](../../../synthesis/rm12/bp_r_stage3/fixed_share_completion_qualification.md)

[Primary source audit](../../../extraction/rm12/bp_r_stage3/fixed_share_completion_source_audit.md)

[Analytical and document checks](fixed_share_completion_execution_validation.json)
