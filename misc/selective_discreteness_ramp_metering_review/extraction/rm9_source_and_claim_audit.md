# RM9 source-to-claim audit

Date: 2026-10-01. All source IDs reused; versions in [screening](../screening/rm9_records.csv).
Main mathematics is in the [PDF](../synthesis/rm9/rm9_compact_state_and_observer_audit.pdf),
with [TeX source](../synthesis/rm9/rm9_compact_state_and_observer_audit.tex).

## Source observations

**FB0030:** conservation and adjacent/downstream lane dependencies provide
candidate structures. Tables 1–2 calibrate distinct lane free-flow speeds.
Printed pp. 1768–1769 discuss time/space mean speeds and detector-derived density.
Equation 17's special branch remains unresolved; no correction or complete
published-update validation is made. The PDF uses selected source branches
conditionally rather than adopting the entire algorithm.

**RM0004:** Section 2.1 explicitly prioritizes entering ramp flow and excludes
mainline spillback onto ramps. This does not specify arbitrary finite-ramp
receiving. Bounded ramp preference is still a valid candidate; priority itself
is not refuted.

**RM0018:** primary published version (2017), Section 3.1/Remark 3.1 and priority
examples: explicit priorities and unused-supply redistribution; cautions against
priorities depending on current demands under first-order nodal invariance.
This is the existing Wright source, not a new RM9 source ID. The archived
arXiv version is not replaced. No whole partial-FIFO network model is adopted.

**RM0003/RM0014:** inherited primary method evidence respectively supplies
history-defined hysteresis and a field merge mechanism with aggregate sensing.
Neither supplies RM9's mathematical claims below.

## Reviewer derivations and strict limits

| Claim ID | Derivation | Status / limit |
|---|---|---|
| RM9-C01 | Exact projected dynamics require agreement of projected next updates for every equal projected state | Necessary closure condition; not a universal sufficiency/minimum-state theorem |
| RM9-C02 | A selected free-flow lateral branch can distinguish the adjacent rest lane at fixed shoulder/rest totals | Conditional local-operator obstruction for 3+ lanes; not an identical-history/action pair |
| RM9-C03 | Two physical mainline lanes need one additional contrast given total mass | Lossless information equivalence; not a proof of dynamic/observer insufficiency |
| RM9-C04 | Distinct known two-lane speeds plus exact co-supported total density/flow can identify a free-flow split | Specific equilibrium observation map; no field reconstruction or whole source-update proof |
| RM9-C05 | An independent passage-weighted speed moment can identify three distinct-speed lane densities in the stated subcase | Requires true co-supported independent observations; not implied by detector-derived density |
| RM9-C06 | Conservative budget constraints alone do not select competing ramp/mainline flows | Family subsequently resolved by RM9-UG1.A as Default; full lane coupling remains pending |
| RM9-C07 | Common total arrivals and departure history imply identical complete system time | Exact accounting identity; queue relocation alone gives no benefit |
| RM9-C08 | A fixed-branch total-time sensitivity depends on departure-history sensitivity | Conceptual identity only; no numerical gradient correctness or external usefulness |
| RM9-C09 | An upstream meter limits upstream release, while merge offer/entry depends on propagation and stored traffic | Do not impose instantaneous meter cap on downstream entry unless co-location is specified |

The group counterexample intentionally matches group mass, not all observed
flow/speed. It must not be promoted to a core hidden-information certificate.
A source-faithful profile can be used as a reference for proving a compact
interface; its temporary analysis does not establish full per-lane necessity.

## Adaptations not approved

Instantaneous mixing across rest lanes; equal lane FDs selected to hide state;
replacing a distinct measured speed with a redundant derived speed; source branch
repair; unrestricted exogenous ramp entry; inherited VSL proportional batch
service as a continuous-flow node; event/stochastic derivative estimators.
There is no new source-based full-chain certificate in this pass.

## Subsequent allocation decision

RM9-UG1.A is now approved as Default. The [joint-flow audit](rm9_joint_flow_readiness_audit.md)
adds scoped claims C10–C16 and the new physical-law boundary. The original PDF
is retained as the dated first audit; source branch repair and full-model
certificates remain unapproved/unestablished.
