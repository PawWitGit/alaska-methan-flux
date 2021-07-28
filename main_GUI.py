from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, _QOpenGLFunctions_2_0

from read_data import ReadData


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        """Create read_data.py objects"""

        read_data = ReadData("CH4_Flux_BigTrail_Goldstream_AK.csv")

        """Setup MainWindow"""

        MainWindow.setObjectName("Badanie danych")
        MainWindow.resize(500, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setStyleSheet("background-color: silver;")

        """Set Buttons Style sheet"""

        style_pushbuttons_sheet = (
            "QPushButton"
            "{"
            "background-color : lightblue;"
            "}"
            "QPushButton::pressed"
            "{"
            "background-color : lightgreen;"
            "}"
        )

        """PushButton Return Data file"""

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 4, 100, 50))
        self.pushButton_1.setStyleSheet(style_pushbuttons_sheet)
        font = QtGui.QFont()
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoFillBackground(True)
        self.pushButton_1.setText("klik")
        self.pushButton_1.setObjectName("pushButton_1")

        """Console return Label"""

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(10, 300, 481, 100))
        self.label_1.setObjectName("label_1")
        self.label_1.setFont(QtGui.QFont("Arial Black", 12))
        self.label_1.setStyleSheet(
            "QLabel { background-color : white; color : black; }"
        )

        """Buttons Actions"""

        self.pushButton_1.clicked.connect(
            lambda: read_data.return_data_file()
            or self.label_1.setText("Wczytano plik: \n" + read_data.lake_methan_history)
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
        self.pushButton_1.setText(
            _translate("MainWindow", "Wyświetl nazwę \npliku z danymi")
        )
        self.label_1.setText(_translate("MainWindow", "Console log"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
