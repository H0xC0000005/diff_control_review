# Speed advice should have an explicit traffic mechanism

**Current selected model, 2026-10-16:** the user selects W-F, closing
J4-W1. Immediate merging work uses actual traffic with fixed coefficients;
advice acts through traffic state. The resumed J4 forward check is
complete at **WF-Q1**, an evidence checkpoint with no new model choice.
Under the retained primary-domain bounds, the joined law has a unique
causal continuation and finite clearance throughout the original advice
interval. Applied MP6, physical marks/scales and dependent information/
action/gradient/SUMO contracts remain open. Step 3 is unfinished; Step 4
and implementation/experiments remain unopened. Earlier notices retain
their delivery-time scope.

[Selected W-F and approval scope](vsl_wf_selection_and_scope.md)

[Complete conditional forward argument and checkpoint](vsl_wf_forward_qualification_and_checkpoint.md)

**Earlier gate report:** the body below records the unselected alternatives
at delivery. The subsequent W-F decision above closes that choice.

Date: 2026-10-16. **J4 opened and begun; stopped at a new decision about
immediate merging work, J4-W1 (Type 2, G3). Step 3 remains open.** The user reviewed the
recovery checkpoint and authorized the remaining qualification. OR-Q1 is
reviewed and carried forward as conditional recovery evidence; its
limits remain. This is not approval of a physically qualified complete model.

The central finding is small in model scope but consequential for gradients:
**the trial merging-work formula lets the posted advice change merging
service directly, even when neither queued stream is moving at that advice.**
We need to decide whether that extra behavioral effect is intended, or whether
merging work should respond through the represented traffic conditions alone.
No equation has been replaced. The proposed repair changes one expression
inside the existing point component and adds no traffic state.

## What your speed-matching intuition means

Suppose E is waiting at the lane end and A is passing freely. A slower advice
can bring A closer to E's entry speed. That can make entry less disruptive:
there is less relative motion to accommodate while E joins the stream. If A
still fits the available service, this is a possible additional VSL benefit,
alongside any change in early preparation. Slower travel still costs time.
Changes in density, available gaps or queueing can offset that benefit.

