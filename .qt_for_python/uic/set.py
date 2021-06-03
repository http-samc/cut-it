# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set.ui'
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
        MainWindow.resize(1051, 537)
        MainWindow.setStyleSheet(u"background-color: #130e2c;\n"
"border-radius: 15px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pref_box = QGroupBox(self.centralwidget)
        self.pref_box.setObjectName(u"pref_box")
        self.pref_box.setGeometry(QRect(30, 20, 611, 481))
        self.pref_box.setStyleSheet(u"QGroupBox {\n"
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
        self.secondary_emphasis_box = QComboBox(self.pref_box)
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.addItem("")
        self.secondary_emphasis_box.setObjectName(u"secondary_emphasis_box")
        self.secondary_emphasis_box.setGeometry(QRect(290, 370, 281, 22))
        self.secondary_emphasis_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.font_label = QLabel(self.pref_box)
        self.font_label.setObjectName(u"font_label")
        self.font_label.setGeometry(QRect(30, 90, 241, 21))
        self.font_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.secondary_emphasis_label = QLabel(self.pref_box)
        self.secondary_emphasis_label.setObjectName(u"secondary_emphasis_label")
        self.secondary_emphasis_label.setGeometry(QRect(30, 370, 241, 21))
        self.secondary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_cut_label = QLabel(self.pref_box)
        self.font_size_cut_label.setObjectName(u"font_size_cut_label")
        self.font_size_cut_label.setGeometry(QRect(30, 210, 241, 21))
        self.font_size_cut_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.category_label = QLabel(self.pref_box)
        self.category_label.setObjectName(u"category_label")
        self.category_label.setGeometry(QRect(30, 50, 241, 21))
        self.category_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.primary_emphasis_label = QLabel(self.pref_box)
        self.primary_emphasis_label.setObjectName(u"primary_emphasis_label")
        self.primary_emphasis_label.setGeometry(QRect(30, 330, 241, 21))
        self.primary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.tertiary_emphasis_box = QComboBox(self.pref_box)
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.addItem("")
        self.tertiary_emphasis_box.setObjectName(u"tertiary_emphasis_box")
        self.tertiary_emphasis_box.setGeometry(QRect(290, 410, 281, 22))
        self.tertiary_emphasis_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.secondary_highlight_box = QComboBox(self.pref_box)
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.addItem("")
        self.secondary_highlight_box.setObjectName(u"secondary_highlight_box")
        self.secondary_highlight_box.setGeometry(QRect(290, 170, 281, 22))
        self.secondary_highlight_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.options_label = QLabel(self.pref_box)
        self.options_label.setObjectName(u"options_label")
        self.options_label.setGeometry(QRect(290, 50, 281, 21))
        self.options_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.fontComboBox = QFontComboBox(self.pref_box)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(290, 90, 281, 22))
        self.fontComboBox.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.font_size_cut_box = QComboBox(self.pref_box)
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
        self.font_size_cut_box.setGeometry(QRect(290, 210, 281, 22))
        self.font_size_cut_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.tertiary_emphasis_label = QLabel(self.pref_box)
        self.tertiary_emphasis_label.setObjectName(u"tertiary_emphasis_label")
        self.tertiary_emphasis_label.setGeometry(QRect(30, 410, 241, 21))
        self.tertiary_emphasis_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.primary_highlight_box = QComboBox(self.pref_box)
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.addItem("")
        self.primary_highlight_box.setObjectName(u"primary_highlight_box")
        self.primary_highlight_box.setGeometry(QRect(290, 130, 281, 22))
        self.primary_highlight_box.setFocusPolicy(Qt.NoFocus)
        self.primary_highlight_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.font_size_min_box = QComboBox(self.pref_box)
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
        self.font_size_min_box.setGeometry(QRect(290, 290, 281, 22))
        self.font_size_min_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.primary_emphasis_box = QComboBox(self.pref_box)
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.addItem("")
        self.primary_emphasis_box.setObjectName(u"primary_emphasis_box")
        self.primary_emphasis_box.setGeometry(QRect(290, 330, 281, 22))
        self.primary_emphasis_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.primary_highlight_label = QLabel(self.pref_box)
        self.primary_highlight_label.setObjectName(u"primary_highlight_label")
        self.primary_highlight_label.setGeometry(QRect(30, 130, 241, 21))
        self.primary_highlight_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_normal_box = QComboBox(self.pref_box)
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
        self.font_size_normal_box.setGeometry(QRect(290, 250, 281, 22))
        self.font_size_normal_box.setStyleSheet(u"background-color:  rgb(140, 84, 255);\n"
"color: #130e2c;")
        self.font_size_normal_label = QLabel(self.pref_box)
        self.font_size_normal_label.setObjectName(u"font_size_normal_label")
        self.font_size_normal_label.setGeometry(QRect(30, 250, 241, 21))
        self.font_size_normal_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.secondary_highlight_label = QLabel(self.pref_box)
        self.secondary_highlight_label.setObjectName(u"secondary_highlight_label")
        self.secondary_highlight_label.setGeometry(QRect(30, 170, 241, 21))
        self.secondary_highlight_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.font_size_min_label = QLabel(self.pref_box)
        self.font_size_min_label.setObjectName(u"font_size_min_label")
        self.font_size_min_label.setGeometry(QRect(30, 290, 241, 21))
        self.font_size_min_label.setStyleSheet(u"color: rgb(169, 204, 227);\n"
"font-size: 12pt;")
        self.short_box = QGroupBox(self.centralwidget)
        self.short_box.setObjectName(u"short_box")
        self.short_box.setGeometry(QRect(670, 20, 351, 91))
        self.short_box.setStyleSheet(u"QGroupBox {\n"
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
        self.edit_shorts = QPushButton(self.short_box)
        self.edit_shorts.setObjectName(u"edit_shorts")
        self.edit_shorts.setGeometry(QRect(20, 50, 311, 21))
        self.edit_shorts.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"\n"
"")
        self.misc_box = QGroupBox(self.centralwidget)
        self.misc_box.setObjectName(u"misc_box")
        self.misc_box.setGeometry(QRect(670, 130, 351, 371))
        self.misc_box.setStyleSheet(u"QGroupBox {\n"
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
        self.updates_button = QPushButton(self.misc_box)
        self.updates_button.setObjectName(u"updates_button")
        self.updates_button.setGeometry(QRect(20, 50, 151, 23))
        self.updates_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.log_out_button = QPushButton(self.misc_box)
        self.log_out_button.setObjectName(u"log_out_button")
        self.log_out_button.setGeometry(QRect(180, 50, 151, 23))
        self.log_out_button.setStyleSheet(u"background-color : rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"")
        self.window_size_box = QCheckBox(self.misc_box)
        self.window_size_box.setObjectName(u"window_size_box")
        self.window_size_box.setGeometry(QRect(30, 80, 111, 31))
        self.window_size_box.setStyleSheet(u"color: rgb(169, 204, 227)")
        self.stay_logged_in_box = QCheckBox(self.misc_box)
        self.stay_logged_in_box.setObjectName(u"stay_logged_in_box")
        self.stay_logged_in_box.setGeometry(QRect(180, 80, 111, 31))
        self.stay_logged_in_box.setStyleSheet(u"color: rgb(169, 204, 227)")
        self.feedback_box = QGroupBox(self.misc_box)
        self.feedback_box.setObjectName(u"feedback_box")
        self.feedback_box.setGeometry(QRect(20, 110, 311, 201))
        self.feedback_box.setStyleSheet(u"QGroupBox {\n"
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
        self.feedback = QTextEdit(self.feedback_box)
        self.feedback.setObjectName(u"feedback")
        self.feedback.setGeometry(QRect(10, 40, 291, 101))
        self.feedback.setStyleSheet(u"background-color: #130e2c;\n"
"color: rgb(169, 204, 227);\n"
"border-radius:10px;\n"
"border: 1px solid rgb(140, 84, 255);\n"
"\n"
"")
        self.submit_feedback = QPushButton(self.feedback_box)
        self.submit_feedback.setObjectName(u"submit_feedback")
        self.submit_feedback.setGeometry(QRect(30, 160, 251, 23))
        self.submit_feedback.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"\n"
"")
        self.save_button = QPushButton(self.misc_box)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(50, 330, 251, 21))
        self.save_button.setStyleSheet(u"background-color: rgb(140, 84, 255);\n"
"color: #130e2c;\n"
"border-radius:10px;\n"
"\n"
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
        self.pref_box.setTitle(QCoreApplication.translate("MainWindow", u"Preferences", None))
        self.secondary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.secondary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.secondary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Italicized", None))
        self.secondary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.secondary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.secondary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary)", None))
        self.secondary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary) + Italicized", None))

        self.font_label.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.secondary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Secondary Emphasis Settings", None))
        self.font_size_cut_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Primary Emphasis", None))
        self.category_label.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.primary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Primary Emphasis Settings", None))
        self.tertiary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.tertiary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.tertiary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Italicized", None))
        self.tertiary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.tertiary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.tertiary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary)", None))
        self.tertiary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Secondary) + Italicized", None))

        self.secondary_highlight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Green", None))
        self.secondary_highlight_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.secondary_highlight_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.secondary_highlight_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.secondary_highlight_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.secondary_highlight_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))

        self.options_label.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.font_size_cut_box.setItemText(0, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_cut_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_cut_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_cut_box.setItemText(3, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_cut_box.setItemText(4, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_cut_box.setItemText(5, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_cut_box.setItemText(6, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_cut_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_cut_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.tertiary_emphasis_label.setText(QCoreApplication.translate("MainWindow", u"Tertiary Emphasis Settings", None))
        self.primary_highlight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Cyan", None))
        self.primary_highlight_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Green", None))
        self.primary_highlight_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Magenta", None))
        self.primary_highlight_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Blue", None))
        self.primary_highlight_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Purple", None))
        self.primary_highlight_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Yellow", None))

        self.font_size_min_box.setItemText(0, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_min_box.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_min_box.setItemText(2, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_min_box.setItemText(3, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_min_box.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_min_box.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_min_box.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_min_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_min_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.primary_emphasis_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Primary)", None))
        self.primary_emphasis_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Bold + Underline + Highlight (Primary) + Italicized", None))
        self.primary_emphasis_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Bold + Underline + Italicized", None))
        self.primary_emphasis_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Bold + Underline", None))
        self.primary_emphasis_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Bold", None))
        self.primary_emphasis_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Underline", None))
        self.primary_emphasis_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Italicized", None))

        self.primary_highlight_label.setText(QCoreApplication.translate("MainWindow", u"Primary Highlight Color", None))
        self.font_size_normal_box.setItemText(0, QCoreApplication.translate("MainWindow", u"8", None))
        self.font_size_normal_box.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.font_size_normal_box.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.font_size_normal_box.setItemText(3, QCoreApplication.translate("MainWindow", u"6", None))
        self.font_size_normal_box.setItemText(4, QCoreApplication.translate("MainWindow", u"10", None))
        self.font_size_normal_box.setItemText(5, QCoreApplication.translate("MainWindow", u"11", None))
        self.font_size_normal_box.setItemText(6, QCoreApplication.translate("MainWindow", u"12", None))
        self.font_size_normal_box.setItemText(7, QCoreApplication.translate("MainWindow", u"14", None))
        self.font_size_normal_box.setItemText(8, QCoreApplication.translate("MainWindow", u"16", None))

        self.font_size_normal_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Normal Text", None))
        self.secondary_highlight_label.setText(QCoreApplication.translate("MainWindow", u"Secondary Highlight Color", None))
        self.font_size_min_label.setText(QCoreApplication.translate("MainWindow", u"Font Size of Minimized Text", None))
        self.short_box.setTitle(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
        self.edit_shorts.setText(QCoreApplication.translate("MainWindow", u"Record/View Shortcuts", None))
        self.misc_box.setTitle(QCoreApplication.translate("MainWindow", u"Miscellaneous", None))
        self.updates_button.setText(QCoreApplication.translate("MainWindow", u"Updates", None))
        self.log_out_button.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.window_size_box.setText(QCoreApplication.translate("MainWindow", u"Lock Window Size", None))
        self.stay_logged_in_box.setText(QCoreApplication.translate("MainWindow", u"Stay Logged In", None))
        self.feedback_box.setTitle(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.feedback.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Bugs? Feature Requests? Let us know here!</span></p></body></html>", None))
        self.submit_feedback.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save All", None))
    # retranslateUi

