# VSL-B2: source reading and the receiver-closure deduction

Date: 2026-10-13. Status: **Primary-source review executed; conditional local
joining established; stopped before selecting a receiver/motion reduction.**

## Reference list: paper actually viewed this review

| Reference | Version and locations inspected | Role and limit |
|---|---|---|
| Carey, M., Balijepalli, C. and Watling, D. (2013). *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*. *Networks and Spatial Economics*. DOI: 10.1007/s11067-013-9193-7. | Institutional submitted manuscript, 26 PDF pages. §2, printed pp. 3–4; §3, pp. 4–6; §4 opening and eager-demand case, pp. 6–7; §5, pp. 8–11, especially R1/A1 and A2's shared steps 3–11; lane-end limitation after A1, p. 10. PDF page numbers are printed page + 1. | Principal R1 source; selected complete local dependencies and residual context, not whole-model adoption or a native common-VSL permanent lane-drop task. |

[Primary manuscript viewed](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

This is the complete fresh-paper list for B2. The earlier B1 five-paper list and
S13/source records were reused. Subraveti was not reopened: the receiver/motion
choice already triggers the planned stopping condition, before a separate
joint-domain extension would be justified.

[Earlier references and qualifications](vsl_b1_source_and_interface_audit.md)

## What is directly supported by the inspected source

The native CTM uses destination occupancy, holding capacity and flow capacity
to determine receiving. Its free-flow cell length matches one time interval.
R1 first serves own-lane flow, then admits weighted lateral demand from spare
receiving. The common residual steps move remaining donor traffic and update
class and lane occupancy conservatively. Lateral movement enters a downstream
cell of the adjacent lane, rather than being a free transfer at an arbitrary
elapsed-time tick. The source acknowledges unfinished lane changing at the
link end and subsequent effects of transferred traffic on through-lane flow.

These facts support the requested local service dependence. They do not specify
a reduction to two cohort totals, a variable-speed fixed-geometry task, or its
permanent lane-end completion rule. Those require a declared adaptation.

The manuscript's numerical examples in §6 use R2's proportional allocation.
R1 is specified as a rule and algorithm in §5, but those examples do not
validate R1 for the proposed lane drop. Its use here is a transparent
structural candidate, with empirical and joined-domain suitability still open.

## What this review derives, rather than attributes to the paper

The supporting note uses the source-compatible receiving ingredient and R1
allocation as a conditional mathematical diagnostic. It derives the original
ten/four receiving illustration from two target occupancies. Paired mass and
receiving work remain distinct. A shared physical donor sending budget still
needs qualification in any fixed-geometry adaptation; the diagnostic does not
certify every native algorithm branch or silently add a sender cap.

The new result is a receiving-state closure counterexample. Two target
occupancies give the same current receiving limit on its capacity plateau.
They have identical own service, merge completion, inflow and outflow but
different next receiving limits. Farther continuing stock can compensate to
keep the ending/combined-continuing totals identical. Thus those totals plus
the current receiving scalar do not generally close future local service in
this stock-based family.

This is not a native reachable equal-history pair, an optimal-VSL comparison,
or proof of full lane-profile necessity. A restricted state family, informative
history, an inferred receiver stock or a compact autonomous stock augmentation
could remove the ambiguity. On a strictly space-limited receiving branch with
known parameters, the receiver stock can be recovered from receiving; the
capacity plateau prevents that inversion in general. Predicting the subsequent
own demand and outflow remains necessary in either case.

The fixed cell/free-speed relation also exposes an action interface obligation:
changing realized speed on fixed geometry cannot retain unit free-flow cell
advance for every action merely by relabeling the speed parameter. No new
transport discretization or capacity-versus-speed law was selected.

[Reference equations, examples and closure proof](../../synthesis/research_readiness/vsl_b2_joined_service_contract.pdf)

## Access and verification boundary

Used primary web `open` and `find` to read the listed sections, including the
complete shared residual-step text. Screenshot requests for PDF pages 11 and
12 returned Internal Error. A page-5 request produced a reference but no image
that was inspected in this orchestration. The source check is therefore textual;
no rendered-source equation or whole-algorithm certification is claimed.
No paper PDF was downloaded or archived anew.

Exact single-opportunity calculations were checked with standard-library
fractions. They are hand/reference checks, not traffic experiments. The new
LaTeX note is a review artifact, not simulator code. The report stops at
VSL-B2-G1 before choosing the autonomous receiver/motion contract, so common
advice response, subsequent traffic chronology and MP6 remain unqualified.

[Traffic findings and the concrete methodological choice](../../reporting/research_readiness/vsl_b2_joined_service_findings_and_gate.md)
