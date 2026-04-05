# Copilot Instructions — Mk2PVRouter Documentation

## What this repo is

A **Sphinx documentation project** (French language) for the Mk2PVRouter — a DIY solar PV router based on the universal **3phaseDiverter** board. The firmware and hardware design live in git submodules (`1-phase/`, `3-phase/`, `hardware/`) that are **read-only** here; don't modify them.

## Build commands

```bash
# Install Python dependencies
pip install -r requirements.txt

# Build HTML (primary target)
make html

# Build PDF
make simplepdf

# Build dirhtml (used by CI/GitHub Pages)
make dirhtml

# Copy hardware renders from submodules into content/img/
make copy-assets

# Check for warnings/errors
make html 2>&1 | grep -E "(WARNING|ERROR|CRITICAL)"

# Check specifically for heading hierarchy errors
make html 2>&1 | grep -i "title level inconsistent"
```

Output: `_build/html/` (HTML), `_build/simplepdf/` (PDF).  
Source root: `content/`, Sphinx config: `content/conf.py`.

## Architecture

```
content/
├── conf.py                  # Sphinx config; all extensions configured here
├── index.rst                # TOC root — all pages must be referenced here
├── common/                  # Shared include snippets (*.inc.rst) — included by other files
├── firmware/                # Firmware-specific include snippets + test guide
├── carte-mere/              # Universal motherboard assembly chapters
├── etage-sortie/            # Output stage board chapters
├── mk2wifi/                 # ESP32 wifi module chapters
├── boitier/                 # Case & cabling chapters
├── drawio/                  # DrawIO diagram sources (.drawio) — auto-converted at build time
├── img/                     # Static images + hardware renders (copied by make copy-assets)
└── _static/                 # CSS/JS assets for HTML/PDF output
```

**Include file pattern**: Shared procedures live in `content/common/*.inc.rst` and `content/firmware/*.inc.rst`. They are pulled into pages with:
```rst
.. include:: ../common/filename.inc.rst
```
Include files are **excluded from the TOC** via `conf.py` (`**/*inc.rst` in `exclude_patterns`). Add new shared content as `.inc.rst` files; standalone pages as `.rst` files listed in `index.rst`.

**Hardware renders**: PCB images are NOT committed directly. They are copied from `hardware/` submodule at build time via `make copy-assets` (see Makefile). The images in `content/img/mainboard-*.png`, `mk2wifi-*.png`, `indicator-*.png` are build artifacts.

**Autosectionlabel**: `autosectionlabel_prefix_document = True` is set. Cross-references must use the format `:ref:`filename:Section Title`` for sections below depth 2.

## Key conventions

### RST heading hierarchy (strict — must not deviate)

```rst
Document Title       =====   (level 1)
Major Section        -----   (level 2)
Subsection           ~~~~~   (level 3)
Sub-subsection       ^^^^^   (level 4)
Paragraph            """""   (level 5)
Sub-paragraph        '''''   (level 6)
```

Do **not** skip levels. Sphinx will error with "Title level inconsistent" if you do.

### French typography

- **Non-breaking space** (U+00A0) before `:`, `;`, `!`, `?`, and between numbers and units (`3 kW`, `230 V`)
- **Guillemets**: `« texte »` (not `"texte"`)
- **Typographic apostrophe**: `'` (U+2019), not `'`
- **Decimal separator**: comma (`3,5 heures`), not period

### Cross-references and glossary

```rst
:ref:`safety-overview`          ← section cross-reference
:ref:`etalonnage`
:term:`CT`                      ← glossary term link
:term:`triac`
```

All technical terms used should be defined in `content/glossary.rst` and linked on first use.

### Safety directives (use the right level)

| Directive       | Use for                                              |
|-----------------|------------------------------------------------------|
| `.. danger::`   | Physical hazards (electric shock, fire, burns)       |
| `.. warning::`  | Mistakes that could damage hardware or software      |
| `.. important::`| Critical info with no physical hazard                |
| `.. note::`     | Clarifications, general info                         |
| `.. tip::`      | Best practices, helpful suggestions                  |

Reserve `.. danger::` strictly for physical safety — overuse causes "warning fatigue".

### New section checklist

When adding a new assembly page:
1. Create `content/<subdirectory>/filename.rst`
2. Add it to the relevant `toctree` in `content/index.rst`
3. Add a time estimate, difficulty level, and prerequisites `admonition` at the top
4. Add verification checkpoint `admonition` blocks after major steps
5. Link terms to glossary, link related pages with `:ref:`

### CI / deployment

- GitHub Actions (`.github/workflows/documentation.yaml`) builds on every push/PR, **except** changes to `1-phase/`, `3-phase/`, `hardware/`, or `.gitmodules`
- Deploys to GitHub Pages from `main` and `legacy` branches
- Also deployed on ReadTheDocs (config: `.readthedocs.yaml`)
- Both require DrawIO installed for diagram rendering
