# UG4-O: brief semantic comparison of C, A and P

Date: 2026-10-05. Status: **Historical comparison; C subsequently approved.**
The [dated approval](../../discussion/rm9_observer_c_approval_and_continuation.md)
supersedes pending-choice wording below. A/P remain unselected. Continuation
findings and the current gate are in [UG5](../../reporting/rm9_70_observer_c_findings_and_disposition_gate.md).
Parent: [full decision report](../../reporting/rm9_60_r1_observation_findings_and_gate.md).
Existing mathematics: [R1 PDF](rm9_r1_observation_contract_audit.pdf).

## The decision in plain language

The main distinction is which traffic the speed measurement describes.
It is not a discount applied to traffic mass or a new service penalty.
Two operations must be kept separate: assign a representative speed within
each lane, then combine lanes using the weights appropriate to the metric.
The proposed FD closure performs the first operation; it does not choose the
second. All choices expose aggregate information, not the per-lane values used
internally, and none changes the adopted traffic law through averaging alone.

There are two decision dimensions: C versus A concerns the speed metric's
population/location/time; A versus P concerns whether the passage mapping is
accepted as an explicit approximation or needs further physical grounding.
P is a further-review route for passage speed, not a third averaging equation.

## Semantic meaning of each candidate

**C — take a snapshot of the traffic inside the section.** Ask: how fast is
the traffic occupying this cell now, on average? A lane containing more traffic
contributes more to the mean, whether or not that traffic crosses a downstream
face. Model each occupied lane cell with one equilibrium FD speed, then average
with the mass present. The selected epoch is the stored state before the next
update. This is an idealized section-wide observer, not a literal camera setup.

**A — watch traffic cross a line during a completed interval.** Ask: how fast
was the traffic that passed this station, on average? A lane contributing more
actual crossings receives more weight. The current proposal uses the upstream
post-lateral FD speed as the speed of its passing traffic. That second step is
the extra cell-to-face approximation; accepted passage weights alone do not
justify it. An occupied lane with no crossings contributes no passage sample.

**P — establish the crossing-speed mapping before using it.** Ask the same
passage-speed question as A, but require a defensible account of speeds actually
at the observation line. Review internal queues, spatial/temporal support and
any necessary reconstruction before accepting a map. P does not already provide
a new formula or guarantee a more detailed model is necessary; any model change
returns for adoption. It requires no traffic experiment by default.

## Fair comparison

| Aspect | C: section benchmark | A: passage approximation | P: passage grounding first |
|---|---|---|---|
| Traffic being averaged | All mass occupying the cell at the stated instant | Actual traffic crossing a face in the completed interval | Same passage target as A; physical realization to establish |
| Lane weights | Mass present | Accepted crossing mass/count | Crossing mass/count once the mapping is justified |
| Speed assignment | Representative equilibrium FD speed in each lane cell | The same type of FD speed, additionally identified with face crossing speed | Unresolved physical/spatial mapping; no new law adopted |
| No face passage | Section speed still exists if mass is present; an empty cell has no sample | No passage-speed sample | No passage-speed sample |
| Main advantage | Consistent section support with the exact cell-inventory benchmark; no extra dynamic state | Operational passage metric and continuity with the earlier proposal; no extra dynamic state | Confronts detector-level validity rather than assuming the missing map |
| Main limitation | Exact section observation and equilibrium/homogeneity remain idealizations | Adds an unverified cell-to-face identification, especially consequential in congestion | Delays R2; may remain unresolved or require separately reviewed assumptions |
| Next work after approval | Complete compatible observer/layout transcription, then R2 | Declare approximation/support, complete transcription, then R2 | Bounded physical-mapping review; stop before adopting new assumptions |

Conceptual illustration: suppose one lane contains much slow traffic but few
crossings, while another contains less traffic but supplies most crossings.
The section metric emphasizes the large slow population; the passage metric
emphasizes those who passed. The metrics answer different questions. This
illustrates averaging populations, not a verified CTM scenario or proof that
the FD closure reproduces those actual speeds. C and A cannot be ranked as
uniformly more informative from their average values alone.

Both metrics are recognized in [FHWA's measurement guidance](https://ops.fhwa.dot.gov/publications/fhwahop08038/04infoshare.htm).
That grounding validates the distinction, not the adapted CTM observation maps.

## Recommendation and decision boundary

Provisional recommendation remains C for the first idealized, methodology-only
task audit: its section support matches the exact cell inventory and avoids
the extra crossing-location approximation. It does not guarantee hiddenness;
under its free-flow closure, section mass/speed can already identify the split.
If actual detector passage is essential now, P is the appropriate route. A is
viable when an explicitly conditional passage benchmark is acceptable.

The adopted dynamics, mass/flow channels, complete history and common feasible
meter actions remain the comparison backbone. Choosing the speed observation
defines the information contract and requires UG4-O discussion/adoption; it
does not close the hiddenness/action/gradient questions. R2 has not started.

Work record: re-read the gate/inventory and primary FHWA metric definitions;
created this formula-free comparison and added semantic clarification/navigation
to the active decision report and handoff. Archived the response in the dialogue.
Commands: sed/tail, primary web open, apply_patch and local-link/status checks.
No scientific tests, traffic runs, formula/PDF or model changes were required.
