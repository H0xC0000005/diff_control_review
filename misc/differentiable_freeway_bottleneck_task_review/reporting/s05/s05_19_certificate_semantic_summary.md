# S05.19 — Certificate analysis in plain language

Sprint: [S05](../../00_review_sequence.md#s05) · Role: 19 short reading companion · Gate: DG-AC1, still pending.

## What are we trying to establish?

At a road narrowing from three lanes to two, does knowing **which lanes contain
the traffic** help choose a better speed recommendation shared by all lanes?
We must compare against a strong simpler model that already knows traffic
amount, average speed and their spatial/history records—not a deliberately
forgetful model.

## What did the analysis establish?

**Lane information can be hidden.** In a simplified free-flow model where every
lane travels at the same speed, cars changing lanes do not change the total
traffic amount. Different lane allocations can therefore look identical in the
full aggregate history. We established this conditionally for an early traffic
preparation, not for the actual near-narrowing reference case.

**Hidden information is not automatically useful.** Suppose the narrowing lets
traffic through at a fixed rate, unaffected by advice. If lower advice only
delays arrivals, it cannot improve total travel time: it merely moves waiting
upstream or adds travel delay. In that simplified case, the highest allowed
advice remains a common best choice, even if hidden configurations have different
fixed discharge capacities.

## What is the actual missing link?

Slowing must improve something about the traffic interaction—for example,
making merging less disruptive or helping traffic use the continuing lanes—
enough to outweigh its delay. These are possibilities, not established results.
We still need a case where the same strong aggregate history hides different
lane configurations **and those configurations genuinely need different useful
common advice**. The analysis neither proves nor rules out such a case.

One practical caution: the planned short speed pulses omit holding advice at
100km/h. Different preferred pulses would not establish an unavoidable decision
problem if this untested common alternative worked well in both configurations.
Testing it is proposed, not approved or assumed beneficial.

**Bottom line:** possible information loss is clearer; useful control value is
still unproved. No richer lane model, minimum retained state or useful gradient
has yet been justified. This companion simplifies the explanation, not the
evidence standard or pending decision.

Details: [findings and gate](s05_20_rb_certificate_findings_and_gate.md),
[formal analysis](../../synthesis/s05/rb_certificate_analysis.pdf).

Preparation record: reread S05 findings and the reading guide; used apply_patch
to add this formula-free companion and navigation links. No scientific contract,
gate status, archived source, experiment setting or code changed. Document-link
checks apply; traffic/gradient tests do not. Next allowed action remains user
review of DG-AC1, not execution of a new sprint.
