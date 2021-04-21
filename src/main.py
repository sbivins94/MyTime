import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("", self)


