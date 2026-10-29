1
"
Hi Peizhu, 

I have reviewed LTM and compared it with other models as well. I think LTM is a good choice as a base model for differentiable simulation model and traffic light control. You can read the paper as follows, 

https://ieeexplore.ieee.org/document/8845756
https://ieeexplore.ieee.org/document/8370049
This team has a strong background in transportation research, and I have read a lot of papers from them before. 
I have some suggestions here. 
Topic 1: Compare LTM-based control with differentiable LTM-based control.
First, reproduce the LTM-based MPC approach in the first paper, then compare it with an approach based on a differentiable LTM. We can evaluate whether differentiable simulation offers benefits in control performance and computational efficiency.
Topic 2: Signal control for blocking caused by limited turning-lane storage.
For the blocking scenarios, I suggest starting with a dedicated turning lane or pocket with limited storage. The initial focus should be on improving signal control using an established queue and storage representation, rather than developing a general road-blocking model.

Please let me know if you need more clarifications. 

Best Regards,
Wang Yu
"

2
"
Hi all,

I think Wang Yu's suggestion can help us clarify the research landscape a bit more. It looks like topic 1 ("compare LTM-based control with differentiable LTM-based control") might have been covered already (https://arxiv.org/pdf/2604.11380). They state that LTM itself is amenable to to plain AutoDiff, with a minor adaptation related to the time steps. From a CS perspective, that makes it pretty straightforward. A little more effort in that paper is spent on the incremental node model (INM) that can handle multi-leg  intersections, and DUO for route choices.

Combining that with Wang Yu's topic 2, the overall line of thought might look like this:
Gradients accelerate convergence to high-quality solutions for LTM-based control (Fig. 18 (a) in the above paper)
LTM is inaccurate if blocking because of limited turning-lane storage dominates
The most well-accepted simple model that accurately models this sort of blocking is not trivially differentiable
We propose a differentiable variant of this model and demonstrate that gradients accelerate convergence to high-quality solutions here as well

Wang Yu: is this in line with your thoughts for topic 2?

Best,
Philipp
"

3
"
Hi Peizhu and Philipp,

 

Yes, correct. Topic 1 appears to have already been addressed. What surprised me is that, in the first of the two papers mentioned in my previous email, the optimization outputs are effective green-time fractions rather than directly implementable traffic-signal control variables. These fractions are then used as high-level reference targets by the lower-level signal controller developed in the second paper.

 

For Topic 2, the limited turning-lane storage scenario was intended as an initial test case rather than the entire research topic. The idea is aligned with Philipp’s overall line of thought. Meanwhile, what I want to emphasize is that, it is difficult to develop a general-purpose model that can accurately represent different forms of road blockage in transportation networks.

Therefore, for an initial study, could we first focus on queue spillback and lane blockage caused by limited turning-lane storage? This scenario is more tractable because it has a clearly defined physical mechanism. We could formulate it as a differentiable model to predict the evolution of blockage, and then use its gradients to optimize traffic-signal control to prevent or mitigate the blockage.

 

Best Regards,

Wang Yu
"

4 (my email)
"
Hi Philipp and Wang Yu,

I think we have a mutual agreement here regarding the scope of the project target and the first set of tasks as the design anchor.
For Philipp, I think your points capture the initial purpose of my project proposal very well (though it is not well defended, but that is the job of detailed proposals). I think a similar project objective is also mentioned in the report (differentiability as the primary target, bridging the non-differentiability of a meso model with similar modeling capability as a secondary method anchor). 
And the reason that I directly apply LTM for far upstream traffic is that it was established in Seo's work (actually a series of papers), and I can borrow their formulation unmodified.
For Wang Yu, while I agree with your claim that blockages are hard to model (as I saw exactly in the microscopic sense), I think the primary concern with blockage modeling is that "the proposed stack can model the correct gradient of a set of traffic engineeringly sound blockage behavior", not modeling a full-coverage set. I planned to model the blockage first in my previous project plan, but (during the last presentation) I tried to claim more than an essential set of blockage behavior to model. I will work on a clean task definition of a first set of blockages I should model and how the behavior from them is causal in the corresponding tasks.
Meanwhile, I am working on defining the tasks that the project should be validated on, as well as the baselines to compare, and adopting your ideas into well-defined and executable task plans. That is the other way around compared to my previous model-first approach, yet after some reviews, I think defining all the anchors and pillars clearly helps to build a well-established foundation in the literature. So I will spend more time on these foundation works before next week.

Best,
Peizhu.
"