Our earlier quick answer endorsed that **conditional mechanism**. It did not
establish a monotone prediction of the trial equations. Empirical merging
evidence involves actual gaps and relative speeds with selection effects;
it does not supply a universal sign or this aggregate formula.
[Marczak, Daamen and Buisson (2013)](https://mocopo.ifsttar.fr/fileadmin/contributeurs/Mocopo/Documents/Other_documents/Article_-_Merging_behaviour_-_Empirical_comparison_between_two_sites_and_new_theory_development.pdf)

The recheck therefore asks two separate questions. Does slower freely moving
A reduce the model's mismatch burden when other inputs are held fixed? And
does advice still alter that burden when both streams are already moving
below the advised speed? The second question exposes the sharper gap.

## What the equations actually establish

The trial rule measures mismatch relative to the **current advice** and A's
passing flow relative to the **capacity associated with that advice**.
Changing advice therefore changes both reference scales as well as possibly
changing actual A speed. Those scales are part of the physical constitutive
law: differentiating them produces a control effect.

| Traffic situation | Direct finding | Meaning and limit |
|---|---|---|
| **E queued, A free** | Slower A reduces the absolute speed difference, but the two moving reference scales can outweigh that reduction. An exact admissible static node example gives lower E service at lower advice while A remains free and its offer still fits the same budget. | The trial formula does not guarantee the proposed benefit. This is a local constitutive diagnostic, not a same-cohort H1 policy comparison or evidence that the real benefit is absent. |
| **A and E both queued** | At the same current budget, A receives the same cooperative flow and has the same queued speed. Nevertheless, lower advice increases the mismatch coefficient and reduces E's unique service whenever its maneuver disadvantage and mismatch coefficient are positive. | There is an additional direct advice effect while the speed limits are inactive. It is not explained by a change in A's actual speed, density or available work budget in this test. |
| **No passing A, no mismatch coefficient, or matched queued streams without maneuver disadvantage** | The corresponding mismatch effect disappears. | These remain useful negative controls; the finding does not invalidate every regime or the recovery component. |

For an intuitive comparison, imagine both streams crawling well below either
of two allowed speed signs. Keep their present queues, recovery account and
available service the same. The trial formula grants A the same share under
both signs. Yet it makes E's maneuver more costly under the lower sign solely
because the reference speed and reference capacity in the formula changed.
If the sign is intended only to cap free motion, that extra effect needs to
be removed. If the sign is also intended to change drivers' merging behavior
directly, that needs to be stated and supported.

The source merge model used for recovery distinguishes insertion speed from
free-flow speed in its congested follower calculation. It provides useful
context for this check, rather than a theorem validating our new work law.
[Leclercq et al. (2016), Section 2](https://repository.tudelft.nl/file/File_c424c1b3-7374-436b-a6a7-abdf69063aa6)

The mathematical note gives the general signs, an exact free-A example,
negative controls and a conditional alternative. No traffic trajectory,
numerical derivative or fitted parameter set was used.

[Algebra and conditional replacement, PDF](../../synthesis/research_readiness/vsl_j4_speed_response_audit.pdf)

## The choice: what should determine immediate merging work?

**Problem statement.** Should immediate E merging work depend on the posted
advice in its own right, or only through the modeled traffic speeds and flows
once the advice's physical limits have been applied?

**Function in the chain.** This is the unit-work expression within the
existing terminal component. It converts E admission into use of the single
shared budget. The resulting admission determines E's speed mark, recovery
history, subsequent A/E waiting and local total system time. H1 preparation,
T1 travel/storage, S-E-P allocation, R-E sources and O-R renewal stay as
selected inputs to either candidate.

**Core gap.** The current formula is concrete and mathematically usable in
qualified regimes, but its advice-dependent reference scales introduce an
additional behavioral assumption. Neither agreeing that speed differences
matter nor the source evidence establishes that assumption. Conversely,
requiring independence from an inactive speed sign is a physical contract,
not a formatting correction. The choice therefore belongs to G3, with
dependent sensitivity and applied-MP6 consequences.

### W-A: retain the advice-relative work law

Keep the present equation and interpret E's maneuver burden relative to the
stream's advised operating speed and nominal saturation, in addition to its
actual traffic speeds. The sign then has a direct behavioral role, even in
queued traffic. This is the strongest coherent interpretation of the current
formula; it is not established merely by keeping its existing algebra.

- **Pros:** retains all existing conditional equations and their evidence.
  Relative operating speed and saturation give a compact phenomenological
  description; they might represent an actual desired-speed effect if
  independent evidence supports it. No extra state or zone is needed.
- **Cons:** that direct effect is currently unsupported. It changes service
  in the queued comparison above and can reverse the free-A speed-matching
  effect. Calling the factors normalization does not make those consequences
  physically neutral. The source evidence does not identify their strength.
- **Dependencies and consequences:** admit the extra desired-speed mechanism
  explicitly and qualify it before treating its gradient as physical advice
  guidance. Conditional analytical use remains possible with the limitation
  disclosed. Full-range events, realistic scales and external validation
  remain unfinished.

### W-F: use fixed physical reference scales in the same work law

Keep the same dependence on A's passing flow and the positive A–E speed
difference, but measure them against fixed common reference values. A change
in advice affects work through actual modeled speeds/flows and constraints;
it does not rescale an unchanged queued interaction merely by changing the
sign. The PDF specifies this concrete candidate and its units.

For a minimal comparison, anchor those reference values once at the existing
upper advice and its capacity. The two formulas then coincide at that anchor.
These are coefficient units fixed for the study: they must not be recomputed
silently when an optimizer's search box changes. Equivalently, one can record
the resulting dimensional interaction coefficient directly.

- **Pros:** one constitutive substitution, with no new queue, zone, speed
  state or observation. It removes the extra advice effect in the queued
  comparison. With A free and the same offer/budget, reducing its speed
  increases E service on the regular queued-E branch. That can also reduce
  the new recovery profile through the existing speed mark. The old
  conservative root and bounded-work conditions remain sufficient under
  the stated anchor.
- **Cons:** still an uncalibrated aggregate approximation. It deliberately
  omits a separate desired-speed effect, and neither resolves real gap
  distributions nor independently validates the queued insertion-speed
  mark. The local benefit does not prove that a slower whole-cohort policy
  is better, or that an interior optimum exists.
- **Dependencies and consequences:** changes G3's trial constitutive family
  away from the anchor, so dependent advice sensitivities must be qualified
  again. The original O-R history formula and its profile bounds remain
  unchanged. The anchor preserves the earlier regular witness there;
  it does not extend that witness across the full action range or supply
  applied MP6.

**Provisional recommendation: W-F.** It matches the selected emphasis on
current traffic state and the triangular congested branch with the smaller
additional behavioral commitment. The reason is causal clarity, including
the queued comparison, rather than a desire to force a VSL benefit. Retain
W-A as a serious sensitivity/model-form rival if its direct behavioral
interpretation can be justified. **Neither candidate is newly selected.**

| Same comparison | W-A: current advice-relative scales | W-F: fixed scales |
|---|---|---|
| A free, E queued; same A offer and budget | Lower advice can improve or worsen E service. | Lower actual A speed helps E on the stated regular branch. |
| Both queued below both signs; same budget | Lower sign alone changes E service. | The sign alone leaves the local allocation unchanged. |
| What would need physical evidence? | Both the actual-state interaction and the direct desired-speed/saturation effect. | The actual-state interaction coefficient and representative speed; no separate direct sign effect. |
| Change to the model structure | None; add an explicit behavioral interpretation. | Replace the two moving scales in one work expression; preserve state and interfaces. |

## Where this leaves the overall review

J4 has **begun substantively**: it audited the selected candidate, rechecked
the relevant primary evidence and derived the response signs and exact
diagnostic. It now stops at a genuinely new methodological choice. This is
not the final Step 3 confirmation gate and not a failure of the elementary
point-model direction.

| Remaining block | Status after this pass |
|---|---|
| Joined behavior across the original advice/scenario range | Conditional storage, service and clearance bounds retained. No whole-range hybrid/event theorem is claimed; the immediate-work interpretation must close first. |
| Joint physical credibility and MP6 | The advice-response gap is now explicit. Crossing-speed interpretation, maneuver/recovery separation and credible joint physical scales remain open. |
| Information, action and gradient comparison | Existing observer fairness, compact ending-statistic and strong aggregate/history/search rivals retained. No successor action or useful-gradient certificate is inherited from S13 or the old terminal. |
| Model → SUMO S-P → SUMO S-L | Selected roles remain. The exact coupled-law correspondence and development/held-out evidence contract remain dependent work; no runnable evaluator is admitted. |

After W-A/W-F is decided, resume J4 with that concrete law: retain the
original action range, qualify the joined event/domain and physical scales,
then complete the dependent information/sensitivity/reference contracts.
No simulator construction, installation, traffic experiment or Step 4 is
opened by this report.

[References actually viewed and source limits](../../extraction/research_readiness/vsl_j4_speed_response_source_audit.md)

[Commands, preservation and checks](vsl_j4_speed_response_work_report.md)
