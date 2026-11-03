# How speed advice changes total system time in the literature-backed VSL task

Higher speed advice directly relaxes the restriction on sending traffic.
It can shorten travel, but it does not directly increase receiving capacity
or improve merging priority. Whether faster movement subsequently relieves
or worsens congestion depends on the traffic state. The model therefore
allows competition between faster travel and congestion management; it does
not guarantee that lower advice is beneficial or that an intermediate
advice is optimal.

The setting is a three-to-two lane drop: E is the ending lane, A the adjacent
continuing lane, and B the farther continuing lane. A finite cohort is
initialized independently of one common, constant advice applied throughout
the road. No later traffic enters, and downstream congestion does not block
the outlets. Total system time (TST) counts every initial unit's time until
it exits, including all waiting and the complete remaining travel time.
The causal interpretation below follows the established lane-cell model
and its analytical qualifications [1], [2].

## 1. What changes immediately when advice increases?

First compare two advice values at exactly the same lane-cell traffic
state. This separates the direct effect of advice from the congestion
changes that may develop afterward.

| Factor | Direction of change | Meaning for movement and TST |
|---|---|---|
| **Sending offer:** how much traffic a cell offers to move | **Nondecreasing:** increases for nonempty cells limited by advice; unchanged where the discharge ceiling already binds | More traffic can move if receiving service is available. An increased offer is not a guarantee of increased realized movement. |
| **Receiving capability and density-dependent discharge ceilings** | **Unchanged immediately** | Higher advice creates neither additional space nor additional bottleneck capacity at the same densities. The nominal fundamental diagram, critical density and capacity also remain fixed. |
| **Lane-change desires and reference priorities** | **Unchanged immediately** | Advice does not directly change the desired lateral fractions or merge priority. Larger sending offers can nevertheless change request amounts and realized service shares. |
| **Initial lane-cell densities and cohort size** | **Unchanged** | The comparison starts with the same traffic. Advice does not change initialization. |

Where service constraints do not impede movement, higher advice reduces
travel time. At a constrained receiver, however, larger offers may mainly
increase competition for an unchanged budget. At E's end, its entire
sending offer must request A's outlet; E has no straight continuation.

## 2. How subsequent traffic changes can help or hurt

Each cell's stock changes through arrivals minus departures. Higher advice
can increase both, so a higher advice does **not** imply a higher density
everywhere. The balance between the two determines the next effect.

| Traffic response after advice increases | Direction of the relevant factor | Consequence for TST |
|---|---|---|
| **Cells clear faster:** departures increase more than arrivals | Local density **decreases**; receiving space can improve and congestion restrictions can relax | Traffic can finish sooner, reducing TST. |
| **Traffic reaches A or the choke faster than it can be served** | Local accumulation and service competition **increase** | A, E or upstream traffic can wait longer, increasing TST. |
| **The accumulation strengthens congestion** | Density-dependent discharge ceilings and receiving capability can **decrease** | Capacity drop and spillback can prolong delays and offset the direct travel-time saving. |
| **Lane redistribution changes** | A/B loading and early merging can improve or worsen | Better use of B may relieve A; concentration in A may do the opposite. There is no universal direction. |

For example, consider E traffic approaching an already busy A outlet.
Higher advice can deliver E traffic sooner without increasing that outlet's
service budget. E may then compete more strongly with A. If A accumulates
traffic, its receiving or discharge restrictions can become tighter, and
the resulting congestion can extend upstream. This can offset the benefit
of faster travel. In another state, faster departures may clear the
congested region instead, reinforcing that benefit.

These delays arise from shared service and evolving densities. There is
no additional E-specific merging-headway, speed-mismatch or post-exit
acceleration-recovery penalty. When adequate service is available, a
diagonal lane change advances one cell just as straight movement does.

## 3. Where diminishing returns can come from

**When advice increases**, ordinary travel-time savings become smaller
for each further equal speed increment: an extra 5 km/h saves less time
per kilometre at a higher starting speed. Service constraints provide a
second limit. Once receiving or discharge binds, additional sending demand
may produce little additional completion. If it also worsens congestion,
the net benefit can disappear or reverse.

**When advice decreases**, reduced arrival pressure may preserve receiving
or discharge capability, but slower travel increases time spent on the
road. That congestion-management benefit has a limit: once further slowing
no longer avoids capacity loss or improves useful lane allocation, it adds
travel time without a compensating gain. This is a possible tradeoff, not
a guaranteed sequence of traffic responses. Lower advice also restricts
departures and can worsen accumulation in some states.

Two distinctions are essential:

- **Longer residence is not automatically more effective merge preparation.**
  Desired lane-change requests are fractions of sending offers. The model
  has no separate clock that accumulates extra attempts simply because
  advice is lower and traffic stays longer.
- **Moving the waiting location is not itself a TST saving.** With the same
  finite cohort and cumulative exits at every time, the number still on the
  road and its total time are unchanged. Lower advice must improve the
  overall completion pattern enough to compensate for slower travel;
  upstream holding time is counted too.

## 4. What this establishes for the control question

Three outcomes remain possible: higher advice can remain beneficial over
the allowed range; its benefit can level off under service constraints;
or congestion effects can make a lower advice preferable. The causal
channels alone do not establish which occurs for a prescribed cohort,
or imply a smooth, U-shaped TST curve. Changes in active traffic rules can
also change slopes or produce discontinuities in this adapted model.

There is already a precise limiting case: when the entire cohort starts
in the established unconstrained small-mass regime, maximum advice is
optimal [2]. Lane redistribution then does not add travel time, and hiding
the A/B split has no action value. Outside that regime, the existing A/B
diagnostic establishes different service and next-state evolution, not
different optimal advice.

Thus the scientific question is whether state-dependent congestion and
lane utilization make the best advice depend on the hidden lane split.
A positive information benefit, an interior optimum and useful numerical
gradients remain to be established. The explanation above adds no traffic
law or empirical result.

## Formulation sources

[1] [VSL task with established peer work as backbone & minimal adapted dependencies](vsl_literature_backbone_review_report.pdf),
Sections 3.1–3.6: lane-cell state, fixed-cohort assumptions, Subraveti
lane-change incentives, inherited Han sending/receiving budgets, Carey-led
movement adaptation, and complete TST accounting. Primary literature and
the retained/adapted formula attribution appear in that report.

[2] [Joined lane-drop VSL candidate: contract and qualification](vsl_joined_candidate_contract_and_qualification.pdf),
Sections 1–4 and 6–8, together with the
[analytical methodology addendum](vsl_methodology_review_analytical_addendum.pdf):
complete movement rules, exact remaining-time accounting, the unconstrained
regime and qualified advice sensitivities.
