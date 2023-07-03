from pyvir import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()



    #ui.listWidget.addItem(print_items())
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

