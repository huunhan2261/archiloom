# CLAUDE.md

Instructions for Claude Code (and anyone else) working in this repository.

## What this repo is

This is the **marketing/landing-page repo** for ArchiLoom, deployed to GitHub Pages
at `https://huunhan2261.github.io/archiloom/`. It is **not** the addin source
repo — ArchiLoom is a native C# Revit add-in (`ArchiLoom.Addin`, .NET 8, sibling
project folder, its own separate repo/build), and this repo is a small static
site that links out to its Releases and Issues. ArchiLoom used to be a pyRevit
extension; that version is retired and no longer referenced on the site.

## Repo layout

- `docs/` — the actual GitHub Pages deployment root. `docs/index.html` is the
  production landing page (plain static HTML/CSS, no build step, no JS framework).
  `docs/assets/` holds the images the page references (logo, favicon, marks).
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
  that workspace is gitignored and disposable.
- `README.md`, `CONTRIBUTING.md`, `EULA.txt` — describe ArchiLoom itself
  (installation, how to report bugs/request features, license terms). ArchiLoom is
  closed-source freeware (see `EULA.txt`), so there is no `LICENSE` file and no
  code-contribution workflow — `CONTRIBUTING.md` only covers bug reports and
  feature requests.

## Tool list / panel content — source of truth

The tool list, panel grouping, and per-tool copy on the landing page (hero stats,
the "tab, panel by panel" section, and the `TOOLS` modal-steps array in
`docs/index.html`) describe the real ArchiLoom.Addin ribbon. That ribbon is built
in `ArchiLoomApp.cs` (`OnStartup`, sibling project) — each button's `ToolTip` and
`LongDescription` there is the source of truth for names, panel grouping, and
How-to steps. If the addin's tool list changes, update this landing page's copy to
match by hand; there is no automated sync between the two repos.

## UI / brand palette

Green `#5EA079` for the header/accent band, coral `#EB664B` reserved for exactly
one primary action per view, everything else neutral grays — defined inline in
`docs/index.html`'s `<style>` block (and mirrored in the `.dc.html` prototype).
Keep the landing page visually consistent with that palette rather than inventing
new colors.

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
- Demo videos referenced by the `TOOLS` array in `docs/index.html` (`videos/*.mp4`)
  are placeholders until real screen recordings of the C# addin's UI are captured —
  see `docs/videos/README.md`.
