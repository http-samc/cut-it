from PyQt5 import QtCore, QtGui, QtWidgets


class LogIn(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 270)
        Dialog.setStyleSheet("background-color: #130e2c;")
        self.email_input = QtWidgets.QLineEdit(Dialog)
        self.email_input.setGeometry(QtCore.QRect(10, 70, 381, 31))
        self.email_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.email_input.setText("")
        self.email_input.setObjectName("email_input")
        self.email_input.setPlaceholderText("Enter your E-Mail here")
        self.pass_input = QtWidgets.QLineEdit(Dialog)
        self.pass_input.setGeometry(QtCore.QRect(10, 120, 381, 31))
        self.pass_input.setStyleSheet("background-color: rgb(234, 242, 248);\n"
        "color: rgb(26, 82, 118);\n"
        "border-radius:5px;")
        self.pass_input.setText("")
        self.pass_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_input.setObjectName("pass_input")
        self.pass_input.setPlaceholderText("Enter your password here")
        self.msg_box = QtWidgets.QLabel(Dialog)
        self.msg_box.setGeometry(QtCore.QRect(10, 210, 381, 41))
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
        self.msg_box.setObjectName("msg_box")
        self.log_in_button = QtWidgets.QPushButton(Dialog)
        self.log_in_button.setGeometry(QtCore.QRect(10, 170, 381, 23))
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
        self.auth_label = QtWidgets.QLabel(Dialog)
        self.auth_label.setGeometry(QtCore.QRect(150, 10, 111, 41))
        self.auth_label.setStyleSheet("font: 24pt \"Segoe UI Semilight\";\n"
        "color: rgb(140, 84, 255);")
        self.auth_label.setObjectName("auth_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log In - Cut-It™ by Offtime Roadmap®"))
        self.msg_box.setText(_translate("Dialog", "Welcome! Please log in. Email us (hello@cutit.cards) if you need help."))
        self.log_in_button.setText(_translate("Dialog", "Log In"))
        self.auth_label.setText(_translate("Dialog", "Log In:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = LogIn()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
