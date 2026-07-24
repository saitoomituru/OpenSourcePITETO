# Open Source Potato Chips 🥔
## Homebrew Potato Thermal Technology — US / Texas Nerd Edition

[🇯🇵 日本語 README](./README.md)

> No job. Still eating chips.  
> Eat the artifact. Upstream the useful knowledge.

I wanted potato chips and did not want to spend money on a bag of potato chips.

So the obvious engineering answer was:

**Build the potato-chip pipeline locally.**

This repo documents a home-kitchen implementation of crispy potato chips using a fryer or frying pan, seasoning, and a hot oven as separate processing stages.

The project was inspired by publicly available information about commercial potato-chip manufacturing, including ideas disclosed by major Japanese snack makers such as Calbee and Koikeya. It does **not** use confidential factory know-how. The goal is to read the function of each process step, then port that function to hardware normal humans actually have in a kitchen.

Call it:

## Potato Thermal Technology, garage edition

![Finished open-source potato chips](./img/04-finished-potato-chips.jpg)

---

## TL;DR

```text
Potato
   ↓
Slice
   ↓
Fry
   │  starch gelatinization
   │  steam generation
   │  porous structure formation
   ↓
Straight out of the fryer
   ↓
Season
   │  use residual moisture + surface oil
   │  to make the flavor stick
   ↓
Drain excess oil
   ↓
Oven at 210°C / about 410°F
   │  short, hot dehydration pass
   │  dry and lock in the porous structure
   ↓
Cool
   ↓
🥔 POTATO DEPLOYED
```

The core rule is simple:

> **Make the fryer do fryer-only work.**  
> **Hand the dehydration job off to the oven.**

---

## 1. Slice the potato

Slice an ordinary potato roughly to potato-chip thickness.

This recipe intentionally does **not** pretend there is one magic thickness and one magic timer for every potato on Earth. Potatoes vary by cultivar, growing region, harvest, storage, moisture, starch content, and whatever chaos happened before the potato reached your kitchen.

Your slicer also has tolerances. Welcome to manufacturing.

That is why the oven stage later uses feedback instead of a fixed time.

![Slicing directly into the frying stage](./img/01-frying-and-slicing.jpg)

---

## 2. Fry stage
### Turn the potato into a tiny steam-built sponge

Fry the slices using normal frying practice for your equipment and oil.

The useful part is not just “hot oil makes potato brown.” Water inside the potato heats up and flashes into steam. At the same time, the starch gelatinizes and the tissue changes structure. As vapor escapes, it helps create a network of tiny voids inside the chip.

In highly technical garage terminology:

> **The potato goes full send in hot oil and steam-machines itself into a microscopic sponge.**

The fry stage is mainly responsible for:

- starch gelatinization
- rapid steam generation
- porous structure formation
- fried flavor and browning

Once those jobs are done, stop asking the oil to be a drying oven too.

---

## 3. Do not chase the entire finish in the frying oil

Trying to drive the chips all the way to bone-dry crispness in an ordinary home frying pan gives you more variables to babysit:

- long oil exposure
- uneven temperature across the pan
- local hot spots
- thermometer location versus actual oil temperature
- changing smoke behavior as oil ages

The desired output is **a dry, crisp chip**, not “the hottest vat of oil a rental kitchen can survive.”

So when the oil-specific work is done, move the remaining job to different hardware.

---

## 4. Seasoning stage
### Season immediately after frying

This timing matters.

The pipeline is:

```text
Out of fryer
    ↓
Onto parchment / draining surface
    ↓
SEASON NOW
    ↓
Drain excess oil + let seasoning bind
    ↓
Oven
```

Use whatever seasoning stack makes you happy:

- seasoned salt
- BBQ
- ranch
- sour cream & onion
- powdered bouillon / consomme-style seasoning
- onion powder blends
- commercial snack seasoning
- the suspiciously effective white powder that makes professional snack food professionally snacky

### Why right now?

Wait until the chip is completely dry and de-oiled, and dry seasoning tends to sit on top instead of becoming part of the chip experience. You end up eating a potato next to a pile of powder.

Season too early, before frying, and a lot of your flavor can migrate into the oil or get hammered by the fry process.

The sweet spot is the short window immediately after frying, while surface oil and some residual moisture are still present.

Those become the binder.

```text
Potato:
“Still got a little moisture over here.”

Flavor powder:
“COPY THAT.”

        ↓

HYPER BINDING
```

Then let excess oil drain while the seasoning grabs the surface.

![Seasoning and oil-drain stage](./img/02-seasoning-and-oil-drain.jpg)

---

## 5. Oven stage
### 210°C / about 410°F, hot and short

Move the seasoned, drained chips into a **preheated 210°C / about 410°F oven**.

