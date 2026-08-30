# Contributing to ArchiLoom

Thanks for considering a contribution! ArchiLoom is a small, opinionated pyRevit extension — the bar for code quality is "would I trust this button on a deadline day?"

## Getting started

1. **Clone** this repo and note the folder that _contains_ `ArchiLoom.extension`.
2. In Revit → pyRevit → Settings → **Custom Extensions Directories** → add that parent folder.
3. **Reload** pyRevit. The ArchiLoom tab should appear on the ribbon.

After editing any file, **Reload** pyRevit and click the button to test. There is no test runner — IronPython 2.7 inside Revit is the only runtime.

## Language

- Code, comments, variable names, commit messages: **English**.
- Tooltip text and dialog labels shown to users may be in Vietnamese, but keep BIM / technical terms in English.

## IronPython 2.7 constraints

This runs on IronPython 2.7 inside Revit. Do **not** use:

| ❌ Forbidden | ✅ Use instead |
|---|---|
| `f"..."` (f-strings) | `"{}".format(x)` |
| `:=` (walrus operator) | regular assignment |
| Type hints (`def f(x: int) -> str:`) | plain signatures |
| `pathlib`, `dataclasses`, `asyncio` | `os.path`, plain classes |

`print(...)` as a function works (pyRevit output console).

## Creating a new tool

1. Copy `lib/GUI/Resources/_TEMPLATE_window.xaml` and `_TEMPLATE_script.py` into a new `MyTool.pushbutton/` folder. Rename both.
2. Add the pushbutton name (without the suffix) to the parent panel's `bundle.yaml` under `layout:`.
3. Follow the **UI Guideline** at `lib/GUI/Resources/UI_GUIDELINE.md` — a dialog that invents its own colours will not be merged.
4. Write both `__doc__` in `script.py` and `tooltip:` in `bundle.yaml` with identical content.
5. Set `__author__ = "Nhan Nguyen Huu <huunhan2261@gmail.com>"`.

### Key patterns

```python
# apply_theme() MUST run BEFORE WPFWindow.__init__
from GUI.theme import apply_theme, set_logo, set_message

class MyWindow(forms.WPFWindow):
    def __init__(self, xaml):
        apply_theme(self)                   # <-- first
        forms.WPFWindow.__init__(self, xaml) # <-- second
        self.main_title.Text = __title__
        set_logo(self.footer_logo)
```

### Checklist before submitting

- [ ] `apply_theme(self)` before `forms.WPFWindow.__init__`
- [ ] Only **one** `PrimaryButton` (coral) per window
- [ ] No hex colours, no numeric `FontSize`, no `Margin` values outside 4/8/12/16/24 in XAML
- [ ] Window width is 460, 620, or 1040 (mode-select dialogs: 400)
- [ ] Footer has `<Image x:Name="footer_logo"/>` + `set_logo(self.footer_logo)`
- [ ] `__doc__` and `bundle.yaml` tooltip match word for word
- [ ] No Python 3 syntax (f-strings, type hints, walrus)
- [ ] Tell the reviewer: **"not yet tested in Revit"** unless you actually tested it

## Pull requests

- One tool per PR when possible.
- Keep diffs focused — style tweaks and new features should be separate PRs.
- If your change affects the shared style dictionary (`ArchiLoom_styles.xaml` or `theme.py`), explain why in the PR description.

## Issues

Bug reports, feature requests, and "this button behaves weirdly in Revit 20XX" are all welcome. Include your Revit version and pyRevit version if relevant.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
