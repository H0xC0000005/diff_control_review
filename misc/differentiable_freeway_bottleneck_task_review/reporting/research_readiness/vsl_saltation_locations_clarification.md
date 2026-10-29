# Where saltation enters the VSL task's complete sensitivity

Date: 2026-10-20. **Explanation and requested report clarification completed.**

[Revised PDF, additions in red](../../synthesis/research_readiness/vsl_compact_methods_report.pdf)

[Retained LaTeX source](../../synthesis/research_readiness/vsl_compact_methods_report.tex)

The saltation correction belongs to the sensitivity of the traffic trajectory
as it passes a moving event. Equation 10 now shows it directly for cumulative
lane departures, rather than leaving the reader to identify those departures
inside an abstract state vector. Equation 11 then integrates the already
corrected departure sensitivities. It does not require another saltation
addend at the end.

## Concrete locations in this model

| Location | What can change abruptly, and what the event correction carries |
|---|---|
| **The cohort reaches or finishes reaching the choke** | Eligibility begins and ends at advice-dependent times. In the unqueued far lane, for example, discharge starts from zero and later returns to zero. Shifting those times changes how much has departed at a fixed observation time, so cumulative-departure sensitivity must receive the event correction. A queue may keep another lane's discharge continuous at a pulse edge; the correction follows that lane's actual rate change. |
| **A lane enters queued service** | The selected priority/cooperation branch and representative boundary speeds can change its discharge. For a smooth A queue onset, the event condition is loss of free-service feasibility, as already specified in AS3; the previously zero free queue is not a transverse crossing condition. The correction uses the actual before/after discharge rates. |
| **A queued lane clears** | Just before the last waiting traffic passes, the lane discharges at its selected queued-service rate. After clearance, a feasible free branch passes current arrivals. At an isolated transverse clearance those rates differ. An advice-dependent clearance time therefore changes departure sensitivity even though the departure count itself stays continuous. |
| **E's discharge or insertion speed changes at an event** | The event partitions the retained recovery history into pre-event and post-event source profiles. Moving that partition produces a source-time boundary contribution when differentiating the recovery account in equation 7. It changes future budget, service and departures. This history contribution is required alongside the departure-state correction; the current budget reading is not a separate memoryless state to reset. |
| **A switch whose vector fields agree** | There is no nonzero physical-state saltation correction from that switch. The preparation law's donor/receiving branches match at their boundary, as already shown in AS3. The sensitivity evolution can change afterward without an instantaneous sensitivity jump there. |

## Why the final cost formula has no separate event sum

At a service switch, the number of unfinished vehicle-equivalents is
continuous because cumulative departures are continuous. If the population-
time integral is split at that moving switch, its two endpoint terms cancel:
the running cost has the same value on either side. The event still matters
through corrected departure sensitivities over subsequent time. Adding a
second event-cost term for the same continuous running cost would count an
extra contribution that is not part of this objective.

The queue-area version is consistent: a queue is zero at its birth/clearance
endpoint, so its direct endpoint contribution vanishes. Effects on later
service and retained recovery history remain and must be propagated.

These are applications of the accepted regular-event contract, not new
traffic laws. The complete history derivative, moving source-event terms,
clearance conditions and clock sensitivities are already in
[AS3's full sensitivity reference](../../synthesis/research_readiness/vsl_as3_asymmetric_actions_and_gradients.pdf),
especially its arrival, history-sensitivity, event and TST equations. This
pass also rechecked the primary [Kong et al. manuscript](https://arxiv.org/pdf/2306.06862),
introduction and PDF page 5's identity-reset/matching-vector-field discussion;
no full-paper rereading or new source-model adoption is claimed.

## Artifact changes and checks

The report's Part 5 now names eligibility-front/end and queue-clearance
events, specializes the existing event correction to cumulative departures,
and explains its route into both the recovery account and the final objective.
The new explanations and specialized equation remain red. All ten other
equation groups, the service table, physical model, objective and seven IEEE
references retain their exact source. The source/coverage map and dialogue
are synchronized. The feedback inbox is unchanged.

Saved the 479 pre-edit package hashes and feedback hash in
`/tmp/vsl_saltation_locations_before.json`; preserved exact prior source/PDF
in the [v4 archive](../../synthesis/research_readiness/vsl_report_versions/v4/README.md).
No earlier scientific result, source audit, build or validation record is
overwritten. The model-specific source-time derivative remains credited to
AS3; Kong supplies the regular event-correction principle.

After initial label resolution, two final LaTeX passes use the installed
toolchain from `synthesis/research_readiness/`:

```bash
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=/tmp/vsl_saltation_locations_latex vsl_compact_methods_report.tex
```

[Final build log](vsl_saltation_locations_build.log)

Verification uses the installed review Python/pypdf environment:

```bash
/home/zpz/miniconda3/envs/differential_sim/bin/python /tmp/vsl_saltation_locations_checks.py
git status --short
```

[Verification record](vsl_saltation_locations_validation.json)

The rebuilt PDF remains four physical pages with about 3.46 methodology
pages excluding references, within 3.5 pages at 10 pt. Final passes have
no warnings or box problems. Checks verify the explicit departure-rate
specialization, objective/history explanation, unchanged equation groups/
table/references, actual red PDF text, page extent, feedback and protected
hashes. PDF text and layout/drawing instructions are inspected; no raster
inspection is claimed.

## Status and next allowed action

The explanation retains isolated transverse events and a regular event/
history sequence. It does not assert ordinary derivatives at grazing or
coincident events, or validate numerical gradients. No new methodological
choice, simulator code, installation or traffic/gradient experiment occurs.
This Step 4 report clarification stops for user reading; the next allowed
action is another requested editorial correction. Overall review and
implementation status are unchanged.
