# BP-R Stage 3 — supplied originals and remaining merge transfer

Date: 2026-10-06. **Both supplied originals read; CM and local IT qualified at
source level; S3-G2-N.A subsequently approved.** This supersedes the
blanket access dependency in the [earlier checkpoint](../../../reporting/rm12/bp_r_stage3/source_qualification_checkpoint.md).
This extraction did not itself adopt the node; the subsequent user approval did.
The [latest bounded evidence audit](post_priority_evidence_audit.md) and
[S3-G3 findings](../../../reporting/rm12/bp_r_stage3/post_priority_findings_and_disposition.md)
record continuation. Stage 3 is not user-closed.

## Provenance and version control

| Stable ID | Actual original / locations read | Unmodified supplied file |
|---|---|---|
| RM12-S3-A01 | Laval & Daganzo, *Lane-changing in traffic streams*, TRB 40 (2006), 251–264; DOI 10.1016/j.trb.2005.04.003. All 14 pages; especially Section 2 and Appendix A, pp. 253–256, 261–262. | [Supplied PDF](../../../archive/user_supplied/rm12_bp_r_stage3/Lane-changing%20in%20traffic%20streams.pdf) |
| RM12-S3-A02 | Daganzo, Lin & Del Castillo, *A simple physical principle for the simulation of freeways with special lanes and priority vehicles*, TRB 31(2) (1997), **103–125**; DOI 10.1016/S0191-2615(96)00032-X. All 23 pages; especially Sections 2–5. | [Supplied PDF](../../../archive/user_supplied/rm12_bp_r_stage3/A%20SIMPLE%20PHYSICAL%20PRINCIPLE%20FOR%20THE%20SIMULATION%20OF%20FREEW%20A%20YS%20WITH%20SPECIAL%20LANES%20AND%20PRIORITY%20VEHICLES.pdf) |

A02's own header gives 103–125; A01's bibliography and earlier review records
give 105–125. Use the supplied original's pagination here, preserving the older
records as dated evidence. A01's 2005 acceptance/copyright dates do not change
its final journal year. Its example parameters differ from RM8-P01; do not
combine them as one source parameterization.

SHA-256:

- A01: `ac4a032d7e9df4baa2daa5b0546c8c22d95bb84f6320eb97463d12cad33c2b58`.
- A02: `512befe8666bbdb17a23386d76d499b85a5a6918ae99d51b7f247c882f7e2895`.

Extracted with installed pypdf; originals not renamed or rewritten. Supplied
figures were not visually inspected. See [source records](../../../screening/rm12_bp_r_stage3_supplied_methods_records.csv)
and [manifest](../../../archive/manifest.csv).

## What the originals resolve

**Conservation and local IT — A01 Section 2.1, equations 6–13.** Continuous lane
density evolves through paired longitudinal/lateral flows. Desired lane changes
depend on positive lane-speed differences; through demand is the remaining
sending share. When a target is overloaded, its receiving is prorated among
incoming demands; otherwise all demands advance. The final journal gives this
explicit recipe. The earlier working paper's abstract IT interface is no longer
a missing local formula.

**Speed support — A01 p. 255, footnote 2.** Lane-choice speed is generalized
space-mean speed on a downstream look-ahead support over a preceding evaluation
period. It differs from a particle's immediately downstream KW speed. An
arbitrary instantaneous cell FD inversion is not automatically either source
quantity. Numerical support must be declared without changing the physical law.

**Constrained motion — A01 Appendix A, equations A.1–A.4.** Realized speed is the
smaller of desired kinetic speed and the immediately downstream KW-stream
speed. Desired speed advances by bounded acceleration; position advances by
realized speed. Acceleration depends on speed, vehicle capability and grade.
The previously unverified minimum-speed construction is now an exact source
rule. Its downstream-speed estimate must use consistent coupled traffic, rather
than a convenient substitute chosen for the task.

**Events versus mass — A01 Section 2.2.** Cumulative actual transfers can generate
deterministic unit-threshold disturbance events; these quantize descriptors,
not the conservation update. The descriptors impose zero *relative* passing
while moving continuously. Positive stationary-detector flow remains possible.
The conserved field already counts traffic; adding each descriptor as extra
TST population would double count. Numerical insertion, birth-speed convention
and coincidences remain transcription obligations. No random sampling,
trajectory jitter or rounding of physical mass is adopted.

