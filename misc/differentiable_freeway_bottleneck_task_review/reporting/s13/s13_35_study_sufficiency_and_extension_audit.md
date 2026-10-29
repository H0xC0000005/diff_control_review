# S13.35 — Study sufficiency and extension audit

Date: 2026-10-01. Status: **audit complete; M2C-A subsequently accepted and S13 closed.**
Parent: [S13 certificate findings and gate](s13_20_m2_certificate_findings_and_gate.md).

## Audit question and boundary

This audit asks whether the elementary S13 task, together with defensible
variants and extensions, can become a study that answers the core freeway
review questions. It does not reopen the approved S13 equations, add an
experiment, or treat model complexity as scientific value by itself.

The audit distinguishes three burdens:

1. a conditional mechanism-existence certificate;
2. a theoretical model-family and minimum-information study; and
3. an empirical gradient-usefulness study for traffic control.

These burdens require different evidence. Passing the first does not pass the
other two.

## Executive verdict

**S13 alone is not a complete study of representation necessity or externally
useful gradients.** It is a complete conditional existence certificate and a
strong study kernel.

**S13 plus a bounded ablation, compression and robustness program can form a
coherent theoretical study.** Such a study can answer which mechanism is needed,
when hidden lane preparation changes a common VSL decision, and how much state
the analytical family actually requires.

**It still cannot establish traffic-valid gradient usefulness without an
independent richer evaluator or empirical evidence.** That is a later evidence
layer, not something that additional algebra or parameter sweeps can supply.

The key finding is that the elementary S13 model compresses all consequential
lane detail into the scalar remaining mandatory-merge mass. This is scientifically
useful but limits the claim. S13 currently supports the value of one omitted
merge-pressure statistic; it does not prove that a complete per-lane state, lane
order, gaps or discrete vehicle identity is necessary.

## Core-question audit

| Core question | What S13 establishes | What a study still needs | Audit verdict |
|---|---|---|---|
| What macro-hidden information can alter control? | Ending-lane fraction, equivalently remaining mandatory-merge mass, can be hidden under the declared aggregate history and can change finite-receiving workload. | Test whether this scalar is sufficient across variants, whether a smaller observable closure exists, and whether richer lane state adds anything after the scalar is supplied. | Conditionally answered; minimum representation unresolved. |
| Can it alter the controller result? | Yes in a nonempty open parameter regime: the paired states have disjoint unique optimal actions over the complete bounded common-VSL family. | Show the distinction is not peculiar to constant-rate exponential transfer, proportional batch service or one objective convention. | Strong analytical answer for one member; family robustness unresolved. |
| Can it provide relevant gradient information? | Yes conceptually inside the fixed active regime: hidden state can reverse the locally useful analytical direction at fastest advice. | Separate model derivative correctness from independent outcome usefulness; inspect active-set boundaries and evaluate perturbations in a richer reference if an applied claim is wanted. | Analytical relevance answered; implementation and external usefulness unanswered. |
| Is the task formulated? | Yes as a complete analytical task with observer, action, hidden state, service, accounting and falsification conditions. | An executable applied study would additionally need scenario generation, parameter provenance, baselines, held-out cases, derivative checks and a reference evaluator. | Complete for theory; incomplete for empirical evaluation. |

## Why the current task risks being too elementary

### 1. The desired result is built from one compact causal chain

The certificate intentionally isolates common speed, residence time, remaining
merge demand and finite receiving. That makes the proof inspectable, but a
single positive construction can be criticized as a consequence of its chosen
closure unless neighboring closures are classified.

The remedy is not a larger simulator by default. It is to establish which
properties of the transfer and service laws are sufficient for the result and
which deletions recover the S05 obstruction.

### 2. Full lane resolution is not needed by the current equations

Once the decision boundary is reached, the objective uses total cohort mass and
remaining merge mass. The two continuing lanes are already symmetric and
aggregated. A macro model augmented with the exact remaining-merge statistic can
reproduce the S13 state and action ranking.

This does not invalidate hidden-information value. It changes the representation
claim from “per-lane state is necessary” to “the declared aggregate observer is
missing at least one consequential statistic.” A serious minimum-information
study must include this compressed model rather than compare only a weak macro
model with a richer lane model.

### 3. The service objective depends on the proportional batch closure

Total receiving work is meaningful across work-conserving rules, but mean
completion time can depend on which class is served first. The current linear
departure and half-clearance-time expression follows the proportional
co-clearance assumption. Continuing-lane-first, merge-first and transient
receiving rules can change mean delay even when total work and final clearance
time agree.

A study must either retain the proportional rule as an explicit conditional
claim, use an objective whose value is priority-invariant, or include a small
priority robustness classification. It should not silently imply that every
finite-receiving rule produces the same result.

### 4. The exact observer collision is inherited conditionally

S13 cleanly separates predecision information from postdecision M2 dynamics,
but its collision relies on the S05 homogeneous preparation. A theoretical
study can retain this as an explicit construction. An applied study would need
to demonstrate reachable matched preparations in the selected reference model
or weaken the claim through a separately approved approximate-matching design.

### 5. Parameter openness is not traffic prevalence

Strict inequalities show that the result is not one isolated favorable point.
They do not show that realistic traffic commonly occupies the regime. More
parameter sweeps within uncalibrated bounds improve phase classification but do
not establish prevalence or field validity.

