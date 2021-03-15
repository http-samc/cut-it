from PyQt5 import QtCore, QtGui, QtWidgets
from api.resource import PATH
from api.auth_tools import tools
from pynotifier import Notification

# TODO implement cached login data
# TODO implement loading screen

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        
        #Setting up MainWindow
        MainWindow.setObjectName("MainWindow")
        self.mw = MainWindow
        MainWindow.setFixedSize(461, 281)
        MainWindow.setStyleSheet("background-color: #130e2c;")
        MainWindow.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(PATH.get('resources/otr_icon.png'))))

        #Setting up centralwidget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Setting up brand label
        self.brand_label = QtWidgets.QLabel(self.centralwidget)
        self.brand_label.setGeometry(QtCore.QRect(40, 20, 381, 51))
        self.brand_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255);")
        self.brand_label.setObjectName("brand_label")

        #Setting up email input
        self.email_input = QtWidgets.QLineEdit(self.centralwidget)
        self.email_input.setGeometry(QtCore.QRect(40, 100, 381, 31))
        self.email_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.email_input.setObjectName("email_input")

        #Setting up password input
        self.pass_input = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_input.setGeometry(QtCore.QRect(40, 160, 381, 31))
        self.pass_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.pass_input.setObjectName("pass_input")

        #Setting up sign up button
        self.sign_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.sign_up_button.setGeometry(QtCore.QRect(40, 220, 181, 23))
        self.sign_up_button.setStyleSheet("QPushButton"
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
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_up_button.clicked.connect(self.sign_up)

        #Setting up log in button
        self.log_in_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_button.setGeometry(QtCore.QRect(240, 220, 181, 23))
        self.log_in_button.setStyleSheet("QPushButton"
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
        self.log_in_button.setObjectName("log_in_button")
        self.log_in_button.clicked.connect(self.log_in)

        #Misc.
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
        self.brand_label.setText(_translate("MainWindow", "Please Authenticate Below"))
        self.pass_input.setText(_translate("MainWindow", "Password"))
        self.email_input.setText(_translate("MainWindow", "Email"))
        self.sign_up_button.setText(_translate("MainWindow", "Sign Up"))
        self.log_in_button.setText(_translate("MainWindow", "Log In"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())