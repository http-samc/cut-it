import qtmodern.windows
from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QApplication, QShortcut, QWidget, QDialog, QTextEdit, QVBoxLayout, QDialogButtonBox)
from PyQt5 import QtCore, QtGui, QtWidgets
import qtmodern.windows
import qtmodern.styles
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    d = qtmodern.windows.ModernDialog(QDialog(), parent=None)
    d.exec_()
    sys.exit(app.exec_())