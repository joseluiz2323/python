

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 680)
        MainWindow.setStyleSheet("background-color: rgb(35, 45, 55);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 230, 45, 45))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-image: url(:/iconecriar/iconecriar.png);\n"
                                      "    background-repeat: no repeat;\n"
                                      "    background-position: center;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    background-image: url(:/iconecriar2/iconecriar2.png);\n"
                                      "    background-repeat: no repeat;\n"
                                      "    background-position: center;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 304, 45, 51))
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    background-image: url(:/iconemontar/iconemontar.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    \n"
                                        "    background-image: url(:/iconemontar2/iconemontar2.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 370, 45, 51))
        self.pushButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    \n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-image: url(:/iconeverificar/iconeverificar.png);\n"
                                        "    background-position: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    \n"
                                        "    \n"
                                        "    background-image: url(:/iconeverificar2/iconeverificar2.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 440, 45, 51))
        self.pushButton_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    background-repeat: no repeat;\n"
                                        "    \n"
                                        "    background-image: url(:/seguientresi/seguirentresi.png);\n"
                                        "    background-position: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    \n"
                                        "    background-image: url(:/iconesbutton/seguirentresi2.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 500, 45, 51))
        self.pushButton_5.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-image: url(:/verificadorgni/verificadorgni.png);\n"
                                        "    background-position: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-image: url(:/verificadorgni2/verificadorgni2.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 570, 45, 51))
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-image: url(:/iconeconfiguracao/iconeconfiguracao.png);\n"
                                        "    background-position: center;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-image: url(:/iconeconfiguracao2/iconeconfiguracao2.png);\n"
                                        "    background-repeat: no repeat;\n"
                                        "    background-position: center;\n"
                                        "}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(5, 20, 220, 130))
        self.frame.setStyleSheet("background-image: url(:./logo2/logo2.png);\n"
                                 "background-position: center;\n"
                                 "background-repeat: no repeat")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(84, 210, 3, 430))
        self.line.setStyleSheet("background-color: rgb(255, 255, 100);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(230, 30, 631, 91))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.listView.setFont(font)
        self.listView.setStyleSheet("border: 3px solid rgb(255,255,100)")
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(118, 220, 350, 300))
        self.listView_2.setStyleSheet("background-color: rgb(230,245,245);")
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(502, 220, 350, 300))
        self.listView_3.setStyleSheet("background-color: rgb(230,245,245);")
        self.listView_3.setObjectName("listView_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
