# B2-A source audit: compact receiving versus travel-time memory

Date: 2026-10-13. Scope: source checks for the approved first qualification
route, B2-A. This is a bounded mechanism review, not a new broad literature
survey or a claim that a compact VSL lane-drop model has been validated.

## Reference list of papers inspected in this pass

| Paper and access | Inspected content | What it supports here; what it does not |
|---|---|---|
| Carey, Balijepalli and Watling (2013), *Extending the Cell Transmission Model to Multiple Lanes and Lane-Changing*, institutional author manuscript. [Primary PDF](https://eprints.whiterose.ac.uk/id/eprint/77315/7/Carey%20et%20al%202013_with_coversheet.pdf) | PDF pp. 2–3 motivation; pp. 7–10 mandatory desire and R1; pp. 10–11 local residual/update steps; pp. 14–15 illustration and cell-level receiving. Rechecked web text; see [B2 extraction](vsl_b2_source_and_reduction_audit.md) for the earlier fuller R1 audit. | R1 is a *local* competition for a target cell's finite receiving: own-lane service first, lateral traffic after. The model tracks location and mass residuals. It neither derives one receiver stock for a whole merging zone nor supplies a native fixed-geometry common-VSL adaptation. Its §6 numerical examples use R2, not R1. |
| Carey (published online 2020; *Transportation Research Part B* 147, 2021, pp. 245–257), *The cell transmission model with free-flow speeds varying over time or space*, DOI 10.1016/j.trb.2020.05.012. [Institutional accepted manuscript](https://pure.ulster.ac.uk/ws/portalfiles/portal/85807280/TRB_2018_842_R2_as_uploaded_to_TR_Part_B_on_2020_04_29.pdf) | PDF p. 6 abstract; pp. 6–7 introduction and the below-one-cell-speed example; pp. 11–12 standard cell sending/receiving and conservation; pp. 19–20 proposed correction using entry-time information; p. 21 conclusion. [Publisher metadata](https://www.sciencedirect.com/science/article/pii/S019126152030326X) checked for volume and pages. | A fixed cell whose free-flow speed is below one cell per step can have badly timed geometric-tail outflow under the naive current-stock fraction rule. Entry timing can correct the illustrated free-flow outflow. This does **not** provide a joined variable-speed lane-change model for P1, or certify the correction in synchronized/congested service. |
| Yperman, Logghe and Immers (2005), *The Link Transmission Model: An Efficient Implementation of the Kinematic Wave Theory in Traffic Networks*, primary six-page conference paper. [KU Leuven PDF](https://www.mech.kuleuven.be/cib/verkeer/dwn/pub/P2005C.pdf) | PDF pp. 0–1 abstract, homogeneous-link setup and boundary cumulative counts; p. 1 sending/receiving and node update outline. | Boundary cumulative traffic histories can retain homogeneous-link travel and queue information without storing every interior cell. This is a serious compact-motion precedent, **not** a demonstrated one-stock model for lateral merges throughout an interior VSL zone or its time-varying speed adaptation. |

Search results also exposed Jin (2015), *Continuous formulations and analytical
properties of the link transmission model*, DOI 10.1016/j.trb.2014.12.006,
through its [institutional abstract](https://escholarship.org/uc/item/6w64d2hf),
and Newell (1993), *A simplified theory of kinematic waves in highway traffic,
part II*, through [bibliographic abstract metadata](https://ideas.repec.org/a/eee/transb/v27y1993i4p289-303.html).
Those texts were **not** substantively inspected in this pass and do not
support a new task claim here. Daganzo CTM metadata appeared in search, but
no original Daganzo paper was used for a conclusion. This separates papers
read from discovery-only leads.

## Source result and our inference

**Directly source-backed.** Carey 2013 provides target-cell receiving,
own-lane-first R1 priority and paired lateral traffic transfer. Carey
2020/2021 demonstrates that simply making current cell outflow a fixed
fraction of current stock when speed is below one cell per tick can produce
a geometric discharge tail for free-flow traffic, unlike finite physical
traversal. Its correction uses an account of when traffic entered. Yperman
et al. establish boundary-history motion for homogeneous links with
node-level exchange.

**Our bounded deduction.** Joining these results for the target task needs
both receiving memory and movement memory. The B2 stock comparison proved
that current receiving plus old grouped masses may hide future space. The
Carey variable-speed example proves that a naive current-stock release rule
can hide exit timing even with no congestion or lane changing. A compact
preparation task could still use travel history, a justified point arrival
curve or a sharply restricted region. The reviewed sources do not prove
that any of these is sufficient for P1's distributed mandatory merging
under one common VSL and complete-time objective.

**Hand/reference check.** For a unit mass uniformly distributed over a
fixed-length free-flow region and speed one-half region length per tick,
physical movement releases one-half in each of two ticks. Repeatedly
releasing one-half of current stock instead releases one-half, one-quarter,
one-eighth, and so on. Exact `fractions.Fraction` arithmetic confirmed that
the physical stock is zero after two ticks while the naive stock is
one-quarter. This is a source-motivated analytical check, not a simulated
traffic experiment or an empirical comparison.

## Limits that control the gate

- The variable-speed paper's demonstrated correction concerns free-flow
  motion. Its coexistence with congested target receiving, R1 lateral
  allocation and permanent lane-end service has not been established.
- The link-transmission source concerns homogeneous links and node
  exchanges. Treating a distributed merge as one node would be a task
  adaptation; adding enough interior nodes may erase A's compact advantage.
- R1's local rule does not determine where the cohort requests merging under
  changing common advice. Donor availability, own-lane demand and downstream
  outflow must belong to the same fixed-geometry chronology.
- Replacing *all upstream early attempts* with one point encounter could
  be a coherent simpler task, but it would alter S13's distributed
  preparation interpretation. Modeling only the later compulsory lane-end
  boundary as a point has no such implication and does not answer the
  upstream timing question. No source result here establishes the
  point-only upstream alternative as the primary information/gradient test.
- No native equal-history witness, calibrated common-VSL response, gradient
  correctness/usefulness result, MP6 applied domain or B2-B necessity is
  established.

[Decision-facing traffic finding and methodological gate](../../reporting/research_readiness/vsl_b2a_compact_closure_findings_and_gate.md)
