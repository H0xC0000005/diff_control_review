# Literature rival selection: inspected references and source limits

2026-11-02. This is the reference list for the bounded rival-selection
review. It distinguishes primary method reading, reused evidence and
metadata/access checks. It does not archive new paper PDFs or report
traffic experiments.

The review starts from the existing
[baseline screen](vsl_successor_baselines_and_evidence_gaps.md),
[S06 source audit](../s06_reference_mechanism_source_audit.md) and
[published-backbone source record](vsl_published_backbone_sources.md).
Historical task-first claims in those documents do not override the
selected lane-cell task.

## Primary papers rechecked

### [1] Zhang et al.: the recommended source route

C. Zhang, E. Chung, N. R. Sabar, A. Bhaskar, and Y. Ma, “Optimisation of
variable speed limits at the freeway lane drop bottleneck,”
*Transportmetrica A: Transport Science*, vol. 19, no. 2, Art. no. 2033878,
2023, doi: [10.1080/23249935.2022.2033878](https://doi.org/10.1080/23249935.2022.2033878).

[Institutional 44-page manuscript](https://ira.lib.polyu.edu.hk/bitstream/10397/92568/1/Zhang_Optimization_Speed_Freeway.pdf)

[Institutional publication metadata](https://research.polyu.edu.hk/en/publications/optimisation-of-variable-speed-limits-at-the-freeway-lane-drop-bo/)

**Actual reading.** Selected extracted paragraphs of Section 2, equation
(1), Figure 3's action constraints, Section 3's optimizer description,
Section 4.3, equation (12), Table 6
and figure captions/text for Figures 14–19. PDF pp. 19–21 are central;
p. 21 explicitly describes enumeration and its inherited search domain.
The manuscript spelling “Optimization” and published title “Optimisation”
are not silently treated as different papers. Metadata confirms February
2023, volume 19(2), article 2033878.

**Use.** Establishes the native CTM/enumeration branch separately from
the microscopic GA branch. The main report's proposed action/objective/
boundary changes are ours and are not attributed to the source.

**Limits.** No author code, GA implementation, field-data reproduction
or independent calibration is audited. No source optimum is transferred.
PDF screenshot requests did not provide a verifiable rendered-page
inspection; this review relies on extracted primary text and earlier
selected-method evidence. The institutional abstract's optimistic
optimization wording is not used as a global-optimum certificate.

**Follow-up question, 2026-11-02.** Recheck the practical paragraph
immediately before Section 5, PDF p. 22 and Figure 19, together with
Section 3 and Section 4.3. It describes demand-conditioned application and
a proposed half-interval feedback search. Record that separately from
GA and enumeration. No gradient optimizer or ordinary derivative
qualification is supplied there. Gradient compatibility of a future
adapted CTM/controller is an open methodological check, not source evidence.

**Matched-controller follow-up, 2026-11-02.** Recheck Section 3.2,
PDF p. 12: the parameter-array representation and the Aimsun fitness
evaluation paragraph. This supports an objective-feedback speed-search
workflow as a possible no-simulator-derivative counterpart. It does not
supply a published gradient counterpart or a learned aggregate-state
policy, and no such equivalence is claimed.

### [2] Han et al.: close physics lineage, different control formulation

Y. Han, A. Hegyi, Y. Yuan, S. Hoogendoorn, M. Papageorgiou, and C. Roncoli,
“Resolving freeway jam waves by discrete first-order model-based predictive
control of variable speed limits,” *Transp. Res. C*, vol. 77, pp. 405–420,
2017, doi: [10.1016/j.trc.2017.02.009](https://doi.org/10.1016/j.trc.2017.02.009).

[Institutional accepted manuscript](https://pure.tudelft.nl/ws/files/45432235/AAM.pdf)

**Actual reading.** Section 2.3's VSL paragraph and Section 3's opening
and selected Sections 3.1–3.3, especially equations (11)–(19), PDF pp. 8–11.
This extends the earlier budget reading into the controller's decision
variables, cost and timing. Selected comparison/controller descriptions
in Section 4 were checked; no complete experimental reproduction is claimed.

**Use.** Distinguishes inherited sending/receiving physics from adoption
of the native MPC controller. The source's flow-to-speed conversion and
objective do not become a common-advice/full-TST controller by name alone.

**Limits.** No solver or runtime result is reproduced. PDF screenshot
retrieval failed; extracted equations and prose support the reading.
The recommendation does not alter the selected H budget.

### [3] Hegyi et al.: aggregate MPC context

A. Hegyi, B. De Schutter, and H. Hellendoorn, “Model predictive control for
optimal coordination of ramp metering and variable speed limits,”
*Transp. Res. C*, vol. 13, no. 3, pp. 185–209, 2005, doi:
[10.1016/j.trc.2004.08.001](https://doi.org/10.1016/j.trc.2004.08.001).

[Author report 03-016](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/03_016.pdf)

[Author publication record](https://www.bartdeschutter.org/publications/03-016-model-predictive-control-optimal)

**Actual reading.** Abstract and selected Sections 3.1–3.2, control/state/
objective context, and Section 6's scope statements. The parsed primary
report confirms its title and rolling-horizon procedure. Initial direct
URL opens timed out; a later indexed primary-PDF open succeeded.

**Version distinction.** This is the TRC coordination article, not the
similarly authored 2005 IEEE paper “Optimal coordination of variable speed
limits to suppress shock waves.” Those two works are not interchangeable
citations. The older review's 03-016 link is identified by its actual title
here; no archived source is rewritten.

**Limits.** Only VSL comparison relevance is reviewed. No ramp controller
is selected, implemented or reopened, and no METANET calibration is
reproduced.

### [4] Jin and Jin: native actuation and constant-control limits

H.-Y. Jin and W.-L. Jin, “Control of a lane-drop bottleneck through variable
speed limits,” arXiv:1310.2658, submitted 2013.

[Primary PDF](https://arxiv.org/pdf/1310.2658)

[Primary HTML](https://arxiv.org/html/1310.2658)

[Previously archived PDF](../../archive/full_text/FB0001.pdf)

**Actual reading.** Selected Section 2.1–2.2 boundary-actuation passages,
equations (6), (10)–(11), the constant-control/equilibrium discussion
in Section 3 and the I/PI definition in Section 4, particularly equations
(15)–(17). The PDF is headed October 29, 2018; the arXiv record reports
submission in 2013. No final journal-version equivalence is assumed.

**Use.** The lack of an inflow-control path for a cohort already entirely
inside our road is our task-fit deduction from the declared actuator.
It is not a claim that the source's feedback method is ineffective in its
native problem.

### [5] Wei et al.: published predictor versus published controller

L. Wei, Y. Han, and M. Wang, “A first-order link-based flow model with
variable speed limits and capacity drops for freeway networks,”
*Comput.-Aided Civ. Infrastruct. Eng.*, vol. 40, no. 21, pp. 3200–3217, 2025,
doi: [10.1111/mice.13492](https://doi.org/10.1111/mice.13492).

[Primary publisher text](https://onlinelibrary.wiley.com/doi/full/10.1111/mice.13492)

**Actual reading.** Metadata, abstract/scope and discussion of control
applications were rechecked. The model's detailed methods reuse the earlier
[source audit](vsl_r1_primary_source_join_audit.md); a new full-method
qualification is not claimed.

**Use.** The authors discuss combining their model with MPC as future
work. That prevents labeling this paper alone an already specified VSL
controller. Its aggregate history remains a serious forward-model rival.

## Other material opened or followed

- A. Hegyi, B. De Schutter, and J. Hellendoorn, *Optimal Coordination of
  Variable Speed Limits to Suppress Shock Waves — Addendum*, technical
  report CSE02-015a, March 2003.
  [Five-page primary addendum](https://www.dcsc.tudelft.nl/~bdeschutter/pub/rep/02_015a.pdf).
  Its title, scope, version and rounding discussion were viewed while
  resolving source identity. It is not the principal [3] and is not used
  to qualify a new rival.
- Van de Weg et al.'s 2015 parameterized-VSL control paper was followed
  from [2]'s reference list at title/metadata level. No primary method
  body was obtained or qualified, so it is not a reviewed rival candidate.
- Existing Delle Monache/Piccoli/Rossi derivative-control evidence is
  retained through the prior baseline screen. It is not newly requalified
  here, and this pass makes no first-gradient-VSL or literature-wide
  absence claim.

## Scope conclusion

The recommended [1] route has a real source precedent. A complete adapted
comparator remains to be specified and accepted. Searches did not establish
that these five papers exhaust the relevant literature or that no closer
native one-advice task exists. This bounded review stops at source
selection rather than expanding into an unrestricted controller survey.

