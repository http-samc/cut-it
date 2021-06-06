from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget, QDialog)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import qtmodern.windows
import qtmodern.styles
from GUI import GUI
import sys

class main(GUI):

    """
        Adds logic to the GUI (inherited from GUI)
    """

    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = main()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())