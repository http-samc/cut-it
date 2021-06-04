# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in.ui'
##
<<<<<<< Updated upstream
## Created by: Qt User Interface Compiler version 6.0.3
=======
## Created by: Qt User Interface Compiler version 5.15.2
>>>>>>> Stashed changes
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

<<<<<<< Updated upstream
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
=======
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
>>>>>>> Stashed changes


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 270)
        Dialog.setStyleSheet(u"background-color: #130e2c;")
        self.email_input = QLineEdit(Dialog)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(10, 70, 381, 31))
        self.email_input.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"border-radius:5px;")
        self.pass_input = QLineEdit(Dialog)
        self.pass_input.setObjectName(u"pass_input")
        self.pass_input.setGeometry(QRect(10, 120, 381, 31))
        self.pass_input.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"border-radius:5px;")
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.msg_box = QLabel(Dialog)
        self.msg_box.setObjectName(u"msg_box")
        self.msg_box.setGeometry(QRect(10, 210, 381, 41))
        self.msg_box.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(140, 84, 255);\n"
"color: rgb(26, 82, 118);\n"
"border-radius:10px;\n"
"color: #130e2c;\n"
"font: 9pt;\n"
"")
        self.log_in_button = QPushButton(Dialog)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setGeometry(QRect(10, 170, 381, 23))
        self.log_in_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.auth_label = QLabel(Dialog)
        self.auth_label.setObjectName(u"auth_label")
        self.auth_label.setGeometry(QRect(150, 10, 111, 41))
        self.auth_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.email_input.setText("")
        self.pass_input.setText("")
        self.msg_box.setText(QCoreApplication.translate("Dialog", u"Welcome! Please sign up with a valid email and password\n"
"(8 characters, 1 uppercase, 1 lowercase) or log in.", None))
        self.log_in_button.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.auth_label.setText(QCoreApplication.translate("Dialog", u"Log In:", None))
    # retranslateUi

