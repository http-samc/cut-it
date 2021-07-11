import datetime
import sys

import chromedriver_autoinstaller
import qtmodern
from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from selenium import webdriver

from utils.resource import PATH
from utils.version_check import pollReleases

class Updater(QDialog):

    def __init__(self, parent=None, data=None) -> None:
        """
            Loads latest UI
        """

        super().__init__(parent=parent)

        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.FramelessWindowHint | Qt.Dialog | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setWindowIcon(QtGui.QIcon(PATH.get('images/otr_icon.png')))
        self.setFixedSize(800,600)
        self.parent = parent

        self.data = data if data else pollReleases()
        if not self.data: self.close(); return # no updates => close

        # Loading UI
        uic.loadUi('Cut-It/update.ui', self)

        self.addOptions()

    def addOptions(self) -> None:
        """Adds data about an update, if any"""

        # Beautify date
        date = datetime.datetime.strptime(self.data["date"], "%Y-%m-%dT%H:%M:%SZ")
        date = date.strftime('%b %d, %Y at %H:%M GMT')

        # Generate & set markdown str
        info: str = f'Version: `{self.data["name"]} ({date})`\n\nRequired: `{"Yes" if self.data["required"] else "No"}`\n\n---\n{self.data["desc"]}'
        self.info.setMarkdown(info)

        # Define our download URL
        self.download = self.data["download"]

        # If we req this update, set ignore text to 'exit' && force quit of entire program (nonex it)
        if self.data["required"]: self.ignore.setText("Exit Without Updating"); self.ignore.clicked.connect(self._quit)

        # Else if the update isn't req => set ignore to close the popup and allow cutit functionality
        else: self.ignore.clicked.connect(self._close)

        # Set the update button to get update
        self.update.clicked.connect(self.getUpdate)

    def getUpdate(self):
        """Opens download URL in Selenium Chrome"""

        chromedriver_autoinstaller.install()

        # Config browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f"--app={self.download}")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--window-size=600,400")
        chrome_options.add_experimental_option("detach", True)

        # Open it to download URI
        browser = webdriver.Chrome(options=chrome_options)

        # Quit program to allow downloaded updater to run
        self._quit()

    def _quit(self):
        quit()

    def _close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)#QtWidgets.QApplication(sys.argv)
    #qtmodern.styles.dark(app)
    gui = Updater()
    #gui = qtmodern.windows.ModernWindow(gui)
    gui.show()
    sys.exit(app.exec_())