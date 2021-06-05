from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import QUrl
from PyQt5 import QtGui
from api.resource import PATH
import sys

class Browser:
    
    def __init__(self, title):
        self.title = title
        
    def setupUi(self, Widget):
        self.widget = Widget
        self.widget.setGeometry(800,500,500,630)
        self.initUI()
    
    def initUI(self):
        vbox = QVBoxLayout(self.widget)
        self.webEngineView = QWebEngineView()
        vbox.addWidget(self.webEngineView)
        self.widget.setWindowTitle('QWebEngineView')
        self.widget.setWindowTitle(self.title)
        self.widget.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))

    def show(self):
        self.widget.show()
        
    def setURL(self, URL):
        self.webEngineView.setUrl(QUrl(URL))
    
    def setHtml(self, HTML):
        self.webEngineView.setHtml(HTML)
    
def main():

    app = QApplication(sys.argv)
    widget = QWidget()
    browser = Browser()
    browser.setup_ui(widget)
    sys.exit(app.exec_())