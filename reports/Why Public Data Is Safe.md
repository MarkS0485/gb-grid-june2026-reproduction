# Why Public Data Is Safe

### _Why you cannot quietly falsify the state of the grid - the cross-connection is the security - by M. Shirley_

---

**Status:** Independent analysis. A companion to "The Wrong Scandal". It sets out the general
principle that the heat-window reconstruction is one worked instance of: that the published record of
the Great Britain power system is tamper-evident by construction, and that any attempt to hide the
true physical state of the grid in the public data leaves a fingerprint that a state estimator sees
immediately.

---

## 1. The claim, stated plainly

When I say the 22-26 June 2026 data "solves" and was not hidden, the natural objection is: how would
you know? Data can be edited. A number in a spreadsheet can be changed. Why should anyone believe that
a reconstruction from public feeds can tell truth from a doctored record?

The answer is the subject of this note, and it is stronger than most people expect. It is not that we
would probably notice a clumsy edit. It is that **there is no small edit that works.** You cannot
change a few entries in one dataset to hide a stressed grid, because the grid is not described by one
dataset. It is described, redundantly and simultaneously, by dozens of independent public feeds that
are all tied together by the physics of a single connected machine. To move one number honestly you
would have to move all of its echoes in every other feed, and then make the whole set satisfy the laws
of the network at every instant. That is not editing a record. That is fabricating a self-consistent
alternate reality. And a state estimator is built precisely to detect when a set of measurements does
not correspond to any real physical state.

The security is not a password or a signature. The security is the cross-connection itself.

## 2. Layer one: the same fact is published many times, by different people

Great Britain does not publish the grid once. It publishes it many times over, through separate
organisations that do not coordinate their numbers.

- **Generation** appears in the Elexon settlement data (per-unit metered output, B1610), in the system
  operator's own generation-mix feed, in the independent GridWatch record, and by fuel type across
  several places.
- **Demand** appears as national demand and transmission-system demand from the operator, in the
  settlement data, and is cross-checked by embedded-generation and metered-supply estimates.
- **Interconnector flows** are metered at both ends - by the GB operator and by the operator on the
  other side of the link, in another country, under another jurisdiction.
- **System frequency** is published by the operator at one-second resolution, and is measured
  independently by more than one outside monitor that has no connection to the operator at all.

The same physical event - a generator's output, a flow across a cable, the frequency of the whole
system - shows up in several of these at once. To hide it in one place, you must hide it in all of
them, including in the records held by parties you do not control and cannot instruct. A single
custodian cannot quietly rewrite a fact that three other custodians are also publishing.

## 3. Layer two: even a coordinated rewrite has to obey physics

Now suppose the impossible first step is taken, and every custodian rewrites their numbers in lockstep.
It still does not work, because the numbers are not free to take any value. They are bound to each
other by the physical laws of a connected grid.

- Generation minus demand minus losses drives the frequency, through the swing equation. If you lower
  the apparent stress by editing demand down, the frequency trace no longer matches the imbalance it
  is supposed to reflect.
- Every power injection at a bus is tied to the flows on the lines around it, and to the voltages, by
  the power-flow equations. Change an injection and the line flows and voltages that are consistent
  with it change too.
- Every transmission line is metered, in effect, at both ends, and the two ends must agree once losses
  are accounted for.

A grid state is not a list of independent numbers. It is a solution to a large set of simultaneous
physical equations. A doctored value that is not matched by a physically consistent change in every
quantity it touches is not a smaller version of the truth. It is a set of numbers that corresponds to
no possible physical grid. And that is exactly the condition a state estimator is designed to find.

## 4. Layer three: the estimator is over-determined, and it rejects what does not fit

A weighted-least-squares state estimator - the same class of tool a real control room runs internally,
and the one used for this reconstruction - takes all of the published measurements at once, weights
each by its stated uncertainty, and solves for the single grid state that best fits all of them
together. Because the grid publishes far more measurements than there are unknown states, the problem
is heavily over-determined. There is enormous redundancy. The measurements have to agree with each
other, not just be individually plausible.

Two things follow, and they are the heart of why this is safe.

