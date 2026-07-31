# Raw public data for the window

These are the raw public data feeds for the days in question, copied verbatim so that anyone can check
the inputs behind the reconstruction directly, without taking the solves on trust. Each file covers the
week-26 partition, 22-28 June 2026 (the five window days plus the two following days), at the source's
native resolution.

All of it is published public data from the National Energy System Operator (NESO). It is redistributed
here, unchanged, as small window slices, for verification. The authoritative source, and the licence
terms for each dataset, are on the NESO data portal (https://www.neso.energy/data-portal). Attribution:
NESO. Nothing here is privileged, restricted, or non-public.

| folder | source dataset (NESO) | resolution | rows | key columns |
|---|---|---|--:|---|
| `generation-mix/` | Historic Generation Mix and Carbon Intensity | settlement period (30 min) | 336 | DATETIME, GAS, COAL, NUCLEAR, WIND, WIND_EMB, HYDRO, IMPORTS, ... |
| `demand/` | Historic Demand Data | settlement period (30 min) | 336 | SETTLEMENT_DATE, SETTLEMENT_PERIOD, ND, TSD, ENGLAND_WALES_DEMAND, EMBEDDED_WIND_GENERATION, ... |
| `demand-rolling/` | Demand Data Update (rolling feed) | settlement period (30 min) | 336 | as above (fresh daily feed of the same fields) |
| `system-frequency-1s/` | System Frequency | 1 second | 604800 | dtm, f |
| `system-inertia/` | System Inertia | settlement period (30 min) | 152 | Settlement Date, Settlement Period, Outturn Inertia, Market Provided Inertia |

Files are Apache Parquet. To read one:

```
python -c "import pandas as pd; d=pd.read_parquet('system-frequency-1s/system_frequency_1s_2026-06-22_to_28.parquet'); print(d.shape); print(d.head())"
```

Notes:
- The one-second frequency file is the single most system-relevant record of the week. It carries the
  full 86,400 samples per day, published in full on every window day. The elevated frequency volatility
  on 23 June discussed in the reports is computed directly from this trace - it is in the open record,
  not hidden anywhere.
- The generation-mix feed carries interconnector flows (imports) alongside the fuel breakdown.
- These raw feeds are the public measurements. The exact, weighted measurement set that was fed to the
  estimator for each half-hour is under `solves/plain-text/<date>/measurements/`, with a SHA-256 per
  period.
