# The FRCR Breaches

### _Operating Below a Self-Certified Floor in Silence - The 102 GVA.s Ledger, January to June 2026, and the Confession Ofgem Cancelled - by Mark S_

---

**Target:** The operator's silent operation below the ~102 GVA.s inertia floor that its own Frequency Risk and Control Report proposed - and the suspension of the one document whose job was to admit it.
**Author:** M. Shirley, Independent Engineer & Inventor
**Status:** Independent analysis and polemic - not adopted regulation, not a submission to any process, not an allegation of wrongdoing against any individual.
**Companion:** [The Managed Collapse of Inertia](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md), [The 1,800 Megawatt Fiction](0021%20-%20The%201,800%20Megawatt%20Fiction.md), and [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md). Reconstructed from the public NESO `system_inertia` series via GDA, and settled against the live GDA server store and NESO's own raw resources (Section 11).
**Date:** 6 August 2026

---

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. The Ledger - What the Public Data Says, January to June](#2-the-ledger-what-the-public-data-says-january-to-june)
- [3. The Duck Curve - Price Above Mass](#3-the-duck-curve-price-above-mass)
- [4. The Number Is Theirs](#4-the-number-is-theirs)
- [5. By Whose Authority Was the Floor Breached?](#5-by-whose-authority-was-the-floor-breached)
- [6. What I Will Not Convict Them Of](#6-what-i-will-not-convict-them-of)
- [7. What I Will - The Silence](#7-what-i-will-the-silence)
- [8. The Days Nobody Was Watching](#8-the-days-nobody-was-watching)
- [9. The Consequence the Silence Bought](#9-the-consequence-the-silence-bought)
- [10. FRCR 2026 - The Confession Ofgem Cancelled](#10-frcr-2026-the-confession-ofgem-cancelled)
- [11. The Instrument, and What It Can and Cannot Say](#11-the-instrument-and-what-it-can-and-cannot-say)
- [12. A Familiar Shape - The Influence the Instrument Cannot See](#12-a-familiar-shape-the-influence-the-instrument-cannot-see)
- [13. What Honesty Would Have Looked Like](#13-what-honesty-would-have-looked-like)
- [14. Manifesto - A Floor You Cross Without a Word](#14-manifesto-a-floor-you-cross-without-a-word)
- [Related Documents](#related-documents)

---

## 1. Executive Summary

In [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) I defended the operator, and I meant it. Pointed at the 22-26 June heatwave, my own sealed instrument refused to convict NESO: the data was complete, it solved, and the system was not materially stressed. I would write that document again word for word.

This is not that document. This is the one the same instrument forces me to write next, because the instrument does not take sides and it has now been pointed at the rest of the year.

The *Frequency Risk and Control Report 2025* proposed a minimum system inertia floor of about 102 GVA.s - the lowest operating floor in the post-privatisation history of the British grid, and, as [The Managed Collapse of Inertia](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md) argued, already a surrender rather than a standard. The claim attached to that number was that it was a *floor* - a boundary held by procurement below which the system would not be run.

The public record for the first half of 2026 says otherwise. Through January, February, March, April and May the floor held, because winter and spring is when holding it is easy. Then, in June - the first low-inertia summer the floor had ever actually faced - NESO's own published Outturn Inertia fell **below 102 GVA.s on four separate days**, for roughly **twenty-five and a half hours in total**, reaching **81 GVA.s** on the morning of 17 June. Not the intrinsic, synchronous-only number I have spent two years arguing is the honest one. The operator's *own* headline figure - the generous one, the one that already counts market-provided and synthetic contributions in the same column as real spinning steel. Even the padded number went under.

And it went under for a reason the shape of the data makes plain: every breach is a duck curve. Cheap solar, winning the merit order at midday, displaced the synchronous gas that was carrying the inertia - the market pricing the megawatt-hour and blind to the stored mass, letting the marginal cost of a fuel override the minimum stability the operator had itself set. The floor did not sag under some slow structural tide. It was dispatched through, at noon, for price.

Here is the distinction this document exists to draw, and I will hold it with the same discipline I held the defence. **NESO cannot buy inertia.** The market it is required to operate has a slot for energy and a slot for response and no slot at all for stored mass. At two o'clock on a low-wind morning the operator cannot procure a single joule of the one thing that would help, because the framework provides no instrument with which to procure it. That is the framework's crime, established at length elsewhere, and I do not lay it at the operator's door.

But operating below your own certified floor is not the crime here. The crime here is operating below it **in silence.** On not one of those four days did the operator turn to the public and say the true and simple thing: *system inertia fell below the FRCR floor today; we held frequency with response, but we could not have held the floor itself, because the fleet to do it no longer exists and the market gives us no way to buy it.* That sentence costs nothing. It procures nothing, it fixes nothing, it is not within the operator's power to make untrue - and it is the one thing the operator could have done and did not. You cannot defend a man from a shortage he was forbidden to remedy. You can absolutely ask why he crossed his own red line without a word.

And the blackest part - the part that turns an omission into a pattern - is that there is a document whose entire statutory purpose is to make exactly this margin visible, and it would have had to report these breaches by name. It is the FRCR itself. The 2026 edition was suspended by Ofgem in March 2026, before the breaches happened, with no rescheduled date. The confession was cancelled three months before it came due.

I defended NESO from a lie. I will not defend it from its own silence.

---

## 2. The Ledger - What the Public Data Says, January to June

Start with the year, because the year is the context that makes June mean something.

NESO's `system_inertia` dataset publishes an Outturn Inertia figure every settlement period. It is the operator's total number, and it is the generous one: [The Stability Market](0012%20-%20The%20Stability%20Market%20-%2036%20GVAs%20of%20Inertia%2C%20Some%20of%20It%20Real.md) sets out why a figure that blends contracted and synthetic contributions into the same total is a market measurement rather than a physics one. I use it here deliberately, and against my own thesis, because if even the padded number breaches the floor, the argument needs no help from the honest one.

Monthly minimum Outturn Inertia, 2026 to date:

| Month | Minimum Outturn (GVA.s) | Below the 102 floor? |
| ----- | ----------------------: | :------------------- |
| January | 112 | No |
| February | 107 | No |
| March | 112 | No |
| April | 112 | No |
| May | 103 | No - by one |
| June | 81 (genuine) | **Yes - four days** |

The floor held for five months and broke in the sixth. That is not a coincidence of timing; it is the physics of the calendar. Inertia is tightest when synchronous plant is pushed off the bars, and synchronous plant is pushed off the bars on long, bright, low-demand days when solar floods the middle of the daylight hours and wind does the rest. Winter holds the floor up for free. Summer is the test. The floor met its first real summer in June 2026 and did not survive it.

The four breach days, from the same public series, each a complete 48-period day:

| Date (2026) | Below-floor window | Hours below 102 | Minimum (GVA.s) |
| ----------- | ------------------ | --------------: | --------------: |
| 17 June | 09:30 - 15:30 | 6.5 | **81** |
| 19 June | 10:00 - 15:00 | 5.5 | 86 |
| 21 June | 07:30 - 14:30 | 7.5 | 89 |
| 27 June | 10:00 - 15:30 | 6.0 | 91 |

Twenty-five and a half hours, on the operator's own generous measure, below the operator's own certified floor. The deepest point - 81 GVA.s, around half past ten on the morning of 17 June - sits roughly a fifth below the line FRCR 2025 drew and called secure. And four is the floor of the count, not its ceiling: as Section 11 sets out, NESO published only the two overnight periods on roughly a third of the days in this window, blanking the daylight hours in which a breach would show. These are the four breaches the public data lets anyone see. The true number is not smaller, and the structure of the missing data says it is larger.

Set against the de-massification timeline in [0006](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md) - about 260 GVA.s in 2016, 175 in 2020, 140 in 2023, the 102 floor written in 2025 - the public record for June 2026 reads 81. The operating point did not approach the floor and stop. It walked through it, on four ordinary afternoons, and the walk was not announced.

And the shape of those four afternoons is not random. Plotted, each breach is a duck curve - and the duck curve is the whole of the mechanism.

---

## 3. The Duck Curve - Price Above Mass

Plot the four breach days and the shape indicts the mechanism on sight. Each trough is a duck curve - inertia high through the morning, collapsing into a broad belly across the middle of the day, climbing back as the light fails. It is the mirror image of the solar-driven net-demand curve every grid engineer now knows by name, and the two do not share a silhouette by accident. The inertia trough *is* the solar belly, read in the one unit the market declines to price.

The causal chain is not subtle. The wholesale market dispatches on marginal price. Solar has a marginal cost of essentially nothing, so when the sun is high it wins the merit order and displaces the next unit in the stack. The next unit in the stack, in the middle of a June day, is gas - and gas, being a synchronous machine, is what was carrying the inertia. So the very economics that make solar attractive strip the stored mass off the bars at precisely the hour the sun is strongest. The floor did not break *in spite of* cheap solar. It broke *because* of it - or more exactly, because the market that dispatched the solar has no term in it for the mass the gas was providing. It prices the megawatt-hour and is blind to the megavolt-ampere-second. A cheaper, inertia-less megawatt beats a dearer, inertia-rich one every time, because the ledger the market keeps has no column for inertia. [The Stability Market](0012%20-%20The%20Stability%20Market%20-%2036%20GVAs%20of%20Inertia%2C%20Some%20of%20It%20Real.md) and [Pricing a Field You Can't See](0014%20-%20Pricing%20a%20Field%20You%20Can%27t%20See.md) set out that blindness at length. The June duck curve is what it looks like when it bites.

And notice what the shape rules out. The synchronous plant that was off the bars at noon was *on* the bars at breakfast and back on by dinner - that is precisely what the morning and evening shoulders of the duck curve are. The mass was not absent that day. It was available, it ran either side of the trough, and it was let go across the middle of the day because across the middle of the day it was the expensive fuel. This is the distinction that decides where the blame sits. The grid did not lack the iron on 17 June the way it lacks it on a dead-calm winter night with the fleet genuinely retired. It *had* the iron, ran it in the morning, and released it at noon for price. The choice - the marginal cost of a fuel set above the minimum stored mass the system needed to stay inside its own floor - was made somewhere in the dispatch chain, and the physics recorded the result at half past ten.

Then the turn that decides *whose* choice it was. The minimum the dispatch overrode - the 102 GVA.s - was not the regulator's number. Ofgem did not set it. NESO did, in FRCR 2025. And in that single instance the regulator did the right thing: it deferred to the operator's engineering judgement, because where the floor sits is an engineering question and deference to the engineer on an engineering question is correct. But deference is not diligence. Ofgem took NESO's floor, rubber-stamped it without a murmur - and then suspended the report that would have checked whether the number it had just blessed was being held. It endorsed the standard and cancelled the audit. Correct on the deference, absent on the verification, and the gap between the two is exactly the space in which a floor can be set, blessed, breached, and never mentioned.

So the paperwork is orderly. The floor is proposed by the competent authority, deferred to by the regulator, certified as secure, and carried forward in every document that matters. And at half past ten on the morning of 17 June, in the one place paperwork cannot reach, the stored rotational energy of the Great Britain power system read 81 GVA.s against a floor of 102. Physics is expressing a divergent view.

---

## 4. The Number Is Theirs

There is a defence available to the operator that is not available here, and it is worth killing it explicitly before anyone reaches for it.

The 102 GVA.s floor is not a number imposed on NESO from outside. It is not an Ofgem licence condition dropped on the operator's desk, nor a European standard, nor a figure a court handed down. It is the operator's own proposal, in the operator's own report. The Frequency Risk and Control Report is a NESO document. The ~102 GVA.s floor is the value NESO itself put forward as the minimum compatible with secure operation. In the language of my own [Inertia Inquiry](../Creative%20Outlet/0002%20-%20Clarke%20and%20Dawe%20-%20The%20Inertia%20Inquiry.md) sketch: *our number, we chose it, FRCR 2025 certified it as acceptable.*

That changes the character of the act. Crossing a line somebody else drew for you is a compliance question - you can argue the line was wrong, unreasonable, impossible. Crossing a line **you drew for yourself**, and certified as the boundary of security, and then said nothing when you stepped over it, is a different kind of act entirely. It is not non-compliance. It is self-contradiction, performed quietly. The operator told the regulator and the public that 102 GVA.s was the floor of safe operation, and then operated below it without amending the statement or flagging the breach. Either 102 was the floor, in which case June needed to be reported, or it was never really the floor at all, in which case the certification was theatre. The silence forces the choice, and neither branch flatters the operator.

---

## 5. By Whose Authority Was the Floor Breached?

There is a question the last two sections have been circling, and because it was asked, it is time to ask it plainly: *who authorised the System Operator to run the grid below its own security floor?* A prosecution that names the breach but not the authority behind it is only half a prosecution. This is the other half.

Begin with what is not in doubt. The System Operator has, and has always had, clear authority to override the economic merit order in the name of system security. It does it every hour of every day. When a thermal rating on a circuit would be exceeded, NESO constrains the cheapest generation off and pays dearer plant to run - the constraint-cost line in [Ninety Billion Pounds of Wire](0017%20-%20Ninety%20Billion%20Pounds%20of%20Wire.md), and the thousands of daily balancing actions behind it, are nothing but the operator overruling price for the physical integrity of the network. When a voltage limit is threatened, it acts. Thermal limits and voltage limits are *defined, delegated security constraints*: the operator holds an unambiguous instrument, an unambiguous authority, and an unambiguous obligation to hold them, and the market settles the bill without argument because everyone agrees those limits are real and that defending them is the operator's job.

Now ask the question the June duck curve forces. **Is the inertia floor a defined, delegated security constraint of that same kind - one the operator is authorised, instructed and obliged to defend against the merit order - or is it not?**

If it is, then on 17 June the operator held the authority to constrain synchronous gas onto the bars to hold 102 GVA.s, declined to exercise it, and the displacement moves back toward the operator's side of the ledger - a judgement call it owns, subject to the honest tension of the next section. But if it is *not* - if the inertia floor is a number NESO was permitted to *set* but never delegated the authority to *enforce*, a target with no constraint instrument bolted to it, no equivalent of the thermal-rating override, no line in the Grid Code that reads "the operator shall act to hold system inertia at or above the floor, and shall be paid to do so" - then something far worse is true. Then the operator was handed a security limit and denied the authority to defend it. Then, when solar displaced the synchronous mass at noon, NESO was not *choosing* price over mass. It was *watching* price displace a system security asset with no delegated power to intervene, because the power to intervene was never written. Then the breach was not a control-room decision at all. It was the predictable output of an authority gap.

And an authority gap, if that is what this is, has exactly one owner. The operator does not delegate authority to itself; the regulator delegates authority to the operator. If NESO was permitted to set an inertia floor but not granted the enforcement authority that every other security limit carries, that is not an operator failure. It is an **Ofgem failure to delegate** - the regulator defining a security standard, deferring to the operator's engineering judgement on its value (rightly, as Section 3 allowed), and then never completing the act by handing over the authority and the instrument to hold the thing it had just blessed. A security limit you are allowed to set but not to enforce is not a security limit. It is a wish with a number on it.

I do not, today, know which of the two it is, and I will not pretend to - the same boundary I drew around the physical claim in [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md). I do not have the Grid Code chapter and verse in front of me that settles whether the operator holds a delegated, paid, obligatory authority to constrain for inertia the way it plainly does for thermal and voltage, or whether inertia sits outside that machinery as an unenforceable aspiration. I argued in [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) that the control room behaved correctly through the heatwave, and I stand by that - for now. But "for now" is carrying weight in that sentence, because it remains to be seen exactly where the operator's authority stopped on the flanking days. Was NESO *forced* to displace a system security asset - the synchronous gas that carries the inertia - because it lacked the authority to do otherwise? If it was, the control room is exonerated further and Ofgem is indicted deeper. If it was not, the displacement is a choice and the accounting shifts onto the operator. The question is precisely answerable, from the Grid Code and the licence conditions, by anyone willing to sit down and trace where the authority runs out.

So here is the one recommendation this document presses with genuine urgency, above even *publish the FRCR*: **there must be an urgent review to define the situations in which the System Operator can, must, and will overrule the merit order to hold system inertia.** If a system security asset was displaced by solar purely on price - and the duck curve says one was - then either the operator held the authority to stop it, and the rules must state plainly when it is obliged to use it, or the operator lacked the authority, and the rules must grant it. There is no tolerable third state in which a security limit exists on paper, is breached in fact, and no one alive can say whether the operator was even permitted to prevent it. That third state is where the British grid appears to have been standing at half past ten on the morning of 17 June - and it is intolerable in a way that a single hot week, correctly handled, never was.

---

## 6. What I Will Not Convict Them Of

Let me be as scrupulous with the defence's remaining ground as I was in [0024](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md), because a prosecution that overreaches its evidence is exactly what I spend my time dismantling.

**I do not convict the operator of the low inertia itself.** The fact that GB inertia fell to 81 GVA.s on 17 June is not something NESO chose and could have avoided. The synchronous fleet has retired faster than its replacement can be built - coal gone, nuclear thinning, the steam plant that used to carry the mass largely off the system. On a bright, low-wind June morning the residual synchronous capacity simply is not there, and the operator has no lever that puts it back. As [Pricing a Field You Can't See](0014%20-%20Pricing%20a%20Field%20You%20Can%27t%20See.md) sets out, the market has no product called inertia; there is no auction the control room can clear at 10:30 to summon 25 more GVA.s of stored kinetic energy onto the bars. [Credit Where Due](0019%20-%20Credit%20Where%20Due%20-%20The%20Market%20Chose%20Steel.md) documents the few places real mass has been procured despite the framework, not because of it. The operator, on the day, could buy response. It could not buy substrate. When 81 GVA.s was the physical state of the system, that was the framework's doing and the fleet's arithmetic, not a decision anyone made in the control room that morning.

The duck curve of Section 3 complicates that concession, and I will not pretend it doesn't. On these particular days the synchronous plant was not absent - it ran in the morning and returned in the evening, and was released only across the solar belly, for price. So the honest position is narrower than a blanket exoneration: the operator cannot rebuild a fleet that has retired, and *that* I do not blame it for; but on a duck-curve day the iron that would have held the floor was on the system a few hours earlier and let go for economics, and holding it there - constraining gas on against the market, or curtailing cheap solar - was a lever whose *availability* is the open question I have just posed in Section 5. If the operator held delegated authority to pull it, the displacement is partly its own, exercised at a balancing cost the framework relentlessly pressures it to minimise. If it did not, the displacement is not the operator's at all; it is Ofgem's, for setting a floor it never armed anyone to defend. So the displacement sits in the shared space between operator and framework - a real choice, or a real absence of authority, and until the review of Section 5 is done I cannot in honesty say which. I place it there, unresolved and clearly marked, and move on, because the clean, undivided charge - the one that needs no such splitting, that survives every answer the authority review could return - is not the displacement. It is the silence.

So the *depth* of the breach is inherited, or at worst half-inherited. If this document stopped here, it would be one more entry in the case against the framework, and NESO would walk out of it exactly as it walked out of *The Wrong Scandal* - the constrained agent, holding up a system the framework has been undermining, denied the one tool that would help.

It does not stop here, because between the physical state and the public record sits one act that was entirely within the operator's power, cost nothing, procured nothing, and was not performed.

---

## 7. What I Will - The Silence

A floor exists to be a tripwire. Its whole function is the signal it sends when it is crossed. A tripwire that is stepped over in silence is not a tripwire; it is a line painted on the floor that everyone has agreed to ignore.

Watch how the operator treats its *other* red lines and the double standard becomes impossible to miss. When the system approaches an energy-margin shortfall - a Capacity Market Notice, a Margin Notice, an Electricity Margin Notice - the operator publishes it, loudly, in something close to real time, because the entire point of the notice is to be seen. The market is told, the press is told, the mechanism is designed for visibility. Energy shortfall is a red line NESO announces the instant it nears.

Inertia is a red line NESO crossed four times in June and mentioned not once.

The asymmetry is not accidental, and it is the same asymmetry every document on this shelf keeps finding. Energy is a *quantity the framework can measure and price*, so its shortfall has an instrument, a notice, a category of public alarm. Inertia is a *property the framework declined to measure or price* - the running theme of [0006](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md), [0012](0012%20-%20The%20Stability%20Market%20-%2036%20GVAs%20of%20Inertia%2C%20Some%20of%20It%20Real.md) and [0014](0014%20-%20Pricing%20a%20Field%20You%20Can%27t%20See.md) - so its shortfall has no instrument, no notice, and no ritual of alarm. The floor could be crossed silently *because the framework built no mechanism that would have made the crossing speak.* The property that has no price also has no alarm bell. That is not a coincidence. It is the same defect twice.

But here is where the operator cannot hide behind the framework. The absence of a *formal* notice mechanism for inertia does not impose silence. It merely fails to compel speech. Nothing stopped the operator from saying, in plain English on its own website on 17 June, that system inertia had fallen below the FRCR floor and why. NESO publishes operational commentary constantly. It published a full account of its own conduct through the 22-26 June heatwave - I quoted it approvingly in [0024](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md), the low wind, the gas outages, the EU interconnector permissions, the customers held on. The operator was perfectly capable of narrating a hard week when the narration made it look competent. It went quiet on the four days the narration would have made the *framework* look culpable and the floor look fictional.

That is the charge. Not that inertia was low - it had to be. Not that the operator failed to buy what it cannot buy. The charge is that the operator crossed its own certified floor and chose not to say so, when saying so was free, true, within its power, and damning of exactly the framework that put it in the position. The silence protected the framework. It did not protect the public, who were left to believe a floor was holding that had already broken.

---

## 8. The Days Nobody Was Watching

There is a detail in the timing that turns this from an indictment into an irony, and it is the detail that binds this document to [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) rather than contradicting it.

The four breach days are 17, 19, 21 and 27 June. The week the entire country spent July arguing about is 22-26 June. **Not one breach falls inside the contested window.** I checked, against the same public series: across 22-26 June the minimum Outturn Inertia was 119 GVA.s, the median 161, and not a single settlement period went below the floor. On 23 June itself - the day of the alleged hidden near-blackout - inertia bottomed at 139 GVA.s, comfortably clear of the line. My defence of the operator on the window stands, reinforced by a second independent reconstruction.

Now hold the two facts together. During the five days the whole political apparatus was watching, the inertia floor was intact. On the ordinary days flanking that window - three before it, one the day after it ended - the floor was breached, in silence, while nobody was looking.

The physics of why is almost too neat. The heatwave week was inertia-*safer* than the days around it, and for the exact reasons that made it a hard week to balance. Low wind and gas dispatched hard for the heat forced synchronous plant onto the bars; the tight conditions that had the operator phoning Brussels for interconnector room were the same conditions that kept real mass spinning. The breaches happened on the *cooler, clearer, easier* days on either side - 17, 19, 21, 27 June - when strong solar and returning wind pushed the synchronous fleet back off the system at midday and demand was slack. The single most dangerous inertia state of the month arrived not during the emergency everyone saw, but on a mild Wednesday morning nobody was reporting on.

This is *The Wrong Scandal* proven in the one quantity that matters. The mob picked the week the physics was fine and missed the four days the floor actually broke. And the operator, which published a detailed defence of its conduct on the safe week, published nothing on the breached days. Both halves of the country's attention - the accusers and the accused - were pointed at the wrong five days. The right four went by in silence, in the public data, uncommented, until now.

---

## 9. The Consequence the Silence Bought

An inertia floor is not a number for its own sake. It is a proxy for the one thing that matters when an infeed is lost: how fast the frequency falls before anything can act. The swing equation the operator's own tools use is linear and unforgiving - df/dt = f0 x deltaP / (2E), with E the stored kinetic energy.

At 81 GVA.s, the state of the system on the morning of 17 June:

- Against the framework's fictional 1,800 MW largest-credible-loss - the number [The 1,800 Megawatt Fiction](0021%20-%20The%201,800%20Megawatt%20Fiction.md) shows is half the real hazard - a loss produces about **0.56 Hz/s**. That is four and a half times the 0.125 Hz/s ceiling against which GB distribution protection was coordinated for most of the post-privatisation period.
- Against the real largest credible loss - a Dogger Bank infeed through shared HVDC, of the order of 3,600 MW - the same 81 GVA.s yields about **1.11 Hz/s**. That exceeds even the relaxed 1.0 Hz/s envelope the framework now tolerates, outright, before the response portfolio arrives.

So on 17 June the grid sat, on the generous measure, in a state where the design-basis loss it is actually exposed to would have driven a rate of change of frequency past the relaxed ceiling and nearly nine times past the historic one - below the operator's own floor, on an ordinary morning, and no one was told. Whether the system would have ridden a Dogger Bank loss in that state depends entirely on a response portfolio arriving after the first phase of the event, which [0006](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md) argues at length it cannot be relied upon to do. The point is not that a blackout was imminent. The point is that the margin between an ordinary June morning and the edge had thinned to a value the operator had itself certified as the floor, and then thinned past it, and the public were left believing the floor was holding.

---

## 10. FRCR 2026 - The Confession Ofgem Cancelled

I flagged the late FRCR in [0024](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) as the darkest joke in the affair. The June ledger makes it darker, because it turns the missing report from an embarrassment into a mechanism.

The Frequency Risk and Control Report is not an optional publication. It exists because of 9 August 2019 - Hornsea and Little Barford, frequency to 48.787 Hz, low-frequency demand disconnection operating, around a million customers off. Out of that came a duty: the operator must publish, regularly, an account of the risk of serious frequency events and how close to the edge the system is running. The FRCR is the one document whose entire statutory purpose is to make the margin visible. And a report on frequency risk that covered the first half of 2026 would have had no honest way to avoid these four days. The breaches are in the operator's own inertia outturn. An FRCR 2026 written in good faith would have had to put 17, 19, 21 and 27 June into the record, state that the ~102 GVA.s floor it proposed the year before had been crossed within twelve months, and explain why.

It will not have to, because there is no FRCR 2026. Ofgem suspended the 2026 requirement in March 2026, after the 2025 report was already late, with no rescheduled date. Read the sequence in order and the shape of it is unmistakable: the disclosure obligation was removed in March; the events that obligation would have disclosed occurred in June. The confession was cancelled three months before it came due.

I am careful with intent, because I cannot see inside the room and I will not pretend to - the same line I held for the whistleblower in [0024](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md). I do not allege that anyone suspended the FRCR *in order to* avoid reporting breaches that had not yet happened. I allege something structurally worse, because it needs no bad actor: the framework is arranged so that the single instrument capable of forcing the inertia floor into daylight can be switched off by the regulator, quietly, for administrative reasons, exactly when the floor is about to fail - and the switching-off attracts none of the alarm that the failure would have. A near-blackout on 23 June that did not happen generated a Shadow Secretary of State, a whistleblower, leaked documents, the House of Lords and three weeks of front pages. Four genuine breaches of the safety floor in the same month, and the suspension of the report that would have named them, generated nothing, because the framework provides no mechanism through which either could speak. The wrong scandal had a megaphone. The right one does not even have a report.

That is the completion of the point I have been making for two years. The framework does not merely fail to procure inertia. It fails to *see* it, fails to *price* it, fails to *alarm* on it - and, when the last remaining instrument that would have written it down becomes inconvenient, it turns that instrument off with a routine letter and no one notices. The floor did not just break in June. The gauge that reads the floor was unplugged in March.

---

## 11. The Instrument, and What It Can and Cannot Say

I hold my own evidence to the standard I demand of everyone else's, so here is exactly what these numbers are and are not.

The breaches are read from NESO's published `system_inertia` Outturn figure, and I have now settled this ledger three ways: against my local capture, against the live GDA server - the authoritative store the acquisition daemon writes to - and against NESO's own raw CSV resources that sit beneath both. All three agree to the digit. Every one of the four breach days is a **complete 48-period day** in NESO's own publication, with a smooth, physically-plausible diurnal profile - high inertia through the morning, a broad minimum across the middle of the day as solar peaks, recovery into the evening. They are troughs, not spikes, and they are not an artefact of my instrument: they are in the numbers NESO itself published, and any party can pull the same resource and reproduce them.

I have **excluded** one apparent breach that the physics rejects, and the settled pull tells me more about it than I knew before. On 1 June 2026 the series reports a sustained collapse to 43 GVA.s - the first two periods normal at 164 and 160, then a cliff to the low-40s held for twenty-two hours. At 43 GVA.s a routine infeed loss would produce a rate of change of frequency approaching 0.8 Hz/s and no such event occurred; the reading is physically impossible, and the same isolated sub-60 GVA.s signature recurs in the 2022 and 2023 records. What the raw source now settles is that this is not my error: the 43 sits in NESO's own published CSV, at source. It is a NESO publication error, not a GDA one - which is its own small indictment of how closely the operator's inertia outturn is watched by anyone, the operator included. I set it aside on physics, and the four breaches stand without it, on the most conservative reading of the series.

And the settled pull forces a correction I owe honestly. In [the heat-window study](0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md) I logged the recent-weeks thinning in the inertia feed as a probable behaviour of my own instrument - correction C2 - and, to be safe, excluded it from any claim about NESO's data. The raw source shows I was too generous to the operator. The thinning is NESO's own. From 18 May 2026, on roughly every other day - nineteen days across May and June - NESO's published inertia outturn carries only the first two settlement periods, SP1 and SP2, the small hours after midnight, and nothing else. The entire daylight span of those days, the hours in which every breach in this document occurs, was never published at all. The four breach days stand out precisely because they are days NESO happened to publish in full. This carries a hard consequence I must state plainly: **four breaches is a floor, not a total.** On nineteen days across those two months the operator did not publish the hours in which a breach would show, and on the two periods it did publish - the overnight peak - the floor is never troubled. Whatever the true count of sub-102 days in June 2026 is, it is not less than four, and the shape of the missing data means it is very likely more. The same dependence touches the window cross-check of Section 8: 22, 24 and 26 June are among the partial days, so that check rests on the full days within the window, 23 and 25 - enough to confirm the contested week did not breach, but I flag what it leans on.

One further thing the settled pull establishes, and it belongs here. As of the acquisition on 20 July, NESO had published no inertia outturn at all beyond 30 June. Its own record of how close the system runs to its own floor is weeks behind, thinned on a third of its days, and carrying at least one physically-impossible day it has not corrected - in the very window in which the FRCR that would summarise it stands suspended. The gauge is not merely unplugged, as Section 10 had it. The sensor feeding the gauge is itself intermittent, delayed, and in one place plainly broken. Everything this document says about the *floor* being unwatched turns out to apply to the *data on the floor* as well.

One last caveat, cutting the other way, because honesty runs in both directions: everything here is the **Outturn** figure, the generous one. The intrinsic, synchronous-only inertia - the honest number the whole [MIF](../Proposals/MIF) argument is built on - was lower than 81 GVA.s on those afternoons, and breaches the floor more often and more deeply than this ledger shows. The instrument understates the case against the framework. It does not overstate it.

---

## 12. A Familiar Shape - The Influence the Instrument Cannot See

I have kept, throughout, to the line I drew in [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md): the instrument sees the grid, not the room. It speaks to fact - was the data thinned, was the floor breached, was the system stressed - and it is silent on conduct, on who said what to whom, on whether anyone leaned on anyone. I hold that line here. What follows is not a finding. It is a shape, offered as a shape, and marked as one from the first word to the last.

The whistleblower's account carried an allegation of *outside influence*. The cover-up story welded that allegation to a physical claim - a hidden near-blackout on 23 June - and [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) took the physical claim apart: there was no near-blackout, the data solved, the system was not stressed. So if there was influence, it was not influence to conceal an operational danger, because the danger the story described was not there to conceal. That much the instrument does settle. It leaves a question it cannot: if not that, then influence about what?

This document has, without setting out to, assembled a candidate - and I present it as a candidate, nothing more. Consider the reputational position the June physics creates. Solar is setting records: the policy's proudest number, the visible proof the transition is working. And on the very days it sets those records, the grid it feeds is too de-massified to absorb it - the synchronous mass that holds the frequency floor has to be kept on the bars, or brought back onto them, against the cheap solar that is displacing it, and on the days that management fails the floor breaks. Say *that* plainly and you have a communications problem with two headlines and no good one. The first is *solar curtailed, solar constrained, solar fails* - poison to the renewable narrative the whole policy edifice exists to project. The second is the true one - *the grid is too weak to accept the solar it built* - poison to the framework that built the weakness. Two toxic stories, aimed at two different institutions, and no version of the day that flatters anyone.

Faced with two toxic headlines and no good one, the path of least institutional resistance is not to choose between them. It is to see that neither gets written - and the way you achieve that is precisely the pattern this document has recorded from the outside without ever asking why. You do not publish the inertia data that would force the story: the feed thins to the overnight hours on a third of the days, freezes after 30 June, and carries an uncorrected impossible day. You do not file the report that would summarise it: the FRCR is suspended. You do not narrate the curtail-and-constrain days: the operator that published a detailed, creditable account of the heatwave it handled well says nothing at all about the ordinary days it crossed its own floor. I am not asserting that any of those things was *done in order to* suppress a story. I am observing something narrower and, in its way, heavier: that if someone had wished to suppress it, the observable state of the record is indistinguishable from what they would have produced.

And here is the one new thing this reframing offers the conduct question - offered, and then handed straight back to the people who can actually reach it. In [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) I said the influence, if any, was not operational, because the control room ran the physics correctly - and I stand by every word of it. But influence over a *narrative* is a wholly different act from influence over an *operation*, and it lives in a wholly different part of an organisation. Operational influence is engineers pressing engineers about how the system is run. Narrative influence is the reputational and communications function pressing on what is said and shown about how it ran. Those are not the same people, not the same act, and not the same allegation - and an inquiry that has spent three weeks aimed at the first has not, as far as any of this can tell, turned to look at the second. The instrument cannot see either; I say again, plainly, that it cannot. But the *shape* of what the instrument can see - the thinned feed, the frozen report, the unnarrated breach - sits more comfortably beside a reluctance to tell a reputationally toxic story than beside an operational cover-up of a danger the physics says was never there.

That is the shape, and I will not inflate it past a shape. I name no one, because it is not for me to say who, if anyone, applied anything, and the distance between *an institution with an incentive* and *a person with a hand on the scale* is the entire distance between analysis and accusation - a line I will not cross with an instrument that cannot see across it. But an incentive this strong, lying this precisely over a record this quiet, is at least worth an inquiry knowing the shape of before it clears the building. The scandal was pointed at the wrong target once already. It would be a poor outcome if, having missed the operational target because there was nothing there to hit, it also missed the reputational one because no one thought to describe its shape.

---

## 13. What Honesty Would Have Looked Like

It is cheap to prosecute and expensive to say what should have been done, so here is the sentence the operator could have published on 17 June 2026, and every day like it:

> *System inertia fell below the FRCR floor of ~102 GVA.s today, to a minimum of 81 GVA.s across the middle of the day. Low-cost solar displaced the synchronous plant that carries the system's inertia, and we did not constrain enough of it back onto the bars to hold the floor: the balancing cost of doing so is real, and the floor - unlike an energy-margin breach - carries no penalty and no alarm to weigh against that cost. Frequency was held within statutory limits throughout using contracted response. And we record plainly that on a genuinely low-fleet day we could not have held the floor at any price, because the market gives us no product through which to procure stored mass. This is a structural condition of the system as currently configured, and it will recur on low-wind, high-solar days until that configuration changes.*

Every clause of that is true. Every clause is within the operator's power to write. It procures nothing and fixes nothing - and it would have done the one thing that matters: told the public the truth about the margin they are standing on. It would have been damning of the framework and exonerating of the operator's competence, which is precisely the division of responsibility [0024](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) spent twenty sections establishing. The operator that landed the heatwave plane and rightly said so could have flagged the broken floor and rightly explained it. It did the first and not the second, and the only difference between them is which institution the truth embarrasses.

And the regulator should not have suspended the FRCR. A framework that has relaxed its RoCoF ceiling eightfold, halved its floor toward a seventh of the real requirement, and priced no product for the fix, does not then get to switch off the one report that would have shown the public the result. Publish the FRCR. Reinstate the duty. If the number it would have to report is embarrassing, the embarrassment is information the public is entitled to - the discomfort is the reading on the gauge, and unplugging the gauge does not lower the temperature. And commission the authority review of Section 5 as a priority, not a footnote: write into the Grid Code the conditions under which the operator can and must overrule the merit order to hold system inertia, so that the next time a security asset is displaced by price there is a plain answer to the question of who was authorised to stop it - and an obligation on someone to do so.

---

## 14. Manifesto - A Floor You Cross Without a Word

I defended the operator when the charge was a lie, and I meant every word of it. I hold it to account now the charge is true, and I mean this just as much, because the credibility of the first depends entirely on the willingness to write the second.

The framework took the operator's ability to hold the floor. That is the framework's crime, and I have prosecuted it for two years and will prosecute it still. But the framework did not take the operator's ability to *tell the truth about not holding it.* That remained, on every one of those four days, free and available and unused. You cannot buy inertia you were never given a market to buy it in. You can always say, out loud, that you have run out of it. One of those failures belongs to Ofgem and DESNZ. The other belongs to the operator, and no amount of framework-blame will move it off their desk.

The floor held for five months and broke in the sixth, four times, in silence, on the days nobody was watching, while the report that would have named the breaches sat cancelled since March. That is not a procurement failure. That is a disclosure failure wrapped inside a procurement failure, and only the outer layer is anybody else's fault.

> **You cannot buy the mass. You can always tell the truth about not having it. They bought silence with the one currency the framework left them, and silence was the one thing the public could not afford.**

---

## Related Documents

- [The Managed Collapse of Inertia](0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md) - the FRCR 2025 critique this ledger tests against the outturn record.
- [The 1,800 Megawatt Fiction](0021%20-%20The%201,800%20Megawatt%20Fiction.md) - the largest-credible-loss basis behind the RoCoF figures in Section 9.
- [The Wrong Scandal](0024%20-%20The%20Wrong%20Scandal%20-%20In%20Defence%20of%20NESO%2C%20Against%20the%20Cover-Up%20Story.md) - the operator defence this document is the necessary counterweight to; the 22-26 June window cross-check in Section 8 is its corroboration, and the control-room authority question in Section 5 is its unfinished business.
- [The 22-26 June 2026 Heat Window](0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md) and [the pre-registered protocol](0022%20-%20METHOD%20-%20June%202026%20Heat-Window%20Forensic%20Protocol%20(Pre-Registration).md) - the method and honesty standard the instrument note in Section 11 inherits.
- [The Stability Market](0012%20-%20The%20Stability%20Market%20-%2036%20GVAs%20of%20Inertia%2C%20Some%20of%20It%20Real.md), [Pricing a Field You Can't See](0014%20-%20Pricing%20a%20Field%20You%20Can%27t%20See.md), [Credit Where Due](0019%20-%20Credit%20Where%20Due%20-%20The%20Market%20Chose%20Steel.md) - why the operator cannot procure the mass, and the one place it was procured anyway.
