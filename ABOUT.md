# About the author

I am not an electrical engineer, and I am not going to pretend to be one. If you are looking for a
reason to trust this work on the strength of my credentials in power systems, you will not find one,
and you should not look for one.

Here is what I actually am. I am a high-performance-computing engineer. I work with large data every
day. I run computational fluid dynamics on large clusters - solving the governing conservation laws of
a physical system, on a discretised domain, at scale, and checking the answer against measurement.
That is the trade: take a physical system, a great deal of data, and a great deal of compute, and make
them meet in a way that produces a result you can verify. Reproducibility, provenance, and validation
gates are not optional extras in that world; they are the job.

This project is that trade, pointed at the electricity grid. The name for the wider body of work is
deliberate - Electrical Fluid Dynamics. Just as computational fluid dynamics solves the conservation
laws of a fluid on a discretised domain and validates against the measured record, this solves the
conservation laws of an electrical network on the real Great Britain topology and validates against the
public settlement and frequency record. Same discipline, different governing equations.

The methods here are not mine and are not novel. Weighted-least-squares state estimation, the bus
admittance matrix, power flow, the chi-square consistency test, bad-data rejection - these are textbook
power-system tools, standardised for decades. I did not invent any of the electrical engineering. What
I did was assemble those established methods, at scale, over a national volume of public data, with the
engineering discipline that high-performance computing demands, and run them honestly. The novelty, if
there is any, is in the assembly and the scale and the refusal to show a number that a physical law,
checked independently, does not admit - not in the physics, which is old and settled.

That is also why the deeper work is unpublished. The full method is written up as a suite of papers -
they are public, in the corpus, at
https://github.com/MarkS0485/TSGB-2026/tree/main/EFD - drafted to the standard of a peer-reviewed
venue. None of them has been submitted. The reason is simple and it is not modesty: I have no formal
electrical-engineering training, and so no route into an electrical-engineering publication venue - no
institution, no supervisor, no standing to put a manuscript in front of a power-systems journal and be
read rather than dismissed on sight. The peer-review pathway is closed to me by credential, not by
content. So the software has to be the peer review. The code is the proof. If the established channels
will not read the paper, the public can run the program.

Which is the whole point of this bundle. I am not asking you to believe me, and I have gone to some
length to make sure you do not have to. Everything needed to check the physical claim is here: the raw
public inputs, the exact measurements with their cryptographic hashes, the network model, the solved
states, and a validator that recomputes the headline figures from first principles. Feed the inputs to
your own state estimator. Try to break a solve. Change a number in the input and watch the residuals
catch it. If I am wrong, the apparatus is built to show that I am wrong, and I would rather you find it
than take my word for anything.

I am not asking for your trust. I am asking you to run it and see for yourself.

M. Shirley
mark@twinscrollgridbalancer.co.uk
