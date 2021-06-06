"""
    Creates a GUI object based off the latest version of app.ui
    GUI visual tests can be ran by running this program 
    Inherited by app.py for simplicity
"""

from PyQt5.QtWidgets import (QDialog, QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from utils.distro import version, tag
from utils.ext_combobox import ExtendedComboBox
from utils.resource import PATH
import qtmodern.windows
import qtmodern.styles
from PyQt5 import uic
import sys

class GUI(QMainWindow):

    def __init__(self) -> None:
        super().__init__()

        # Loading UI
        uic.loadUi('app.ui', self)

        # Setting Title (Spaces are due to a centering bug in QtModern)
        self.setWindowTitle(f"                    Cut-It™ by Offtime Roadmap® v.{version()}@{tag()}")
        
        # Applying custom changes to GUI
        self.distro.setText(self.getDistroDetails())
        self.addCardHistory()
        self.addAttrs()

    def addCardHistory(self):
        """
            Manually fill out the Card History groupBox (due to custom widgets)
        """

        self.cardSelector = ExtendedComboBox()
        self.cardSelector.setObjectName(u"cardSelector")
        self.cardSelector.setMinimumSize(QSize(150, 0))
        self.horizontalLayout.addWidget(self.cardSelector)

        self.open_card = QtWidgets.QPushButton()
        self.open_card.setObjectName(u"open_card")
        self.open_card.setMinimumSize(QSize(20, 20))
        self.open_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.open_card)
        self.open_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/open_icon.png')))

        self.delete_card = QtWidgets.QPushButton()
        self.delete_card.setObjectName(u"delete_card")
        self.delete_card.setMinimumSize(QSize(15, 15))
        self.delete_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.delete_card)
        self.delete_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/delete_icon.png')))

        self.copy_card = QtWidgets.QPushButton()
        self.copy_card.setObjectName(u"copy_card")
        self.copy_card.setMinimumSize(QSize(15, 15))
        self.copy_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.copy_card)
        self.copy_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/copy_icon.png')))

        self.save_card = QtWidgets.QPushButton()
        self.save_card.setObjectName(u"save_card")
        self.save_card.setMinimumSize(QSize(15, 15))
        self.save_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.save_card)
        self.save_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/save_icon.png')))

    def addAttrs(self):
        """
            Adds in misc. GUI attributes
        """

        self.autocut.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/cut_icon.png')))

    def getDistroDetails(self) -> str:
        """
            Returns a formatted String to be inserted into the Distro box in the about section
        """

        distroDetails = f"""<p align="center">
        🚀Cut-It FAQ🚀 || Version 📝 {version()} || Tag🏷️ @{tag()} 
        || Website🌐 https://cutit.cards || GitHub Repository📚 https://github.com/http-samc/cut-it 
        || Contributors👐 https://github.com/http-samc/cut-it/graphs/contributors 
        || Current Project Managers👷 Samarth Chitgopekar, Adithya Vaidyanathan, Gabriel Seidman
        """.replace('\n','') + "<br><br>Icon Credits: Scissors Icon by Daniel Bruce, Save Icon by Google Inc., "
        distroDetails += "Delete Icon by Alex Martynov, Clipboard Icon by Soni Sokell, Export Icon by Typicons.</p>"

        return distroDetails
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = GUI()
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())