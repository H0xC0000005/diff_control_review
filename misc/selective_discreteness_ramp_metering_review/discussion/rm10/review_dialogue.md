# RM10 approval, execution and result record

Date: 2026-10-05.

## User decision and authority

The user selects Option A, requires A to reach a complete positive or negative
conclusion, and excludes involvement of C before A completes. This supersedes
the earlier procedural A/C screen authorization. Record UG5.A scoped RM9 closure
and open RM10 A-only source/analytic review. No duplicate planning gate was imposed.
Production implementation, SUMO, traffic runs, numerical gradients and installs
remain outside the methodology-only scope. The feedback inbox was not edited.

## Scope held during execution

Single ramp, common bounded open-loop rate schedules, strong mass/flow/speed/ramp
history, public arrivals/geometry/parameters and complete all-stream TST. No extra
lanes, private forcing, erased observations or gap-timed actuation was introduced.
The old equilibrium FD-speed observation is not silently used as a physical
non-equilibrium speed closure. Source geometry was inspected to delimit A-source
assumptions; no C review, C search or joint A+C law was opened.

## Source and analytic work

Recorded sixteen targeted queries and sixteen new/reused source records. Reused
the prior empirical/hybrid, modified-demand and gradient packet; followed the
nearest endogenous-capacity/heterogeneity and bounded-acceleration primary
frontier. S12A005 is reused across branches rather than assigned a duplicate ID.
The 2011 proceedings body is distinguished from its journal landing metadata;
the 2016 journal manuscript from the 2014 conference antecedent; the PDE–ODE
2020 author version from its 2021 publication. Abstract/indexed access is marked.

Comparison order was basic CTM, aggregate recovery law, reconstructible mode,
observed homogeneous speed state, then heterogeneous/local recovery state.
The last family retains physical plausibility but did not yield a genuine joined
history/action certificate. Approximate capacity agreement was not promoted to
exact closure; source-local retained constraints were not mislabeled purely
aggregate. The complete result is the scoped negative task-admission finding,
with family-level physical support recorded separately.

## Mathematical artifact and build

Main mathematics: `synthesis/rm10/rm10_information_tst_and_gradient_audit.tex`
and sibling PDF. Four pages cover the task envelope, population/TST accounting,
history consistency and conditional sufficiency, aggregate competitors, and
general chain-rule/adjoint sensitivities with event limitations.

Verified installed `latexmk` and `pdflatex`; no package change. Build:

```
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/rm10_latex misc/selective_discreteness_ramp_metering_review/synthesis/rm10/rm10_information_tst_and_gradient_audit.tex
```

An initial tool orchestration string failed before creating the TeX file; corrected
the literal and retried. Initial LaTeX layout overflow was corrected by splitting
the chain diagram and allowing path wrapping. TeX generated font-cache files in
its normal `/tmp` fallback; build completed without installing anything. Final
build and artifact verification are recorded in the work report. No mathematical
acceptance rule was relaxed.

## Result and gate

G0 remained unchanged; G1/G2 source and rival audits complete; G3 negative task
admission; G4 conditional general path, not verified/useful-gradient evidence.
E1–E4 completed. G5 is user acceptance of this completed result, not approval
to continue the same uncompleted A review. No positive task law was frozen and
no new implementation milestone was opened. C is retained but unexecuted.

## Semantic interpretation of the negative result — 2026-10-05

The user interprets A as reviewing merging recovery/speed distributions and asks
whether the negative means existing assumptions cannot hide states, with richer
alternatives merely added assumptions that cannot yield hidden information even
when known at initialization. Clarification: the scoped negative is the absence
of an admitted joined physical/history/action/gradient task, not impossibility
of a complete physical model. Restricted aggregate/known-mode subclasses have
conditional sufficiency; richer local/distribution families lack the joined
certificate and are not universally refuted.

Recovery means adjustment after a merge disturbance: slowed entering/lane-changing
traffic accelerates and the traffic stream reorganizes over time; aggregate
discharge may recover as those disturbances subside. A speed distribution tracks
traffic at different recovery speeds instead of only its mean. These are physical
source-backed possibilities. Keeping an LWR/CTM backbone does not make local
non-equilibrium additions artificial, nor prove them necessary.

Most critically, exact deterministic dynamics with a known complete initial
state and all public inputs cannot generate epistemically new unknown state for
an ideal controller retaining that knowledge. Knowing only initial aggregate
mass/flow/mean speed does not identify every physical coordinate and is not the
same premise. Additional physical coordinates, unknown inputs or limited memory
must not be silently interchanged. No new assumption, source family, task,
closure acceptance or C execution was approved by this interpretive question.
Rechecked RM8-P01 primary explanation and current RM10 findings; synchronized
the findings' semantic boundary. Read/open and documentation edits only, no
new formulas, simulation or scientific tests required.

## User closure and subsequent planning check — 2026-10-05

The user agrees with the clarified scoped result, regards A as closable and asks
whether C should be revised or replaced before proceeding. Record RM10-G5 closure
in `reporting/rm10/rm10_99_user_closure.md`. Planning review of C and alternatives
is authorized; full C execution is not. The RM11 direction proposal preserves
the A result and inherited information/control contracts unless the user chooses
an explicitly different research claim or actuator. No experiment is opened.
