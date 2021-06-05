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
        self.distro.setText(self.getDistroDetails())
    
    def getDistroDetails(self) -> str:
        """
            Returns a formatted String to be inserted into the Distro box in the about section
        """

        distroDetails = f"""<p align="center">
🚀Cut-It FAQ🚀 || Version 📝: {version()} || Tag🏷️: @{tag()} 
|| Website🌐: https://cutit.cards || GitHub Repository📚: https://github.com/http-samc/cut-it 
|| Contributors👐: https://github.com/http-samc/cut-it/graphs/contributors 
|| Current Project Managers👷: Samarth Chitgopekar, Adithya Vaidyanathan, Gabriel Seidman
</p>""".replace('\n','')

        return distroDetails

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    gui = GUI()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())