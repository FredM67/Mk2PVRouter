# Calibration, easy first; the single-phase pages on the new firmware

Status: design, for approval. Repo: Mk2PVRouter, branch from `dev`. Site texts in French.

## Intent

In « Logiciel & Étalonnage », each firmware has an « Étalonnage » page and a configurator page with
its own « Mode étalonnage ». A beginner who follows the steps lands on « Étalonnage » and meets the
hard way first: on the 3-phase page, 250 lines of manual methods (meter flashes, formula), the
configurator in one tip near the end. The user's words: "hard then easy, the user will die".

On `dev`, the single-phase pages are worse: « Étalonnage — Monophasé » and the installation pages
describe the old firmware `Mk2_fasterControl_Full` (calibration sketches `cal_CT1_v_meter.ino`,
`cal_CT2_v_CT1.ino`, `powerCal_grid`), while the configurator next to them is for the new firmware
`Mk2_1phase_RFdatalog_temp`. The user decided: the old firmware goes from the `dev` docs; even with
an old board, users migrate to the new firmware, which does everything and better.

## Goals

- **One calibration procedure per firmware, on its « Étalonnage » page, easy first:**
  1. what you need: a reference reading (Linky instantaneous power, plug-in wattmeter, clamp
     meter) and a strong resistive load;
  2. calibrating with the configurator's calibration mode, step by step;
  3. checking the result;
  4. going further: by hand (the formula, the meter-flash method), and why calibration matters.
- **The configurator pages** keep what is on screen in calibration mode (the fields, what the page
  computes and flags, loading `calibration.h`), and link to « Étalonnage » for the procedure. One
  procedure per firmware, not two.
- **Why calibrate, per router, said at the top of each page:**
  - 3-phase: **mandatory**. The router adds the three phases; one phase off throws the sum off.
  - Single-phase: **not needed for diversion through the triacs** (the router acts on the sign of the
    grid energy, a scale error does not change it), **needed for realistic values**: what the
    router shows and sends (display, serial, Home Assistant through mk2Wifi), and every setting in
    watts compared with measured power: **relay diversion thresholds** (surplus, import), CT2's
    anti-creep limit, the export offset. The user's words on relays: "we need realistic values
    there".
- **The single-phase pages describe only `Mk2_1phase_RFdatalog_temp`:**
  - « Étalonnage — Monophasé »: rewritten, same layout as the 3-phase page, the readings `P`, `V`
    and `diverted`, the values per board (old boards `f_powerCalOldBoard`,
    `f_powerCalDivertedOldBoard`, `f_voltageCalOldBoard`; new board `f_ctRating`,
    `f_ctRatingDiverted`, `f_powerCalPerAmp`, `f_voltageCalNewBoard`).
  - « Installation et tests — Monophasé » and the `config.h` walkthrough
    (`firmware-monophase.inc.rst`): the new firmware; the configurator is the recommended way to
    get `config.h`.
  - The other mentions of the old firmware: `carte-mere/choix-configuration.rst`,
    `common/installation-platformio.inc.rst`, `logiciel-etalonnage-monophase.rst`.
  - A short note for owners of the old firmware: migrate; link to "Upgrading from
    `Mk2_fasterControl_Full`" in the PVRouter-1-phase CHANGELOG.
  - In the single-phase « Prochaines étapes », calibration is recommended, no longer
    « OBLIGATOIRE ».

## Non-goals

- No change to the configurators or the firmware.
- No change to the stable documentation (`main`): it keeps describing the released firmware until
  `dev` is merged at a release.
- The other sections (hardware, final installation, mk2Wifi) are not reviewed, apart from the
  mentions of the old single-phase firmware listed above.

## Anti-goals

- A beginner who reads the formula before learning the configurator does it.
- Two procedures for the same firmware that can say different things.
- A single-phase user who skips calibration and then sets relay thresholds on wrong watts, because
  the page said "optional" without the relay caveat.
- A page on `dev` that still describes `Mk2_fasterControl_Full` as the firmware to use.

## Constraints

- French typography: U+00A0 before `: ; ! ?` and inside « ».
- The page labels stay (`etalonnage-monophase`, `etalonnage-triphase`, `configurateur-*`,
  `logiciel-*`): other pages link to them.
- The build stays without new warnings (the CI builds HTML and PDF).
- Facts come from the firmware repos at their `dev` head: `calibration.h`, `config.h`, the sketch
  Readmes ("Étalonnage du routeur" in `Mk2_1phase_RFdatalog_temp/Readme.md`) and the configurators.

## Approaches

1. **« Étalonnage » holds the single procedure, easy first; the configurator page keeps the screen
   and links there (chosen by the user).** It is the page the step lists already point to, and one
   procedure stays up to date.
2. A box at the top of today's « Étalonnage » pointing to the configurator. Quick, but the reader
   still bounces between two pages, and two procedures drift apart.
3. The procedure on the configurator page, « Étalonnage » as theory and a link. The step lists
   would land on a page without a procedure.

## Design

### « Étalonnage — Triphasé » (`firmware/etalonnage-triphase.rst`)

- Top: time, level, risk, prerequisites, as today; then « obligatoire » and why (the sum of the
  phases), in one short `important`.
