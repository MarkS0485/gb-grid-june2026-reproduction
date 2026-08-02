**GDA/GRIDSIM FORENSIC NOTE**

**The 22-26 June 2026 Heat Window: Public-Data Quality and System Stress Against a Trailing-12-Month Baseline**

*A neutral, pre-registered reconstruction from public data alone - testing two narrow, falsifiable questions and asserting no wrongdoing*

Prepared by: Mark (mark@twinscrollgridbalancer.co.uk)
Date: 25 July 2026
Method: pre-registered in [0022](0022 - METHOD - June 2026 Heat-Window Forensic Protocol (Pre-Registration).md), sealed by commit before any result was computed
Confidentiality: **None.** Written for publication in full.

*Scope: Ofgem's transparency notice of 14 July 2026 announced an independent investigation into NESO connected to the 22-26 June 2026 heatwave, concerning (1) record-keeping and whether "system risk data was hidden", and (2) improper influence on decision-making. This note addresses ONLY the factual, physical, public-data-answerable part of that picture. It tests two pre-registered questions - was the published data materially poorer that week, and was the system materially more stressed that week - against the preceding twelve months. It asserts no wrongdoing, no concealment and no improper conduct; the conduct allegation (2) is out of scope and cannot be spoken to by any measurement. Every figure is derived from public data; the solved states behind the consistency test are published in full for independent checking. This is an analysis of public information, not a disclosure of an incident.*

# **1. Executive Summary**

Between 22 and 26 June 2026 Great Britain experienced a genuinely record-breaking heatwave - the hottest June day ever recorded in the UK (37.7 C, Lingwood, 26 June), a Red Extreme Heat Warning on a record third consecutive day, and seven consecutive days above 30 C. Against that backdrop, two narrow questions can be answered from public data: was the data NESO and the networks published *during* the window materially different in quality from the preceding year, and was the physical system materially more stressed?

Reconstructing the grid's state for every half-hour of the window and of the preceding 365 days, entirely from public data, and ranking each window day against that twelve-month baseline at a strict P95/P5 bar under two lenses (all days, and heat-matched to comparable hot days), the picture is predominantly one of **no material difference** - the published data was fully complete and internally consistent, and the system was not materially stressed on the great majority of measures - with three specific, modest, within-limits signals reported honestly below.

> **\[HEADLINE FINDING\] Despite record-breaking heat, the public data covering 22-26 June 2026 was published in full and is internally consistent, and the physical system was not materially stressed on the great majority of measures relative to the preceding twelve months. Generation-mix, demand and 1-second frequency data were complete on every window day; the published measurements solve into a coherent grid state on every day with zero bad-data rejections; system inertia was adequate; balancing was unremarkable; and frequency stayed within statutory limits throughout. Three modest signals sit near the top of the year's normal range and are recorded plainly: on 22 June the published data was marginally less internally tight than a typical day (96.7th/97.3rd percentile - though it still passed every consistency test); on 23 June the measured rate-of-change-of-frequency was elevated (98th percentile all-days, highest of any comparable hot day) while remaining within statutory limits; and demand ran high FOR A HOT DAY (a modest cooling response) while staying below the annual median. None indicates degraded data management, hidden risk, or a system emergency; together they are the faint, physically-plausible fingerprint of a hot, high-embedded-generation summer week. The public record does not show either degraded data or an abnormally stressed grid during the window - a neutral finding, and explicitly NOT a statement about record-keeping intent or internal decision-making, which lie outside what any measurement can address.**

The instrument is honest about its own limits (Section 9): part of it rests on pseudo-measurements; the completeness axis measures the research lake's *ingestion*, not directly NESO's publication; and several convenience metrics that embed a present-day snapshot were excluded from the twelve-month comparison rather than allowed to mislead.

# **2. Why the Scope Is Deliberately Narrow**

Two allegations were reported. One is about *conduct* - whether records were poor and whether risk data was hidden, and whether decision-making was improperly influenced. The other, implicit in the first, is about *fact* - whether there was, in the public record, anything unusual about the data or the system during those days.

Only the second is answerable from outside. No reconstruction from public data can establish what anyone intended, knew, or decided internally; asserting otherwise would be to overreach the evidence. This note therefore confines itself, by design, to two falsifiable nulls and reports them whether they are confirmed or refuted. A finding of "no material difference" is as much a result as its opposite, and is stated as plainly.

The physics cannot be coaxed. The publication policy and the weather are the givens; what the public data shows is the only variable this note touches.

