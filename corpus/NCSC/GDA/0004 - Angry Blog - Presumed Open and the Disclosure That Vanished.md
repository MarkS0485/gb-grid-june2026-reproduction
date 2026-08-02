# On Presumed Open, Quietly Adopted

*An angry blog about the Data Best Practice Guidance, the responsible disclosure it made necessary, and the Ofgem consultation that arrived six weeks later wearing the same architecture and none of the attribution.*

---

## The policy was too lax. Always. No matter how you cut it.

There is no version of the previous open data policy that survives serious scrutiny, and there never was.

The Data Best Practice Guidance and its "presumed open" doctrine asked the operator of the GB electricity system to publish, in machine-readable form: the heartbeat of the grid (one-second frequency), the geometry of the grid (shapefiles of every cable, transformer and pole at street-level precision), the loading of the grid (half-hourly transformer flows), and the playbook of the grid (fifteen years of balancing decisions). It then asked the world to assume that no actor with internet access would assemble these into a near-operational picture of Critical National Infrastructure.

That was not a defensible bet in 2021. It was not a defensible bet in 2023 when it was extended to the DNOs. It was not a defensible bet on the day the Ofgem consultation now blandly describes as "before the changed risk environment". The "Good Actor environment" the policy implicitly assumed has never existed in the form the policy required. The doctrine was written as if the threat model began with adversarial intent and ended with a single dataset. Both ends of that model were wrong, and the people who wrote it should have known they were wrong.

I am not making that argument from hindsight. I am making it from the fact that one person, working alone, with no privileged access, demonstrated it in weeks.

## The thing that proves it

In April I disclosed a system called GDA - Grid Data Analysis. It ingests roughly seven and a half thousand discrete public data sources, normalises them to a common time domain, anchors everything to the published one-second frequency trace, and uses the physics of the Swing Equation to collapse the solution space until what remains is a near-operational reconstruction of the GB electricity grid.

It runs on commodity hardware. It cost ten pounds to train end-to-end on a cheap GPU instance. It uses no privileged access of any kind. Every single byte of input is something Ofgem's policy actively required somebody to publish.

That is the falsification of the policy. Not a hypothetical. Not a future risk to be mitigated. A working system, written by one person, demonstrating that the presumed-open doctrine put a near-operational picture of CNI on the open internet for anyone to walk in and pick up.

I disclosed it on 11 April 2026 to NCSC, DSIT, Ofgem, NESO and DESNZ through the proper channel. I was invited to brief NCSC on 19 April. The work was recognised, on the public record, with an Ada Lovelace challenge coin.

I mention the coin not to wave it around. I mention it because it is documentary evidence that the path I took was the path I was meant to take. The channel worked. The receiving authority took it seriously. The disclosure produced its intended effect - a policy review.

So far so good. This is where it stops being so good.

## Six weeks later, the same architecture

On 29 May 2026, Ofgem published "Securing Open Data in Energy". It presents three options for reforming the triage process - Centralised, Hybrid and Educational - and a minded-to position favouring the Hybrid Model.

Read alongside s.11 of the disclosure, the resemblance is not subtle.

| GDA Responsible Disclosure (11 April) | Ofgem Consultation (29 May) |
|---|---|
| s.11.3.2 - *"Registered Access Tiers... available to identified academic institutions, commercial parties and regulated service providers, with audit trail and terms of use."* | **Hybrid Model.** Minded-to position. |
| s.11.2.2 / s.11.1.1 - gated query interfaces and registered-access schemes replacing bulk public downloads, held centrally. | **Centralised Model.** |
| s.11.4.2 - NCSC to issue guidance to CNI operators on the mosaic effect, including *"a recommended methodology for collective sensitivity assessment and a standard for data publication decisions"*. | **Educational Model.** |
| s.11.3.1 - collective sensitivity assessment framework; aggregation as the central problem. | s.2.14 - aggregation risk; s.3.2 - collective triage framework. |
| s.11.1.1 - temporal coarsening / publication lag on high-resolution data. | s.2.17 - noise, delay, aggregation, redaction. |

Three buckets in, three buckets out. Same framing of aggregation risk. Same minded-to position. Six weeks between the NCSC briefing and the consultation going to press.

I want to be careful about what I am and am not claiming. I am not claiming exclusive authorship of these ideas. Registered access tiers, mosaic-effect framing and collective sensitivity assessment are not novel concepts. Ofgem has every right to converge on them, and frankly should have converged on them years ago. I do not want my name on the consultation. I do not want a footnote. I do not want a coin from Ofgem to go with the coin from NCSC.

What I want is for the policy record to be honest about what made this consultation possible, because if it isn't, the channel that made this consultation possible breaks.

## What's missing - and why it matters

The Berlin power cut cited in s.2.10 happened in January. The consultation went out in May. The threat picture in s.2 is sourced from international press coverage, the National Risk Register, and the IEA's reporting on Ukraine. Read the document cold and you would think the rationale for action came entirely from abroad.

It did not. A domestic researcher demonstrated, on UK soil, against UK CNI, using UK public data, that the policy was broken. That demonstration was disclosed through the proper channel and accepted. It is the most direct piece of evidence the consultation could cite - and the consultation does not cite it.

You can verify this for yourself. Open the PDF. Search for "responsible disclosure". Zero hits. Search for "disclosure". Zero hits. Search the executive summary, s.2, s.3, the glossary, Appendix 1's list of linked publications. Nothing. A reader of this consultation has no way of knowing that the three-option framework they are being asked to comment on did not arrive by spontaneous policy generation.

That omission is not neutral. It removes from the public record the evidence that the responsible disclosure channel works in this sector. The next researcher who builds something comparable will look at this consultation to see what happened to the last one and will see no trace of them. The lesson on offer is that the channel produces policy outcomes but not visibility - and that is precisely the lesson that will persuade the next person, who may not pick up the phone, not to.

If the policy intent is to keep responsible disclosure functioning as an instrument of CNI defence, the policy process has to close the loop visibly with the people who feed it. This one doesn't.

That is the thing I am angry about. Not the work. The work is, broadly, correct. The Hybrid Model is the right answer. I will be saying so, in detail, in my formal response.

I am angry about a process that takes a demonstration, accepts the conclusions, adopts the architecture, and then files the disclosure into a part of the record that the public version cannot see. A process that talks at length about transparency while being structurally incapable of transparency about its own inputs.

## The bit I want to land cleanly

The data is out there. The physics cannot be changed. The publication policy is the only variable left.

Whether responsible disclosure remains a useful instrument in this sector is also a variable. That one is controlled by Ofgem and DESNZ. The next person who finds something will read this consultation before they decide what to do. Make sure the version they read is one that gives them a reason to call.

-

**Mark**
Author, GDA Responsible Disclosure (11 April 2026)
Briefed NCSC, 19 April 2026 - Ada Lovelace challenge coin
mark@twinscrollgridbalancer.co.uk
6 June 2026
