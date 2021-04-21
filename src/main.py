import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        loadUi("task-log_v02.ui",self)

# main
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")