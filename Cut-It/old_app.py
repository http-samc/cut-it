from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget)
from PyQt5 import QtCore, QtGui, QtWidgets
from api.QComboBoxPlus import ExtendedComboBox
from PyQt5.QtWidgets import QFileDialog
from api.feedback import send_feedback
from api.export import make, PrintPDF
from api.settings import Settings
from api.QBrowser import Browser
from api.auth_tools import tools
from bs4 import BeautifulSoup
from api.resource import PATH
from api.version import check
from PyQt5.QtCore import *
from api.citer import cite
from api.texter import text
from api.texter import news
from api.data import store
# For WIN, comment out this line
from api.clipboard_OSX import clipboard 
# For OSX, comment out this line
from api.clipboard_WIN import clipboard 
import sys
import os

"""
@beta info:
0.5.1 : add ctrl+f
0.5.2 : add keep selected text
0.5.3 : QDialog class w/ custom message + loading wheel
0.5.4 : Log in/Sign up rework
"""

global settings
settings = Settings()

"""
Main Windows
"""
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
                             "border: none;"
                             "outline: none;"
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
                             "border: none;"
                             "outline: none;"
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

    """
    Appreciated in 0.5.4@beta (for direct in-app signup)
    """
    def sign_up_(self):

        self.widget = QWidget()
        self.browser = Browser('Sign Up - Cut-It™')
        self.browser.setupUi(self.widget)
        self.browser.setURL("http://api.flare-software.live/otr/cut-it/signup")
        self.browser.show()
        self.Auth_window.close()

    """
    Depreciated in 0.5.4@beta (for direct in-app signup)
    """
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
        
        #Setting up MainWindow
        MainWindow.closeEvent = self.closeEvent
        MainWindow.setObjectName("MainWindow")

        if settings.WS():
            MainWindow.setFixedSize(890, 580)
        
        else:
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

        self.evidence_box.setGeometry(QtCore.QRect(330, 20, 541, 481))
        self.evidence_box.setObjectName("evidence_box")
        self.evidence_box.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:10px;\n"
        "")

        font = QtGui.QFont()
        font.setFamily(settings.font())
        font.setWeight(int(settings.FSNT()))
        self.evidence_box.setFont(font)
        self.evidence_box.zoomIn(store.getData()["zoom"])

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
        self.shortcuts()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.selectCard()

    """
    Utils
    """
    def selectCard(self):
        self.dialog = QtWidgets.QDialog()
        self.beta = CardDialog()
        self.beta.setupUi(self.dialog)
        self.dialog.exec_()
        self.index = None
        self.loadCard()

    def loadCard(self):
        self.index = store.getCurrentCard()
        
        document = self.evidence_box.document()
        document.clear()

        if self.index is None:
            self.warrant_input.setText("")
            self.cite_input.setText("")
            self.creds_input.setText("")
            self.link_input.setText("")
            return
        
        card = store.getCard()
        self.warrant_input.setText(card["tag"])
        self.cite_input.setText(card["cite"])
        self.creds_input.setText(card["creds"])
        self.link_input.setText(card["link"])
        cursor = self.evidence_box.textCursor()

        cursor.insertHtml(card["html"])
        cursor.setPosition(0, QtGui.QTextCursor.MoveAnchor)
        self.evidence_box.setTextCursor(cursor)

    def closeEvent(self, event):

        evidence_data = self.toHTML()
        tag = self.warrant_input.text()
        cite = self.cite_input.text()
        creds = self.creds_input.text()
        link = self.link_input.text()

        card = {
            "tag" : tag,
            "cite" : cite,
            "creds" : creds,
            "link" : link,
            "html" : evidence_data[1],
            "text" : evidence_data[0]
        }

        if self.index is None:
            store.addCard(card)

        else:
            store.updateCard(card, self.index)

        event.accept()

    def shortcuts(self):

        # CF DONE
        CF = QShortcut(QtGui.QKeySequence('Ctrl+Z'), self.evidence_box)
        CF.activated.connect(self.clearFormatting)

        # Find
        KST = QShortcut(QtGui.QKeySequence('Ctrl+F'), self.evidence_box)
        KST.activated.connect(self.find)
        self.cursor_find = self.evidence_box.textCursor()

        # KST TODO
        KST = QShortcut(QtGui.QKeySequence(settings.KST()), self.evidence_box)
        KST.activated.connect(self.keepSelectedText)

        # PE DONE
        PE = QShortcut(QtGui.QKeySequence(settings.PE()), self.evidence_box)
        PE.activated.connect(self.cut_it)

        # SE DONE

        SE = QShortcut(QtGui.QKeySequence(settings.SE()), self.evidence_box)
        SE.activated.connect(self.secondary_emphasis)

        # TE DONE

        TE = QShortcut(QtGui.QKeySequence(settings.TE()), self.evidence_box)
        TE.activated.connect(self.tertiary_emphasis)

        # MT DONE

        MT = QShortcut(QtGui.QKeySequence(settings.MT()), self.evidence_box)
        MT.activated.connect(self.MT)

        # AP DONE

        AP = QShortcut(QtGui.QKeySequence(settings.AP()), self.evidence_box)
        AP.activated.connect(self.AP)

        # AC DONE

        AC = QShortcut(QtGui.QKeySequence(settings.AC()), self.evidence_box)
        AC.activated.connect(self.AC)

        # AP_AC DONE

        AP_AC = QShortcut(QtGui.QKeySequence(settings.AP_AC()), self.evidence_box)
        AP_AC.activated.connect(self.AP_AC)

        # PDF DONE

        PDF = QShortcut(QtGui.QKeySequence(settings.PDF()), self.evidence_box)
        PDF.activated.connect(self.print)

        # NC

        NC = QShortcut(QtGui.QKeySequence(settings.IP()), self.evidence_box)
        NC.activated.connect(self.openNewCard)

        # OS DONE

        OS = QShortcut(QtGui.QKeySequence(settings.OS()), self.evidence_box)
        OS.activated.connect(self.settings)

        # CW DONE

        CW = QShortcut(QtGui.QKeySequence(settings.CW()), self.evidence_box)
        CW.activated.connect(self.quit_)

    def toHTML(self):
        doc = self.evidence_box.document()
        soup = BeautifulSoup(doc.toHtml(), 'html.parser')
        html = str(soup.find('p'))
        html = html.replace('600', 'bold')
        html = f'<body style="font-family: {settings.font()}">' + html + '</body>'
        text = str(soup.text)
        return [text, html]

    def auto(self, autoCite, autoPoll):
        """
        Takes in 2 bools that can override the state of the checkboxes for each option,
        then executes them
        """

        URL = self.link_input.text()
        
        citation = f"""
        <p>
        """

        # If both Poll/Cite enabled
        if (self.autocite_box.isChecked() is True or autoCite is True) and (self.autopoll_box.isChecked() is True or autoPoll is True):

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

            return True

        #AutoCite checked Only
        elif (self.autocite_box.isChecked() is True) or (autoCite is True):
            
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
            
            return True

        #Autopoll Checked Only
        elif (self.autopoll_box.isChecked() is True) or (autoPoll is True):
            
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

            return True

        else:
            return False  

    def cut_it(self):
        
        # If user has checked one or both auto boxes, it will exec that first. else, it will assume you want to style
        if self.auto(False, False) == True:
            return None
        
        self.primary_emphasis()

    """
    Shortcut call wrappers
    """
    
    def find(self):
        # TODO: implement w/ extraselections
        return None        
        # document = self.evidence_box.document()
        # if self.cursor_find.hasSelection():
        #     FROM = self.cursor_find.selectionEnd()
        # else:
        #     FROM = 0
        # self.cursor_find = document.find("the", FROM)
        # self.evidence_box.setTextCursor(self.cursor_find)

    def keepSelectedText(self):
        # TODO Implement
        return None

    def clearFormatting(self):
        cursor  = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        selection_plain = cursor.selectedText()
        cursor.insertText(selection_plain)

    def MT(self):
        
        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        selection = cursor.selectedText()
        
        selection = self.size(selection, settings.FSMT())
        cursor.removeSelectedText()        
        cursor.insertHtml(selection)
        
        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def AC(self):
        self.auto(True, False)

    def AP(self):
        self.auto(False, True)   
    
    def AP_AC(self):
        self.auto(True, True)

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

        if filename != "/.pdf":
            try:
                self.widget = QWidget()
                self.browser = PrintPDF(html, filename)
                self.browser.setupUi(self.widget)
            
            except Exception:
                pass

    def openNewCard(self):
        evidence_data = self.toHTML()
        tag = self.warrant_input.text()
        cite = self.cite_input.text()
        creds = self.creds_input.text()
        link = self.link_input.text()

        card = {
            "tag" : tag,
            "cite" : cite,
            "creds" : creds,
            "link" : link,
            "html" : evidence_data[1],
            "text" : evidence_data[0]
        }

        if self.index is None:
            store.addCard(card)

        else:
            store.updateCard(card, self.index)
        
        self.selectCard()

    def quit_(self):
        if settings.LI() == False:
            store.log_out()
        quit()

    """
    emphasis levels
    """
    def primary_emphasis(self):
        """
        Formats using Primary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        
        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.PES()

        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.PHC(), settings.FSPE()) if config[3] else self.size(selection, settings.FSPE())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def secondary_emphasis(self):
        """
        Formats using Secondary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None

        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.SES()

        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.SHC(), settings.FSNT()) if config[3] else self.size(selection, settings.FSNT())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    def tertiary_emphasis(self):
        """
        Formats using Tertiary emphasis
        """

        cursor = self.evidence_box.textCursor()
        if cursor.hasSelection() == False:
            return None
        
        START = cursor.selectionStart()

        selection = cursor.selectedText()
        config = settings.TES()

        selection = self.italic(selection) if config[0] else selection
        selection = self.bold(selection) if config[1] else selection
        selection = self.underline(selection) if config[2] else selection
        selection = self.highlight(selection, settings.SHC(), settings.FSNT()) if config[3] else self.size(selection, settings.FSNT())
        
        cursor.insertHtml(selection)
        cursor.setPosition(START, QtGui.QTextCursor.KeepAnchor)
        self.evidence_box.setTextCursor(cursor)

        data = self.toHTML()
        clipboard.add(data[0], data[1])

    """
    styling methods
    """
    def italic(self, html):
        """
        italicises selected text
        """
             
        return f"<em>{html}</em>"

    def bold(self, html):
        """
        adds html bolding to str
        """
   
        return f"<b>{html}</b>"

    def underline(self, html):
        """
        adds html underlining to str
        """  

        return f"<u>{html}</u>"
        
    def highlight(self, html, color, font_size):
        """
        adds html highlighting to str
        """
        return f"<span style='background-color: {color}; font-size: {font_size}pt;'>{html}</span>"

    def size(self, html, font_size):
        """
        adds html font resizing to str
        """
        return f"<span style='font-size: {font_size}pt;'>{html}</span>"

    """
    Misc.
    """
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
        self.version.setText(_translate("MainWindow", "v.0.5.0"))
        self.autopoll_box.setText(_translate("MainWindow", "AutoPoll"))

class SettingsWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        MainWindow.setFixedSize(1051, 537)
        MainWindow.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pref_box = QtWidgets.QGroupBox(self.centralwidget)
        self.pref_box.setGeometry(QtCore.QRect(30, 20, 611, 481))
        self.pref_box.setStyleSheet("QGroupBox {\n"
        "border: 1px solid rgb(169, 204, 227);;\n"
        "border-color: rgb(169, 204, 227);\n"
        "margin-top: 7px;\n"
        "font-size: 14px;\n"
        "border-radius: 15px;\n"
        "}\n"
        "QGroupBox::title {\n"
        "padding: 2px 82px;\n"
        "background-color:  rgb(140, 84, 255);\n"
        "border-radius: 5px;\n"
        "color: #130e2c;\n"
        "}")
        self.pref_box.setObjectName("pref_box")
        self.secondary_emphasis_box = QtWidgets.QComboBox(self.pref_box)
        self.secondary_emphasis_box.setGeometry(QtCore.QRect(290, 370, 281, 22))
        self.secondary_emphasis_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.secondary_emphasis_box.setObjectName("secondary_emphasis_box")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.font_label = QtWidgets.QLabel(self.pref_box)
        self.font_label.setGeometry(QtCore.QRect(30, 90, 241, 21))
        self.font_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;\n"
        "border: none;\n"
        "outline: none;")
        self.font_label.setObjectName("font_label")
        self.secondary_emphasis_label = QtWidgets.QLabel(self.pref_box)
        self.secondary_emphasis_label.setGeometry(QtCore.QRect(30, 370, 241, 21))
        self.secondary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.secondary_emphasis_label.setObjectName("secondary_emphasis_label")
        self.font_size_cut_label = QtWidgets.QLabel(self.pref_box)
        self.font_size_cut_label.setGeometry(QtCore.QRect(30, 210, 241, 21))
        self.font_size_cut_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_cut_label.setObjectName("font_size_cut_label")
        self.category_label = QtWidgets.QLabel(self.pref_box)
        self.category_label.setGeometry(QtCore.QRect(30, 50, 241, 21))
        self.category_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.category_label.setObjectName("category_label")
        self.primary_emphasis_label = QtWidgets.QLabel(self.pref_box)
        self.primary_emphasis_label.setGeometry(QtCore.QRect(30, 330, 241, 21))
        self.primary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.primary_emphasis_label.setObjectName("primary_emphasis_label")
        self.tertiary_emphasis_box = QtWidgets.QComboBox(self.pref_box)
        self.tertiary_emphasis_box.setGeometry(QtCore.QRect(290, 410, 281, 22))
        self.tertiary_emphasis_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.tertiary_emphasis_box.setObjectName("tertiary_emphasis_box")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.secondary_highlight_box = QtWidgets.QComboBox(self.pref_box)
        self.secondary_highlight_box.setGeometry(QtCore.QRect(290, 170, 281, 22))
        self.secondary_highlight_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.secondary_highlight_box.setObjectName("secondary_highlight_box")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.options_label = QtWidgets.QLabel(self.pref_box)
        self.options_label.setGeometry(QtCore.QRect(290, 50, 281, 21))
        self.options_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.options_label.setObjectName("options_label")
        self.fontComboBox = QtWidgets.QFontComboBox(self.pref_box)
        self.fontComboBox.setGeometry(QtCore.QRect(290, 90, 281, 22))
        self.fontComboBox.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.fontComboBox.setObjectName("fontComboBox")
        self.font_size_cut_box = QtWidgets.QComboBox(self.pref_box)
        self.font_size_cut_box.setGeometry(QtCore.QRect(290, 210, 281, 22))
        self.font_size_cut_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
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
        self.tertiary_emphasis_label = QtWidgets.QLabel(self.pref_box)
        self.tertiary_emphasis_label.setGeometry(QtCore.QRect(30, 410, 241, 21))
        self.tertiary_emphasis_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.tertiary_emphasis_label.setObjectName("tertiary_emphasis_label")
        self.primary_highlight_box = QtWidgets.QComboBox(self.pref_box)
        self.primary_highlight_box.setGeometry(QtCore.QRect(290, 130, 281, 22))
        self.primary_highlight_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.primary_highlight_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.primary_highlight_box.setObjectName("primary_highlight_box")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.font_size_min_box = QtWidgets.QComboBox(self.pref_box)
        self.font_size_min_box.setGeometry(QtCore.QRect(290, 290, 281, 22))
        self.font_size_min_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
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
        self.primary_emphasis_box = QtWidgets.QComboBox(self.pref_box)
        self.primary_emphasis_box.setGeometry(QtCore.QRect(290, 330, 281, 22))
        self.primary_emphasis_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
        self.primary_emphasis_box.setObjectName("primary_emphasis_box")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_highlight_label = QtWidgets.QLabel(self.pref_box)
        self.primary_highlight_label.setGeometry(QtCore.QRect(30, 130, 241, 21))
        self.primary_highlight_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.primary_highlight_label.setObjectName("primary_highlight_label")
        self.font_size_normal_box = QtWidgets.QComboBox(self.pref_box)
        self.font_size_normal_box.setGeometry(QtCore.QRect(290, 250, 281, 22))
        self.font_size_normal_box.setStyleSheet("background-color:  rgb(140, 84, 255);\n"
        "color: #130e2c;\n"        
        "border: none;\n"
        "outline: none;")
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
        self.font_size_normal_label = QtWidgets.QLabel(self.pref_box)
        self.font_size_normal_label.setGeometry(QtCore.QRect(30, 250, 241, 21))
        self.font_size_normal_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_normal_label.setObjectName("font_size_normal_label")
        self.secondary_highlight_label = QtWidgets.QLabel(self.pref_box)
        self.secondary_highlight_label.setGeometry(QtCore.QRect(30, 170, 241, 21))
        self.secondary_highlight_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.secondary_highlight_label.setObjectName("secondary_highlight_label")
        self.font_size_min_label = QtWidgets.QLabel(self.pref_box)
        self.font_size_min_label.setGeometry(QtCore.QRect(30, 290, 241, 21))
        self.font_size_min_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.font_size_min_label.setObjectName("font_size_min_label")
        self.short_box = QtWidgets.QGroupBox(self.centralwidget)
        self.short_box.setGeometry(QtCore.QRect(670, 20, 351, 91))
        self.short_box.setStyleSheet("QGroupBox {\n"
        "border: 1px solid rgb(169, 204, 227);;\n"
        "border-color: rgb(169, 204, 227);\n"
        "margin-top: 7px;\n"
        "font-size: 14px;\n"
        "border-radius: 15px;\n"
        "}\n"
        "QGroupBox::title {\n"
        "padding: 2px 82px;\n"
        "background-color:  rgb(140, 84, 255);\n"
        "border-radius: 5px;\n"
        "color: #130e2c;\n"
        "}")
        self.short_box.setObjectName("short_box")
        self.edit_shorts = QtWidgets.QPushButton(self.short_box)
        self.edit_shorts.setGeometry(QtCore.QRect(20, 50, 311, 21))
        self.edit_shorts.setStyleSheet("background-color: rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "border-radius:10px;\n"
        "\n"
        "")
        self.style(self.edit_shorts)
        self.edit_shorts.setObjectName("edit_shorts")
        self.misc_box = QtWidgets.QGroupBox(self.centralwidget)
        self.misc_box.setGeometry(QtCore.QRect(670, 130, 351, 371))
        self.misc_box.setStyleSheet("QGroupBox {\n"
        "border: 1px solid rgb(169, 204, 227);;\n"
        "border-color: rgb(169, 204, 227);\n"
        "margin-top: 7px;\n"
        "font-size: 14px;\n"
        "border-radius: 15px;\n"
        "}\n"
        "QGroupBox::title {\n"
        "padding: 2px 82px;\n"
        "background-color:  rgb(140, 84, 255);\n"
        "border-radius: 5px;\n"
        "color: #130e2c;\n"
        "}")
        self.misc_box.setObjectName("misc_box")
        self.updates_button = QtWidgets.QPushButton(self.misc_box)
        self.updates_button.setGeometry(QtCore.QRect(20, 50, 151, 23))
        self.updates_button.setStyleSheet("background-color : rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "border-radius:10px;\n"
        "")
        self.style(self.updates_button)
        self.updates_button.setObjectName("updates_button")
        self.log_out_button = QtWidgets.QPushButton(self.misc_box)
        self.log_out_button.setGeometry(QtCore.QRect(180, 50, 151, 23))
        self.log_out_button.setStyleSheet("background-color : rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "border-radius:10px;\n"
        "")
        self.log_out_button.setObjectName("log_out_button")
        self.style(self.log_out_button)
        self.window_size_box = QtWidgets.QCheckBox(self.misc_box)
        self.window_size_box.setGeometry(QtCore.QRect(30, 80, 111, 31))
        self.window_size_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.window_size_box.setObjectName("window_size_box")
        
        self.stay_logged_in_box = QtWidgets.QCheckBox(self.misc_box)
        self.stay_logged_in_box.setGeometry(QtCore.QRect(180, 80, 111, 31))
        self.stay_logged_in_box.setStyleSheet("color: rgb(169, 204, 227)")
        self.stay_logged_in_box.setObjectName("stay_logged_in_box")
        self.feedback_box = QtWidgets.QGroupBox(self.misc_box)
        self.feedback_box.setGeometry(QtCore.QRect(20, 110, 311, 201))
        self.feedback_box.setStyleSheet("QGroupBox {\n"
        "border: 1px solid rgb(169, 204, 227);\n"
        "border-color: rgb(169, 204, 227);\n"
        "margin-top: 7px;\n"
        "font-size: 14px;\n"
        "border-radius: 15px;\n"
        "}\n"
        "QGroupBox::title {\n"
        "padding: 2px 82px;\n"
        "background-color:  rgb(140, 84, 255);\n"
        "border-radius: 5px;\n"
        "color: #130e2c;\n"
        "}")
        self.feedback_box.setObjectName("feedback_box")
        self.feedback = QtWidgets.QTextEdit(self.feedback_box)
        self.feedback.setGeometry(QtCore.QRect(10, 40, 291, 101))
        self.feedback.setStyleSheet("background-color: #130e2c;\n"
        "color: rgb(169, 204, 227);\n"
        "border-radius:10px;\n"
        "border: 1px solid rgb(140, 84, 255);\n"
        "\n"
        "")
        self.feedback.setObjectName("feedback")
        self.submit_feedback = QtWidgets.QPushButton(self.feedback_box)
        self.submit_feedback.setGeometry(QtCore.QRect(30, 160, 251, 23))
        self.submit_feedback.setStyleSheet("background-color: rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "border-radius:10px;\n"
        "\n"
        "")
        self.submit_feedback.setObjectName("submit_feedback")
        self.submit_feedback.clicked.connect(self.push_feedback)
        self.style(self.submit_feedback)
        self.save_button = QtWidgets.QPushButton(self.misc_box)
        self.save_button.setGeometry(QtCore.QRect(50, 330, 251, 21))
        self.save_button.setStyleSheet("background-color: rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "border-radius:10px;\n"
        "\n"
        "")
        self.style(self.save_button)
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.save_button.clicked.connect(self.save_config)
        self.updates_button.clicked.connect(self.open_beta)
        self.edit_shorts.clicked.connect(self.open_shortcuts)
        self.log_out_button.clicked.connect(self.log_out)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.load_config()
        MainWindow.move(100, 350)

    def push_feedback(self):
        send_feedback(store.getData()["login"]["email"], self.feedback.toPlainText())
        self.feedback.clear()
        self.feedback.setPlaceholderText("Thank you for submitting your feedback!")

    def log_out(self):
        store.log_out()
        quit()

    def style(self, button):
        button.setStyleSheet("QPushButton"
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

    def load_config(self):
        masterdata = store.getData()

        self.window_size_box.setCheckState(masterdata["fixed_win"])
        self.stay_logged_in_box.setCheckState(masterdata["stay_logged_in"])

        data = masterdata["settings"]["preferences"]
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
        store.add_prefs(data)
        store.add_misc(self.window_size_box.isChecked(), self.stay_logged_in_box.isChecked())

    def open_beta(self):
        self.dialog = QtWidgets.QDialog()
        self.beta = Beta()
        self.beta.setupUi(self.dialog)
        self.dialog.exec_()

    def open_shortcuts(self):
        self.dialog = QtWidgets.QDialog()
        self.shortcuts = Shortcuts()
        self.shortcuts.setupUi(self.dialog)
        self.dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings - Cut-It™"))
        self.pref_box.setTitle(_translate("MainWindow", "Preferences"))
        self.secondary_emphasis_box.setItemText(0, _translate("MainWindow", "Bold"))
        self.secondary_emphasis_box.setItemText(1, _translate("MainWindow", "Underline"))
        self.secondary_emphasis_box.setItemText(2, _translate("MainWindow", "Italicized"))
        self.secondary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.secondary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.secondary_emphasis_box.setItemText(5, _translate("MainWindow", "Bold + Underline + Highlight (Secondary)"))
        self.secondary_emphasis_box.setItemText(6, _translate("MainWindow", "Bold + Underline + Highlight (Secondary) + Italicized"))
        self.font_label.setText(_translate("MainWindow", "Font"))
        self.secondary_emphasis_label.setText(_translate("MainWindow", "Secondary Emphasis Settings"))
        self.font_size_cut_label.setText(_translate("MainWindow", "Font Size of Primary Emphasis"))
        self.category_label.setText(_translate("MainWindow", "Category"))
        self.primary_emphasis_label.setText(_translate("MainWindow", "Primary Emphasis Settings"))
        self.tertiary_emphasis_box.setItemText(0, _translate("MainWindow", "Underline"))
        self.tertiary_emphasis_box.setItemText(1, _translate("MainWindow", "Bold"))
        self.tertiary_emphasis_box.setItemText(2, _translate("MainWindow", "Italicized"))
        self.tertiary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.tertiary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.tertiary_emphasis_box.setItemText(5, _translate("MainWindow", "Bold + Underline + Highlight (Secondary)"))
        self.tertiary_emphasis_box.setItemText(6, _translate("MainWindow", "Bold + Underline + Highlight (Secondary) + Italicized"))
        self.secondary_highlight_box.setItemText(0, _translate("MainWindow", "Green"))
        self.secondary_highlight_box.setItemText(1, _translate("MainWindow", "Cyan"))
        self.secondary_highlight_box.setItemText(2, _translate("MainWindow", "Magenta"))
        self.secondary_highlight_box.setItemText(3, _translate("MainWindow", "Blue"))
        self.secondary_highlight_box.setItemText(4, _translate("MainWindow", "Purple"))
        self.secondary_highlight_box.setItemText(5, _translate("MainWindow", "Yellow"))
        self.options_label.setText(_translate("MainWindow", "Options"))
        self.font_size_cut_box.setItemText(0, _translate("MainWindow", "12"))
        self.font_size_cut_box.setItemText(1, _translate("MainWindow", "2"))
        self.font_size_cut_box.setItemText(2, _translate("MainWindow", "4"))
        self.font_size_cut_box.setItemText(3, _translate("MainWindow", "6"))
        self.font_size_cut_box.setItemText(4, _translate("MainWindow", "8"))
        self.font_size_cut_box.setItemText(5, _translate("MainWindow", "10"))
        self.font_size_cut_box.setItemText(6, _translate("MainWindow", "11"))
        self.font_size_cut_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_cut_box.setItemText(8, _translate("MainWindow", "16"))
        self.tertiary_emphasis_label.setText(_translate("MainWindow", "Tertiary Emphasis Settings"))
        self.primary_highlight_box.setItemText(0, _translate("MainWindow", "Cyan"))
        self.primary_highlight_box.setItemText(1, _translate("MainWindow", "Green"))
        self.primary_highlight_box.setItemText(2, _translate("MainWindow", "Magenta"))
        self.primary_highlight_box.setItemText(3, _translate("MainWindow", "Blue"))
        self.primary_highlight_box.setItemText(4, _translate("MainWindow", "Purple"))
        self.primary_highlight_box.setItemText(5, _translate("MainWindow", "Yellow"))
        self.font_size_min_box.setItemText(0, _translate("MainWindow", "2"))
        self.font_size_min_box.setItemText(1, _translate("MainWindow", "4"))
        self.font_size_min_box.setItemText(2, _translate("MainWindow", "6"))
        self.font_size_min_box.setItemText(3, _translate("MainWindow", "8"))
        self.font_size_min_box.setItemText(4, _translate("MainWindow", "10"))
        self.font_size_min_box.setItemText(5, _translate("MainWindow", "11"))
        self.font_size_min_box.setItemText(6, _translate("MainWindow", "12"))
        self.font_size_min_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_min_box.setItemText(8, _translate("MainWindow", "16"))
        self.primary_emphasis_box.setItemText(0, _translate("MainWindow", "Bold + Underline + Highlight (Primary)"))
        self.primary_emphasis_box.setItemText(1, _translate("MainWindow", "Bold + Underline + Highlight (Primary) + Italicized"))
        self.primary_emphasis_box.setItemText(2, _translate("MainWindow", "Bold + Underline + Italicized"))
        self.primary_emphasis_box.setItemText(3, _translate("MainWindow", "Bold + Underline"))
        self.primary_emphasis_box.setItemText(4, _translate("MainWindow", "Bold"))
        self.primary_emphasis_box.setItemText(5, _translate("MainWindow", "Underline"))
        self.primary_emphasis_box.setItemText(6, _translate("MainWindow", "Italicized"))
        self.primary_highlight_label.setText(_translate("MainWindow", "Primary Highlight Color"))
        self.font_size_normal_box.setItemText(0, _translate("MainWindow", "8"))
        self.font_size_normal_box.setItemText(1, _translate("MainWindow", "2"))
        self.font_size_normal_box.setItemText(2, _translate("MainWindow", "4"))
        self.font_size_normal_box.setItemText(3, _translate("MainWindow", "6"))
        self.font_size_normal_box.setItemText(4, _translate("MainWindow", "10"))
        self.font_size_normal_box.setItemText(5, _translate("MainWindow", "11"))
        self.font_size_normal_box.setItemText(6, _translate("MainWindow", "12"))
        self.font_size_normal_box.setItemText(7, _translate("MainWindow", "14"))
        self.font_size_normal_box.setItemText(8, _translate("MainWindow", "16"))
        self.font_size_normal_label.setText(_translate("MainWindow", "Font Size of Normal Text"))
        self.secondary_highlight_label.setText(_translate("MainWindow", "Secondary Highlight Color"))
        self.font_size_min_label.setText(_translate("MainWindow", "Font Size of Minimized Text"))
        self.short_box.setTitle(_translate("MainWindow", "Shortcuts"))
        self.edit_shorts.setText(_translate("MainWindow", "Record/View Shortcuts"))
        self.misc_box.setTitle(_translate("MainWindow", "Miscellaneous"))
        self.updates_button.setText(_translate("MainWindow", "Updates"))
        self.log_out_button.setText(_translate("MainWindow", "Log Out"))
        self.window_size_box.setText(_translate("MainWindow", "Lock Window Size"))
        self.stay_logged_in_box.setText(_translate("MainWindow", "Stay Logged In"))
        self.feedback_box.setTitle(_translate("MainWindow", "Feedback"))
        self.feedback.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\"></span></p></body></html>"))
        self.feedback.setPlaceholderText("Bugs? Feature Requests? Tokens of appreciation? Let us know here!")
        self.submit_feedback.setText(_translate("MainWindow", "Submit"))
        self.save_button.setText(_translate("MainWindow", "Save All"))

