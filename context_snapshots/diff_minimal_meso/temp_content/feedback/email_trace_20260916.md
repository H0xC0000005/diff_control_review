## 1 (sending the report to colleagues)
Hi Wang Yu and Philipp,

The attachment is a brief report on the feasibility of treating ramp control as the primary task or as a second parallel task.
Since I don't have any literature knowledge in this branch, I adopted a feasibility study straightaway and went for the essential literature work only when necessary. Nevertheless, I think the current review findings are sufficient to reject ramp control as a primary task, and thus it should not affect the discussed task formulation and implementation plan. 
I appreciate your questions and further ideas because I may miss some important points due to a lack of branch knowledge. If this remains closed, I plan to revise the plan according to last week's review and the task formulation results and continue development.

Best,
Peizhu.

## 2
Hi Peizhu,

It's a bit hard to figure out from the somewhat cryptic LLM-generated text, but it seems to me that the argumentation takes your model as the fixed starting point, and then says that if the task is made to be compatible with your model (not the other way around!), there's no scientific vlaue. My understanding from the previous discussions was that we're trying to take the opposite approach, which is to start from the task and then see what is required on the model side. If we start from the model, it's a "solution looking for a problem" setup, which doesn't always work out...

Let's wait and see what Wang Yu thinks of this.

Best,
Philipp

## 3
Hi Philipp,

A quick response to your idea:
You largely capture the line of the review. While the missing pieces are two:
Freeway and Urban traffic have different definitions of "mesoscopic". I indeed tried to proceed by your proposed method (finding the common ground and updating the model design), but since they differ at this basic representation level, I think it is hard to find the common ground at all, so I went the other way. Moreover, (mentioned in the report but I would like to summarize that here), ramp control has strong macroscopic baselines, while the value of mesoscopic mainly lies on microscopic behavior, such as following dynamics, lane changing, evading behavior, and speed control; this is contradictory to the current project scope at the foundation level.
I also conducted a brief compatibility check for the common ground of the two tasks. The short conclusion: they can be compatible by implementing different node solvers (this is the least set to make the two tasks to use the same simulation), and mass grid dynamics (fine-grained freeway simulation has behavior such as lane changing all the way to the merging point so it needs specific handling at least). The core issue is that such construction cannot verify the mesoscopic stack against the macroscopic stack at all. 
So there's a gap between the modeling compatibility and the methodological compatibility and I cannot find a way to reasonably bridge it, and that's why I try to go from the current modeling design as the anchor point.
I hope this briefly addresses your concern.

Best,
Peizhu.

## 4
Hi Peizhu and Philipp,
I agree with Philipp that we should start by defining the tasks and the questions we want to answer, and then determine what is needed on the modelling side. The report is useful in identifying limitations of the current formulation, but I would not treat that formulation as a fixed constraint when evaluating possible tasks.
My understanding is that the broader aim is to investigate what insights differentiable simulation can provide for traffic control. Different tasks could require different model components or representations. That would be acceptable, provided that they support a clear, shared research question. We should also keep the modelling and validation effort in mind when considering the scope of the work.
For the expressway example, I had a more specific bottleneck scenario in mind. One or two lanes may become temporarily unavailable because of an incident or scheduled maintenance, such as tree pruning. Permanent lane reductions provide another related setting. Under low demand, the impact may be limited; under high demand, a substantial queue can form. Vehicles may continue moving through the bottleneck while the queue persists, and after a temporary closure ends, the queue may still take time to dissipate if demand remains high. There are two possible actions to mitigate this issue, 
Coordinated upstream ramp metering. This is an established approach, but its effectiveness depends on traffic conditions and available ramp storage. It also raises fairness questions about how delays are distributed between mainline and ramp users.
Connected and automated vehicles (CAVs). Another possibility is cooperative speed control based on CAV approaches. Similar control algorithms could potentially generate speed recommendations delivered through Singapore’s ERP 2.0 on-board units, with drivers implementing the recommendations instead of automated vehicle controllers. We could first explore this possibility in simulation.
The urban task also has room for a deeper investigation. The specific situation discussed earlier involves a short right-turn storage lane: if right-turn traffic is not served, its queue can extend into the through lane and obstruct straight-ahead traffic. This raises at least two sets of questions:
How can we reduce the risk of blocking? Building on the paper discussed earlier, we could examine effective green-time ratios. Explicitly accounting for the limited right-turn storage might also help identify an appropriate upper limit on cycle length under given demand conditions, or determine whether the right-turn movement should be served twice within one cycle.
What happens once blocking occurs? When right-turn vehicles obstruct a through lane, how does this affect the link’s throughput and travel time? What do the resulting sensitivities tell us about adjustments to the local signal and coordination with downstream signals?
At this stage, we would not focus too much on whether both tasks fit into a single paper. We can continue investigating both directions and assess how far each develops. Based on the findings and their connections, we can then decide whether to organise the work into one paper or two papers with distinct contributions.
Best regards,
Wang Yu

## 5
Hi Wang Yu and Philipp,

OK, in this case, let me put aside the current formulation first and go back to finding common ground between the two tasks again. But I am still worried about the ramp control because
I don't have much literature knowledge,
The ramp metering task seems to need a separate control task setting.
As you suggested that this path alone may have some distinct value if formed appropriately, I would spend the rest of this week (and probably not only this week) on this, starting with a broad literature review and a good candidate set of problem definitions for ramp metering first. So maybe I should discuss this with you more frequently.

Best,
Peizhu.