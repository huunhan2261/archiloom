# -*- coding: utf-8 -*-
__title__  = "My Tool"
__author__ = "Nhan Nguyen Huu <huunhan2261@gmail.com>"
__doc__    = """Description of the tool shown as the button tooltip.

How-to:
1. ...
2. ...
3. ..."""

# IMPORTS
from pyrevit import forms, revit

from GUI.theme import apply_theme, set_logo, set_message   # brand styles, logo, message bar

doc   = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# GUI
class MyWindow(forms.WPFWindow):
    def __init__(self, xaml):
        # apply_theme() MUST run before WPFWindow.__init__: XAML parsing
        # (wpf.LoadComponent) resolves {StaticResource ...} eagerly, so the
        # merged dictionary has to be on self.Resources beforehand, or every
        # StaticResource in the file (TitleText, AccentRule, PrimaryButton,
        # ...) throws "Cannot find resource named ...".
        apply_theme(self)
        forms.WPFWindow.__init__(self, xaml)
        self.main_title.Text = __title__
        set_logo(self.footer_logo)      # brand wordmark, bottom-left of the footer
        self.ShowDialog()

    # EVENT HANDLERS (names must match Click=/MouseDown= in the XAML)
    def button_close(self, sender, e):
        self.Close()

    def header_drag(self, sender, e):
        from System.Windows.Input import MouseButtonState
        from System.Windows.Window import DragMove
        if e.LeftButton == MouseButtonState.Pressed:
            DragMove(self)

    def button_browse(self, sender, e):
        folder = forms.pick_folder()
        if folder:
            self.input_folder.Text = folder

    def button_run(self, sender, e):
        # One message bar, one style. kind: info | warn | success | danger
        if not self.input_author.Text:
            set_message(self.msg_bar, self.msg_text, 'warn', "Report author is empty.")
            return
        with revit.Transaction(__title__):
            pass   # <-- tool logic here
        self.Close()

# MAIN
if __name__ == '__main__':
    MyWindow("_TEMPLATE_window.xaml")   # rename to your own *.xaml
