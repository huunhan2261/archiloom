<div align="center">

<img src="docs/assets/logo.png" alt="ArchiLoom" height="40">

**A Revit ribbon tab of small, sharp tools for detailing and family housekeeping.**

[![.NET 8](https://img.shields.io/badge/.NET-8-5EA079?style=flat-square)](https://dotnet.microsoft.com/)
[![Revit](https://img.shields.io/badge/Revit-3F4643?style=flat-square)](https://www.autodesk.com/products/revit)
[![License: Freeware](https://img.shields.io/badge/License-Freeware%20(EULA)-EB664B?style=flat-square)](EULA.txt)

[**Landing Page**](https://huunhan2261.github.io/archiloom/) · [**Download**](https://github.com/huunhan2261/archiloom/releases/latest) · [**Issues**](https://github.com/huunhan2261/archiloom/issues)

</div>

---

## What is ArchiLoom?

ArchiLoom is a native C# Revit add-in — one Revit ribbon tab packed with 20 tools across 5 working panels (plus About), built for the work nobody schedules time for: renaming families in bulk, syncing parameters through Excel, laying out detail items, renumbering sheets, auditing filters/view templates, and reusing sheet layouts. Every dialog follows one UI standard, so you learn the pattern once.

### Panels

| Panel | Tools | Purpose |
|---|---|---|
| **Family** | 4 | Naming and cleanup for families and types — bulk edits with a preview you can trust |
| **Detailing** | 6 | Detail items, line styles and sheet layouts — the repetitive half of documentation |
| **Checking** | 5 | QA on the model in front of you: missing tags, annotation/parameter highlighting, 3D crop, Excel parameter sync |
| **Auditing** | 4 | Project-wide housekeeping: filter and view-template audits, sheet renumbering, system-definition renames |
| **Visual** | 1 | Camwalk — turn the active 3D view into a live fly-through |
| **About** | 1 | Opens this landing page |

## Installation

Supported Revit versions: **2024, 2025 and 2026**. The `.msi` installer detects which of them are on the machine and registers ArchiLoom for each one.

1. Download the latest installer from [Releases](https://github.com/huunhan2261/archiloom/releases/latest) (`ArchiLoom.msi`, or `ArchiLoom-Setup.exe` for a Revit 2026-only install).
2. Close Revit, then run it — no admin rights needed, it installs for the current Windows user only and registers ArchiLoom as a Revit add-in.
3. Open Revit. The **ArchiLoom** tab appears on the ribbon.

## Contributing

ArchiLoom is closed-source freeware — see [License](#license) below. Bug reports and feature requests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Freeware — see [EULA.txt](EULA.txt). ArchiLoom is **not** open source: no modification, decompilation, or redistribution without written permission from the author. The logo and wordmark stay with ArchiLoom.

## Author

Built by **Nhan Nguyen Huu**, architect and BIM Specialist.
[huunhan2261@gmail.com](mailto:huunhan2261@gmail.com)
