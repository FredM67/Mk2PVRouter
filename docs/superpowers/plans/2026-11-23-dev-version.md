# Dev version of the documentation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** readers pick stable, dev or legacy from the docs site's version menu. The dev version is
built from Mk2PVRouter `dev` and the firmware repos' latest `dev`, and its configurators come from
those repos.

**Architecture:**
- `conf.py` learns which branch it builds and derives everything version-specific from it;
- a template override and a small script give the menu and the banner;
- the workflow deploys `dev`, pulls the firmware `dev` heads when it builds it, and serializes
  deploys.

**Tech Stack:** Sphinx with sphinx_rtd_theme, Jinja templates, plain JavaScript, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-11-23-dev-version-design.md`

## Global Constraints

- **Version names and base URLs:**
  - stable: `/Mk2PVRouter/` (branch `main`);
  - dev: `/Mk2PVRouter/branch/dev/`;
  - legacy: `/Mk2PVRouter/branch/legacy/`;
  - other branches: `/Mk2PVRouter/branch/<branch with / as -->/` (the workflow's existing rule).
- **The branch built:** `GITHUB_REF` (`refs/heads/<name>`) in CI, `git rev-parse --abbrev-ref HEAD`
  locally.
- **Site texts:** in French, with U+00A0 before `: ; ! ?` and inside « ».
- **Deploy branches:** `main`, `legacy` and `dev`. Update_gh-pages and Deploy share
  `concurrency: { group: gh-pages, cancel-in-progress: false }`.
- **`.gitmodules`:** unchanged. The firmware `dev` is checked out at build time, only when building
  `dev`.
- **Plausible analytics:** on `main` only, as today.
- **GitHub Actions:** keep readable `@vX` action tags, never SHA pins.
- **Commits:** end with `Co-Authored-By: Claude <noreply@anthropic.com>`.
- **The `dev` branch:** created on GitHub only after this PR is merged, with the user's go-ahead.

## Review Focus

1. **A page that exists in one version and not the other.** Switching falls back to that version's
   home page, never a 404. Owner: Task 2.
2. **A local build with no `GITHUB_REF` and a detached HEAD** (`git rev-parse` gives `HEAD`). It
   builds as stable, with no crash. Owner: Task 1.
3. **A feature branch build.** It names itself after the branch and shows the banner (anything that
   is not stable is pre-release), with View/Edit links on that branch. Owner: Tasks 1 and 2.
4. **The single-phase submodule without `configurator/`** (today's `main`). The build warns and
   still publishes the 3-phase configurator. Owner: Task 3.
5. **A scheduled run.** It builds and deploys `dev` only, never `main`. Owner: Task 4.

---

### Task 1: conf.py knows the version it builds

**Files:**
- Modify: `content/conf.py` (`github_version`, `html_context`, the PDF link, the analytics condition).
- Create: `content/doc_version.py`, a pure function, testable without Sphinx.
- Test: `tests/test_doc_version.py` (pytest; add `pytest` to `requirements.txt` if it is missing).

**Interfaces:**
- Produces: `doc_version.describe(branch: str | None) -> dict`, with keys:
  - `branch`, the git branch, `main` when unknown;
  - `name`: `stable`, `dev`, `legacy`, or the branch;
  - `base`: the URL prefix with a trailing `/`;
  - `is_stable: bool`;
  - `versions`: a list of `(name, base)` for stable, dev and legacy.
- `conf.py` puts these in `html_context` as `doc_version`, `doc_base`, `doc_is_stable` and
  `versions`. `github_version` becomes the branch.

- [ ] **Step 1: Write the failing tests.**
  - `describe('main')` gives `name` `stable` and `base` `/Mk2PVRouter/`.
  - `describe('dev')` gives `dev` and `/Mk2PVRouter/branch/dev/`.
  - `describe('legacy')` gives `legacy` and `/Mk2PVRouter/branch/legacy/`.
  - `describe('feat/x')` gives `feat/x` and `/Mk2PVRouter/branch/feat--x/`.
  - `describe(None)` and `describe('HEAD')` give `stable`.
  - `versions` is `[('stable','/Mk2PVRouter/'), ('dev','/Mk2PVRouter/branch/dev/'), ('legacy','/Mk2PVRouter/branch/legacy/')]`.
- [ ] **Step 2: Run them and check they fail.** Run `python -m pytest tests/test_doc_version.py -q`.
  Expected: FAIL (no module).
- [ ] **Step 3: Implement.**
  - `doc_version.py`.
  - In `conf.py`, read the branch (`GITHUB_REF`, else `git rev-parse --abbrev-ref HEAD`, else
    `None`) and fill `html_context`.
  - The PDF link is `{base}_static/Mk2PVRouter.pdf`.
  - The analytics condition keeps using the branch `main`.
- [ ] **Step 4: Run the tests and build.** Run `python -m pytest tests/test_doc_version.py -q`, then
  `make dirhtml`. Expected: PASS, and the build succeeds with no new warning.
- [ ] **Step 5: Commit** `feat: the build knows its version (stable, dev, legacy, branch)`.

### Task 2: Version menu and dev banner

**Files:**
- Modify: `content/_templates/versions.html`.
- Create:
  - `content/_templates/layout.html` (`{% extends "!layout.html" %}`, the banner block);
  - `content/_static/version-switch.js`;
  - `content/_static/version-banner.css`.
- Modify: `content/conf.py` (`html_js_files`, `html_css_files`).

**Interfaces:**
- Consumes: `doc_version`, `doc_base`, `doc_is_stable`, `versions` (Task 1).

- [ ] **Step 1: Write the menu.** `versions.html` shows `{{ doc_version }}` as the current version,
  replacing the `"latest" if is_latest else "stable"` expression. Each entry is
  `<a href="{{ url }}" data-base="{{ url }}">`.
- [ ] **Step 2: Write `version-switch.js`.** For each `a[data-base]`, the target is the current path
  with the current `doc_base` replaced by the entry's base. Pass the current base through a
  `data-current-base` attribute on `.rst-versions`. Use the same-page target if
  `fetch(target, {method: 'HEAD'})` is ok; otherwise keep the version's home page. Check on click,
  not at load.
- [ ] **Step 3: Write the banner.**
  - In `layout.html`, when not `doc_is_stable`, a banner at the top of the content block: « Version de
    développement : pour le firmware publié, voir la documentation stable ». The link goes to the same
    page under `/Mk2PVRouter/`, through the same script.
  - Mind the U+00A0 before « : » and inside « ».
  - The theme's warning colours, in `version-banner.css`.
- [ ] **Step 4: Check.**
  - Run `make dirhtml` (build stable), then `GITHUB_REF=refs/heads/dev make dirhtml` into another
    output directory.
  - Serve both under `/Mk2PVRouter/` and `/Mk2PVRouter/branch/dev/` with
    `python -m http.server` from a temp tree.
  - In headless Chrome, check: the menu names the version; the banner shows on dev only; switching
    from a dev page opens the same page in stable; a page missing in the target falls back to its
    home page (test with a page deleted from the stable copy).
- [ ] **Step 5: Commit** `feat: version menu that keeps the page, and a banner on the dev version`.

### Task 3: Configurators per version (on top of PR #157, after this PR)

> Moved out of this PR: `copy_configurator` and `configurateur-triphase.rst` only exist in PR #157.
> After this PR is merged and `dev` exists, #157 is retargeted to `dev` and this task is done on top of it.

**Files:**
- Modify: `content/conf.py` (`copy_configurator`).
- Create: `content/firmware/configurateur-monophase.rst`, next to `configurateur-triphase.rst`, in
  the same toctree.

- [ ] **Step 1: Copy both configurators.** `copy_configurator` copies
  `3-phase/configurator` → `configurateur/` (as today) and `1-phase/configurator` →
  `configurateur-monophase/`. Each copy is skipped with the existing warning when its
  `configurator/index.html` is missing.
- [ ] **Step 2: Write the version marker.** In each copied folder, write `doc-version.js`:
  `window.PVR_DOC_VERSION = "<name>";`, with the name from Task 1. The configurators read it to tag
  their title with "dev" (that page-side change is in the configurator plans, Tasks 6 and 8).
- [ ] **Step 3: Write the single-phase page.** `configurateur-monophase.rst`, modelled on
  `configurateur-triphase.rst`, links to `../../configurateur-monophase/`. The relative depth must
  match the triphase page's link.
- [ ] **Step 4: Check.**
  - Run `make dirhtml` with today's submodules. Expected: the 3-phase copy is there, and a warning
    says the single-phase configurator is missing.
  - With `1-phase` checked out at a commit that has `configurator/` (the configurator branch, locally),
    both copies are there, each with its `doc-version.js`.
- [ ] **Step 5: Commit** `feat: the single-phase configurator at /configurateur-monophase/, each with its version`.

### Task 4: Workflow, dev deploys and firmware dev

**Files:**
- Modify: `.github/workflows/documentation.yaml`.

- [ ] **Step 1: Change the triggers.**
  - Add `schedule: - cron: '17 3 * * *'`. When `github.event_name == 'schedule'`, the checkout uses
    `ref: dev`.
  - Remove `1-phase/**` from both `paths-ignore` lists, and the comments that justify it.
- [ ] **Step 2: Pull the firmware `dev`.** Add a step after "Trust the workspace", run when the built
  branch is `dev` (`github.ref == 'refs/heads/dev' || github.event_name == 'schedule'`). For `1-phase`
  and `3-phase`, it runs `git -C <sub> fetch origin dev` and `git -C <sub> checkout FETCH_HEAD`, then
  prints `git -C <sub> log --oneline -1`.
- [ ] **Step 3: Pass the branch to the build.** For scheduled runs, the build step sets
  `GITHUB_REF=refs/heads/dev`, since `GITHUB_REF` is the default branch there. The "Copy new build"
  steps use the same branch: compute it once as a job output or env, `dev` for schedule.
- [ ] **Step 4: Deploy and queue.**
  - The Deploy `if` becomes `main`, `legacy` or `dev`, including scheduled runs.
  - Update_gh-pages and Deploy share `concurrency: { group: gh-pages, cancel-in-progress: false }`.
  - The existing run-level concurrency stays.
- [ ] **Step 5: Check the YAML.** Run
  `python -c "import yaml,sys;yaml.safe_load(open(sys.argv[1]))" .github/workflows/documentation.yaml`,
  and `actionlint` if it is available. Expected: OK.
- [ ] **Step 6: Commit** `ci: deploy the dev version, built with the firmware dev, one deploy at a time`.

### Task 5: Where documentation changes go

**Files:**
- Modify: `README.md`, `CONTRIBUTING.md`, `CLAUDE.md` (if it describes branches).

- [ ] **Step 1: Write it down.**
  - Documentation for unreleased firmware goes to `dev`, and fixes to the released documentation go
    to `main`.
  - At a release, `dev` is merged into `main`.
  - The dev version is at `/Mk2PVRouter/branch/dev/`, rebuilt daily with the firmware `dev`.
  - In French where those files are French, with U+00A0.
- [ ] **Step 2: Commit** `docs: where documentation changes go, stable and dev`.

### After the PR is merged (asks the user first)

- Create `dev` from `main` on GitHub, retarget PR #157 to `dev`, and do Task 3 on top of it.
- Run the workflow on `dev` by hand.
- Check `/Mk2PVRouter/branch/dev/`: the banner, the menu, and the configurator.