"""
Dialogs
"""
class Shortcuts(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(402, 254)
        Dialog.setStyleSheet("background-color: #130e2c;\n"
        "border-radius: 15px;")
        Dialog.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        self.shortcuts = QtWidgets.QComboBox(Dialog)
        self.shortcuts.setGeometry(QtCore.QRect(20, 110, 361, 21))
        self.shortcuts.setStyleSheet("background-color: rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "")
        self.shortcuts.setObjectName("shortcuts")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("")
        self.shortcuts.addItem("Keep Selected Text")
        self.shortcuts.currentTextChanged.connect(self.updateShortcut)
        self.window_label = QtWidgets.QLabel(Dialog)
        self.window_label.setGeometry(QtCore.QRect(20, 20, 351, 31))
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
        self.short_input = QtWidgets.QKeySequenceEdit(Dialog)
        self.short_input.setGeometry(QtCore.QRect(20, 190, 361, 21))
        self.short_input.setStyleSheet("background-color: rgb(140, 84, 255);\n"
        "color: #130e2c;\n"
        "padding: 5px;")
        self.short_input.setObjectName("short_input")
        self.short_input.editingFinished.connect(self.saveShortcuts)
        self.select_shortcut = QtWidgets.QLabel(Dialog)
        self.select_shortcut.setGeometry(QtCore.QRect(20, 70, 241, 21))
        self.select_shortcut.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.select_shortcut.setObjectName("select_shortcut")
        self.record_shortcut = QtWidgets.QLabel(Dialog)
        self.record_shortcut.setGeometry(QtCore.QRect(20, 150, 311, 21))
        self.record_shortcut.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.record_shortcut.setObjectName("record_shortcut")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def updateShortcut(self):
        data = store.getData()["settings"]["shortcuts"]
        self.short_input.setKeySequence(data[self.shortcuts.currentText()])

    def saveShortcuts(self):
        data = store.getData()
        sequence = self.short_input.keySequence()
        data["settings"]["shortcuts"][self.shortcuts.currentText()] = sequence.toString()
        store.setData(data)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Shortcuts - Cut-It™"))
        self.shortcuts.setItemText(0, _translate("Dialog", "Cut-It (Primary Emphasis)"))
        self.shortcuts.setItemText(1, _translate("Dialog", "Cut-It (Secondary Emphasis)"))
        self.shortcuts.setItemText(2, _translate("Dialog", "Cut-It (Tertiary Emphasis)"))
        self.shortcuts.setItemText(3, _translate("Dialog", "Minimize Text"))
        self.shortcuts.setItemText(4, _translate("Dialog", "AutoPoll"))
        self.shortcuts.setItemText(5, _translate("Dialog", "AutoCite"))
        self.shortcuts.setItemText(6, _translate("Dialog", "AutoPoll + AutoCite"))
        self.shortcuts.setItemText(7, _translate("Dialog", "Save As PDF"))
        self.shortcuts.setItemText(8, _translate("Dialog", "Open/Create Card"))
        self.shortcuts.setItemText(9, _translate("Dialog", "Open Settings"))
        self.shortcuts.setItemText(10, _translate("Dialog", "Close Window"))
        self.window_label.setText(_translate("Dialog", "Record & View Shortcuts:"))
        self.select_shortcut.setText(_translate("Dialog", "Select a Shortcut"))
        self.record_shortcut.setText(_translate("Dialog", "Click & Record A New Shortcut (if desired)"))

class Beta(object):

    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        Dialog.setObjectName("Dialog")
        Dialog.resize(364, 280)
        Dialog.setStyleSheet("background-color: #130e2c;\n"
        "")
        self.zoom = QtWidgets.QSpinBox(Dialog)
        self.zoom.setGeometry(QtCore.QRect(180, 90, 161, 21))
        self.zoom.setStyleSheet("background-color:   #130e2c; \n"
        "color: rgb(169, 204, 227);\n"
        "border: none;\n"
        "outline: none;\n"
        "padding: 5px;")
        self.zoom.setObjectName("zoom")
        self.window_label = QtWidgets.QLabel(Dialog)
        self.window_label.setGeometry(QtCore.QRect(50, 20, 261, 41))
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
        self.zoom_label = QtWidgets.QLabel(Dialog)
        self.zoom_label.setGeometry(QtCore.QRect(30, 90, 121, 21))
        self.zoom_label.setStyleSheet("color: rgb(169, 204, 227);\n"
        "font-size: 12pt;")
        self.zoom_label.setObjectName("zoom_label")
        self.updates_button = QtWidgets.QPushButton(Dialog)
        self.updates_button.setGeometry(QtCore.QRect(30, 170, 311, 23))
        self.updates_button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "border: none;"
                             "outline: none;"
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
        self.legal = QtWidgets.QLabel(Dialog)
        self.legal.setGeometry(QtCore.QRect(40, 210, 291, 51))
        self.legal.setStyleSheet("QLabel"
                             "{"
                             "color: rgb(169, 204, 227);"
                             "font: 9.5pt;"
                             "}"
                             "QLabel::hover"
                             "{"
                             "color: rgb(26, 82, 118);"
                             "font: 9.5pt;"
                             "}"
                             )
        self.legal.setObjectName("legal")
        self.sam_plug = QtWidgets.QPushButton(Dialog)
        self.sam_plug.setGeometry(QtCore.QRect(30, 130, 311, 23))
        self.sam_plug.setStyleSheet("QPushButton"
                             "{"
                             "background-color : rgb(140, 84, 255);"
                             "color: #130e2c;"
                             "border-radius:10px;"
                             "border: none;"
                             "outline: none;"
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
        self.sam_plug.setObjectName("sam_plug")
        self.sam_plug.clicked.connect(self.open_sam_plug)
        self.updates_button.clicked.connect(self.open_updates)
        self.zoom.setValue(store.getData()["zoom"])
        self.zoom.valueChanged.connect(self.save_config)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def save_config(self):
        store.setZoom(self.zoom.value())

    def open_updates(self):
        self.widget = QWidget()
        self.browser = Browser('Versions - Cut-It™')
        self.browser.setupUi(self.widget)
        self.browser.setURL("https://cut-it.gitbook.io/cut-it/")
        self.browser.show()
    
    def open_sam_plug(self):
        self.widget = QWidget()
        self.browser = Browser('http://sam-c.me/')
        self.browser.setupUi(self.widget)
        self.browser.setURL("http://sam-c.me/")
        self.browser.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Beta - Cut-It™"))
        self.window_label.setText(_translate("Dialog", "Beta Settings/Info:"))
        self.zoom_label.setText(_translate("Dialog", "Text Zoom Level"))
        self.updates_button.setText(_translate("Dialog", "Updates and Patches"))
        self.legal.setText(_translate("Dialog", "Beta Versions are available to *authorized* users. \n"
        "Offtime Roadmap, LLC is not responsible for any\n"
        "damages that may incur while in the Beta phase."))
        self.sam_plug.setText(_translate("Dialog", "Developed by Samarth Chitgopekar (click for info)"))

class CardDialog(object):

    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(331, 121)
        Dialog.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))
        Dialog.setStyleSheet("background-color: #130e2c;\n"
        "font: 8pt \"Segoe UI Semibold\";")
        self.submit = QtWidgets.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(20, 80, 291, 21))
        self.submit.setStyleSheet("QPushButton"
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
        self.submit.clicked.connect(self.card_selected)
        self.submit.setObjectName("submit")
        self.cards = ExtendedComboBox(Dialog)
        self.cards.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.cards.setStyleSheet("background-color: #130e2c;\n"
        "color: rgb(140, 84, 255);\n"
        "border: none;\n"
        "font-size: 9.5pt;\n"
        "outline: none;")
        self.cards.currentIndexChanged.connect(self.reset_position)
        self.cards.setObjectName("cards")
        self.cards.addItem("")
        self.addOptions()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def reset_position(self):
        self.cards.goToStart()

    def addOptions(self):
        data = store.getCardData()["cards"]
        i = 0

        for card in data:
            name = None

            if self.clean(card["tag"]) != "":
                name = card["tag"]

            elif self.clean(card["text"]) != "":
                name = card["text"].replace("\n", "")
            
            if name != None:
                self.cards.addItem(f"{i}: {name}")
            
            i+=1
            
    def clean(self, text):
        return text.replace(" ", "").replace("\n", "").replace("\t", "")
    
    def card_selected(self):
        self.reset_position()
        store.setCurrentCard(str(self.cards.currentText())[0])
        self.Dialog.close()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Select Card - Cut-It™"))
        self.submit.setText(_translate("Dialog", "Start Cutting"))
        self.cards.setItemText(0, _translate("Dialog", "Cut a new card"))

if __name__ == '__main__':

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