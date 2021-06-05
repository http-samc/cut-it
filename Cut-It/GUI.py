"""
    Creates a GUI object based off the latest version of app.ui
    GUI visual tests can be ran by running this program 
    Inherited by app.py for simplicity
"""

from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from utils.distro import version, tag
import qtmodern.windows
import qtmodern.styles
from PyQt5 import uic
import sys

class GUI(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # Loading UI
        uic.loadUi('app.ui', self)

        # Setting Title
        self.setWindowTitle(f"Cut-It™ by Offtime Roadmap® v.{version()}@{tag()}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    gui = GUI()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())