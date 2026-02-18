# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Sphinx documentation repository** for the **Mk2PVRouter** project - a DIY solar PV router for optimizing self-consumption of solar energy. The documentation is written entirely in **French** and covers assembly, installation, calibration, and troubleshooting of electronic kits for both single-phase (monophasé) and three-phase (triphasé) systems.

The actual firmware code is maintained in separate repositories linked as git submodules:
- `1-phase/`: https://github.com/FredM67/PVRouter-1-phase
- `3-phase/`: https://github.com/FredM67/PVRouter-3-phase

### Firmware Structure

Both firmware repositories contain:
- **Main firmware**: Arduino sketches (.ino files) targeting ATmega328P microcontroller
- **PlatformIO support**: `platformio.ini` files for modern build system
- **Development tools**: Calibration programs, test utilities in `dev/` subfolder
- **Doxygen documentation**: Generated API documentation (see GitHub Pages)

**1-phase firmware variants:**
- `Mk2_fasterControl_Full/` - Main firmware with all features (display, temperature sensor, telemetry)
- `Mk2_fasterControl_twoLoads_temp_1/` - Two-load variant
- `Mk2_fasterControl_threeLoads_temp_1/` - Three-load variant
- `Robin/` - Original Robin Emley implementation

**3-phase firmware:**
- `Mk2_3phase_RFdatalog_temp/` - Main three-phase firmware with RF logging and temperature support
- `dev/cal_CTx_v_meter/` - CT sensor calibration tool (critical for accurate power measurement)

## Common Development Commands

### Building Documentation

```bash
# Build HTML documentation (default)
make html

# Build PDF documentation
make simplepdf

# View all available Sphinx build targets
make help

# Clean build artifacts
make clean

# Manually export DrawIO diagrams to PDF (if needed)
./build_pdf_from_drawio.sh
```

Built documentation is output to `_build/html/` (HTML) or `_build/simplepdf/` (PDF).

**Note**: DrawIO diagrams in `content/drawio/*.drawio` are automatically converted during the Sphinx build process via the `sphinxcontrib.drawio` extension. The `build_pdf_from_drawio.sh` script is for manual export only.

### Viewing Built Documentation

```bash
# Open the main index page (macOS)
open _build/html/index.html

# Linux
xdg-open _build/html/index.html
```

### Installing Dependencies

```bash
# Install Python dependencies for building documentation
pip install -r requirements.txt
```

Key dependencies: Sphinx 8.2.3+, sphinx_rtd_theme, sphinxcontrib-drawio (for diagram support), sphinx-copybutton, sphinx-simplepdf.

### VSCode Tasks

The repository includes `.vscode/tasks.json` with pre-configured tasks:
- **build**: Run `make html`
- **build PDF**: Run `make simplepdf`
- **open page**: Open built HTML index

### Checking Build Quality

```bash
# Check for build warnings and errors
make html 2>&1 | grep -E "(WARNING|ERROR|CRITICAL)"

# Check for title level inconsistencies specifically
make html 2>&1 | grep -i "title level inconsistent"

# Count total warnings
make html 2>&1 | grep WARNING | wc -l
```

The goal is to keep warnings to a minimum (currently ~11 warnings is baseline).

## High-Level Architecture

### Content Organization

Documentation source files are in `content/` with this structure:

```
content/
├── conf.py                    # Sphinx configuration
├── index.rst                  # Main documentation entry point
├── introduction.rst           # General introduction
├── principe-fonctionnement.rst
├── burst-fire-control.rst
├── safety-overview.rst        # Unified safety chapter (CRITICAL - must be read first)
├── installation-logiciel.rst  # Software installation guide
├── installation-finale.rst    # Final electrical installation (high voltage)
├── troubleshooting.rst        # Comprehensive troubleshooting guide
├── glossary.rst              # Technical terms glossary
├── soldering-tutorial.rst    # Beginner soldering guide
├── common/                   # Shared content for both mono and tri versions
│   ├── *.inc.rst            # Include files (assembly, calibration, testing)
│   └── ...
├── mono/                     # Single-phase specific content
│   ├── carte-mere-mono.rst
│   ├── etalonnage-mono.rst
│   └── ...
└── tri/                      # Three-phase specific content
    ├── carte-mere-tri.rst
    ├── etalonnage-tri.rst
    └── ...
```

### Include File Pattern

To minimize duplication, shared procedures are extracted into **include files** (`.inc.rst`) in `content/common/`:

- `ordre-soudure.inc.rst` - Soldering order recommendations
- `carte-sortie.inc.rst` - Output board assembly (36KB, most detailed)
- `percages.inc.rst` - Drilling procedures
- `connexion-ftdi.inc.rst` - FTDI connection for programming
- `installation-arduino-ide.inc.rst` - Arduino IDE setup
- `installation-platformio.inc.rst` - PlatformIO alternative
- `compilation-televerement.inc.rst` - Firmware compilation and upload
- `moniteur-serie.inc.rst` - Serial monitor usage
- `resolution-problemes-upload.inc.rst` - Upload troubleshooting

These are included in version-specific files using:
```rst
.. include:: ../common/filename.inc.rst
```

