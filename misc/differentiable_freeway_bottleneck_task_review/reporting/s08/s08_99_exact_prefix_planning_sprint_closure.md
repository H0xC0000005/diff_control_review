# S08.99 — Exact-prefix planning closure and execution handoff

Date: 2026-09-29. Status: **Closed by explicit user approval of DG-R5
Candidate A.**

## Accepted outcome

The exact-prefix feasibility screen will use the full dual-step bank. All 18
frozen preparations must be evaluated at both 0.5 s and 0.25 s before pair
selection. Qualifying pairs are intersected across both steps and at most two are
selected by the frozen contrast/lexical rule. The staged 0.5 s discovery filter
is not selected.

Methodological soundness and feasibility govern this choice. The 14-instance
difference between the full and staged banks is constant-factor operational cost,
not an algorithmic-complexity change. The approved scientific bank therefore has
36 prefix invocations, with the separately bounded readiness allowance bringing
the maximum to 60.

## Next review step

The next bounded continuation is an exact-prefix readiness and execution sprint.
It must proceed in this order:

1. perform read-only provider/version discovery and report absence or
   incompatibility without installing or reconfiguring anything;
2. implement only the repository-owned prefix/readiness/summarize harness needed
   by the approved contract;
3. use at most 24 readiness invocations to verify connections, lane permissions,
   entry and source-delay semantics, native behavior, deterministic replay,
   canonical observation coverage and serialization;
4. if readiness passes, execute all 18 prefixes at both frozen time steps;
5. produce the complete within-time pair registry, intersect qualifying pairs
   across steps and select at most two without consulting action outcomes; and
6. stop at a user gate with the evidence and failure label.

The possible stop results are: qualifying dual-step exact pair; primary-step
pair not robust at 0.25 s; no exact-history pair; exact pair with zero lane
contrast; invalid provider/harness/reference result; or incomplete execution.

## Boundary

Candidate A approval freezes the method but does not itself authorize provider
inspection, harness implementation or traffic invocations. Those require an
explicit instruction to open and execute the next sprint. Installation,
configuration changes, advice-action evaluation, broader S07 preparations,
approximate matching, held-out contexts, candidate simulator construction and
gradient work remain outside.

**Subsequent status:** the user explicitly opened S09 through its next gate.
Read-only provider discovery found no usable local SUMO provider, so S09 stopped
at [DG-R6](../s09/s09_20_exact_prefix_readiness_findings_and_gate.md) before harness or
traffic execution.

The user then reaffirmed that the review is methodology-only. The empirical S09
interpretation and DG-R6 provisioning gate are superseded by the [scope
correction](../s09/s09_35_scope_correction_and_methodology_alternatives.md). This S08
contract remains a future empirical protocol, not current execution authority.
