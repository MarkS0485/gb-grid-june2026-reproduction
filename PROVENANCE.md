# Provenance and integrity

This bundle lets an independent party check the physical findings of "The Wrong Scandal" against the
public record. This file records exactly what produced the solves, and the integrity claim behind the
pre-registered study.

## What produced the solves

Every solve in this bundle was produced by the GridSim weighted-least-squares state estimator, run
over the reduced "gb-spine" GB network against real published measurements. Per-day provenance is
recorded in each `solves/parquet/manifest_YYYYMMDD.json`. For the window days it is:

- Estimator: GridSim, commit `dbeee06b54ab78910777aa45cb7b53d16c38c376`.
- Build state: working tree DIRTY at solve time (44 modified files), recorded per day. This means a
  bit-exact re-run requires that exact working tree; it is why the primary reproduction path in this
  bundle is estimator-independent (see below).
- Estimator executable SHA-256: `e6798f455846fa8824f1d2f5ded2c7cc7b03b9c33142ed10ca95b1aa55e99501`.
- Case: `gb-spine` (shipped in `gridsim/case/`).
- No-forward-inference horizon: 169 hours. Every solved instant is at least 169 hours old by
  construction. This is historical replay, never a nowcast or a forward estimate.
- Solved at: 2026-07-25 (UTC), for all five window days; 46 settlement periods each, all converged,
  all chi-square consistent, zero bad-data rejections.

GridSim itself is the author's estimator and is not part of this public release. You do not need it:
the exact inputs and outputs are shipped so that any weighted-least-squares state estimator can
reproduce the result. See `gridsim/INSTRUCTIONS.md`.

## The pre-registration integrity claim

The study "The Wrong Scandal" stands on was pre-registered: the method was sealed to version
control BEFORE any result was computed, so the method could not have been tuned to the answer. The
integrity claim is the ordering of these commits in the author's version control; the hashes and
timestamps are recorded here as attestation. The sealed method (0022) and the forensic note (0023)
are themselves included in full in this bundle (see below), so you can read exactly what was
pre-registered and check it against the results:

- Method sealed: commit `7d51426`, 2026-07-25 05:13:53 +0100
  (`Policy/0022 - METHOD ... (Pre-Registration).md`).
- Pre-results corrections, all logged before the results they could affect:
  - `5d3794b` 05:29:46 - C1, temperature metric moved to national max-cell (made the heat look worse).
  - `f583d5f` 05:47:02 - C2, completeness axis measures ingestion not publication; inertia feed's
    recency thinning excluded from any operator attribution.
  - `ee16424` 05:54:30 - C3, present-fleet-snapshot metrics excluded from the ranked claim.
- Results published: commit `40fc747`, 2026-07-25 07:45:23 +0100
  (`Policy/0023 - The 22-26 June 2026 Heat Window ...md`).

The method-sealing commits precede the result-producing commit by roughly two hours, and every
correction was made in the direction of making the operator look worse and the instrument look weaker,
in writing, before the results were known.

The two documents this claim rests on are included in full in this bundle:
- Method (0022): [corpus/Policy/0022 - METHOD - June 2026 Heat-Window Forensic Protocol (Pre-Registration).md](corpus/Policy/0022%20-%20METHOD%20-%20June%202026%20Heat-Window%20Forensic%20Protocol%20%28Pre-Registration%29.md)
- Forensic note, full tables (0023): [corpus/Policy/0023 - The 22-26 June 2026 Heat Window - Data Quality and System Stress Against a Trailing-12-Month Baseline.md](corpus/Policy/0023%20-%20The%2022-26%20June%202026%20Heat%20Window%20-%20Data%20Quality%20and%20System%20Stress%20Against%20a%20Trailing-12-Month%20Baseline.md)

## Honest limits

- A large part of every measurement set is pseudo-measurement (per-bus demand from a national shape,
  and reactive power) at loose uncertainties, because there is no public per-site demand metering and
  no public reactive telemetry. This dilutes the consistency signal, making the detector conservative.
- The gb-spine network is a reduced model of the GB grid, not a full network model.
- The reduced chi-square is a relative index of internal tension between days under one fixed model,
  not an absolute goodness-of-fit score. The baseline runs below one (median about 0.36), which means
  the stated measurement uncertainties are conservative.

These limits are stated next to the findings in the reports, not buried.
