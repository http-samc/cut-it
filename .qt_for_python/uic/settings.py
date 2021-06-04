# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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
        MainWindow.resize(221, 299)
        MainWindow.setStyleSheet(u"background-color: #130e2c;\n"
"border-radius: 15px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.settings_label = QLabel(self.centralwidget)
        self.settings_label.setObjectName(u"settings_label")
        self.settings_label.setGeometry(QRect(60, 0, 111, 51))
        self.settings_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255);")
        self.preferences_button = QPushButton(self.centralwidget)
        self.preferences_button.setObjectName(u"preferences_button")
        self.preferences_button.setGeometry(QRect(20, 60, 181, 23))
        self.preferences_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.shortcuts_button = QPushButton(self.centralwidget)
        self.shortcuts_button.setObjectName(u"shortcuts_button")
        self.shortcuts_button.setGeometry(QRect(20, 100, 181, 23))
        self.shortcuts_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.updates_button = QPushButton(self.centralwidget)
        self.updates_button.setObjectName(u"updates_button")
        self.updates_button.setGeometry(QRect(20, 140, 181, 23))
        self.updates_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.log_out_button = QPushButton(self.centralwidget)
        self.log_out_button.setObjectName(u"log_out_button")
        self.log_out_button.setGeometry(QRect(20, 180, 181, 23))
        self.log_out_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.window_size_box = QCheckBox(self.centralwidget)
        self.window_size_box.setObjectName(u"window_size_box")
        self.window_size_box.setGeometry(QRect(50, 220, 111, 21))
        self.window_size_box.setStyleSheet(u"color: rgb(169, 204, 227)")
        self.stay_logged_in_box = QCheckBox(self.centralwidget)
        self.stay_logged_in_box.setObjectName(u"stay_logged_in_box")
        self.stay_logged_in_box.setGeometry(QRect(50, 250, 111, 21))
        self.stay_logged_in_box.setStyleSheet(u"color: rgb(169, 204, 227)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.settings_label.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.preferences_button.setText(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.shortcuts_button.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
        self.updates_button.setText(QCoreApplication.translate("MainWindow", u"Updates", None))
        self.log_out_button.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.window_size_box.setText(QCoreApplication.translate("MainWindow", u"Lock Window Size", None))
        self.stay_logged_in_box.setText(QCoreApplication.translate("MainWindow", u"Stay Logged In", None))
    # retranslateUi

