from docx import Document
from htmldocx import HtmlToDocx
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from api.resource import PATH
from PyQt5.QtWidgets import QApplication
import sys
import time

# TODO have PrintPDF inherit from QBrowser
class PrintPDF(object):

    def __init__(self, html, save_path):
        
        self.html = html
        self.save_path = save_path

    def setupUi(self, Widget):
        self.widget = Widget
        self.initUI()

    def initUI(self):

        vbox = QVBoxLayout(self.widget)

        self.webEngineView = QWebEngineView()
        self.webEngineView.setGeometry(500,500,500,500)
        self.getFile()

        vbox.addWidget(self.webEngineView)

        self.widget.setLayout(vbox)

        self.widget.setGeometry(300, 300, 350, 250)
        self.widget.setWindowTitle('Save as PDF - Cut-It™')
        self.widget.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        self.widget.show()

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
        self.widget.close()

class make:

    @staticmethod
    def html(html, filename):
        with open(filename, 'w') as f:
            f.write(html)

    @staticmethod
    def docx(html, filename):

        document = Document()

        new_parser = HtmlToDocx()

        new_parser.add_html_to_document(html, document)

        document.save(filename)

    @staticmethod
    def pdf(html, filename):
        
        if filename.endswith('.pdf') == False:
            html += '.pdf'

        return make.convert_html_to_pdf(html, filename)

    @staticmethod
    def convert_html_to_pdf(source_html, output_filename):

        with open(output_filename, 'w') as f:
            f.write(source_html)
    
        # result_file = open(output_filename, "w+b")

        # pisa_status = pisa.CreatePDF(
        #         source_html,                
        #         dest=result_file)           

        # result_file.close()                 

        # if pisa_status.err == None:
        #     return True

        # else:
        #     return False
