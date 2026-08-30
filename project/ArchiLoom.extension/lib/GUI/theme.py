# -*- coding: utf-8 -*-
"""ArchiLoom GUI theme — brand palette & shared WPF styles (UI Standard v2).

Apply the shared style dictionary to any WPF window (pyRevit's
forms.WPFWindow):

    from GUI.theme import apply_theme

    class MyWindow(forms.WPFWindow):
        def __init__(self, xaml):
            apply_theme(self)                   # BEFORE WPFWindow.__init__
            forms.WPFWindow.__init__(self, xaml)

apply_theme() MUST run before WPFWindow.__init__: wpf.LoadComponent parses
the XAML and resolves every {StaticResource ...} eagerly, so the merged
dictionary has to be on self.Resources beforehand.

Rules, tokens and do/don't: Resources/UI_GUIDELINE.md
Single source of truth for colours: Resources/ArchiLoom_styles.xaml
(the constants below are mirrors for code that needs a hex string).
"""
import os, clr
clr.AddReference("System")
from System import Uri
from System.Windows import ResourceDictionary

# --- Brand ------------------------------------------------------------
BRAND_GREEN = "#5EA079"      # identity: header band, selection, success
BRAND_CORAL = "#EB664B"      # action: THE primary button + accent rule
BRAND_RED   = BRAND_CORAL    # legacy alias

# --- Green ramp -------------------------------------------------------
GREEN_50, GREEN_100, GREEN_200 = "#EEF5F1", "#DCEAE2", "#B9D5C5"
GREEN_400, GREEN_500           = "#74AF8B", "#5EA079"
GREEN_600, GREEN_700           = "#4E8A67", "#3D6E52"

# --- Coral ramp -------------------------------------------------------
CORAL_50, CORAL_100, CORAL_200 = "#FDEEEA", "#FAD9D1", "#F5B8A9"
CORAL_400, CORAL_500           = "#EF7F68", "#EB664B"
CORAL_600, CORAL_700           = "#D8543B", "#B44530"

# --- Neutral ramp (carries ~90% of the UI) ----------------------------
NEUTRAL_000, NEUTRAL_50, NEUTRAL_100 = "#FFFFFF", "#F7F9F8", "#EFF2F0"
NEUTRAL_200, NEUTRAL_300, NEUTRAL_400 = "#E2E6E4", "#CBD1CE", "#A3ACA8"
NEUTRAL_500, NEUTRAL_600, NEUTRAL_700 = "#78827E", "#5A6360", "#3F4643"
NEUTRAL_800, NEUTRAL_900              = "#2E3230", "#1E2120"

# --- Semantic (message bars + table diff cells only) ------------------
INFO_TEXT,    INFO_BG    = "#2F6B85", "#EDF4F8"
WARN_TEXT,    WARN_BG    = "#9A6B15", "#FBF3E3"
SUCCESS_TEXT, SUCCESS_BG = "#3D6E52", "#EEF5F1"
DANGER_TEXT,  DANGER_BG  = "#B44530", "#FDEEEA"

# --- Type scale (5 sizes, 2 weights: Normal / SemiBold) ---------------
FS_TITLE, FS_SECTION, FS_BODY, FS_LABEL, FS_OVERLINE = 20, 14, 13, 12, 11
FONT_UI, FONT_MONO = "Segoe UI", "Consolas"

# --- Fixed sizes ------------------------------------------------------
HEADER_HEIGHT = 52       # green band
ACCENT_HEIGHT = 2        # coral rule under the band
INPUT_HEIGHT  = 28
BUTTON_HEIGHT = 30       # ghost/row buttons: 26
ROW_HEIGHT    = 28
GUTTER        = 16       # window padding, all four sides
RADIUS        = 4        # inputs: 3

# Window widths — pick one, do not invent new ones.
WIDTH_FORM   = 460       # single-column form (Family Rename)
WIDTH_WIZARD = 620       # form + preview (Batch Rename)
WIDTH_LIST   = 1040      # table / list tools (Detail Type Excel Sync)

_RES_DIR     = os.path.join(os.path.dirname(__file__), "Resources")
_STYLES_PATH = os.path.join(_RES_DIR, "ArchiLoom_styles.xaml")

LOGO_MARK     = os.path.join(_RES_DIR, "logo_mark.png")       # symbol only
LOGO_WORDMARK = os.path.join(_RES_DIR, "logo_wordmark.png")   # symbol + text
LOGO_HEIGHT   = 16    # wordmark height in the footer


def apply_theme(window):
    """Merge ArchiLoom_styles.xaml into the window's resources."""
    rd = ResourceDictionary()
    rd.Source = Uri(_STYLES_PATH)
    window.Resources.MergedDictionaries.Add(rd)
    return window


def set_logo(image, wordmark=True):
    """Point an <Image x:Name="footer_logo"/> at the brand logo.

    The logo lives in lib/GUI/Resources/, which has no pack URI from a
    pushbutton folder, so the Source must be set from code:

        set_logo(self.footer_logo)

    Placement rule: the wordmark sits at the BOTTOM-LEFT of the footer,
    full colour, 16px tall. Never in the green header band.
    """
    from System import Uri
    from System.Windows.Media.Imaging import BitmapImage
    path = LOGO_WORDMARK if wordmark else LOGO_MARK
    image.Source = BitmapImage(Uri(os.path.abspath(path)))
    image.Height = LOGO_HEIGHT
    return image


def set_message(border, text_block, kind, text):
    """Fill a message bar and switch it to one of the semantic styles.

    kind: 'info' | 'warn' | 'success' | 'danger'
    Usage (XAML has a Border x:Name="msg_bar" wrapping a TextBlock
    x:Name="msg_text"):
        set_message(self.msg_bar, self.msg_text, 'warn', "3 types in use.")
    """
    kind = (kind or "info").lower()
    border.Style = border.FindResource("Message{}".format(kind.capitalize()))
    text_block.Style = text_block.FindResource("Message{}Text".format(kind.capitalize()))
    text_block.Text = text
    from System.Windows import Visibility
    border.Visibility = Visibility.Visible
