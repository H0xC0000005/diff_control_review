# RM9 joint-flow readiness and continuation evidence

Date: 2026-10-01. Scope: primary methods/static mathematics; no traffic execution.

## Provenance and inspected locations

| Source | Access and location | Role / strict limitation |
|---|---|---|
| RM0018 Wright et al. 2017 | Existing 23-page author-hosted published PDF, printed 216–218, Section 3.1, equations 3.6/3.8/3.9, Remark 3.1 | Priorities/redistribution; two-input transcription derived below. No full MIMO/partial-FIFO scheme adopted. |
| FB0030 Nagalur Subraveti et al. | Existing 24-page final PDF, printed 1762–1766, equations 5–22 | Bounded predecessor attractiveness, fuller incentive/receiving/coupling diagnostics. Isolated range/branch checks do not certify or invalidate the complete calibrated algorithm. |
| FB0034 Roncoli et al. 2014 | Six-page primary IFAC proceedings PDF, printed 4179–4181, Sections 2–3 | Lane conservation and feasible-flow constraints; lateral/longitudinal/ramp flows are optimized controls, so not an autonomous meter-only closure. Existing ID reused. |
| RM0002 Schmitt et al. | Existing primary preprint, https://arxiv.org/pdf/1611.06766 | Conditional best-effort/monotonic CTM background; not a universal optimal-policy or hidden-lane result. |
| RM8-P01 Laval et al. merge theory | Existing primary author-hosted PDF, https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/f/3571/files/2023/03/merges.pdf | Acceleration/merge mechanism background, not a first-order closed-law or gradient certificate. |
| RM9-L01 Roncoli et al. 2015 Part I | Primary publisher/author-institution metadata only; DOI 10.1016/j.trc.2015.06.014; https://research.aalto.fi/en/publications/traffic-flow-optimisation-in-presence-of-vehicle-automation-and-c-2/ | **Lead only, no full-method admission.** Lane CTM and capacity drop described in abstract. Retrieved 2014 methods are not silently substituted for this 2015 article. |

Part I must not be confused with Part II DOI 10.1016/j.trc.2015.05.011. Direct
publisher and guessed repository routes did not yield full Part I methods in
this pass. That access outcome is not evidence that the law is unavailable.
No source archive was overwritten or duplicate full-method ID introduced.

## Scoped claims

| ID | Result | Evidence level / boundary |
|---|---|---|
| RM9-C10 | Two-input positive-priority allocation has a closed piecewise form respecting offers and shared receiving, with total accepted flow equal to the lesser of supply and total eligible offer | Reviewer transcription/proof of RM0018 MISO family; applies to one receiver, not arbitrary independent multilane allocations |
| RM9-C11 | Local ramp-offer changes can alter the stream split while leaving total accepted service unchanged | Hand calculations/branch derivative; not a whole-trajectory gradient or utility proof |
| RM9-C12 | Fixed lane-specific offers/receivers can yield different total service at the same road-total offer | Algebraic availability diagnostic; not identical density/flow/speed history, not a core certificate |
| RM9-C13 | Printed combined-incentive coefficient can exceed one for stated local inputs | Reviewer range diagnostic from FB0030; reachability under full source dynamics not established |
| RM9-C14 | Printed zero-receiving special branch does not implement a simple accepted-transfer receiving bound on its own | Reviewer branch diagnostic; further full-update interpretation required, no silent correction |
| RM9-C15 | Sequential bounded lateral exchange followed by recomputed state limits and residual shared sending/receiving budgets yields a conservative, storage-bounded reference update under the stated step restrictions | Reviewer **proposal**, not adopted or calibrated source physics |
| RM9-C16 | The inspected 2014 optimization predecessor leaves lateral flow to the optimizer | Source methods; importing it would change the approved meter-only action |

## Range and shared-budget audit

Main derivations are in the [PDF](../synthesis/rm9/rm9_priority_allocator_and_control_effects.pdf).
The fuller coefficient and receiving branch need a domain explanation before
being used as accepted lateral flow. A source demand/supply correction cannot
simply be combined with another allocator: each actual transfer must be counted
once, with one donor balance and one receiving/storage budget. No added clipping,
smoothing or source repair has been adopted.

## Candidate synchronization

[RM9-UG2](../reporting/rm9_30_allocator_contract_and_control_chain.md) distinguishes
an explicitly bounded discretionary/two-stage adaptation from retaining the
fuller source family for further source-level resolution. Candidate A's exact
bounded update is a proposed methodological adaptation, even though its
attractiveness form and merge node have inspected literature antecedents.
Candidate B retains the strongest physical advantages of the fuller mechanism.
Neither is approved by RM9-UG1.A. No cost or exact numerical priority gate added.

## Subsequent disposition — 2026-10-02

UG2.A was accepted by the user. Its mathematical bounds remain valid; continued
analysis quantifies an implicit free-flow service debit from the residual shared
budgets. [New claims C17–C22](rm9_accepted_kernel_claims.md) and
[UG3](../reporting/rm9_40_accepted_kernel_findings_and_resource_gate.md) explicitly
reopen that resource clause. The accepted handout is preserved; the proposed
separate-resource amendment is not adopted. Earlier unapproved-UG2 statements
above describe the pre-acceptance audit rather than current status.


The user subsequently [approved UG3.B](../discussion/rm9_resource_b_approval_and_continuation.md).
The separate-resource law is current; earlier proposed/not-adopted language
describes history. [C23–C28](rm9_separate_resource_claims.md) and
[UG4 findings](../reporting/rm9_50_separate_resource_findings_and_observer_gate.md)
record the continued audit and pending observer contract.
