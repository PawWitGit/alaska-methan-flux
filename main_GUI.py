from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("Badanie danych")
        MainWindow.resize(400, 400)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
