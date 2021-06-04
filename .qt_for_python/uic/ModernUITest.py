# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModernUITest.ui'
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
        MainWindow.resize(708, 500)
        MainWindow.setStyleSheet(u"color: #d3d3d3;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color: #d3d3d3;")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.plainTextEdit = QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout_3.addWidget(self.plainTextEdit, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 2, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_4)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_5.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_5.addWidget(self.pushButton_3, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.plainTextEdit_2 = QPlainTextEdit(self.groupBox_3)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.gridLayout_4.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setCursor(QCursor(Qt.WaitCursor))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Scrape Custom Data", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter Tournament URL's to Scrape (Tabroom Homepage)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter Division Keywords", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Scraping", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Generate Competitor Report", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Enter Event URL (Tabroom Entries Page)", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Generate Report", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"User Agreement", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"This agreement defines the relationship between You (the User), the Software (this program), and the Company (Offtime Roadmap, LLC). The software may not be relabled or redistributed by You, the User, in any capacity - regardless of whether or not a monetary gain is involved. The Company makes no guarentee, neither explicit nor implicit, regarding the functionality and the long term support of the Software. The company makes no guarentee that the Software will not crash, and by installing the Software, You, the User, agree to the risk of this occuring and are solely responsible for the damages that could be incurred. The Company is in no way, shape, or form associated with Tabroom.com or the National Speech and Debate association. All information pulled is publicly available. This program was written by Samarth Chitgopekar, the CTO of Offtime Roadmap, LLC. See https://github.com/http-samc for the Source Code to the Software and more. By using the Software to any extent, you agree to these terms and conditions.", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Need Help? Click here to Read the Docs", None))
    # retranslateUi

