# Inertia

> ***Inertia is not a service. It is a state of matter. You cannot procure it. You can only spin it.***

# Table of Contents

- [1. Inertia in one paragraph](#1-inertia-in-one-paragraph)
- [2. The physics that matters](#2-the-physics-that-matters)
- [3. RoCoF - the thing inertia actually buys you](#3-rocof-the-thing-inertia-actually-buys-you)
- [4. How inertia is measured on a grid](#4-how-inertia-is-measured-on-a-grid)
- [5. How much inertia does the GB grid have](#5-how-much-inertia-does-the-gb-grid-have)
- [6. Where the inertia went](#6-where-the-inertia-went)
- [7. "Synthetic" inertia - what it is and isn't](#7-synthetic-inertia-what-it-is-and-isnt)
- [8. The temporal argument](#8-the-temporal-argument)
- [9. Inertia and the cascade-blackout problem](#9-inertia-and-the-cascade-blackout-problem)
- [10. Inertia and TSGB](#10-inertia-and-tsgb)
- [11. Bottom line](#11-bottom-line)
- [Related Documents](#related-documents)

---

# 1. Inertia in one paragraph

Every spinning thing on a power network - generator rotor, motor armature, even big industrial flywheels - carries kinetic energy. When the network's frequency tries to change, all those spinning things resist that change physically. They don't ask permission, they don't compute, they don't communicate. They just resist, because Newton said so. The total kinetic energy available to resist frequency change is the **inertia** of the system. More inertia means slower frequency excursions, more time to respond, smaller swings, less risk of cascade. Less inertia means faster excursions, less time, bigger swings, more risk. That's it. That's the entire concept. The rest of this explainer is filling in why it can't be faked.

---

# 2. The physics that matters

For a rotating body, kinetic energy is:

$$E_{k} = \tfrac{1}{2} J \omega^{2}$$

Where:

- **J** is the moment of inertia (kg.m^2, a property of how mass is distributed around the axis of rotation),
- **omega** (omega) is the angular velocity (rad/s).

A synchronous generator's rotor is rigidly locked to the grid frequency via the magnetic coupling between rotor and stator. Change the grid frequency and you have to change the rotor's omega. Changing omega requires changing E_k. Changing E_k requires energy in or out of the rotor.

So when something perturbs the grid frequency - a generator trips, a load steps, a line opens - the perturbation has to draw kinetic energy out of every synchronous rotor on the network (if frequency is falling) or push energy in (if frequency is rising). And that draw/push happens **instantly**, because the rotors are physically connected. There's no decision, no detection, no PLL, no comms.

That's the gift of synchronous mass. Frequency stability is, for free, the steady-state expression of all the spinning things on the grid being unwilling to change speed quickly.

For an entire system, the **inertia constant H** (in seconds) is defined as:

$$H = \dfrac{E_{k,\text{stored}}}{S_{\text{rated}}}$$

H tells you how many seconds the machine could supply its rated power purely from its own kinetic reservoir before its speed dropped to zero. Typical values:

- **Steam turbine alternator:** H ~= 4-7 s
- **Hydro alternator:** H ~= 2-4 s
- **Gas turbine alternator:** H ~= 4-6 s
- **Wind turbine (locked rotor):** H ~= 2-3 s, but it's _decoupled_ from grid frequency through the inverter, so it doesn't contribute system inertia.
- **Solar PV:** H = 0. Zero. Nothing rotating, nothing coupled.

The grid's _system inertia_ is the sum of (H x S) across all the synchronously coupled machines on the network. That sum is what dictates how fast the frequency can swing.

---

# 3. RoCoF - the thing inertia actually buys you

**Rate of Change of Frequency** (RoCoF) is how fast the grid's frequency is moving, in Hz per second. It is, more than any other single number, the thing that inertia controls.

The relationship, in simplified form:

$$\dfrac{df}{dt} = \dfrac{f_{0}}{2H_{\text{sys}}} \cdot \dfrac{\Delta P}{S_{\text{sys}}}$$

Where:

- **f0** is nominal frequency (50 Hz in the UK),
- **H_sys** is the system inertia constant,
- **deltaP** is the size of the active-power disturbance (e.g. a generator trip),
- **S_sys** is the total connected synchronous capacity.

You can see from that equation: **halve the inertia, double the RoCoF**, for the same disturbance. This is why a grid with lots of synchronous plant rides through events that would break a low-inertia grid. The disturbance is the same; the response is gentler because the rotors swallow the shock.

Modern UK protection codes (G99, ENA TS 48) typically require generators to ride through up to **1.0 Hz/s** RoCoF. Historically, with hundreds of GVA.s of inertia, the GB grid rarely saw more than 0.1-0.2 Hz/s during major events. Today, with system inertia routinely sitting at 120 GVA.s, the 9 August 2019 blackout showed RoCoF spikes near 0.5 Hz/s, and the network was within a hair of cascading further.

RoCoF and inertia are the same equation read from different sides.

---

# 4. How inertia is measured on a grid

System inertia is typically reported in **gigawatt-volt-amperes-seconds** (GVA.s) or sometimes megawatt-seconds (MW.s). Either way it's an energy reservoir - the kinetic energy stored across all the synchronously coupled rotating mass on the grid at a given instant.

The number is _instantaneous_, not nameplate. A 660 MW thermal unit with H = 5 s contributes 660 x 5 = 3,300 MVA.s ~= 3.3 GVA.s _when it's synchronised and running_. The moment it trips, that contribution evaporates from the grid's total.

ESO publishes "Outturn Inertia" figures showing what the system actually had at a given half-hour. The Markout vs Outturn gap (the difference between forecast and actual) is itself a useful operational signal - and the gap has been growing.

Industry conventions you'll see:

- **GVA.s** - total system kinetic reservoir.
- **MW.s/MW** - H expressed as seconds.
- **System H** - area-wide inertia constant.

When you see policy documents talk about a "minimum inertia requirement," they're saying _the system shall not be operated below this many GVA.s of stored kinetic energy at any instant_. The current GB requirement has been progressively lowered. [Frequency Risk and Control 2025](../Policy/0006 - The Managed Collapse of Inertia.md) takes it to roughly 102 GVA.s, an unprecedented contraction.

---

# 5. How much inertia does the GB grid have

Historically - say, 1990s, when GB ran on coal and nuclear with a few CCGTs - system inertia routinely sat between **300 and 400 GVA.s**, sometimes more. Disturbances were absorbed without drama. RoCoF events were small and rare. Frequency stayed inside +/-0.2 Hz almost all the time.

Today (rough orders, varying half-hour to half-hour):

- **Low load, high wind/solar:** 120-160 GVA.s.
- **High load, traditional plant online:** 200-280 GVA.s.
- **Historic record low (observed):** ~50 GVA.s, briefly, in 2019.
- **Future target (FRCR 2025):** 102 GVA.s minimum.

The trend is unambiguously down. The mass is being retired and not replaced.

You can plot this. ESO publishes the data. The shape of the chart is a slow, continuous slide that maps almost perfectly onto the decommissioning of coal stations and the integration of inverter-based renewables. It is not subtle.

---

# 6. Where the inertia went

Three things happened, in order:

1. **Coal retired.** The UK retired about 30 GW of coal between 2012 and 2024. Each of those units contributed 4-6 seconds of H x hundreds of MW of S. That's the bulk of the bleed.

2. **Nuclear is on the way out.** Old AGRs are end-of-life. New build is delayed. Nuclear was a high-H contributor; its decline removes a lot.

3. **Renewable replacements don't replace the inertia.** A 660 MW coal unit contributing 3.3 GVA.s gets replaced with 660 MW of wind, whose mechanical mass is huge but **decoupled** from the grid via inverters. From a grid-inertia perspective, that's a swap of 3.3 GVA.s for 0. Solar is even worse - there's nothing rotating to begin with.

This is the "drained battery" pattern: every retirement removes inertia, every renewable addition adds zero. The grid was running on the legacy inertia base for years; that base is now visibly drained.

You can argue this was foreseeable or not, deliberate or not. It is **the reason** RoCoF events have gone from rare to routine. It is the reason the system has become brittle to single contingencies that it would have shrugged off in 2005.

The policy framing for this is documented in [The Managed Collapse of Inertia](../Policy/0006 - The Managed Collapse of Inertia.md) and the broader strategic critique in [The 2050 Lie](../Policy/0005 - The 2050 Delusion.md).

---

# 7. "Synthetic" inertia - what it is and isn't

Synthetic inertia is the marketing-friendly name for an inverter control mode that **detects** a frequency change and responds with an active-power injection chosen to mimic what a real inertial machine would have done.

Three things to understand about it:

**It is reactive, not resistive.** A real inertia machine resists change continuously, by physics, at the moment of disturbance. Synthetic inertia needs to first **detect** that a disturbance is happening (typically a frequency deviation crossing a threshold), then **decide** to respond, then **dispatch** an active-power injection. Detection takes a measurement window. Decision takes computation. Dispatch takes a control loop. The fastest implementations are around 50-100 ms; real synchronous inertia acts in zero milliseconds because there's no detection stage.

**It is bounded by the silicon.** A real synchronous rotor's kinetic energy is whatever is stored in it, instantly available, limited only by the mechanical strength of the steel. A synthetic inertia injection is bounded by whatever the inverter's IGBTs can pass safely, for however long the thermal margin allows. That's measured in cycles, not seconds.

**It depends on having a DC source ready to deliver.** Real inertia is _kinetic energy already in the rotor_. Synthetic inertia is _energy that has to flow from a DC source, through the inverter, into the AC network_. If the DC source is a battery, fine - for a while. If it's a wind turbine running at curtailed output, the energy is being _taken out of the rotor_, which means the turbine spins down, which means the next event has even less to work with.

Synthetic inertia is not useless. Done well, it improves the system's response to slow, gentle frequency events. But it cannot replace real inertia for fast, large events - and the fast, large events are exactly the ones that take a grid down. The policy framing that treats them as equivalent is a category error.

---

# 8. The temporal argument

The thing inertia really gives you is **time**. Time for governors to respond. Time for primary frequency control to kick in. Time for the system operator to dispatch reserves. Time for protection coordination to work as designed.

Without inertia, the system has the same disturbances but no time to handle them. Protection schemes that were designed assuming 0.1 Hz/s now see 0.5 Hz/s and trip aggressively. Frequency response services that were designed to act within 1 second can't catch up before the frequency has already breached the trip threshold.

This is why you'll see operators talking about "fast frequency response" (FFR), "dynamic containment," and similar reactive services. These are all attempts to fill the temporal gap that lost inertia has opened. They're real and they do something. They are not a substitute for the original gift, which is "time, granted free, by physics."

If you want a one-liner: **inertia buys you time; reactive services try to spend more in less time. Whichever costs less is debatable. Which one is reliable is not.**

---

# 9. Inertia and the cascade-blackout problem

Most large blackouts are RoCoF cascades. The sequence is depressingly consistent:

1. Initiating event - generator trip, line opens, fault.
2. Frequency starts to move; rate of change is large because system inertia is low.
3. Distributed generation hits its RoCoF protection threshold and trips out _because the standard tells it to_ - typically 1.0 Hz/s for new connections, lower for older equipment.
4. Tripped generation means more lost active power, which makes RoCoF worse.
5. More trips. Cascade.
6. Grid fragments into islands. Some islands die. Some survive on whatever inertia is locally trapped.

The 2019 GB blackout is the case study. ~1.4 GW of generation lost in seconds, partly due to RoCoF tripping that was technically conforming to its protection settings. In a higher-inertia grid, the same initiating event would have produced a smaller RoCoF and fewer follow-on trips. The cascade would have stopped earlier or never started.

The argument is not "blackouts wouldn't happen with more inertia." The argument is "small events are less likely to become big ones." That's all inertia ever did. It's still all it has to do.

---

# 10. Inertia and TSGB

A Twin Scroll Grid Balancer is a fully synchronous machine with a deliberately heavy rotor and a wide selection of available shaft inertias. Its job is to put real inertia back on the network, modularly, distributable to substations and renewable sites, without relying on the fuel plant we're retiring.

The contribution is straightforward:

- A 10 MW TSGB module with a 10-tonne rotor at 3,000 rpm carries roughly 100 MJ of kinetic energy, contributing on the order of 0.1 GVA.s of system inertia per unit.
- A fleet of 100 modules across the country contributes ~10 GVA.s - a meaningful slice of the 102 GVA.s FRCR 2025 minimum.
- Larger TSGB units (50-100 MW) scale linearly. A 100 MW unit with appropriate shaft sizing can contribute ~1 GVA.s by itself.

The technical detail is in the White Paper sections 4.2 and 5. The crucial design choice - that the rotor is fed by a DC drive that can accept solar, wind, HVDC or battery input - means the inertia is **decoupled from the fuel source**. You can run a TSGB on renewable input and still get the synchronous mass contribution that wind and solar alone cannot provide.

The point is not that TSGB is the only answer. The point is that **putting synchronous rotating mass back on the grid is the only path to restoring inertia, and TSGB is one available way to do it without retreating from the renewable transition**.

---

# 11. Bottom line

Inertia is the time and reflexive resistance the grid gets for free from spinning steel. It is finite. It is being drained. It cannot be replaced by software, because software responds - it does not resist. The two are not the same physical phenomenon, and treating them as equivalent has cost real money, real disruption, and increasingly real reliability.

> **Stop optimising response. Start restoring resistance.**

---

## Related Documents

### Companion Electrical Explainers

- Phase Authority
- Reactive Power
- Voltage Control
- Harmonic Distortion
- Hunting
- SCL & Fault Current
- Generator Excitation
- PCC - Point of Common Coupling
- GSP - Grid Supply Point
- BSP - Bulk Supply Point
- Engineering Recommendations

### TSGB Core Documents

- TSGB White Paper (Full) - Complete technical specification including inertia calculations.
- TSGB White Paper (Concise) - Short-form overview.
- Addendum A1 - Lean In And Get Under It - How inertia is _applied_ as torque, sub-cycle.

### Policy Critique

- [The Managed Collapse of Inertia](../Policy/0006 - The Managed Collapse of Inertia.md) - FRCR 2025 as a managed reduction in inertia.
- [The 2050 Lie](../Policy/0005 - The 2050 Delusion.md) - Net Zero strategy as admission of inertia loss.
- Why the Grid Must Be Built on Intrinsics - Inertia as an intrinsic property.

### Theoretical Underpinnings

- Loss of Signal - Emergent behaviour when inertia is exhausted.
- FlexFreq - Frequency-flexible architecture built on inertia distribution.
