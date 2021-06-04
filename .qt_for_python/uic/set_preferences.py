# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_preferences.ui'
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
        MainWindow.resize(561, 502)
        MainWindow.setStyleSheet(u"background-color: #130e2c;\n"
"border-radius: 15px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.primary_highlight_box = QComboBox(self.centralwidget)
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.setObjectName(u"primary_highlight_box")
        self.primary_highlight_box.setGeometry(QRect(270, 130, 281, 22))
        self.primary_highlight_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.options_label = QLabel(self.centralwidget)
        self.options_label.setObjectName(u"options_label")
        self.options_label.setGeometry(QRect(270, 50, 281, 21))
        self.options_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.set_preferences_label = QLabel(self.centralwidget)
        self.set_preferences_label.setObjectName(u"set_preferences_label")
        self.set_preferences_label.setGeometry(QRect(10, 0, 231, 41))
        font = QFont()
        font.setFamily(u"Segoe UI Semilight")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
<<<<<<< Updated upstream
=======
        font.setWeight(50)
>>>>>>> Stashed changes
        self.set_preferences_label.setFont(font)
        self.set_preferences_label.setStyleSheet(u"font: 24pt \"Segoe UI Semilight\";\n"
"color: rgb(140, 84, 255)")
        self.primary_emphasis_box = QComboBox(self.centralwidget)
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.setObjectName(u"primary_emphasis_box")
        self.primary_emphasis_box.setGeometry(QRect(270, 330, 281, 22))
        self.primary_emphasis_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.font_size_cut_box = QComboBox(self.centralwidget)
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.addItem("")
        self.font_size_cut_box.setObjectName(u"font_size_cut_box")
        self.font_size_cut_box.setGeometry(QRect(270, 210, 281, 22))
        self.font_size_cut_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.save_button = QPushButton(self.centralwidget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(180, 450, 221, 23))
        self.save_button.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"\n"
"")
        self.category_label = QLabel(self.centralwidget)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(10, 50, 241, 21))
        self.category_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_label = QLabel(self.centralwidget)
        self.font_label.setObjectName(u"font_label")
        self.font_label.setGeometry(QRect(10, 90, 241, 21))
        self.font_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.primary_highlight_label = QLabel(self.centralwidget)
        self.primary_highlight_label.setObjectName(u"primary_highlight_label")
        self.primary_highlight_label.setGeometry(QRect(10, 130, 241, 21))
        self.primary_highlight_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_cut_label = QLabel(self.centralwidget)
        self.font_size_cut_label.setObjectName(u"font_size_cut_label")
        self.font_size_cut_label.setGeometry(QRect(10, 210, 241, 21))
        self.font_size_cut_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_normal_label = QLabel(self.centralwidget)
        self.font_size_normal_label.setObjectName(u"font_size_normal_label")
        self.font_size_normal_label.setGeometry(QRect(10, 250, 241, 21))
        self.font_size_normal_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_min_label = QLabel(self.centralwidget)
        self.font_size_min_label.setObjectName(u"font_size_min_label")
        self.font_size_min_label.setGeometry(QRect(10, 290, 241, 21))
        self.font_size_min_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.primary_emphasis_label = QLabel(self.centralwidget)
        self.primary_emphasis_label.setObjectName(u"primary_emphasis_label")
        self.primary_emphasis_label.setGeometry(QRect(10, 330, 241, 21))
        self.primary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.secondary_emphasis_label = QLabel(self.centralwidget)
        self.secondary_emphasis_label.setObjectName(u"secondary_emphasis_label")
        self.secondary_emphasis_label.setGeometry(QRect(10, 370, 241, 21))
        self.secondary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.tertiary_emphasis_label = QLabel(self.centralwidget)
        self.tertiary_emphasis_label.setObjectName(u"tertiary_emphasis_label")
        self.tertiary_emphasis_label.setGeometry(QRect(10, 410, 241, 21))
        self.tertiary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.secondary_highlight_label = QLabel(self.centralwidget)
        self.secondary_highlight_label.setObjectName(u"secondary_highlight_label")
        self.secondary_highlight_label.setGeometry(QRect(10, 170, 241, 21))
        self.secondary_highlight_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.secondary_highlight_box = QComboBox(self.centralwidget)
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.setObjectName(u"secondary_highlight_box")
        self.secondary_highlight_box.setGeometry(QRect(270, 170, 281, 22))
        self.secondary_highlight_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.font_size_normal_box = QComboBox(self.centralwidget)
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.addItem("")
        self.font_size_normal_box.setObjectName(u"font_size_normal_box")
        self.font_size_normal_box.setGeometry(QRect(270, 250, 281, 22))
        self.font_size_normal_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.font_size_min_box = QComboBox(self.centralwidget)
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.addItem("")
        self.font_size_min_box.setObjectName(u"font_size_min_box")
        self.font_size_min_box.setGeometry(QRect(270, 290, 281, 22))
        self.font_size_min_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.secondary_emphasis_box = QComboBox(self.centralwidget)
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.setObjectName(u"secondary_emphasis_box")
        self.secondary_emphasis_box.setGeometry(QRect(270, 370, 281, 22))
        self.secondary_emphasis_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.tertiary_emphasis_box = QComboBox(self.centralwidget)
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.setObjectName(u"tertiary_emphasis_box")
        self.tertiary_emphasis_box.setGeometry(QRect(270, 410, 281, 22))
        self.tertiary_emphasis_box.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
