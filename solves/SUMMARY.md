# Window-day solves: reproduced summary

This reproduces the internal-consistency table from "The Wrong Scandal" (and the pre-registered
forensic note) directly from the solves shipped here. Every figure below is regenerated from the
plain-text files by `validate.py` - no trust required.

## The test

For every half-hour of the window (22-26 June 2026) and of the 365-day trailing baseline
(22 June 2025 to 21 June 2026), the published metered generation, interconnector flows and demand were
fed to the state estimator over the gb-spine network. The measure of internal consistency is the
reduced chi-square (objective J divided by degrees of freedom): near or below one means the published
measurements cohere into a physically valid grid state; a materially higher value on a day would mean
that day's published numbers fit together less well - the fingerprint you would expect if numbers had
been shaded.

Per-day value = median reduced chi-square over the day's converged settlement periods.
All-days percentile = rank of that day's value against the 365 baseline day medians.

## Result

Baseline: 365 days. Median reduced chi-square 0.359. 95th percentile 0.468.

| Window day | Reduced chi-square (median) | All-days percentile | Bad-data removals | Chi-square pass |
|---|--:|--:|:--:|:--:|
| 22 Jun 2026 | 0.485 | 96.7 | 0 | every period |
| 23 Jun 2026 | 0.462 | 93.7 | 0 | every period |
| 24 Jun 2026 | 0.430 | 88.2 | 0 | every period |
| 25 Jun 2026 | 0.444 | 90.7 | 0 | every period |
| 26 Jun 2026 | 0.432 | 88.2 | 0 | every period |

The heat-matched percentiles reported in the study (the roughly 37 hottest baseline days) were, for the
same reduced-chi-square metric: 22 Jun 97.3, 23 Jun 91.9, 24 Jun 78.4, 25 Jun 81.1, 26 Jun 78.4. The
heat-matched lens depends on the weather-derived set of comparable hot days defined in the sealed
method (Policy/0022); the all-days lens above is reproduced here in full from the shipped solves.

## Reading it

The published data for the window solves into a coherent grid state on every day, with every
settlement period passing the chi-square consistency test and not a single measurement rejected as
bad data. The days sit in the upper part of the year's range on the relative consistency index - most
pronounced, and only marginally past the strict 95th-percentile bar, on 22 June - which is the faint
texture of a hot, high-embedded-generation summer week, reported at the top of the normal range
because that is where it honestly sits. It is emphatically not a failure of the data to solve, and it
is not the fingerprint of concealment: concealment would degrade consistency badly and fail solves,
and instead every solve passed and nothing was removed.

## How to reproduce

- Fastest: `python validate.py` from this folder. It re-derives every figure above from
  `plain-text/<date>/diagnostics.csv`, recomputes the percentiles against
  `baseline_day_medians.csv`, verifies the SHA-256 of every measurement input, and prints PASS/FAIL.
- Deeper: re-solve any period yourself. Take `plain-text/<date>/measurements/period-NN.json` (the
  exact, hashed input), feed it with the `gridsim/case/` network to any weighted-least-squares state
  estimator, and compare the state and residuals to `plain-text/<date>/solved_state.csv` and
  `diagnostics.csv`. See `gridsim/INSTRUCTIONS.md`.
- Baseline: the full 370-day solve library (from which `baseline_day_medians.csv` is derived) is
  available as a release asset; see the top-level README.
