# RM10 information and action audit

Date: 2026-10-05. Reviewer deductions; source claims and access grades are in the
[primary audit](../../extraction/rm10/primary_source_audit.md).
The [mathematical companion](rm10_information_tst_and_gradient_audit.pdf) defines
history consistency, task accounting and the conditional gradient path.

## Source-grounded task envelope

The A envelope is a single-ramp freeway merge with bounded acceleration/recovery,
common public arrivals, geometry and model parameters, finite ramp/mainline
storage, a common bounded open-loop metering **rate** schedule, and complete
population time through clearance. Two mainline lanes remain the default aim.
Release permission is not actual entry flow: demand, travel and receiving can
limit entry. Metering moves waiting upstream and can alter merge discharge.
Both effects belong in the objective.

This is a comparison envelope, not a newly approved simulator equation. The
literature supplies physical families and reference laws, but no single inspected
source closes all these task contracts with the required information claim.
Do not splice stationary capacity equations into a transient CTM and describe
the splice as a source-validated task.

## Strong observer and history

Preserve exact aggregate cell inventory/density, separately supported completed
face flows/counts, available section speed, ramp inventories/history, public
inputs and past controls. For a non-equilibrium candidate, declare actual speed
support and averaging before making an identifiability claim. A stored section
mean speed, a face spot/time mean, and an equilibrium FD proxy are different
observations. The closed RM9 representative FD observer does not make physical
acceleration speed algebraic. No favorable averaging choice is adopted here.

The strongest simple aggregate candidate has homogeneous cell inventory and
mean-speed state, both exactly observed. If these and observed queues are its
complete state, there is no residual state hidden by that candidate's observation.
This is a conditional fact about that closed model; it neither verifies its
traffic fidelity nor proves observation sufficiency for heterogeneous lane speeds,
within-cell waves, multiple leader positions, or vehicle distributions.

## Comparison completed before an extra-state claim

| A family / competitor | Why it is a fair contender | Information conclusion | Task consequence |
|---|---|---|---|
| Density-only ordinary equilibrium CTM | Basic first-order reference | May omit recovery physics; failure is model inadequacy, not automatically missing information | Cannot be the only aggregate baseline |
| Modified aggregate demand or public flow-ratio/capacity relation | Recovery/drop can enter the public law | No extra hidden state **within a closed density/rate law** | Strong rival; stationary laws still need lawful transient/storage transcription |
| Density-history hysteresis mode | Captures different congested regimes | Known initial mode is reconstructible from admitted history; unknown initialization remains conditional | Mode retention alone is not necessity for selective information |
| Homogeneous aggregate density plus dynamic mean speed | Represents non-equilibrium mean motion | Exact observation of every state gives conditional sufficiency | Reject a hidden-state claim for this restricted model, not the whole A family |
| Lane/hybrid moving constraints or heterogeneous recovery distribution | Retains physical transients not guaranteed to close in a mean law | Full-history unresolved state is possible in principle but not established for this task | A physical lead survives; positive task admission fails without a lawful history/action certificate |

Neither an approximate good aggregate fit nor a nonzero reconstruction slope
proves exact global sufficiency. Conversely, adding a physically meaningful
variable does not prove it remains unknown after the controller reads its history.

## Why the residual lead does not yet yield a positive task

The most substantial residual possibility is **where traffic lies within a
recovery process**, including localized leaders/voids and a distribution of
recovery speeds. Equal mass and mean speed alone need not encode that distribution.
This is a snapshot possibility, not a constructed genuine freeway case.

Four successive obligations were checked:

1. **Lawful task and initial domain.** The richer family must specify initial
   traffic consistent with a real review setting and a common public population.
   Changing acceleration/truck proportions or random insertion sequences between
   cases is not an approved hidden lane-state comparison. Unknown positions or
   recovery states can be investigated only with their own source-grounded
   observation/history contract.
2. **Identical admitted history.** Different transient flows already visible to
   the controller do not furnish the required pair. The full history can also
   reconstruct a state absent from a snapshot. Known complete initialization
   continues to imply deterministic future sufficiency.
3. **Different useful common actions.** The same feasible rate schedule must be
   compared under all-stream TST. A changed discharge, a parameter sensitivity,
   a better mean-capacity fit or different performance under one policy is not
   enough to show different useful directions or policy rankings. It is possible
   for richer states to affect prediction while retaining the same best action.
4. **Gradient of that comparison.** Rate changes must traverse release, actual
   entry, recovery, receiving/conservation and exit timing. Events and queue caps
   cannot be frozen or smoothed merely to obtain derivatives. A derivative of
   mean capacity with respect to acceleration is a different derivative.

The inspected rich-family evidence reaches physical forward effects, but does
not supply obligations 1–3 together. Consequently no specific retained state is
admitted as *necessary for useful ramp-rate gradients*. This obstruction occurs
before numerical gradient testing; running SUMO would not repair the missing
methodological comparison by itself.

## Complete A conclusion and its limits

**Scoped negative task admission:** no source-supported A task in this inspected
envelope has passed the full strong-history/useful-action requirement. The
aggregate-law, known-mode and completely observed homogeneous-state subclasses
have explicit conditional sufficiency explanations. The distribution/leader
subclass has physical support but insufficient task-level evidence, not a proof
of impossibility. It must not be silently promoted on that physical support.

This completes the bounded A review under its stated negative-admission rule.
It does not assert that every acceleration-aware task is impossible, that mean
capacity approximations are exact, or that all detailed models are redundant.
A fresh positive reopening would need a genuine initialization/observation domain
and source-grounded rate/TST certificate addressing the four obligations; a
larger literature pile alone is not a changed conclusion. Candidate C is held
outside this review, including during the residual-lead audit.
