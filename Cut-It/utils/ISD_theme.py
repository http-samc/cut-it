"Qt Theme for ISD version of Cut-It"

from PyQt5.QtGui import QPalette, QColor
from qtmodern.styles import _apply_base_theme

def ISD(app):
    """ Apply ISD Theme to the Qt application instance.

        Args:
            app (QApplication): QApplication instance.
    """

    lightPalette = QPalette()

    # base
    lightPalette.setColor(QPalette.WindowText, QColor(193, 200, 215))
    lightPalette.setColor(QPalette.Button, QColor(56, 84, 110))
    lightPalette.setColor(QPalette.Light, QColor(66, 101, 132))
    lightPalette.setColor(QPalette.Midlight, QColor(66, 101, 132))
    lightPalette.setColor(QPalette.Dark, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.Text, QColor(193, 200, 215))
    lightPalette.setColor(QPalette.BrightText, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.ButtonText, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.Base, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.Window, QColor(36, 92, 132))
    lightPalette.setColor(QPalette.Shadow, QColor(20, 20, 20))
    lightPalette.setColor(QPalette.Highlight, QColor(76, 163, 224))
    lightPalette.setColor(QPalette.HighlightedText, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.Link, QColor(0, 162, 232))
    lightPalette.setColor(QPalette.AlternateBase, QColor(7, 47, 78))
    lightPalette.setColor(QPalette.ToolTipBase, QColor(36, 92, 132))
    lightPalette.setColor(QPalette.ToolTipText, QColor(7, 47, 78))

    # disabled
    lightPalette.setColor(QPalette.Disabled, QPalette.WindowText,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.Text,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.ButtonText,
                         QColor(115, 115, 115))
    lightPalette.setColor(QPalette.Disabled, QPalette.Highlight,
                         QColor(190, 190, 190))
    lightPalette.setColor(QPalette.Disabled, QPalette.HighlightedText,
                         QColor(115, 115, 115))

    app.setPalette(lightPalette)

    _apply_base_theme(app)