# **3. The Window and Its Premise**

The heatwave is established meteorological context, not a finding of this study. The Met Office recorded the warmest June on record for England; a provisional 37.7 C at Lingwood, Norfolk on 26 June - the hottest June day on record in the UK and the sixth-hottest UK day ever; a Red Extreme Heat Warning issued on a record third consecutive day on 25 June; and seven consecutive days above 30 C from 21 to 27 June.

The reconstruction confirms the premise in its own data. Taking the hottest grid cell in Great Britain each day, the five window days reached 35.7, 37.6, 37.5, 38.1 and 36.5 C - **every one hotter than all 362 baseline days** (whose hottest reached 35.0 C). On that measure the window sits at the 100th percentile of the year. In the South-East - the most heavily loaded distribution area - the peak reached 36.5 C on 26 June. The window was, unambiguously, the hottest stretch of the year.

That extremity is the reason the study exists. It is not, in itself, evidence of anything about the grid or the data - which is the whole point of the two tests that follow.

# **4. Method in Brief**

The full protocol is pre-registered in document 0022, sealed to version control on 25 July 2026 before any comparison was computed; the commit ordering is the integrity claim. In brief:

- **Two hypotheses only.** H1 - was the public data materially different in quality/completeness or internal consistency? H2 - was the system materially more stressed? Each is a neutral null the study tries to falsify.
- **Baseline.** The 365 days immediately before the window (22 June 2025 - 21 June 2026), one GB settlement day at a time.
- **Two lenses.** All-days, and heat-matched (the ~37 top-decile-temperature baseline days) - the latter to control for "it was hot" when judging the non-temperature metrics.
- **Materiality.** A strict, uniform P95/P5 bar (a window day beyond the 95th / below the 5th percentile of baseline), chosen to make any positive finding robust and to bias the study toward under-claiming. Exact percentile ranks are reported regardless.
- **Three transparent corrections** were logged in 0022 before the final ranks, each pre-dating the results it could affect: C1 - the temperature metric was moved from a national spatial mean (which washes out a regional extreme) to the national daily maximum-cell; C2 - the completeness axis was recognised to measure the research lake's ingestion rather than NESO's publication directly, and the inertia feed's recent-weeks ingestion thinning was excluded from any NESO attribution; C3 - metrics embedding a present-day fleet snapshot were excluded from the twelve-month comparison.

# **5. Finding - H1(a): Data Completeness**

*Does the public data for the window show missing or thinned records relative to the baseline?*

For the three feeds whose ingestion into the research lake is robust - generation mix, national demand and 1-second system frequency - the window is complete and indistinguishable from an ordinary day. Generation and demand carried **every settlement period on every one of the 365 baseline days and all five window days** (48 of 48, bar the ordinary 46/48 boundary shape common to the whole year). The 1-second frequency record was **complete on all five window days - the full 86,400 samples each day** (the baseline median and 5th percentile are both 86,400). There is no thinning, no gap and no missing partition on the window days on any of these feeds.

> **\[IMPORTANT - RESTRAINT\]** The completeness axis measures what is present in the research data lake, which depends on *both* what NESO published *and* how the lake ingested it - the two cannot be separated from inside the lake. The system-inertia feed in the lake thins over the most recent five weeks (fourteen partial days, all between 18 May and 20 June 2026 - i.e. beginning before the window), a recency-correlated ingestion pattern that is a known behaviour of the lake, not a window-specific publication event. It is therefore **excluded** from any statement about NESO's data, and reported here only as an artifact of the instrument. The completeness finding rests on generation, demand and frequency, whose ingestion is complete across the whole period.

# **6. Finding - H1(b): Internal Consistency (the "solves badly" test) [LEAD]**

*Do the published measurements for the window fit together - physically and across independent feeds - as well as on an ordinary day?*

This is the core of H1 and the part least confounded by ingestion. For every half-hour, the published metered generation, interconnector flows and demand are fed to a weighted-least-squares state estimator; the objective normalised by degrees of freedom (the reduced chi-square) measures how well the day's published numbers cohere within their stated uncertainties. A value near or below one means consistent; a materially higher value on a given day would mean that day's published data fit together less well.

Every half-hour of the window and of the full 365-day baseline was solved with one pinned estimator build (16,000-plus solves; all published in the library of Section 12). The result is that **the published data for the window is internally consistent**: on every one of the five window days, the chi-square consistency test passed in every settlement period, and there were zero bad-data rejections - no published measurement had to be discarded as inconsistent on any window day.