**First, disagreement is measured, not hidden.** The estimator reports how well the measurements
cohered, through a quantity called the reduced chi-square - roughly, the average squared mismatch
between what was measured and what a consistent grid state says should have been measured, in units of
the measurements' own stated uncertainty. If the published numbers all fit together, this sits near or
below one. If someone had shaded the numbers so that they no longer told a single consistent story, the
mismatch would rise, because the doctored rows would fight the honest ones. You do not have to trust a
verdict. You can read the residual.

**Second, bad data is thrown out and the state is recomputed.** When a single measurement is
irreconcilable with the overwhelming weight of the others, the estimator identifies it, rejects it, and
solves again from what remains. A fabrication is not quietly absorbed into the answer. It is isolated,
flagged, and excluded - and the count of rejections is itself a published diagnostic. To hide a stress
event you would need your edits to survive this rejection, which means they would have to be consistent
with every other measurement, which is the very thing they cannot be if they are hiding something real.

So a real tamper has nowhere to go. If it is small, the redundancy swamps it and it is rejected as bad
data. If it is large enough to matter, it breaks consistency across the feeds it touches and the
reduced chi-square climbs and the confidence in the day's reconstruction falls. Either way it shows up
in the output, immediately, as a number anyone can read.

## 5. The theorem

Put the three layers together and the result is not a hope. It is close to a theorem about this
system:

> To hide the true physical state of the grid in the public data, you would have to simultaneously
> rewrite dozens of independently published datasets, held by parties in more than one country, so that
> every rewritten number still satisfied the swing equation and the power-flow equations across the
> entire network, at one-second resolution, with no residual left over. Anything less than that -
> which is to say, every attempt that is actually possible - leaves a measurable inconsistency that a
> state estimator reports as rising reduced chi-square, falling agreement, and bad-data rejections.

You cannot falsify a spreadsheet here. You would have to falsify physics, everywhere, at once, in
public, in agreement with people you do not control. That is why the public data is safe to reason
from. Not because anyone is trusted. Because the record is over-determined, and physics is not
negotiable, and the mismatch is published.

## 6. What honesty requires me to add

I hold my own instrument to the standard I hold everyone else's, so here are its real limits, stated
next to the claim rather than buried.

A large part of every half-hourly measurement set is pseudo-measurement - per-bus demand allocated
from a national shape, and reactive power - carried at loose uncertainties, because there is no public
per-site demand metering and no public reactive telemetry. Those loose rows dilute the consistency
signal: an elevated residual reflects tension chiefly among the well-metered rows, and the soft rows
soften it. The network used here is a reduced model of the real grid, not a full one. And the reduced
chi-square, because the stated uncertainties are conservative, is best read as a relative index of
internal tension between days under one fixed model, not as an absolute score.

None of that weakens the core argument. It means the instrument is a conservative detector - it is
harder for it to raise a false alarm than to miss a subtle one, so when it says a week was consistent,
that is the cautious reading, not the generous one. A more complete measurement set, with real per-site
demand and reactive telemetry, would make the detector sharper, not overturn its logic. The logic is
the redundancy and the physics, and those hold regardless.

## 7. Why this note exists

"The Wrong Scandal" argues that the 22-26 June 2026 public record was complete, internally consistent,
and showed no hidden stress. That is a specific finding about one week. This note is the general reason
you should expect such a finding to be trustworthy, and to be reproducible by anyone who doubts it: the
inputs and outputs are published here in full, and the same measurements fed to any state estimator
will either reproduce the state and the residuals or they will not.

The heat-window reconstruction is one worked instance of the principle. The principle is that a
connected physical system, published many times over, cannot be quietly edited into a different shape.
The cross-connection that makes the grid hard to operate is the same cross-connection that makes its
public record hard to fake. It is, for once, the honest party's advantage.

---

**M. Shirley**
mark@twinscrollgridbalancer.co.uk

*This document is analysis and opinion. It asserts no wrongdoing against any individual. It describes
the general tamper-evidence properties of over-determined state estimation from public data; the
specific reconstruction it refers to is published in full alongside it for independent checking.*
