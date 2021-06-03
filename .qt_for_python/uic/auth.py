# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(421, 190)
        MainWindow.setStyleSheet(u"background-color: #130e2c;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.auth_label = QLabel(self.centralwidget)
        self.auth_label.setObjectName(u"auth_label")
        self.auth_label.setGeometry(QRect(30, 10, 361, 51))
        self.auth_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255);")
        self.sign_up_button = QPushButton(self.centralwidget)
        self.sign_up_button.setObjectName(u"sign_up_button")
        self.sign_up_button.setGeometry(QRect(20, 80, 181, 23))
        self.sign_up_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.log_in_button = QPushButton(self.centralwidget)
        self.log_in_button.setObjectName(u"log_in_button")
        self.log_in_button.setGeometry(QRect(220, 80, 181, 23))
        self.log_in_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.msg_box = QLabel(self.centralwidget)
        self.msg_box.setObjectName(u"msg_box")
        self.msg_box.setGeometry(QRect(20, 120, 381, 41))
        self.msg_box.setStyleSheet(u"text-align: center;\n"
"background-color: rgb(140, 84, 255);\n"
"color: rgb(26, 82, 118);\n"
"border-radius:10px;\n"
"color: #130e2c;\n"
"font: 9pt;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.auth_label.setText(QCoreApplication.translate("MainWindow", u"Please Authenticate Below", None))
        self.sign_up_button.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.log_in_button.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
        self.msg_box.setText(QCoreApplication.translate("MainWindow", u"Welcome! Please sign up with a valid email and password\n"
"(8 characters, 1 uppercase, 1 lowercase) or log in.", None))
    # retranslateUi

