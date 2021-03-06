from requests import api

from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0


""" In the following class, are located GUI elements
    App working with PyQT5 """


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(9, 4, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet(
            "QPushButton"
            "{"
            "background-color : lightblue;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color : lightgreen;"
            "}"
        )
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 35, 400, 20))
        self.label.setObjectName("label")
        self.label.setFont(QFont("Times New Roman", 12))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 120, 400, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QFont("Times New Roman", 12))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 210, 1400, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(QFont("Times New Roman", 12))
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 310, 400, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(QFont("Times New Roman", 12))
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(770, 10, 400, 50))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(QFont("Times New Roman", 12))
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(770, 180, 400, 50))
        self.label_6.setObjectName("label_6")
        self.label_6.setFont(QFont("Times New Roman", 12))
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 90, 400, 50))
        self.label_7.setObjectName("label_7")
        self.label_7.setFont(QFont("Times New Roman", 12))
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 180, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 270, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(580, 0, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(580, 80, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 90, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(580, 170, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sterowanie piecem"))
        self.pushButton_7.setText(_translate("MainWindow", "Po????cz z baz?? danych"))
        # self.pushButton_8.setText(_translate("MainWindow", "Temp. W Katowicach"))
        # self.pushButton_9.setText(_translate("MainWindow", "Inf. o Temp. W JSON"))
        # self.pushButton_10.setText(_translate("MainWindow", "Tryb AUTO ON"))
        # self.pushButton_11.setText(_translate("MainWindow", "Tryb Manual ON"))
        # self.pushButton_12.setText(_translate("MainWindow", "Zapisanie Temp. do DB"))
        # self.pushButton_13.setText(_translate("MainWindow", "Zamknij Aplkacj??"))
        # self.label.setText(_translate("MainWindow", "<-- klik"))
        # self.label_2.setText(_translate("MainWindow", "<-- klik"))
        # self.label_3.setText(_translate("MainWindow", "<-- klik"))
        # self.label_4.setText(_translate("MainWindow", "<-- klik"))
        # self.label_5.setText(_translate("MainWindow", "<-- klik"))
        # self.label_6.setText(
        #     _translate(
        #         "MainWindow", "Wy????cz aplikacj?? \n przerwij sterowanie pieca z apki"
        #     )
        # )
        # self.label_7.setText(_translate("MainWindow", "<-- klik"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