### Documentation Structure Philosophy

The documentation follows a **progressive assembly workflow**:

1. **Safety chapter** (`safety-overview.rst`) - MUST be read first
2. **Introduction** - Overview, tools, time estimates, skill levels
3. **Theory** - How the router works (principle, burst-fire control)
4. **Software setup** - Arduino IDE or PlatformIO installation
5. **Assembly** - Step-by-step soldering (motherboard → output boards)
6. **Drilling** - Case and heatsink preparation
7. **Assembly** - Mounting components in case
8. **Calibration** - CT sensor calibration
9. **Final installation** - Connection to mains electrical system
10. **Troubleshooting** - Diagnosis and problem resolution

Each major assembly section includes:
- **Time estimates** (beginner vs. experienced)
- **Skill level indicators** (difficulty rating)
- **Prerequisites boxes** (checklist before starting)
- **Verification checkpoints** (checklist after each major step)
- **Safety warnings** (using RST `.. danger::` directive)

### RST Section Level Conventions

The project uses a consistent RST heading hierarchy (see `RST_SECTION_LEVELS.md`):

```rst
Document Title (Level 1)
=========================

Major Section (Level 2)
-----------------------

Subsection (Level 3)
~~~~~~~~~~~~~~~~~~~~

Sub-subsection (Level 4)
^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph (Level 5)
"""""""""""""""""""

Sub-paragraph (Level 6)
'''''''''''''''''''''''
```

**IMPORTANT**: Always maintain this hierarchy. Sphinx will error on "Title level inconsistent" if you skip levels or use inconsistent characters.

### Glossary and Cross-References

Technical terms are defined in `content/glossary.rst` and should be linked using:
```rst
:term:`PCB`
:term:`CT`
:term:`triac`
```

Cross-references between sections use:
```rst
:ref:`safety-overview`
:ref:`etalonnage-mono`
```

### French Language Conventions

The documentation is written in **French** with proper French typography:

1. **Non-breaking spaces** (U+00A0 ` `) before:
   - Punctuation: `!`, `?`, `;`, `:`
   - Units: `3 kW`, `230 V`, `50 Hz`
   - Guillemets: `« texte »`

2. **Typographic apostrophes** (U+2019 `'`) not straight quotes (`'`)

3. **French quotation marks**: `« guillemets »` not `"quotes"`

4. **Decimal comma**: `3,5 heures` not `3.5 heures`

5. **Inclusive writing** (when appropriate): `Pont·s redresseur·s`

To insert non-breaking space in vim: `Ctrl+V u00a0` or `Ctrl+V xa0`

### Sphinx Configuration

Key configuration in `content/conf.py`:

- **Language**: `language = 'fr'`
- **Theme**: `sphinx_rtd_theme` (Read the Docs theme)
- **Extensions**:
  - `sphinxcontrib.drawio` - Diagram support (requires DrawIO installation)
  - `sphinx_copybutton` - Copy button on code blocks
  - `sphinx_simplepdf` - PDF generation
  - `sphinx_last_updated_by_git` - Show last update time from git
  - `sphinx.ext.autosectionlabel` - Auto-generate section labels for cross-refs
  - `sphinx.ext.graphviz` - Graphviz diagram support
  - `sphinx.ext.imgmath` - Math rendering as images (SVG format)

- **Auto-section labeling**:
  ```python
  autosectionlabel_prefix_document = True  # Prefix labels with document name
  autosectionlabel_maxdepth = 2           # Only top 2 levels get auto-labels
  ```
  This prevents duplicate label warnings in large documentation.

## Key Development Patterns

### Adding a New Assembly Section

1. Create the file in `content/mono/` or `content/tri/` (or `content/common/` if shared)
2. Add frontmatter with metadata:
   ```rst
   ⏱️ **Temps estimé** : X-Y heures (débutant), A-B heures (expérimenté)
   🔧 **Niveau de difficulté** : Débutant / Intermédiaire / Avancé
   ⚠️ **Niveau de risque** : Faible / Moyen / Élevé / Très élevé
   ```

3. Add prerequisites box:
   ```rst
   .. admonition:: 📋 Prérequis

      Avant de commencer ce chapitre :

      ☐ Chapitre :ref:`safety-overview` lu et compris
      ☐ Outils nécessaires à disposition
      ☐ Temps disponible (X heures)
      ☐ Espace de travail propre et organisé
   ```

4. Add verification checkpoints after major steps:
   ```rst
   .. admonition:: ✅ Point de Contrôle — [Component Type]

      Avant de continuer, vérifiez :

      ☐ Item 1
      ☐ Item 2
      ☐ Item 3
   ```

5. Link technical terms to glossary using `:term:`term``
6. Add cross-references to related sections using `:ref:`label``
7. Update `index.rst` to include the new section in the table of contents

### Modifying Shared Content

If you need to modify content that's shared between mono and tri versions:

1. **Check if it's an include file**: Look for `.. include::` directives in mono/tri files
2. **Edit the include file** in `content/common/*.inc.rst`
3. **Test both versions**: Build and check that changes work correctly in both contexts
4. **Verify section levels**: Include files should start at level 3 (`~~~`) or deeper since they're included in level 2 sections

