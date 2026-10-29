# R8 baseline map

Date: 2026-09-07  
Status: review recommendation, not an implementation approval

## Approved minimum comparison logic

| Rung | Scientific alternative controlled | Literature basis | Smallest defensible realization |
|---|---|---|---|
| 1. Homogeneous differentiable macro | any gain comes merely from using a different implementation rather than retained mesoscopic information | Seo's differentiable LTM; Yperman/Tampère/COS foundations; analytic stochastic DNL as historical context | matched internal macro baseline with identical demand, FD, node/signal parameters, objective, and optimizer budget |
| 2. Structured aggregate queue | movement totals or partial-FIFO restrictions suffice; exact order is unnecessary | Wright partial FIFO; Wei turn-level queues; LNCTM commodities | one matched movement-queue or partial-FIFO ablation/reference implementation |
| 3. Lane/storage-aware aggregate | lane allocation, lane-group queues, or finite storage alone explain the result | Gong–Bliemer–Raadsen; Liu–Chang; Gao; Wong–Lee; Shiomi | matched lane permissions/storage and aggregate lane/movement state without exact sequence |
| 4. Identity/order mesoscopic forward reference | proposed continuous ordered mass does not reproduce established individual/event mesoscopic behavior | de Souza individual LTM; LIFT; SUMO discrete-time LTM alternative | reference cases and, where feasible, an executable forward comparison; no gradient comparison is expected |

## Deferred comparison

Son et al.'s differentiable hybrid simulator remains a useful conceptual and possible small-case ablation, but the user deferred it from the minimum ladder. It cannot define a standalone project experiment and should be reconsidered only after Question B establishes a task that permits fair matching.

## Practical recommendation

The causal core should be implemented as internal matched ablations because no external package supplies the complete desired chain. External papers should be reproduced only at the strongest fair level: equations/reference cases for structured queues and lane storage, executable forward comparisons for individual/event mesoscopic LTM where feasible, and conceptual comparison where task or physics mismatches would make numerical ranking misleading.
