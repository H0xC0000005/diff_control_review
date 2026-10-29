# RM12 planning revision — a bounded next question before R

Date: 2026-10-06. **Proposal only; successor execution and R adoption unapproved.**
Its initial priority is superseded by the
[four-position backtracking comparison](rm12_20_backtracking_point_comparison.md).
This remains the available BP-M task/control admission proposal, not the default
escape from information sufficiency. It originally superseded the recommendation in the
[earlier backtracking check](rm12_00_post_c_backtracking_plan_check.md).
RM9/RM10/RM11 closures and evidence grades remain unchanged.

## Why the previous recommendation was too broad

The user correctly observes that R — finding a representation that preserves
useful control gradients — resembles the overall research objective. R specifies
a possible change in the claim being tested, but does not itself specify a finite
review question, evidence obligation or stopping rule. Calling R the next stage
without those boundaries was insufficient planning.

R remains a possible umbrella direction. It would test model adequacy against
declared strong reductions, rather than prove irreducible missing information
under an ideal full-history controller. That claim change remains a user decision.
There is no need to adopt it merely to audit whether a physical control task has
the required leverage in the first place.

## Available bounded question under BP-M

**Does source-supported discharge recovery at one freeway merge provide a
credible ramp-rate control task whose benefit survives complete traffic-time
accounting?**

Semantically: temporarily holding ramp traffic can delay some travelers. The
candidate mechanism is that reduced merging interference permits downstream
discharge to recover. The review must determine whether the resulting exit-time
changes can compensate for the holding delay, including ramp and external waiting
through eventual clearance. Merely moving a queue to the ramp, increasing a mean
capacity number, or reporting more exits at one arbitrary horizon is insufficient.
No claim is made that the restrictive policy is universally beneficial.

This is one necessary task-admission question. It does not seek minimum traffic
resolution, a hidden-history pair, or validated gradients in the same pass.

### Existing support and the precise missing piece

- **Physical/intervention lead:** RM0014 Sections 3–4 connect metering changes
  to shoulder-queue reduction and temporary discharge recovery. RM8-P01 Sections
  2–4 give a lane-stream/acceleration mechanism. Their prior selected-method
  extraction is [here](extraction/rm8_source_studies/isolated_merge_and_hybrid.md).
  This supports the candidate mechanism, not a complete all-stream delay claim.
