<div align="center">

<img src="project/uploads/Logo%20w%20Text.png" alt="ArchiLoom" height="40">

**A Revit ribbon tab of small, sharp tools for detailing and family housekeeping.**

[![pyRevit](https://img.shields.io/badge/pyRevit-IronPython%202.7-5EA079?style=flat-square)](https://github.com/eirannejad/pyRevit)
[![Revit](https://img.shields.io/badge/Revit-2021–2026-3F4643?style=flat-square)](https://www.autodesk.com/products/revit)
[![License: MIT](https://img.shields.io/badge/License-MIT-EB664B?style=flat-square)](LICENSE)

[**Landing Page**](https://huunhan2261.github.io/archiloom/) · [**Download**](https://github.com/huunhan2261/archiloom/releases/latest) · [**Issues**](https://github.com/huunhan2261/archiloom/issues)

</div>

---

## What is ArchiLoom?

ArchiLoom is a pyRevit extension — one Revit ribbon tab packed with 20 tools across 4 panels, built for the work nobody schedules time for: renaming families in bulk, syncing detail type data through Excel, laying out detail items, and reusing sheet layouts. Every dialog follows one UI standard, so you learn the pattern once.

### Panels

| Panel | Tools | Purpose |
|---|---|---|
| **Detailing** | 9 | Detail items, line styles and sheet layouts — the repetitive half of documentation |
| **Family** | 6 | Naming and cleanup for families and types — bulk edits with a preview you can trust |
| **Elements** | 2 | Model-side edits on whatever you already have selected |
| **Sandbox** | 3 | Newer tools still earning their place on the ribbon |

## Installation

1. Download the latest release from [Releases](https://github.com/huunhan2261/archiloom/releases/latest).
2. Extract the `ArchiLoom.extension` folder.
3. In Revit → pyRevit → Settings → **Custom Extensions Directories** → add the folder that **contains** `ArchiLoom.extension` (not the extension folder itself).
4. **Reload** pyRevit. The ArchiLoom tab appears on the ribbon.

## UI Standard

Every dialog follows the ArchiLoom UI Standard v2 — one green header band, one coral action button, neutral everything else. The design system is documented in `lib/GUI/Resources/UI_GUIDELINE.md` within the extension.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup instructions, IronPython 2.7 constraints, and the new-tool checklist.

## License

[MIT](LICENSE) — © 2026 Nhan Nguyen Huu. The logo and wordmark stay with ArchiLoom.

## Author

Built by **Nhan Nguyen Huu**, architect and BIM lead.
[huunhan2261@gmail.com](mailto:huunhan2261@gmail.com)
