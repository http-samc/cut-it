# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_shortcuts.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(305, 147)
        MainWindow.setStyleSheet(u"background-color: #130e2c;\n"
"border-radius: 15px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.window_label = QLabel(self.centralwidget)
        self.window_label.setObjectName(u"window_label")
        self.window_label.setGeometry(QRect(10, 10, 231, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
<<<<<<< Updated upstream
=======
        font.setWeight(50)
>>>>>>> Stashed changes
        self.window_label.setFont(font)
        self.window_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255)")
        self.fxn_box = QComboBox(self.centralwidget)
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.addItem("")
        self.fxn_box.setObjectName(u"fxn_box")
        self.fxn_box.setGeometry(QRect(10, 61, 181, 20))
        self.fxn_box.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(20, 100, 271, 23))
        self.save_button.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"\n"
"")
        self.keys = QKeySequenceEdit(self.centralwidget)
        self.keys.setObjectName(u"keys")
        self.keys.setGeometry(QRect(200, 60, 101, 20))
        self.keys.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
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
        self.window_label.setText(QCoreApplication.translate("MainWindow", u"Set Shortcuts:", None))
        self.fxn_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Cut-It (Primary Emphasis)", None))
        self.fxn_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Cut-It (Secondary Emphasis)", None))
        self.fxn_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Cut-It (Tertiary Emphasis)", None))
        self.fxn_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Minimize Text", None))
        self.fxn_box.setItemText(4, QCoreApplication.translate("MainWindow", u"AutoPoll", None))
        self.fxn_box.setItemText(5, QCoreApplication.translate("MainWindow", u"AutoCite", None))
        self.fxn_box.setItemText(6, QCoreApplication.translate("MainWindow", u"AutoPoll + AutoCite", None))
        self.fxn_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Save As PDF", None))
        self.fxn_box.setItemText(8, QCoreApplication.translate("MainWindow", u"Save Card In Progress", None))
        self.fxn_box.setItemText(9, QCoreApplication.translate("MainWindow", u"Open Shortcuts", None))
        self.fxn_box.setItemText(10, QCoreApplication.translate("MainWindow", u"Open Preferences", None))
        self.fxn_box.setItemText(11, QCoreApplication.translate("MainWindow", u"Close Window", None))

        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

