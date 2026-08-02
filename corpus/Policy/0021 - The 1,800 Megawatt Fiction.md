# The 1,800 Megawatt Fiction

### _How NESO Sized the Grid's Deadliest Contingency to Fit the Answer It Wanted - the Dogger Bank Infeed, the Loss Larger Than the Nuclear Fleet, and the Number That Halves Every Stability Report - by Mark S_

---

**Target:** The largest-credible-loss assumption underpinning NESO's frequency-risk and system-security framework (Security and Quality of Supply Standard; Frequency Risk and Control Report 2025).
**Author:** M. Shirley, Independent Engineer & Inventor
**Status:** Independent critique - not adopted regulation.
**Date:** July 2026

---

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. The Number That Runs the Grid](#2-the-number-that-runs-the-grid)
- [3. The 1,800 MW Assumption and Its Missing Provenance](#3-the-1800-mw-assumption-and-its-missing-provenance)
- [4. Dogger Bank: One Wire, 3,600 Megawatts](#4-dogger-bank-one-wire-3600-megawatts)
- [5. Larger Than the Fleet It Replaced](#5-larger-than-the-fleet-it-replaced)
- [6. The Swing Equation Does Not Negotiate](#6-the-swing-equation-does-not-negotiate)
- [7. Halving the Loss Halves the Duty](#7-halving-the-loss-halves-the-duty)
- [8. Marking Your Own Homework](#8-marking-your-own-homework)
- [9. What 2019 Actually Cost](#9-what-2019-actually-cost)
- [10. The Companion Crime: 0.125 to 1.0 Hz/s](#10-the-companion-crime-0125-to-10-hzs)
- [11. Comparative Table - The Design Basis vs the Physics](#11-comparative-table-the-design-basis-vs-the-physics)
- [12. What the Framework Refuses to See](#12-what-the-framework-refuses-to-see)
- [13. The Accountability That Already Expired](#13-the-accountability-that-already-expired)
- [14. The Ethical Dimension](#14-the-ethical-dimension)
- [15. Restoration Path - Size to the Real Loss, Publish the Honest Floor](#15-restoration-path-size-to-the-real-loss-publish-the-honest-floor)
- [16. Manifesto - Design for the Storm You Are Actually Building](#16-manifesto-design-for-the-storm-you-are-actually-building)
- [Related Documents](#related-documents)

---

## 1. Executive Summary

There is a single number sitting underneath the entire edifice of British frequency security, and it is wrong. Not approximately wrong, not conservatively wrong, not wrong in the direction that buys safety margin. It is wrong in the one direction a design assumption must never be wrong: it understates the hazard. NESO's frequency-risk framework sizes the system against a *largest credible loss* of the order of **1,800 MW** - the sudden disappearance of the single biggest infeed the system must be built to ride through. The framework's inertia floors, its response volumes, its Rate-of-Change-of-Frequency ceilings, its published assurances that the system remains secure at ever-lower quantities of real synchronous mass - all of it is derived from, and only makes sense against, that 1,800 MW figure.

In today's network configuration the largest credible loss is not 1,800 MW. It is **3,600 MW**: the Dogger Bank complex (A, B and C), delivered into the GB system through high-voltage direct-current links that share landfall and converter infrastructure. The design basis is out by a factor of two, and it is out on the wrong side. The framework has been built to withstand half the disturbance the grid can actually deliver to itself.

To grasp the scale of what 3,600 MW means, stop thinking in abstract megawatts and look at what is running. At the moment this document was written - 05:10 on 7 July 2026 - the entire British nuclear fleet, every reactor at every station, was generating **3,007 MW** (GridWatch telemetry, `gridwatch.templar.co.uk`, five-minute cadence, aggregating Elexon and National Grid settlement data). Through June and July 2026 the fleet has averaged a shade under 3,000 MW. **A single Dogger Bank infeed loss is larger than everything Britain's nuclear power stations are currently producing, combined.** One offshore wire, tripping, removes more instantaneous generation than the summed output of Sizewell B, Heysham 1, Heysham 2, Hartlepool and Torness put together. The framework is designed to survive losing two-thirds of that.

This is the entire case, and the rest of this document is its elaboration: **a design basis that understates the largest credible loss by a factor of two understates the required intrinsic energy of the system by a factor of two.** The swing equation is linear in the loss. Double the loss and you double the stored kinetic energy the system needs to hold the same Rate of Change of Frequency. NESO's own honest physics - the physics set out in the Minimum Intrinsic Floor papers - says that riding a 1,800 MW loss within the historic protection-design RoCoF ceiling of 0.125 Hz/s requires about 360 GVA.s of real inertia. Riding a 3,600 MW loss within the same ceiling requires about **720 GVA.s**. The framework does not ask for 720. It does not ask for 360. It is drifting toward a floor of **102 GVA.s** and calling it secure.

The gap between 102 and 720 is not a modelling nicety. It is the difference between a grid that can be governed by a human being after a disturbance and a grid that has already been handed to automatic disconnection relays before anyone in the control room has read the first alarm. And the whole apparatus of assurance that says otherwise rests on the quiet decision to design against 1,800 MW - to answer the easy version of the exam question and mark the paper a pass.

This document is not a claim that NESO is unaware of Dogger Bank. It is a claim about what the *design basis* is anchored to, what the published stability case is graded against, and what happens to every reassuring number in the frequency-risk framework the moment you replace the fictional loss with the real one. The reassurance does not survive the substitution. That is why the substitution is not made.

---

## 2. The Number That Runs the Grid

Most people who read energy policy never encounter the largest credible loss, because it is buried three layers below the language of targets and pathways and gigawatts-connected. But it is the load-bearing number of the entire security framework, and everything visible in policy is downstream of it.

Here is the chain. A synchronous power system holds its frequency at 50 Hz because generation and demand are in continuous balance and the spinning mass of the fleet resists any sudden change. When a large infeed is lost - a generating unit trips, an interconnector fails, an HVDC link blocks - the balance breaks instantly, and the frequency begins to fall. How *fast* it falls in the first instant is the Rate of Change of Frequency, the RoCoF, and it is governed by one relationship, the swing equation, which in its stored-energy form says:

> RoCoF = (f0 x deltaP) / (2 x E)

where f0 is nominal frequency (50 Hz), deltaP is the size of the loss, and E is the kinetic energy stored in all the synchronous mass electromagnetically coupled to the system, measured in gigavolt-ampere-seconds (GVA.s). Read it plainly: **the initial RoCoF is proportional to the size of the loss and inversely proportional to the stored energy.** Bigger loss, faster fall. More stored mass, slower fall. There are no other terms. No control system, no market, no firmware appears in this equation, because the first phase of a frequency event is decided before any control system has finished measuring it. This is the physics the [Inertia explainer](../Electrical Explainers/0003 - Inertia.md) sets out in full, and the [Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md) builds its entire case upon.

Now watch how the largest credible loss sizes everything else. The system operator must keep the RoCoF below a ceiling - historically 0.125 Hz/s, the rate beyond which distribution protection was never coordinated to ride through. Rearrange the swing equation for the minimum stored energy:

> E_required = (f0 x deltaP) / (2 x RoCoF)

The required inertia - the floor the operator must hold at all times - is set by exactly two numbers: the RoCoF ceiling you are willing to tolerate, and the largest credible loss you are designing against. **deltaP is half of the entire specification.** Get it wrong, and the floor you compute is wrong by the same proportion, and every downstream quantity - the inertia you must schedule, the response you must contract, the margin you must carry - inherits the error at full strength.

This is why the largest credible loss is not a technical footnote. It is the single most consequential assumption in the security framework, because it is one of only two inputs to the floor that keeps the grid inside its protection design. A framework can get everything else right - can model its response products beautifully, can procure its dynamic containment with great sophistication, can publish immaculate stability assessments - and if it has anchored deltaP to the wrong number, all of that sophistication is being applied to the wrong problem. It is a fire suppression system engineered with exquisite care for a fire half the size of the one that is going to happen.

And here is the part that should end any comfortable reading of the framework: the error does not announce itself. A design basis that understates the loss produces a security case that *looks* fully satisfied. Every report closes green. Every floor is shown to be adequate against the contingency the framework chose to test. The inadequacy is invisible precisely because the framework declines to test itself against the disturbance the grid can actually produce. You cannot fail an exam whose hardest question you have removed from the paper.

---

## 3. The 1,800 MW Assumption and Its Missing Provenance

Ask where the 1,800 MW comes from, and the answer is more troubling than a simple error would be.

The GB Security and Quality of Supply Standard (SQSS) and the Grid Code operational codes have long carried a secured-event standard built around three tiers: a *normal infeed loss* of the order of 1,000 MW, an *infrequent infeed loss* of the order of 1,320 MW, and a largest secured loss taken, in the frequency-risk framework's operational planning, at around 1,800 MW. These numbers have a history. They were sized in an era when the largest single infeeds on the system were large thermal units and the first generation of interconnectors - a 1,000 MW nuclear unit, a 2,000 MW interconnector run at part-loading within a secured limit. In that world, 1,800 MW was a defensible envelope for the largest loss the system would credibly suffer in a single event.

That world is gone. And the number did not move with it.

Note something the TSGB corpus itself must own up to here, because a document that accuses NESO of anchoring to a stale figure cannot pretend its own house is spotless. The foundational Minimum Intrinsic Floor paper derives its headline 360 GVA.s(i) floor from "a credible maximum loss of the order of 1,800 MW" - and it does so *without citing a NESO source for that figure*. It is presented as a design assumption, inherited from the secured-event convention, not anchored to a specific published contingency. The MIF vs Current GB Outturn paper carries the same 1,800 MW loss through its purchased-time tables. So does the Dynamic MIF sensitivity analysis. The whole MIF apparatus was, until now, built on the same 1,800 MW envelope it is about to accuse the establishment of clinging to.

That is not an embarrassment to be hidden. It is the point, sharpened. If an independent engineer building a floor designed *specifically to be conservative* reached for 1,800 MW out of convention, then the convention is powerful, invisible, and wrong, and it has captured even the people trying to correct the system. The 1,800 MW figure is not a NESO conspiracy. It is something worse: an inherited default that no one re-derived when the infeeds changed, sitting unexamined at the base of both the official framework and its critics, quietly halving the hazard for everyone who touched it. This document is the re-derivation. It corrects the corpus's own MIF papers in the same breath it corrects NESO, and it does so because the physics does not care whose spreadsheet the stale number was sitting in.

The provenance problem is therefore twofold. NESO's 1,800 MW is anchored to a secured-event convention sized for a fleet that no longer exists. And the figure is so embedded that it propagated into the corpus's own conservative floor without challenge. Both are now confronted with the same fact: the largest credible loss on the GB system is no longer set by a thermal unit or a first-generation interconnector. It is set by an offshore wind complex delivered through direct current, and it is twice the size of the number everyone has been using.

---

## 4. Dogger Bank: One Wire, 3,600 Megawatts

Dogger Bank sits 130 kilometres off the Yorkshire coast, and when complete it is the largest offshore wind development in the world. It is built in phases - Dogger Bank A, Dogger Bank B, Dogger Bank C - each rated at roughly 1.2 GW, for a combined capacity of the order of **3.6 GW**. Unlike the offshore wind of the previous decade, which connected through alternating-current cables over shorter distances, Dogger Bank's distance from shore requires **high-voltage direct-current (HVDC)** transmission: the offshore array's power is rectified to DC, carried to shore through DC cables, and inverted back to AC at an onshore converter station before entering the transmission network.

This HVDC architecture is what makes Dogger Bank a *loss-of-infeed* problem of a class the 1,800 MW convention never contemplated. Three considerations compound.

**First, HVDC converters are single points of failure at gigawatt scale.** A converter block, a DC pole, a control-system fault - any of these can remove the entire link's infeed in a single event, faster and more completely than a thermal unit trips. Where a large power station is several units that fail somewhat independently, a 1.2 GW HVDC pole is one thing that either delivers 1.2 GW or delivers nothing.

**Second, the links share infrastructure.** Dogger Bank A and B land their power at a common onshore area (Creyke Beck), while C lands separately (Teesside). Shared infrastructure is the mechanism by which nominally independent links become a single credible loss. A fault on a common busbar, a common connection point, or a common protection zone does not politely disconnect one link and spare the others. It takes what it is connected to.

**Third - and this is where the argument is made deliberately robust against its own strongest objection** - even if one refuses the full 3.6 GW common-mode loss as too pessimistic, the conservative reading still breaks the framework. If Dogger Bank A and B share landfall and converter infrastructure, then a common-mode event on that shared infrastructure is a **2,400 MW** single loss - and 2,400 MW already exceeds the 1,800 MW design basis by a third. So the framework fails at both readings. Against the full complex it is out by a factor of two. Against the conservative A+B common-landing loss it is still out by a third. There is no reading of Dogger Bank on which an 1,800 MW design basis is adequate. The only question is whether the framework is under-sized by 33% or by 100%.

The corpus has already recorded the direction of travel here. The Stability Market rebuke flagged, against its own 1.3 GW loss figure, that the number is "subject to ongoing review as offshore wind farms increase their contribution and multi-infeed losses become credible." That review has now been overtaken by physical fact. The multi-infeed loss is not a future contingency to be modelled. It is commissioned, it is connecting, and it is called Dogger Bank.

Set the frame precisely, because it is the whole argument: a single offshore complex now presents the GB system with a credible loss of infeed that is somewhere between one-third larger and twice as large as the number the entire frequency-security framework is built to withstand. The framework has not been re-derived to meet it. And the reason the inadequacy has not surfaced in any published stability assessment is that the assessments are run against the 1,800 MW convention, not against the wire in the sea.

---

## 5. Larger Than the Fleet It Replaced

Numbers on a page do not frighten anyone. So make the 3,600 MW concrete, and make it concrete against the one comparison that captures what has happened to the British grid in a single image.

The nuclear fleet is what Dogger Bank is replacing - not asset for asset, but in the role of the large, firm, synchronous infeed around which the system's contingency planning was historically built. So ask the direct question: how does a single Dogger Bank infeed loss compare to the whole of British nuclear generation, right now?

The GridWatch telemetry archive (`gridwatch.templar.co.uk`, five-minute cadence, aggregating Elexon BMRS and National Grid settlement data; the same public series available through Kate Morley's Grid tool and other portals) records the fuel-by-fuel output of the GB system continuously. Interrogated across fifteen years of that record, held in the GDA data lake, the nuclear column tells a stark story.

**At the moment of writing - 05:10 on 7 July 2026 - the entire GB nuclear fleet was generating 3,007 MW.** Through June 2026 it averaged 2,940 MW; through the first week of July, 3,001 MW. Across the summer of 2026 the fleet has been sitting at approximately three gigawatts as its ageing Advanced Gas-cooled Reactors cycle through the maintenance and refuelling outages that a fleet in its final years cannot avoid.

Put the two numbers side by side and hold them there:

- **Dogger Bank single credible infeed loss: ~3,600 MW.**
- **Entire British nuclear fleet, live output, 7 July 2026: 3,007 MW.**

**A single Dogger Bank trip removes more instantaneous generation than every nuclear reactor in Britain is producing put together.** Sizewell B, Heysham 1, Heysham 2, Hartlepool, Torness - the whole surviving fleet, every rod in every core - sums, this summer, to less than one offshore wind complex can take off the system in one event. And the frequency-security framework is designed to survive losing two-thirds of *that*.

Two honest qualifications, because the argument is only as strong as its refusal to overstate.

The nuclear fleet's *nameplate* is about 5.9 GW across nine reactors at five sites; its ~3 GW summer output reflects outages, not permanent capacity. So the strict claim is not that 3.6 GW exceeds nuclear's maximum possible output; it is that 3.6 GW exceeds what the fleet is *actually delivering* through this operating period - which is the output the system actually has to work with when the disturbance arrives. A contingency is suffered at the operating point, not at the nameplate.

And the fleet is not merely running low this summer; it is structurally shrinking. The same GridWatch record shows the annual peak of nuclear output falling year on year as the AGRs retire: from **9,346 MW in 2013** to **7,505 MW in 2019** to **5,310 MW in 2025**. The ceiling has nearly halved in a decade, and Hartlepool and Heysham 1 are scheduled to close in 2028, Heysham 2 and Torness around 2030. The firm synchronous infeed the contingency framework was built around is leaving the system on a published timetable, and the infeed replacing it in the connection queue - Dogger Bank and the offshore HVDC fleet behind it - is both larger as a single loss and lighter as a source of the inertia that would ride that loss through. The [Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md) chronicled the disappearance of the mass. This is the other blade of the same scissors: as the mass that absorbs the loss falls, the size of the loss itself rises. The framework has kept its design basis fixed while both blades closed on it.

---

## 6. The Swing Equation Does Not Negotiate

Everything above is context. Here is the mechanism, and it is arithmetic a competent sixth-former can check.

Return to the required-energy form of the swing equation:

> E_required = (f0 x deltaP) / (2 x RoCoF)

Hold the RoCoF ceiling at the historic protection-design value of 0.125 Hz/s - the value the MIF foundational paper derives from and the value distribution protection was actually coordinated against. Now compute the floor for the two loss figures.

**At the design-basis loss of 1,800 MW:**
E = (50 x 1.8) / (2 x 0.125) = 90 / 0.25 = **360 GVA.s.**

**At the real largest credible loss of 3,600 MW:**
E = (50 x 3.6) / (2 x 0.125) = 180 / 0.25 = **720 GVA.s.**

The floor doubles. It must double, because the swing equation is linear in the loss and nothing in it lets a doubled disturbance be ridden by the same stored energy at the same RoCoF. There is no cleverness available here. There is no product, no service, no market instrument that changes the left-hand side. **A 3,600 MW largest credible loss demands 720 GVA.s of intrinsic energy to hold the protection-design RoCoF ceiling, and that is the honest floor.**

This is the point at which the corpus must correct itself in public, because the error is instructive. The recent ministerial report on the Minimum Intrinsic Floor took the correct step of naming Dogger Bank's 3,600 MW as the current largest credible loss - and then, in the same tables, retained the **360 GVA.s** floor and the 0.125 Hz/s pairing that belong to the *1,800 MW* case. That is internally inconsistent by exactly the factor this section derives: 360 GVA.s holds 0.125 Hz/s against 1,800 MW, not against 3,600 MW. Against 3,600 MW, 360 GVA.s yields 0.25 Hz/s - already double the protection-design ceiling - and the honest floor is 720. The ministerial report's own headline loss and its own floor were describing two different grids. That error is being corrected in this document and in the report itself, and the correction runs the same direction as the argument: **naming the real loss makes the required floor worse, not better.** An honest engineer does not flinch from that. The number that makes the case uncomfortable is the number that makes the case true.

Now hold the *loss* at the real 3,600 MW and let the inertia vary across the operating points the framework actually contemplates. This is the table that matters, computed correctly for a 3,600 MW loss, showing the initial RoCoF and the purchased time to the 49.2 Hz low-frequency-demand-disconnection set-point (a fall of 0.8 Hz), which is the working set-point the MIF papers use for time-to-disconnection:

| Inertia held (GVA.s) | Context | RoCoF for a 3,600 MW loss | Purchased time to 49.2 Hz |
|---|---|---|---|
| **720** | The honest floor for a 3,600 MW loss at 0.125 Hz/s | 0.125 Hz/s | ~6.4 s |
| 360 | The floor the framework and the MIF papers compute *for 1,800 MW* | 0.25 Hz/s | ~3.2 s |
| 155 | GB system average, 2025 | ~0.58 Hz/s | ~1.4 s |
| 102 | The FRCR floor NESO is drifting toward | ~0.88 Hz/s | ~0.9 s |
| 50 | A low-wind, low-demand future night | ~1.8 Hz/s | ~0.45 s |

Read the third and fourth rows, because that is where the grid actually lives. At the 2025 system-average inertia of about 155 GVA.s, a 3,600 MW Dogger Bank loss produces an initial RoCoF near 0.58 Hz/s - well beyond the 0.125 Hz/s the protection was coordinated against - and buys about **1.4 seconds** to the disconnection set-point. At the 102 GVA.s floor the frequency framework is normalising, the same loss buys about **0.9 seconds.** Not 0.9 seconds to intervene. 0.9 seconds until the automatic protection begins shedding demand - shedding customers - because the human operator to whom Parliament assigned the system cannot act in under a second, and was never expected to.

The framework's published security case does not show these numbers, because the framework's published security case is run against 1,800 MW. Halve the loss in the model and every figure in that table improves: the RoCoF halves, the purchased time doubles, the floor that looks adequate becomes adequate. The 1,800 MW assumption is not a modelling convenience. It is the specific input that turns a 0.9-second grid into a paper that reads as secure.

---

## 7. Halving the Loss Halves the Duty

It is worth being explicit about what the understatement *does* to the rest of the framework, because the 1,800 MW figure does not sit in isolation. It is multiplied through every derived quantity, and each multiplication carries the factor-of-two error forward.

**The inertia floor.** As section 6 shows, the required floor is linear in the loss. Designing against 1,800 MW rather than 3,600 MW does not shave a margin; it *halves the requirement*, from 720 GVA.s to 360, before the further relaxations discussed below take it down toward 102. The single largest driver of the gap between the honest floor and the operating floor is not the RoCoF relaxation, provocative as that is. It is the loss assumption. Even if the RoCoF ceiling were held sacred at 0.125 Hz/s, the 1,800 MW assumption alone would understate the floor by a factor of two.

**The response volumes.** The framework's dynamic-response products - the Dynamic Containment portfolio and its relatives, dissected in the [Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md) - are procured to arrest a frequency fall of a given steepness and depth. Both steepness and depth scale with the loss. A portfolio sized to contain the excursion from an 1,800 MW loss is, against a 3,600 MW loss, arriving into a fall twice as steep and heading twice as deep, having been volume-sized for half the event. And these products, as the corpus has shown at length, are already too slow at the *design* loss - they respond after the first phase of the event because they are responses and not stored energy. Sizing them for half the real loss compounds a timing failure with a magnitude failure.

**The security assessments.** Every published statement that the system remains secure at a given inertia level is a statement about a specific contingency. Change the contingency from 1,800 MW to 3,600 MW and the assessment does not degrade gracefully - it inverts. Operating points certified as secure against the design-basis loss are, against the real loss, points at which the grid rides out to automatic disconnection before human intervention is possible. The certification was true. It was true about the wrong disturbance.

This is the mechanism by which a single stale number produces a fully self-consistent, wholly reassuring, and comprehensively wrong picture of system security. Nothing downstream has to be individually dishonest. The response modelling can be scrupulous. The inertia accounting can be precise. The reports can be written in good faith by capable engineers. And the entire structure still describes a grid that does not exist, because the disturbance at its foundation is half the size of the one the sea is going to deliver. **Garbage sizing in, immaculate reassurance out.** The immaculateness is the danger - it is what allows the floor to keep falling toward 102 GVA.s with every report closing green.

---

## 8. Marking Your Own Homework

Here is where charity runs out, and it runs out on a structural observation rather than an accusation of intent.

A design basis is meant to be chosen adversarially. You identify the worst credible thing the system can do to itself and you build to survive it. The entire discipline of security engineering is the discipline of *not* choosing the contingency you would like to face. The largest credible loss is supposed to be the hardest question on the paper, selected precisely because it is hard, because surviving it is what makes the system safe.

The 1,800 MW assumption inverts this discipline. It is a design basis that has been allowed to lag the physical system until it no longer describes the worst credible event - until it describes a comfortably survivable event, roughly half the size of the real one. And because the framework grades itself against that comfortable event, it passes. Every time. By construction.

Consider what it would mean to grade honestly. If NESO's frequency-security framework tested itself against the real 3,600 MW Dogger Bank loss, its published inertia floors would be shown to be inadequate by a factor of two or more, its response portfolios would be shown to be sized for half the event, and its assurance that the system remains secure at 102 or 155 GVA.s would collapse into an admission that at those inertia levels a credible loss drives the grid to automatic disconnection before a human can act. Every one of those conclusions is available today, from public data, using the operator's own swing equation. The framework does not reach them because it does not ask the question that produces them.

That is what marking your own homework means. It is not fraud and this document does not allege fraud. It is something more insidious and more durable: an institutional arrangement in which the body that must demonstrate security also chooses the contingency against which security is demonstrated, and has allowed that contingency to drift to a size that guarantees the demonstration succeeds. The [Governance Without Physics](0007 - ESO - Governance Without Physics.md) critique identified the general form of this pathology - a framework that answers to its own definitions rather than to the physical system. The 1,800 MW assumption is its purest instance. The exam is set, sat, and marked by the same institution, and the hardest question has quietly been removed from the paper.

The remedy is not more sophistication in the answer. It is a harder question. Restore the design basis to the real largest credible loss, and every downstream number is forced to tell the truth, whether or not the truth is convenient. That the truth is *inconvenient* - that it doubles the required floor and indicts the operating point - is not a reason to keep the fiction. It is the reason the fiction exists.

---

## 9. What 2019 Actually Cost

The reason a 3,600 MW loss must be taken seriously is not theoretical. Britain has a recent, documented, well-understood object lesson in what happens when a loss of infeed meets a system short of inertia, and it happened at *less than half* the Dogger Bank figure.

On 9 August 2019, at 16:52:33, the Hornsea One offshore wind farm and the Little Barford gas-turbine station were lost in rapid succession - a combined infeed loss of about **1.4 GW** (Hornsea ~1.2 GW, Little Barford's units ~0.7 GW, with associated offshore wind, decomposed in the TSGB White Paper). The system frequency fell to **48.787 Hz**, the low-frequency demand disconnection scheme operated, and around **one million customers** were disconnected for up to 45 minutes. Trains stopped. Traffic signals failed. A hospital lost supply. This is chronicled across the corpus - in the [Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md), the [Inertia explainer](../Electrical Explainers/0003 - Inertia.md), and the SCADA Adequacy brief - because it is the single most important stability event in modern British grid history.

Now hold 2019 against Dogger Bank. The 2019 event was **1.4 GW** and it shed a million people. The Dogger Bank credible loss is **3.6 GW** - roughly **2.6 times** the disturbance that took a million customers off the system. And it will, on present trends, arrive into a grid holding *less* inertia than the grid of August 2019 held, because the synchronous fleet has continued to retire in the seven years since. A disturbance more than two and a half times larger, into a system more than a little weaker, designed against a contingency half its size.

The 2019 event also carries a second lesson the framework has not absorbed, and it bears directly on why the loss figure cannot be treated as a comfortable planning convention. Part of what made 2019 severe was that the inverter-coupled Hornsea plant contributed a control-interaction disturbance the protection had not been configured for - the loss was not a clean thermal trip but a messier, faster, IBR-flavoured event. Dogger Bank is HVDC-coupled offshore wind: the same family of dynamics, at more than double the scale, through converters whose fault behaviour is set by firmware rather than by the physics of a spinning machine. The 1,800 MW convention was sized for thermal trips. The real losses now arriving are larger, faster, and shaped by power electronics. The design basis is stale in its magnitude *and* in its character.

If 1.4 GW shed a million customers in 2019, the question the framework must answer - and the question the 1,800 MW assumption exists to avoid - is what 3.6 GW does to a grid running at 102 GVA.s. The swing equation in section 6 gives the answer: roughly nine-tenths of a second to automatic disconnection. 2019 is not the worst case. 2019 is the warning that the worst case was already coming, and the worst case is now a commissioned asset with a connection date.

---

## 10. The Companion Crime: 0.125 to 1.0 Hz/s

The 1,800 MW understatement does not operate alone. It has a partner, and the two together explain the full descent from a 720 GVA.s honest floor to a 102 GVA.s operating floor.

The partner is the relaxation of the RoCoF ceiling. For most of the post-privatisation period, GB distribution protection was coordinated against a Rate of Change of Frequency of **0.125 Hz/s** - the design value the MIF paper uses and the value beyond which distributed generation was never guaranteed to ride through rather than trip. As inertia fell and RoCoF rose, the ceiling was progressively relaxed - to 0.5 Hz/s, then to **1.0 Hz/s** for credible-event design purposes, with the frequency framework contemplating still-higher values. That is an **eightfold** relaxation, dissected in full by the [Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md): "The grid did not get eight times stronger. The threshold got eight times more permissive."

Watch how the two moves combine, because their product is the whole story. Return to the required floor:

> E_required = (f0 x deltaP) / (2 x RoCoF)

- Start from the honest specification: 3,600 MW loss, 0.125 Hz/s ceiling. Floor = **720 GVA.s.**
- Halve the loss to the fictional 1,800 MW. Floor drops to **360 GVA.s.**
- Relax the ceiling eightfold to 1.0 Hz/s. Floor drops to **45 GVA.s** at 1,800 MW, or **90 GVA.s** at the real 3,600 MW.

The 102 GVA.s floor the framework is normalising is what you land on when you both understate the loss *and* relax the ceiling - when you take the 720 GVA.s the real grid needs and permit yourself, through two independent administrative moves, to hold roughly a seventh of it. The MIF paper put it exactly: "The 102 GVA.s floor is what you get when you relax the RoCoF ceiling eightfold and decline to ask what kind of GVA.s you are counting." This document adds the third term the MIF paper had not yet isolated: *and design against half the real loss.*

The relaxation and the understatement are the same species of move - both take a physical constraint the grid cannot actually escape and redefine it into administrative comfort. Neither adds a single joule of stored energy to the system. Neither slows the fall of frequency by a single millisecond when Dogger Bank trips. They change the number in the document. The grid is governed by the swing equation, and the swing equation has not read the document.

---

## 11. Comparative Table - The Design Basis vs the Physics

| Quantity | The Framework's Design Basis | The Physical Reality | Consequence of the Gap |
|---|---|---|---|
| Largest credible loss | ~1,800 MW (secured-event convention) | ~3,600 MW (Dogger Bank A+B+C); ~2,400 MW even on the conservative A+B common-landing reading | Design basis understated by 33-100% |
| Character of the loss | Thermal-unit / early-interconnector trip | HVDC-coupled offshore wind; converter-set fault behaviour | Sized for the wrong dynamics as well as the wrong magnitude |
| Required inertia floor at 0.125 Hz/s | 360 GVA.s (computed for 1,800 MW) | 720 GVA.s (for 3,600 MW) | Floor understated by a factor of two before any RoCoF relaxation |
| RoCoF ceiling | Relaxed to 1.0 Hz/s | Protection coordinated to 0.125 Hz/s | A further eightfold permission the hardware never received |
| Operating inertia floor | Drifting toward 102 GVA.s | 720 GVA.s honest requirement | Holding ~1/7 of what the real loss demands |
| Purchased time at the floor | Modelled comfortable against 1,800 MW | ~0.9 s to disconnection at 102 GVA.s against 3,600 MW | Grid handed to automatic relays before human action is possible |
| Comparison to nuclear fleet | An abstract megawatt figure | 3,600 MW exceeds the fleet's ~3,000 MW live summer output | A single infeed larger than all British reactors are generating |
| What resolves the gap | More response product, faster containment | Real stored energy, sized to the real loss | Only intrinsic mass changes the left-hand side of the swing equation |

The table reads as eight rows. It is one proposition eight times: **the framework is designed against a disturbance half the size of the real one, holds a fraction of the inertia the real one demands, and reassures on the basis of a contingency the sea is not obliged to respect.**

---

## 12. What the Framework Refuses to See

Enumerated plainly, so that none of it can be waved away as rhetorical emphasis:

1. **That the largest credible loss has doubled.** The single most important input to the security framework has changed physically, from an ~1,800 MW thermal-era envelope to an ~3,600 MW HVDC-era reality, and the design basis has not moved to meet it.

2. **That the required inertia floor has doubled with it.** The swing equation is linear in the loss. A doubled loss is a doubled floor - from 360 to 720 GVA.s at the protection-design ceiling - before any other adjustment.

3. **That the operating floor is a fraction of the honest floor.** The 102 GVA.s the framework is normalising is roughly one-seventh of the 720 GVA.s a 3,600 MW loss demands at 0.125 Hz/s.

4. **That a single infeed now exceeds the live nuclear fleet.** At ~3 GW of actual summer output, the entire British nuclear fleet generates less than one Dogger Bank credible loss.

5. **That the loss has changed character, not just magnitude.** HVDC-coupled offshore wind fails through converter and control-system faults with dynamics the thermal-era secured standard never contemplated, as the 2019 IBR-flavoured event foreshadowed at less than half the scale.

6. **That the purchased time has fallen below the human floor.** At the operating inertia levels the framework accepts, a real Dogger Bank loss buys under a second to automatic disconnection - below any plausible operator reaction time and below the 3-to-5-second human-response floor the MIF papers derive.

7. **That the reassurance is an artefact of the assumption.** Every published statement of security is true about the 1,800 MW contingency and false about the 3,600 MW one, and the framework tests only the former.

8. **That the fix is not procurable as a service.** No quantity of response product changes the stored-energy term in the swing equation. Only real synchronous mass - the intrinsic inertia the MIF framework insists on counting separately - can meet a doubled loss. This is the regulatory gap the whole corpus circles: the thing the grid actually needs is the one thing the market has no category to buy.

Each of these is derivable today, from public data, using the operator's own equations. None of them requires privileged access to NESO's internal models. The MIF vs Current GB Outturn paper made the same point about the inertia figure: "the same inertia figure NESO tracks internally can be reconstructed from outside the building." So can the correct largest credible loss. So can the floor it demands. The framework's refusal to see these things is not a limit of knowledge. It is a limit of will.

---

## 13. The Accountability That Already Expired

The deepest consequence of the 1,800 MW fiction is not technical. It is constitutional, and it connects this critique to the statutory argument the ministerial report on the MIF makes at length.

The Electricity Act 1989 placed a continuous physical-outcome duty on the system operator, re-enacted word-for-word for NESO by the Energy Act 2023: to develop and maintain an efficient, coordinated and economical system, meeting all reasonable demands with security and quality of supply. That duty has an owner. Parliament assigned responsibility for the whole system to a named body.

But responsibility presupposes the capacity to act. And the swing equation, run against the real loss, shows that at the inertia levels the framework accepts, the capacity to act has already expired before the responsible human can exercise it. At 102 GVA.s, a 3,600 MW Dogger Bank loss buys about **0.9 seconds** to automatic disconnection. The MIF papers derive a human-response floor of 3 to 5 seconds - the minimum time in which a control-room operator in a non-startle environment can perceive, orient and intervene. Nine-tenths of a second is not intervention time. It is the time it takes the protection relays to begin shedding customers while the operator is still reading the first line of the first alarm.

This is the state of affairs the 1,800 MW assumption conceals. Against the fictional loss, the modelled purchased time is longer, the operator appears to remain in the loop, the duty appears dischargeable by the body Parliament named. Against the real loss, the duty is being discharged - in the window that matters, the sub-second window in which the event is decided - not by NESO but by automatic under-frequency relays operating without human involvement, because there is no longer time for human involvement. Parliament assigned the system to a public body. The physics, at the operating point the framework has normalised for a loss half the real size, has already reassigned the decisive moment to a protection scheme.

The 1,800 MW fiction is therefore not merely an engineering understatement. It is the device by which a grid that has passed out of human control at its most critical moment continues to be described, in statutory terms, as a grid under human governance. Correct the loss to 3,600 MW and that description fails. Which is precisely why the loss is not corrected.

---

## 14. The Ethical Dimension

Strip away the equations and there is a plain ethical fact at the centre of this.

An engineering design basis is a promise. When a system is declared secure against its largest credible loss, the declaration is an assurance to the people who depend on that system - the hospital on the ward round, the signal box on the mainline, the household on the ventilator - that the worst credible thing has been thought about and built for. The largest credible loss is the mechanism by which that promise is made specific and testable. It is the number that says: *this is the worst we believe can happen, and we have built to survive it.*

To set that number at half the real value is to make the promise against a disturbance you have chosen for its survivability rather than its truth. It is to tell the ward and the signal box and the household that the worst has been planned for, while quietly defining "the worst" as something comfortably smaller than what the physical system can actually deliver. The people relying on the promise cannot check the design basis. They do not know that "largest credible loss" has drifted to mean "a loss we are confident we can survive" rather than "the largest loss that can credibly occur." They hear "secure" and they trust it.

The 2019 event is the proof that the stakes are not abstract. A million customers, 45 minutes, a hospital in the dark - and that was 1.4 GW, less than half the Dogger Bank figure, into a grid stronger than today's. The framework's response to that warning has been to relax the ceiling and hold the loss assumption fixed while the real losses on the system doubled. That is not caution exercised on behalf of the vulnerable. It is comfort purchased at their expense, and purchased silently, in a design assumption they will never read.

An honest framework designs for the storm it is actually building. It sizes the contingency to the physical worst case, publishes the floor that worst case demands, and if the floor is uncomfortable, it says so - because the discomfort is information, and the people relying on the grid are entitled to it. The 1,800 MW fiction withholds that information. It is the difference between an engineer who tells you the bridge is rated for the heaviest truck that can credibly cross it, and one who tells you it is rated for the heaviest truck he is confident it can carry.

---

## 15. Restoration Path - Size to the Real Loss, Publish the Honest Floor

The remedy is not exotic. It is the restoration of ordinary engineering discipline to a single number, and the propagation of that correction through the framework it sizes.

1. **Re-derive the largest credible loss from the present physical system.** Retire the 1,800 MW secured-event convention. Establish the current largest credible loss from the actual infeeds on the system - the HVDC-coupled offshore complexes, Dogger Bank foremost - and from an honest analysis of shared converter, busbar and connection-point infrastructure that determines whether the credible single loss is 2.4 GW, 3.6 GW, or larger. Publish the topology and the reasoning, so the figure can be checked from outside the building.

2. **Recompute the inertia floor against the real loss.** At the protection-design RoCoF ceiling of 0.125 Hz/s, a 3,600 MW loss requires ~720 GVA.s of intrinsic energy. That is the honest floor. It should be stated, defended, and held - not relaxed away through a redefinition of the ceiling the hardware never received.

3. **Denominate the floor in intrinsic energy that survives the disconnection test.** Follow the MIF framework: count toward the floor only the real stored rotational energy that survives severance of sensors, communications and firmware - GVA.s(i), not the undifferentiated GVA.s that lets synthetic response masquerade as stored mass. A doubled loss cannot be met by a doubled contract. It can only be met by real inertia.

4. **Re-run every downstream security assessment against the corrected loss.** Response volumes, operating floors, published security statements - all of them inherit the factor-of-two error and all of them must be recomputed. The results will be uncomfortable. That is the correction working.

5. **Correct the record, including our own.** The corpus's own MIF papers and the ministerial report that carried 1,800 MW, or carried 3,600 MW against a 360 GVA.s floor, are being corrected in the same pass as this critique. An argument for honest sizing that would not correct its own arithmetic would forfeit the right to make the argument.

6. **Build the floor the corrected loss demands.** 720 GVA.s of intrinsic energy against a 3,600 MW loss is a large number, and the synchronous fleet that once supplied it is retiring. The Twin Scroll Grid Balancer exists to supply exactly this - real stored rotational energy, sized deliberately, as a stability service rather than as a by-product of thermal generation. The honest floor is not an argument for despair. It is a specification. Something has to hold 720 GVA.s against Dogger Bank. The only question is whether the framework will admit the number and build to it, or keep the fiction and discover the truth the way Britain discovered it in August 2019, at more than twice the scale.

The path is not complicated. It is one honest number, correctly propagated. The difficulty is not technical. It is that the honest number is inconvenient, and the fiction is comfortable, and the framework has so far preferred comfort.

---

## 16. Manifesto - Design for the Storm You Are Actually Building

The largest credible loss is the promise a power system makes to the people who depend on it: *this is the worst we believe can happen, and we have built to survive it.* NESO's frequency-security framework makes that promise against 1,800 MW. The sea, through Dogger Bank, can deliver 3,600 - a single infeed larger than every reactor in Britain is generating this summer combined. The framework has built to survive half the storm it is actually building.

The swing equation is not a policy instrument. It does not negotiate, it does not relax, and it has not read the Frequency Risk and Control Report. Double the loss and it doubles the stored energy the grid must hold - from 360 GVA.s to 720 - and no market, no product, no redefinition of the RoCoF ceiling changes that, because none of them add a joule to the spinning mass that arrests the fall. You can relax the number in the document. You cannot relax the physics the document is supposed to describe.

Stop sizing the grid against the loss you can survive. Size it against the loss that can happen.

Stop grading the exam you set yourself against the question you removed from the paper. Restore the question.

Stop calling 102 GVA.s secure. Against the real largest credible loss it buys nine-tenths of a second before the relays take the grid away from the human being Parliament put in charge of it.

**Design for the storm you are actually building. Publish the floor it demands. And hold it in real mass, because the sea does not accept a firmware promise.**

---

## Related Documents

This critique targets the largest-credible-loss assumption underpinning NESO's frequency-security framework - the GB Security and Quality of Supply Standard secured-event convention and the Frequency Risk and Control Report 2025. It grants the framework's internal sophistication and locates the single stale input - the 1,800 MW largest credible loss - that halves every quantity derived from it, and corrects the corpus's own inheritance of the same figure.

### Companion Policy Analysis

- [The Managed Collapse of Inertia](0006 - The Managed Collapse of Inertia.md) - The FRCR 2025 rebuke; the GVA.s decline, the eightfold RoCoF relaxation, and why response cannot replace stored momentum. The direct companion to this document.
- [The 2050 Delusion](0005 - The 2050 Delusion.md) - The RoCoF wall moving toward the operating point; the market that cannot see the wall because the wall is not denominated in any currency it trades.
- [ESO - Governance Without Physics](0007 - ESO - Governance Without Physics.md) - The framework that answers to its own definitions rather than to the physical system; the general form of the marking-your-own-homework pathology.
- The Stability Market - 36 GVA.s of Inertia, Some of It Real - Where the largest-credible-loss figure was already flagged as under review "as multi-infeed losses become credible."
- An Ordered Queue for a Disordered Grid - The connected fleet that has its full complement of capacity and almost none of the intrinsic response to ride the loss.
- A Map Without a Substrate - Why a national inertia average conceals the regional inadequacy a local largest-credible-loss would demand.
- Fallen Through Every Rule - The regulatory gap: the intrinsic asset with no category to occupy.

### The Physics

- [Inertia](../Electrical Explainers/0003 - Inertia.md) - Stored kinetic energy as a state, not a service; the swing equation and the 2019 event in full.
- SCL and Fault Current - The declining synchronous fleet (~5 GW nuclear operational, end-of-life) and the stiffness that left with it.
- Phase Authority - Why anchoring phase and tracking phase are different, and why a fleet of trackers rides a loss worse than a fleet of anchors.

### The Proposed Engineering Response

- The Minimum Intrinsic Floor (MIF) - The swing-equation derivation of the floor; the source of the 360 GVA.s figure this document doubles, and the framework for counting intrinsic energy separately.
- Dynamic MIF - Sensitivity Analysis - How the floor behaves as loss, demand and synchronised mass vary; the storm biggest when the ship is lightest.
- MIF vs Current GB Outturn - The 360 GVA.s protection-design floor against actual outturn; the reconstruction of the inertia figure from public data.
- MIF in the Grid Code - The Secured Largest Loss as a defined, binding parameter rather than a number in a post-event report.
- Ministerial Report on the Minimum Intrinsic Floor - The statutory case; the document whose 3,600 MW loss and 360 GVA.s floor this critique reconciles to 720.
- TSGB White Paper (Full) - The intrinsic machine built to hold the floor the real largest credible loss demands.

### Statutory Framework

- Energy Act 2023 - Re-enacts the physical-outcome duty for NESO without redefining the physical conception of the grid.
- The Regulatory Gap - The connection categories of generation and storage, and the intrinsic-stability asset that fits neither.

### Data

- GridWatch telemetry archive - `gridwatch.templar.co.uk` - five-minute fuel-by-fuel output, 2011 to present, aggregating Elexon BMRS and National Grid settlement data. Nuclear output figures in section 5 are computed from this series as held in the GDA data lake.

---

*TSGB protected by 7 GB patent applications filed 20 September 2025 - All rights reserved. Do not reproduce or disclose without written permission from the author.*
