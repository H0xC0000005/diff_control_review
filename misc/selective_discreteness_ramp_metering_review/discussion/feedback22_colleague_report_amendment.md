# Feedback 22 — colleague-facing report amendment

Date: 2026-09-15  
Decision status: incorporated into the RM5 report contract; report drafting remains gated

> Voice amendment: `feedback23_objective_voice_revision.md` supersedes the
> first-person framing below. The substantive value--compatibility position and
> audience cleanup remain active.

## User's intended position

The colleague's suggestion to treat ramp metering as a parallel new task is not
acceptable for the current project. The report should make this the author's
position, rather than presenting a neutral menu of future options.

The reason is a two-sided incompatibility of value and scope:

1. **Compatible but low-value formulation.** If ramp metering is kept within the
   present continuous-mass, first-order traffic formulation, its main behavior is
   aggregate ramp admission, queue regulation and merge supply allocation. Strong
   macroscopic models and gradient-based control methods already address this
   formulation. It therefore offers little distinct evidence about the value of
   selectively retained mesoscopic order or route semantics.
2. **Potentially distinctive but incompatible formulation.** The freeway
   behaviors most likely to give a richer mesoscopic model distinct control value
   include lane-changing and access dynamics, gap acceptance, car-following,
   heterogeneous speed or driving behavior, and related merge phenomena. These
   are not native to the current project formulation. Adopting them would require
   substantial new methodology, state, operators, validation and engineering;
   this would be a material project expansion rather than a parallel application
   of the existing model.

Accordingly, the report's recommendation is to reject ramp metering as a parallel
new task. This does not deny the operational value of ramp metering or the
scientific value of other mesoscopic freeway models. It says that the proposal
does not satisfy both project compatibility and distinct scientific value at the
same time.

## Audience cleanup

The report is written for colleagues who have not followed this review's internal
workflow. Its default vocabulary will therefore be semantic:

- “traffic-signal control task,” not an internal task abbreviation;
- “restricted upstream-meter/downstream-diverge example,” not its candidate code;
- “ordered local service mechanism,” not a milestone/component label;
- ordinary prose descriptions of compatibility and evidence value, not review
  question IDs, source-record IDs or phase/gate names.

Numerical literature citations are retained because they help readers verify the
evidence. An internal identifier may appear only if it is genuinely needed to
identify an artifact; none is presently expected in the colleague report.

The report will not contain internal closure administration, project-file status,
ownership assignments, reopen conditions, approval gates or future-work routing.
Those controls remain in this review package and are not part of the external
narrative.

## Wording discipline

The conclusion must remain precise:

- say “unacceptable as a parallel task for the current project,” not “ramp
  metering is unacceptable” without qualification;
- say “little distinctive value under the current formulation,” not “no value”;
- say “requires substantial methodological and engineering work,” rather than the
  ambiguous phrase “needs decent effort”; and
- acknowledge the strongest favorable evidence before showing why it does not
  overcome the value/scope dilemma.

## Resulting report shape

The report will lead with the rejection, state the project-relevant evaluation
standard, summarize the macroscopic/mesoscopic/differentiable evidence, explain
the central dilemma, address the strongest counterarguments, optionally delimit
two narrow validation uses, and close with a concise project-specific conclusion
and references. The former section on project consequences and reopen conditions
is removed.

## Next gate

The amended contract is in `../reporting/rm5_report_scope_gate.md`. Explicit user
approval opens the LaTeX/PDF drafting and rendering pass. Until then, no colleague
report is drafted and no project file is changed.
