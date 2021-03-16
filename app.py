from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
import sys
import os
import klembord
from bs4 import BeautifulSoup
from api.resource import PATH
from api.version import check
from api.citer import cite
from api.texter import text
from api.texter import news
from api.export import make
from api.auth_tools import tools
from pynotifier import Notification

# FIXME buttons/shortcuts not connecting in slave window
# TODO add OSX clipboard rich support https://pypi.org/project/richxerox/ 
# TODO font selector (css not recognized), https://forum.qt.io/topic/35999/solved-qplaintextedit-how-to-change-the-font-to-be-monospaced/7 
# TODO threading in cut_it
# TODO break up resources folder into images and code

class MainGUI(object):

    def setupUi(self, MainWindow):
        
        self.settings_window = None

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

        #Setting up shortcuts
        self.cutit_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+S'), self.evidence_box)
        self.cutit_shortcut.activated.connect(self.cut_it)

        self.autocite_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Shift+S'), self.evidence_box)
        self.autocite_shortcut.activated.connect(self.enableAutocite)

        self.autopoll_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Alt+S'), self.evidence_box)
        self.autopoll_shortcut.activated.connect(self.enableAutopoll)

        self.AIO_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+Shift+X'), self.evidence_box)
        self.AIO_shortcut.activated.connect(self.enableAIO)

        self.toPDF_shortcut = QShortcut(QtGui.QKeySequence('Ctrl+P'), self.evidence_box)
        self.toPDF_shortcut.activated.connect(self.print)

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
                             "QPushButton:hover:!pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(140, 84, 255);"
                             "border: 1px solid rgb(140, 84, 255);"
                             "border-radius:10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(169, 204, 227);"
                             "border: 1px solid rgb(169, 204, 227);"
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

        #Setting up settings button
        
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(150, 270, 141, 21))
        self.settings_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "}"
                             "QPushButton:hover:!pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(140, 84, 255);"
                             "border: 1px solid rgb(140, 84, 255);"
                             "border-radius:10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(169, 204, 227);"
                             "border: 1px solid rgb(169, 204, 227);"
                             "border-radius:10px;"
                             "}"
                             ) 

        self.settings_button.setObjectName("cutit_button")
        self.settings_button.clicked.connect(self.settings)

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
        self.settings_button.raise_()

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
        html = '<body style="font-family: Times">' + html + '</body>'
        text = str(soup.text)

        return [text, html]

    def print(self):
        
        # Getting Current Dir
        startingDir = os.getcwd()

        # Getting User Input for Target Dir
        destDir = QFileDialog.getExistingDirectory(None, 
                                                'Folder To Save In', 
                                                startingDir, 
                                                QFileDialog.ShowDirsOnly)

        # Getting HTML, filename
        html = self.toHTML()[1] 
        filename = destDir + '/' + self.warrant_input.text() + '.pdf'
        
        # Making PDF
        try:
            make.pdf(html, filename)
        
        except Exception:
            pass

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

    def settings(self):
        # if self.settings_window is None:
        #     self.settings_window = QtWidgets.QMainWindow()
        #     auth_win = AuthWindow() # needs to be a SettingsWindow
        #     auth_win.setupUi(self.settings_window)

        # self.settings_window.show()
        pass

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
        self.settings_button.setText(_translate("MainWindow", "Settings"))
        self.autocite_box.setText(_translate("MainWindow", "AutoCite"))
        self.OTR_brand_label.setText(_translate("MainWindow", "Cut-It™ by Offtime Roadmap, LLC"))
        self.version.setText(_translate("MainWindow", "v.0.1.3"))
        self.autopoll_box.setText(_translate("MainWindow", "AutoPoll"))

