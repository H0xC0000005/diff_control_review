# Joined VSL stack: bounded analytical and methodological review

2026-10-21. **Approved by the user; executed and delivered at JM1.**
The executable proposal remains withdrawn. The approved review scope below
has been completed without implementation or experiments. User acceptance
of the findings is pending; no further task is started.

[Current findings and JM1 checkpoint](../../reporting/research_readiness/vsl_methodology_review_findings_and_gate.md)

The question is whether we can responsibly recommend this stack, built
around published work, as a coherent task with limited, justified adaptations.
Answering that question requires checking its assumptions, component joins
and analytical claims. Demonstrating that a controller performs well is a
separate research activity. The colleague's complexity concern can be
addressed by explaining the backbone, necessary changes and their limits;
it does not require experimental proof that this is the best possible model.

**Keep the three conceptual checks, at review level.** VC1–VC3 below are
review questions, not software components. Carry them out as one bounded
review sprint, reusing the existing source studies and analytical results.
The next result gate is **JM1**, a methodological qualification and
recommendation for the joined stack. Stop earlier if a genuine new modeling
choice is needed. The old VJV implementation/experiment gates are retired.

| Review question | What is already available | Focus of the remaining review | Direct answer required at JM1 |
|---|---|---|---|
| **VC1 — Does the joined traffic model make a coherent, sufficiently supported whole?** | Selected lane/incentive backbone, full Han budgets, conservative allocation, shared-budget/storage proofs and explicit boundaries. | Audit the source-to-component changes, physical meanings and interface assumptions together. Check that “one allocation replacement” does not conceal several unsupported mechanisms. Reuse proofs; add only a focused derivation or hand case if a real gap appears. | Which components are retained or adapted, why the joins are justified, and under which assumptions the model respects mass, storage and service constraints. |
| **VC2 — Is complete accounting and its sensitivity mathematically justified?** | Finite complete population-time, an exact residual value and a regular-branch derivative formula. | Check that their assumptions hold for the same joined model: initialization, progress, exit, tail regime, state dependence and native switches. Trace the whole causal derivative, including residual-state and direct-speed terms. | What derivative exists, where it applies, what fails at switches, and which mathematical claims remain conditional. |
| **VC3 — Does this formulation support the intended research question and a credible response to the colleague?** | Same-observation A/B service contrast, the exactly sufficient scalar on the diagnostic pair, and conceptual comparison requirements. | Trace how hidden lane loading and advice can affect service and the full objective. Check for established structural degeneracy; distinguish an open action-value question from a proved benefit. Review strong simpler rivals and the burden of the adaptations. | Why this is a feasible, focused task for the RQs, which simpler rivals matter, and what can be claimed now without empirical results. |

**How to carry out the review.** Start with VC1: follow the traffic chain
from lane densities and desired movements through shared service, realized
flows and completion. Compare the principal paper's behavior with the actual
selected stack. Distinguish the Han lineage, the new allocation composition,
finite-domain conventions and task assumptions; do not count citations as
separate mechanisms or hide substantive changes under one component name.

Then examine VC2 against that same chain. The existing conservation, progress,
exact-tail and derivative results are inputs, not work to repeat wholesale.
Check their dependencies and consistency. Explain why the remaining-time
term counts unfinished traffic and why a fixed-step branch derivative has
the stated scope while the same traffic regimes and active constraints
persist. This is an analytical check of the formula, not AD/JVP or
finite-difference verification of a program.

Finally examine VC3. For example, the existing A/B swap changes E's service
despite unchanged E and A+B observations. That establishes a meaningful
state distinction, but not different optimal advice. The extra A-density
scalar already identifies the diagnostic pair, so full lane detail cannot
be claimed necessary from it. Keep model-aware reduced-information reasoning,
the compact rival, maximum advice and scalar action search in the conceptual
comparison. Explain what each would test; do not implement or run them.

A missing proof of positive information value is not itself a model defect.
Do not require a new optimal-policy certificate, search for a favorable
scenario, or prove that gradients beat search. If existing equations or a
bounded analytical argument instead reveal that the intended control or
information question is structurally absent, report that as a methodological
issue and stop for the smallest necessary choice. Do not silently redesign
the stack to manufacture the desired effect.

**Evidence and scope.** Use primary-source reconciliation, traffic-semantic
reasoning, mathematical consistency/proofs and small exact hand examples.
Search literature only for a specifically identified unresolved methodological
point. Preserve the distinction between source support, our adaptation,
conditional assumptions and unproved applied validity.

No simulator or reference-evaluator code, executable traffic tests, numerical
rollouts, AD/JVP/FD checks, optimization, training, calibration or SUMO is
part of this review. No run configurations, numerical pass tolerances,
optimizer/query budgets, implementation file plan or environment milestone
is needed. Document/link checks are housekeeping, not traffic evidence.
Illustrative numerical defaults remain illustrative; this plan freezes no
experimental configuration.

**Output and completion gate.** Produce one readable findings memo centered
on the model that can be formed and why its interfaces fit. Include a compact
source/adaptation map, assumption/claim limits, direct VC1–VC3 conclusions
and a proportionate response to the complexity concern. Add mathematical
support only where a new derivation is necessary, retaining PDF/LaTeX for
substantial mathematics. Do not replace the accepted report by default.

At JM1, state what is methodologically qualified, under which assumptions,
which claims still need future empirical evidence, and whether any specific
methodological choice remains unresolved. Review completion does not depend
on positive experimental results. Numerical
correctness, gradient usefulness, calibration and transfer remain future
evidence obligations, not unfinished items in this review. The old report
and Step 4 closure, separate historical acceptance records, closed ramp line
and urban work retain their status.

**Completion record.** The user accepts this corrected plan and requests
execution. VC1's analytical audit and VC2–VC3 are complete at JM1 without
a new methodological choice. The findings and analytical addendum are
delivered for user review. This approved plan records the scope of that
completed pass; no implementation or later review begins automatically.

[Existing complete model and analytical qualifications](vsl_joined_candidate_contract_and_qualification.pdf)

[Scope correction and preservation record](../../reporting/research_readiness/vsl_methodology_scope_correction_work_report.md)