"")
        self.fontComboBox = QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(270, 90, 281, 22))
        self.fontComboBox.setStyleSheet(u"background-color: rgb(234, 242, 248);\n"
"color: rgb(26, 82, 118);\n"
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
        self.primary_highlight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.primary_highlight_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.primary_highlight_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.primary_highlight_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.primary_highlight_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.primary_highlight_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))

        self.options_label.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.set_preferences_label.setText(QCoreApplication.translate("MainWindow", u"Set Preferences:", None))
        self.primary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Primary)", None))
        self.primary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Primary) + Italicized", None))
        self.primary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.primary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.primary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.primary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.primary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Italicized", None))

        self.font_size_cut_box.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_cut_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_cut_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_cut_box.setItemText(3, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_cut_box.setItemText(4, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_cut_box.setItemText(5, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_cut_box.setItemText(6, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_cut_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_cut_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.font_label.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.primary_highlight_label.setText(QCoreApplication.translate("MainWindow", u"Primary Highlight Color", None))
        self.font_size_cut_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Primary Emphasis", None))
        self.font_size_normal_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Normal Text", None))
        self.font_size_min_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Minimized Text", None))
        self.primary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Primary Emphasis Settings", None))
        self.secondary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Secondary Emphasis Settings", None))
        self.tertiary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Tertiary Emphasis Settings", None))
        self.secondary_highlight_label.setText(QCoreApplication.translate("MainWindow", u"Secondary Highlight Color", None))
        self.secondary_highlight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Green", None))
        self.secondary_highlight_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.secondary_highlight_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.secondary_highlight_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.secondary_highlight_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.secondary_highlight_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))

        self.font_size_normal_box.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_normal_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_normal_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_normal_box.setItemText(3, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_normal_box.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_normal_box.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_normal_box.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_normal_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_normal_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.font_size_min_box.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_min_box.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_min_box.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_min_box.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_min_box.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_min_box.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_min_box.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_min_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_min_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.secondary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.secondary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.secondary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Italicized", None))
        self.secondary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.secondary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.secondary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary)", None))
        self.secondary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary) + Italicized", None))

        self.tertiary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.tertiary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.tertiary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Italicized", None))
        self.tertiary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.tertiary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.tertiary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary)", None))
        self.tertiary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary) + Italicized", None))

    # retranslateUi

