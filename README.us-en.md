# Open Source Potato Chips 🥔
## Home-Scale Potato Thermal Technology

[日本語（正本）](./README.md) | **English (US) — Texas garage-lab edition**

> No job. Still eating chips.  
> We eat the artifact and return the useful knowledge to the commons.

We were broke, wanted potato chips, and asked the obvious engineering question:

**Why not build them?**

This is a home potato-chip manufacturing experiment for NEETs, garage-lab nerds, kitchen hackers, and anyone who would rather understand a process than pay for mystery.

The famous homebrew failure mode is simple:

**You fry the potato, but it never gets properly crisp.**

So we treated published commercial potato-chip methods and general food science as public references, then asked what physical job each stage performs. We are not cloning a factory line. We are porting its useful functions onto hardware already found in a home:

- a fryer or deep pot;
- an oven;
- parchment paper or another oven-safe liner;
- and a human mouth.

Call it:

## Potato Thermal Technology: the home OSS port

<p align="center">
  <img src="./img/04-finished-potato-chips.jpg" alt="Homemade potato chips after the oven drying stage" width="560">
</p>

> This is the edible output from the documented household setup, not a generated beauty shot.

---

## TL;DR

```text
potato
  ↓
slice thin
  ↓
FRY
  │  gelatinize starch
  │  generate steam
  │  form a porous structure
  ↓
season immediately
  │  use surface oil and residual moisture
  │  to bind the flavor powder
  ↓
drain
  ↓
OVEN AT 210°C / 410°F
  │  short, hot finishing dry
  │  lock in the porous structure
  ↓
cool
  ↓
🥔 POTATO DEPLOYED
```

The governing rule:

> **Let the oil do only the jobs that require oil. Let the oven handle the final drying.**

---

## 1. Slice the potato

Slice an ordinary potato to roughly potato-chip thickness.

There is no single sacred thickness in this implementation. Cultivar, source, storage, water content, starch content, and slicer geometry all change the run. That variability is why the final oven stage uses feedback instead of a fake universal timer.

## 2. Fry: build a microscopic potato sponge

Frying does more than “cook it in oil.” Water inside the slice becomes steam and escapes. The starch heats and gelatinizes while the tissue changes structure. Fine voids form inside the chip.

In less polite lab language:

> The potato goes feral in hot oil and the steam turns it into a tiny sponge.

The fryer is responsible for:

- starch gelatinization;
- rapid steam generation;
- porous-structure formation;
- and fried flavor.

That is where the fryer’s assignment ends.

## 3. Do not force the oil to finish every job

Trying to reach final dryness in a household fryer adds variables: long oil heating, hot spots, thermometer placement, pot geometry, and the changing smoke behavior of the oil.

We do not want “unreasonably hot oil.” We want “a crisp chip with less residual water.”

Once oil is no longer required for the next physical job, move the workload to another heat source.

## 4. Season immediately after frying

The seasoning window is short:

```text
out of the fryer
  ↓
onto the liner
  ↓
season immediately
  ↓
drain excess oil while the powder binds
  ↓
oven
```

Use whatever powder works for the run: seasoned salt, onion, sour cream, bouillon-style seasoning, commercial potato seasoning, or your own suspiciously effective white powder.

If the chip is already bone-dry and all the surface oil is gone, the powder will not bind well. You end up eating separate layers of potato and loose seasoning. If you load the seasoning before frying, too much flavor can escape into the oil or take excessive heat.

Right after frying, the chip still has surface oil and residual water. Use that window as the binding interface.

<p align="center">
  <img src="./img/02-seasoning-and-oil-drain.jpg" alt="Freshly fried potato chips being seasoned and drained" width="480">
</p>

> Seasoned immediately after frying, then held while the excess oil drains.

## 5. Oven finish: 210°C / 410°F

Move the drained chips into an oven preheated to **210°C / 410°F**.

> [!WARNING]
> **That temperature is the oven setpoint. Do not heat the frying oil to 210°C / 410°F.**

The goal is not a second fry. It is a short, high-temperature removal of residual moisture from the porous structure already formed during frying.

<p align="center">
  <img src="./img/03-oven-210c.jpg" alt="Household oven operating at a 210 degree Celsius setpoint" width="480">
</p>

> The test appliance displaying the oven setpoint. This is evidence of the oven stage, not an oil-temperature instruction.

```text
Fryer
├─ gelatinization
├─ steam expansion
└─ porous structure

Seasoning
└─ flavor binding through surface oil and residual moisture

Oven
├─ rapid finishing dry
└─ dry fixation of the porous structure

Cooling
└─ final texture and flavor stabilization
```

## 6. There is no universal oven time

We do not specify “210°C for exactly N minutes,” because every potato and every household oven is different.

The controller for this version is extremely advanced:

# It is a human.

## Sample one chip every five minutes.

```text
wait 5 minutes
  ↓
taste one
  ↓
still floppy? ── YES → keep heating
  │ NO
  ↓
crisp and good? ── NO → inspect and continue if appropriate
  │ YES
  ↓
POTATO DEPLOYED
```

If they start burning, you overfit the model. Roll back immediately.

This is the **Human-in-the-loop Potato Control System**. Texas pit nerds already understand the principle: the dial is an input, but the food is the sensor that closes the loop.

## 7. Cool before final judgment

