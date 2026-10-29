# Short version: impact on M2 and later milestones

Date: 2026-09-14
Basis: accepted T7 impact classifications, including revised M3 ownership of service-order resolution (P8).

The review gives development a concrete target: allocate four effective-service fractions at a four-leg junction, minimize clearance-complete total system time, and test which retained order/access/storage information improves decisions through V0–V4. The milestone structure remains usable; the main changes are clearer interface obligations, stronger baselines, and an earlier external perturbation check.

| Milestone | Practical effect of this review |
|---|---|
| **M2 — interaction-zone infrastructure** | Keep the agreed scope. Before Phase C, ensure lane/scenario interfaces, conservative mass accounting, continuous gradient paths and comparison seams can support the later task. Expose enough state to count moving and queued traffic once for TST. Use neutral cases to verify equivalence; shared-lane blockage and bay behavior stay with M3. |
| **M3 — lane/storage/access and service** | Define the actual operators needed by V1–V3. M3 chooses exact FIFO or approved bin-level homogeneity and defragmentation, specifies what order is retained, and establishes conservation, resolution effects and local derivative evidence. Update the task's detailed operator/claim wording to match the chosen design. |
| **M4 — sensitivity study** | Validate the complete service-to-TST gradient and compare homogeneous, movement-queue, lane/storage and selective-order representations. Use V0 equivalence and separate order/storage cases to explain gradient differences. Arrange the bounded external perturbation check before full optimization. |
| **M5 — optimization** | Optimize the shared effective-service/TST task using validated gradients. Keep representation comparisons separate from optimizer comparisons; freeze budgets and scenario splits, keep paired order cases together, and evaluate held-out V4 cases. |
| **M6 — richer-simulator transfer** | Evaluate final actions and held-out usefulness in the richer simulator. Prepare the common service-to-signal mapping and a small perturbation evaluation earlier, before full M5 optimization; the complete transfer campaign remains here. |

M1 is retained. Exact numerical settings are calibrated after the relevant interfaces exist and frozen before confirmatory evaluation. V5/I1 and the unapproved future-task map are outside this review's accepted scope.

These are accepted planning implications, not edits to the authoritative milestone plans or permission to begin implementation. See `project_impact_matrix.md` for owners, timing and evidence obligations.
