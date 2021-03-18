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
from api.data import store

class AuthWindow(QMainWindow):
    
    def setupUi(self, MainWindow): 
        
        #Setting up MainWindow
        MainWindow.setObjectName("MainWindow")
        self.Auth_window = MainWindow
        MainWindow.setFixedSize(421, 317)
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
        self.msg_box.setGeometry(QtCore.QRect(20, 260, 381, 40))
        self.msg_box.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_box.setStyleSheet("QLabel"
                             "{"
                             "color: rgb(140, 84, 255);"
                             "font: 9pt;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "color: rgb(26, 82, 118);"
                             "font: 9pt;"
                             "}"
                             )

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

        if EMAIL.endswith("*"): 
            EMAIL = EMAIL.replace("*", "")
            tools.log_out(EMAIL, PASSWORD)

        if tools.log_in(EMAIL, PASSWORD) == True:
            store.init()
            store.add_login(EMAIL, PASSWORD)
            self.MainWin()

        else:
            self.msg_box.setText("Invalid Login! Try again.")
        
    def MainWin(self):
        
        self.Main_Window = QMainWindow()
        self.ui2 = MainWindow()
        self.ui2.setupUi(self.Main_Window)

        self.Main_Window.show()
        self.Auth_window.close()

    def sign_up(self):

        EMAIL = self.email_input.text()
        PASSWORD = self.pass_input.text()

        if tools.sign_up(EMAIL, PASSWORD) == True:
            self.msg_box.setText("Sign Up Success!\nCheck your email to verify your account then come back and Log In.")

        else:
            self.msg_box.setText("Sign Up Error!\nThat email could already be in use, or your password does not meet our requirements (8 characters long, 1 uppercase, 1 number).")

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

class MainWindow(object):

    def setupUi(self, MainWindow):
        
        self.settings_window = None
        store.init()
        
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
        font.setFamily(store.get_font())
        font.setWeight(int(store.fsnt()))
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
        html = f'<body style="font-family: {store.get_font()}">' + html + '</body>'
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
            formatted_selection = f"""<span style='background-color: {store.phc()}; font-size: {store.fspe()}pt;'><u><strong>{selection}</strong></u></span>"""
            cursor.insertHtml(formatted_selection)

    def highlight(self):
        """
        highlights selected text
        """

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

        self.Settings_Window = QMainWindow()
        self.ui2 = SettingsWindow()
        self.ui2.setupUi(self.Settings_Window)

        self.Settings_Window.show()

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

