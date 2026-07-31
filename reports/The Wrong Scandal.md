# The Wrong Scandal

### _In Defence of NESO, Against My Own Instincts - Why the 22-26 June "Cover-Up" Does Not Survive the Public Data, and Why the Operator Is Being Scapegoated for a Framework Ofgem and DESNZ Built to Fail - by Mark S_

---

**Target:** The July 2026 political and press campaign alleging that the National Energy System Operator (NESO) hid a near-blackout during the 22-26 June 2026 heatwave and falsified its records - and, standing behind it, the regulatory framework that made the operator a scapegoat available for exactly this use.
**Author:** M. Shirley, Independent Engineer & Inventor
**Status:** Independent analysis and polemic - not adopted regulation, not a submission to any process, not an allegation of wrongdoing against any individual.
**Companion:** [The 22-26 June 2026 Heat Window - Data Quality and System Stress Against a Trailing-12-Month Baseline](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md) - the pre-registered forensic note this blog stands on.
**Date:** 30 July 2026

---

## Table of Contents

- [1. Executive Summary](#1-executive-summary)
- [2. A Confession, and the Line I Will Not Cross](#2-a-confession-and-the-line-i-will-not-cross)
- [3. What Actually Happened, 22-26 June](#3-what-actually-happened-22-26-june)
- [4. The Instrument I Pointed At Them](#4-the-instrument-i-pointed-at-them)
- [5. The Test I Sealed Before I Looked](#5-the-test-i-sealed-before-i-looked)
- [6. The Verdict On The Data: It Solves](#6-the-verdict-on-the-data-it-solves)
- [7. The Verdict On The System: Not Stressed](#7-the-verdict-on-the-system-not-stressed)
- [8. The Three Honest Signals - Because A Real Defence Names The Nuance](#8-the-three-honest-signals-because-a-real-defence-names-the-nuance)
- [9. What My Study Cannot Say - And Will Not Pretend To](#9-what-my-study-cannot-say-and-will-not-pretend-to)
- [10. So Why The Circus?](#10-so-why-the-circus)
- [11. The Impossible Job](#11-the-impossible-job)
- [12. Independence Is Only In The Plan](#12-independence-is-only-in-the-plan)
- [13. The Man In The Chair](#13-the-man-in-the-chair)
- [14. Where The Real Scandal Lives](#14-where-the-real-scandal-lives)
- [15. Who Benefits From The Wrong Scandal](#15-who-benefits-from-the-wrong-scandal)
- [16. The FRCR, Missing, In The Middle Of A Frequency Row](#16-the-frcr-missing-in-the-middle-of-a-frequency-row)
- [17. A Word To The Whistleblower](#17-a-word-to-the-whistleblower)
- [18. What Honesty Would Actually Look Like](#18-what-honesty-would-actually-look-like)
- [19. Comparative Table - The Two Scandals](#19-comparative-table-the-two-scandals)
- [20. The Objections, Answered](#20-the-objections-answered)
- [21. Manifesto - Defend The Operator, Prosecute The Framework](#21-manifesto-defend-the-operator-prosecute-the-framework)
- [Related Documents](#related-documents)

---

## 1. Executive Summary

I have spent the better part of two years prosecuting the way Britain runs its electricity system. I built a machine to do it. I have written that the system operator's founding review was governance without physics; that the largest-credible-loss the whole security framework rests on is a fiction half the size of the real number; that the inertia floor has been quietly relaxed toward a value that hands the grid to automatic relays before a human can act. I do not retract a word of it. Every one of those documents is still on the shelf, and every one of them is still right.

And now I am going to defend NESO.

Not the framework it sits inside - I will prosecute that harder in this document than I ever have. The operator. The people in the control room on the week the whole country is now arguing about. Because in the last three weeks a Shadow Secretary of State, a whistleblower, a small mountain of leaked documents and a great deal of front-page certainty have converged on a single claim: that during the record heatwave of 22-26 June 2026 the grid came within a whisker of blacking out, that NESO ran the system beyond safe limits, that senior managers ordered the control room to hide the risk, and that the records were cooked to cover it up.

I am one of the very few people outside the building who can actually check the physical half of that claim, because I already had the instrument pointed at exactly that week. In April 2026 I disclosed GDA - a system that reconstructs the state of the GB grid from public data alone. On 25 July, in direct response to Ofgem's 14 July transparency notice, I ran a pre-registered forensic study of the 22-26 June window: the method was sealed to version control by commit *before a single result was computed*, and it tested two narrow, falsifiable questions against the preceding twelve months. Was the published data worse that week? Was the physical system more stressed that week?

The answer, in both cases, is no.

The published data covering 22-26 June was **complete** - generation, demand and one-second frequency present in full on every window day, the full 86,400 frequency samples each day, nothing thinned, nothing missing. It was **internally consistent** - across more than sixteen thousand independent state-estimator solves the published measurements cohered into a physically valid grid state on every day, chi-square passing in every settlement period, with **zero bad-data rejections**. And the system was **not materially stressed** on the great majority of measures: inertia adequate, demand *below* the annual median, balancing costs unremarkable, and frequency inside the statutory band for every second of every day. The one genuine system signal of the entire week - a real spike in frequency volatility on 23 June - is not hidden anywhere. It is sitting in the open, in the one-second frequency trace that anyone with a browser can download, at the 98th percentile of the year and still comfortably within statutory limits.

So here is the plain finding, and I will state it as coldly as I stated the finding against the framework: **in the period in question, the grid was not less stable, and the public record was not less honest, than on an ordinary day.** The "hidden risk data" was not hidden. It was published, it was complete, and it solved.

That is the first half of this document, and it defends NESO.

The second half prosecutes the people this fake scandal is protecting. Because a grid operator handed a shrinking synchronous fleet, a largest-credible-loss that has doubled to exceed the entire live nuclear output of the country, a RoCoF ceiling relaxed eightfold, an inertia floor drifting toward a seventh of what the real loss demands, and a market with no category to buy the one thing that would help - that operator has an impossible job. It did that impossible job, through the hottest week of the year, on low wind, with gas out and interconnectors adverse, and it kept every single customer connected. It even had to go to the European Union for permission to breach interconnector trading limits to do it. That is not a cover-up. That is an operator being crushed inside a straitjacket the regulator designed, and holding the system up anyway.

The scandal being fought is that NESO hid a bad week. The scandal being avoided is that Ofgem's framework and DESNZ's Net Zero policy have guaranteed a bad decade - and that the operator's much-advertised "independence" exists in the org chart and in the maths of the plan, and nowhere near the desk of the person balancing the system at two o'clock on a low-wind morning. The fake scandal is a gift to the exact people the real one would implicate. That is why it is being fought so loudly, and that is what this document is about.

I am defending NESO from the lie. I am prosecuting the framework for the truth. Those are not in tension. They are the same act.

---

## 2. A Confession, and the Line I Will Not Cross

Let me be honest about how strange this is for me to write, because the strangeness is the point.

The masthead of my policy work is a stack of documents with titles like *Governance Without Physics*, *The Managed Collapse of Inertia*, *The 1,800 Megawatt Fiction*, *The 2050 Delusion*. I did not choose those titles to be gentle. I have called the operator's founding review "the institutional codification of physical detachment." I have written that the framework "answers to its own definitions rather than to the physical system," that it has built "a grid governed by intent, not inertia," that it grades an exam it set itself against the question it removed from the paper. If there is a person in Britain with less reason to leap to NESO's defence, I have not met them.

So understand that when I say the cover-up story is bullshit, I am not saying it because I am on their side. I have spent two years being emphatically not on their side. I am saying it because I built the one tool that can test the physical claim, I sealed the test before I looked, and the data came back clean. When your own instrument, pointed at your own least-favourite institution, refuses to convict them, you have two choices. You can quietly put the instrument away and let the mob have its afternoon. Or you can say what the instrument says.

I am going to say what the instrument says. That is the whole of my method and it is the whole of my credibility. A man who has published "here is the framework's stale number and here is the physics that indicts it" does not then get to publish "here is a hot week and here is the physics that convicts the operator" *only when the physics does no such thing*. The swing equation does not take sides, and neither do I. It indicted the framework. It exonerates the operator. Both are in this document, and both are load-bearing.

Now the line, because a defence without a limit is a whitewash, and I have accused other people of whitewashing.

**I am defending the physical record of 22-26 June. I am not vouching for anybody's minutes, anybody's culture, or anybody's conversation.** There are two allegations in the air. One is about *fact* - whether the data and the system showed anything abnormal that week. That one is answerable from outside the building, and I have answered it. The other is about *conduct* - whether records were poorly kept, whether risk information was suppressed, whether decision-making was improperly leaned on. That one cannot be reached by any measurement I own, and I will not pretend otherwise. No reconstruction from public data can tell you what someone said to someone else in a control room, or whether a manager put a thumb on a report. If a person inside NESO genuinely experienced pressure to shade the truth, that is a real and serious matter and it deserves a real and serious hearing, and nothing in my study calls that person a liar.

What my study does is narrower and harder: it removes the *physical* claim from underneath the conduct allegation. The story being told is not "the culture was bad." The story being told is "the culture was bad *and therefore the grid nearly went down and they hid it*." The second clause is a physics claim. The physics claim is false. And once you take the false physics claim away, what is left is a workplace-conduct question that should be heard on its own merits, in its own forum, without a phantom near-blackout strapped to its back inflating it into a national-security scandal it is not.

That is the line. Defend the record. Prosecute the framework. Leave the conduct question to the people who can actually see the conduct, and refuse to let it borrow a physics it does not have.

---

## 3. What Actually Happened, 22-26 June

Start with the weather, because the weather is the one thing in this story nobody disputes.

The week of 22 June 2026 was not a warm spell. It was the hottest June in the English record. The Met Office logged a provisional 37.7 C at Lingwood in Norfolk on 26 June - the hottest June day ever recorded in the United Kingdom, and the sixth-hottest UK day of any month, ever. A Red Extreme Heat Warning was issued on a record third consecutive day on 25 June. There were seven consecutive days above 30 C, from 21 to 27 June. My own reconstruction confirms the premise in its own data: taking the hottest grid cell in Great Britain each day, the five window days reached 35.7, 37.6, 37.5, 38.1 and 36.5 C - every single one hotter than all 362 baseline days in the preceding year. On temperature, the window sits at the 100th percentile. It was, unambiguously, the most extreme stretch of the year.

Now the grid, in NESO's own published account, which I have no reason to dispute and every reason to quote. Across that week the system experienced sustained pressure from a genuinely nasty combination: low wind generation, reduced availability of some gas plant, high sustained demand, adverse interconnector flows and network constraints, all at once, in record heat. Frequency moved outside the *normal* operating range - which is exactly what it is supposed to do under stress; the normal range is a comfort band, not a safety limit. The lowest recorded value across the week was 49.66 Hz and the highest was 50.23 Hz. The statutory lower limit is 49.5 Hz. The level at which automatic customer disconnection begins is 48.8 Hz. So the worst instant of the worst week of the year sat 0.16 Hz above the statutory floor and 0.86 Hz above the disconnection trigger.

To manage that week, the control room did what a control room is for: it engaged the market, called on demand flexibility, deployed reserve, traded with neighbouring system operators and instructed the interconnectors. On the 24th and the 26th it had to go a step further and seek permission from the European Union to breach the intraday interconnector trading limits, because the ordinary limits did not leave enough room to balance the system. Hold that fact in your hand for a moment, because it will matter later: to keep the lights on during a record heatwave, the operator of a sovereign nation's grid had to phone Brussels and ask to exceed a trading cap. That is not the signature of an operator hiding how easy its week was. It is the signature of an operator scraping every last tool off the shelf.

And the outcome NESO states, plainly: no customer demand was disconnected, frequency stayed within statutory limits, voltage stayed within limits, and no lines or cables were overloaded. Nobody lost supply. The hottest, tightest week of the year ended with every customer still connected.

That is what actually happened. Everything else - the whistleblower, the leaked documents, the "beyond safe limits," the "scaremongering," the lawyers - is interpretation laid on top of that outcome. And the useful thing about an outcome that leaves a physical trace is that the interpretation can be checked against the trace. That is what the next four sections do.

---

## 4. The Instrument I Pointed At Them

Most of the people commentating on 22-26 June are working from press briefings and leaked slides. I am working from the grid.

GDA - Grid Data Analysis - is the system I disclosed to NCSC, DSIT, Ofgem, NESO and DESNZ on 11 April 2026 through the responsible-disclosure channel, and briefed to NCSC on 19 April. It ingests thousands of discrete public data sources - the generation mix, the metered interconnector flows, national and settlement-level demand, the published one-second system frequency - normalises them to a common time domain, and anchors everything to the frequency trace. On top of it sits a state estimator: for every half-hour of GB operation, it takes the published measurements, weights them by their stated uncertainties, and solves for the electrical state of the network that best fits all of them at once. This is the same class of tool - weighted least squares state estimation - that a real control room runs internally. The difference is that mine runs entirely on public data, on commodity hardware, from outside the building.

That matters here for one specific reason. When the accusation is "NESO hid the true state of the system," the natural rebuttal is "well, only NESO can see the true state of the system, so we just have to trust the inquiry." That rebuttal is wrong, and GDA is why it is wrong. The true state of the system is over-determined by public data. Generation is published. Demand is published. Interconnector flows are published. Frequency is published at one-second resolution. Feed all of that to a state estimator and the physics does the rest - because a grid state either reconciles all those independent measurements within their uncertainties or it does not, and if the published numbers had been massaged to hide a stressed system, the massage would show up as *inconsistency*: measurements that no longer fit together, residuals that no longer close, solves that fail or throw out data. You cannot quietly hide stress in a system whose inputs are all public and all mutually constraining. The lie would leave a fingerprint in the residuals.

For this study I did not just run the estimator over the window. I built and published a full solved-state library - **GDA-SOLVES** - covering 370 days at roughly 46 periods a day: 17,328 solves, 99.9% of them converged, each one carrying its input public measurements, its solved grid state, its residual diagnostics, and per-solve provenance including the estimator build and the data hashes. Every solved instant obeys a hard rule the whole GDA project is built on: the no-forward-inference horizon. Every state in the library is at least a week old by construction; the instrument is a historian, not a forecaster, and it never touches an instant fresh enough to be operationally sensitive. The point of publishing the library is that you do not have to take my word for any of this. Any party - NESO, Ofgem, a journalist, a hostile critic - can re-run any solve and reproduce its objective and its state, or challenge it. The reconstruction is not an opinion. It is a computation, and it is open.

This is the second time in this saga I have found myself as the one person outside the establishment holding a working reconstruction of the thing everyone else is arguing about from the outside. I do not particularly enjoy the position. But it does mean that when I say the June data solves, I am not offering a vibe. I am offering sixteen thousand solves and inviting you to break one.

---

## 5. The Test I Sealed Before I Looked

Here is the part that separates this from a man with a spreadsheet and a grievance.

The single easiest way to lie with data is to compute a hundred things, notice which three support the story you already wanted to tell, and publish those three. It is so easy that most people who do it do not even know they are doing it; the human mind is a machine for finding the pattern it went looking for. The only known defence against it is to decide, in writing, *before you look at any result*, exactly what you are going to measure, exactly how, and exactly what would count as a finding - and then to timestamp that decision in a way you cannot later alter. That is pre-registration, and it is the reason this study can be trusted where a press leak cannot.

The full protocol lives in a companion document, [0022 - the June 2026 Heat-Window Forensic Protocol](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0022%20-%20METHOD%20-%20June%202026%20Heat-Window%20Forensic%20Protocol%20%28Pre-Registration%29.md). It was sealed to version control by a commit that predates, in the repository history, the commit that computed a single comparison. The commit ordering *is* the integrity claim. The method-sealing commit came first; the result-producing commit came second; the timestamps are public and immutable. I could not have tuned the method to the answer even if I had wanted to, because the method was frozen before the answer existed. If you want to attack this study, that is where you attack it - go to the history, check the ordering, and if the seal came after the result, I am a fraud and you should say so. It did not.

What the sealed method committed me to, in brief:

- **Two hypotheses, and only two.** H1: was the public data materially different in quality, completeness or internal consistency that week? H2: was the physical system materially more stressed that week? Each is framed as a neutral null the study *tries to falsify*. I was not looking to exonerate NESO. I was looking to catch a difference, and pre-committing to report it whether I caught one or not.
- **A twelve-month baseline.** The 365 days immediately before the window - 22 June 2025 to 21 June 2026 - one settlement day at a time. The window is judged against the year that produced it, not against a vibe of what a normal day feels like.
- **Two lenses.** All-days, and heat-matched - the roughly 37 hottest baseline days - so that when I judge a non-temperature metric I can control for "well, it was hot," and not mistake a weather effect for a system effect.
- **A strict materiality bar.** A window day only counts as a finding if it sits beyond the 95th or below the 5th percentile of the baseline. That is a deliberately high bar, chosen to bias the study toward *under*-claiming - toward missing a real signal rather than inventing a fake one. And regardless of the bar, the exact percentile rank of every metric is reported, so nobody can accuse me of hiding a near-miss behind a threshold.
- **Three transparent corrections, all logged before the results they could affect.** C1: I moved the temperature metric from a national spatial mean, which washes out a regional extreme, to the national daily maximum-cell, which does not - a correction that made the heat *look worse*, i.e. against my eventual finding, not for it. C2: I recognised that my completeness axis measures what my research lake *ingested*, not directly what NESO *published*, and I excluded a recent-weeks thinning in the inertia feed from any NESO attribution because it is a known behaviour of my own instrument, not a window event. C3: I excluded several convenience metrics that embed a present-day fleet snapshot, because ranking them across historical baseline days would be invalid.

Read C1 and C2 again, because they are the tell. A dishonest study makes every judgement call in the direction of its conclusion. This one made its corrections in the direction of *making the operator look worse and the instrument look weaker*, and did so in writing before the results were known. That is not what advocacy looks like. That is what an instrument built to be trusted looks like. I biased the study toward catching NESO out, sealed it, and it still did not catch them out. That is the strongest thing I can say about the finding, and I earned the right to say it by making it hard to reach.

---

## 6. The Verdict On The Data: It Solves

The first allegation, stripped of adjectives, is that "system risk data was hidden." So test it directly. Was the published data for the window missing, thinned, or degraded relative to the year? And did it hang together, physically, as well as it does on an ordinary day?

**Completeness first.** For the three feeds whose ingestion into my research lake is robust - generation mix, national demand, and one-second system frequency - the window is complete and indistinguishable from an ordinary day. Generation and demand carried every settlement period on every one of the 365 baseline days and all five window days. The one-second frequency record was complete on all five window days: the full 86,400 samples each day, which is exactly the baseline median and the baseline fifth percentile. There is no gap. There is no thinning. There is no missing partition on any window day on any of these feeds. If someone at NESO was hiding the state of the grid by not publishing it, they did a remarkably poor job, because they published all of it, at full resolution, every day of the week in question.

I will be scrupulous here, the way the sealed method requires me to be. My completeness axis measures what is present in my data lake, which depends on both what NESO published and how my lake ingested it - the two cannot be separated from inside the lake. There is a feed - system inertia - that thins over the most recent five weeks of my capture, fourteen partial days between 18 May and 20 June, a pattern that *begins before the window* and is a known recency behaviour of my instrument, not a window-specific publication event. I excluded it from any statement about NESO's data, and I am telling you that plainly rather than letting a quirk of my own pipeline masquerade as a NESO failure. The completeness finding rests on generation, demand and frequency, whose ingestion is complete across the whole period. Even after handing the prosecution that caveat for free, the data is complete.

**Now the harder test - internal consistency, the part least confoundable by ingestion and the real heart of the matter.** For every half-hour, I fed the published metered generation, interconnector flows and demand to the state estimator and looked at how well the day's published numbers cohere within their stated uncertainties. The measure is the reduced chi-square: near or below one means consistent; a materially higher value on a given day would mean that day's published data fit together less well - the fingerprint you would expect if numbers had been shaded. Every half-hour of the window and of the full 365-day baseline was solved with one pinned estimator build - more than sixteen thousand solves.

The result: **the published data for the window is internally consistent.** On every one of the five window days, the chi-square consistency test passed in every settlement period, and there were **zero bad-data rejections** - not a single published measurement had to be discarded as inconsistent on any window day. The published numbers reconcile into a coherent grid state, every day, with nothing thrown out. If the risk had been hidden by massaging the published measurements, the massage would have shown up right here, as inconsistency the estimator could not reconcile. It did not show up, because it is not there.

Two honest nuances live inside that clean result, and I report them because the sealed method requires it and because a defence that hides its own nuance is worth nothing. First, a calibration note: the reduced chi-square runs below one across the whole year - baseline median 0.36 - which means the published measurements' stated uncertainties are conservative. So I use it as a *relative* index of internal tension between days under an identical model, which is valid, and not as an absolute goodness-of-fit score, which it is not. Second, on that relative index the window does sit in the upper part of the year's range, and one day crosses the strict bar. Here are the numbers, in full, nothing withheld:

| Window day | Reduced chi-square (median) | All-days percentile | Heat-matched percentile | Bad-data removals |
|---|--:|--:|--:|:--:|
| 22 Jun | 0.485 | **96.7** | **97.3** | 0 |
| 23 Jun | 0.462 | 93.7 | 91.9 | 0 |
| 24 Jun | 0.430 | 88.2 | 78.4 | 0 |
| 25 Jun | 0.444 | 90.7 | 81.1 | 0 |
| 26 Jun | 0.432 | 88.2 | 78.4 | 0 |

(Baseline median 0.359, P95 0.468, independently re-derived.)

On 22 June the day's published measurements were marginally *less* internally tight than a typical day and a typical hot day - the 97th percentile on both lenses, just past the strict bar. The other four days are elevated but do not cross it. The plain reading, which I will not dress up in either direction: the published data solves into a coherent grid state on every window day with nothing rejected, while carrying slightly more internal tension than usual, most pronounced but still only marginally so on 22 June. That is a property of how well the numbers agree with each other. It is emphatically **not** a failure of the data to solve, and it is not evidence of concealment - concealment would degrade consistency badly and fail solves, and instead every solve passed and nothing was removed. What it is, is the faint texture you would expect from a hot, high-embedded-generation summer week, reported at the top of the normal range because that is where it honestly sits.

So: the data was published, it was complete, and it solved. The claim that risk data was *hidden* does not survive contact with the data that was, in fact, right there the whole time.

---

## 7. The Verdict On The System: Not Stressed

The second allegation is that the physical system was run "beyond safe limits" - that the grid was, in reality, in a materially more dangerous condition than usual and that this danger was papered over. So test the danger directly, against the twelve-month baseline, on the metrics that can be ranked honestly.

| Metric | Window range | All-days rank | Material? |
|---|---|---|---|
| Minimum system inertia | 119-165 GVA.s | 24th-86th percentile | No - adequate throughout |
| Peak national demand | 29.3-31.8 GW | 37th-50th percentile (below annual median 32.1 GW) | No (all-days) |
| Worst modelled RoCoF | 0.27-0.38 Hz/s | 14th-76th percentile | No |
| Daily balancing cost (BSUoS) | GBP 1.4-11.2 m | 10th-75th percentile | No |

Read it and the picture is dull, in the best possible way. System inertia was adequate throughout - never near the low tail of the year, sitting in the ordinary middle of the distribution. Peak demand ran *below the annual median*, which surprises people until they remember that British peak demand is a winter phenomenon and summer cooling load in a country with little air conditioning is small; a hot June day is simply not a high-demand day in GB terms. The modelled worst-case rate of change of frequency was ordinary. Balancing costs were unremarkable. On the metrics that actually characterise system stress, the hottest week of the year looks like a normal week of the year.

The one metric that crosses the bar does so only in the heat-matched lens: peak demand ranks at the 84th to 100th percentile *among comparable hot days* on 22-25 June. But read that honestly and it evaporates as a stress signal. It does not mean demand was high; demand was below the year's median and far below its winter peaks. It means demand was high *for a hot day* - the expected modest cooling response, exactly what physics predicts when it is 38 C. That is a signal about weather-driven demand, not about a system under threat, and the two-lens design is precisely what lets you tell the difference. An honest instrument reports it and then tells you why it does not mean what a headline would want it to mean.

Then there is the measured frequency record, which supplies the single genuine system signal of the entire week - and I want to hand it to the prosecution deliberately, because it is the closest thing to their case and it still does not make it. Taken straight from the one-second frequency, the maximum measured rate of change of frequency was ordinary on four of the five days, 62nd to 81st percentile. But on **23 June it reached 0.112 Hz/s - the 98th percentile of the year on all days, and the highest of any comparable hot day.** That is a real, measurable spike in frequency volatility. It is the most frequency-active day of the window, and I will not wave it away.

But read it in proportion, which is what an engineer does and a headline does not. Frequency never left the statutory band on any window day - the seconds spent beyond 49.5 to 50.5 Hz were zero on all five days, exactly as on a normal day. The day's data still solved and still passed every consistency test. And 0.112 Hz/s is well inside the protection thresholds; it is a fraction of even the historic 0.125 Hz/s design ceiling, and a small fraction of the relaxed ceilings the framework now tolerates. So 23 June was a genuine deviation worth recording - the busiest day the frequency had all year - and it was not a statutory event, not a security event, and not a near-blackout. It was a hard day, handled, within limits.

Put the two verdicts together. The data was complete and it solved. The system was not materially stressed. In the period everyone is now shouting about, the grid was not less stable, and the record was not less honest, than on an ordinary day. That is not me being generous to NESO. That is the sealed instrument, pointed at NESO, refusing to convict them - and I would be a liar and a coward to have built the instrument, run it, and then not told you what it said because the answer was inconvenient to the story everyone wanted.

---

## 8. The Three Honest Signals - Because A Real Defence Names The Nuance

The difference between a defence and a whitewash is that a defence tells you where the case against it is strongest and deals with it in the open. There are exactly three signals in the window that sit near the top of the year's normal range. A whitewash would bury them. I am going to put all three on the table and tell you precisely what each one is and is not, because if I do not, someone will find them and wave them as a smoking gun, and they are not one.

**Signal one: 22 June, the data was slightly less internally tight than usual.** The reduced chi-square sat at the 97th percentile on both lenses - just past the strict bar. What it means: on 22 June, the published measurements agreed with each other marginally less well than on a typical day. What it does *not* mean: it does not mean the data failed. Every solve passed. Zero measurements were rejected. The grid state reconstructed cleanly. This is a relative-tension observation at the top of the normal band, not a break. Its cause is out of scope for my instrument - it could be anything from a slightly noisier metering day to the ordinary consequence of high embedded generation making the national picture harder to reconcile. It is a texture, not a fault.

**Signal two: 23 June, elevated measured frequency volatility.** The max measured RoCoF hit 0.112 Hz/s, 98th percentile all-days, top of any hot day. This is the realest signal in the window and I have already given it a full paragraph in Section 7. Here is the part that actually demolishes the cover-up theory rather than merely surviving it: **this signal is in the public record.** It is derived from the published one-second frequency trace - a feed anyone on earth can download, that NESO published in full, all 86,400 samples, on the very day in question. The single most system-relevant fingerprint of the entire week is not hidden. It is the most open number in the whole story. You cannot simultaneously believe that NESO conspired to conceal the risk of 23 June *and* accept that the sharpest measure of 23 June's risk is sitting in NESO's own published data at one-second resolution for anyone to compute. The theory refutes itself on the one day it most needs to be true.

**Signal three: demand a little high for a hot day.** Heat-matched, peak demand ranked 84th-100th percentile among comparable hot days, 22-25 June. What it means: people turned on fans and the modest amount of cooling the country has. What it does not mean: it does not mean the system was demand-stressed - demand was below the annual median and nowhere near the winter peaks that actually size the system. This is a weather signal wearing a system signal's coat, and the two-lens design is what takes the coat off.

Three signals. All within limits. None a statutory breach, a data failure, or a security event. Together they are not the fingerprint of a concealed emergency. They are the faint, physically-plausible fingerprint of a hot, high-embedded-generation summer week - exactly, and only, what the physics predicts. I report them at the top of the normal range because that is where they honestly sit, and I refuse to let anyone inflate them into the thing they are not. That refusal is the defence. Naming them is how you earn it.

---

## 9. What My Study Cannot Say - And Will Not Pretend To

I have accused the framework, at length and in writing, of overreaching its evidence - of dressing an assumption as a finding, of grading itself against a question it removed. I would be exactly what I have condemned if I let this defence overreach its own evidence. So here, plainly, is the boundary of what I have proven, marked as clearly as I can mark it.

**My study speaks to fact, not conduct.** It answers "was the published data degraded, and was the system materially stressed?" It cannot answer "did a manager tell an operator to keep quiet, were the minutes of a decision meeting properly kept, was someone leaned on to soften a report?" Those are questions about human behaviour inside a building, and no reconstruction from public data can reach them. My instrument sees the grid. It does not see the room.

So I am not telling you the whistleblower is lying. I am not telling you the record-keeping was immaculate. I am not telling you no manager ever put a thumb anywhere. Those may be true or false and I have no instrument that can say which, and I will not borrow the authority of the physics to pronounce on things the physics cannot see. That would be the exact move I have spent two years prosecuting - claiming a rigour you have not got for a conclusion you happen to want.

What I *am* telling you is that the conduct allegation, as it has been sold to the public, comes welded to a physical claim - that the grid nearly went down on 23 June and the danger was hidden - and that the physical claim is false. The grid did not nearly go down. The danger, such as it was, is in the open record. So whatever the conduct question turns out to be, it is not "they concealed a near-blackout," because there was no near-blackout to conceal. Strip the false physics off the conduct allegation and you are left with a workplace-culture question that should be investigated properly and calmly, on its own evidence, in its own forum - not a national-security thriller.

There is a further honesty I owe, because the sealed method demands it and because I would want it demanded of anyone else. My instrument has real limits. A substantial part of every half-hourly measurement set is pseudo-measurement - per-bus demand allocated from a national shape, and all reactive power, at loose uncertainties, because there is no public reactive telemetry and no per-site demand metering. That dilutes the consistency signal: an elevated residual reflects tension chiefly among the *metered* rows, and the pseudo rows soften it. My thermal limb is descriptive only - there is no dynamic-rating model in my estate, so I make no claim that any asset did or did not breach a heat-derated limit. And my reduced chi-square is a relative index, not an absolute test. None of these limits is hidden in a footnote; each sits next to the finding it bears on, in the companion note, where a hostile reader can use it against me. I would rather hand you the weaknesses of my instrument than have you think I am pretending it is omniscient. It is not. It is honest, and honest is a different and better thing.

---

## 10. So Why The Circus?

If the physics was fine, why has the last month looked like the physics was on fire? Walk the timeline, because the shape of it is the story.

The heatwave ran 22-26 June. On 2 July, the specialist commentary began - a well-known independent energy blog flagged that NESO's decision to cut exports during a low-frequency event might come back to bite in winter, a legitimate technical debate about interconnector policy. On 7 July, it stopped being technical: Shadow Energy Secretary Claire Coutinho went public with a whistleblower "at the heart" of NESO, alleging that senior managers had ordered control-room operators to hide information showing the grid was not being run securely, and wrote to the Information Commissioner's Office alleging that NESO was avoiding keeping proper records of how operational decisions were made. Bloomberg ran "UK Lawmaker Accuses Grid of Cover Up That Risked Blackout." On 14 July, Ofgem issued a transparency notice and NESO's chief executive, Fintan Slye, commissioned the law firm Eversheds Sutherland to conduct an independent investigation. On 15 July, Energy Minister Michael Shanks told MPs there had been no "emergency situation" on 23 June and called it "scaremongering" to suggest the country was close to blackouts. By 17 July the critics had reframed a company hiring its own lawyers to investigate itself as "marking their own homework." On 20 July the row reached the House of Lords. In the days after, leaked documents were reported as showing that engineers had been "forced to run the grid beyond safe limits," and Coutinho branded the whole inquiry a "sham," asking - not unreasonably - why it was being run by NESO's chosen lawyers rather than by Ofgem or the department, and who was setting the terms of reference. Then, on 29 July, the story widened again: NESO had *missed* the deadline for its Frequency Risk and Control Report, and had been released from its obligation to publish a ten-year electricity supply statement after missing two deadlines.

Now stand back from the sequence and ask the only question that matters: **what is this fight actually about?**

Look closely and you will see that almost none of it is about the physics of the week. It is about records. It is about who told whom to say what. It is about whether a minister was misled, whether a report was softened, whether an inquiry is independent, whether deadlines were met. It is a fight about *governance and conduct and process* - and every one of those is a fight you can have indefinitely, because none of it is settled by a number. Meanwhile the one part of the story that *is* settled by a number - was the grid actually in danger, was the data actually hidden - has been quietly assumed rather than checked, because assuming it is what powers the rest.

This is the tell. When a scandal is real and physical, the physical evidence leads and the governance argument follows. When a scandal is manufactured or inflated, the governance argument leads and the physical evidence is *asserted* - "beyond safe limits," "risked blackout" - and never actually reconstructed, because reconstructing it would end it. Nobody in this row has published a reconstruction of 22-26 June. I have. And the reconstruction says the physical premise underneath the entire circus - dangerous grid, hidden data - is false.

Which does not mean nothing happened in that building. It means the thing being fought about and the thing that actually happened are not the same thing, and the gap between them is being filled with heat because heat is politically useful. Section 15 is about who it is useful *for*. But first, the fact that should generate sympathy rather than suspicion for the operator: the job NESO was doing that week was very close to impossible, and it is impossible by design.

---

## 11. The Impossible Job

I have been harder on NESO's framework than almost anyone alive. So let me be the one to say the thing its critics in Parliament will not, because it does not fit their story: **the operator did an impossible job that week, and it did it well.**

Consider what the control room was actually handed on 22-26 June. Record heat - the hottest June in the English record, 38 C at the hottest cell. Low wind, so the renewable fleet that now dominates the energy market was largely absent exactly when it was hottest. Reduced availability of some gas plant, so the dispatchable backup was thinner than usual. High sustained demand for a summer, the cooling response biting. Adverse interconnector flows, the neighbours pulling the wrong way. Network constraints, the wires themselves limiting what could be moved where. And underneath all of it, the structural condition I have documented for two years: a synchronous fleet that has been retiring faster than its replacement can be built, an inertia base thinner than it was in 2019, and a market with no mechanism to procure the one thing that would have made the week easy.

Now watch what the operator did with that hand. It engaged the market. It called demand flexibility. It deployed reserve. It traded with neighbouring system operators. It instructed the interconnectors. And when the ordinary interconnector trading limits did not give it enough room, it went to the European Union and got permission to breach them - twice, on the 24th and the 26th. It reached past the edge of its own normal toolbox and borrowed room from a neighbour to hold the system up. And at the end of the hottest, tightest week of the year, the outcome was: nobody disconnected, frequency in limits, voltage in limits, nothing overloaded.

That is not the performance of an organisation that had a near-death experience and covered it up. That is the performance of a highly competent operator doing an impossibly constrained job and just barely getting away with it every single day, because "just barely getting away with it" is now the *design condition* of the British grid, not an emergency. The margins are thin because the framework made them thin. The operator did not choose the thin margins. The operator inherited them, and then spent a record heatwave holding the system inside them by main force and international goodwill.

Here is the cruelty of the politics. The very fact that the week required extraordinary effort - the EU calls, the reserve, the flexibility, the constant balancing - is being read by the prosecution as evidence that the week was secretly a disaster. But effort is not disaster. A pilot who lands a heavily loaded aircraft in a crosswind at night with one engine degraded, and taxis to the gate with every passenger safe, has not had a disaster he is covering up. He has done a hard job well. The sweat on his brow is not evidence of a crash. It is evidence of the skill that prevented one. NESO landed the plane, every day, for a week, in the worst conditions of the year, and is now being accused of hiding a crash that did not happen because the landing was visibly hard.

And the reason the landing was hard is the subject of every document I have ever written. The operator was flying an aircraft the framework had been stripping of ballast for a decade. That is not NESO's crime. In large part it is NESO's inheritance. Which brings us to the thing the operator's defenders and its prosecutors both keep getting wrong: what "independent" actually means here, and how little of it the operator actually has.

---

## 12. Independence Is Only In The Plan

The National Energy System Operator was stood up in October 2024 as an "independent public corporation," the culmination of Ofgem's 2021 System Operation Review and the Energy Act 2023. The word "independent" is doing enormous work in this story - it is why a whistleblower's allegation lands as "the independent operator lied," why a minister can be accused of being misled by "the independent operator," why the whole affair reads as an autonomous body caught in a wrongdoing of its own. So it is worth saying, precisely and unfashionably, what that independence actually is and is not.

Independence, in any meaningful sense, requires the capacity to act on your own judgement toward your own objectives with your own tools. NESO has none of the three in the sense that matters.

**Its objectives are set upstream.** The operator does not choose the Net Zero pathway; DESNZ does. It does not choose the economic and regulatory framework it runs inside; Ofgem does. It does not choose the largest-credible-loss convention it designs against, the RoCoF ceiling it is permitted to tolerate, or the market categories through which it is allowed to procure stability - all of that is set by the framework the 2021 Review built and the 2023 Act codified. The operator is handed a remit it did not write and asked to deliver it. That is not independence. That is agency, in the delegated sense - an agent executing a principal's instructions.

**Its tools are chosen for it, and the one it needs most does not exist.** I have written this at length elsewhere and I will compress it here: the grid's stability, in the moment that matters, is set by stored rotational energy - inertia - and by the largest loss the system must ride through. The market NESO is required to operate has slots for energy and slots for response services, and no slot at all for intrinsic stored mass. There is no procurement vehicle for substrate. So when the operator looks at a low-wind, low-inertia night and knows, in the physics, that what it needs is more real spinning mass, it cannot buy it, because the framework provides no category in which to buy it. It can only buy more of the response products that arrive *after* the first phase of an event. The operator is told it is responsible for a physical outcome and denied the one instrument that would secure it. Responsibility without the means to discharge it is not independence. It is exposure.

**Its accountability is diffuse by construction.** When the lights flicker, no single entity owns the fault. NESO manages the response, Ofgem manages the compliance, DESNZ manages the narrative. Each operates within its mandate. The system operates outside the conditions that produced the last major event, and there is no entity whose specific job it is to prevent the next one. I called this the accountability mirage when I was using it against the framework. It cuts exactly the same way in the operator's defence: an operator embedded in a structure designed so that responsibility diffuses cannot be the sole author of a system-level outcome, because the structure was built precisely so that no one is.

So here is the sentence that I think is the truest thing in this whole affair, and I mean it as both defence and indictment: **NESO's independence exists in the org chart and in the mathematics of the plan, and nowhere near the desk of the person balancing the system at two o'clock on a low-wind morning.** On paper - in the Review, in the Act, in the corporate structure, in the press release that announced the "independent public corporation" - the operator is free. In the plan - in the modelled pathways, the tidy scenarios, the spreadsheets where the inertia always somehow adds up - independent operation is real, because in a plan you can assume the tool exists. In the control room, on the night, with the fleet retired and the wind low and the market offering you response you cannot use for a problem that is already over by the time it clears, the independence is a fiction. The operator is not free. The operator is trapped inside a framework that wrote it a job it cannot fully do and then gave it a nameplate that says it can.

That is why the cover-up story is not just factually wrong but *structurally* wrong. It imagines an autonomous operator making a free choice to conceal a danger. The real operator is a constrained agent executing an upstream framework's instructions with an incomplete toolbox, and the "danger" it is accused of concealing is one it neither created nor could have bought its way out of. You cannot scapegoat an agent for the sins of the principal. But that is exactly what is being attempted, and the next section is about why it is so attractive to attempt it.

---

## 13. The Man In The Chair

There is a sketch in my own creative folder - [The Inertia Inquiry](https://github.com/MarkS0485/TSGB-2026/blob/main/Creative%20Outlet/0002%20-%20Clarke%20and%20Dawe%20-%20The%20Inertia%20Inquiry.md), written in the manner of Clarke and Dawe - and it is, I have come to realise, the truest single thing I have written about where NESO sits. Two chairs. No set. One country without power. An interviewer, and a man from the operator, being walked line by line through a blackout. And the genius of the form - the reason Clarke and Dawe endures - is that the man in the chair is not a villain. He is not shifty. He is not even embarrassed. He is a decent, competent, entirely sincere official, doing his level best to answer for a set of decisions he did not make, in a vocabulary that has been carefully engineered to distribute accountability, in his own words, "to a point where it becomes mathematically undetectable."

That is how I see NESO. That is the position they are in. Not the liar in the dock. The man in the chair.

Watch what the form does to him. Every honest answer he gives makes him look worse, because the chair itself presumes guilt. He explains that the inertia floor was "our number, we chose it, FRCR 2025 certified it as acceptable" - and it lands as an admission, when it is really the recitation of a parameter handed down to him by a framework he did not author. He explains that the batteries "responded beautifully, within specification" - and it lands as spin, when it is the literal truth about a tool he was given instead of the tool he needed. He reaches for "unscheduled demand-side reconnection event" not because he is a weasel but because the entire institutional language he has been issued is built to soften physical facts into governance abstractions, and he has been marinated in it for so long that it is simply how the operator is required to speak. The euphemisms are not his character flaw. They are his uniform. Somebody upstream sewed them.

And here is the part that matters for July 2026, the part that makes the real version more absurd than the sketch: in the sketch, at least there was a blackout. The man in the chair is answering for an eleven-hour failure that actually occurred. In the real world of 22-26 June 2026, they have put the operator in the chair to answer for a catastrophe **that did not happen at all.** The data was complete. The system was not stressed. Every customer stayed connected. And still the chair was set out, the folder was opened, the lawyers were retained, the Lords convened, and the operator was made to sit down and account, in the presence of the nation, for a disaster that exists only in the framing. The witness chair is the punishment, and being placed in it is the verdict, and the evidence was never going to be allowed to change either. That is what it means to be the available scapegoat: you can be summoned to confess even when there is nothing to confess to, because the summoning is the point.

Now ask the question the sketch asks by never showing them: who is *not* in the chair? BEIS set the policy. Ofgem regulated the framework. The operator ran the system inside the framework Ofgem regulated under the policy BEIS set. So who was responsible? "Collectively, all three - which in practice means none of them." The 2021 Review that started it all - the document in which the word "inertia" appears, by the sketch's count, once, glancingly, in a hundred pages about operating a machine whose entire behaviour is governed by it - that document has no chair. Its authors have no chair. The people who set the terms of reference that omitted a minimum inertia floor, who relaxed the RoCoF ceiling eightfold, who priced a market with no slot for the one thing the grid needs - none of them will ever be walked line by line through anything, because the framework was built, with real care, so that accountability diffuses before it can reach them. The operator is in the chair precisely *because* it is the only body concrete enough to sit in one. Everyone upstream has been abstracted into a process, and you cannot subpoena a process.

That is the cruelty the sketch sees and the news does not. The man in the chair is the most visible, most sincere, most answerable figure in the whole structure - which is exactly why he is in the chair and the actual authors of the risk are at home. Visibility is not culpability. Answerability is not authorship. The operator can be made to account for everything and be the author of almost none of it, and the format is designed to make that distinction impossible to see, because the person sitting down and explaining themselves *looks* like the person who did it. Clarke and Dawe built an entire comedy on that gap between looking responsible and being responsible. July 2026 is that comedy, played straight, with a real operator in the chair and a real framework nowhere to be found - and, this time, without even a blackout to justify the interrogation.

So when I say "defend the operator," this is the image I am defending against. Not a guilty man protesting innocence. A sincere man in a chair he was put in by people who will never sit in one, being made to answer in a language they issued him, for an event that did not occur, while the authors of the actual risk watch from outside the room. Get him out of the chair. Then go and find the people who built it, and sit *them* down, and ask *them* why "inertia" appears once.

---

## 14. Where The Real Scandal Lives

If you want to know why I am willing to defend NESO on 22-26 June, understand that it is because I am unwilling to let a fake scandal about one hot week bury the real scandal I have documented for two years - a scandal that is structural, published, ignored, and vastly more dangerous than anything the whistleblower alleges.

Here is the real scandal, in four moves, each of which I have set out in full elsewhere and each of which is derivable today from public data using the operator's own equations.

**One: the largest-credible-loss the entire security framework is built on is a fiction.** The framework sizes the grid against a largest single infeed loss of the order of 1,800 MW - a number inherited from an era of thermal units and first-generation interconnectors. That world is gone and the number did not move with it. The real largest credible loss today is the Dogger Bank complex, delivered through shared HVDC infrastructure - of the order of 3,600 MW, and 2,400 MW even on the most conservative common-landing reading. To make that concrete: a single Dogger Bank infeed loss is *larger than the entire live output of Britain's nuclear fleet*, which through the summer of 2026 has been sitting at around 3,000 MW. One offshore wire can take off the system more than every reactor in the country is generating combined. The framework is built to survive two-thirds of that.

**Two: the required inertia floor doubles with the loss, and the framework has let it fall to a seventh.** The swing equation is linear in the loss: double the disturbance and you double the stored energy needed to ride it at the same rate of change. Riding a real 3,600 MW loss within the historic 0.125 Hz/s protection ceiling requires about 720 GVA.s of real inertia. The framework does not ask for 720. It does not ask for the 360 the fictional 1,800 MW loss would demand. It is drifting toward a floor of about 102 GVA.s and calling it secure - roughly a seventh of the honest number.

**Three: the RoCoF ceiling was relaxed eightfold to make the falling floor look adequate.** For most of the post-privatisation period, GB distribution protection was coordinated against 0.125 Hz/s. As inertia fell and the real rate of change of frequency rose, the ceiling was progressively relaxed - toward 1.0 Hz/s for credible-event purposes under the Frequency Risk and Control Report 2025. The grid did not get eight times stronger. The threshold got eight times more permissive. No joule of stored energy was added. The number in the document changed; the physics did not.

**Four: the fix is the one thing the market cannot buy.** Every one of these problems has the same solution - real synchronous stored mass, sized to the real loss. And the framework has no category in which to procure it. The catalogue has slots for energy and for response. Substrate has no slot, no price, and therefore no procurement. The grid needs the one thing the market was not built to sell.

*That* is the scandal. Not a hot week where the data was fine. A framework that grades its own homework against a question it removed from the paper, that has let the safety floor fall to a fraction of what the real hazard demands, that relaxed the ceiling to keep the paperwork green while the actual margin shrank, and that structurally cannot buy its way back to safety. It is enormous, it is documented, it is public, and it has generated almost none of the political heat that one hot week has generated in three weeks.

And here is the sharpest irony, the one that should make anyone genuinely worried about grid security furious at the *shape* of this row rather than its target. The phrase the critics reached for to attack NESO's Eversheds inquiry was "marking their own homework." It is the exact phrase I have used, for two years, to describe the *framework's* central pathology - a body that must demonstrate security also choosing the contingency against which security is demonstrated, and letting it drift to a size that guarantees a pass. The real marking-your-own-homework in British grid policy is not a company hiring lawyers to review one week. It is a security framework that sets, sits and marks its own exam every year and has quietly removed the hardest question. The critics borrowed the right phrase and pointed it at the wrong scandal.

---

## 15. Who Benefits From The Wrong Scandal

Follow the consequences, because consequences reveal purpose more reliably than motive ever does.

Suppose the story that wins is: *NESO hid a bad week.* What follows? An inquiry - ideally one NESO commissioned itself, so it can be dismissed as a whitewash and the row can run for months. A lessons-learned exercise. Some new record-keeping obligation. Perhaps a governance tweak, a strengthened reporting line, a resignation if the pressure gets high enough. The operator absorbs the damage. The story is "a public body behaved badly and is being held to account." And crucially - *the framework is never mentioned.* Ofgem's 1,800 MW convention is not examined. DESNZ's Net Zero pathway is not questioned. The inertia floor is not recomputed. The people who built the structure that made the margins thin walk away entirely clean, because the story was never about them. It was about the operator's conduct in one week, and the operator took the hit.

Now suppose the story that wins is the true one: *the framework guarantees a bad decade.* What follows from *that*? An admission that the largest-credible-loss is double what the framework designs against. A recomputed inertia floor of 720 GVA.s that the current system misses by a factor of seven. An acknowledgement that the market has no category to buy the fix. A hard look at the RoCoF relaxation, the retiring synchronous fleet, the Dogger Bank exposure. In other words, a story that implicates Ofgem's framework and DESNZ's policy directly, expensively, and by name - and that cannot be closed by a governance tweak because the problem is physical and the bill is measured in gigavolt-ampere-seconds of real mass that somebody has to build.

Look at those two outcomes side by side and the answer to "who benefits from the wrong scandal" is obvious. **The wrong scandal is convenient for precisely the people the right scandal would implicate.** A row about the operator's record-keeping in one week is the single most effective way imaginable to *not* have a row about the regulator's design basis over a decade. It is not necessarily that anyone sat in a room and planned it that way - politics rarely needs a conspiracy when an incentive gradient will do. It is that a fake scandal about NESO's conduct is a perfect heat-sink. It draws all the political energy, all the press oxygen, all the parliamentary time, onto the operator - the delegated agent, the visible face, the body with "independent" in its name and therefore the body it is safe to blame - and away from the framework, the invisible principal, the actual author of the risk.

The whistleblower may be entirely sincere. Coutinho may be entirely sincere. That is not the point. Sincere people are the most effective possible carriers of a convenient story, precisely because they mean it. The question is not whether the people pushing the wrong scandal believe it. The question is who is served by everyone spending July arguing about a week where the data was fine, instead of arguing about a design basis that is half the real hazard and a floor that is a seventh of the real requirement. And the answer is: everyone who built the second thing and would rather you kept looking at the first.

I have spent two years trying to make people look at the framework. I am not going to stand quietly by while a fake scandal about the operator sucks all the air out of the room and lets the framework off the hook one more time. Defending NESO here is not a betrayal of everything I have written. It is the completion of it. The operator is not the villain of my story. The operator never was. The operator is the agent holding up a system the framework has been undermining - and the last thing I will do is let the framework use the operator as a lightning rod.

---

## 16. The FRCR, Missing, In The Middle Of A Frequency Row

There is one detail in the timeline that deserves its own section, because it is the darkest joke in the entire affair and almost nobody has connected it to the rest.

The Frequency Risk and Control Report - the FRCR; the document some coverage has garbled and the public has never heard of - is the single most important safety document NESO produces. It exists *because of* the 9 August 2019 blackout, when the loss of Hornsea and Little Barford dropped the frequency to 48.787 Hz, the low-frequency demand-disconnection scheme operated, and around a million customers lost supply for up to 45 minutes. Trains stopped. A hospital went dark. Out of that came a requirement: the operator must publish, regularly, an account of the risk of serious frequency events, how it plans to manage them, and what it costs to protect the system. The FRCR is the mechanism by which the public and the regulator can *see* how close to the edge the grid is running. It is the one document whose entire purpose is to make the margin visible.

And in the middle of a national row about whether the grid's frequency margins are safe, that document is missing. NESO has missed the FRCR deadline. Ofgem suspended the 2026 FRCR requirement back in March, after the 2025 report was already late. NESO has separately been released from its obligation to publish a ten-year electricity supply statement after missing two deadlines. So the country is having a screaming argument about frequency risk on 23 June while the one report designed to quantify frequency risk goes unpublished and un-required.

Sit with the absurdity of that. The prosecution's case is that NESO hid the risk of a frequency event. The genuinely alarming fact, hiding in plain sight, is that the formal report on frequency risk - the one everyone would turn to for the real numbers - is not on the table at all, and its absence has been *waved through by the regulator*. If you actually cared about whether the grid's margins are safe, the FRCR being late would be your headline, not a whistleblower's account of one week. The late FRCR is a framework failure - a joint one, operator and regulator - and it is directly, mechanically relevant to the exact question everyone claims to be asking. The one-week conduct story is a distraction from it.

And notice the direction the two failures point. A late FRCR is not evidence that the grid was fine and NESO exaggerated the danger. If anything it points the other way - toward a system whose formal risk accounting has become so uncomfortable, so hard to reconcile with a framework that has relaxed its own thresholds, that the report keeps slipping and the regulator keeps granting relief from the obligation to produce it. That is not the operator hiding a risk to make itself look good. That is the whole apparatus struggling to write down, in an official document, a risk the framework's own numbers have made embarrassing. The missing FRCR belongs in the *real* scandal, and it is the strongest single piece of evidence that the real scandal is the one worth having.

Which is precisely why it has been reported as one more stick to beat the operator with, rather than as the framework-level indictment it actually is. Even the genuinely damning fact gets absorbed into the wrong scandal. That is how effective the wrong scandal is.

---

## 17. A Word To The Whistleblower

I want to address the whistleblower directly, and generously, because the easy thing for a defence to do is to sneer at them and I am not going to do the easy thing.

If you sat in that control room and felt pressure - if you believed decisions were being shaped by reputation rather than physics, if you saw records not being kept the way they should be, if you were told to soften something you did not think should be softened - then you did a hard and brave thing by speaking, and nothing in my study calls you a liar. The conduct question is real, it is out of my scope, and it deserves a proper, calm, independent hearing on its own evidence. I mean that. I have spent two years arguing that the framework values reputation over physics; I am the last person who would dismiss out of hand the idea that the culture around it does the same.

But I have to tell you what the physics says, because it matters to you more than to anyone, and because the way your account has been used may end up hurting the very thing you were trying to protect.

The claim that has been built on top of your account - that 23 June was a hidden near-blackout, that the grid was run beyond safe limits and the danger concealed - does not survive the public data. I reconstructed that week from published measurements, sealed the method before I looked, and the grid was not in danger and the data was not hidden. The single sharpest signal of the whole week, the elevated frequency volatility on 23 June, is not concealed anywhere; it is in the one-second trace NESO published in full, for anyone to compute, that same day. So whatever was wrong in that building, "they hid a near-blackout" is not it, because there was no near-blackout, and the one real signal was published, not buried.

Here is why that should concern you rather than offend you. When a genuine conduct grievance gets welded to a false physics claim, the false physics claim becomes the load-bearing part of the public story - and when the physics claim collapses, and it will, because the data is public and reproducible and I am not the only one who can run it, *it takes your grievance down with it.* The moment someone demonstrates cleanly that the grid was fine on 23 June, the entire edifice reads as debunked, and your real point - about culture, about pressure, about records - gets buried under "the whole thing was scaremongering, the grid was never in danger." Shanks has already reached for exactly that word. The false physics claim is not protecting your grievance. It is a time bomb underneath it.

The best thing that could happen to a sincere whistleblower is for the physical facts to be settled cleanly and early - the grid was not in danger, the data was not hidden - so that the conduct question can finally be heard as what it is, a workplace-culture and record-keeping matter, on its own merits, without a phantom emergency inflating and then discrediting it. If your grievance is about how NESO is run rather than about a specific hidden catastrophe, then say that, plainly, and let it stand on its own. It will stand better alone than chained to a physics claim the public frequency trace refutes. Do not let the people amplifying you for their own reasons attach your name to the weakest version of your case.

---

## 18. What Honesty Would Actually Look Like

It is cheap to demolish and expensive to build, so here is what an honest response to July 2026 would look like - for the politicians, for the regulator, for the operator, and for me.

**For the politicians.** Separate the two questions and stop letting one borrow the other's authority. If the concern is conduct - records, pressure, culture - then commission a genuinely independent conduct inquiry, run by someone neither NESO nor Ofgem chose, with published terms of reference, and let it examine the culture on its own evidence. Coutinho is right that an inquiry commissioned by the body under investigation is not good enough; she is wrong that the fix is to keep asserting a near-blackout that the public data refutes. Demand the independence. Drop the phantom emergency. And if the concern is genuinely grid security, then aim it where the security actually lives - at the design basis, the inertia floor, the RoCoF relaxation, the missing FRCR - and not at one operator's record-keeping in one hot week.

**For the regulator.** Publish the FRCR. Stop granting relief from the obligation to write down the risk. Re-derive the largest-credible-loss from the physical system that actually exists - the HVDC-coupled offshore fleet, Dogger Bank foremost - and publish the topology and the reasoning so it can be checked from outside the building. Recompute the inertia floor against the real loss and state it, even though it is uncomfortable, because the discomfort is information the public is entitled to. And create the category the market is missing: a procurement route for intrinsic stored mass, so that the operator you have declared responsible for a physical outcome is finally given the one tool that can secure it.

**For the operator.** You did the impossible job well; now stop being a lightning rod and start being a witness. You are being blamed for a framework you did not write. The honest move is not to hire lawyers to litigate one week - it is to publish, loudly, the physical constraints you are operating under: the real largest-credible-loss you plan against, the inertia you actually hold on a bad night, the tools you do not have and wish you did. Turn the scrutiny you are receiving into scrutiny of the framework that produced your impossible week. You have more standing to indict that framework than anyone, because you are the one it traps. Use it.

**For me.** Keep the instrument pointed at everyone, including the people I am today defending. If a future reconstruction shows the operator running beyond limits and hiding it, I will publish that with exactly the same coldness I published this. My credibility is that the swing equation does not take sides and neither do I. It indicted the framework in *The 1,800 Megawatt Fiction*. It exonerated the operator in *The Heat Window*. It will say whatever it says next, and I will report that too, whether it is convenient or not.

Honesty here is not complicated. It is one separation - conduct from physics - and one redirection - operator to framework - and a handful of documents that are late being made to appear. The difficulty is not technical. It is that the honest version implicates powerful people and the dishonest version implicates a convenient one, and the system has so far preferred the convenient one. That preference is the actual scandal underneath all the others.

---

## 19. Comparative Table - The Two Scandals

| Axis | The Fake Scandal (being fought) | The Real Scandal (being avoided) |
|---|---|---|
| The claim | NESO hid a near-blackout and cooked its records during 22-26 June | The framework designs against half the real largest-credible-loss and holds a seventh of the inertia it demands |
| The timescale | One hot week | A decade of managed inertia collapse |
| The evidence offered | Whistleblower account, leaked slides, "beyond safe limits" - asserted, never reconstructed | The swing equation, public data, 16,000+ reproducible solves, the operator's own published numbers |
| What a reconstruction shows | Data complete, data solves, system not stressed, one within-limits signal in the open record | 3,600 MW loss > entire live nuclear fleet; 720 GVA.s needed, ~102 held; RoCoF ceiling relaxed 8x |
| Who is implicated | The operator - the visible, "independent," blameable agent | Ofgem's framework and DESNZ's policy - the invisible principals |
| The fix if it wins | An inquiry, a lessons-learned, a record-keeping obligation, a resignation | Re-derived loss, recomputed floor, a market category for real mass, gigawatts of built inertia |
| Cost of the fix | Cheap, procedural, closable | Expensive, physical, measured in GVA.s that must be built |
| The FRCR | One more stick to beat the operator with | Late and un-required - the framework's own risk report, missing in a frequency row |
| "Marking own homework" | Aimed at NESO's Eversheds inquiry | The framework grading the exam it set itself, with the hardest question removed |
| What it does to the whistleblower | Welds their real grievance to a false physics claim that will collapse and take it down | Settles the physics cleanly so the conduct question can be heard on its own merits |
| Net effect | The framework escapes scrutiny one more time | The framework is finally named as the author of the risk |

The table has eleven rows and one proposition: **the country is fighting the scandal that is cheap to fix and convenient to whoever built the framework, and avoiding the scandal that is expensive to fix and inconvenient to exactly those people.** The operator is the fall guy in the first and the trapped agent in the second. In neither is it the author of the risk.

---

## 20. The Objections, Answered

An honest polemic pre-loads the strongest objections and answers them in the open. Here are the ones I expect, and my answers.

**"You are just a NESO shill now."** I have written *Governance Without Physics*, *The Managed Collapse of Inertia*, *The 1,800 Megawatt Fiction*, and a dozen more, all prosecuting the way this operator's framework runs the grid. A shill does not build the most detailed public indictment of an institution's design basis in existence and then defend the institution on precisely the one point where the evidence supports it. I am defending a finding, not an institution. If the finding had gone the other way, this document would be a prosecution, and it would be just as long.

**"Public data can't see everything, so you can't clear them."** Correct, and I said so first, in Section 9. I am not clearing anyone of conduct. I am refuting a *physical* claim - dangerous grid, hidden data - that is fully within the reach of public data because the grid's state is over-determined by public measurements. The conduct claim is out of my scope and I have said so louder than any critic would. What I have removed is the false physics welded to the conduct claim, not the conduct claim itself.

**"The chi-square was at the 97th percentile on 22 June - that's your smoking gun."** It is the opposite of a smoking gun and I put it on the table myself rather than waiting for you to find it. A 97th-percentile relative-tension reading on a day when every solve passed and zero measurements were rejected is a day at the top of the normal range, not a day that broke. Concealment degrades consistency and fails solves; this data did neither. The signal is real, within the normal band, and reported precisely because an honest defence names its own strongest counter-evidence.

**"They had to phone the EU to keep the lights on - that proves it was an emergency."** It proves the week was *hard*, which nobody disputes and I have emphasised. Reaching for every tool on the shelf, including borrowing interconnector room from a neighbour, is what competent operation of a tightly-constrained grid looks like. Effort is not disaster. The pilot who uses every technique to land safely in a storm did not crash. Every customer stayed connected. That is the outcome that matters, and it is the outcome that happened.

**"The whistleblower is at the heart of NESO and you are not - who are you to say?"** I am the person holding the reconstruction. Proximity to the building is not the same as proximity to the truth of a physical claim; the physical claim is settled by the grid's public data, not by where you sit. And I have gone out of my way, in Section 17, to take the whistleblower seriously on the one thing they are placed to speak to - the conduct - while noting that the physics claim built on top of their account is not theirs to guarantee and does not survive the data.

**"If the grid was fine, why is Ofgem investigating and NESO hiring lawyers?"** Because the *conduct* allegation is real as an allegation and has to be looked at, and because in a political firestorm institutions commission inquiries to be seen to respond. An investigation into whether records were properly kept is not evidence that the grid nearly failed. Those are different questions, and conflating them is the entire engine of the wrong scandal.

**"You're doing the establishment's work by defending the operator."** I am doing the exact opposite, and Section 15 is the proof. The establishment's interest is served by the *wrong* scandal - the one that blames the operator and spares the framework. By refusing to let the operator be scapegoated and redirecting the whole thing at the framework, I am attacking the establishment's heat-sink. Defending NESO here is how you get to prosecute Ofgem and DESNZ. That is not their work. It is the last thing they want.

---

## 21. Manifesto - Defend The Operator, Prosecute The Framework

I built a machine to hold this operator's framework to account, and I have used it for two years without mercy. This week I turned it on the operator itself, on the worst allegation it has ever faced, and it refused to convict. So I am going to tell you what the machine says, because the whole of my credibility is that I tell you what the machine says whether I like the answer or not.

In the period in question, the grid was not less stable than any other day. The data was not hidden - it was published, complete, at full resolution, and it solved. The system was not stressed - inertia adequate, demand below the median, frequency in limits every second of every day. The one real signal of the week is sitting in the open record, at one-second resolution, for anyone to compute. **The cover-up needs a catastrophe to conceal, and there was no catastrophe. It is bullshit, and the public data proves it is bullshit.**

But do not mistake a defence of the operator for a defence of the framework, because they are opposites. The operator did an impossible job and did it well. The framework made the job impossible. The operator kept every customer connected through the hottest week of the year on low wind with gas out and interconnectors adverse, and had to borrow room from Europe to do it. The framework gave it a shrinking fleet, a doubled loss, a relaxed ceiling, a falling floor, and no category to buy the one thing that would help. The operator is the agent. The framework is the principal. **You cannot scapegoat the agent for the sins of the principal, and that is exactly what July 2026 is trying to do.**

The independence they gave NESO is real on the org chart and real in the plan and a fiction in the control room at two in the morning. Independent operation is only in the maths. In the physics, the operator is trapped inside a framework that wrote it a job it cannot fully do and handed it a nameplate that says it can.

So here is where I stand, and it is one sentence in two halves:

> **Defend the operator, because the operator did not lie. Prosecute the framework, because the framework did.**

The wrong scandal blames NESO for a week where the data was fine and lets Ofgem and DESNZ walk away from a decade where the design basis is a fiction. I will not carry water for it. I will defend the operator from the lie with a sealed instrument and sixteen thousand reproducible solves. And I will prosecute the framework for the truth with the same swing equation that has indicted it in every document I have ever written.

Stop hunting the operator for concealing a catastrophe that did not happen.

Start naming the framework that is building the real one in plain sight.

**The grid was fine on 23 June. The decade is not. Fight the scandal that is true.**

---

**Mark**
mark@twinscrollgridbalancer.co.uk
30 July 2026

*Author, GDA Responsible Disclosure (11 April 2026); briefed NCSC, 19 April 2026. This blog stands on the pre-registered forensic note [0023](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md), whose method was sealed to version control before any result was computed, and whose 17,328 solved grid states are published in full for independent verification. The physical findings here are reproducible by any party. The conduct allegations referenced are out of scope of that instrument and are neither asserted nor denied.*

---

## Related Documents

This blog is the polemic companion to the neutral forensic note. It defends the operator on the physical facts of the window and redirects the scrutiny at the framework the rest of the corpus prosecutes.

### The Evidence It Stands On

- [The 22-26 June 2026 Heat Window - Data Quality and System Stress](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md) - the pre-registered forensic note; the sealed method, the two nulls, the full results tables.
- [June 2026 Heat-Window Forensic Protocol (Pre-Registration)](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0022%20-%20METHOD%20-%20June%202026%20Heat-Window%20Forensic%20Protocol%20%28Pre-Registration%29.md) - the method, sealed by commit before any result was computed; the integrity claim is the commit ordering.

### The Framework This Prosecutes

- [ESO - Governance Without Physics](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0007%20-%20ESO%20-%20Governance%20Without%20Physics.md) - the accountability mirage; why an operator embedded in a diffuse-responsibility framework cannot be the sole author of a system outcome.
- [The 1,800 Megawatt Fiction](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0021%20-%20The%201%2C800%20Megawatt%20Fiction.md) - the design basis half the real hazard; Dogger Bank at 3,600 MW; the 720 GVA.s honest floor against the ~102 the framework normalises.
- [The Managed Collapse of Inertia](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0006%20-%20The%20Managed%20Collapse%20of%20Inertia.md) - the eightfold RoCoF relaxation; FRCR 2025; why response cannot replace stored mass.
- [The 2050 Delusion](https://github.com/MarkS0485/TSGB-2026/blob/main/Policy/0005%20-%20The%202050%20Delusion.md) - the RoCoF wall moving toward the operating point.

### The Instrument

- [GDA Responsible Disclosure Report](https://github.com/MarkS0485/TSGB-2026/blob/main/NCSC/GDA/0001%20-%20GDA%20Responsible%20Disclosure%20Report.md) - the reconstruction system, disclosed 11 April 2026.
- [On Presumed Open, Quietly Adopted](https://github.com/MarkS0485/TSGB-2026/blob/main/NCSC/GDA/0004%20-%20Angry%20Blog%20-%20Presumed%20Open%20and%20the%20Disclosure%20That%20Vanished.md) - the prior angry blog; the same instrument, the same refusal to let a process bury the truth of its own inputs.

### The Framing

- [The Inertia Inquiry - Clarke and Dawe](https://github.com/MarkS0485/TSGB-2026/blob/main/Creative%20Outlet/0002%20-%20Clarke%20and%20Dawe%20-%20The%20Inertia%20Inquiry.md) - the man in the chair; sincere, answerable, and not the author of the risk; accountability distributed to a point where it becomes mathematically undetectable. The truest single picture of NESO's structural position.

### The Physics

- [Inertia](https://github.com/MarkS0485/TSGB-2026/blob/main/Electrical%20Explainers/0003%20-%20Inertia.md) - stored kinetic energy as a state, not a service; the swing equation and the 2019 event in full.

---

*TSGB protected by GB patent applications - All rights reserved. This document is analysis and opinion offered for publication; it asserts no wrongdoing against any individual and makes no claim beyond what the cited public-data reconstruction supports.*
