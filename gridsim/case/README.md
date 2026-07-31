# gb-spine network case

These eight JSON files are the reduced Great Britain transmission network ("gb-spine") that the state
estimator solves against. The case is self-contained plain JSON with no external dependencies, so it
travels with this bundle and can be loaded by any tool that reads the format.

Scale: 316 buses, 579 branches, 1025 generators, 305 demand points. Slack bus MELK_1 (Melksham).
Base 100 MVA, 50 Hz. It is a fold of a larger full-GB model down to a GSP-level spine; it is a coarse
reduced model, not a full network model, and that is stated wherever findings depend on it.

| file | contents |
|---|---|
| `system.json` | case-level settings (base MVA, frequency) |
| `buses.json` | buses: id, name, base kV |
| `transmission.json` | branches: from/to, impedance, ratings |
| `generation.json` | generators: bus, limits, type |
| `demand.json` | demand points: bus, share |
| `boundaries.json` | network boundary definitions |
| `fold_map.json` | map from full-model buses to their spine owner (provenance) |
| `diagnostics.json` | build statistics (bus/branch/generator counts, totals) |

The case was built from public data. It carries the network topology and electrical parameters only;
it contains no measurements. The measurements for each solved period are shipped separately under
`solves/plain-text/<date>/measurements/`.
