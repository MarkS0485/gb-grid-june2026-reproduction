# Reproducing a solve

There are two ways to check a solve in this bundle. The first needs nothing but a state estimator of
your own and is the one that matters. The second reproduces the exact estimator that produced the
library.

## What a solve is

For each settlement period, the estimator takes a set of public measurements (metered generation,
interconnector flows, and demand and voltage pseudo-measurements), weights each by its stated
uncertainty, and solves for the single grid state - bus voltage magnitudes and angles, and net
injections - that best fits all of them at once over the gb-spine network. It reports how well the
measurements agreed (the objective J, the degrees of freedom, the reduced chi-square) and rejects any
measurement that is irreconcilable with the rest (bad-data rejection).

The exact input to each period is `solves/plain-text/<date>/measurements/period-NN.json`, a
`gridsim-measurements/1` document. Its SHA-256 is recorded in the same folder's `checksums.csv`, so the
input is provably the one that was used.

## Path 1: estimator-independent (recommended)

You do not need our estimator. Any weighted-least-squares state estimator will do.

1. Load the network from `gridsim/case/` (316 buses, 579 branches, 1025 generators; base 100 MVA).
2. Take the measurement set for a period from
   `solves/plain-text/<date>/measurements/period-NN.json`. Each entry gives a measurement kind, the
   bus or branch it applies to, its value, and its standard deviation (weight).
3. Run your weighted-least-squares estimator: minimise the sum of squared normalised residuals over
   the network, with bad-data rejection on the largest normalised residual as usual.
4. Compare your result to ours:
   - the state, against `solves/plain-text/<date>/solved_state.csv` (per bus: vm, va_deg, p_inj_mw,
     q_inj_mvar);
   - the branch flows, against `solves/plain-text/<date>/line_flows.csv`;
   - the objective J, degrees of freedom, reduced chi-square and any rejections, against
     `solves/plain-text/<date>/diagnostics.csv`.

If the published measurements had been shaded to hide a stressed grid, an honest estimator would show
it: the residuals would not close, the reduced chi-square would climb, and measurements would be
rejected. On these days they do not. That check does not depend on trusting our code at all.

## Path 2: the exact estimator (GridSim)

The solves were produced by GridSim, the author's weighted-least-squares estimator. GridSim is not part
of this public release. If you have it, a period is reproduced with:

```
GridSim.Cli estimate <path to gridsim/case> \
    --measurements <path to a period-NN.json> \
    --prior solve --warm-start --export-solve
```

and the reported objective, degrees of freedom, chi-square verdict and solved state can be compared to
the `diagnostics`/`solved_state` files above. Note that the library was built from a specific working
tree of GridSim (commit `dbeee06`, recorded per day in `solves/parquet/manifest_*.json` together with
the executable SHA-256); a bit-exact match requires that build. For everyone else, Path 1 is the
stronger check anyway, because it is independent of our software.
