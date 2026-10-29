# S13.20 — M2 analytical-certificate findings and user gate

Date: 2026-09-30. Status: **Closed 2026-10-01; M2C-R1 Candidate A accepted.**
Parent: [approved S13 plan](../../s13_00_m2_analytical_contract_certificate_review.md).

Formula-bearing evidence:

- [M2 model contract](../../synthesis/s13/s13_m2_model_contract.pdf) and
  [LaTeX source](../../synthesis/s13/s13_m2_model_contract.tex);
- [certificate analysis](../../synthesis/s13/s13_m2_certificate_analysis.pdf)
  and [LaTeX source](../../synthesis/s13/s13_m2_certificate_analysis.tex); and
- [source-to-equation audit](../../extraction/s13_m2_source_to_equation_audit.md).

## Decision summary

Under the approved source-bounded analytical contract, M2 produces a complete
conditional information-to-decision chain. The provisional verdict is:

> **M2C-A — conditional decision-relevant certificate.**

The construction uses two preparations with the same declared strong aggregate
history and total cohort mass but different hidden ending-lane fractions. At the
decision boundary both enter the same fixed preparation zone. One common lane-
uniform VSL determines zone residence time. Conservative mandatory transfer
reduces ending-lane mass while the cohort traverses the zone. Mass still needing
to merge at the choke consumes additional finite receiving work.

This produces a real tradeoff under complete accounting: slower advice adds
travel time but can reduce receiving workload. Over a nonempty open parameter
regime, the low ending-lane state uniquely selects fastest advice, while the high
ending-lane state uniquely selects a slower interior action. The action sets are
disjoint, and any deterministic controller restricted to the identical aggregate
history has strictly positive worst-state regret.

## What changed relative to S05

S05's service process was fixed with respect to advice, so fastest arrivals
could not be made worse by complete accounting. S13 makes receiving workload
depend on how much mandatory transfer remains after an advice-dependent
preparation duration. Advice therefore changes service, not only arrivals. The
premise behind S05's common-fastest-action theorem is absent.

The result remains conservative: every lateral transfer removes and adds the
same mass, all affected mass clears, and the action-induced preparation delay is
fully counted.

## Results against the approved global contracts

| Contract | S13 result |
|---|---|
| G1-A neutral proportional finite receiving | Passed in a homogeneous fluid-batch active regime; alternative priorities remain outside the certificate. |
| G2-A common VSL through longitudinal speed | Passed: speed changes spatial-zone residence time; transfer desire is not directly controlled. |
| G3-A exact spatial handoff | Passed conditionally on the S05 aggregate-invariant preparation: the decision boundary is first entry to the fixed M2 zone. |
| G4-A open source-bounded parameter regime | Passed with strict inequality conditions; no nominal traffic calibration was selected. |
| G5-A full continuous action family | Passed: the fastest endpoint and a slower interior optimum are compared over the complete bounded interval. |
| G6-A observer identity plus aggregate countermodel | Passed at the decision point: identical histories force one deterministic observer-only action/prediction, which cannot be optimal for both hidden states. |
| G7-A conditional conceptual gradient | Passed within the fixed active regime: hidden state reverses the useful gradient direction at fastest advice. |

## Status of the core review questions

### 1. What hidden macro-omitted information can alter the controller result?

**Conditionally answered.** Ending-lane fraction is hidden under the inherited
exact aggregate-history construction. It determines how much mandatory transfer
remains at the choke and therefore the receiving workload under each action.

### 2. Can that information alter the controller result?

**Conditionally answered.** The two hidden states have different unique optimal
common VSL actions over the same continuous action family. The result survives
small parameter perturbations because its defining inequalities are strict.

### 3. Can it provide relevant gradient information?

**Conditionally answered at the conceptual analytical level.** The differentiable
path is common VSL → traversal time → remaining ending-lane mass → receiving
workload → complete delay. At fastest advice, the locally improving direction is
opposite in the two hidden states. No implementation-level automatic-
differentiation or finite-difference claim is made.

## Aggregate countermodel interpretation

The paired states present exactly the same declared history at the decision
point. Any deterministic aggregate controller or capacity-drop model using only
that history and the common future action must make the same initial choice and
prediction for both. It may fit one case, an average, or react after aggregate
postdecision observations diverge, but it cannot condition the initial action on
the hidden ending-lane fraction.

