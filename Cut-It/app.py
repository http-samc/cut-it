from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget, QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
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
        #self.cardHistory = dlg()
        self.cardHistory = qtmodern.windows.ModernDialog(QDialog())
        self.cardHistory.exec_()

class dlg(CARD_DIALOG):
    def __init__(self) -> None:
        super().__init__()

# Starts program with QtModern Styling
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = main()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())