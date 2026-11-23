# Calibration path, easy first, and the single-phase pages on the new firmware — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** each « Étalonnage » page holds its firmware's one calibration procedure, configurator first,
and the single-phase pages on `dev` describe only `Mk2_1phase_RFdatalog_temp`.

**Architecture:** reStructuredText pages under `content/`, built by Sphinx (HTML and PDF in CI).
Structure rules are pinned by pytest tests in `tests/test_calibration_docs.py`, which read the `.rst`
sources (CI already runs `python -m pytest tests -q`).

**Tech Stack:** Sphinx 9 (`sphinx_rtd_theme`, `autosectionlabel` with document prefix, depth 2),
reStructuredText in French, pytest.

**Spec:** `docs/superpowers/specs/2026-11-23-calibration-path-design.md`

## Global Constraints

- Site texts in French: U+00A0 before `: ; ! ?` and inside « ». Write the files with a script that
  converts ` :`, ` ;`, ` !`, ` ?` followed by a space or line end, and `« `/` »` (never touch
  `:ref:`, `.. note::` and the like); keep each file's line endings (most are CRLF).
- Labels stay: `etalonnage-monophase`, `etalonnage-triphase`, `configurateur-monophase`,
  `configurateur-triphase`, `logiciel-monophase`, `logiciel-triphase`,
  `logiciel-etalonnage-monophase`, `logiciel-etalonnage-triphase`.
- Calibration pages, section titles, in this order: « Ce qu’il vous faut », « Étalonner avec le
  configurateur », « Vérifier », « Pour aller plus loin ».
- 3-phase: calibration **obligatoire**. Single-phase: not needed for diversion through the triacs;
  needed for realistic values (display, serial, Home Assistant) and for every setting in watts:
  **relay thresholds** (surplus, import), CT2's anti-creep limit, the export offset.
- Facts from the firmware `dev` heads only: check out `1-phase` and `3-phase` at `origin/dev`
  before writing (configurators `configurator/i18n.js` `cal.*` texts and `app.js`,
  `calibration.h`, `config.h`, `Mk2_1phase_RFdatalog_temp/Readme.md` « Étalonnage du routeur »).
  Never commit the submodule pointers.
- Calibration mode never switches a load, overrides included: a CT2 reading needs a resistive load
  plugged in directly through a cable passing through CT2, or switched by hand; a `danger` box:
  cabling only with the power off at the panel.
