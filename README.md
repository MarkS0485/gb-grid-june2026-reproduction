# The Grid Was Fine on 23 June: a reproduction bundle

This repository is the evidence and data companion to two reports about the 22-26 June 2026 Great
Britain heatwave and the claim that the grid operator (NESO) hid a near-blackout that week.

It contains everything an independent party needs to check the physical half of that claim for
themselves, from public data: the reports, the raw public feeds for the days in question, a portable
copy of the network model, the state-estimation solves, and a one-command validator.

## The claim, and what is checkable

The public case against NESO welds a conduct allegation (records, pressure, culture) to a physics
claim: that on 23 June 2026 the grid nearly went down and the danger was concealed. The conduct
question cannot be reached from outside the building and is not addressed here. The physics claim can
be, because the state of the grid is over-determined by public data - and it does not survive that
data. In the window the published record was complete, it was internally consistent (every settlement
period passed the estimator's chi-square consistency test, with zero bad-data rejections), and the
system was not materially stressed. The one real signal of the week, elevated frequency volatility on
23 June, is in the open one-second frequency trace, not hidden.

Why you cannot simply have doctored the data to hide stress - the cross-connection makes it
tamper-evident - is the subject of the second report.

A note on who built this and why it is reproduction-first rather than credentials-first is in
[ABOUT.md](ABOUT.md): I am a high-performance-computing engineer, not an electrical engineer, and the
whole point is that you do not have to take my word for any of it - you can run it.

## The two reports

- [reports/The Wrong Scandal.md](reports/The%20Wrong%20Scandal.md) - the argument: defend the operator
  on the physical facts of the window; prosecute the framework that made its job impossible.
- [reports/Why Public Data Is Safe.md](reports/Why%20Public%20Data%20Is%20Safe.md) - why a
  reconstruction from public data is tamper-evident: you cannot alter a few entries in one database,
  because the grid is published many times over and bound together by physics.

## Reproduce it

1. Fastest, no dependencies beyond Python:

   ```
   python solves/validate.py
   ```

   This re-derives every headline figure from the plain-text files, recomputes the percentiles against
   the 365-day baseline, verifies the SHA-256 of every measurement input, and prints PASS/FAIL.

2. Independently, with your own estimator: feed the shipped measurements and network case to any
   weighted-least-squares state estimator and compare the state and residuals. See
   [gridsim/INSTRUCTIONS.md](gridsim/INSTRUCTIONS.md). This needs none of our software.

3. Check the raw inputs: the underlying public data for the window is in
   [evidence-raw-data/](evidence-raw-data/).

## What is in here

```
reports/              the two reports
solves/
  plain-text/         the window-day solves as CSV + measurement JSON (+ SHA-256), no parquet needed
  parquet/            the same solves as parquet, with per-day provenance manifests
  baseline_day_medians.csv   365-day baseline used for the percentiles
  SUMMARY.md          the reproduced consistency table
  validate.py         one-command validator (standard library only)
gridsim/
  case/               the gb-spine network model (portable JSON)
  INSTRUCTIONS.md     how to reproduce a solve
evidence-raw-data/    raw public NESO feeds for 22-28 June 2026
PROVENANCE.md         estimator build, no-forward-inference horizon, pre-registration commit ordering
LICENSE               GPL-3.0
```

The full 370-day solve library (about 1.4 GB), from which the baseline is derived, is published as a
release asset on this repository rather than in the tree.

## Provenance and honesty

The study these reports stand on was pre-registered: the method was sealed to public version control
before any result was computed, and the commit ordering is checkable in the TSGB-2026 repository.
Details, and the honest limits of the instrument (pseudo-measurements, a reduced network, a relative
consistency index), are in [PROVENANCE.md](PROVENANCE.md). The reconstruction was produced by a private
system (GDA) from public data; GDA is not released, but everything needed to check the result is here.

## Data and licence

The raw feeds are public data from the National Energy System Operator (NESO); see
[evidence-raw-data/README.md](evidence-raw-data/README.md) for sources and terms. This repository is
released under the GNU General Public License v3.0 (see LICENSE).

Contact: mark@twinscrollgridbalancer.co.uk