- **Ce qu'il vous faut:** a reference reading per phase (wattmeter or clamp on the phase cable;
  the Linky display shows the total, usable with one load on one phase), a strong resistive load
  (water heater, radiator), the configurator.
- **Étalonner avec le configurateur:** from loading `calibration.h` (or typing its values) and the
  CT ratings on the universal board, to the readings `P1`/`P2`/`P3` (and `V1`...) against the
  reference, upload, « Nouvelles valeurs téléversées : nouvelle mesure », leaving calibration mode.
  The values per board (today's table) go here.
- **Vérifier:** what a calibrated router shows (router and reference within a few percent on each
  phase), the signs of a CT mounted backwards.
- **Pour aller plus loin:** the manual methods of today (meter flashes, meter display, external
  meter, finding `f_powerCal` the first time) and the formula, unchanged in substance; the
  three-phase water heater case.
- `common/etalonnage-intro.inc.rst` (included by both pages) is reworded or split so that its
  "Introduction" does not contradict the 3-phase "mandatory" (today it says the router diverts
  reliably without calibration), and its meter-flash "principe de base" moves to « Pour aller plus
  loin ».

### « Étalonnage — Monophasé » (`firmware/etalonnage-monophase.rst`)

- Same layout. Top: a green box: not needed for the triacs; needed for realistic values and as
  soon as relays divert (thresholds in watts), plus the anti-creep limit and the export offset.
- **Étalonner avec le configurateur:** `P` against the reference at the grid connection, `V`;
  with CT2, `diverted` (in W) with a resistive load wired through CT2 and running by other means,
  since calibration mode never switches a load. Old boards: the CT2 reading corrects
  `f_powerCalDivertedOldBoard`; new board: it corrects `f_ctRatingDiverted`.
- **Vérifier:** `P` negative on import means CT1 is backwards; `diverted` negative, CT2.
- **Pour aller plus loin:** by hand, `CALIBRATION_MODE` in `config.h` and the formula (from the
  sketch Readme); the CT1 filter of the old boards (`lpf_gainOldBoard`, `alphaOldBoard`) in one
  line, left as shipped.

### Configurator pages

- `configurateur-triphase.rst` and `configurateur-monophase.rst`, section « Étalonnage »: what calibration mode does to
  the page and to `config.h`, the fields, what the page flags, rewriting `calibration.h`; the
  procedure itself is a link to the « Étalonnage » page.

### Single-phase migration

- `logiciel-monophase.rst`: the firmware `Mk2_1phase_RFdatalog_temp`; the measurement test stays
  if it still applies to the new firmware, otherwise it uses the router's own serial output.
- `firmware-monophase.inc.rst`: the file tree and the settings of the new `config.h` (board,
  display, CT2, loads, relays...), short, pointing to the configurator and to the sketch Readme
  for the details, as `firmware-triphase.inc.rst` does for its firmware.
- The migration note: where the old firmware was named (installation page, section page).

## Settled after the builder check

- **Where the facts come from (answered).** Both configurators, calibration mode included, are on
  the firmware `dev` heads (PVRouter-1-phase#33, PVRouter-3-phase#253). The builder checks out
  `1-phase` and `3-phase` at their `dev` heads and writes the procedures from the configurators
  (their `cal.*` texts in `i18n.js`, the fields in `app.js`), `calibration.h`, `config.h` and the
  sketch Readmes.
- **Consistency sweep (my call).** Every statement on whether calibration is needed, for either
  router (step lists, intro pages, FAQ, `principe-fonctionnement.rst`, `index.rst`), is brought in
  line: mandatory for 3-phase; for single-phase, not needed for the triacs, needed for realistic
  values and relays.
- **Running a load through CT2 in calibration mode (my call, safety).** Calibration mode never
  switches a load, overrides included, so the load runs by other means: plugged in directly
  through a cable that passes through CT2 (the modified extension cable the old page describes),
  or switched by hand. The page uses the configurator's own wording and keeps a `danger` box: work
  on the cabling only with the power off at the panel.
- **The measurement test (my call).** Checked first, as an investigation step:
  `RawSamplesTool_2chan.ino` is still in PVRouter-1-phase (`dev/`, Robin's tools); if it is,
  the test stays; if not, the router's own serial output in calibration mode replaces it.
- **Acceptance (my call).** The CI build, HTML and PDF, with no new warning. Figures, downloads
  and labels that only the old-firmware text used are deleted; anything still referenced
  elsewhere stays.
- **The migration link (my call).** The dev documentation describes the dev firmware: the link
  goes to the CHANGELOG on PVRouter-1-phase `dev`, section "Upgrading from
  `Mk2_fasterControl_Full`" (`https://github.com/FredM67/PVRouter-1-phase/blob/dev/CHANGELOG.md`
  with its anchor). At the release, `dev` becomes `main` with the rest.

## Left to the builder

- The wording and how much of today's manual-method text survives in « Pour aller plus loin ».
- Whether `etalonnage-intro.inc.rst` is reworded or split per router.
- Whether the single-phase measurement test (`RawSamplesTool_2chan.ino`) still applies to the new
  firmware; if not, what replaces it.
- The exact list of old-firmware mentions, from a `git grep` at the start.