This establishes information value under the fixed observer and open-loop
decision contract. It does not rule out later feedback adaptation or an aggregate
model supplied with an additional statistic that effectively reveals lane
allocation.

## Evidence boundary and remaining gap

The decisive adaptation is a positive constant-rate mandatory-transfer branch
inside the preparation zone. It is a deterministic continuous-mass
specialization of source-supported repeated lateral transfer, but it is not a
calibrated VSL response law from one paper. The homogeneous batch handoff and
proportional choke service are likewise analytical reductions.

Accordingly, S13 establishes **methodological possibility and a complete
conditional chain**. It does not establish:

- that real or native-reference traffic occupies the certified parameter regime;
- that the constant transfer-rate closure predicts a field lane drop;
- that this ending-lane fraction is the minimum sufficient mesoscopic state;
- robustness to every receiving-priority or lane-change law;
- implementation-level derivative correctness; or
- empirical superiority over a calibrated aggregate controller.

These are model-validity, robustness and later evidence questions. They do not
invalidate the conditional certificate, but they limit its claim.

## S13-UG1 / M2C-R1 — certificate disposition

### Problem statement

Should S13 accept the completed conditional certificate as the review result,
extend the analytical burden across a broader receiving/transfer family, or
reject the source-to-equation adaptation as insufficient?

### Assumed model-chain function

The accepted result would state that hidden ending-lane allocation can change a
common VSL decision and its useful gradient direction within one conservative,
source-bounded continuous-mass M2 member. It would not claim field validity or
universal necessity.

### Core gap

The analytical chain is complete, but its action-to-transfer closure and
homogeneous proportional service are explicit adaptations rather than a jointly
validated source model. The user must decide whether a conditional methodology
certificate is the intended stopping level.

### Candidate A — accept M2C-A and close S13 (provisional recommendation)

Accept the conditional certificate with its stated source/adaptation and
empirical boundaries. Do not open ramp metering automatically because the
planned VSL branch produced a positive methodology result.

**Pros:** Directly answers the core questions at the approved analytical level,
includes the fastest action and complete accounting, preserves the strong
observer, and identifies an explicit useful gradient path. It records every new
assumption and falsification limit.

**Cons:** The result remains conditional on a simplified transfer/service member
and does not establish that the certified regime occurs in real traffic.

**Dependencies and consequences:** S13 closes positively. Any implementation,
cross-fidelity validation, robustness expansion or empirical source review must
be separately planned. Ramp metering remains available but is no longer the
automatic next step under the approved ordering.

### Candidate B — amend S13 for family-wide robustness

Reopen G1/G2/G4 and require the action distinction across multiple conservative
priority rules or a broader transfer-law family.

**Pros:** Reduces dependence on proportional service and the constant-rate
active branch. A robust result would support a wider methodological claim.

**Cons:** Changes the approved existence-certificate burden into a uniform-
family theorem. Aggregate and fixed-service limits guarantee that no useful
split can hold everywhere, so the new quantifier would need another decision.

**Dependencies and consequences:** Requires a new bounded amendment plan and
must define which family and robustness measure before further derivation.

### Candidate C — reject the adaptation and close as M2C-E

Treat the absence of one directly validated common-VSL/transfer/receiving source
model as disqualifying, despite the explicit source-bounded construction.

**Pros:** Applies a stricter evidence standard and avoids treating analytical
adaptation as traffic validity.

**Cons:** Rejects the methodology-level existence result for an empirical burden
that S13 explicitly excluded. It would erase a sound conditional deduction
rather than merely limit its interpretation.

**Dependencies and consequences:** Close the M2 branch as contract-unsupported;
the separately planned ramp-metering admission review becomes eligible again.

**Provisional recommendation: Candidate A.** It matches the approved S13 purpose
and keeps the distinction between conditional methodology evidence and empirical
validity explicit.

## Gate question

Select **M2C-R1 Candidate A, B or C**. No successor review starts automatically.

## Gate resolution

On 2026-10-01, the user accepted **Candidate A**. S13 closes with M2C-A;
extensions are assigned to further work. See the
[S13 closure](s13_99_m2_certificate_sprint_closure.md).
