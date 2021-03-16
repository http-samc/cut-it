from PyQt5 import QtCore, QtGui, QtWidgets
from api.resource import PATH
from api.auth_tools import tools
from pynotifier import Notification

# TODO implement cached login data
# TODO implement loading screen
# TODO use in-app msg box, not pynotifier

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        
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

        if tools.log_in(EMAIL, PASSWORD) == True:
            self.log_out()
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
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())