- Migration link: `https://github.com/FredM67/PVRouter-1-phase/blob/dev/CHANGELOG.md`, section
  "Upgrading from `Mk2_fasterControl_Full`" (use GitHub's anchor of that heading).
- No new Sphinx warning, HTML and PDF. Figures, downloads and labels used only by removed text are
  deleted.
- Commits end with `Co-Authored-By: Claude <noreply@anthropic.com>`.

## Review Focus

1. **Safety of the CT2 reading.** A reader running a load through CT2 in calibration mode must see
   how (plugged directly, by hand) and the `danger` box before touching cables. Owner: Task 2
   (test `test_mono_ct2_reading_is_safe`).
2. **The Linky reading on 3-phase.** The Linky shows the total of the phases: the page must say it
   works only with one load on one phase, otherwise a per-phase meter. Owner: Task 1 (test
   `test_tri_linky_is_total`).
3. **The relay caveat at the top of the single-phase page,** not buried: a reader who stops at the
   first box must know relays need calibration. Owner: Task 2 (test `test_mono_top_box_has_relays`).
4. **Broken links after renaming headings or deleting text** (`autosectionlabel`, `:ref:`,
   `:download:`). Owner: Task 5 (build check: no `undefined label`, `unknown document`,
   `toctree`, `not readable` warning added).
5. **A step list or intro that still says the opposite** (single-phase « OBLIGATOIRE », shared intro
   "reliable without calibration" on the 3-phase page). Owner: Tasks 1, 4 and 5 (tests
   `test_shared_intro_no_contradiction`, `test_mono_steps_not_mandatory`).

---

### Task 1: « Étalonnage — Triphasé », configurator first

**Files:**
- Modify: `content/firmware/etalonnage-triphase.rst`, `content/common/etalonnage-intro.inc.rst`.
- Create: `tests/test_calibration_docs.py`.

**Interfaces:**
- Produces: in `tests/test_calibration_docs.py`, `read(path: str) -> str` (UTF-8, relative to
  `content/`) and `section_order(text: str) -> list[str]` (the titles underlined with `-`, in
  order). Later tasks add their tests to this file.
- Produces: the shared intro, either reworded for both routers or split (builder's call). If split,
  name the parts `common/etalonnage-pourquoi-*.inc.rst`; the 3-phase page must not include text
  saying the router diverts reliably without calibration.

- [ ] **Step 1: Write the failing tests.**
  - `test_tri_section_order`: `section_order(read('firmware/etalonnage-triphase.rst'))` contains the
    four titles of the Global Constraints in that order (other sections may sit between or before).
  - `test_tri_mandatory_first`: « obligatoire » appears before « Ce qu’il vous faut ».
  - `test_tri_configurator_before_formula`: the first `:ref:` to `configurateur-triphase` comes
    before the first `f_powerCal` formula (« × appareil / routeur » or « valeur actuelle × »).
  - `test_tri_linky_is_total`: in « Ce qu’il vous faut », `Linky` and « une seule phase » (or « une
    phase ») are both present.
  - `test_shared_intro_no_contradiction`: the text the 3-phase page includes (follow its
    `.. include::` lines) has no « sans nécessiter d'étalonnage ».
- [ ] **Step 2: Run them and check they fail.** Run `python -m pytest tests/test_calibration_docs.py -q`.
  Expected: 5 failures.
- [ ] **Step 3: Rewrite the page** as the spec's « Étalonnage — Triphasé » section says: today's
  values-per-board table moves into « Étalonner avec le configurateur »; today's manual methods
  (meter flashes, meter display, external meter, finding `f_powerCal`, the three-phase water heater)
  move under « Pour aller plus loin », unchanged in substance; the configurator's steps come from
  `3-phase/configurator` at `dev`.
- [ ] **Step 4: Run the tests and the build.** `python -m pytest tests -q`: PASS. Then the build
  check of Task 5, Step 2. Expected: no warning added.
- [ ] **Step 5: Commit** `docs: 3-phase calibration, configurator first, manual methods last`.

### Task 2: « Étalonnage — Monophasé » for the new firmware

**Files:**
- Modify: `content/firmware/etalonnage-monophase.rst` (rewritten).
- Test: `tests/test_calibration_docs.py`.

**Interfaces:**
- Consumes: `read`, `section_order`, and the shared intro of Task 1.

- [ ] **Step 1: Write the failing tests.**
  - `test_mono_section_order`: the four titles, in order.
  - `test_mono_top_box_has_relays`: the first admonition of the page (`.. tip::`, `.. note::` or
    `.. admonition::`) mentions « relais » and « triac ».
  - `test_mono_readings_and_values`: the page has the readings `` ``P`` ``, `` ``V`` ``,
    `` ``diverted`` `` and the names `f_powerCalOldBoard`, `f_powerCalDivertedOldBoard`,
    `f_voltageCalOldBoard`, `f_ctRating`, `f_ctRatingDiverted`, `f_powerCalPerAmp`,
    `f_voltageCalNewBoard`.
  - `test_mono_ct2_reading_is_safe`: a `.. danger::` comes before the first mention of the CT2
    reading's load, and « calibration » mode text says no load is switched.
  - `test_mono_no_old_firmware`: none of `cal_CT1_v_meter`, `cal_CT2_v_CT1`, `powerCal_grid`,
    `powerCal_diverted`, `Mk2_fasterControl_Full` in the page.
- [ ] **Step 2: Run them and check they fail.** Expected: 5 failures.
- [ ] **Step 3: Write the page** as the spec's « Étalonnage — Monophasé » section says. CT2: old
  boards correct `f_powerCalDivertedOldBoard`, the new board corrects `f_ctRatingDiverted`.
  « Vérifier »: `P` negative on import means CT1 backwards, `diverted` negative means CT2.
  « Pour aller plus loin »: `CALIBRATION_MODE` and the formula by hand; the old boards' CT1 filter
  (`lpf_gainOldBoard`, `alphaOldBoard`) in one line. Time and level at the top: 30–45 min,
  « Intermédiaire ».
- [ ] **Step 4: Run the tests and the build** (Task 5, Step 2). Expected: PASS, no warning added.
- [ ] **Step 5: Commit** `docs: single-phase calibration on the new firmware, configurator first`.

### Task 3: Configurator pages point to « Étalonnage »

**Files:**
- Modify: `content/firmware/configurateur-triphase.rst`, `content/firmware/configurateur-monophase.rst`.
- Test: `tests/test_calibration_docs.py`.

- [ ] **Step 1: Write the failing tests.**
  - `test_configurator_calibration_points_to_page[tri|mono]`: the configurator page's
    « Étalonnage » section has a `:ref:` to `etalonnage-<router>` and no enumerated list (`#.` or
    `1.` lines).
- [ ] **Step 2: Run them and check they fail.** Expected: 2 failures.
- [ ] **Step 3: Rewrite both « Étalonnage » sections**: what calibration mode does to the page and
  to `config.h`, the fields, what the page flags, loading and rewriting `calibration.h`; one line
  « La marche à suivre, pas à pas : :ref:`etalonnage-<router>` ».
- [ ] **Step 4: Run the tests and the build** (Task 5, Step 2). Expected: PASS, no warning added.
- [ ] **Step 5: Commit** `docs: the configurator pages describe calibration mode, the procedure is on Étalonnage`.

### Task 4: Single-phase pages on `Mk2_1phase_RFdatalog_temp`

**Files:**
- Modify: `content/firmware/logiciel-monophase.rst`, `content/firmware/firmware-monophase.inc.rst`,
  `content/firmware/logiciel-etalonnage-monophase.rst`, `content/carte-mere/choix-configuration.rst`,
  `content/common/installation-platformio.inc.rst`.
- Create: `content/common/ancien-firmware-monophase.inc.rst` (the migration note).
- Test: `tests/test_calibration_docs.py`.

- [ ] **Step 1: Investigate.** Is `RawSamplesTool_2chan.ino` in PVRouter-1-phase `dev`
  (`1-phase/dev/` or `1-phase/Robin/`)? If yes, the measurement test of `logiciel-monophase.rst`
  stays, with its new path; if not, it is replaced by the router's own serial output in calibration
  mode. Note the answer in the commit message.
- [ ] **Step 2: Write the failing tests.**
  - `test_no_old_firmware_anywhere`: in every `.rst` under `content/` except
    `common/ancien-firmware-monophase.inc.rst`, none of `Mk2_fasterControl_Full`, `cal_CT1_v_meter`,
    `cal_CT2_v_CT1`, `powerCal_grid`, `powerCal_diverted`, `OLD_PCB`, `physicalPin_dump_load`,
    `forcePin`, `dumpLoad_startup_sequence`, `TEMP_ENABLED`, `sensor_list`.
  - `test_mono_install_names_new_firmware`: `logiciel-monophase.rst` and
    `firmware-monophase.inc.rst` name `Mk2_1phase_RFdatalog_temp`; `logiciel-monophase.rst`
    includes the migration note and links `configurateur-monophase`.
  - `test_mono_steps_not_mandatory`: `logiciel-monophase.rst` has no « OBLIGATOIRE » next to
    « Étalonnage », and its calibration step mentions « relais ».
- [ ] **Step 3: Rewrite.**
  - `firmware-monophase.inc.rst`: the file tree and settings of the new `config.h` (board, display,
    CT2, loads, relays, temperature, dual tariff, RF), short, pointing to the configurator and to the
    sketch Readme, in the manner of `firmware-triphase.inc.rst`.
  - `logiciel-monophase.rst`: firmware `Mk2_1phase_RFdatalog_temp`; the « Prochaines étapes »
    calibration step: recommended, needed with relays.
  - The migration note: the old firmware is no longer described; old boards run the new firmware
    (`PCB_VERSION` `OLD_SEG` or `OLD_OLED`); calibration values carry over; link to the CHANGELOG
    section (Global Constraints).
  - `logiciel-etalonnage-monophase.rst`, `choix-configuration.rst`, `installation-platformio.inc.rst`:
    the new firmware's name and path.
- [ ] **Step 4: Run the tests and the build** (Task 5, Step 2). Expected: PASS, no warning added.
- [ ] **Step 5: Commit** `docs: the single-phase pages describe Mk2_1phase_RFdatalog_temp`.

### Task 5: Consistency sweep and build check

**Files:**
- Modify, where a sentence says whether calibration is needed: `content/index.rst`,
  `content/introduction.rst`, `content/principe-fonctionnement.rst`,
  `content/firmware/logiciel-etalonnage-triphase.rst`, `content/firmware/logiciel-triphase.rst`,
  `content/troubleshooting-mk2wifi.rst`, and any other file a
  `git grep -n -i "étalonn" -- content` shows with such a sentence.

- [ ] **Step 1: Sweep.** Each statement says: 3-phase mandatory; single-phase not needed for the
  triacs, needed for realistic values and relays. List the files changed in the commit message.
- [ ] **Step 1b: Orphans.** Figures and downloads that only the removed text used (look for files under
  `content/` no longer referenced by any `.rst`, among those the old pages pointed to): delete them.
- [ ] **Step 2: Build check.** With `1-phase` and `3-phase` at `origin/dev`, run
  `sphinx-build -b dirhtml content _build/dirhtml 2>&1 | tee build.log` (WSL venv `~/.venvs/mk2docs`,
  drawio stub on `PATH` locally). Compare with the same build on `origin/dev`
  (`git stash` is forbidden: use a second worktree). Expected: no added line matching
  `undefined label|unknown document|toctree|not readable|duplicate label|WARNING: .*etalonnage`.
- [ ] **Step 3: Run the tests.** `python -m pytest tests -q`. Expected: PASS.
- [ ] **Step 4: Commit** `docs: what calibration is for, said the same way everywhere`.
- [ ] **Step 5: Push and check CI**: the HTML and PDF steps of the run show no warning or error
  absent from the latest `dev` run.
