from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0

from read_data import ReadData


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        """Create read_data.py objects"""

        read_data = ReadData("CH4_Flux_BigTrail_Goldstream_AK.csv", "0")

        """Setup MainWindow"""

        MainWindow.setObjectName("Badanie danych")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setStyleSheet("background-color: silver;")
        # MainWindow.setStyleSheet("background-image:url(./file/data_image.jpg)")

        """Set Buttons Style sheet"""

        style_pushbuttons_sheet = (
            "QPushButton"
            "{"
            "border-width: 2px;"
            "border-radius: 8px;"
            "padding: 4px;"
            "background-color : lightblue;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color : lightgreen;"
            "border-width: 2px;"
            "border-radius: 8px;"
            "padding: 4px;"
            "}"
        )

        """pushbutton1 Return Data file"""

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 4, 120, 50))
        self.pushButton_1.setStyleSheet(style_pushbuttons_sheet)
        font = QtGui.QFont()
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoFillBackground(True)
        self.pushButton_1.setText("klik")
        self.pushButton_1.setObjectName("pushButton_1")

        """pushbutton2 Return data table"""

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 120, 50))
        self.pushButton_2.setStyleSheet(style_pushbuttons_sheet)
        font = QtGui.QFont()
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setText("klik")
        self.pushButton_2.setObjectName("pushButton_1")

        """pushbutton3 Return max methane value"""

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 116, 120, 50))
        self.pushButton_3.setStyleSheet(style_pushbuttons_sheet)
        font = QtGui.QFont()
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setText("klik")
        self.pushButton_3.setObjectName("pushButton_3")

        """pushbutton3 Return min methane value"""

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 116, 120, 50))
        self.pushButton_4.setStyleSheet(style_pushbuttons_sheet)
        font = QtGui.QFont()
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setText("klik")
        self.pushButton_4.setObjectName("pushButton_4")

        """Console return label"""

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 400, 380, 100))
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(QtGui.QFont("Arial Black", 12))
        self.label_1.setStyleSheet(
            "QLabel { background-color : white; color : black; }"
        )

        """Values console label log"""

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 200, 380, 100))
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QtGui.QFont("Arial Black", 12))
        self.label_2.setStyleSheet(
            "QLabel { background-color : white; color : black; }"
        )

        """Buttons Actions"""

        self.pushButton_1.clicked.connect(
            lambda: read_data.return_data_file()
            or self.label_1.setText("Load file: \n" + read_data.lake_methan_history)
        )

        self.pushButton_2.clicked.connect(
            lambda: read_data.return_data_table()
            or self.label_1.setText(
                read_data.lake_methan_history + ":\n" + "load view in your console"
            )
        )

        self.pushButton_3.clicked.connect(
            lambda: read_data.return_max_methane_value()
            or self.label_1.setText(
                read_data.lake_methan_history + ":\n" + "max methane value in console"
            )
            or self.label_2.setText(str(read_data.data_out))
        )

        self.pushButton_4.clicked.connect(
            lambda: read_data.return_min_methane_value()
            or self.label_1.setText(
                read_data.lake_methan_history + ":\n" + "min methane value in console"
            )
            or self.label_2.setText(str(read_data.data_out))
        )
        """Setup Menubar and retlanslateUI"""

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retlanslateUI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retlanslateUI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Control Panel"))
        self.pushButton_1.setText(_translate("MainWindow", "Show data file \nname"))
        self.pushButton_2.setText(_translate("MainWindow", "Show \n data"))
        self.pushButton_3.setText(_translate("MainWindow", "Show max\n methane value"))
        self.pushButton_4.setText(_translate("MainWindow", "Show min\n methane value"))
        self.label_1.setText(_translate("MainWindow", "Console log"))
        self.label_2.setText(_translate("MainWindow", "Values"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
