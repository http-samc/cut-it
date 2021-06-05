from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget, QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import qtmodern.windows
import qtmodern.styles
from GUI import MAIN
import sys

class main(MAIN):

    """
        Adds logic to the GUI
    """

    def __init__(self) -> None:
        super().__init__()
        self.bold.clicked.connect(self.s)
    
    def s(self):
        print(self.geometry())

# Starts program with QtModern Styling
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = main()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())