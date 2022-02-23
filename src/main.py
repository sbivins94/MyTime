import sys
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QWidget, QTableWidget

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.resize(920, 723)
        # loadUi("task-log_v02.ui",self)

        self.centralwidget = QWidget(MainWindow)
        # self.input_table = QTableWidget(32, 5, self.centralwidget)
        # self.input_table.setGeometry(QtCore.QRect(10, 40, 491, 611))
        self.input_table = InputTable(32, 5, self.centralwidget)
        self.input_table.setColumnWidth(0,200)

class InputTable(QTableWidget):
    """Table into which user inputs daily tasks"""
    def __init__(self, rows, cols, parent):
        super().__init__(rows, cols, parent)
        self.setGeometry(QtCore.QRect(10, 40, 491, 611))
        # self.setGeometry(10, 40, 491, 611)
        # self.setRowCount(32)
        # self.setColumnCount(5)

        

# main
app = QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow(MainWindow)
MainWindow.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")