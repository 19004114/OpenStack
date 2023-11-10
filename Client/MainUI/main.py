from PyQt5 import QtCore, QtGui, QtWidgets
from API import get_container

list_container = get_container.get_data()
btn_list = get_container.get_data()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 183, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_list = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_list.setContentsMargins(0, 0, 0, 0)
        self.main_list.setObjectName("main_list")
        self.run_VM = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_VM.sizePolicy().hasHeightForWidth())
        self.run_VM.setSizePolicy(sizePolicy)
        self.run_VM.setMinimumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.run_VM.setFont(font)
        self.run_VM.setIconSize(QtCore.QSize(16, 16))
        self.run_VM.setObjectName("run_VM")
        self.main_list.addWidget(self.run_VM)
        self.group_Containers = QtWidgets.QGroupBox(self.centralwidget)
        self.group_Containers.setGeometry(QtCore.QRect(210, 90, 571, 441))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.group_Containers.setFont(font)
        self.group_Containers.setAlignment(QtCore.Qt.AlignCenter)
        self.group_Containers.setFlat(False)
        self.group_Containers.setObjectName("group_Containers")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.group_Containers)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 160, 411))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.containers_list_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.containers_list_1.setContentsMargins(0, 0, 0, 0)
        self.containers_list_1.setObjectName("containers_list_1")

        if len(list_container) <= 4:
            for i in range(len(list_container)):
                btn_list[i]['name'] = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
                btn_list[i]['name'].setMinimumSize(QtCore.QSize(100, 50))
                btn_list[i]['name'].setObjectName(list_container[i]['name'])
                self.containers_list_1.addWidget(btn_list[i]['name'])

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.group_Containers)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(200, 20, 161, 411))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.containers_list_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.containers_list_2.setContentsMargins(0, 0, 0, 0)
        self.containers_list_2.setObjectName("containers_list_2")

        if len(list_container) <= 8 and len(list_container) > 4:
            for i in range(5, len(list_container)):
                btn_list[i]['name'] = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
                btn_list[i]['name'].setMinimumSize(QtCore.QSize(100, 50))
                btn_list[i]['name'].setObjectName(list_container[i]['name'])
                self.containers_list_2.addWidget(btn_list[i]['name'])

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.group_Containers)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(390, 20, 160, 411))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.containers_list_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.containers_list_3.setContentsMargins(0, 0, 0, 0)
        self.containers_list_3.setObjectName("containers_list_3")

        if len(list_container) <= 12 and len(list_container) > 8:
            for i in range(9, len(list_container)):
                btn_list[i]['name'] = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
                btn_list[i]['name'].setMinimumSize(QtCore.QSize(100, 50))
                btn_list[i]['name'].setObjectName(list_container[i]['name'])
                self.containers_list_3.addWidget(btn_list[i]['name'])

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run_VM.setText(_translate("MainWindow", "CHẠY MÁY ẢO"))
        self.group_Containers.setTitle(_translate("MainWindow", "DANH SÁCH DỊCH VỤ"))

        for i in range(len(list_container)):
            btn_list[i]['name'].setText(_translate("MainWindow", list_container[i]['name']))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
