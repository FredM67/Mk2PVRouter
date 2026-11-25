# Facts confirmed by the maintainer

These cannot be read from KiCad or the firmware. Use them as a source; anything about the kit,
the factory or the enclosure that is not here must be asked. Add a line (with the date) when the
maintainer confirms something new.

## Mainboard

- The maintainer's uncommitted KiCad changes are the coming production version (2026-11): e.g.
  JP0 « V sel. » pad 1 = U1 output, pad 3 = +5V, factory bridge 1–centre (`--worktree`), while
  `origin/main` still has pad 1 = +5V. When the docs and `origin/main` disagree, compare with
  `--worktree` before calling the docs wrong, and say which version you checked.

- GDT0–GDT3 are optional and soldered by the user, always in pairs with RV0–RV3, for full
  lightning protection (2026-11). In KiCad they are SMD, in the BOM, not DNP.
- A board running on 5 V (V sel. cut on one side, soldered on the other) can never take an RF
  module; this is checked when the order is placed (2026-11).
- GM1–GM3 (IsoMOV, MOV + GDT in one package, phase to neutral) are the basic protection, never
  optional. They are hard to find in small quantities: depending on supply, plain varistors are
  delivered for the GM positions instead. Only the GDTx + RVx pairs are optional (2026-11).
- Which GDT (and RV) positions a configuration uses: single-phase N and L1 (GDT0, GDT1);
  three-phase with neutral all four; 3×230 V without neutral N, L1 and L2 (GDT0–GDT2), the
  router's N terminal taking one of the phases (2026-11).
- Fuses FS0–FS3 are soldered directly, no holder. The supplied rating varies with what can be
  sourced: 0.75 A, 1 A or 1.25 A, 250 V. Docs say "same rating and type as the original, as marked
  on the fuse" (2026-11).
- CT2 is usable in single-phase, optional, to measure the diverted power (single-phase
  firmware); CT3 is not available in single-phase when JP2 routes A5 to I2C SCL (KiCad PR #1,
  2026-11). The schematic's "Monophasé/Triphasé" fields predate this.
- A blown fuse is the fuse doing its job on a fault; do not write "a blown fuse means a short".
- The ATmega328P only needs one of the two firmwares uploaded; the number of connectors supplied
  depends on the order (2026-11).
- GND_LINK: when to close it is not settled; keep "open by default, see the jumpers page".
- High-current joints are soldered at about 450 °C (confirmed).
- Every THT part is soldered by the user (C1, FL1, GM1–GM3, PS1, PWR1, fuses…); IC1 sits in a
  socket and comes ready for a firmware upload (bootloader in place) (2026-11).
- JP1 « SDA » / JP2 « SCL » are open: the user solders 1–centre (L3 measurement) or 3–centre
  (I2C). JP3 « IRQ » and JP41 « NSS » are open by default (2026-11).
- Usual tolerances are fine for test points (3.3 V ±0.1 V, 5 V ±0.2 V, VREF 1.0–1.2 V) (2026-11).
- Router consumption: at most 10 W, the rating of PS1; do not write a lower figure (2026-11).
- A faulty SMD part: contact support, some can be repaired; never "replace the board" (2026-11).
- Soldering: 350 °C for normal joints, 450 °C for heavy parts; fuse pins briefly (a fuse melts)
  (2026-11). A 30 mA RCD is general electrical practice, fine to state (2026-11).
- The mainboard schematic note "R16-R26-R36 only for Current Output CTs (old variant)" is a typo
  for R18-R28-R38 (current-output CT burden, in the D13/D23/D33 holes). R16/R26/R36 are the
  ZMPT101K burden. Do not follow the note's refs (2026-11).

## Output stage and loads

- J1 of the output stage is rated 20 A or more (the KiCad footprint is for PCB manufacture);
  keep "no more than 3 kW per output" (2026-11).
- Relay boards are standard opto-isolated relay boards driving a heavy-duty contactor
  (e.g. Hager ETC225).
- If the off-peak boost is not driven by the router, the off-peak contactor is wired in parallel
  with the output stage; the thermostat stays in series (2026-11).
- MOC part supplied with the BTA41-800B: open question, waiting for the maintainer.
- Triac supplied: BTA41-600B or BTA41-800B; the 800 V part is needed for a delta-wired water
  heater (2026-11).
- CT arrows: grid CT towards the house, diversion CT towards the load (2026-11).
- Diversion CT: closed toroid inside the box on old boards; on the universal board a clip-on CT
  (333 mV variants still being researched) (2026-11).
- Three-phase loads: delta (no neutral by definition) 2 triacs; star with virtual neutral
  2 triacs; star with the neutral connected 3 triacs (2026-11).

## Enclosure and assembly

- Heatsink: the centre screw is the triac's; the earth wire has a crimped ring terminal under one
  of the two screws holding the heatsink to the enclosure.
- Triac insulator: silicone pad or mica, both fine (the BTA41 tab is insulated).
- Indicator LED sits in a holder screwed on the lid: 8 mm hole (confirmed 2026-11).
- Reset push-button (supplied in the 3-phase kit): 13 mm hole.
- OLED: cut-out in the lid or a remote display, the user's choice.
- Only M3 screws and nuts; M4 is no longer used (2026-11).
- Torque: leave "couple indiqué par le fabricant" as is.
- Heatsink fixing: M3 screws, holes drilled 3.5 mm for some room; no 4 mm step. The other hole
  sizes in percages.rst are correct (2026-11).
- Cable lengths in confection-cables.rst were measured by the maintainer (2026-11).
- Heatsink statements in troubleshooting (paste, vertical, outside the box, no vents, 3 kW) are
  fine (2026-11).
- Earth wires: one per heatsink (2026-11).

## Programming and mk2Wifi

- Kit FTDI adapter: male pins and a USB connector; it does not power the board.
- PlatformIO is the recommended way, the Arduino IDE the simplest; both must keep working.
- mk2Wifi (ESP32-C6, not C3): first flash over USB, then OTA. The USB cable must NOT be connected
  while the module is plugged on the mainboard. Whether the C6 flashes without holding Boot:
  open question.
- Split-phase is not supported. 3×230 V without neutral is documented for the hardware (router N
  terminal on one phase, CT1 and CT2, GDT0–GDT2); the firmware has no mode for it (2026-11).
