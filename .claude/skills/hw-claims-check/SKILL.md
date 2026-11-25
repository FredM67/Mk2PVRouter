---
name: hw-claims-check
description: Use when writing, editing or reviewing any page of the Mk2PVRouter docs that states a hardware or firmware fact - a part reference or value, SMD or through-hole, fitted at the factory or soldered by the user, a pinout, net, jumper, test point, voltage, fuse rating, hole size, baud rate or config.h name - including troubleshooting entries, assembly steps and checklists.
---

# Hardware and firmware claims in the Mk2PVRouter docs

## Overview

Much of this documentation was once generated from general knowledge and was wrong in ways a
builder pays for: SMD parts in "check your joints" lists, a burden resistor "on the D13 pads",
fuses "in their holders", a "blown fuse means a short". Every fact in the docs must come from a
source that is actually authoritative for it, and a fact without such a source does not go into
the published text.

## Sources: what can answer what

| Kind of fact | Authoritative source | How |
|---|---|---|
| Ref, value, footprint, SMD/THT, DNP/in BOM, which net a pad is on | KiCad **as committed on `origin/main`** of PVRouter-KiCad | `python scripts/kicad_parts.py <kicad repo> <board> REF...` |
| What a firmware does: baud rate, serial format, pins, `config.h` names, messages | Firmware source on `dev` (PVRouter-3-phase, PVRouter-1-phase) | grep the code, cite file:line |
| Factory-fitted vs user-soldered, kit contents, supplied part values, enclosure, holes, torque, procedures | **The maintainer only** | see [maintainer-facts.md](maintainer-facts.md); otherwise ask |
| Electrical behaviour of a part (ratings, tolerances) | The part's datasheet, if you can open it | otherwise leave the figure out |

**Not sources:** existing doc pages (including the one you are editing), the KiCad `Readme.md`,
the 1-phase/3-phase Readmes for hardware, your general knowledge of "typical" kits. They are
claims to verify, never evidence. When one disagrees with KiCad or the firmware, KiCad and the
firmware win, and the disagreement is worth reporting.

**Read the committed design.** The maintainer's checkout of PVRouter-KiCad often holds
uncommitted work in progress; the scripts read `origin/main` through `git show` by default.
Run `git -C <kicad repo> fetch` first if it may be stale. `<kicad repo>` is a checkout of
PVRouter-KiCad, or this repo's `hardware` submodule after `git submodule update --init hardware`
(never commit a submodule pointer). The maintainer's uncommitted changes are
the coming production board (see maintainer-facts.md): when the docs disagree with `origin/main`,
run the same query with `--worktree` before calling the docs wrong, and say which version you checked.

## The rule for every claim

For each technical statement you write or keep, you can name its source from the table above.
If you cannot:

- the statement does **not** go into the RST, not even with "à vérifier", "typiquement" or a
  plausible figure;
- write the page without it, and list it under "questions for the maintainer" in your reply.

A side note saying "unverified" does not make it acceptable to publish the claim.

## Reading KiCad correctly

- **Pad kind** decides who solders it: `smd` parts are factory-soldered, `tht` parts are usually
  the builder's; `smd+tht` is a mixed footprint (D13/D23/D33: SMD TVS plus two holes for the
  axial burden; R16/R26/R36: SMD or THT resistor). Exception: GDT0–GDT3 are SMD, in the BOM, yet
  optional and user-soldered (maintainer).
- **"NOT ON THIS BOARD"** means the part exists only in the schematic (R18/R28/R38): describe
  where it goes, never "solder Rxx" as if it had pads with its name.
- **Nets give the configuration.** Index 0 is the neutral, 1–3 are L1–L3 (FS0/RV0/GDT0 on
  NEUTRAL, FS1/RV1/GDT1 on L1…). CT1–CT3 measure L1–L3. Check with the pad nets before saying
  which parts a configuration needs; do not invent configurations (no "biphasé", no split-phase).
- **List a function's parts from KiCad, not from memory or from the question's wording.** For
  "the surge protection" or "the CT inputs", query the nets: `--net NEUTRAL --net L1_VOLTAGE
  --net Earth` gives every fuse, varistor (GM1–GM3 between phase and neutral, always fitted),
  RV/GDT pair, C1 and FL1; `--net "Net-(CT1-Pin_1)"` gives the CT1 chain. A part you forget is
  as wrong as a part you invent.
- **Optional is optional.** RVx + GDTx pairs are optional, for full lightning protection: never
  list them as required.
- Silkscreen names differ from refs: say both when it helps (JP8 « UART_EXT », J0 « FTDI »,
  GND_LINK1 « GND_LINK », TP41 « +3.3V » is the regulator output, TP3 « VCC » is the selected supply).

## Before you hand the change over

1. Run `python scripts/refcheck.py content <kicad repo> <changed .rst files>` and read every
   `MISSING`, `VALUE?` and `SMD-SOLDER` line. Phase names (L1–L3) and Arduino pins (D2–D13)
   match the ref pattern: ignore those lines. An SMD part on a line about soldering is wrong
   unless it is one of the maintainer's exceptions.
2. Re-read every number you wrote (V, A, Ω, mm, baud, cycles) and point at its source.
3. In your reply, give the source of each new or changed fact in one line, and the open
   questions for the maintainer.

## Red flags - stop and check

| Thought | Reality |
|---|---|
| "The cavaliers page already says it" | The docs are not a source. Check KiCad. |
| "115200 baud is the usual rate" | This firmware runs at 9600 (`serial_output.h`). Grep, don't assume. |
| "It's SMD, so it's factory-fitted" | Usually; GDT0–GDT3 are the exception. |
| "I'll mark it 'à vérifier' and move on" | Unverified facts stay out of the RST. |
| "The user is waiting, it's only a troubleshooting tip" | A wrong tip costs a builder a board. Same rule. |
| "The KiCad Readme lists it" | The Readme has been wrong before. Read the PCB. |
| "The file on disk is the design" | Uncommitted work. Read `origin/main`. |
