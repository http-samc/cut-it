"""
    - Logic to export a card (in HTML form) to various filetypes (docx, pdf)
    - TODO: add docx support
    - FIXME: PDF builder with QWebEngineView not working in Binary
"""

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from utils.resource import PATH
from PyQt5 import QtGui
import PyQt5
import time
import sys

class PrintPDF(QWidget):

    def __init__(self, html, save_path, parent = None):
        super().__init__(parent=parent)
        self.html = html
        self.save_path = save_path
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        self.webEngineView.setGeometry(500,500,500,500)
        self.getFile()

        vbox.addWidget(self.webEngineView)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.show()

    def getFile(self):
        self.webEngineView.setHtml(self.html)
        self.webEngineView.loadFinished.connect(self.save)

    def save(self):
        page = self.webEngineView.page()
        page.printToPdf(self.save_path)
        page.pdfPrintingFinished.connect(self.finished)
    
    def finished(self):
        self.webEngineView.close()
        time.sleep(1)
        self.close()

if __name__ == "__main__":
    
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    p = PrintPDF("""
    <body style="font-family: Times New Roman"><p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:bold; text-decoration: underline; background-color:#00ffff;">big</span> <span style=" font-weight:bold;">normal</span> <span style=" font-size:2pt;">small</span></p></body>""", r"C:/Users/chitg/Test.pdf")
    sys.exit(app.exec_())