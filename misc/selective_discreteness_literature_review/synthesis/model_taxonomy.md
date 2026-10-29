# R8 model taxonomy

Date: 2026-09-07

The 37-study corpus is best understood by implemented state and derivative mechanism, not by authors' macro/meso/micro labels.

| Family | Representative studies | Traffic state and order | Differentiation position | Relevance to the project |
|---|---|---|---|---|
| Continuous aggregate LWR/LTM/node | Yperman; Tampère et al.; COS; Seo | continuous cumulative mass; aggregate FIFO/commodities | analytic or reverse AD is natural through continuous operations | inherited scalable backbone and macro baseline |
| Stochastic differentiable aggregate DNL | Osorio, Flötteröd, Bierlaire; Flötteröd and Osorio | queue-length distributions and probabilistic link boundaries | smooth analytic mappings | establishes that differentiable spillback DNL predates modern AD; no exact semantic order |
| Smooth learned DNL surrogate | Song et al. | learned delay operator over aggregate inputs | closed-form smooth surrogate derivatives | explicit accuracy/differentiability trade-off; not a derivative of the original simulator |
| Partial-FIFO and multi-commodity node | Wright et al.; LNCTM | continuous commodities and parameterized movement restrictions | generally not differentiated in the paper | strongest aggregate alternative to exact order |
| Lane/movement queue models | Gong–Bliemer–Raadsen; Wei et al.; Gao; Liu–Chang; Shiomi et al. | lane, lane-group, or movement aggregates; physical queues/storage | analytic or black-box optimization, not end-to-end simulator gradients | proves lane allocation, blockage, and finite storage are established components |
| Integer/event mesoscopic LTM | de Souza et al.; LIFT; SUMO alternative | persistent vehicles/events and exact realized sequence | not differentiated | closest forward identity/order references; contrasts with divisible mass |
| Packet/individual mesoscopic signal simulation | TRAFFMED; MESCOP; DTALite | packets or individuals under aggregate movement rules | metaheuristic/black-box optimization | establishes mature mesoscopic control/evaluation tasks |
| Differentiable microscopic agent model | Andelfinger; TrAAD; parallel differentiable IDM | individual vehicles and explicit trajectories/order | smoothing or reverse AD | retains rich state at larger graphs or altered discrete logic |
| Differentiable micro/macro hybrid | Son et al. | mixed macro and micro state with conversion | reverse AD across representations | nearest multiresolution architecture; deferred experimental comparator |

The unoccupied intersection in this corpus is not “mesoscopic plus differentiable” broadly. It is the narrower combination of divisible traffic mass, persistent exact semantic order, localized lane/storage state, derivatives of the implemented traffic model rather than a learned surrogate, and external evidence that the resulting decision direction is useful.