### Adding Safety Warnings

Use appropriate RST directives based on severity:

- `.. danger::` - Physical safety hazards (electrical shock, fire, burns)
- `.. warning::` - Software/configuration issues, potential mistakes
- `.. important::` - Critical information that's not a safety hazard
- `.. note::` - General information, clarifications, tips
- `.. tip::` - Helpful suggestions, best practices
- `.. hint::` - Reminders, procedural guidance

**Reserve `.. danger::` for actual physical safety hazards only** to avoid "warning fatigue" where users start ignoring danger alerts.

### Maintaining Build Quality

After making changes:

1. **Build and check for errors**:
   ```bash
   make html
   ```

2. **Review warnings**: Aim to keep warnings minimal. Common acceptable warnings:
   - Glossary terms not yet linked (will be fixed incrementally)
   - External links that are correct but Sphinx can't verify

3. **Check French typography**: Use proper non-breaking spaces and typographic apostrophes

4. **Verify cross-references**: Ensure all `:ref:` and `:term:` links resolve correctly

5. **Test visual appearance**: Open `_build/html/index.html` and spot-check pages

## Important Notes

### Git Submodules

The `1-phase/` and `3-phase/` directories are git submodules pointing to external repositories. They are not actively developed in this repository. If you need to work on the firmware code, clone the respective repository directly.

#### Submodule Management

```bash
# Initialize and update submodules (first time or after clone)
git submodule update --init --recursive

# Update submodules to latest commit from their remote repositories
git submodule update --remote

# Check current submodule status
git submodule status
```

#### Working with Firmware Code

If you need to modify firmware code:

1. **For documentation purposes only**: The submodules are read-only references. Do NOT modify them in this repository.

2. **For firmware development**: Clone the firmware repository directly:
   ```bash
   # Single-phase firmware
   git clone https://github.com/FredM67/PVRouter-1-phase.git

   # Three-phase firmware
   git clone https://github.com/FredM67/PVRouter-3-phase.git
   ```

3. **For documentation cross-references**: You can reference firmware files in documentation using relative paths like `../../1-phase/Mk2_fasterControl_Full/` but avoid duplicating firmware documentation in this repository.

The submodules are primarily included for:
- Easy access to firmware version information
- Generating cross-references in documentation
- Ensuring documentation matches firmware capabilities

### Continuous Integration & Deployment

The documentation has two deployment targets:

#### 1. GitHub Pages (via GitHub Actions)

Workflow: `.github/workflows/documentation.yaml`

Triggers on:
- Push to any branch (except changes to submodules)
- Pull requests
- Manual workflow dispatch

Build process:
1. Installs DrawIO (with caching) for diagram rendering
2. Installs Graphviz for graph diagrams
3. Installs Python dependencies from `requirements.txt`
4. Builds HTML documentation with Sphinx
5. Deploys to GitHub Pages (on main branch only)

**Note**: Changes to submodules (`1-phase/`, `3-phase/`) do NOT trigger documentation builds since they're maintained separately.

#### 2. ReadTheDocs

Configuration: `.readthedocs.yaml`

The documentation is also built and deployed to ReadTheDocs on push to the `main` branch. ReadTheDocs uses custom build commands to install DrawIO for diagram rendering.

Both deployments ensure diagrams (`.drawio` files) are properly rendered to PNG/SVG format.

### Recent Major Improvements

The documentation has undergone significant improvements (see `DOCUMENTATION_REVIEW.md`):
- **Phase 1** (mostly complete): Critical safety content, troubleshooting, software installation guide
- **Phase 2** (in progress): Beginner accessibility improvements
- Build quality improved from 73 warnings → 11 warnings (85% reduction)
- Added 16 verification checkpoints across assembly guides
- Created comprehensive safety chapter (684 lines)
- Added detailed troubleshooting guide (1,159 lines)

### Documentation Quality Goals

The target audience is **non-specialist users with minimal electrical/electronics knowledge**. All content should:
- Explain technical terms before using them
- Provide clear, detailed procedures (not vague instructions like "use adhesive")
- Include safety context and prevention measures
- Have photos or diagrams for complex steps
- Anticipate common mistakes and provide guidance
- Use verification checkpoints to prevent errors from propagating

### Critical Safety Context

This project involves:
- **High voltage electrical work** (230V AC, life-threatening)
- **Fire hazards** (high-power soldering, incorrect wiring)
- **Legal requirements** (French NF C 15-100 standard, Consuel certification, insurance implications)

Always maintain and enhance safety warnings. The `installation-finale.rst` chapter is particularly critical as it covers mains electrical connection.

## Support and Documentation Resources

- **GitHub Issues**: Report documentation issues at https://github.com/FredM67/Mk2PVRouter/issues
- **DOCUMENTATION_REVIEW.md**: Comprehensive documentation quality assessment and improvement roadmap
- **RST_SECTION_LEVELS.md**: Reference for RST heading hierarchy
- **CONTRIBUTING.md**: General contribution guidelines
