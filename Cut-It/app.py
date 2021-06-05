from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget, QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import qtmodern.windows
import qtmodern.styles
from GUI import MAIN, CARD_DIALOG
import sys

class main(MAIN):

    """
        Adds logic to the GUI
    """

    def __init__(self) -> None:
        super().__init__()
        self.bold.clicked.connect(self.createPopup)
    
    def createPopup(self):
        self.cardHistory = dlg(parent=self)
        self.cardHistory = qtmodern.windows.ModernWindow(self.cardHistory, parent=self, hide_window_buttons=True)
        self.cardHistory.setWindowModality(Qt.Qt.WindowModal)
        self.cardHistory.show()

class dlg(CARD_DIALOG):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)

# Starts program with QtModern Styling
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = main()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())