class AuthWindow(object):

    def setupUi(self, MainWindow):
        
        self.main_window = None

        #Setting up MainWindow
        MainWindow.setObjectName("MainWindow")
        self.mw = MainWindow
        MainWindow.setFixedSize(421, 319)
        MainWindow.setStyleSheet("background-color: #130e2c;")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        
        #Setting up centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Setting up auth label
        self.auth_label = QtWidgets.QLabel(self.centralwidget)
        self.auth_label.setGeometry(QtCore.QRect(30, 10, 361, 51))
        self.auth_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255);")
        self.auth_label.setObjectName("auth_label")

        #Setting up email label
        self.email_label = QtWidgets.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(20, 70, 91, 21))
        self.email_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font: 10pt;\n"
        "")
        self.email_label.setObjectName("email_label") 

        #Setting up email input
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(20, 100, 381, 31))
        self.email_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")

        #Setting up pass label
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(20, 140, 91, 21))
        self.pass_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font: 10pt;\n"
        "")
        self.pass_label.setObjectName("pass_label")
                
        #Setting up pass input
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(20, 170, 381, 31))
        self.pass_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.pass_input.setText("")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        
        #Setting up sign up button
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(20, 220, 181, 23))
        self.sign_up_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "}"
                             "QPushButton:hover:!pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(140, 84, 255);"
                             "border: 1px solid rgb(140, 84, 255);"
                             "border-radius:10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(169, 204, 227);"
                             "border: 1px solid rgb(169, 204, 227);"
                             "border-radius:10px;"
                             "}"
                             ) 
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_up_button.clicked.connect(self.sign_up)

        #Setting up log in button
        self.log_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_button.setGeometry(QtCore.QRect(220, 220, 181, 23))
        self.log_in_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "}"
                             "QPushButton:hover:!pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(140, 84, 255);"
                             "border: 1px solid rgb(140, 84, 255);"
                             "border-radius:10px;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #130e2c;"
                             "color: rgb(169, 204, 227);"
                             "border: 1px solid rgb(169, 204, 227);"
                             "border-radius:10px;"
                             "}"
                             )  
        self.log_in_button.setObjectName("log_in_button")
        self.log_in_button.clicked.connect(self.log_in)

        #Setting up msg box
        self.msg_box = QtWidgets.QLabel(self.centralwidget)
        self.msg_box.setObjectName("msg_box")
        self.msg_box.setGeometry(QtCore.QRect(20, 250, 381, 61))
        self.msg_box.setStyleSheet("color: rgb(169, 204, 227);\n""font: 9pt;\n")

        #Misc
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def log_in(self):

        EMAIL = self.email_input.text()
        PASSWORD = self.pass_input.text()

        tools.log_out(EMAIL, PASSWORD)

        if tools.log_in(EMAIL, PASSWORD) == True:

            if self.main_window is None:
                self.main_window = QtWidgets.QMainWindow()
                main_win = MainGUI() 
                main_win.setupUi(self.main_window)

            self.main_window.show()

            self.mw.close()

        else:
            Notification(
                title='Login Error!',
                description='You entered an unknown username/password combination!',
                icon_path=PATH.get("resources/otr_icon.ico"), 
                duration=5,                             
                urgency=Notification.URGENCY_NORMAL
            ).send()
                
    def sign_up(self):

        EMAIL = self.email_input.text()
        PASSWORD = self.pass_input.text()

        if tools.sign_up(EMAIL, PASSWORD) == True:
            Notification(
                title='Sign Up Success!',
                description='Check your email to verify your account then come back and Log In.',
                icon_path=PATH.get("resources/otr_icon.ico"), 
                duration=5,                             
                urgency=Notification.URGENCY_NORMAL
            ).send()

        else:
            Notification(
                title='Sign Up Error!',
                description="""
                That email could already be in use, or your password does not meet our requirements (8 characters long, 1 uppercase, 1 number).
                """,
                icon_path=PATH.get("resources/otr_icon.ico"), 
                duration=5,                             
                urgency=Notification.URGENCY_NORMAL
            ).send()

    def log_out(self):

        EMAIL = self.email_input.text()
        PASSWORD = self.pass_input.text()

        tools.log_out(EMAIL, PASSWORD)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Authenticate - Cut-It™ by Offtime Roadmap®"))
        self.auth_label.setText(_translate("MainWindow", "Please Authenticate Below"))
        self.sign_up_button.setText(_translate("MainWindow", "Sign Up"))
        self.log_in_button.setText(_translate("MainWindow", "Log In"))
        self.email_label.setText(_translate("MainWindow", "Email: "))
        self.pass_label.setText(_translate("MainWindow", "Password: "))
        welcome_msg = """Welcome! Please sign up with a valid email and password\n(min. 8 characters, 1 uppercase, 1 number) or log in.
        """
        self.msg_box.setText(_translate("MainWindow", welcome_msg))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AuthWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())