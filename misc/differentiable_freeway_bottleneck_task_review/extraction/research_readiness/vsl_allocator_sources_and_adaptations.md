# Allocator review: viewed references and adaptation boundaries

**Later status, 2026-10-21.** The user selects the attempt-and-forward
candidate for qualification. This source/adaptation record remains unchanged
in substance; the selection does not turn its new composition into a native
published algorithm or transfer empirical/gradient certificates.

[LF1 decision](../../reporting/research_readiness/vsl_allocator_selection.md)

[New congestion/VSL source check and LF2](vsl_congestion_join_sources_and_adaptations.md)

2026-10-21. This is the reference list for the allocator pass, including
inspection depth. Papers returned by searches but not method-read are not
treated as established allocation candidates. Public reading copies remain
in `/tmp`; no full-paper archive addition is made.

## Newly read primary methods

**[1]** M. Carey, C. Balijepalli, and D. Watling, “Extending the cell
transmission model to multiple lanes and lane-changing,” *Networks and Spatial
Economics*, vol. 15, pp. 507–535, 2015, doi: 10.1007/s11067-013-9193-7.
Published online July 27, 2013; institutional submitted manuscript labeled
2013. The worked-method reading uses that submitted version, not an unseen
final typeset algorithm.

[Publisher metadata and version dates](https://link.springer.com/article/10.1007/s11067-013-9193-7)

[Institutional record](https://eprints.whiterose.ac.uk/id/eprint/77315/)

[Primary manuscript read](https://eprints.whiterose.ac.uk/77315/7/Carey%20et%20al%202013_with_coversheet.pdf)

Local reading file: `/tmp/vsl_allocator_review/Carey_2013_author_manuscript.pdf`,
985,961 bytes, 26 PDF pages. SHA-256:
`4709f6b71cc70419098359d98a2dd839d244707d29bf887ac9575c223158a455`.
Extracted with installed pypdf. Read introduction
and selected methods, especially PDF pp. 5–13 (printed 4–12): diagonal
transport/conservation; intention and cohort definitions; headway weighting;
priority rules R1–R3 and algorithms A1–A3. The detailed worked algorithms
restrict attention to L2-to-L1 changing on two lanes. They permit residual
traffic to advance in its original lane after actual lateral movement is
removed. R1 prioritizes existing-lane traffic; R2 shares by competing
quantities; R3 permits other fixed shares with unused-share redistribution.
The paper explicitly cautions that some desired changes may remain unserved
at the final cell. We do not treat it as a ready permanent-lane-end closure.

Our candidate uses this transport/attempt interpretation but does **not**
copy its FIFO cohort ledger or claim its two-lane algorithm already solves
the three-lane donor competition. The proposed common donor normalization,
all-target first pass, later forward fallback and permanent-end connection
are review adaptations. The elementary alpha = 1 receiving case is an
explicit proposed simplification, not an empirical claim about merging gaps.

**[2]** M. A. Wright, G. Gomes, R. Horowitz, and A. A. Kurzhanskiy, “On node
models for high-dimensional road networks,” *Transportation Research Part B:
Methodological*, vol. 105, pp. 212–234, 2017,
doi: 10.1016/j.trb.2017.09.001.

[Primary author preprint, HTML](https://arxiv.org/html/1601.01054)

[Preprint record](https://arxiv.org/abs/1601.01054)

Read §2.1's demand/supply, priority, FIFO and redistribution requirements;
§3.1's MISO rule and remarks 3.1–3.2; §3.2's full/partial/no-FIFO distinction;
selected §3.3 MIMO constraints; and the capacity/demand-priority contrast in
§4.2. The inspected HTML identifies arXiv v3 (2017). The separately opened
31-page PDF has a different body date (2018); its pagination is not used as
the equation locator here. The publication identity is distinct from these
preprint versions. Appendix B is linked but its full algorithm was not
transcribed in this pass.

The source supports explicit fixed-priority receiving allocation with unused
share redistribution and the fixed-fraction/full-FIFO alternative. It warns
that demand-based priorities can violate nodal invariance, and that applying
a MISO proportional-demand relation independently at every MIMO output is
not automatically a proper general junction solver. Our preferred two-pass
rule is therefore **not labeled the Wright MIMO model**, nor credited with
its complete junction theorems. The capacity-based priorities proposed here
are fixed reference values, not advice-capped current demand. The mapping
from lane incentives and diagonal cells remains our adaptation.

## Reused primary evidence

**[3]** H. H. S. Nagalur Subraveti, V. L. Knoop, and B. van Arem, “First
order multi-lane traffic flow model – an incentive based macroscopic model
to represent lane change dynamics,” *Transportmetrica B: Transport Dynamics*,
vol. 7, no. 1, pp. 1758–1779,
doi: 10.1080/21680566.2019.1700846. Repository/copyright 2019; article
header 2020. Native lane-density/incentive and capacity-drop evidence is
reused from the preceding qualification pass, not newly certified by this
allocation construction.

[Archived source](../../archive/full_text/FB0030.pdf)

**[4]** H. H. S. Nagalur Subraveti, *Lane-specific Traffic Flow Control*,
Ph.D. dissertation, TU Delft, 2021,
doi: 10.4233/uuid:e405a549-b1fe-4fa1-8090-4429612359d9. The preceding pass's
selected chapters clarify a receiving branch and give a three-to-two case;
they do not establish the allocator proposed here.

[Institutional dissertation](https://repository.tudelft.nl/record/uuid:e405a549-b1fe-4fa1-8090-4429612359d9)

**[5]** Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and
C. Roncoli, “Resolving freeway jam waves by discrete first-order model-based
predictive control of variable speed limits,” *Transportation Research Part C:
Emerging Technologies*, vol. 77, pp. 405–420, 2017,
doi: 10.1016/j.trc.2017.02.009. Reuse the preceding §2.3 sending-cap reading;
it is an actuation lead, not a joint-lane allocator or a certified joined
capacity-drop model.

[Primary accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

[Detailed preceding reading scopes](vsl_lane_backbone_source_audit.md)

## Preview-only checks and excluded evidence

**[6]** C. M. J. Tampère, R. Corthout, D. Cattrysse, and L. H. Immers,
“A generic class of first order node models for dynamic macroscopic
simulation of traffic flows,” *Transportation Research Part B: Methodological*,
vol. 45, no. 1, pp. 289–309, 2011, doi: 10.1016/j.trb.2010.06.004.
Publisher preview/abstract and Wright's primary restatement were inspected.
No direct full-algorithm reading or inherited qualification is claimed.

[Primary publisher preview](https://www.sciencedirect.com/science/article/pii/S0191261510000846)

**[7]** C. Roncoli, M. Papageorgiou, and I. Papamichail, “Traffic flow
optimisation in presence of vehicle automation and communication systems –
Part I: A first-order multi-lane model for motorway traffic,” *Transportation
Research Part C: Emerging Technologies*, vol. 57, pp. 241–259, 2015,
doi: 10.1016/j.trc.2015.06.014. Additional institutional/publisher search
returned previews; no native allocation method was newly qualified. Part II
metadata (doi: 10.1016/j.trc.2015.05.011) was also checked, but its linked
manuscript retrieval failed. Neither is used as evidence for our new equations.
Search snippets and third-party software summaries are excluded as technical
method evidence. No claim of an exhaustive allocator survey is made.

## Provenance of the mathematical note

| Item | Status |
|---|---|
| Continuous lane stocks; density/lookahead-based preferences | Retained principal-source candidate [3], with prior cautions unchanged. |
| One-cell diagonal transport; unsuccessful desired changes need not be realized | Supported modeling approach from [1]; replacing the principal source's same-cell/forward sequence is explicit. |
| Shared donor normalization when outgoing desires exceed one budget | New proposed interface completion, not an extracted source equation. |
| Fixed-priority capped sharing of one receiving budget | Established MISO/R3 principle [1], [2]; capacity-based reference weights proposed here. |
| First allocate bounded directional requests; then return residual traffic to its own forward connection | New three-lane composition; its conservation proof is ours. No general-node theorem transfers. |
| Permanent E end, with only E-to-A permitted | Proposed geometry/boundary adaptation. Native Carey does not guarantee all desired changes before an exit. |
| Storage proof, hand examples and throughput counterexample | New analytical deductions under stated input conditions, not experiments or calibration. |
| Full task, joined VSL/capacity drop, information gap and useful gradients | Not established by this pass. |

The component uses established ideas from a small modeling family, but it
remains a proposed adaptation. Source count alone neither certifies nor
disqualifies its simplicity.

## 2026-10-22: Carey as principal movement source; Wright as supporting credit

Reread the existing local Carey manuscript around R3/A3, printed p. 12,
and the transport/fallback discussion. R3/A3 already permits chosen shares,
caps actual service by available traffic and redistributes unused share.
In its two-stream unit-headway case, equal shares reproduce the selected
equal-priority capped-sharing logic. Wright is therefore not indispensable
as a separate physical mechanism. Its multiple-input formulation and wider
junction analysis support and helped formulate the selected kernel; that
actual contribution remains credited.

A Carey-led description with Wright as a supporting allocation reference
is defensible for the existing selected component, without changing its
equations or adding an independent Wright dynamics module. It does not
turn the whole component into an unchanged Carey algorithm. The permanent
E end and finite geometry are scenario-specific. Joint donor normalization,
the all-target allocation followed by one straight fallback, equal-priority
selection and omission of Carey cohort/FIFO state are model adaptations
that affect behavior and must remain explicit. Generalizing a worked
two-lane algorithm to competing three-lane requests is part of that burden.

This clarification changes no LF1 decision, rule, proof or empirical limit.
It does not claim that a native Carey three-lane algorithm was newly found,
or remove the source history behind the current formulation. No traffic
experiment or new method selection is performed.

## 2026-10-22: finer attribution for the outgoing normalization

The user asks why the intuitive Equation (4) is entirely red. Reread
Subraveti's source Eq. (14), printed p. 1765: lateral demand is sending
demand times a desired movement fraction. Reread Carey's R2/Eq. (9) and
A2: common capacity is rationed in proportion to requests when they exceed
it. Wright's introduction/Section 2.1 also supplies the standard split-ratio
framing. These are existing source families, not new model dependencies.

The exact sender-side conditional normalization remains a review-specified
adaptation; the source's proportional receiving rule is not relabeled as
the same native donor equation. However, the full request equation should
not imply wholly new mathematics. A finer account distinguishes the retained
Subraveti request form, standard straight-share remainder and the application
of proportional rationing to outgoing desires. Carey can support that last
principle with the explicit adaptation boundary. This changes no LF1 rule,
and Equation (5) still uses the selected equal fixed receiving priorities.

[Question, evidence, proposed attribution and work record](../../reporting/research_readiness/vsl_equation4_source_attribution_clarification.md)

The user subsequently approves incorporating the separation. Equation (4)
now credits the adapted proportional normalization to Carey (A), marks the
remainder as standard (S) and credits Subraveti's request form (B). The
sender-side placement is explicitly ours. This presentation change does
not alter the selected rule, make R2 the receiving allocator, or introduce
an additional model dependency.
