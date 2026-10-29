# RM7 method-first candidate task matrix

Date: 2026-10-01. Status: **RM7-UG1 closed; F1/Candidate A approved.**

The user retained F3/Candidate C as a possible future extension after positive
local results and a separate decision. F2 remains unselected. The matrix below
preserves the task-selection comparison; see the
[decision record](../discussion/rm7_candidate_a_approval_and_extension_record.md).

| Criterion | F1 — local merge opportunity | F2 — downstream route access | F3 — coordinated local merges |
|---|---|---|---|
| Infrastructure action | One meter; continuous rate or fixed-shape release schedule | One meter; same action affects downstream composition/timing | Multiple continuous meters or coordinated policy parameters |
| Candidate hidden information | Target-lane occupancy, usable merge opportunity, lane-change/relaxation stage, local order or gap distribution | Local route-access order, exit-lane occupancy and pocket/spillover state | Per-merge hidden states plus corridor propagation |
| Strong macro comparator | Mainline totals, ramp queue, finite storage, aggregate merge/capacity state, multiclass variants | Destination-aware/FIFOQ route memory plus storage/spillover | Coordinated CTM/METANET, buffers, fairness and MPC |
| Minimum-state ladder | Aggregate → merge-pressure scalar → lane group → finer local merge state | Aggregate → route/time cohort → lane/storage → residual order | Aggregate corridor → local scalar states → lane-resolved zones → richer reference |
| Isolation quality | High: one action and one merge directly connect hidden state to service | Medium: downstream geometry adds propagation and route-composition confounds | Low initially: coordination and network effects obscure local attribution |
| Gradient motivation | Meter action directly changes arrivals to the merge; later sensitivity path is compact but nontrivial | Long action-to-effect path tests metadata propagation | Strong scaling motivation from many controls; already mature at macro level |
| Independent evaluator | Microscopic or hybrid merge reference can expose lane/gap behavior | Destination-aware lane/microscopic downstream restriction | Corridor meso/micro or multiresolution evaluator |
| Main risk | Aggregate-plus-scalar state may be sufficient; gap state may be nonsmooth or difficult to match | Repeats ordered-service hypothesis or is absorbed by route-aware models | Scientific signal lost among coordination, forecasting and fairness choices |
| Initial disposition | **Recommended first task.** | Retain as alternative/extension. | Retain as later extension after local mechanism is established. |

## Recommended F1 formulation

- **Geometry:** one controlled on-ramp, finite ramp storage, a multilane mainline
  and a local merge/acceleration region with downstream recovery space.
- **Action:** one common infrastructure metering release schedule; no direct
  vehicle, route, lane-change or speed action.
- **Observer:** complete declared road-total mainline and ramp-queue history,
  known demands/geometry and future forcing, without lane/gap decomposition.
- **Candidate hidden state:** local merge opportunity, including target-lane
  occupancy and whatever lane/gap/relaxation state a later evidence review finds
  minimally necessary.
- **Primary outcome:** all-stream total system time/delay through common
  clearance. Throughput, ramp spillback, safety/feasibility and residual demand
  are secondary metrics or guardrails.
- **Research ladder:** strong aggregate/multiclass baseline; compressed merge-
  pressure augmentation; lane-group/local mesoscopic candidate; independent
  richer reference.
- **Core question:** what minimum local merge information is needed for a model
  to predict useful ramp-metering perturbations under otherwise matched inputs?

This is a task contract for review. It does not select the richer model or assert
that the hidden-state pair, action distinction or gradient exists.