## Minimum extension set for a theoretical study

The following four work packages are jointly sufficient for a bounded
model-family study. They are not authorized for execution by this audit.

### A. Mechanism deletion and limiting ablations

Use the same observer, action family and complete accounting while removing one
causal link at a time:

- no action-sensitive transfer opportunity;
- no extra merge receiving work;
- nonbinding choke receiving;
- no hidden ending-lane contrast; and
- fixed advice-independent service as the S05 recovery case.

These ablations establish that the positive result needs the joined
action–transfer–receiving chain rather than lane labels alone. Omitting complete
accounting should be shown only as a biased-objective diagnostic, not as a valid
competing model.

### B. Transfer and service robustness

Replace the exponential with a small preregistered family sharing clear traffic
semantics, such as constant fractional transfer, a bounded finite-completion law,
and a receiving-limited saturating law. Classify results by the marginal
preparation benefit rather than demanding one action split for every admissible
law.

Likewise compare the approved proportional service with at least one alternative
priority or use a priority-invariant completion objective. The aim is to expose
which qualitative conditions produce fastest, interior or slowest optima—not to
tune every closure until it agrees.

### C. Representation and compression ladder

Use nested information models under the same physics and objective:

1. declared strong aggregate history only;
2. aggregate history plus one merge-pressure or remaining-merge statistic;
3. ending-lane versus continuing-lane grouped state; and
4. fuller per-lane state only if it predicts something not recoverable from the
   compressed statistic.

The principal outcome may legitimately be that one continuous scalar is enough
for this task. Richer state earns a claim only when a matched case defeats the
compressed closure. This ladder directly answers “how much information” more
strongly than a macro-versus-lane binary comparison.

### D. Decision and analytical-gradient phase classification

Map the predeclared parameter and model-form regions in which the common optimum
is fastest, interior, slowest or state-dependent. Within smooth regions, report
the analytical sensitivity and its state dependence; identify action endpoints,
receiving switches and priority switches as boundaries.

This supplies a model-family result and prevents the positive open regime from
being presented as universal. It also makes negative and aggregate-sufficient
regions part of the contribution.

## Additional requirements for an applied gradient-usefulness study

A traffic-control study making an external usefulness claim would need a later,
separately approved layer:

- a source-supported or calibrated transfer/receiving response rather than an
  unconstrained constant-rate branch;
- reachable matched or carefully controlled preparations in a richer evaluator;
- a fair ladder containing strong aggregate, scalar-augmented and lane-resolved
  candidates;
- implementation-level double-precision derivative checks away from declared
  active-set boundaries;
- evaluation of small control perturbations in the independent richer evaluator,
  including whether the predicted direction improves complete delay; and
- held-out demand, hidden-state and parameter regimes with all traffic accounted
  through clearance.

SUMO is one possible richer evaluator, not a methodological prerequisite for the
theoretical study. Static analysis cannot replace this layer if the claim is
that gradients are useful for realistic traffic rather than useful inside the
analytical model.

## What would not make the study sufficient

- Sweeping many values of the same uncalibrated exponential model without
  changing or ablating its structural assumptions.
- Comparing only the declared aggregate observer with full lane state while
  omitting the exact scalar statistic used by the equations.
- Treating finite analytical gradients as evidence of external gradient
  usefulness.
- Selecting a service priority, action interval or parameter region after
  observing which one yields a positive split.
- Claiming literature-wide novelty or empirical necessity from the bounded
  source audit.

## Study forms and attainable claims

| Study form | Required content | Defensible final claim |
|---|---|---|
| Current S13 certificate | Existing contract and proof | A conservative source-bounded M2 member can make hidden merge preparation decision- and gradient-relevant. |
| Extended theoretical study | A–D above | Qualitative conditions and minimum retained statistic needed for information-dependent common-VSL decisions in the declared analytical family. |
| Applied methodology study | A–D plus independent-evaluator requirements | Whether the retained statistic/model improves derivative direction and downstream control outcomes in the tested traffic domain. |

## Recommended disposition

Accepting M2C-A remains methodologically sound because S13 achieved its approved
certificate burden. That acceptance should describe S13 as the analytical
kernel, not the completed representation/gradient-usefulness study.

If the intended deliverable is a full theoretical study, close S13 on its
conditional result and separately plan the bounded A–D extension. Do not replace
that plan with the existing Candidate B's unrestricted family-wide burden; the
right target is classification across a small preregistered family, including
negative regions and compressed-state sufficiency.

If the intended deliverable includes realistic traffic-gradient usefulness,
the theoretical extension is still only an intermediate stage. A later
independent-evaluator protocol is indispensable. No such successor is opened by
this audit.

## Evidence basis and unresolved risks

This audit uses the S05 obstruction, S10 claim–evidence matrix, S12 source-family
admission and S13 contract/certificate. The reviewed literature supports the
mechanism pieces but not one jointly calibrated common-VSL exponential-transfer
and finite-receiving model. The source review is bounded and does not establish
global novelty or absence.

The principal unresolved risks are model-form dependence, priority-sensitive
mean delay, conditional reachability of the exact observer collision, lack of
traffic-calibrated parameter prevalence, lack of implementation derivative
evidence, and lack of independent gradient/outcome transfer.
