# RM9-R1 findings and concrete observation-contract gate

Date: 2026-10-05. Status: **Historical R1 proposal; UG4-O subsequently closed with C approved.**
The user selected C and authorized continuation. The dated
[approval](../discussion/rm9_observer_c_approval_and_continuation.md) and
[current findings/UG5](rm9_70_observer_c_findings_and_disposition_gate.md)
supersede pending-choice and next-action wording below. Candidate descriptions
are preserved for decision provenance; A/P were not adopted.
R2 and extensions have not been executed. This is a continuation of RM9.
Observer Candidate C here is distinct from the deferred multi-ramp task
Candidate C; no multi-ramp branch is opened.
For the plain-language decision, read the
[brief semantic comparison](../synthesis/rm9/rm9_r1_observer_semantic_comparison.md).

## What R1 established

Physical passage, section and space-time means are distinct legitimate speed
metrics. The current two-lane CTM supplies inventory and accepted boundary
flows, but not a uniquely justified physical passage-speed realization in
congestion. FB0030's detector-calibrated density is not the exact independent
cell inventory admitted to our strong comparison. The new estimation sources
also need initialization/trajectory assumptions and do not validate a
lane-changing-CTM observer by themselves.

This is a concrete G1 contract issue, not a requirement for simulator execution
or proof that every aggregate method fails. Detailed sources and the channel/
task matrix are in the [source audit](../extraction/rm9_r1_measurement_source_audit.md).
Definitions and causal indexing are in the
[mathematical handout](../synthesis/rm9/rm9_r1_observation_contract_audit.pdf)
and [TeX](../synthesis/rm9/rm9_r1_observation_contract_audit.tex).

## Proposed common information and timing contract

All choices below retain the strong information comparison and G0/G2 dynamics:

- Exact road-total mass for every declared mainline CTM cell, without per-lane
  output; full admitted history from a common stated initialization epoch.
- Actual aggregate face counts/flows over every declared completed interval;
  label mainline donor passage, ramp entry and downstream combined passage.
  Use the same declared sections/faces in both comparisons; do not omit an
  informative station to produce a collision.
- Current stored-state observations occur after the preceding step is completed
  and before the next lateral/forward update. Historical step face flows occur
  after that step's lateral transfer. No future action-dependent flow is known
  when the common open-loop action schedule is selected.
- Public geometry, FD/lateral/priority parameters, lane boundary allocation
  rules, common demands/forcing and all previous meter permissions. Full initial
  lane state is not secretly changed if it is declared known. If only initial
  aggregate information is admitted, latent alternatives must match all those
  initial observations and every subsequent historical channel.
- Ramp waiting/storage, actual meter release, post-meter storage where present
  and actual merge entry are separately accounted for. A meter permission cannot
  be equated with downstream entry across an intervening storage region.

These are proposed concrete transcriptions, not an adopted observer. Exact
site layout and boundary allocation remain to be tied to a source-grounded
task before any feasible G3 certificate. A declared finite cell layout is
required; numerical cell counts are not a new scientific gate by themselves.
No hidden ramp mass, added lane, mixing law or dynamics is introduced here.

## RM9-UG4-O — which concrete speed observation should bind the first task audit?

**Classification / owner:** Type 2, user adopts G1; source extraction and
conditional identities are reviewer evidence. Dependencies: inherited G0,
approved G2 and the R1 source matrix. G3/G4 depend on closure.

**Problem statement:** Select the speed statistic and state-to-measurement
assumptions for the first exact aggregate-history test.

**Assumed model-chain function:** The chosen mass/flow/speed/history channels
determine the information available before a common future rate schedule.
Existing conservative CTM dynamics then determine all-stream departure/time
outcomes. The observation function neither adds an actuator nor alters G2.

**Core gap:** Road-total mean speed was retained but not given a fixed physical
support. The earlier upstream-cell-to-face passage approximation remains
unverified in congestion. Source-first review now exposes a materially distinct
section-average choice. Picking either changes the information contract; the
reviewer cannot silently substitute them or select by favorable hiddenness.

Semantic clarification: C and A average different populations (traffic present
versus traffic passing), rather than apply different discounts. Both use a
representative FD speed hypothesis; A additionally maps cell speed to crossing
speed. P is a grounding route for A's passage target, not a third averaging rule.
Different weighting changes information support without amending G2 traffic laws;
neither observer has automatic information superiority over all branches.

### Candidate C — section-aligned first-order speed benchmark (new; recommended)

