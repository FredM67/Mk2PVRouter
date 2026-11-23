# A "dev" version of the documentation

Status: design, for approval. Repo: Mk2PVRouter.

## Intent

The site publishes one documentation, built from `main` with the firmware repos' `main`
(submodules `1-phase`, `3-phase`), plus the old `legacy` branch. The firmware repos work on `dev`
and release to `main`, so new features, and soon both configurators, are invisible until a release.
The user wants readers to pick **stable** or **dev** from the site itself, and to see and use what is
coming (the new configurators first) without waiting for a release.

## Goals

- **A long-lived `dev` branch of Mk2PVRouter.**
  - Documentation for unreleased firmware goes there first.
  - It is merged into `main` at a release, as the firmware repos do.
  - Published at `/Mk2PVRouter/branch/dev/`.
- **The dev build uses the firmware repos' latest `dev`.**
  - When the workflow builds `dev`, it checks out each submodule's `dev` head before building, so
    no bump commits are needed.
  - A daily scheduled build picks up firmware changes, and `workflow_dispatch` runs it by hand.
- **The version menu** (bottom of the sidebar) lists stable (the site root), dev, and legacy.
  - The current version is named correctly. Today it always says "stable".
  - Picking a version opens the same page in that version, or its home page when that page does
    not exist there.
- **A banner on every dev page:** "Development version: for the released firmware, see the stable
  documentation", with a link to the same page in stable. It is in French, like the site.
- **The rest of the dev pages points at dev:**
  - "View/Edit on GitHub" and the PDF download point at dev's own source and PDF;
  - the configurators are dev's (`/branch/dev/configurateur/` and, once it exists,
    `/branch/dev/configurateur-monophase/`).

## Non-goals

- No versioned releases (v1, v2...): just stable, dev and legacy.
- No change to how `main` is built, apart from the shared fixes below.

## Anti-goals

- A reader on stable who lands on dev pages without noticing. That is why the banner is there, and
  why the menu names the version.
- A deploy that silently wipes another branch's pages.

## Approaches (firmware `dev` into the dev build)

1. **The build pulls the firmware `dev` itself (chosen by the user).** `.gitmodules` stays identical
   on both branches, so there is no merge conflict at a release.
2. **Dependabot bump PRs on `dev`.** Each firmware change is a commit, but the site waits for a
   merge, and `.gitmodules` must name `dev` on that branch, which conflicts at each release.
3. **The firmware repos trigger a rebuild on every push.** Updates come within minutes, but it needs
   a write token stored as a secret in two other repos.

## Design

### Workflow (`.github/workflows/documentation.yaml`)

- **Triggers:**
  - push on any branch, as today;
  - `schedule` (daily), which builds `dev`: the job checks out `ref: dev` when
    `github.event_name == 'schedule'`;
  - `workflow_dispatch`.
- **Paths:** drop `1-phase/**` from `paths-ignore`, since the single-phase repo will bring its own
  configurator. Keep `hardware/**`.
- **Firmware `dev`:** after the checkout, when the branch built is `dev`, a step runs
  `git -C 1-phase fetch origin dev && git -C 1-phase checkout FETCH_HEAD`, and the same for
  `3-phase`. The commits used are printed in the log.
- **Deploy:** on `main`, `legacy` and `dev`.
- **One deploy queue:** the Update_gh-pages and Deploy jobs share a single
  `concurrency: { group: gh-pages, cancel-in-progress: false }`. Today two deploys running at once
  each rebuild gh-pages from the old copy and force-push it, so the later one drops the other's
  update.

### Version-aware build (`content/conf.py`)

- **The branch built:** from `GITHUB_REF` (or `git rev-parse --abbrev-ref HEAD` locally). It sets:
  - `github_version` (View/Edit links), today hard-coded to `main`;
  - the current version's name: stable for `main`, dev, legacy, and the branch name otherwise;
  - the base URL: `/Mk2PVRouter/` for `main`, `/Mk2PVRouter/branch/<dir>/` otherwise;
  - the PDF link, under that base URL.
- **`versions`:** stable `/Mk2PVRouter/`, dev `/Mk2PVRouter/branch/dev/`, legacy
  `/Mk2PVRouter/branch/legacy/`.
- **Plausible analytics:** stays on `main` only, as today.

### Menu and banner (`content/_templates/`, `content/_static/`)

- **`versions.html`:**
  - shows the current version's name;
  - marks each entry with `data-base`;
  - a small script (`version-switch.js`) rewrites each entry's link to the same page under that
    base. It checks with a `HEAD` request that the page exists, and falls back to the version's home
    page.
- **Banner:**
  - shown on every page when the version is dev;
  - added through the theme's `layout.html` block, or a template override that is kept small;
  - links to the same page in stable;
  - the theme's "warning" colours.

### Configurators

- **On the site, the single-phase/3-phase switch links are relative**
  (`../configurateur-monophase/`, `../configurateur/`), so each version stays in itself.
  - Offline, or on a firmware repo's GitHub Pages preview, they fall back to the stable absolute
    URLs.
  - This changes the plan of the single-phase configurator: Tasks 6 and 8 use the relative link
    when the page is served under `/Mk2PVRouter/`.
- **In the dev version, the configurator's title gets a "dev" tag.** `copy_configurator` writes a
  small marker that the page reads, e.g. a `version.js` that sets `window.PVR_DOC_VERSION`.
- **The single-phase configurator** is copied to `configurateur-monophase/` from `1-phase/configurator`
  when that folder exists (the existing warning otherwise). This was Task 9 of the configurator plan,
  done here.

### Branch and release flow

- **Creating `dev`:** made from `main` once this PR is merged. It is a branch push to the shared
  repo, so it gets the user's go-ahead.
- **At a release:** merge `dev` into `main`; the submodule pointers on `main` are bumped as today
  (Dependabot).
- **The Mk2PVRouter README** (and `CONTRIBUTING.md`) say where documentation changes go: `dev` for
  unreleased firmware, `main` for fixes to the released documentation.

## Left to the builder

- The exact theme hook for the banner (sphinx_rtd_theme's `layout.html` blocks).
- How the page-exists check is done: `HEAD` with a fallback, or a list of pages per version written
  at build time.
- The log output of the firmware commits used.
