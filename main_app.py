from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5.QtCore import *
import sys
import klembord
from api.resource import PATH
from api.version import check
from api.citer import cite
from api.texter import text
from api.texter import news
from bs4 import BeautifulSoup

# TODO add OSX clipboard rich support https://pypi.org/project/richxerox/ 
# TODO font selector (css not recognized), https://forum.qt.io/topic/35999/solved-qplaintextedit-how-to-change-the-font-to-be-monospaced/7 
# TODO threading in cut_it
# TODO break up resources folder into images and code

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        #Setting up MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 580)
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")

        #Setting up centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Setting up evidence box
        self.evidence_box = QPlainTextEdit(self.centralwidget)

        self.cutit_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+S'), self.evidence_box)
        self.cutit_shortcut.activated.connect(self.cut_it)

        self.autocite_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Shift+S'), self.evidence_box)
        self.autocite_shortcut.activated.connect(self.enableAutocite)

        self.autopoll_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Alt+S'), self.evidence_box)
        self.autopoll_shortcut.activated.connect(self.enableAutopoll)

        self.AIO_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Shift+X'), self.evidence_box)
        self.AIO_shortcut.activated.connect(self.enableAIO)

        self.evidence_box.setGeometry(QtCore.QRect(330, 20, 541, 481))
        self.evidence_box.setObjectName("evidence_box")
        self.evidence_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:10px;\n"
        "")

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setWeight(10)
        self.evidence_box.setFont(font)

        #Setting up tagline input
        self.warrant_input = QtWidgets.QLineEdit(self.centralwidget)
        self.warrant_input.setGeometry(QtCore.QRect(10, 80, 281, 21))
        self.warrant_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;\n"
        "")
        self.warrant_input.setObjectName("warrant_input")

        #Setting up tagline label
        self.warrant_label = QtWidgets.QLabel(self.centralwidget)
        self.warrant_label.setGeometry(QtCore.QRect(10, 60, 221, 16))
        self.warrant_label.setStyleSheet("color: rgb(169, 204, 227)")
        self.warrant_label.setObjectName("warrant_label")

        #Setting up cite input
        self.cite_input = QtWidgets.QLineEdit(self.centralwidget)
        self.cite_input.setGeometry(QtCore.QRect(10, 130, 281, 21))
        self.cite_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;\n"
        "")
        self.cite_input.setObjectName("cite_input")

        #Setting up cite label
        self.cite_label = QtWidgets.QLabel(self.centralwidget)
        self.cite_label.setGeometry(QtCore.QRect(10, 110, 221, 16))
        self.cite_label.setStyleSheet("color: rgb(169, 204, 227)")
        self.cite_label.setObjectName("cite_label")

        #Setting up creds input
        self.creds_input = QtWidgets.QLineEdit(self.centralwidget)
        self.creds_input.setGeometry(QtCore.QRect(10, 180, 281, 21))
        self.creds_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;\n"
        "")
        self.creds_input.setObjectName("creds_input")

        #Setting up creds label
        self.creds_label = QtWidgets.QLabel(self.centralwidget)
        self.creds_label.setGeometry(QtCore.QRect(10, 160, 221, 16))
        self.creds_label.setStyleSheet("color: rgb(169, 204, 227)")
        self.creds_label.setObjectName("creds_label")

        #Setting up URL input
        self.link_input = QtWidgets.QLineEdit(self.centralwidget)
        self.link_input.setGeometry(QtCore.QRect(10, 230, 281, 21))
        self.link_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"    
        "border-radius:5px;")
        self.link_input.setText("")
        self.link_input.setObjectName("link_input")

        #Setting up URL label
        self.link_label = QtWidgets.QLabel(self.centralwidget)
        self.link_label.setGeometry(QtCore.QRect(10, 210, 221, 16))
        self.link_label.setStyleSheet("color: rgb(169, 204, 227)")
        self.link_label.setObjectName("link_label")

        #Setting up card label
        self.card_info_label = QtWidgets.QLabel(self.centralwidget)
        self.card_info_label.setGeometry(QtCore.QRect(10, 10, 261, 41))

        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.card_info_label.setFont(font)

        self.card_info_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255)")
        self.card_info_label.setObjectName("card_info_label")

        #Setting up cut-it button
        self.cutit_button = QtWidgets.QPushButton(self.centralwidget)
        self.cutit_button.setGeometry(QtCore.QRect(490, 530, 221, 23))
        self.cutit_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #ffffff;"
                             "border-radius:10px;"
                             "}"
                             ) 

        self.cutit_button.setObjectName("cutit_button")
        self.cutit_button.clicked.connect(self.cut_it)

        #Setting up autocite checkbox
        self.autocite_box = QtWidgets.QCheckBox(self.centralwidget)
        self.autocite_box.setGeometry(QtCore.QRect(10, 270, 70, 17))
        self.autocite_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.autocite_box.setObjectName("autocite_box")

        #Setting up autopoll checkbox
        self.autopoll_box = QtWidgets.QCheckBox(self.centralwidget)
        self.autopoll_box.setGeometry(QtCore.QRect(80, 270, 70, 17))
        self.autopoll_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.autopoll_box.setObjectName("cite_box_2") 

        #Adding Offtime Logo
        self.OTR_logo = QtWidgets.QLabel(self.centralwidget)
        self.OTR_logo.setGeometry(QtCore.QRect(-30, 260, 441, 311))
        self.OTR_logo.setStyleSheet("")
        self.OTR_logo.setText("")
        self.OTR_logo.setPixmap(QtGui.QPixmap(PATH.get("resources/otr_logo.png")))
        self.OTR_logo.setScaledContents(True)
        self.OTR_logo.setObjectName("OTR_logo")

        #Adding Offtime branding
        self.OTR_brand_label = QtWidgets.QLabel(self.centralwidget)
        self.OTR_brand_label.setGeometry(QtCore.QRect(50, 490, 171, 31))
        self.OTR_brand_label.setStyleSheet("color: rgb(140, 84, 255);\n"
        "")
        self.OTR_brand_label.setObjectName("OTR_brand_label")

        #Adding version number
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(110, 520, 47, 13))
        self.version.setStyleSheet("color: rgb(140, 84, 255)")
        self.version.setObjectName("version")

        #Raising all elems
        self.OTR_logo.raise_()
        self.evidence_box.raise_()
        self.warrant_input.raise_()
        self.cite_input.raise_()
        self.creds_input.raise_()
        self.link_input.raise_()
        self.warrant_label.raise_()
        self.cite_label.raise_()
        self.creds_label.raise_()
        self.link_label.raise_()
        self.card_info_label.raise_()
        self.cutit_button.raise_()
        self.autocite_box.raise_()
        self.OTR_brand_label.raise_()
        self.version.raise_()
        self.autopoll_box.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def toHTML(self):
        doc = self.evidence_box.document()
        soup = BeautifulSoup(doc.toHtml(), 'html.parser')
        html = str(soup.find('p'))
        html = html.replace('600', 'bold')

        text = str(soup.text)

        return [text, html]

    def enableAutocite(self):
        self.autocite_box.setCheckState(True)
        self.cut_it()

    def enableAutopoll(self):
        self.autopoll_box.setCheckState(True)
        self.cut_it()

    def enableAIO(self):
        self.autocite_box.setCheckState(True)
        self.autopoll_box.setCheckState(True)
        self.cut_it()

    def cut_it(self):

        URL = self.link_input.text()
        
        citation = f"""
        <p>
        """

        #Both Checked
        if (self.autocite_box.isChecked() is True) and (self.autopoll_box.isChecked() is True):

            #De-checking both boxes
            self.autocite_box.setCheckState(False)
            self.autopoll_box.setCheckState(False)

            #Inputting Cite
            CREDS = self.creds_input.text()
            TAG = self.warrant_input.text()

            c = cite(URL)
            citation_data_debate = c.debate()
            citation_mla = c.mla()

            if TAG != "":
                citation += f"""
                <span style='background-color: yellow; font-size: 12pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """
            
            citation += f"""
            <span style='background-color: cyan; font-size: 12pt;'><u><strong>
                {citation_data_debate[0]} '{citation_data_debate[1]}<br>
            </strong></u></span>
            """

            if CREDS != "":
                citation += f"""
                <i>
                {CREDS}<br>
                </i>
                """
    
            citation += f"""
            {citation_data_debate[2]} • {citation_data_debate[3]}<br>
            {citation_mla}<br><br>
            """

            #Inputting Article Text
            if "nytimes.com" in URL:
                article = text.get(URL)
            else:
                article = news.paper(URL)
            citation += article + "</p>"

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation)  

        #AutoCite checked Only
        elif self.autocite_box.isChecked() is True:
            
            #De-checking box
            self.autocite_box.setCheckState(False)

            #Inputting Cite
            CREDS = self.creds_input.text()
            TAG = self.warrant_input.text()

            c = cite(URL)
            citation_data_debate = c.debate()
            citation_mla = c.mla()

            if TAG != "":
                citation += f"""
                <span style='background-color: yellow; font-size: 12pt;'><u><strong>
                    {TAG}
                </strong></u></span><br>
                """
            
            citation += f"""
            <span style='background-color: cyan; font-size: 12pt;'><u><strong>
                {citation_data_debate[0]} '{citation_data_debate[1]}<br>
            </strong></u></span>
            """

            if CREDS != "":
                citation += f"""
                <i>
                {CREDS}<br>
                </i>
                """
    
            citation += f"""
            {citation_data_debate[2]} • {citation_data_debate[3]}<br>
            {citation_mla}<br><br>
            </p>
            """

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation) 

        #Autopoll Checked Only
        elif self.autopoll_box.isChecked() is True:
            
            #De-checking box
            self.autopoll_box.setCheckState(False)

            #Getting article, inputting it
            if "nytimes.com" in URL:
                article = text.get(URL)
            else:
                article = news.paper(URL)
            citation += article + "</p>"

            #Inserting Text
            cursor = self.evidence_box.textCursor()
            cursor.setPosition(0)
            cursor.insertHtml(citation)    
        
        self.emphasize()
        klembord.init()
        data = self.toHTML()
        klembord.set_with_rich_text(data[0], data[1])

    def emphasize(self):
        """
        bolds, highlights, underlines selected text
        """

        cursor = self.evidence_box.textCursor()

        if cursor.hasSelection():
            selection = cursor.selectedText()
            cursor.removeSelectedText()        
            formatted_selection = f"""<span style='background-color: cyan; font-size: 12pt;'><u><strong>{selection}</strong></u></span>"""
            cursor.insertHtml(formatted_selection)

    def highlight(self):
        """
        highlights selected text
        """

        # TODO: use cursor.selection().toHtml to get the HTML of the fragment and do double formatting

        cursor = self.evidence_box.textCursor()

        if cursor.hasSelection():
            selection = cursor.selectedText()
            cursor.removeSelectedText()        
            formatted_selection = f"<span style='background-color: cyan;'>{selection}</span>"
            cursor.insertHtml(formatted_selection)

    def bold(self):
        """
        bolds selected text
        """
        cursor = self.evidence_box.textCursor()

        if cursor.hasSelection():
            selection = cursor.selectedText()
            #cursor.removeSelectedText()        
            formatted_selection = f"<b>{selection}</b>"
            cursor.insertHtml(formatted_selection)

    def underline(self):
        """
        underlines selected text
        """
        cursor = self.evidence_box.textCursor()

        if cursor.hasSelection():
            selection = cursor.selectedText()
            cursor.removeSelectedText()        
            formatted_selection = f"<u>{selection}</u>"
            cursor.insertHtml(formatted_selection)
        
    def italic(self):
        """
        italicises selected text
        """
        
        cursor = self.evidence_box.textCursor()

        if cursor.hasSelection():
            selection = cursor.selectedText()
            cursor.removeSelectedText()        
            formatted_selection = f"<em>{selection}</em>"
            cursor.insertHtml(formatted_selection)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cut-It™ by Offtime Roadmap®"))
        self.evidence_box.appendHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.warrant_label.setText(_translate("MainWindow", "Tagline:"))
        self.cite_label.setText(_translate("MainWindow", "Cite:"))
        self.creds_label.setText(_translate("MainWindow", "Credentials:"))
        self.link_label.setText(_translate("MainWindow", "Link:"))
        self.card_info_label.setText(_translate("MainWindow", "Card Information: "))
        self.cutit_button.setText(_translate("MainWindow", "Cut-It"))
        self.autocite_box.setText(_translate("MainWindow", "AutoCite"))
        self.OTR_brand_label.setText(_translate("MainWindow", "Cut-It™ by Offtime Roadmap, LLC"))
        self.version.setText(_translate("MainWindow", "v.0.1.2"))
        self.autopoll_box.setText(_translate("MainWindow", "AutoPoll"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())