**IT scope — A02 Sections 2–3.** The incremental construction allocates two
traffic classes with different permissions to two lane sets and is shown
equivalent to the corresponding Godunov fluxes. Its priority class may use
lanes unavailable to regular traffic. That is not a fixed mainline-versus-ramp
priority parameter. Section 4's example is a congested **exit** ramp/diverge;
Section 5 explicitly leaves broader junction extensions for further research.
The title and homogeneous proof do not establish the merge manuscript's 40%
ramp-priority construction.

Source equations and proposed adaptations are kept separate in the
[mathematical companion](../../../synthesis/rm12/bp_r_stage3/source_laws_and_merge_choices.pdf).

## Nearest primary-method checks after receipt

**RM12-S3-C01, 2003 PWP-2003-10**, [*On the Numerical Treatment of Moving Bottlenecks*](https://escholarship.org/content/qt69r4t5pp/qt69r4t5pp.pdf),
was rechecked. Prescribed-trajectory cumulative-count convergence does not by
itself establish pointwise speed feedback. Its automatic browser title is
incorrect; the actual cover/body identify the intended report.

**RM12-S3-S02, 2003 RR-2003-2**, [*Moving Bottlenecks: A Numerical Method that Converges in Flows*](https://escholarship.org/content/qt1hp588xx/qt1hp588xx.pdf),
Sections 2–4 and appendix, was newly read. Continuous-space constraints and
counts are updated through composite Riemann problems with crossing and
wave-interaction step conditions. This is the antecedent of the separate 2005
paper cited by A01 Section 2.2; Appendix A cites the other 2005 paper. Keep the
versions and count-versus-speed distinction explicit. This supports a coupling
route, not a complete metering/gradient theorem. Suggested perturbations at
degenerate coincidences are not adopted.

**RM12-S3-S01, 1994 PWP-94-12**, [*The Cell Transmission Model: Network Traffic*](https://escholarship.org/content/qt9pz309w7/qt9pz309w7.pdf),
Section 3.2, printed pp. 8–10, was newly read. Two approaches share receiving
under fixed junction priority, with unused shares reallocated when demand is
exhausted. This supports a conservative point-merge proposal. It is an
antecedent of the 1995 Part II journal paper, not the unread gridlock chapter.

At the historical source-access pass the institutional gridlock record was
rechecked; its body remained unavailable. The user now declares it unavailable
and directs continuation without further retrieval.
Four actual queries in two batches have a separate [search log](../../../search/rm12_bp_r_stage3_supplied_methods_query_log.csv).
Secondary descriptions do not establish equations.

## Is the third paper still essential?

**For exact reproduction of RM8-P01's priority adjustment: yes, or an original
equivalent construction must be read.** RM8-P01 Section 2 says the 40% adjustment
implements entry priority without creating additional physical receiving. It
does not give its complete mapping. No fixed priority fraction can be inferred
from “1.4” alone.

**For a defensible method-first local ramp task: no.** The supplied laws and
accessible merge original support a concrete adaptation proposal. Selecting it
changes service and requires a small physical-contract gate. The
[S3-G2-N candidates](../../../reporting/rm12/bp_r_stage3/merge_allocation_gate.md)
compare fixed junction priority and demand-proportional sharing. Both retain the
approved upstream meter and all-stream accounting; neither is declared an exact
reproduction of the unread chapter or a validated site model.

CM, local IT and a conservative moving-boundary route are now explicit.
Joining the mandatory node, finite clearance, public projections and strong
independent closures remains Stage 3 work. Complete-TST benefit, compact
insufficiency and useful gradients remain unproved. **S3-E1.C-ACCESS is superseded
as the blanket blocker; S3-G2-N.A is now approved.** The bounded continuation
reaches S3-G3 with a partial formulation result; Stage 4 unopened and older
negative closures unchanged. The source-law PDF is the historical N-gate
companion; the current equation artifact is linked from the latest findings.