Two honest nuances sit within that clean result. First, a calibration note: the reduced chi-square runs below one across the whole year (baseline median 0.36), which means the published measurements' stated uncertainties are conservative; the metric is therefore used here as a **relative** index of internal tension across days (the model is identical throughout), not as an absolute goodness-of-fit. Second, on that relative index the window sits in the upper part of the year's range, and one day crosses the bar:

| Window day | Reduced chi-square (median) | All-days pctile | Heat-matched pctile | Bad-data removals |
|---|--:|--:|--:|:--:|
| 22 Jun | 0.485 | **96.7** | **97.3** | 0 |
| 23 Jun | 0.462 | 93.7 | 91.9 | 0 |
| 24 Jun | 0.430 | 88.2 | 78.4 | 0 |
| 25 Jun | 0.444 | 90.7 | 81.1 | 0 |
| 26 Jun | 0.432 | 88.2 | 78.4 | 0 |

(Baseline median 0.359, P95 0.468 - independently re-derived.) On **22 June** the day's published measurements were marginally *less* internally tight than a typical day, and than a typical hot day - the 97th percentile on both lenses, just past the strict bar. The other four days are elevated but do not cross it. The plain reading: the published data solves into a coherent grid state on every window day with nothing rejected, while carrying slightly more internal tension than usual - most pronounced, but still only marginally material, on 22 June. This is a property of the data's mutual consistency; its cause is out of scope, and it is emphatically not a failure of the data to solve.

# **7. Finding - H2: System Stress**

*Was the physical system materially more stressed during the window than in the preceding year?*

On the metrics that can be ranked honestly against a twelve-month baseline (Section 9 explains which were excluded and why), the window does not stand out:

| Metric | Window range | All-days rank | Material? |
|---|---|---|---|
| Minimum system inertia | 119-165 GVA.s | 24th-86th pct | No - adequate |
| Peak national demand | 29.3-31.8 GW | 37th-50th pct (below annual median 32.1 GW) | No (all-days) |
| Worst modelled RoCoF | 0.27-0.38 Hz/s | 14th-76th pct | No |
| Daily BSUoS balancing cost | GBP 1.4-11.2 m | 10th-75th pct | No |

System inertia was adequate throughout (never near the low tail); the modelled worst-case rate-of-change-of-frequency was ordinary; balancing costs were unremarkable. Peak demand sat *below* the annual median - unsurprising, since UK summer demand is low and domestic cooling load is small.

The one metric that crosses the bar does so only in the heat-matched lens: peak demand ranks at the 84th-100th percentile *among comparable hot days* on 22-25 June. The honest reading is not that demand was high - absolutely it was below the year's median and far below its winter peaks - but that it was high *for a hot day*, the expected modest cooling response. That is a signal about weather-driven demand, not about system stress, and the two-lens design is what makes the distinction visible.

The measured frequency record adds the one genuine system signal of the window. Taken from the 1-second frequency directly, the maximum measured rate-of-change-of-frequency was ordinary on four of the five days (62nd-81st percentile), but on **23 June it reached 0.112 Hz/s - the 98th percentile of the year on all days, and the highest of any comparable hot day (100th percentile heat-matched)**. That is a real, measurable spike in frequency volatility. It should be read in proportion: frequency never left the statutory band on any window day (the seconds spent beyond 49.5-50.5 Hz were zero on all five days, as in a normal day), the day's data still solved and passed every consistency test, and 0.112 Hz/s is well inside the protection thresholds. So 23 June was the most frequency-active day of the window - a genuine deviation worth recording - but not a statutory or security event. The count of seconds beyond the softer +/-0.2 Hz operational band was not materially different from baseline on any window day.

# **8. Finding - Thermal (Descriptive)**

The thermal limb is descriptive only; there is no dynamic-rating model in the estate, so no claim is made that any asset breached a heat-derated limit (Section 9). What can be said: ambient temperature was at the 100th percentile of the year (Section 3), and it coincided with peak demand that was elevated relative to comparable hot days but below the annual peak (Section 7). Asset loading against static ratings is characterised for the window without a per-day twelve-month ranking, consistent with the static-rating limitation.

# **9. Limitations (the instrument's own honesty)**

Per the pre-registered rule that the instrument must disclose its own limits:

- **Pseudo-measurements.** A substantial part of each half-hourly measurement set is pseudo-measurement - per-bus demand allocated from a national shape, and all reactive power, at loose uncertainties, because there is no public reactive telemetry or per-site demand metering. An elevated consistency residual therefore reflects inconsistency chiefly among the *metered* generation and interconnector rows against the allocation, weighted toward the metered data; the pseudo rows dilute the signal. The consistency test is a real but not omniscient instrument.
- **Completeness measures ingestion, not publication** (C2). See Section 5. Generation and demand are complete; inertia's recent-weeks thinning is an ingestion artifact excluded from NESO attribution.
- **Present-fleet snapshot** (C3). Fragility index, reserve margin and credible-loss embed a present-day synchronous-fleet snapshot; ranking them across historical baseline days would be invalid, so they were excluded from the twelve-month claim and used only as window context. (System inertia, by contrast, uses the trusted time-varying reconstruction and is ranked honestly.)
- **Static thermal ratings.** Asset loading is measured against fixed nameplate/firm ratings; no ambient-temperature derating exists in the estate, so no hot-day-limit-breach claim is made.
- **Temperature is a grid extreme, not a station reading.** The max-cell metric is the hottest 0.25-degree cell; it tracks the record closely (38.1 C peak) but is a gridded reanalysis value, not the official station maximum.
- **Reduced chi-square is a relative index, not absolute goodness-of-fit.** It runs below one all year (median 0.36), so the measurement uncertainties are conservative; it is used only to compare internal tension *between* days under an identical model, which is valid, and not as an absolute measure of fit. The 22 June signal is a relative-tension observation, not a claim that the data failed any absolute test - it passed every one.

None of these limits is hidden in a footnote; each is stated where the finding it bears on is made.

# **10. Conclusion**

> **\[PRINCIPAL CONCLUSION\] On the two questions a public-data reconstruction can answer, the record heat of 22-26 June 2026 left only a faint fingerprint. The published data was fully complete and internally consistent - it solved into a coherent grid state on every window day with nothing rejected - and the system was not materially stressed on the great majority of measures: inertia adequate, demand below the annual peak, balancing unremarkable, frequency within statutory limits throughout. Three modest, within-limits signals sit near the top of the year's normal range and are recorded plainly: slightly greater internal tension in the published data on 22 June (97th percentile, still fully consistent), elevated measured frequency volatility on 23 June (98th percentile, within statutory limits), and demand a little high for a hot day (a modest cooling response, below the annual median). None is a statutory breach, a data failure, or a security event; together they are what physics predicts of a hot, high-embedded-generation summer week. The public record does not show either degraded data or an abnormally stressed grid during the window - offered neutrally, and explicitly NOT a statement about record-keeping intent or internal decision-making, which no measurement can reach.\]**

If the investigation's concern is whether a real, out-of-limits physical risk during the window went unreflected in the record, this reconstruction is one independent, public-data check on that question, and it does not find such a risk: the only genuine system signal, 23 June's elevated frequency volatility, is itself present and measurable in the public record, not hidden by it. That is a limited claim, made deliberately within the limits of the instrument (Section 9).

# **11. Route**

This note is offered as an input to the independent review, through the responsible-disclosure relationship already established with NCSC, DSIT, Ofgem, NESO and DESNZ in April 2026 - not as a submission to any open process, of which there is none, and not as an allegation. Its value is that it is reproducible: the pre-registered method (0022) and the published solved states (Section 12) let any party re-run it and reach the same numbers, or challenge them.

# **12. Provenance, Reproducibility and Timeline**

Every figure derives from public data. The internal-consistency test rests on a published solved-state library (`GDA-SOLVES`): for every half-hour, the input public measurements, the solved grid state, and the residual diagnostics, with per-solve provenance (estimator build, data hashes, and the no-forward-inference horizon attestation - every solved instant is at least a week old by construction). Any solve can be re-run and its objective and state reproduced.

- **11 April 2026** - GDA Responsible Disclosure to NCSC, DSIT, Ofgem, NESO, DESNZ.
- **22-26 June 2026** - the heat window.
- **14 July 2026** - Ofgem transparency notice; independent NESO review announced.
- **25 July 2026** - method 0022 pre-registered and sealed; this reconstruction computed.

-

**Mark**
mark@twinscrollgridbalancer.co.uk
25 July 2026

*Author, GDA Responsible Disclosure (11 April 2026). Pre-registered method sealed before results; solved states published for independent verification.*

---
Document date: 25 July 2026 | Neutral analysis of public data | No assertion of wrongdoing