At each stored-state epoch, observe true cell total and the mass-weighted
longitudinal mean speed of traffic present in that same cell. Assign each lane
one representative equilibrium speed from its existing FD and current density.
Aggregate those speeds with lane mass weights internally; expose only the
road-total result. Retain completed accepted face flows as separate observations.
Do not calculate the speed as accepted face flow divided by current total
density. Empty cells have an unavailable-speed flag; occupied stopped cells can
have zero speed, independently of whether anyone crosses a face.

**Pros:** The section support matches the idealized true cell inventory. It
avoids identifying cell speed with a physical crossing speed. It adds no dynamic
state, lane or traffic-law amendment. The statistic is defined independently
of the accepted face-flow channel and retains a concrete road-total speed mean.

**Cons:** Exact section-wide observation and within-cell equilibrium speed are
idealizations; they are not validated physical detector data. The statistic can
reveal lane contrast even when face flow is receiving-limited. It is not the
earlier passage statistic and does not prove that all possible speed information
has been supplied. First-order internal shocks/acceleration are outside this
representative-speed closure.

**Dependencies/scientific consequence:** Adopt as a conditional first-order
G1 benchmark, explicitly recording its support change relative to the earlier
unapproved passage proposal. Do not reinterpret a claim about this observer as
a detector-field result. The existing free-flow post-lateral proof remains
historical; the new current-state speed consequences must be indexed separately.
If actual point passage speed is an indispensable task requirement, C cannot
replace it; choose P instead. C is recommended for support consistency and fewer
extra approximations, not because it creates a positive information result.

### Candidate A — retain the idealized passage benchmark (historical UG4.A)

For each completed interval/face, average the upstream post-lateral lane FD
speeds using actual accepted lane passage weights. Keep true cell totals,
counts, complete history and ramp balances as above. Explicitly declare one
representative speed per lane plus the upstream-cell-to-face approximation.
With zero face passage, that speed observation is unavailable; neither stopped
cell traffic nor zero counts fabricate a passage-speed sample.

**Pros:** Preserves the previously proposed metric and free-flow diagnostic.
Flow-weighted passage means have an operational measurement interpretation.
No additional state or revised traffic dynamics is required for a conditional
mathematical benchmark.

**Cons:** It adds the cell-to-face approximation to the equilibrium closure.
Physical crossing speeds in congestion need not equal upstream FD cell speeds.
Source-first review does not validate that equality; any result remains more
strongly qualified than a physically realized detector comparison.

**Dependencies/scientific consequence:** User must explicitly accept this
observation hypothesis and support/stage conventions before R2. Preserve
physical transfer limits and revisit G1 if the approximation is decisive.
This is the old observer A, not an undoing of the accepted source-first route B.

### Candidate P — require physical passage realization before the information test

Retain passage speed as the desired observation, but defer exact hidden-history
testing until a defensible physical/spatial mapping is available. Undertake a
bounded analytic reconstruction/model review, including internal queues and
initialization, before admitting any trajectory or extra speed law. Retain true
cell totals and the complete strong information contract; do not replace them
with detector-derived estimates or use noise/sparse sampling to force ambiguity.

**Pros:** Strongest viable option when detector-level traffic claims are the
primary objective. It directly confronts the missing mapping and can expose
necessary physical extensions rather than assume them away.

**Cons:** Source definitions alone do not supply this mapping for the current
adapted lateral CTM. The inspected multilane estimator excludes lane changes;
using it would require additional assumptions. This option may remain unresolved
or lead to a larger physical-model review instead of an immediate R2 result.

**Dependencies/scientific consequence:** Keep G1 open; present any additional
law/state change at its own smallest gate. Neither simulator execution nor a
trajectory/microscopic model is approved by choosing this review direction.

**Provisional recommendation: C.** For the first methodology-only, first-order
task audit, it defines a legitimate section speed using existing state and
removes the extra passage-location approximation. It openly retains equilibrium
and exact-observation idealizations. If physical point-detector fidelity is
required now, P is the appropriate alternative. A remains a viable deliberately
qualified benchmark. No candidate is adopted by the source-first approval.

## Result, remaining work and next allowed action

R1 delivered source-backed metric distinctions, an evidence/task matrix,
causal/history/ramp accounting requirements and a concrete observer proposal.
It has reached its planned user gate; G1 is not yet frozen, nor is a field speed
map established. G2/UG1–UG3 remain unchanged. There is no G3 matched-history/
useful-action certificate or G4 numerical/independent usefulness evidence.

Next: discuss C/A/P at UG4-O. Once the selected contract and necessary geometry/
initialization transcription are coherent, proceed under the accepted flow to
R2. R3 amendments and R5 extensions are not automatically admitted. See the
[work report](rm9_98_r1_work_report.md). No SUMO, production, traffic experiment,
numeric gradient test, deferred VSL continuation or successor stage was opened.