> [!WARNING]
> **210°C / 410°F is the OVEN SETPOINT.**  
> **This is NOT an instruction to heat your frying oil to 210°C.**

The second thermal stage is not “fry it again because more frying must be better.” The target is rapid removal of residual moisture from the porous structure you already built during frying.

```text
Fryer
├─ gelatinization
├─ steam expansion
└─ porous structure formation

Seasoning
└─ flavor binding using surface oil + residual moisture

Oven
├─ rapid dehydration
└─ dry structural finishing

Cooling
└─ final texture + flavor stabilization
```

![Oven set to 210°C for the short dehydration pass](./img/03-oven-210c.jpg)

Separating these responsibilities also means you do not need to push a whole pan of frying oil into an unnecessarily aggressive temperature regime just to remove the last bit of water.

---

## 6. There is no fixed oven time

This is the important bit.

I am deliberately **not** giving you “210°C for exactly N minutes.”

Required time changes with:

- slice thickness
- potato cultivar
- growing region
- moisture content
- storage history
- how far the fry stage already went
- actual oven temperature
- airflow
- location on the tray

So this project uses an advanced closed-loop sensor package:

# You.

## Eat one every five minutes.

That is the official control algorithm.

```text
5 minutes
   ↓
sample one chip
   ↓
┌───────────────────────┐
│ Still floppy / chewy? │── YES → keep drying
└───────────────────────┘
   │ NO
   ↓
┌───────────────────────┐
│ Crisp and delicious?  │── NO → inspect and continue
└───────────────────────┘
   │ YES
   ↓
POTATO DEPLOYED
```

If it starts turning into carbon, congratulations: you overfit the model. Roll back immediately.

This is the **Human-in-the-loop Potato Control System**.

---

## 7. Cooling stage
### Do not judge the final build while it is screaming hot

When the texture is where you want it, stop heating and cool the chips promptly instead of letting residual oven heat keep cooking them.

And yes:

# Let them cool before you really go to town on them.

That matters for more than burn prevention. Temperature changes texture, aroma, salt perception, and how intense the seasoning feels.

A heavily seasoned chip straight out of the oven can go from:

```text
THIS RULES

↓

GOOD LORD THAT IS SALTY
```

with impressive speed.

Final acceptance testing should include the cooled product.

---

## 8. POTATO_RECOVERY: resurrecting stale chips

The same basic dehydration idea can sometimes restore crunch to commercial chips that have simply absorbed humidity.

So the repo supports two conceptual modes:

```text
POTATO_BUILD
```

and

```text
POTATO_RECOVERY
```

This is not a time machine for rancid oil or genuinely spoiled food. Re-drying can address moisture-related loss of crunch; it cannot reverse oxidation or make bad food safe again.

---

## Design philosophy

The point is not to photocopy a factory process.

The point is to ask:

> **What function is this processing step actually performing?**

If an industrial line uses multiple thermal stages, your kitchen probably does not have the same machinery. That is fine. Decompose the process into functions and remap those functions to the hardware you do have.

If the required second-stage function is residual-water removal rather than “more oil,” then a hot-air oven can be a valid hardware port.

This is less “secret recipe” and more:

**porting a potato-processing algorithm to commodity kitchen hardware.**

Very normal behavior for people who own both a slicer and opinions about systems architecture.

---

## Safety

This project does **not** recommend pushing frying oil to extreme temperatures.

Again, **210°C / about 410°F refers to the oven setpoint**.

Use normal frying safety appropriate to your oil, fryer/pan, stove, thermometer, and kitchen. Never leave hot oil or the oven stage unattended. Oven setpoints and real cavity temperatures can differ substantially between appliances.

Stop heating if you see abnormal smoking, scorching, or other signs that the process is getting away from you.

Hot trays, hot oil, steam, and freshly cooked chips can burn you. Please keep the Potato CI pipeline out of the incident-response channel.

---

## Status

**v0.2 Experimental / EATABLE**

Tested with:

- home frying pan / fryer
- home oven
- oven setpoint: 210°C / ~410°F
- human-in-the-loop sampling interval: 5 minutes
- result: **Yep. Those are potato chips. 😼🥔**

![The deployed artifact](./img/04-finished-potato-chips.jpg)

---

## Philosophy

Get potatoes from people.

Build chips locally.

Eat the artifact.

Then upstream what was useful.

No job.  
Still eating chips.  
Still doing R&D.  
Not hoarding the knowledge.

# Legal open-source potato chips. 🥔🌱

---

## License

This documentation and recipe are published under **CC BY 4.0 + Remix Declaration**.

Reuse, remixing, redistribution, regional ports, flavor forks, device ports, translations, and commercial use are welcome under the terms of CC BY 4.0. Keep attribution and indicate meaningful modifications.

See [`LICENSE`](./LICENSE) for details.