class SettingsWindow(object):

    def setupUi(self, MainWindow):

        #Setting up Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        MainWindow.setFixedSize(221, 299)
        MainWindow.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")

        #Setting up Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Setting up settings label
        self.settings_label = QtWidgets.QLabel(self.centralwidget)
        self.settings_label.setGeometry(QtCore.QRect(60, 0, 111, 51))
        self.settings_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255);")
        self.settings_label.setObjectName("settings_label")

        #Setting up Preferences button
        self.preferences_button = QtWidgets.QPushButton(self.centralwidget)
        self.preferences_button.setGeometry(QtCore.QRect(20, 60, 181, 23))
        self.preferences_button.setStyleSheet("QPushButton"
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
        self.preferences_button.setObjectName("preferences_button")
        self.preferences_button.clicked.connect(self.open_prefs)

        #Setting up shortcuts button
        self.shortcuts_button = QtWidgets.QPushButton(self.centralwidget)
        self.shortcuts_button.setGeometry(QtCore.QRect(20, 100, 181, 23))
        self.shortcuts_button.setStyleSheet("QPushButton"
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
        self.shortcuts_button.setObjectName("shortcuts_button")
        self.shortcuts_button.clicked.connect(self.open_shorts)

        #Setting up updates button
        self.updates_button = QtWidgets.QPushButton(self.centralwidget)
        self.updates_button.setGeometry(QtCore.QRect(20, 140, 181, 23))
        self.updates_button.setStyleSheet("QPushButton"
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
        self.updates_button.setObjectName("updates_button")

        #Setting up log out button
        self.log_out_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_out_button.setGeometry(QtCore.QRect(20, 180, 181, 23))
        self.log_out_button.setStyleSheet("QPushButton"
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
        self.log_out_button.setObjectName("log_out_button")
        self.log_out_button.clicked.connect(self.log_out)

        #Setting up window size box
        self.window_size_box = QtWidgets.QCheckBox(self.centralwidget)
        self.window_size_box.setGeometry(QtCore.QRect(50, 220, 111, 21))
        self.window_size_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.window_size_box.setObjectName("window_size_box")

        #setting up stay logged in box
        self.stay_logged_in_box = QtWidgets.QCheckBox(self.centralwidget)
        self.stay_logged_in_box.setGeometry(QtCore.QRect(50, 250, 111, 21))
        self.stay_logged_in_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.stay_logged_in_box.setObjectName("stay_logged_in_box")

        #Misc
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def open_prefs(self):
        
        self.Pref_Window = QMainWindow()
        self.ui2 = PreferencesWindow()
        self.ui2.setupUi(self.Pref_Window)

        self.Pref_Window.show()

    def open_shorts(self):
        self.Shorts_Window = QMainWindow()
        self.ui2 = ShortcutsWindow()
        self.ui2.setupUi(self.Shorts_Window)

        self.Shorts_Window.show()
    
    def updates(self):
        pass

    def log_out(self):
        store.init()
        store.log_out()
        quit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cut-It™"))
        self.settings_label.setText(_translate("MainWindow", "Settings"))
        self.preferences_button.setText(_translate("MainWindow", "Preferences"))
        self.shortcuts_button.setText(_translate("MainWindow", "Shortcuts"))
        self.updates_button.setText(_translate("MainWindow", "Updates"))
        self.log_out_button.setText(_translate("MainWindow", "Log Out"))
        self.window_size_box.setText(_translate("MainWindow", "Lock Window Size"))
        self.stay_logged_in_box.setText(_translate("MainWindow", "Stay Logged In"))

class PreferencesWindow(object):

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        MainWindow.setFixedSize(561, 502)
        MainWindow.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.primary_highlight_box = QtWidgets.QComboBox(self.centralwidget)
        self.primary_highlight_box.setGeometry(QtCore.QRect(270, 130, 281, 22))
        self.primary_highlight_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.primary_highlight_box.setObjectName("primary_highlight_box")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")

        self.options_label = QtWidgets.QLabel(self.centralwidget)
        self.options_label.setGeometry(QtCore.QRect(270, 50, 281, 21))
        self.options_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.options_label.setObjectName("options_label")

        self.set_preferences_label = QtWidgets.QLabel(self.centralwidget)
        self.set_preferences_label.setGeometry(QtCore.QRect(10, 0, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.set_preferences_label.setFont(font)
        self.set_preferences_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255)")
        self.set_preferences_label.setObjectName("set_preferences_label")

        self.primary_emphasis_box = QtWidgets.QComboBox(self.centralwidget)
        self.primary_emphasis_box.setGeometry(QtCore.QRect(270, 330, 281, 22))
        self.primary_emphasis_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.primary_emphasis_box.setObjectName("primary_emphasis_box")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")

        self.font_size_cut_box = QtWidgets.QComboBox(self.centralwidget)
        self.font_size_cut_box.setGeometry(QtCore.QRect(270, 210, 281, 22))
        self.font_size_cut_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.font_size_cut_box.setObjectName("font_size_cut_box")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(180, 450, 221, 23))
        self.save_button.setStyleSheet("QPushButton"
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
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_config)

        self.category_label = QtWidgets.QLabel(self.centralwidget)
        self.category_label.setGeometry(QtCore.QRect(10, 50, 241, 21))
        self.category_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.category_label.setObjectName("category_label")

        self.font_label = QtWidgets.QLabel(self.centralwidget)
        self.font_label.setGeometry(QtCore.QRect(10, 90, 241, 21))
        self.font_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_label.setObjectName("font_label")

        self.primary_highlight_label = QtWidgets.QLabel(self.centralwidget)
        self.primary_highlight_label.setGeometry(QtCore.QRect(10, 130, 241, 21))
        self.primary_highlight_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.primary_highlight_label.setObjectName("primary_highlight_label")

        self.font_size_cut_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_cut_label.setGeometry(QtCore.QRect(10, 210, 241, 21))
        self.font_size_cut_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_cut_label.setObjectName("font_size_cut_label")

        self.font_size_normal_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_normal_label.setGeometry(QtCore.QRect(10, 250, 241, 21))
        self.font_size_normal_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_normal_label.setObjectName("font_size_normal_label")

        self.font_size_min_label = QtWidgets.QLabel(self.centralwidget)
        self.font_size_min_label.setGeometry(QtCore.QRect(10, 290, 241, 21))
        self.font_size_min_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_min_label.setObjectName("font_size_min_label")

        self.primary_emphasis_label = QtWidgets.QLabel(self.centralwidget)
        self.primary_emphasis_label.setGeometry(QtCore.QRect(10, 330, 241, 21))
        self.primary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.primary_emphasis_label.setObjectName("primary_emphasis_label")

        self.secondary_emphasis_label = QtWidgets.QLabel(self.centralwidget)
        self.secondary_emphasis_label.setGeometry(QtCore.QRect(10, 370, 241, 21))
        self.secondary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.secondary_emphasis_label.setObjectName("secondary_emphasis_label")

        self.tertiary_emphasis_label = QtWidgets.QLabel(self.centralwidget)
        self.tertiary_emphasis_label.setGeometry(QtCore.QRect(10, 410, 241, 21))
        self.tertiary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.tertiary_emphasis_label.setObjectName("tertiary_emphasis_label")

        self.secondary_highlight_label = QtWidgets.QLabel(self.centralwidget)
        self.secondary_highlight_label.setGeometry(QtCore.QRect(10, 170, 241, 21))
        self.secondary_highlight_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.secondary_highlight_label.setObjectName("secondary_highlight_label")

        self.secondary_highlight_box = QtWidgets.QComboBox(self.centralwidget)
        self.secondary_highlight_box.setGeometry(QtCore.QRect(270, 170, 281, 22))
        self.secondary_highlight_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.secondary_highlight_box.setObjectName("secondary_highlight_box")

        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.font_size_normal_box = QtWidgets.QComboBox(self.centralwidget)
        self.font_size_normal_box.setGeometry(QtCore.QRect(270, 250, 281, 22))
        self.font_size_normal_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.font_size_normal_box.setObjectName("font_size_normal_box")

        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_min_box = QtWidgets.QComboBox(self.centralwidget)
        self.font_size_min_box.setGeometry(QtCore.QRect(270, 290, 281, 22))
        self.font_size_min_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.font_size_min_box.setObjectName("font_size_min_box")
        
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")

        self.secondary_emphasis_box = QtWidgets.QComboBox(self.centralwidget)
        self.secondary_emphasis_box.setGeometry(QtCore.QRect(270, 370, 281, 22))
        self.secondary_emphasis_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.secondary_emphasis_box.setObjectName("secondary_emphasis_box")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.tertiary_emphasis_box = QtWidgets.QComboBox(self.centralwidget)
        self.tertiary_emphasis_box.setGeometry(QtCore.QRect(270, 410, 281, 22))
        self.tertiary_emphasis_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.tertiary_emphasis_box.setObjectName("tertiary_emphasis_box")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(270, 90, 281, 22))
        self.fontComboBox.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.fontComboBox.setObjectName("fontComboBox")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_config()

    def load_config(self):

        store.init()
        data = store.getData()["settings"]["preferences"]

        self.fontComboBox.setCurrentText(data["Font"])
        self.primary_highlight_box.setCurrentText(data["Primary Highlight Color"])
        self.secondary_highlight_box.setCurrentText(data["Secondary Highlight Color"])
        self.font_size_cut_box.setCurrentText(data["Font Size of Primary Emphasis"])
        self.font_size_normal_box.setCurrentText(data["Font Size of Normal Text"])
        self.font_size_min_box.setCurrentText(data["Font Size of Minimized Text"])
        self.primary_emphasis_box.setCurrentText(data["Primary Emphasis Settings"])
        self.secondary_emphasis_box.setCurrentText(data["Secondary Emphasis Settings"])
        self.tertiary_emphasis_box.setCurrentText(data["Tertiary Emphasis Settings"])

    def save_config(self):

        data = {
            "Font" : self.fontComboBox.currentText(),
            "Primary Highlight Color" : self.primary_highlight_box.currentText(),
            "Secondary Highlight Color" : self.secondary_highlight_box.currentText(),
            "Font Size of Primary Emphasis" : self.font_size_cut_box.currentText(),
            "Font Size of Normal Text" : self.font_size_normal_box.currentText(),
            "Font Size of Minimized Text" : self.font_size_min_box.currentText(),
            "Primary Emphasis Settings" : self.primary_emphasis_box.currentText(),
            "Secondary Emphasis Settings" : self.secondary_emphasis_box.currentText(),
            "Tertiary Emphasis Settings" : self.tertiary_emphasis_box.currentText(),
        }
        
        store.init()
        store.add_prefs(data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Set Preferences - Cut-It™"))
        self.primary_highlight_box.setItemText(0, _translate("MainWindow", "Cyan"))
        self.primary_highlight_box.setItemText(1, _translate("MainWindow", "Green"))
        self.primary_highlight_box.setItemText(2, _translate("MainWindow", "Magenta"))
        self.primary_highlight_box.setItemText(3, _translate("MainWindow", "Blue"))
        self.primary_highlight_box.setItemText(4, _translate("MainWindow", "Purple"))
        self.primary_highlight_box.setItemText(5, _translate("MainWindow", "Yellow"))
        self.options_label.setText(_translate("MainWindow", "Options"))
        self.set_preferences_label.setText(_translate("MainWindow", "Set Preferences:"))
        self.primary_emphasis_box.setItemText(0, _translate("MainWindow", "Bold + Underline + Highlight (Primary)"))
        self.primary_emphasis_box.setItemText(1, _translate("MainWindow", "Bold + Underline + Highlight (Primary) + Italicized"))
        self.primary_emphasis_box.setItemText(2, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.primary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.primary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold"))
        self.primary_emphasis_box.setItemText(5, _translate("MainWindow", "Underline"))
        self.primary_emphasis_box.setItemText(6, _translate("MainWindow", "Italicized"))
        self.font_size_cut_box.setItemText(0, _translate("MainWindow", "12"))
        self.font_size_cut_box.setItemText(1, _translate("MainWindow", "2"))
        self.font_size_cut_box.setItemText(2, _translate("MainWindow", "4"))
        self.font_size_cut_box.setItemText(3, _translate("MainWindow", "6"))
        self.font_size_cut_box.setItemText(4, _translate("MainWindow", "8"))
        self.font_size_cut_box.setItemText(5, _translate("MainWindow", "10"))
        self.font_size_cut_box.setItemText(6, _translate("MainWindow", "11"))
        self.font_size_cut_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_cut_box.setItemText(8, _translate("MainWindow", "16"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.category_label.setText(_translate("MainWindow", "Category"))
        self.font_label.setText(_translate("MainWindow", "Font"))
        self.primary_highlight_label.setText(_translate("MainWindow", "Primary Highlight Color"))
        self.font_size_cut_label.setText(_translate("MainWindow", "Font Size of Primary Emphasis"))
        self.font_size_normal_label.setText(_translate("MainWindow", "Font Size of Normal Text"))
        self.font_size_min_label.setText(_translate("MainWindow", "Font Size of Minimized Text"))
        self.primary_emphasis_label.setText(_translate("MainWindow", "Primary Emphasis Settings"))
        self.secondary_emphasis_label.setText(_translate("MainWindow", "Secondary Emphasis Settings"))
        self.tertiary_emphasis_label.setText(_translate("MainWindow", "Tertiary Emphasis Settings"))
        self.secondary_highlight_label.setText(_translate("MainWindow", "Secondary Highlight Color"))
        self.secondary_highlight_box.setItemText(0, _translate("MainWindow", "Green"))
        self.secondary_highlight_box.setItemText(1, _translate("MainWindow", "Cyan"))
        self.secondary_highlight_box.setItemText(2, _translate("MainWindow", "Magenta"))
        self.secondary_highlight_box.setItemText(3, _translate("MainWindow", "Blue"))
        self.secondary_highlight_box.setItemText(4, _translate("MainWindow", "Purple"))
        self.secondary_highlight_box.setItemText(5, _translate("MainWindow", "Yellow"))
        self.font_size_normal_box.setItemText(0, _translate("MainWindow", "8"))
        self.font_size_normal_box.setItemText(1, _translate("MainWindow", "2"))
        self.font_size_normal_box.setItemText(2, _translate("MainWindow", "4"))
        self.font_size_normal_box.setItemText(3, _translate("MainWindow", "6"))
        self.font_size_normal_box.setItemText(4, _translate("MainWindow", "10"))
        self.font_size_normal_box.setItemText(5, _translate("MainWindow", "11"))
        self.font_size_normal_box.setItemText(6, _translate("MainWindow", "12"))
        self.font_size_normal_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_normal_box.setItemText(8, _translate("MainWindow", "16"))
        self.font_size_min_box.setItemText(0, _translate("MainWindow", "2"))
        self.font_size_min_box.setItemText(1, _translate("MainWindow", "4"))
        self.font_size_min_box.setItemText(2, _translate("MainWindow", "6"))
        self.font_size_min_box.setItemText(3, _translate("MainWindow", "8"))
        self.font_size_min_box.setItemText(4, _translate("MainWindow", "10"))
        self.font_size_min_box.setItemText(5, _translate("MainWindow", "11"))
        self.font_size_min_box.setItemText(6, _translate("MainWindow", "12"))
        self.font_size_min_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_min_box.setItemText(8, _translate("MainWindow", "16"))
        self.secondary_emphasis_box.setItemText(0, _translate("MainWindow", "Bold"))
        self.secondary_emphasis_box.setItemText(1, _translate("MainWindow", "Underline"))
        self.secondary_emphasis_box.setItemText(2, _translate("MainWindow", "Italicized"))
        self.secondary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.secondary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.secondary_emphasis_box.setItemText(5, _translate("MainWindow", "Bold + Underline + Highlight (Secondary)"))
        self.secondary_emphasis_box.setItemText(6, _translate("MainWindow", "Bold + Underline + Highlight (Secondary) + Italicized"))
        self.tertiary_emphasis_box.setItemText(0, _translate("MainWindow", "Underline"))
        self.tertiary_emphasis_box.setItemText(1, _translate("MainWindow", "Bold"))
        self.tertiary_emphasis_box.setItemText(2, _translate("MainWindow", "Italicized"))
        self.tertiary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.tertiary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.tertiary_emphasis_box.setItemText(5, _translate("MainWindow", "Bold + Underline + Highlight (Secondary)"))
        self.tertiary_emphasis_box.setItemText(6, _translate("MainWindow", "Bold + Underline + Highlight (Secondary) + Italicized"))

class ShortcutsWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        MainWindow.setFixedSize(682, 633)
        MainWindow.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.window_label = QtWidgets.QLabel(self.centralwidget)
        self.window_label.setGeometry(QtCore.QRect(10, 10, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.window_label.setFont(font)
        self.window_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255)")
        self.window_label.setObjectName("window_label")
        self.f1_box = QtWidgets.QComboBox(self.centralwidget)
        self.f1_box.setGeometry(QtCore.QRect(10, 100, 281, 22))
        self.f1_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f1_box.setObjectName("f1_box")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.f1_box.addItem("")
        self.m1_box = QtWidgets.QComboBox(self.centralwidget)
        self.m1_box.setGeometry(QtCore.QRect(310, 100, 91, 22))
        self.m1_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m1_box.setObjectName("m1_box")
        self.m1_box.addItem("")
        self.m1_box.addItem("")
        self.k1_box = QtWidgets.QComboBox(self.centralwidget)
        self.k1_box.setGeometry(QtCore.QRect(530, 100, 61, 22))
        self.k1_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k1_box.setObjectName("k1_box")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.k1_box.addItem("")
        self.function_label = QtWidgets.QLabel(self.centralwidget)
        self.function_label.setGeometry(QtCore.QRect(10, 60, 281, 21))
        self.function_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.function_label.setObjectName("function_label")
        self.mod_1_label = QtWidgets.QLabel(self.centralwidget)
        self.mod_1_label.setGeometry(QtCore.QRect(310, 60, 91, 21))
        self.mod_1_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.mod_1_label.setObjectName("mod_1_label")
        self.mod_2_label = QtWidgets.QLabel(self.centralwidget)
        self.mod_2_label.setGeometry(QtCore.QRect(420, 60, 91, 21))
        self.mod_2_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.mod_2_label.setObjectName("mod_2_label")
        self.key_1_label = QtWidgets.QLabel(self.centralwidget)
        self.key_1_label.setGeometry(QtCore.QRect(530, 60, 61, 21))
        self.key_1_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.key_1_label.setObjectName("key_1_label")
        self.key_2_label = QtWidgets.QLabel(self.centralwidget)
        self.key_2_label.setGeometry(QtCore.QRect(610, 60, 61, 21))
        self.key_2_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.key_2_label.setObjectName("key_2_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(230, 580, 221, 23))
        self.save_button.setStyleSheet("QPushButton"
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
        self.save_button.setObjectName("save_button")
        self.save_button.clicked.connect(self.save_config)
        self.f2_box = QtWidgets.QComboBox(self.centralwidget)
        self.f2_box.setGeometry(QtCore.QRect(10, 140, 281, 22))
        self.f2_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f2_box.setObjectName("f2_box")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f2_box.addItem("")
        self.f3_box = QtWidgets.QComboBox(self.centralwidget)
        self.f3_box.setGeometry(QtCore.QRect(10, 180, 281, 22))
        self.f3_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f3_box.setObjectName("f3_box")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f3_box.addItem("")
        self.f4_box = QtWidgets.QComboBox(self.centralwidget)
        self.f4_box.setGeometry(QtCore.QRect(10, 220, 281, 22))
        self.f4_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f4_box.setObjectName("f4_box")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f4_box.addItem("")
        self.f5_box = QtWidgets.QComboBox(self.centralwidget)
        self.f5_box.setGeometry(QtCore.QRect(10, 260, 281, 22))
        self.f5_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f5_box.setObjectName("f5_box")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f5_box.addItem("")
        self.f6_box = QtWidgets.QComboBox(self.centralwidget)
        self.f6_box.setGeometry(QtCore.QRect(10, 300, 281, 22))
        self.f6_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f6_box.setObjectName("f6_box")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f6_box.addItem("")
        self.f8_box = QtWidgets.QComboBox(self.centralwidget)
        self.f8_box.setGeometry(QtCore.QRect(10, 380, 281, 22))
        self.f8_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f8_box.setObjectName("f8_box")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f8_box.addItem("")
        self.f9_box = QtWidgets.QComboBox(self.centralwidget)
        self.f9_box.setGeometry(QtCore.QRect(10, 420, 281, 22))
        self.f9_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f9_box.setObjectName("f9_box")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f9_box.addItem("")
        self.f10_box = QtWidgets.QComboBox(self.centralwidget)
        self.f10_box.setGeometry(QtCore.QRect(10, 460, 281, 22))
        self.f10_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f10_box.setObjectName("f10_box")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f10_box.addItem("")
        self.f11_box = QtWidgets.QComboBox(self.centralwidget)
        self.f11_box.setGeometry(QtCore.QRect(10, 500, 281, 22))
        self.f11_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f11_box.setObjectName("f11_box")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f11_box.addItem("")
        self.f12_box = QtWidgets.QComboBox(self.centralwidget)
        self.f12_box.setGeometry(QtCore.QRect(10, 540, 281, 22))
        self.f12_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f12_box.setObjectName("f12_box")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f12_box.addItem("")
        self.f7_box = QtWidgets.QComboBox(self.centralwidget)
        self.f7_box.setGeometry(QtCore.QRect(10, 340, 281, 22))
        self.f7_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.f7_box.setObjectName("f7_box")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.f7_box.addItem("")
        self.m1b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m1b_box.setGeometry(QtCore.QRect(420, 100, 91, 22))
        self.m1b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m1b_box.setObjectName("m1b_box")
        self.m1b_box.addItem("")
        self.m1b_box.addItem("")
        self.m1b_box.addItem("")
        self.m1b_box.addItem("")
        self.k1b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k1b_box.setGeometry(QtCore.QRect(610, 100, 61, 22))
        self.k1b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k1b_box.setObjectName("k1b_box")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k1b_box.addItem("")
        self.k2b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k2b_box.setGeometry(QtCore.QRect(610, 140, 61, 22))
        self.k2b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k2b_box.setObjectName("k2b_box")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.k2b_box.addItem("")
        self.m2b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m2b_box.setGeometry(QtCore.QRect(420, 140, 91, 22))
        self.m2b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m2b_box.setObjectName("m2b_box")
        self.m2b_box.addItem("")
        self.m2b_box.addItem("")
        self.m2b_box.addItem("")
        self.m2b_box.addItem("")
        self.m2_box = QtWidgets.QComboBox(self.centralwidget)
        self.m2_box.setGeometry(QtCore.QRect(310, 140, 91, 22))
        self.m2_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m2_box.setObjectName("m2_box")
        self.m2_box.addItem("")
        self.m2_box.addItem("")
        self.k3b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k3b_box.setGeometry(QtCore.QRect(610, 180, 61, 22))
        self.k3b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k3b_box.setObjectName("k3b_box")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.k3b_box.addItem("")
        self.m3b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m3b_box.setGeometry(QtCore.QRect(420, 180, 91, 22))
        self.m3b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m3b_box.setObjectName("m3b_box")
        self.m3b_box.addItem("")
        self.m3b_box.addItem("")
        self.m3b_box.addItem("")
        self.m3b_box.addItem("")
        self.m3_box = QtWidgets.QComboBox(self.centralwidget)
        self.m3_box.setGeometry(QtCore.QRect(310, 180, 91, 22))
        self.m3_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m3_box.setObjectName("m3_box")
        self.m3_box.addItem("")
        self.m3_box.addItem("")
        self.m5_box = QtWidgets.QComboBox(self.centralwidget)
        self.m5_box.setGeometry(QtCore.QRect(310, 260, 91, 22))
        self.m5_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m5_box.setObjectName("m5_box")
        self.m5_box.addItem("")
        self.m5_box.addItem("")
        self.m6b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m6b_box.setGeometry(QtCore.QRect(420, 300, 91, 22))
        self.m6b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m6b_box.setObjectName("m6b_box")
        self.m6b_box.addItem("")
        self.m6b_box.addItem("")
        self.m6b_box.addItem("")
        self.m6b_box.addItem("")
        self.m5b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m5b_box.setGeometry(QtCore.QRect(420, 260, 91, 22))
        self.m5b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m5b_box.setObjectName("m5b_box")
        self.m5b_box.addItem("")
        self.m5b_box.addItem("")
        self.m5b_box.addItem("")
        self.m5b_box.addItem("")
        self.m6_box = QtWidgets.QComboBox(self.centralwidget)
        self.m6_box.setGeometry(QtCore.QRect(310, 300, 91, 22))
        self.m6_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m6_box.setObjectName("m6_box")
        self.m6_box.addItem("")
        self.m6_box.addItem("")
        self.k4b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k4b_box.setGeometry(QtCore.QRect(610, 220, 61, 22))
        self.k4b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k4b_box.setObjectName("k4b_box")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k4b_box.addItem("")
        self.k5_box = QtWidgets.QComboBox(self.centralwidget)
        self.k5_box.setGeometry(QtCore.QRect(530, 260, 61, 22))
        self.k5_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k5_box.setObjectName("k5_box")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.k5_box.addItem("")
        self.m4b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m4b_box.setGeometry(QtCore.QRect(420, 220, 91, 22))
        self.m4b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m4b_box.setObjectName("m4b_box")
        self.m4b_box.addItem("")
        self.m4b_box.addItem("")
        self.m4b_box.addItem("")
        self.m4b_box.addItem("")
        self.k4_box = QtWidgets.QComboBox(self.centralwidget)
        self.k4_box.setGeometry(QtCore.QRect(530, 220, 61, 22))
        self.k4_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k4_box.setObjectName("k4_box")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k4_box.addItem("")
        self.k5b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k5b_box.setGeometry(QtCore.QRect(610, 260, 61, 22))
        self.k5b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k5b_box.setObjectName("k5b_box")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k5b_box.addItem("")
        self.k6_box = QtWidgets.QComboBox(self.centralwidget)
        self.k6_box.setGeometry(QtCore.QRect(530, 300, 61, 22))
        self.k6_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k6_box.setObjectName("k6_box")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.k6_box.addItem("")
        self.m4_box = QtWidgets.QComboBox(self.centralwidget)
        self.m4_box.setGeometry(QtCore.QRect(310, 220, 91, 22))
        self.m4_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m4_box.setObjectName("m4_box")
        self.m4_box.addItem("")
        self.m4_box.addItem("")
        self.k6b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k6b_box.setGeometry(QtCore.QRect(610, 300, 61, 22))
        self.k6b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k6b_box.setObjectName("k6b_box")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.k6b_box.addItem("")
        self.m8_box = QtWidgets.QComboBox(self.centralwidget)
        self.m8_box.setGeometry(QtCore.QRect(310, 380, 91, 22))
        self.m8_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m8_box.setObjectName("m8_box")
        self.m8_box.addItem("")
        self.m8_box.addItem("")
        self.m9b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m9b_box.setGeometry(QtCore.QRect(420, 420, 91, 22))
        self.m9b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m9b_box.setObjectName("m9b_box")
        self.m9b_box.addItem("")
        self.m9b_box.addItem("")
        self.m9b_box.addItem("")
        self.m9b_box.addItem("")
        self.m8b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m8b_box.setGeometry(QtCore.QRect(420, 380, 91, 22))
        self.m8b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m8b_box.setObjectName("m8b_box")
        self.m8b_box.addItem("")
        self.m8b_box.addItem("")
        self.m8b_box.addItem("")
        self.m8b_box.addItem("")
        self.m9_box = QtWidgets.QComboBox(self.centralwidget)
        self.m9_box.setGeometry(QtCore.QRect(310, 420, 91, 22))
        self.m9_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m9_box.setObjectName("m9_box")
        self.m9_box.addItem("")
        self.m9_box.addItem("")
        self.k7b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k7b_box.setGeometry(QtCore.QRect(610, 340, 61, 22))
        self.k7b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k7b_box.setObjectName("k7b_box")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k7b_box.addItem("")
        self.k8_box = QtWidgets.QComboBox(self.centralwidget)
        self.k8_box.setGeometry(QtCore.QRect(530, 380, 61, 22))
        self.k8_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k8_box.setObjectName("k8_box")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.k8_box.addItem("")
        self.m7b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m7b_box.setGeometry(QtCore.QRect(420, 340, 91, 22))
        self.m7b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m7b_box.setObjectName("m7b_box")
        self.m7b_box.addItem("")
        self.m7b_box.addItem("")
        self.m7b_box.addItem("")
        self.m7b_box.addItem("")
        self.k7_box = QtWidgets.QComboBox(self.centralwidget)
        self.k7_box.setGeometry(QtCore.QRect(530, 340, 61, 22))
        self.k7_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k7_box.setObjectName("k7_box")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k7_box.addItem("")
        self.k8b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k8b_box.setGeometry(QtCore.QRect(610, 380, 61, 22))
        self.k8b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k8b_box.setObjectName("k8b_box")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k8b_box.addItem("")
        self.k9_box = QtWidgets.QComboBox(self.centralwidget)
        self.k9_box.setGeometry(QtCore.QRect(530, 420, 61, 22))
        self.k9_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k9_box.setObjectName("k9_box")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.k9_box.addItem("")
        self.m7_box = QtWidgets.QComboBox(self.centralwidget)
        self.m7_box.setGeometry(QtCore.QRect(310, 340, 91, 22))
        self.m7_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m7_box.setObjectName("m7_box")
        self.m7_box.addItem("")
        self.m7_box.addItem("")
        self.k9b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k9b_box.setGeometry(QtCore.QRect(610, 420, 61, 22))
        self.k9b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k9b_box.setObjectName("k9b_box")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.k9b_box.addItem("")
        self.m11_box = QtWidgets.QComboBox(self.centralwidget)
        self.m11_box.setGeometry(QtCore.QRect(310, 500, 91, 22))
        self.m11_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m11_box.setObjectName("m11_box")
        self.m11_box.addItem("")
        self.m11_box.addItem("")
        self.m12b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m12b_box.setGeometry(QtCore.QRect(420, 540, 91, 22))
        self.m12b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m12b_box.setObjectName("m12b_box")
        self.m12b_box.addItem("")
        self.m12b_box.addItem("")
        self.m12b_box.addItem("")
        self.m12b_box.addItem("")
        self.m11b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m11b_box.setGeometry(QtCore.QRect(420, 500, 91, 22))
        self.m11b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m11b_box.setObjectName("m11b_box")
        self.m11b_box.addItem("")
        self.m11b_box.addItem("")
        self.m11b_box.addItem("")
        self.m11b_box.addItem("")
        self.m12_box = QtWidgets.QComboBox(self.centralwidget)
        self.m12_box.setGeometry(QtCore.QRect(310, 540, 91, 22))
        self.m12_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m12_box.setObjectName("m12_box")
        self.m12_box.addItem("")
        self.m12_box.addItem("")
        self.k10b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k10b_box.setGeometry(QtCore.QRect(610, 460, 61, 22))
        self.k10b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k10b_box.setObjectName("k10b_box")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k10b_box.addItem("")
        self.k11_box = QtWidgets.QComboBox(self.centralwidget)
        self.k11_box.setGeometry(QtCore.QRect(530, 500, 61, 22))
        self.k11_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k11_box.setObjectName("k11_box")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.k11_box.addItem("")
        self.m10b_box = QtWidgets.QComboBox(self.centralwidget)
        self.m10b_box.setGeometry(QtCore.QRect(420, 460, 91, 22))
        self.m10b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m10b_box.setObjectName("m10b_box")
        self.m10b_box.addItem("")
        self.m10b_box.addItem("")
        self.m10b_box.addItem("")
        self.m10b_box.addItem("")
        self.k10_box = QtWidgets.QComboBox(self.centralwidget)
        self.k10_box.setGeometry(QtCore.QRect(530, 460, 61, 22))
        self.k10_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k10_box.setObjectName("k10_box")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k10_box.addItem("")
        self.k11b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k11b_box.setGeometry(QtCore.QRect(610, 500, 61, 22))
        self.k11b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k11b_box.setObjectName("k11b_box")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k11b_box.addItem("")
        self.k12_box = QtWidgets.QComboBox(self.centralwidget)
        self.k12_box.setGeometry(QtCore.QRect(530, 540, 61, 22))
        self.k12_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k12_box.setObjectName("k12_box")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.k12_box.addItem("")
        self.m10_box = QtWidgets.QComboBox(self.centralwidget)
        self.m10_box.setGeometry(QtCore.QRect(310, 460, 91, 22))
        self.m10_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.m10_box.setObjectName("m10_box")
        self.m10_box.addItem("")
        self.m10_box.addItem("")
        self.k12b_box = QtWidgets.QComboBox(self.centralwidget)
        self.k12b_box.setGeometry(QtCore.QRect(610, 540, 61, 22))
        self.k12b_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k12b_box.setObjectName("k12b_box")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k12b_box.addItem("")
        self.k2_box = QtWidgets.QComboBox(self.centralwidget)
        self.k2_box.setGeometry(QtCore.QRect(530, 140, 61, 22))
        self.k2_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k2_box.setObjectName("k2_box")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k2_box.addItem("")
        self.k3_box = QtWidgets.QComboBox(self.centralwidget)
        self.k3_box.setGeometry(QtCore.QRect(530, 180, 61, 22))
        self.k3_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "")
        self.k3_box.setObjectName("k3_box")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        self.k3_box.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_boxes(self):
        functions = [
            self.f1_box,
            self.f2_box,
            self.f3_box,
            self.f4_box,
            self.f5_box,
            self.f6_box,
            self.f7_box,
            self.f8_box,
            self.f9_box,
            self.f10_box,
            self.f11_box,
            self.f12_box
        ]

        mods = [
            self.m1_box,
            self.m1b_box,
            self.m2_box,
            self.m2b_box,
            self.m3_box,
            self.m3b_box,
            self.m4_box,
            self.m4b_box,
            self.m5_box,
            self.m5b_box,
            self.m6_box,
            self.m6b_box,
            self.m7_box,
            self.m7b_box,
            self.m8_box,
            self.m8b_box,
            self.m9_box,
            self.m9b_box,
            self.m10_box,
            self.m10b_box,
            self.m11_box,
            self.m11b_box,
            self.m12_box,
            self.m12b_box
        ]

        keys = [
            self.k1_box,
            self.k1b_box,
            self.k2_box,
            self.k2b_box,
            self.k3_box,
            self.k3b_box,
            self.k4_box,
            self.k4b_box,
            self.k5_box,
            self.k5b_box,
            self.k6_box,
            self.k6b_box,
            self.k7_box,
            self.k7b_box,
            self.k8_box,
            self.k8b_box,
            self.k9_box,
            self.k9b_box,
            self.k10_box,
            self.k10b_box,
            self.k11_box,
            self.k11b_box,
            self.k12_box,
            self.k12b_box
        ]

        return [functions, mods, keys]

    def load_config(self):
        # TODO implement in future
        pass

    def save_config(self):

        # Getting all combo boxes
        boxes = self.get_boxes()

        # Getting function boxes
        functions = boxes[0]

        # Getting modifier boxes
        mods = boxes[1]

        # Getting key boxes
        keys = boxes[2]

        # Getting user data
        data = store.getData()

        # Creating new dict for shortcuts
        shortcuts = {}

        # Iterating through all 12 functions
        for i in range(0,12):
            
            # Key Sequence is the sequence of keys to activate the function
            key_sequence = ""

            # The indicies tells us where to look in the modifier/key boxes
            # relative to the loop iteration, since each fxn has 2 possible modifiers/keys

            i1 = 2 * i
            i2 = i1 + 1

            # Getting 2 possible modifiers
            m1 = mods[i1]
            m2 = mods[i2]

            # Getting 2 possible keys
            k1 = keys[i1]
            k2 = keys[i2]

            # creating a sequence of 2 modifiers, 2 keys
            sequence = [m1, m2, k1, k2]

            # making sure a primary modifier and a primary key exist
            if (m1.currentText() != "NONE") and (k1.currentText() != "NONE"):
                
                # removing second modifier if it doesn't exist
                if (m2.currentText() == "NONE"):
                    sequence.remove(m2)

                # removing second key if it doesn't exist
                if (k2.currentText() == "NONE"):
                    sequence.remove(k2)
                
                # creating a string representation of the current sequence
                for key in sequence:
                    key_sequence += key.currentText() + "+"

                key_sequence = key_sequence[:-1]

                # adding the function name to the dict
                shortcuts[str(functions[i].currentText())] = key_sequence.replace('CTRL/CMD', 'CTRL')

        # updating main dataset
        data["settings"]["shortcuts"] = shortcuts

        # pushing to JSON
        store.setData(data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Set Shortcuts - Cut-It™"))
        self.window_label.setText(_translate("MainWindow", "Set Shortcuts:"))
        self.f1_box.setItemText(0, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f1_box.setItemText(1, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f1_box.setItemText(2, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f1_box.setItemText(3, _translate("MainWindow", "Minimize Text"))
        self.f1_box.setItemText(4, _translate("MainWindow", "AutoPoll"))
        self.f1_box.setItemText(5, _translate("MainWindow", "AutoCite"))
        self.f1_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f1_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f1_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f1_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f1_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f1_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.m1_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m1_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k1_box.setItemText(0, _translate("MainWindow", "S"))
        self.k1_box.setItemText(1, _translate("MainWindow", "A"))
        self.k1_box.setItemText(2, _translate("MainWindow", "B"))
        self.k1_box.setItemText(3, _translate("MainWindow", "C"))
        self.k1_box.setItemText(4, _translate("MainWindow", "D"))
        self.k1_box.setItemText(5, _translate("MainWindow", "E"))
        self.k1_box.setItemText(6, _translate("MainWindow", "F"))
        self.k1_box.setItemText(7, _translate("MainWindow", "G"))
        self.k1_box.setItemText(8, _translate("MainWindow", "H"))
        self.k1_box.setItemText(9, _translate("MainWindow", "I"))
        self.k1_box.setItemText(10, _translate("MainWindow", "J"))
        self.k1_box.setItemText(11, _translate("MainWindow", "K"))
        self.k1_box.setItemText(12, _translate("MainWindow", "L"))
        self.k1_box.setItemText(13, _translate("MainWindow", "M"))
        self.k1_box.setItemText(14, _translate("MainWindow", "N"))
        self.k1_box.setItemText(15, _translate("MainWindow", "O"))
        self.k1_box.setItemText(16, _translate("MainWindow", "P"))
        self.k1_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k1_box.setItemText(18, _translate("MainWindow", "R"))
        self.k1_box.setItemText(19, _translate("MainWindow", "T"))
        self.k1_box.setItemText(20, _translate("MainWindow", "U"))
        self.k1_box.setItemText(21, _translate("MainWindow", "V"))
        self.k1_box.setItemText(22, _translate("MainWindow", "W"))
        self.k1_box.setItemText(23, _translate("MainWindow", "X"))
        self.k1_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k1_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k1_box.setItemText(26, _translate("MainWindow", "0"))
        self.k1_box.setItemText(27, _translate("MainWindow", "1"))
        self.k1_box.setItemText(28, _translate("MainWindow", "2"))
        self.k1_box.setItemText(29, _translate("MainWindow", "3"))
        self.k1_box.setItemText(30, _translate("MainWindow", "4"))
        self.k1_box.setItemText(31, _translate("MainWindow", "5"))
        self.k1_box.setItemText(32, _translate("MainWindow", "6"))
        self.k1_box.setItemText(33, _translate("MainWindow", "7"))
        self.k1_box.setItemText(34, _translate("MainWindow", "8"))
        self.k1_box.setItemText(35, _translate("MainWindow", "9"))
        self.function_label.setText(_translate("MainWindow", "Function To Execute"))
        self.mod_1_label.setText(_translate("MainWindow", "Modifier #1"))
        self.mod_2_label.setText(_translate("MainWindow", "Modifier #2"))
        self.key_1_label.setText(_translate("MainWindow", "Key #1"))
        self.key_2_label.setText(_translate("MainWindow", "Key #2"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.f2_box.setItemText(0, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f2_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f2_box.setItemText(2, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f2_box.setItemText(3, _translate("MainWindow", "Minimize Text"))
        self.f2_box.setItemText(4, _translate("MainWindow", "AutoPoll"))
        self.f2_box.setItemText(5, _translate("MainWindow", "AutoCite"))
        self.f2_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f2_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f2_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f2_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f2_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f2_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f3_box.setItemText(0, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f3_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f3_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f3_box.setItemText(3, _translate("MainWindow", "Minimize Text"))
        self.f3_box.setItemText(4, _translate("MainWindow", "AutoPoll"))
        self.f3_box.setItemText(5, _translate("MainWindow", "AutoCite"))
        self.f3_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f3_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f3_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f3_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f3_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f3_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f4_box.setItemText(0, _translate("MainWindow", "Minimize Text"))
        self.f4_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f4_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f4_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f4_box.setItemText(4, _translate("MainWindow", "AutoPoll"))
        self.f4_box.setItemText(5, _translate("MainWindow", "AutoCite"))
        self.f4_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f4_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f4_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f4_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f4_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f4_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f5_box.setItemText(0, _translate("MainWindow", "AutoPoll"))
        self.f5_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f5_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f5_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f5_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f5_box.setItemText(5, _translate("MainWindow", "AutoCite"))
        self.f5_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f5_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f5_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f5_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f5_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f5_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f6_box.setItemText(0, _translate("MainWindow", "AutoCite"))
        self.f6_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f6_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f6_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f6_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f6_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f6_box.setItemText(6, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f6_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f6_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f6_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f6_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f6_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f8_box.setItemText(0, _translate("MainWindow", "Save As PDF"))
        self.f8_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f8_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f8_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f8_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f8_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f8_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f8_box.setItemText(7, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f8_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f8_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f8_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f8_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f9_box.setItemText(0, _translate("MainWindow", "Save Card In Progress"))
        self.f9_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f9_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f9_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f9_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f9_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f9_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f9_box.setItemText(7, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f9_box.setItemText(8, _translate("MainWindow", "Save As PDF"))
        self.f9_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f9_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f9_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f10_box.setItemText(0, _translate("MainWindow", "Open Shortcuts"))
        self.f10_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f10_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f10_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f10_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f10_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f10_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f10_box.setItemText(7, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f10_box.setItemText(8, _translate("MainWindow", "Save As PDF"))
        self.f10_box.setItemText(9, _translate("MainWindow", "Save Card In Progress"))
        self.f10_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f10_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f11_box.setItemText(0, _translate("MainWindow", "Open Preferences"))
        self.f11_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f11_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f11_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f11_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f11_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f11_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f11_box.setItemText(7, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f11_box.setItemText(8, _translate("MainWindow", "Save As PDF"))
        self.f11_box.setItemText(9, _translate("MainWindow", "Save Card In Progress"))
        self.f11_box.setItemText(10, _translate("MainWindow", "Open Shortcuts"))
        self.f11_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.f12_box.setItemText(0, _translate("MainWindow", "Close Window"))
        self.f12_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f12_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f12_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f12_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f12_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f12_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f12_box.setItemText(7, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f12_box.setItemText(8, _translate("MainWindow", "Save As PDF"))
        self.f12_box.setItemText(9, _translate("MainWindow", "Save Card In Progress"))
        self.f12_box.setItemText(10, _translate("MainWindow", "Open Shortcuts"))
        self.f12_box.setItemText(11, _translate("MainWindow", "Open Preferences"))
        self.f7_box.setItemText(0, _translate("MainWindow", "AutoPoll + AutoCite"))
        self.f7_box.setItemText(1, _translate("MainWindow", "Cut-It (Primary Emphasis)"))
        self.f7_box.setItemText(2, _translate("MainWindow", "Cut-It (Secondary Emphasis)"))
        self.f7_box.setItemText(3, _translate("MainWindow", "Cut-It (Tertiary Emphasis)"))
        self.f7_box.setItemText(4, _translate("MainWindow", "Minimize Text"))
        self.f7_box.setItemText(5, _translate("MainWindow", "AutoPoll"))
        self.f7_box.setItemText(6, _translate("MainWindow", "AutoCite"))
        self.f7_box.setItemText(7, _translate("MainWindow", "Save As PDF"))
        self.f7_box.setItemText(8, _translate("MainWindow", "Save Card In Progress"))
        self.f7_box.setItemText(9, _translate("MainWindow", "Open Shortcuts"))
        self.f7_box.setItemText(10, _translate("MainWindow", "Open Preferences"))
        self.f7_box.setItemText(11, _translate("MainWindow", "Close Window"))
        self.m1b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m1b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m1b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m1b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.k1b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k1b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k1b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k1b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k1b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k1b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k1b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k1b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k1b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k1b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k1b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k1b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k1b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k1b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k1b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k1b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k1b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k1b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k1b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k1b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k1b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k1b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k1b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k1b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k1b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k1b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k1b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k1b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k1b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k1b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k1b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k1b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k1b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k1b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k1b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k1b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k1b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k2b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k2b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k2b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k2b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k2b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k2b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k2b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k2b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k2b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k2b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k2b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k2b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k2b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k2b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k2b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k2b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k2b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k2b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k2b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k2b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k2b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k2b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k2b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k2b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k2b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k2b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k2b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k2b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k2b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k2b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k2b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k2b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k2b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k2b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k2b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k2b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k2b_box.setItemText(36, _translate("MainWindow", "9"))
        self.m2b_box.setItemText(0, _translate("MainWindow", "SHIFT"))
        self.m2b_box.setItemText(1, _translate("MainWindow", "NONE"))
        self.m2b_box.setItemText(2, _translate("MainWindow", "CTRL/CMD"))
        self.m2b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m2_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m2_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k3b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k3b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k3b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k3b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k3b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k3b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k3b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k3b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k3b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k3b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k3b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k3b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k3b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k3b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k3b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k3b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k3b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k3b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k3b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k3b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k3b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k3b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k3b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k3b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k3b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k3b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k3b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k3b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k3b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k3b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k3b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k3b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k3b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k3b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k3b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k3b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k3b_box.setItemText(36, _translate("MainWindow", "9"))
        self.m3b_box.setItemText(0, _translate("MainWindow", "ALT"))
        self.m3b_box.setItemText(1, _translate("MainWindow", "NONE"))
        self.m3b_box.setItemText(2, _translate("MainWindow", "CTRL/CMD"))
        self.m3b_box.setItemText(3, _translate("MainWindow", "SHIFT"))
        self.m3_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m3_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.m5_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m5_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.m6b_box.setItemText(0, _translate("MainWindow", "SHIFT"))
        self.m6b_box.setItemText(1, _translate("MainWindow", "NONE"))
        self.m6b_box.setItemText(2, _translate("MainWindow", "CTRL/CMD"))
        self.m6b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m5b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m5b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m5b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m5b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m6_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m6_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k4b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k4b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k4b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k4b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k4b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k4b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k4b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k4b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k4b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k4b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k4b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k4b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k4b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k4b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k4b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k4b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k4b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k4b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k4b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k4b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k4b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k4b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k4b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k4b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k4b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k4b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k4b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k4b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k4b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k4b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k4b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k4b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k4b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k4b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k4b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k4b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k4b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k5_box.setItemText(0, _translate("MainWindow", "D"))
        self.k5_box.setItemText(1, _translate("MainWindow", "A"))
        self.k5_box.setItemText(2, _translate("MainWindow", "B"))
        self.k5_box.setItemText(3, _translate("MainWindow", "C"))
        self.k5_box.setItemText(4, _translate("MainWindow", "E"))
        self.k5_box.setItemText(5, _translate("MainWindow", "F"))
        self.k5_box.setItemText(6, _translate("MainWindow", "G"))
        self.k5_box.setItemText(7, _translate("MainWindow", "H"))
        self.k5_box.setItemText(8, _translate("MainWindow", "I"))
        self.k5_box.setItemText(9, _translate("MainWindow", "J"))
        self.k5_box.setItemText(10, _translate("MainWindow", "K"))
        self.k5_box.setItemText(11, _translate("MainWindow", "L"))
        self.k5_box.setItemText(12, _translate("MainWindow", "M"))
        self.k5_box.setItemText(13, _translate("MainWindow", "N"))
        self.k5_box.setItemText(14, _translate("MainWindow", "O"))
        self.k5_box.setItemText(15, _translate("MainWindow", "P"))
        self.k5_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k5_box.setItemText(17, _translate("MainWindow", "R"))
        self.k5_box.setItemText(18, _translate("MainWindow", "S"))
        self.k5_box.setItemText(19, _translate("MainWindow", "T"))
        self.k5_box.setItemText(20, _translate("MainWindow", "U"))
        self.k5_box.setItemText(21, _translate("MainWindow", "V"))
        self.k5_box.setItemText(22, _translate("MainWindow", "W"))
        self.k5_box.setItemText(23, _translate("MainWindow", "X"))
        self.k5_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k5_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k5_box.setItemText(26, _translate("MainWindow", "0"))
        self.k5_box.setItemText(27, _translate("MainWindow", "1"))
        self.k5_box.setItemText(28, _translate("MainWindow", "2"))
        self.k5_box.setItemText(29, _translate("MainWindow", "3"))
        self.k5_box.setItemText(30, _translate("MainWindow", "4"))
        self.k5_box.setItemText(31, _translate("MainWindow", "5"))
        self.k5_box.setItemText(32, _translate("MainWindow", "6"))
        self.k5_box.setItemText(33, _translate("MainWindow", "7"))
        self.k5_box.setItemText(34, _translate("MainWindow", "8"))
        self.k5_box.setItemText(35, _translate("MainWindow", "9"))
        self.m4b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m4b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m4b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m4b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.k4_box.setItemText(0, _translate("MainWindow", "M"))
        self.k4_box.setItemText(1, _translate("MainWindow", "A"))
        self.k4_box.setItemText(2, _translate("MainWindow", "B"))
        self.k4_box.setItemText(3, _translate("MainWindow", "C"))
        self.k4_box.setItemText(4, _translate("MainWindow", "D"))
        self.k4_box.setItemText(5, _translate("MainWindow", "E"))
        self.k4_box.setItemText(6, _translate("MainWindow", "F"))
        self.k4_box.setItemText(7, _translate("MainWindow", "G"))
        self.k4_box.setItemText(8, _translate("MainWindow", "H"))
        self.k4_box.setItemText(9, _translate("MainWindow", "I"))
        self.k4_box.setItemText(10, _translate("MainWindow", "J"))
        self.k4_box.setItemText(11, _translate("MainWindow", "K"))
        self.k4_box.setItemText(12, _translate("MainWindow", "L"))
        self.k4_box.setItemText(13, _translate("MainWindow", "N"))
        self.k4_box.setItemText(14, _translate("MainWindow", "O"))
        self.k4_box.setItemText(15, _translate("MainWindow", "P"))
        self.k4_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k4_box.setItemText(17, _translate("MainWindow", "R"))
        self.k4_box.setItemText(18, _translate("MainWindow", "S"))
        self.k4_box.setItemText(19, _translate("MainWindow", "T"))
        self.k4_box.setItemText(20, _translate("MainWindow", "U"))
        self.k4_box.setItemText(21, _translate("MainWindow", "V"))
        self.k4_box.setItemText(22, _translate("MainWindow", "W"))
        self.k4_box.setItemText(23, _translate("MainWindow", "X"))
        self.k4_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k4_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k4_box.setItemText(26, _translate("MainWindow", "0"))
        self.k4_box.setItemText(27, _translate("MainWindow", "1"))
        self.k4_box.setItemText(28, _translate("MainWindow", "2"))
        self.k4_box.setItemText(29, _translate("MainWindow", "3"))
        self.k4_box.setItemText(30, _translate("MainWindow", "4"))
        self.k4_box.setItemText(31, _translate("MainWindow", "5"))
        self.k4_box.setItemText(32, _translate("MainWindow", "6"))
        self.k4_box.setItemText(33, _translate("MainWindow", "7"))
        self.k4_box.setItemText(34, _translate("MainWindow", "8"))
        self.k4_box.setItemText(35, _translate("MainWindow", "9"))
        self.k5b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k5b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k5b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k5b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k5b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k5b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k5b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k5b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k5b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k5b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k5b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k5b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k5b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k5b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k5b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k5b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k5b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k5b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k5b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k5b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k5b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k5b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k5b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k5b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k5b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k5b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k5b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k5b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k5b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k5b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k5b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k5b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k5b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k5b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k5b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k5b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k5b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k6_box.setItemText(0, _translate("MainWindow", "D"))
        self.k6_box.setItemText(1, _translate("MainWindow", "A"))
        self.k6_box.setItemText(2, _translate("MainWindow", "B"))
        self.k6_box.setItemText(3, _translate("MainWindow", "C"))
        self.k6_box.setItemText(4, _translate("MainWindow", "E"))
        self.k6_box.setItemText(5, _translate("MainWindow", "F"))
        self.k6_box.setItemText(6, _translate("MainWindow", "G"))
        self.k6_box.setItemText(7, _translate("MainWindow", "H"))
        self.k6_box.setItemText(8, _translate("MainWindow", "I"))
        self.k6_box.setItemText(9, _translate("MainWindow", "J"))
        self.k6_box.setItemText(10, _translate("MainWindow", "K"))
        self.k6_box.setItemText(11, _translate("MainWindow", "L"))
        self.k6_box.setItemText(12, _translate("MainWindow", "M"))
        self.k6_box.setItemText(13, _translate("MainWindow", "N"))
        self.k6_box.setItemText(14, _translate("MainWindow", "O"))
        self.k6_box.setItemText(15, _translate("MainWindow", "P"))
        self.k6_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k6_box.setItemText(17, _translate("MainWindow", "R"))
        self.k6_box.setItemText(18, _translate("MainWindow", "S"))
        self.k6_box.setItemText(19, _translate("MainWindow", "T"))
        self.k6_box.setItemText(20, _translate("MainWindow", "U"))
        self.k6_box.setItemText(21, _translate("MainWindow", "V"))
        self.k6_box.setItemText(22, _translate("MainWindow", "W"))
        self.k6_box.setItemText(23, _translate("MainWindow", "X"))
        self.k6_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k6_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k6_box.setItemText(26, _translate("MainWindow", "0"))
        self.k6_box.setItemText(27, _translate("MainWindow", "1"))
        self.k6_box.setItemText(28, _translate("MainWindow", "2"))
        self.k6_box.setItemText(29, _translate("MainWindow", "3"))
        self.k6_box.setItemText(30, _translate("MainWindow", "4"))
        self.k6_box.setItemText(31, _translate("MainWindow", "5"))
        self.k6_box.setItemText(32, _translate("MainWindow", "6"))
        self.k6_box.setItemText(33, _translate("MainWindow", "7"))
        self.k6_box.setItemText(34, _translate("MainWindow", "8"))
        self.k6_box.setItemText(35, _translate("MainWindow", "9"))
        self.m4_box.setItemText(0, _translate("MainWindow", "ALT"))
        self.m4_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.k6b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k6b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k6b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k6b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k6b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k6b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k6b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k6b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k6b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k6b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k6b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k6b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k6b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k6b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k6b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k6b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k6b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k6b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k6b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k6b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k6b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k6b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k6b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k6b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k6b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k6b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k6b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k6b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k6b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k6b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k6b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k6b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k6b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k6b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k6b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k6b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k6b_box.setItemText(36, _translate("MainWindow", "9"))
        self.m8_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m8_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.m9b_box.setItemText(0, _translate("MainWindow", "SHIFT"))
        self.m9b_box.setItemText(1, _translate("MainWindow", "NONE"))
        self.m9b_box.setItemText(2, _translate("MainWindow", "CTRL/CMD"))
        self.m9b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m8b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m8b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m8b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m8b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m9_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m9_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k7b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k7b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k7b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k7b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k7b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k7b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k7b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k7b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k7b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k7b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k7b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k7b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k7b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k7b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k7b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k7b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k7b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k7b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k7b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k7b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k7b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k7b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k7b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k7b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k7b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k7b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k7b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k7b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k7b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k7b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k7b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k7b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k7b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k7b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k7b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k7b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k7b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k8_box.setItemText(0, _translate("MainWindow", "P"))
        self.k8_box.setItemText(1, _translate("MainWindow", "A"))
        self.k8_box.setItemText(2, _translate("MainWindow", "B"))
        self.k8_box.setItemText(3, _translate("MainWindow", "C"))
        self.k8_box.setItemText(4, _translate("MainWindow", "D"))
        self.k8_box.setItemText(5, _translate("MainWindow", "E"))
        self.k8_box.setItemText(6, _translate("MainWindow", "F"))
        self.k8_box.setItemText(7, _translate("MainWindow", "G"))
        self.k8_box.setItemText(8, _translate("MainWindow", "H"))
        self.k8_box.setItemText(9, _translate("MainWindow", "I"))
        self.k8_box.setItemText(10, _translate("MainWindow", "J"))
        self.k8_box.setItemText(11, _translate("MainWindow", "K"))
        self.k8_box.setItemText(12, _translate("MainWindow", "L"))
        self.k8_box.setItemText(13, _translate("MainWindow", "M"))
        self.k8_box.setItemText(14, _translate("MainWindow", "N"))
        self.k8_box.setItemText(15, _translate("MainWindow", "O"))
        self.k8_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k8_box.setItemText(17, _translate("MainWindow", "R"))
        self.k8_box.setItemText(18, _translate("MainWindow", "S"))
        self.k8_box.setItemText(19, _translate("MainWindow", "T"))
        self.k8_box.setItemText(20, _translate("MainWindow", "U"))
        self.k8_box.setItemText(21, _translate("MainWindow", "V"))
        self.k8_box.setItemText(22, _translate("MainWindow", "W"))
        self.k8_box.setItemText(23, _translate("MainWindow", "X"))
        self.k8_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k8_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k8_box.setItemText(26, _translate("MainWindow", "0"))
        self.k8_box.setItemText(27, _translate("MainWindow", "1"))
        self.k8_box.setItemText(28, _translate("MainWindow", "2"))
        self.k8_box.setItemText(29, _translate("MainWindow", "3"))
        self.k8_box.setItemText(30, _translate("MainWindow", "4"))
        self.k8_box.setItemText(31, _translate("MainWindow", "5"))
        self.k8_box.setItemText(32, _translate("MainWindow", "6"))
        self.k8_box.setItemText(33, _translate("MainWindow", "7"))
        self.k8_box.setItemText(34, _translate("MainWindow", "8"))
        self.k8_box.setItemText(35, _translate("MainWindow", "9"))
        self.m7b_box.setItemText(0, _translate("MainWindow", "ALT"))
        self.m7b_box.setItemText(1, _translate("MainWindow", "NONE"))
        self.m7b_box.setItemText(2, _translate("MainWindow", "CTRL/CMD"))
        self.m7b_box.setItemText(3, _translate("MainWindow", "SHIFT"))
        self.k7_box.setItemText(0, _translate("MainWindow", "D"))
        self.k7_box.setItemText(1, _translate("MainWindow", "A"))
        self.k7_box.setItemText(2, _translate("MainWindow", "B"))
        self.k7_box.setItemText(3, _translate("MainWindow", "C"))
        self.k7_box.setItemText(4, _translate("MainWindow", "E"))
        self.k7_box.setItemText(5, _translate("MainWindow", "F"))
        self.k7_box.setItemText(6, _translate("MainWindow", "G"))
        self.k7_box.setItemText(7, _translate("MainWindow", "H"))
        self.k7_box.setItemText(8, _translate("MainWindow", "I"))
        self.k7_box.setItemText(9, _translate("MainWindow", "J"))
        self.k7_box.setItemText(10, _translate("MainWindow", "K"))
        self.k7_box.setItemText(11, _translate("MainWindow", "L"))
        self.k7_box.setItemText(12, _translate("MainWindow", "M"))
        self.k7_box.setItemText(13, _translate("MainWindow", "N"))
        self.k7_box.setItemText(14, _translate("MainWindow", "O"))
        self.k7_box.setItemText(15, _translate("MainWindow", "P"))
        self.k7_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k7_box.setItemText(17, _translate("MainWindow", "R"))
        self.k7_box.setItemText(18, _translate("MainWindow", "S"))
        self.k7_box.setItemText(19, _translate("MainWindow", "T"))
        self.k7_box.setItemText(20, _translate("MainWindow", "U"))
        self.k7_box.setItemText(21, _translate("MainWindow", "V"))
        self.k7_box.setItemText(22, _translate("MainWindow", "W"))
        self.k7_box.setItemText(23, _translate("MainWindow", "X"))
        self.k7_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k7_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k7_box.setItemText(26, _translate("MainWindow", "0"))
        self.k7_box.setItemText(27, _translate("MainWindow", "1"))
        self.k7_box.setItemText(28, _translate("MainWindow", "2"))
        self.k7_box.setItemText(29, _translate("MainWindow", "3"))
        self.k7_box.setItemText(30, _translate("MainWindow", "4"))
        self.k7_box.setItemText(31, _translate("MainWindow", "5"))
        self.k7_box.setItemText(32, _translate("MainWindow", "6"))
        self.k7_box.setItemText(33, _translate("MainWindow", "7"))
        self.k7_box.setItemText(34, _translate("MainWindow", "8"))
        self.k7_box.setItemText(35, _translate("MainWindow", "9"))
        self.k8b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k8b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k8b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k8b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k8b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k8b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k8b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k8b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k8b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k8b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k8b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k8b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k8b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k8b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k8b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k8b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k8b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k8b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k8b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k8b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k8b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k8b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k8b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k8b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k8b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k8b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k8b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k8b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k8b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k8b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k8b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k8b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k8b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k8b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k8b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k8b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k8b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k9_box.setItemText(0, _translate("MainWindow", "P"))
        self.k9_box.setItemText(1, _translate("MainWindow", "A"))
        self.k9_box.setItemText(2, _translate("MainWindow", "B"))
        self.k9_box.setItemText(3, _translate("MainWindow", "C"))
        self.k9_box.setItemText(4, _translate("MainWindow", "D"))
        self.k9_box.setItemText(5, _translate("MainWindow", "E"))
        self.k9_box.setItemText(6, _translate("MainWindow", "F"))
        self.k9_box.setItemText(7, _translate("MainWindow", "G"))
        self.k9_box.setItemText(8, _translate("MainWindow", "H"))
        self.k9_box.setItemText(9, _translate("MainWindow", "I"))
        self.k9_box.setItemText(10, _translate("MainWindow", "J"))
        self.k9_box.setItemText(11, _translate("MainWindow", "K"))
        self.k9_box.setItemText(12, _translate("MainWindow", "L"))
        self.k9_box.setItemText(13, _translate("MainWindow", "M"))
        self.k9_box.setItemText(14, _translate("MainWindow", "N"))
        self.k9_box.setItemText(15, _translate("MainWindow", "O"))
        self.k9_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k9_box.setItemText(17, _translate("MainWindow", "R"))
        self.k9_box.setItemText(18, _translate("MainWindow", "S"))
        self.k9_box.setItemText(19, _translate("MainWindow", "T"))
        self.k9_box.setItemText(20, _translate("MainWindow", "U"))
        self.k9_box.setItemText(21, _translate("MainWindow", "V"))
        self.k9_box.setItemText(22, _translate("MainWindow", "W"))
        self.k9_box.setItemText(23, _translate("MainWindow", "X"))
        self.k9_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k9_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k9_box.setItemText(26, _translate("MainWindow", "0"))
        self.k9_box.setItemText(27, _translate("MainWindow", "1"))
        self.k9_box.setItemText(28, _translate("MainWindow", "2"))
        self.k9_box.setItemText(29, _translate("MainWindow", "3"))
        self.k9_box.setItemText(30, _translate("MainWindow", "4"))
        self.k9_box.setItemText(31, _translate("MainWindow", "5"))
        self.k9_box.setItemText(32, _translate("MainWindow", "6"))
        self.k9_box.setItemText(33, _translate("MainWindow", "7"))
        self.k9_box.setItemText(34, _translate("MainWindow", "8"))
        self.k9_box.setItemText(35, _translate("MainWindow", "9"))
        self.m7_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m7_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k9b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k9b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k9b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k9b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k9b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k9b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k9b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k9b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k9b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k9b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k9b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k9b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k9b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k9b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k9b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k9b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k9b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k9b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k9b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k9b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k9b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k9b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k9b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k9b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k9b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k9b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k9b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k9b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k9b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k9b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k9b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k9b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k9b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k9b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k9b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k9b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k9b_box.setItemText(36, _translate("MainWindow", "9"))
        self.m11_box.setItemText(0, _translate("MainWindow", "ALT"))
        self.m11_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m12b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m12b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m12b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m12b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m11b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m11b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m11b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m11b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.m12_box.setItemText(0, _translate("MainWindow", "CTRL/CMD"))
        self.m12_box.setItemText(1, _translate("MainWindow", "ALT"))
        self.k10b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k10b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k10b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k10b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k10b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k10b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k10b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k10b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k10b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k10b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k10b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k10b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k10b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k10b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k10b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k10b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k10b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k10b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k10b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k10b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k10b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k10b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k10b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k10b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k10b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k10b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k10b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k10b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k10b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k10b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k10b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k10b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k10b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k10b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k10b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k10b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k10b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k11_box.setItemText(0, _translate("MainWindow", "P"))
        self.k11_box.setItemText(1, _translate("MainWindow", "A"))
        self.k11_box.setItemText(2, _translate("MainWindow", "B"))
        self.k11_box.setItemText(3, _translate("MainWindow", "C"))
        self.k11_box.setItemText(4, _translate("MainWindow", "D"))
        self.k11_box.setItemText(5, _translate("MainWindow", "E"))
        self.k11_box.setItemText(6, _translate("MainWindow", "F"))
        self.k11_box.setItemText(7, _translate("MainWindow", "G"))
        self.k11_box.setItemText(8, _translate("MainWindow", "H"))
        self.k11_box.setItemText(9, _translate("MainWindow", "I"))
        self.k11_box.setItemText(10, _translate("MainWindow", "J"))
        self.k11_box.setItemText(11, _translate("MainWindow", "K"))
        self.k11_box.setItemText(12, _translate("MainWindow", "L"))
        self.k11_box.setItemText(13, _translate("MainWindow", "M"))
        self.k11_box.setItemText(14, _translate("MainWindow", "N"))
        self.k11_box.setItemText(15, _translate("MainWindow", "O"))
        self.k11_box.setItemText(16, _translate("MainWindow", "Q"))
        self.k11_box.setItemText(17, _translate("MainWindow", "R"))
        self.k11_box.setItemText(18, _translate("MainWindow", "S"))
        self.k11_box.setItemText(19, _translate("MainWindow", "T"))
        self.k11_box.setItemText(20, _translate("MainWindow", "U"))
        self.k11_box.setItemText(21, _translate("MainWindow", "V"))
        self.k11_box.setItemText(22, _translate("MainWindow", "W"))
        self.k11_box.setItemText(23, _translate("MainWindow", "X"))
        self.k11_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k11_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k11_box.setItemText(26, _translate("MainWindow", "0"))
        self.k11_box.setItemText(27, _translate("MainWindow", "1"))
        self.k11_box.setItemText(28, _translate("MainWindow", "2"))
        self.k11_box.setItemText(29, _translate("MainWindow", "3"))
        self.k11_box.setItemText(30, _translate("MainWindow", "4"))
        self.k11_box.setItemText(31, _translate("MainWindow", "5"))
        self.k11_box.setItemText(32, _translate("MainWindow", "6"))
        self.k11_box.setItemText(33, _translate("MainWindow", "7"))
        self.k11_box.setItemText(34, _translate("MainWindow", "8"))
        self.k11_box.setItemText(35, _translate("MainWindow", "9"))
        self.m10b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.m10b_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.m10b_box.setItemText(2, _translate("MainWindow", "SHIFT"))
        self.m10b_box.setItemText(3, _translate("MainWindow", "ALT"))
        self.k10_box.setItemText(0, _translate("MainWindow", "S"))
        self.k10_box.setItemText(1, _translate("MainWindow", "A"))
        self.k10_box.setItemText(2, _translate("MainWindow", "B"))
        self.k10_box.setItemText(3, _translate("MainWindow", "C"))
        self.k10_box.setItemText(4, _translate("MainWindow", "D"))
        self.k10_box.setItemText(5, _translate("MainWindow", "E"))
        self.k10_box.setItemText(6, _translate("MainWindow", "F"))
        self.k10_box.setItemText(7, _translate("MainWindow", "G"))
        self.k10_box.setItemText(8, _translate("MainWindow", "H"))
        self.k10_box.setItemText(9, _translate("MainWindow", "I"))
        self.k10_box.setItemText(10, _translate("MainWindow", "J"))
        self.k10_box.setItemText(11, _translate("MainWindow", "K"))
        self.k10_box.setItemText(12, _translate("MainWindow", "L"))
        self.k10_box.setItemText(13, _translate("MainWindow", "M"))
        self.k10_box.setItemText(14, _translate("MainWindow", "N"))
        self.k10_box.setItemText(15, _translate("MainWindow", "O"))
        self.k10_box.setItemText(16, _translate("MainWindow", "P"))
        self.k10_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k10_box.setItemText(18, _translate("MainWindow", "R"))
        self.k10_box.setItemText(19, _translate("MainWindow", "T"))
        self.k10_box.setItemText(20, _translate("MainWindow", "U"))
        self.k10_box.setItemText(21, _translate("MainWindow", "V"))
        self.k10_box.setItemText(22, _translate("MainWindow", "W"))
        self.k10_box.setItemText(23, _translate("MainWindow", "X"))
        self.k10_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k10_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k10_box.setItemText(26, _translate("MainWindow", "0"))
        self.k10_box.setItemText(27, _translate("MainWindow", "1"))
        self.k10_box.setItemText(28, _translate("MainWindow", "2"))
        self.k10_box.setItemText(29, _translate("MainWindow", "3"))
        self.k10_box.setItemText(30, _translate("MainWindow", "4"))
        self.k10_box.setItemText(31, _translate("MainWindow", "5"))
        self.k10_box.setItemText(32, _translate("MainWindow", "6"))
        self.k10_box.setItemText(33, _translate("MainWindow", "7"))
        self.k10_box.setItemText(34, _translate("MainWindow", "8"))
        self.k10_box.setItemText(35, _translate("MainWindow", "9"))
        self.k11b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k11b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k11b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k11b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k11b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k11b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k11b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k11b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k11b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k11b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k11b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k11b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k11b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k11b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k11b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k11b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k11b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k11b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k11b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k11b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k11b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k11b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k11b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k11b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k11b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k11b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k11b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k11b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k11b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k11b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k11b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k11b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k11b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k11b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k11b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k11b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k11b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k12_box.setItemText(0, _translate("MainWindow", "W"))
        self.k12_box.setItemText(1, _translate("MainWindow", "A"))
        self.k12_box.setItemText(2, _translate("MainWindow", "B"))
        self.k12_box.setItemText(3, _translate("MainWindow", "C"))
        self.k12_box.setItemText(4, _translate("MainWindow", "D"))
        self.k12_box.setItemText(5, _translate("MainWindow", "E"))
        self.k12_box.setItemText(6, _translate("MainWindow", "F"))
        self.k12_box.setItemText(7, _translate("MainWindow", "G"))
        self.k12_box.setItemText(8, _translate("MainWindow", "H"))
        self.k12_box.setItemText(9, _translate("MainWindow", "I"))
        self.k12_box.setItemText(10, _translate("MainWindow", "J"))
        self.k12_box.setItemText(11, _translate("MainWindow", "K"))
        self.k12_box.setItemText(12, _translate("MainWindow", "L"))
        self.k12_box.setItemText(13, _translate("MainWindow", "M"))
        self.k12_box.setItemText(14, _translate("MainWindow", "N"))
        self.k12_box.setItemText(15, _translate("MainWindow", "O"))
        self.k12_box.setItemText(16, _translate("MainWindow", "P"))
        self.k12_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k12_box.setItemText(18, _translate("MainWindow", "R"))
        self.k12_box.setItemText(19, _translate("MainWindow", "S"))
        self.k12_box.setItemText(20, _translate("MainWindow", "T"))
        self.k12_box.setItemText(21, _translate("MainWindow", "U"))
        self.k12_box.setItemText(22, _translate("MainWindow", "V"))
        self.k12_box.setItemText(23, _translate("MainWindow", "X"))
        self.k12_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k12_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k12_box.setItemText(26, _translate("MainWindow", "0"))
        self.k12_box.setItemText(27, _translate("MainWindow", "1"))
        self.k12_box.setItemText(28, _translate("MainWindow", "2"))
        self.k12_box.setItemText(29, _translate("MainWindow", "3"))
        self.k12_box.setItemText(30, _translate("MainWindow", "4"))
        self.k12_box.setItemText(31, _translate("MainWindow", "5"))
        self.k12_box.setItemText(32, _translate("MainWindow", "6"))
        self.k12_box.setItemText(33, _translate("MainWindow", "7"))
        self.k12_box.setItemText(34, _translate("MainWindow", "8"))
        self.k12_box.setItemText(35, _translate("MainWindow", "9"))
        self.m10_box.setItemText(0, _translate("MainWindow", "ALT"))
        self.m10_box.setItemText(1, _translate("MainWindow", "CTRL/CMD"))
        self.k12b_box.setItemText(0, _translate("MainWindow", "NONE"))
        self.k12b_box.setItemText(1, _translate("MainWindow", "A"))
        self.k12b_box.setItemText(2, _translate("MainWindow", "B"))
        self.k12b_box.setItemText(3, _translate("MainWindow", "C"))
        self.k12b_box.setItemText(4, _translate("MainWindow", "D"))
        self.k12b_box.setItemText(5, _translate("MainWindow", "E"))
        self.k12b_box.setItemText(6, _translate("MainWindow", "F"))
        self.k12b_box.setItemText(7, _translate("MainWindow", "G"))
        self.k12b_box.setItemText(8, _translate("MainWindow", "H"))
        self.k12b_box.setItemText(9, _translate("MainWindow", "I"))
        self.k12b_box.setItemText(10, _translate("MainWindow", "J"))
        self.k12b_box.setItemText(11, _translate("MainWindow", "K"))
        self.k12b_box.setItemText(12, _translate("MainWindow", "L"))
        self.k12b_box.setItemText(13, _translate("MainWindow", "M"))
        self.k12b_box.setItemText(14, _translate("MainWindow", "N"))
        self.k12b_box.setItemText(15, _translate("MainWindow", "O"))
        self.k12b_box.setItemText(16, _translate("MainWindow", "P"))
        self.k12b_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k12b_box.setItemText(18, _translate("MainWindow", "R"))
        self.k12b_box.setItemText(19, _translate("MainWindow", "S"))
        self.k12b_box.setItemText(20, _translate("MainWindow", "T"))
        self.k12b_box.setItemText(21, _translate("MainWindow", "U"))
        self.k12b_box.setItemText(22, _translate("MainWindow", "V"))
        self.k12b_box.setItemText(23, _translate("MainWindow", "W"))
        self.k12b_box.setItemText(24, _translate("MainWindow", "X"))
        self.k12b_box.setItemText(25, _translate("MainWindow", "Y"))
        self.k12b_box.setItemText(26, _translate("MainWindow", "Z"))
        self.k12b_box.setItemText(27, _translate("MainWindow", "0"))
        self.k12b_box.setItemText(28, _translate("MainWindow", "1"))
        self.k12b_box.setItemText(29, _translate("MainWindow", "2"))
        self.k12b_box.setItemText(30, _translate("MainWindow", "3"))
        self.k12b_box.setItemText(31, _translate("MainWindow", "4"))
        self.k12b_box.setItemText(32, _translate("MainWindow", "5"))
        self.k12b_box.setItemText(33, _translate("MainWindow", "6"))
        self.k12b_box.setItemText(34, _translate("MainWindow", "7"))
        self.k12b_box.setItemText(35, _translate("MainWindow", "8"))
        self.k12b_box.setItemText(36, _translate("MainWindow", "9"))
        self.k2_box.setItemText(0, _translate("MainWindow", "S"))
        self.k2_box.setItemText(1, _translate("MainWindow", "A"))
        self.k2_box.setItemText(2, _translate("MainWindow", "B"))
        self.k2_box.setItemText(3, _translate("MainWindow", "C"))
        self.k2_box.setItemText(4, _translate("MainWindow", "D"))
        self.k2_box.setItemText(5, _translate("MainWindow", "E"))
        self.k2_box.setItemText(6, _translate("MainWindow", "F"))
        self.k2_box.setItemText(7, _translate("MainWindow", "G"))
        self.k2_box.setItemText(8, _translate("MainWindow", "H"))
        self.k2_box.setItemText(9, _translate("MainWindow", "I"))
        self.k2_box.setItemText(10, _translate("MainWindow", "J"))
        self.k2_box.setItemText(11, _translate("MainWindow", "K"))
        self.k2_box.setItemText(12, _translate("MainWindow", "L"))
        self.k2_box.setItemText(13, _translate("MainWindow", "M"))
        self.k2_box.setItemText(14, _translate("MainWindow", "N"))
        self.k2_box.setItemText(15, _translate("MainWindow", "O"))
        self.k2_box.setItemText(16, _translate("MainWindow", "P"))
        self.k2_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k2_box.setItemText(18, _translate("MainWindow", "R"))
        self.k2_box.setItemText(19, _translate("MainWindow", "T"))
        self.k2_box.setItemText(20, _translate("MainWindow", "U"))
        self.k2_box.setItemText(21, _translate("MainWindow", "V"))
        self.k2_box.setItemText(22, _translate("MainWindow", "W"))
        self.k2_box.setItemText(23, _translate("MainWindow", "X"))
        self.k2_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k2_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k2_box.setItemText(26, _translate("MainWindow", "0"))
        self.k2_box.setItemText(27, _translate("MainWindow", "1"))
        self.k2_box.setItemText(28, _translate("MainWindow", "2"))
        self.k2_box.setItemText(29, _translate("MainWindow", "3"))
        self.k2_box.setItemText(30, _translate("MainWindow", "4"))
        self.k2_box.setItemText(31, _translate("MainWindow", "5"))
        self.k2_box.setItemText(32, _translate("MainWindow", "6"))
        self.k2_box.setItemText(33, _translate("MainWindow", "7"))
        self.k2_box.setItemText(34, _translate("MainWindow", "8"))
        self.k2_box.setItemText(35, _translate("MainWindow", "9"))
        self.k3_box.setItemText(0, _translate("MainWindow", "S"))
        self.k3_box.setItemText(1, _translate("MainWindow", "A"))
        self.k3_box.setItemText(2, _translate("MainWindow", "B"))
        self.k3_box.setItemText(3, _translate("MainWindow", "C"))
        self.k3_box.setItemText(4, _translate("MainWindow", "D"))
        self.k3_box.setItemText(5, _translate("MainWindow", "E"))
        self.k3_box.setItemText(6, _translate("MainWindow", "F"))
        self.k3_box.setItemText(7, _translate("MainWindow", "G"))
        self.k3_box.setItemText(8, _translate("MainWindow", "H"))
        self.k3_box.setItemText(9, _translate("MainWindow", "I"))
        self.k3_box.setItemText(10, _translate("MainWindow", "J"))
        self.k3_box.setItemText(11, _translate("MainWindow", "K"))
        self.k3_box.setItemText(12, _translate("MainWindow", "L"))
        self.k3_box.setItemText(13, _translate("MainWindow", "M"))
        self.k3_box.setItemText(14, _translate("MainWindow", "N"))
        self.k3_box.setItemText(15, _translate("MainWindow", "O"))
        self.k3_box.setItemText(16, _translate("MainWindow", "P"))
        self.k3_box.setItemText(17, _translate("MainWindow", "Q"))
        self.k3_box.setItemText(18, _translate("MainWindow", "R"))
        self.k3_box.setItemText(19, _translate("MainWindow", "T"))
        self.k3_box.setItemText(20, _translate("MainWindow", "U"))
        self.k3_box.setItemText(21, _translate("MainWindow", "V"))
        self.k3_box.setItemText(22, _translate("MainWindow", "W"))
        self.k3_box.setItemText(23, _translate("MainWindow", "X"))
        self.k3_box.setItemText(24, _translate("MainWindow", "Y"))
        self.k3_box.setItemText(25, _translate("MainWindow", "Z"))
        self.k3_box.setItemText(26, _translate("MainWindow", "0"))
        self.k3_box.setItemText(27, _translate("MainWindow", "1"))
        self.k3_box.setItemText(28, _translate("MainWindow", "2"))
        self.k3_box.setItemText(29, _translate("MainWindow", "3"))
        self.k3_box.setItemText(30, _translate("MainWindow", "4"))
        self.k3_box.setItemText(31, _translate("MainWindow", "5"))
        self.k3_box.setItemText(32, _translate("MainWindow", "6"))
        self.k3_box.setItemText(33, _translate("MainWindow", "7"))
        self.k3_box.setItemText(34, _translate("MainWindow", "8"))
        self.k3_box.setItemText(35, _translate("MainWindow", "9"))

# class Updates Window

if __name__ == '__main__':

    store.init()

    # Checking if login exists

    if store.check_login() == True:
        app = QApplication(sys.argv)
        Main_Window = QtWidgets.QMainWindow()
        ui = MainWindow()
        ui.setupUi(Main_Window)
        Main_Window.show()
        sys.exit(app.exec_())
    
    else:
        app = QApplication(sys.argv)
        Auth_Window = QtWidgets.QMainWindow()
        ui = AuthWindow()
        ui.setupUi(Auth_Window)
        Auth_Window.show()
        sys.exit(app.exec_())