# RM10 Option A — completed review and admission conclusion

Date: 2026-10-05. **Closed by user acceptance: scoped negative admission for
the proposed core-question task.** See [closure](rm10_99_user_closure.md).
The subsequent C/alternatives planning check is authorized; no substantive task C
review or experiment is opened.

## What the conclusion means

Acceleration/recovery is a defensible physical mechanism at freeway merges.
However, the inspected A families do not yet establish a task in which information
missing from the admitted **aggregate mass, flow, speed and full history** changes
useful common ramp-rate actions. A is therefore **not admitted as a positive
selective-information/gradient task on this evidence**. This completes the A
review; it is not a recommendation to continue the same search indefinitely.

The negative has two distinct bases. Some restricted models have conditional
information sufficiency: their relevant state is observed or reconstructed from
known initialization and history. Richer recovery models have physically relevant
state, but lack the combined genuine-task/history/action evidence. The second
finding is insufficient support, not a universal impossibility theorem.

Clarification after user discussion: a complete physical traffic model is not
what was shown impossible. The unestablished chain joins physical mechanism,
unresolved information under the full observation history, useful common rate
actions, and useful gradients. Source-backed additions to an LWR/CTM backbone
are not automatically artificial assumptions. Known **complete** initialization
with exact deterministic public dynamics is different from knowing only initial
aggregate statistics; only the former supplies the conditional sufficiency claim.

Read the [information/action audit](../../synthesis/rm10/information_and_action_audit.md)
for assumptions and the [four-page mathematical companion](../../synthesis/rm10/rm10_information_tst_and_gradient_audit.pdf)
for task accounting, information consistency and gradient derivation. The
[primary-source audit](../../extraction/rm10/primary_source_audit.md) records
selected sections, exact versions and access limits.

## What A actually added beyond RM9

A introduced non-equilibrium **recovery physics as a candidate family**, rather
than another equilibrium lane-count construction. Its review envelope remains
single-ramp, bounded open-loop rate control, finite storage/receiving and
all-stream TST through clearance. Public inputs and observations remain strong.
No new physical law or favorable sensor/initial-state choice was adopted.

The old RM9 equilibrium speed proxy is not used to erase acceleration state.
Actual non-equilibrium speed needs its own declared support and averaging.
Stationary capacity relations, observed dynamic mean speed, reconstructible
hysteresis, and local moving constraints were examined as distinct mechanisms.
Compatibility with current project implementation played no role in admission.

## Evidence and inference matrix

| Claim ID | Completed finding | Evidence / logical basis | Status for the core task |
|---|---|---|---|
| RM10-C01 | Acceleration and resulting recovery can affect merge discharge | RM8-P01 and RM0011 inspected hybrid mechanisms; source audit | Physical family supported; not sufficient for hidden information |
| RM10-C02 | Recovery need not require extra retained identity/state in every model | RM9-L03's density-dependent demand; RM10-P01/P02 effective-capacity laws | Stronger aggregate rivals required; their source domains do not automatically validate a transient ramp task |
| RM10-C03 | Known hysteresis memory is not hidden from full density history | RM0003 Section II.B plus induction from its stated initial mode | Conditional negative for that known-initialization subclass |
| RM10-C04 | Observing the complete homogeneous aggregate density/speed state leaves no unknown model coordinate | Conditional state-observation argument, mathematical companion Section 2 | Negative within that closed model; no adequacy theorem for heterogeneous traffic |
| RM10-C05 | Mean-capacity agreement can coexist with different transient traffic | S12A005 Section 5/Figure 5; approximate mean-law comparison | Richer transient lead survives; differing observed flow histories do not furnish the required hidden-history pair |
| RM10-C06 | The term macroscopic does not guarantee absence of local retained state | RM10-P04 Section 2 moving constraints; its full initialization fixes leaders from density jumps | Supports a selective physical family; no coarse-history identifiability or ramp-rate TST certificate transferred |
| RM10-C07 | Discharge benefit or different prediction is not enough to establish different useful actions | Complete-population balance and common-policy comparison; mathematical companion Sections 1–2 | Equal exits imply equal TST; no joined full-history/action certificate established |
| RM10-C08 | A conditional gradient chain can be specified without claiming verified/useful gradients | Mathematical companion Section 4; existing RM0024/RM0025 evidence boundaries | General path established conditionally; specific task correctness and independent usefulness remain unestablished |

In particular, [S12A005](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)
is useful evidence on both sides: its mean-capacity approximation is a serious
aggregate competitor, while its transient comparison prevents us from treating
mean agreement as exact dynamic sufficiency. This does **not** close the strong
history question in either direction.

## Where the strongest remaining lead fails admission

Localized recovery position, leader/void state or a recovery-speed distribution
could contain more information than a snapshot mean. To admit that as the current
research task, the review would need a source-grounded initial traffic domain
and lawful dynamics producing unresolved state after **all** admitted past
observations, followed by a demonstrable difference in useful **common feasible
rate actions** under complete TST. No inspected study or sound source transfer
supplies those obligations together.

The obvious replacements are not valid certificates: queued versus unqueued
ramps differ in known ramp observations; heterogeneous transient flow curves
differ in known flow observations; changing public acceleration/population
parameters changes the problem; changing future stochastic realizations changes
forcing; differentiating stationary capacity changes neither a common finite
queue task nor its complete TST gradient. We did not use any of them as rescue
assumptions. Nor does known deterministic initialization become hidden simply
because the model now contains more physical variables.

The result is narrower than “there is no hidden information in freeway traffic.”
Unresolved within-cell/per-lane recovery state and partially known initial
histories are not ruled out. They remain **hypotheses requiring a new concrete
certificate**, not a current positive conclusion. An accurate compact recovery
model could also be useful for control for reasons independent of selective
information retention.

## Review products and question closure

| Question/product | Outcome | What remains outside the established result |
|---|---|---|
| G1: physical task mechanism | Completed, family-level positive | A validated adaptation binding all finite-storage/rate contracts |
| G2: strong aggregate competitors | Completed, conditional sufficiency and source-domain audit | Exact closure for heterogeneous local recovery is not proved |
| G3: genuine hidden state changing useful control | Completed, scoped negative admission | A lawful full-history/action certificate; not merely simulation measurements |
| G4: general gradient concepts | Completed as a conditional derivation | Specific nonsmooth/event sensitivities, reference correctness and independent usefulness |
| G5: disposition | Closed by user acceptance | C/alternatives planning check authorized; no automatic task adoption |

This result ends the authorized bounded A pass. It does not defer an already
available positive task to experiment, and it does not use missing numerical
experiments as the reason for rejection. The missing methodological certificate
occurs earlier. There is no need to install/run SUMO to reach this conclusion.

The completion rule was scoped task admission, not exhaustive proof across all
possible acceleration laws. The logged nearest-source frontier was reviewed;
an unavailable abstract-only source is not counted as failed full methods or
used to prove absence. No outstanding in-scope source transcription was left
as a pretend user decision.

## Current gate and next allowed action

RM9 is properly closed with the scoped result under UG5.A. RM10 is now closed
by user acceptance. The user requests a check of C and alternatives before
the next substantive review. That planning check is authorized, without
automatically opening C, B, an experiment or simulator development. C was not
involved during the A pass.

The [work report](rm10_99_work_report.md) lists changed files, commands,
verification and remaining limits.
