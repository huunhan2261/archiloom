# CLAUDE.md

Instructions for Claude Code (and anyone else) working in this repository.

## What this repo is

This is the **marketing/landing-page repo** for the ArchiLoom pyRevit addin, deployed
to GitHub Pages at `https://huunhan2261.github.io/archiloom/`. It is **not** the addin
source repo — it's a separate, small static site that links out to the real addin
releases and source.

## Scope boundary — do not edit `project/ArchiLoom.extension/`

`project/ArchiLoom.extension/` is a **read-only reference copy** of a few files from
the real ArchiLoom addin (`lib/GUI/Resources/UI_GUIDELINE.md`, `theme.py`,
`ArchiLoom_styles.xaml`, `_TEMPLATE_*`, logo assets). It exists here only so the
landing page's copy and visual design can stay accurate to the real product —
tool lists, panel names, and the brand color palette all come from these files.

**Never edit anything under `project/ArchiLoom.extension/`.** If it looks stale or
wrong, that's a signal to resync it from the real addin repo, not to patch it here.
Everything else in this repo (the landing page itself) is fair game.

## Repo layout

- `docs/` — the actual GitHub Pages deployment root. `docs/index.html` is the
  production landing page (plain static HTML/CSS, no build step, no JS framework).
  `docs/assets/` holds the images the page references (currently just the logo).
- `.github/workflows/static.yml` — deploys `docs/` to GitHub Pages via
  `actions/upload-pages-artifact` + `actions/deploy-pages` on every push to `main`.
  It uploads `docs/` only, not the whole repo.
- `archiloom-landing.dc.html` (repo root) — the original **design prototype**,
  authored with Claude's Design canvas tool (`x-dc` custom elements, `sc-for`/`sc-if`
  template directives, `{{ }}` bindings, a `support.js` runtime). This file is a
  **mockup/reference only** — it is not valid deployable HTML on its own (the
  template directives never resolve and `support.js` isn't shipped), and it is
  gitignored from *new* changes for that reason. `docs/index.html` is the hand-built,
  fully resolved static translation of this design. When the design changes, edit
  the `.dc.html` prototype first, then manually re-apply the same changes to
  `docs/index.html` — there is no automated sync between the two. If you reopen this
  design in the Claude Design canvas tool, it recreates its own local workspace
  (`project/Canvas.dc.html`, `support.js`, cursor images, `project/uploads/`, etc.) —
  that workspace is gitignored and disposable; only `project/ArchiLoom.extension/`
  under `project/` is meant to persist.
- `README.md`, `CONTRIBUTING.md`, `LICENSE` — describe the addin itself (installation,
  contributing rules, license), copied/kept in sync with the real addin repo.

## UI / brand standard

The landing page reuses the ArchiLoom UI Standard v2 palette and type scale
documented in `project/ArchiLoom.extension/lib/GUI/Resources/UI_GUIDELINE.md`
(read-only reference, see above): green `#5EA079` header/accent, coral `#EB664B`
for exactly one primary action per view, everything else neutral grays. Keep the
landing page visually consistent with that system rather than inventing new colors.

## Working conventions

- This is plain static HTML/CSS — no bundler, no npm install, no build step.
  "Building" this project means editing `docs/index.html` directly and previewing
  it in a browser.
- Don't reintroduce Claude Design-specific markup (`<x-dc>`, `sc-for`, `sc-if`,
  `{{ }}` bindings, `style-hover` attributes, `support.js`) into `docs/index.html` —
  it must stay plain, dependency-free HTML that renders correctly with zero JS.
  Hover states belong in a real `<style>` block using CSS classes and `:hover`.
- Real links (GitHub repo, releases, issues) are hardcoded in `docs/index.html`;
  update them there if the repo ever moves.
