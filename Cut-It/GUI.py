"""
    Creates a GUI object based off the latest version of app.ui
    GUI visual tests can be ran by running this program 
    Inherited by app.py for simplicity
"""

from utils.ext_combobox import ExtendedComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from utils.distro import version, tag
from utils.resource import PATH
from PyQt5.QtCore import QSize
import qtmodern.windows
import qtmodern.styles
from PyQt5 import uic
import sys

class GUI(QMainWindow):

    def __init__(self, isLight = False) -> None:
        """
            Loads latest UI
        """

        super().__init__()
        
        # Storing theme
        self.isLight = isLight

        # Loading UI
        uic.loadUi('app.ui', self)

        # Setting Title (Spaces are due to a centering bug in QtModern)
        SPACES = "                    "
        self.setWindowTitle(f"{SPACES}Cut-It™ by Offtime Roadmap® v.{version()}@{tag()}")
        
        # Applying custom changes to GUI
        self.addDistroDetails()
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
        
        self.delete_card = QtWidgets.QPushButton()
        self.delete_card.setObjectName(u"delete_card")
        self.delete_card.setMinimumSize(QSize(15, 15))
        self.delete_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.delete_card)

        self.copy = QtWidgets.QPushButton()
        self.copy.setObjectName(u"copy")
        self.copy.setMinimumSize(QSize(15, 15))
        self.copy.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.copy)
        
        self.save_card = QtWidgets.QPushButton()
        self.save_card.setObjectName(u"save_card")
        self.save_card.setMinimumSize(QSize(15, 15))
        self.save_card.setFocusPolicy(QtCore.Qt.NoFocus)
        self.horizontalLayout.addWidget(self.save_card)
        
    def addAttrs(self):
        """
            Adds in misc. GUI attributes
        """

        # Set theme-appropriate tooltip background
        if self.isLight:
            self.setStyleSheet("QToolTip { color: #616161; background-color: #f2f2f2; border: 0px;}")
        
        else:
            self.setStyleSheet("QToolTip { color: #f2f2f2; background-color: #616161; border: 0px;}")

        # Adding ToolTips
        self.autocut.setToolTip("""
        <code>AutoCut</code> is a feature that saves time getting card details!<br><br>
        - If the <code>AutoCite</code> checkbox (to the left) is activated, it will add an MLA & 
        Debate-style citation to your card.<br><br>
        - If the <code>AutoPoll</code> checkbox to the left is activated, it will add the text 
        of the website to your card.<br><br>
        - You need to select which (or both) of these options you want prior to 
        clicking the button.<br><br>
        - Make sure you enter any card details in the 
        <code>Card Information</code> section prior to AutoCutting - <em>they won't fill in afterwards</em>!
        """)

        # Setting up message box
        self.msg.setCurrentFont(QtGui.QFont("Roboto"))
        self.msg.insertHtml("Welcome to Cut-It! Hover over an item for a few seconds to get a description, or read the docs at: <a>docs.cutit.cards!")

        # Adding Icons
        self.autocut.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/cut_icon.png')))
        self.open_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/open_icon.png')))
        self.delete_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/delete_icon.png')))
        self.copy.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/copy_icon.png')))
        self.save_card.setIcon(QtGui.QIcon(PATH.get('Cut-It/images/save_icon.png')))

    def addDistroDetails(self) -> str:
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

        self.distro.setText(distroDetails)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    gui = GUI(isLight=False)
    gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())