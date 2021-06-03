# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Beta.ui'
##
## Created by: Qt User Interface Compiler version 6.0.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(364, 280)
        Dialog.setStyleSheet(u"background-color: #130e2c;\n"
"")
        self.zoom = QSpinBox(Dialog)
        self.zoom.setObjectName(u"zoom")
        self.zoom.setGeometry(QRect(180, 90, 161, 21))
        self.zoom.setStyleSheet(u"background-color:   #130e2c; \n"
"color: rgb(169, 204, 227);\n"
"border: none;\n"
"outline: none;\n"
"padding: 5px;")
        self.window_label = QLabel(Dialog)
        self.window_label.setObjectName(u"window_label")
        self.window_label.setGeometry(QRect(50, 20, 261, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.window_label.setFont(font)
        self.window_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255)")
        self.zoom_label = QLabel(Dialog)
        self.zoom_label.setObjectName(u"zoom_label")
        self.zoom_label.setGeometry(QRect(30, 90, 121, 21))
        self.zoom_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.updates_button = QPushButton(Dialog)
        self.updates_button.setObjectName(u"updates_button")
        self.updates_button.setGeometry(QRect(30, 170, 311, 23))
        self.updates_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.legal = QLabel(Dialog)
        self.legal.setObjectName(u"legal")
        self.legal.setGeometry(QRect(40, 210, 291, 51))
        self.legal.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 9.5pt;")
        self.sam_plug = QPushButton(Dialog)
        self.sam_plug.setObjectName(u"sam_plug")
        self.sam_plug.setGeometry(QRect(30, 130, 311, 23))
        self.sam_plug.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.window_label.setText(QCoreApplication.translate("Dialog", u"Beta Settings/Info:", None))
        self.zoom_label.setText(QCoreApplication.translate("Dialog", u"Text Zoom Level", None))
        self.updates_button.setText(QCoreApplication.translate("Dialog", u"Updates and Patches", None))
        self.legal.setText(QCoreApplication.translate("Dialog", u"Beta Versions are Available to All Authorized Users. \n"
"Offtime Roadmap, LLC is not responsible for any\n"
"damages that may incur while in the Beta phase.", None))
        self.sam_plug.setText(QCoreApplication.translate("Dialog", u"Developed by Samarth Chitgopekar (click for info)", None))
    # retranslateUi

