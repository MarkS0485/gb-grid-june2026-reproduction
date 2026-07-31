#!/usr/bin/env python3
"""
Independent validation of the window-day solves, from the plain-text files only.

Standard library only - no pandas, no pyarrow, no network. Run from anywhere:

    python solves/validate.py

It does three things, all from the shipped plain text:

  1. Re-derives each window day's headline reduced-chi-square (median over the
     day's converged settlement periods) and bad-data removals straight from
     solves/plain-text/<date>/diagnostics.csv, and checks them against the
     figures published in the reports.
  2. Recomputes each day's all-days percentile by ranking that median against
     the 365 trailing-baseline day medians in solves/baseline_day_medians.csv.
  3. Verifies the SHA-256 of every stored measurement input against the
     recorded checksum, so the exact estimator inputs are proven unaltered.

Exit code 0 and "ALL CHECKS PASSED" if everything reconciles, else non-zero.
"""
import csv, os, sys, hashlib, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
PT = os.path.join(HERE, "plain-text")
WINDOW = ["2026-06-22", "2026-06-23", "2026-06-24", "2026-06-25", "2026-06-26"]

# Published figures (from "The Wrong Scandal" / the pre-registered study summary).
PUBLISHED = {
    "2026-06-22": {"rchi2_median": 0.485, "all_days_pctile": 96.7, "removed": 0},
    "2026-06-23": {"rchi2_median": 0.462, "all_days_pctile": 93.7, "removed": 0},
    "2026-06-24": {"rchi2_median": 0.430, "all_days_pctile": 88.2, "removed": 0},
    "2026-06-25": {"rchi2_median": 0.444, "all_days_pctile": 90.7, "removed": 0},
    "2026-06-26": {"rchi2_median": 0.432, "all_days_pctile": 88.2, "removed": 0},
}
BASELINE_MEDIAN_PUBLISHED = 0.359
BASELINE_P95_PUBLISHED = 0.468


def as_bool(s):
    return str(s).strip().lower() in ("true", "1", "yes")


def load_baseline():
    path = os.path.join(HERE, "baseline_day_medians.csv")
    vals = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            vals.append(float(row["rchi2_median"]))
    return vals


def pctile(baseline, value):
    n = len(baseline)
    below = sum(1 for x in baseline if x < value)
    equal = sum(1 for x in baseline if x == value)
    return round(100.0 * (below + 0.5 * equal) / n, 1)


def day_stats(date):
    d = os.path.join(PT, date, "diagnostics.csv")
    rchi, removed = [], 0
    with open(d, newline="") as f:
        for row in csv.DictReader(f):
            if as_bool(row["converged"]):
                rchi.append(float(row["reduced_chi2"]))
            removed += int(float(row["removed_n"]))
    return statistics.median(rchi), removed, len(rchi)


def check_hashes(date):
    mdir = os.path.join(PT, date, "measurements")
    ok = bad = 0
    with open(os.path.join(mdir, "checksums.csv"), newline="") as f:
        for row in csv.DictReader(f):
            sp = int(row["settlement_period"])
            expect = row["measurements_sha256"].strip()
            with open(os.path.join(mdir, "period-%02d.json" % sp), "rb") as g:
                got = hashlib.sha256(g.read()).hexdigest()
            if got == expect:
                ok += 1
            else:
                bad += 1
                print("    SHA MISMATCH period %02d" % sp)
    return ok, bad


def approx(a, b, tol):
    return abs(a - b) <= tol


def main():
    baseline = load_baseline()
    bmed = statistics.median(baseline)
    bp95 = sorted(baseline)[int(round(0.95 * (len(baseline) - 1)))]
    print("Baseline: %d days, median %.4f (published %.3f), P95 %.4f (published %.3f)"
          % (len(baseline), bmed, BASELINE_MEDIAN_PUBLISHED, bp95, BASELINE_P95_PUBLISHED))
    print()
    header = "%-12s %10s %10s %8s %8s %10s %8s" % (
        "date", "rchi2_med", "published", "pctile", "pub", "removals", "sha")
    print(header); print("-" * len(header))

    failures = 0
    for date in WINDOW:
        med, removed, nconv = day_stats(date)
        pa = pctile(baseline, med)
        ok, bad = check_hashes(date)
        pub = PUBLISHED[date]
        med_ok = approx(med, pub["rchi2_median"], 0.001)
        pct_ok = approx(pa, pub["all_days_pctile"], 0.2)
        rem_ok = removed == pub["removed"]
        sha_ok = bad == 0
        if not (med_ok and pct_ok and rem_ok and sha_ok):
            failures += 1
        print("%-12s %10.4f %10.3f %8.1f %8.1f %10d %8s"
              % (date, med, pub["rchi2_median"], pa, pub["all_days_pctile"],
                 removed, "%d/%d" % (ok, ok + bad)))

    print()
    if failures == 0:
        print("ALL CHECKS PASSED: window-day medians, all-days percentiles, bad-data")
        print("removals and every measurement SHA-256 reconcile with the published figures.")
        return 0
    print("FAILURES: %d day(s) did not reconcile." % failures)
    return 1


if __name__ == "__main__":
    sys.exit(main())
