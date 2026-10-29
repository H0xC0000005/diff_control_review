# Pilot downstream-task taxonomy

Status: approved at T3 and refined into the T5 shortlist on 2026-09-10

## A. Primary family: fixed-time green allocation

The leading family optimizes continuous green/service allocation under fixed phase topology. It divides into two meanings that must not be conflated:

1. **Effective-service allocation:** continuous fractions scale movement capacity over a horizon or cycle. This is the smallest derivative contract and matches the current project boundary.
2. **Realizable timing:** fractions or durations are converted into an executable phase plan with cycle, minimum-green, yellow/all-red, and interval constraints.

The review must decide at T5/T6 which meaning supports the primary claim.

## B. Diagnostic scenario layers within the primary family

1. **Aggregate-equivalence layer:** homogeneous or mechanism-disabled setting; proposed and macro models should agree.
2. **Finite-pocket layer:** pocket storage fills and changes attainable discharge or spillback.
3. **Access/order layer:** aggregate-matched states differ in movement order or pocket accessibility and therefore in realized service.
4. **Combined and held-out layer:** demand, pocket length, order, and initial queue vary without changing the task definition.

These are intended as one experimental suite, not four unrelated optimization topics.

## C. Model and comparison roles

- differentiable homogeneous LTM;
- structured movement/turn queue;
- lane/storage-aware aggregate;
- proposed selective-discreteness differentiable model;
- identity/order richer forward reference;
- microscopic evaluator such as SUMO; and
- optimizer-only comparators under a fixed model and budget.

Representation comparisons and optimizer comparisons are separate axes.

## D. Supporting task families

- diagnostic gradient-direction perturbation before full optimization;
- short-corridor green allocation with interacting spillback;
- multi-fidelity optimization using low- and high-resolution simulators;
- robustness across stochastic demand and microscopic seeds.

## E. Later conceptual families

- directly realizable signal-plan optimization if the primary task remains service-level;
- cycle length or offsets once within-cycle and lost-time effects are represented;
- actuated control or continuous controller parameters;
- calibration or demand estimation using mesoscopic sensitivities;
- network design or pricing where local blockage changes gradients.

These remain conceptual and do not expand current project scope.

## T3 decision

The five-part taxonomy was approved on 2026-09-10 as the basis for full-text extraction, including the separation between effective service and realizable timing and between representation and optimizer effects.

## T5 synthesis outcome

The evidence supports treating fixed-topology effective-service allocation as the recommended primary family; the four diagnostic layers remain one suite. Gradient-direction perturbation is an embedded evidence stage, directly realizable timing is the first later task, and a short arterial is the first spatial extension. This outcome remains provisional until the T5 user gate closes.