Stop heating when the texture is right, remove the tray from continued heat, and let the chips cool.

Cooling changes texture, aroma, salt perception, and the overall seasoning balance. A chip that tastes perfect while dangerously hot can taste aggressively salty once you keep eating it. Final acceptance testing includes a cooled sample.

## 8. Recovery mode

The same idea can re-dry store-bought or homemade chips that lost their crunch to humidity:

```text
POTATO_BUILD
POTATO_RECOVERY
```

Drying can recover texture lost to moisture. It cannot reverse rancidity or make oxidized food new again.

---

## Design philosophy: port the function, not the factory

The central move is to stop copying the visible machine and ask:

> What physical job is this machine here to accomplish?

If a factory uses two heat stages, your kitchen does not need the same machines. If the second job is moisture removal rather than another oil-specific transformation, it can be ported to an oven.

This is recipe engineering for the human logistics layer: low-cost inputs, household hardware, body-scale sensing, an edible artifact, and knowledge returned to the commons. It is separate from the SphereOS abstract-software workspace and the Deb800 field-hardware workspace; it does not require either one to cook a chip.

## Safety

- Follow the normal safety limits for your oil, fryer, pot, oven, liner, and kitchen.
- **210°C / 410°F is the oven setting in this test, not a frying-oil target.**
- Household oven setpoints and actual cavity temperatures can differ.
- Do not leave hot oil, an oily tray, or high-temperature drying unattended.
- Stop heating if you see burning, smoke, liner failure, or other abnormal behavior.

## Status

**v0.2 Experimental / EATABLE**

Tested with:

- household fryer / deep-frying pot;
- household oven;
- oven setpoint: 210°C / 410°F;
- human sampling interval: 5 minutes;
- observed result: **it became an actual potato chip 😼🥔**

The three photos document the post-fry, oven-running, and post-oven states of this run. They do not establish one universal cook time across potatoes, slice thicknesses, or appliances.

## Contribute an experiment note

Reproductions, modifications, failed batches, and humidity-recovery tests can be recorded under [`note/`](./note/). Read [`note/AGENTS.md`](./note/AGENTS.md) and copy [`note/TEMPLATE.ja.md`](./note/TEMPLATE.ja.md) before writing.

Keep observations, interpretation, hypotheses, inner notes or project poetry, and unknowns separate. A draft note does not automatically change the canonical Japanese recipe.

## Experience OSS stewardship through a potato

We are testing whether OpenSourcePITETO can work as a natural-language OSS field school where non-programmers experience forks, provenance, licenses, branches, diffs, issues, and reproduction costs.

- [en-US research note: Can a Potato Explain the OSS Free-Rider Problem?](./note/20260724-1339__can-a-potato-explain-the-oss-free-rider-problem.en-US.md)
- [en-US issue draft: Natural-Language OSS Potato Field School](./note/20260724-1348__natural-language-oss-potato-field-school.issue.en-US.md)
- [Japanese source issue draft](./note/20260724-1348__自然言語OSS芋寺子屋_issue草案.ja.md)

Codespaces, Copilot, Codex, and similar tools can assist with documents, comparisons, history, and collaboration. They are not the authority for rights, publication, or food safety. You can fork the document. You cannot fork the potato or the human body.

AI can structure the recipe. Your mouth and subjective experience review whether the chip tastes good. This OSS potato lab preserves both wheels: objective rerun records and the non-fungible personal experience of “delicious.”

Potato spirit does not make a rotten potato safe. Perfect process specifications do not make an unbearable flavor delicious. The two-wheel contract keeps story from canceling safety, keeps safety and uniformity from impersonating demand, and keeps taste mismatch separate from abusive customer behavior.

When the question grows into “good for which observer, in which body state, moment, purpose, and World?”, it routes toward [SphereOS Atlantis](https://github.com/saitoomituru/SphereOS-Atlantis) and its [Context Dimension / D Fold / OAE shelf](https://github.com/saitoomituru/SphereOS-Atlantis/blob/main/docs/tutorial/sphere-architecture.ja.md). Today this is a prompt-bound route through documents, PLI, `AGENTS.md`, and the Manifest. The standalone runner, resident daemon, and OAE persistence are not implemented.

For a friendly en-US doorway: a `Yokai Observer` keeps one personal taste experience, while a scoped `Ninja Runner` may someday carry the receipt. The folklore skin grants no secret authority and does not hide consent, provenance, safety, or unfinished engineering.

# Eat a potato first. 🥔

## Philosophy

Get the potatoes as a gift.

Build the chips yourself.

Eat the artifact.

Return the useful knowledge.

No job.  
Still eating chips.  
Still doing R&D.  
Not hoarding the result.

# Legally open-source potato chips. 🥔🌱

## README image compression

The JPEG files in `img/` are resized to a 1280-pixel maximum edge and re-encoded without Exif/GPS capture metadata. The repeatable maintenance tool is [`lib/compress_readme_images.py`](./lib/compress_readme_images.py):

```bash
python3 lib/compress_readme_images.py
```

It requires `ffmpeg` and replaces each source JPEG only after a successful conversion.

## License

This document and recipe are released under **CC BY 4.0 + Remix Declaration**.

Reuse, modification, redistribution, and commercial use are allowed. Keep attribution and state what you changed. See [`LICENSE`](./LICENSE).