- **Strong compact rival:** RM0003 Section II.B models density and congestion
  memory; Section IV discusses restriction, recovery and subsequent operation.
  It supplies a public dynamic alternative and evidence that horizon matters.
  Its controller, source topology and finite-horizon objective must not be
  silently identified with the approved single-ramp open-loop clearance task.
  [Primary paper](https://arxiv.org/pdf/2106.10347).
- **Later representation lead:** S12A005 Section 5/Figure 5 distinguishes mean
  capacity approximation from heterogeneous transient flow. Different flow
  curves do not yet establish different useful common rate actions under complete
  TST. This is a lead for the second checkpoint, not the first checkpoint's proof.
  [Author manuscript](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6).

RM10 already closed the stronger joined hidden-history/action admission question
negatively within scope. Its [product matrix](reporting/rm10/rm10_70_findings_and_conclusion.md)
also explicitly leaves a validated finite-storage/rate adaptation unestablished.
The proposed pass separates that task/control obligation from the failed stronger
information obligation. It does not repeat the completed broad recovery search
or present existing physical evidence as a new positive discovery.

## Immediate model-chain boundary and output

Start with the previously reviewed local discharge-recovery source family,
RM0014/RM8-P01. Use RM0003 as a compact dynamic cross-check. These are distinct
source models, not ingredients to splice into an invented favorable law.
The output is **one task-admission record or one explicit rejection/gate**, with:

1. A genuine operational setting, source-supported recovery mechanism, public
   inputs/initialization, actual meter mapping and common feasible rate actions.
2. The causal chain from commanded rate to actual ramp entry, merge discharge,
   cumulative exits and all-stream time spent in the system.
3. A source-supported or transparent conditional analytic comparison of two
   feasible rate schedules, accounting for ramp/external waiting and clearance.
   Identify source statements, analytic consequences and adaptation assumptions
   separately. A favorable discharge response alone cannot pass.
4. The strongest relevant compact alternative and the exact remaining obligation
   that a later representation review would need to test.

Known fine initialization may be used to check this physical control leverage;
that does not establish a hidden-information advantage. Keep sensing/history,
public inputs, continuous mass, conservation, receiving/storage and complete TST
contracts. Rate control does not automatically imply coarse release timing.
If a conservative task needs a new boundary law, demand regime, storage rule or
actuator assumption, state it and stop for its methodological decision. Do not
invent private forcing, remove measurements, add lanes or suppress competing
memory merely to make a positive result possible.

The pass is source/analytic review only. It does not run a traffic simulation,
optimizer, numerical derivative or richer-reference experiment. It follows the
nearest already reviewed recovery frontier; it is not a new all-freeway search.
If that frontier cannot supply a defensible transfer, report the gap and stop.

## Candidates for the immediate checkpoint

**Problem:** which finite obligation should precede a representation study?
**Model-chain function:** establish a physical task in which common rate actions
can affect complete traffic time, before asking which state best preserves that
response. **Core gap:** the earlier evidence supports recovery and some control
effects but does not establish the approved complete-accounting task together.

These are RM12 target choices L/D, distinct from the closed RM10 A and RM11 C.

**Candidate L — task/control leverage audit first (recommended).** Review the
single local recovery mechanism and produce the admission record above.
**Pros:** resolves a named missing prerequisite; reuses completed evidence;
can stop with a compact-model or negative result; does not require R adoption
or a new hidden-state construction. **Cons:** does not answer representation or
gradient questions; complete TST transfer may remain conditional or need a gate.
**Dependency/consequence:** an admitted task enables, but does not approve, a
separate representation comparison.

**Candidate D — transient representation comparison first.** Compare a mean/
compact dynamic closure with retained recovery state using the reviewed transient
lead, while recording task/action usefulness as unresolved.
**Pros:** directly targets the physical detail most plausibly lost by reduction;
could establish dynamic closure inadequacy even with known initial state.
**Cons:** a flow-prediction difference may have no useful rate-control consequence;
the task/accounting gap can invalidate an eventual control interpretation.
**Dependency/consequence:** needs an explicit representation-fidelity claim and
fair comparator contract; it cannot inherit a positive hidden-history conclusion.

**Within BP-M, provisional recommendation: L before D.** It resolves the missing
task/control link before a transient representation comparison. The subsequent
four-position screen withdraws BP-M's fixed priority: neither L nor D is selected
as the overall next step. D is not a parallel search or automatic fallback.

## Finite stopping rules

- **Admit:** a defensible local rate-action/task chain shows a regime in which
  exit-time changes can outweigh all counted holding costs. Report its assumptions
  and limitations; proceed to a separate representation/claim decision only after
  user review. This is a task/control result, not the core research answer.
- **Negative:** the inspected transfer offers only queue relocation, stationary
  mean capacity, an unconnected throughput result, or no defensible complete-TST
  rate comparison. Close this bounded admission question without claiming
  impossibility for every ramp task.
- **User gate:** a concrete new law, initialization, sensing, demand/storage or
  actuator contract is necessary. Describe the smallest amendment and stop.

## Proposed decomposition — three conditional checkpoints

1. **Admit the rate-control/discharge-recovery task.** Resolve the bounded
   question above; output one task record, rejection or methodological gate.
2. **Test the relevant dynamic reduction.** For an admitted task, ask whether
   density plus a credible compact recovery/memory closure captures the
   rate-sensitive exit-time response, or which additional local state is needed.
   Mean-capacity agreement alone is not dynamic closure. Before starting, choose
   the intended representation-fidelity or strict-information claim explicitly.
3. **Specify sensitivity and validation obligations.** Only for a surviving
   consequential representation difference, identify the gradient/event path,
   rival closures, ablations, derivative checks and independent one-step
   usefulness test. The review writes a research plan; it does not perform those
   experiments. Sufficient compact models remain an admissible outcome.

This decomposition applies if BP-M is selected. Checkpoints 2–3 are conditional
planning context; choosing a backtracking position now precedes this sequence.
No full R programme or automatic move to T, incomplete initialization or
multi-ramp control is opened.

## Ownership, dependencies and status

| ID | Question/work | Classification and owner | Dependency/status |
|---|---|---|---|
| G1 | Select the bounded immediate target L or D | Type 2; user | Proposed, unapproved |
| E1 | Extract source action/recovery/domain contracts | Type 1; reviewer | After G1 selection; reuse prior extraction first |
| E2 | Audit complete accounting and conservative source transfer | Type 1 within unchanged contracts; reviewer | E1; any scientific amendment escalates to G2 |
| G2 | Adopt any necessary law/task/interface amendment | Type 2; user | Triggered only by a concrete E1/E2 conflict; no silent adaptation |
| G3 | Adopt R or retain strict information necessity; freeze comparison | Type 2; user | Before checkpoint 2; not resolved by a checkpoint-1 positive |

The mixed transfer question is split into E2's evidence/accounting audit and
G2's methodological adoption. Global target selection precedes dependent evidence
execution. This inventory is conditional on BP-M; the current selection gate is
RM12-BG1 in the four-position comparison. Planning documentation alone adopts
neither a backtracking point nor an executable successor.
