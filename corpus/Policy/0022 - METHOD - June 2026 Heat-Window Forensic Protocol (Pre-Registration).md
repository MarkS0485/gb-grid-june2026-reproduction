# METHOD - June 2026 Heat-Window Forensic Protocol (Pre-Registration)

**Author:** Mark - independent researcher
**Email:** mark@twinscrollgridbalancer.co.uk
**Date sealed:** 25 July 2026
**Confidentiality:** **None.** Written for publication in full, and as the pre-registered protocol for the report at [0023](0023 - The 22-26 June 2026 Heat Window - Data Quality and System Stress Against a Trailing-12-Month Baseline.md).
**Status:** Pre-registration. This document fixes the hypotheses, baseline, metrics and decision rules **before** the comparison is computed. It is committed to version control at the point of sealing; the commit timestamp is the integrity claim. Nothing in the results may retroactively change anything in this file - if the method changes, that is a new, separately dated protocol.

---

## Provenance

I am the author of the Grid Data Analysis (GDA) Responsible Disclosure dated 11 April 2026, submitted under responsible-disclosure protocols to NCSC, DSIT, Ofgem, NESO and DESNZ, and briefed to NCSC on 19 April 2026. The instrument used in this protocol (GDA, and the GridSim historical state estimator) is the same instrument described in that disclosure. Where I quote a source, I quote verbatim and cite it so a recipient can verify against the document they already hold.

This protocol is written to a single standard: **a reader who disagrees with me should still be able to run it and get the same numbers.** That is the whole point of pre-registering it.

---

## 1. Why this document exists

On 14 July 2026 Ofgem published a transparency notice announcing an independent investigation into NESO in connection with the 22-26 June 2026 heatwave. As reported, the investigation concerns two allegations: (1) poor record-keeping, and whether "system risk data was hidden"; and (2) improper influence on decision-making.

This protocol addresses **only** the factual, physical, public-data-answerable part of that picture. It tests two narrow questions and no others:

- **H1 - data quality/management.** Was the public data NESO and the networks published *covering* the window materially different, in completeness or internal consistency, from the trailing twelve months?
- **H2 - system stress.** Was the physical stress on the GB system during the window materially different from the trailing twelve months?

It is **not** an accusation. It asserts no wrongdoing, no deception and no concealment. Allegation (2) - intent and conduct - is **out of scope** and cannot be spoken to by any physical measurement. The report that follows this protocol may only say what the public data shows, relative to a baseline.

## 2. The verified premise (context, not a finding)

The window was authentically record-breaking, and this is stated as established meteorological context, not as anything this study discovered:

- Warmest June on record for England (Met Office).
- Provisional **37.7 C at Lingwood, Norfolk on 26 June 2026** - the hottest June day ever recorded in the UK, and the 6th-hottest UK day on record.
- Met Office **Red Extreme Heat Warning issued on a record third consecutive day, 25 June 2026**.
- Seven consecutive days above 30 C, 21-27 June 2026.

Sources: Met Office, "June 2026 heatwave: a recap of the temperature records"; Met Office, "Heatwave continues as UK records unprecedented run of 35 C days"; and the public record of the 2026 UK heatwaves.

Two consequences follow for the method, and both are declared here in advance:

1. The peak day, 26 June 2026, is precisely the day currently **missing** from the estimator's solved-state record. Its reconstruction is therefore the highest-priority solve, not an afterthought.
2. A 37.7 C June day is unprecedented, so a "heat-matched" baseline **cannot** contain a true equal. The report states the residual temperature gap between the window and its warmest comparators plainly rather than implying a match exists.

## 2a. Correction log (transparent; each entry pre-dates the results it could affect)

**C1 - temperature metric (2026-07-25, before any H1/H2 comparison was computed).** As first sealed, this protocol used *national mean* daily temperature for the heat-matched lens (s.4) and the thermal limb (s.6). On building the daily series it was found that the national mean is a spatial average over ~2,000 grid cells and so cannot represent a regionally-concentrated extreme: on 25-26 June 2026 the national mean is ~17 C, while the per-cell daily maximum is 36-38 C (consistent with the 37.7 C record). Using the national mean would both misrepresent the event and defeat the heat-matched lens (the window would not register as hot). The temperature metric is therefore corrected - before any comparison result existed - to **national daily maximum-cell temperature** (the hottest point in GB each day) as primary, with a **South-East England regional** view (the most heavily loaded distribution area) and the national mean retained for transparency. The heat-matched lens (s.4) is redefined as the top-decile baseline days by national daily maximum-cell temperature. This is a measurement-validity correction, not a result-driven one; the two hypotheses, all H1/H2 metrics, and the P95/P5 rule are unchanged. The original seal (commit history) stands; this entry and the re-commit that carries it both pre-date any computed comparison.

