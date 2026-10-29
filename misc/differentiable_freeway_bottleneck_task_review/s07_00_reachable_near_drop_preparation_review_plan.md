# S07.00 — Reachable near-drop preparation review protocol

Date: 2026-09-29. Status: **Executed to S07-UG1 / DG-R4; Candidate A approved
and S07 closed.** Parent: [S06 closure](reporting/s06/s06_99_reference_bridge_sprint_closure.md).

## Objective

Determine whether the accepted near-drop information test can be given a
physically reachable and reviewable preparation contract before any reference
simulation. The target is a small bank capable of placing nontrivial traffic in
the final 400 m upstream of the permanent three-to-two narrowing while preserving
the possibility—not assuming the fact—of an exact strong-history collision and
different useful common advice.

## Fixed inputs

- Retain the synthetic 2,400 m three-lane approach, 800 m two-lane downstream
  road, final-400 m contrast region, common lane-wide desired-speed advice,
  homogeneous response semantics, and native following/lane changing.
- Retain the exact full predecision aggregate/history channel, known future
  inputs, outcome-blind pair selection, all-intended-cohort accounting,
  conservation, and Gap 7.
- Treat the current 40/60/80-second schedule and entry details as operative old
  settings under review, not silently amended facts.
- Do not weaken exact equality, shorten history, turn off native anticipation,
  force lane changes, invent a merge penalty, or select preparations by favorable
  action outcomes.

## Review questions and ownership

**S07-Q1 — reachable timing and population envelope (Type 1; analytical).**
Under explicit road-entry position/speed, acceleration, advice-response and
demand assumptions, when can low- and peak-demand cohorts first reach and
meaningfully occupy the final 400 m?

**S07-Q2 — native anticipation and observability tension (Mixed).**
Global contract: an admissible pair must remain exactly identical in the declared
aggregate history through decision time. Local review: identify where native
strategic lane changing and speed adaptation can begin and which recorded
channels they may alter. A documentary lack of a fixed anticipation bound must
be reported, not replaced by an invented distance.

**S07-Q3 — preparation-family choice (Type 2; user-owned at S07-UG1).**
Compare the smallest viable near-drop preparation families: extend road-start
warm-up into the peak-arrival window; shift the demand/preparation schedule while
retaining road-start entry; or use a closer/nonempty initialization with an
explicit reachability burden. State Pros, Cons, dependencies and claim changes.

**S07-Q4 — candidate bank and stop rules (Mixed).**
For each viable family, define an outcome-blind small-bank structure and the
earliest feasibility stops. No numerical run or revised contract is approved by
describing a bank.

Discussion order: Q1 → Q2 → Q3 → Q4. Q3 is the next user gate. A conflict with
exact history reopens DG-G2 rather than being repaired locally; a spatial move to
an earlier upstream contrast reopens DG-R3 and is outside Candidate A.

## Bounded method

1. Reconstruct the current geometry, demand, response, observation and
   preparation contracts from S04–S06 records.
2. Derive continuous-time lower arrival bounds and free-flow region-occupancy
   envelopes for the low-to-peak demand transition. Report equations, units and
   endpoint qualifications in a retained LaTeX/PDF analysis artifact.
3. Inspect only primary native-method or official documentation needed to bound
   departure semantics, desired versus actual speed, strategic anticipation and
   lane-change effects. Reuse S06 sources before new discovery.
4. Audit which preparation families preserve Candidate A's near-drop meaning and
   which introduce hidden initial-state/oracle or observability problems.
5. Present a findings report and S07-UG1 with viable candidates, recommendation,
   dependencies and explicit nonclaims.

## Acceptance and stop conditions

The sprint passes its documentary purpose if it supplies checked timing bounds,
an explicit anticipation/observability audit, and a complete user-owned candidate
choice. A positive recommendation need not certify that an exact native pair
exists. Stop with an obstruction if every near-drop family requires weakening
exact history, forced lane behavior, undisclosed past inputs, or unsupported
dynamics. Stop for a decision-critical inaccessible primary source, identifying
the exact document and claim; otherwise no access gate is expected.

## Outputs and exclusions

Create an analytical source/PDF, source/method audit, S07 findings/gate, work
report, and synchronized navigation/inventory records. Search/access logs are
required only if new online discovery occurs. No code, dependency, server check,
SUMO execution, calibration, experiment, detached process, model construction,
or gradient test.
