
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class UpdateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("self")
        self.resize(501, 514)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.info = QtWidgets.QTextEdit(self)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(14)
        self.info.setFont(font)
        self.info.setReadOnly(True)
        self.info.setObjectName("info")
        self.gridLayout.addWidget(self.info, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtWidgets.QPushButton(self.groupBox)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.ignore = QtWidgets.QPushButton(self.groupBox)
        self.ignore.setObjectName("ignore")
        self.horizontalLayout.addWidget(self.ignore)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label.setText(_translate("self", "Cut-It Update Available!"))
        self.info.setHtml(_translate("self", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Segoe UI Semilight\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Emoji\'; font-size:8.25pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Segoe UI Emoji\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("self", "Options"))
        self.update.setText(_translate("self", "Update Now"))
        self.ignore.setText(_translate("self", "Remind Me later"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw = UpdateDialog()
    mw.show()
    sys.exit(app.exec_())