**C2 - H1(a) completeness measures GDA-lake INGESTION, a confounded proxy for NESO publication (2026-07-25, before final ranks).** H1(a) row-density is the count of records present in the GDA lake, which is a function of *both* what NESO published *and* how the GDA pipeline fetched and stored it; the two cannot be separated from inside the lake (disclosed per R8). Empirically over the study span: generation mix and national demand are **100% complete (all 48 settlement periods) on every one of the 365 baseline days and all 5 window days** - no thinning in the robustly-ingested operational feeds. The system_inertia feed, by contrast, thins only in the most recent ~5 weeks (14 partial days, all between 2026-05-18 and 2026-06-20 - i.e. beginning five weeks *before* the window), a recency-correlated ingestion-lag/freeze pattern that is a known GDA-lake behaviour, not a window-specific NESO event. GDA-lake inertia completeness is therefore **excluded from the H1(a) claim** and reported only as a disclosed instrument artifact; H1(a) rests on generation, demand and frequency completeness. (H2's inertia is unaffected: it uses the trusted *reconstructed* inertia product, not the raw feed.)

**C3 - present-fleet-snapshot metrics excluded from the ranked twelve-month claim (2026-07-25, before final ranks).** The composite fragility index, reserve margin and credible-loss embed a **present-day** synchronous-fleet capacity/stress snapshot (s.6/s.7 already flagged margin and stress as present-time diagnostics). Ranking them across historical baseline days would compare each past day against *today's* fleet, which is invalid; they are therefore excluded from the ranked H1/H2 claim and used only as window context. The metrics that are genuinely per-epoch - system inertia (the trusted time-varying reconstruction), peak demand, modelled RoCoF (a deterministic transform of inertia), the measured-frequency metrics, and the balancing cost - are ranked normally. This enforces, rather than changes, the sealed guidance.

## 3. The epistemic contract (rules R1-R8)

- **R1 - No conduct claims.** No statement about intent, honesty, concealment or competence. The only admissible form of finding is: "the published data for these days has property X relative to the last twelve months."
- **R2 - Two hypotheses only** (H1, H2), each stated as a neutral null that the study tries to falsify.
- **R3 - A bad solve is a property of the data, not a verdict on a person.** An elevated normalized residual or chi-square is reported as "the day's published measurements are less internally self-consistent than baseline." Cause is out of scope. The technique is standard weighted-least-squares bad-data detection: the chi-square test on the objective, and the largest-normalized-residual test.
- **R4 - Pre-registration.** Baseline, metrics and the materiality threshold are fixed in this document before the comparison runs. Every pre-registered metric is reported, whether or not it shows a difference.
- **R5 - Null results are first-class.** "No material difference detected" is a valid, publishable conclusion and is stated as plainly as any positive finding.
- **R6 - Provenance on every number.** Public data only. Each figure in the report carries its source dataset and the means to re-derive it. The solved states that underpin H1 are published in full (Section 9) so they can be independently checked.
- **R7 - Two axes kept separate.** Data-quality (H1) and system-stress (H2) are reported separately and never conflated. A day can be stressed with clean data, or calm with messy data.
- **R8 - Disclose the instrument's own limits.** The pseudo-measurement dilution (Section 7), the static-rating thermal caveat (Section 6), and the metered-versus-pseudo weighting are stated plainly in the report body, not buried.

## 4. Baseline, per-day definition, lenses and materiality

- **Baseline B** = the 365 days immediately preceding the window: 22 June 2025 to 21 June 2026 inclusive. The five window days (22-26 June 2026) are separate and are never part of B.
- **"Per-day" = one GB settlement day** (Europe/London local day, 46/48/50 settlement periods across DST), not a UTC calendar day. Conversion uses the settlement-day anchoring already standard in the estate. The baseline distribution for any metric is therefore up to 365 settlement-day values.
- **Two lenses, both always reported:**
  - **(i) all-days:** the window day ranked against all 365 baseline days.
  - **(ii) heat-matched:** the window day ranked against the top-decile-temperature baseline days (the ~36 warmest settlement days in B, by **national daily maximum-cell temperature** - see Correction log C1). This lens exists to **control for "it was hot"**: it asks whether data-quality or stress differed *beyond what a hot day normally brings*. Because the window is record-breaking, the report also states the temperature gap between the window and this comparator set, so the reader sees how imperfect the match necessarily is.
- **Materiality threshold: P95 / P5.** A window day is flagged "materially different" on a metric if it falls **above the 95th percentile or below the 5th percentile** of the baseline distribution for that metric. This is a decision rule applied **uniformly to every metric**; it is deliberately *not* tied to the extremity of the weather. The rationale is claim-robustness: a strict bar makes each positive finding harder to challenge and biases the whole report toward under-claiming, which is the correct posture for a neutral instrument. The exact empirical percentile rank is reported for every metric regardless of whether it crosses the threshold.
- **Ranking is empirical (non-parametric).** For each metric, a window day's rank is the fraction of baseline days at or below its value. No normality is assumed. Where a trailing-causal formulation is used, the current day is excluded from its own baseline.

## 5. H1 - data quality and management (two sub-signals)

*Null: the public data covering 22-26 June 2026 is not materially different, in completeness or internal consistency, from baseline B.*

**H1(a) - completeness and management.** Per feed, per settlement day: row density versus the feed's own recent median (internal thinning), edge-freshness/gaps, and missing-partition counts. Feeds in scope, fixed here: system frequency (1 s), generation mix, system inertia, national demand, and balancing/constraint. A day is flagged if a feed's density for that day sits below P5 of the baseline density distribution for that feed.

**H1(b) - internal consistency ("solves badly").** For each settlement period of each day, the GDA/GridSim weighted-least-squares state estimator is solved against that period's real published measurements. The per-period diagnostics are aggregated to per settlement day:

- **Reduced chi-square J/dof** (the lead metric): the estimator objective normalized by degrees of freedom. ~1 means the published measurements are mutually consistent to within their stated uncertainties; a materially higher value on a given day means that day's published numbers fit together less well.
- **Chi-square pass fraction** (fraction of the day's periods passing the 95% chi-square test).
- **Bad-data removals** (`removed_total`) and the **outlier league** (which measurement is repeatedly rejected across periods) - a pointer to *which* published quantity is inconsistent, stated as a data property, never as an accusation.
- **Closure: estimated load versus NESO national demand** (`load_vs_nd_pct`) - an independent cross-check that the published numbers cohere at the national total.

Each of these is ranked per window day against B under both lenses, at P95/P5.

## 6. H2 - system stress

*Null: physical system stress on 22-26 June 2026 is not materially different from baseline B.*

Per settlement day, ranked against B under both lenses at P95/P5: minimum system inertia (GVA.s); maximum absolute RoCoF (Hz/s); count and severity of frequency excursions and time spent near statutory limits; balancing and constraint volume and cost; and peak national demand. These are drawn from the estate's existing detectors and the composite system-condition series.

**Thermal (descriptive limb).** Ambient temperature (national daily maximum-cell, plus a South-East England regional view; national mean retained for transparency - see Correction log C1) and asset loading (hours at or above 80% of static nameplate/firm rating, from the asset-stress ledger) are each ranked against B, and their **co-incidence** on the window days is noted. This limb is **descriptive only**. There is no ambient-temperature-dependent dynamic-rating model in the estate; building one would inject contestable assumptions. Therefore the report does **not** claim any asset breached a hot-day-derated limit - it reports only observed loading against static ratings, and observed temperature, side by side. Dynamic thermal derating and temperature-to-demand coupling are explicitly out of scope.

## 7. The instrument, and its declared limits

The consistency signal in H1(b) is produced by the GridSim weighted-least-squares estimator applied to the reduced "gb-spine" GB network, driven by GDA's public-data measurement sets (B1610 per-GSP metered generation, metered interconnector flows, and demand/voltage pseudo-measurements). It is a historical estimator governed by a hard no-forward-inference horizon (169 hours); every day in this study is months old and therefore unambiguously historical.

Declared limits, per R8:

- **Pseudo-measurement dilution.** A substantial part of each measurement set is pseudo-measurement: per-bus demand allocated from a national shape, and all reactive power, carried at loose sigmas because there is no public reactive telemetry and no per-GSP demand metering on non-B1610 days. Consequently an elevated objective on a given day reflects inconsistency chiefly among the **metered** rows (generation and interconnector flows) against the demand/topology allocation, weighted toward the metered rows; the pseudo rows dilute the signal. This is stated wherever H1(b) is reported.
- **Uniform version.** To make the twelve-month comparison fair, **all** solves used for H1(b) - window and baseline alike - are generated by a single, pinned build of the estimator, recorded by commit and binary hash in the per-solve manifests. The report does not mix these with any pre-existing solved rows of other provenance.
- **Calibration.** Before J/dof is interpreted as a reduced chi-square, the leverage-corrected residual RMS of the measurement noise model is checked to be ~1 over the baseline; this check is reported.

## 8. What is reported, and what is not

The report presents, for every metric above, the window days' exact percentile ranks under both lenses, and flags those crossing P95/P5. It honours null results (R5). It states the meteorological premise as context (Section 2). It does **not**: assert wrongdoing or intent (R1); address the record-keeping or influence allegations as conduct; claim a dynamic-thermal breach (Section 6); or draw any operational, real-time or forward-looking conclusion (the horizon forbids it).

## 9. Reproducibility artefact

Every state solved for this study is retained in full - inputs (measurement sets), solved states, and per-measurement residual diagnostics - as a published solved-state library (`GDA-SOLVES`), with per-solve provenance (topology hash, measurement-set hash, estimator commit and binary hash, solve time, horizon attestation) and instructions to re-run any solve and reproduce its objective and state. This makes H1(b) independently checkable rather than asserted. Publication of that library is a separate, deliberate act reserved to the author; this protocol only builds it.

## 10. Seal

This protocol is sealed by committing it to the corpus version control on the date above, before the comparison at [0023](0023 - The 22-26 June 2026 Heat Window - Data Quality and System Stress Against a Trailing-12-Month Baseline.md) is computed. The pre-registration claim rests on that commit ordering.

-

**Mark**
mark@twinscrollgridbalancer.co.uk
25 July 2026

*Author, GDA Responsible Disclosure (11 April 2026)*
*Pre-registered protocol - sealed before results.*
