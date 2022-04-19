
from PyQt5 import QtCore, QtGui, QtWidgets
import imagemlogin1
import janelaqrcode

#


class Ui_BotH51(object):
    def setupUi(self, BotH51):
        BotH51.setObjectName("BotH51")
        BotH51.resize(480, 680)
        BotH51.setMinimumSize(QtCore.QSize(480, 680))
        BotH51.setMaximumSize(QtCore.QSize(480, 680))
        BotH51.setStyleSheet("QWidget {\n"
                             "    background-color: rgb(35,45,55);\n"
                             "\n"
                             "}")
        BotH51.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.janelaLogin = QtWidgets.QWidget(BotH51)
        self.janelaLogin.setObjectName("janelaLogin")
        self.frame = QtWidgets.QFrame(self.janelaLogin)
        self.frame.setGeometry(QtCore.QRect(110, 100, 260, 180))
        self.frame.setStyleSheet("background-image: url(:/logo1/Untitled-1.png);\n"
                                 "border: none;\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: center;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineUsuario = QtWidgets.QLineEdit(self.janelaLogin)
        self.lineUsuario.setGeometry(QtCore.QRect(100, 380, 280, 50))
        font = QtGui.QFont()
        font.setFamily("CocoSharpL-ExtraboldItalic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineUsuario.setFont(font)
        self.lineUsuario.setStyleSheet("QLineEdit {\n"
                                       "    background-color: rgb(230,245,245);\n"
                                       "    padding: 10px;\n"
                                       "    color: rgb(35,45,55);\n"
                                       "}\n"
                                       "QLineEdit:hover {\n"
                                       "    background-color: rgb(255,255,100);\n"
                                       "    border: 3px solid rgb(255,255,100);\n"
                                       "    padding: 10px;\n"
                                       "    color: rgb(35,45,55);\n"
                                       "}\n"
                                       "")
        self.lineUsuario.setInputMask("")
        self.lineUsuario.setText("")
        self.lineUsuario.setObjectName("lineUsuario")
        self.lineSenha = QtWidgets.QLineEdit(self.janelaLogin)
        self.lineSenha.setGeometry(QtCore.QRect(100, 440, 280, 50))
        font = QtGui.QFont()
        font.setFamily("CocoSharpL-ExtraboldItalic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineSenha.setFont(font)
        self.lineSenha.setStyleSheet("QLineEdit {\n"
                                     "    background-color: rgb(230,245,245);\n"
                                     "    padding: 10px;\n"
                                     "    color: rgb(35,45,55);\n"
                                     "}\n"
                                     "QLineEdit:hover {\n"
                                     "    background-color: rgb(255,255,100);\n"
                                     "    border: 3px solid rgb(255,255,100);\n"
                                     "    padding: 10px;\n"
                                     "    color: rgb(35,45,55);\n"
                                     "}\n"
                                     "")
        self.lineSenha.setInputMask("")
        self.lineSenha.setText("")
        self.lineSenha.setObjectName("lineSenha")
        self.salvarlogin = QtWidgets.QCheckBox(self.janelaLogin)
        self.salvarlogin.setGeometry(QtCore.QRect(100, 500, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.salvarlogin.setFont(font)
        self.salvarlogin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.salvarlogin.setStyleSheet("QCheckBox:hover {\n"
                                       "    color: rgb(255, 255, 100);\n"
                                       "}\n"
                                       "QCheckBox {\n"
                                       "    color: rgb(213,240,237);\n"
                                       "}\n"
                                       "")
        self.salvarlogin.setObjectName("salvarlogin")
        self.buttonEntrar = QtWidgets.QPushButton(self.janelaLogin)
        self.buttonEntrar.setGeometry(QtCore.QRect(170, 501, 131, 35))
        font = QtGui.QFont()
        font.setFamily("CocoSharpL-ExtraboldItalic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonEntrar.setFont(font)
        self.buttonEntrar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonEntrar.setStyleSheet("background-color: rgb(255, 255, 100);\n"
                                        "color: rgb(35,45,55);")
        self.buttonEntrar.setObjectName("buttonEntrar")
        self.buttonQrcode = QtWidgets.QPushButton(self.janelaLogin)
        self.buttonQrcode.setGeometry(QtCore.QRect(310, 501, 70, 35))
        font = QtGui.QFont()
        font.setFamily("CocoSharpL-ExtraboldItalic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonQrcode.setFont(font)
        self.buttonQrcode.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonQrcode.setStyleSheet("background-color: rgb(255, 255, 100);\n"
                                        "color: rgb(35,45,55);")
        self.buttonQrcode.setObjectName("buttonQrcode")
        BotH51.setCentralWidget(self.janelaLogin)

        self.retranslateUi(BotH51)
        QtCore.QMetaObject.connectSlotsByName(BotH51)

    def retranslateUi(self, BotH51):
        _translate = QtCore.QCoreApplication.translate
        BotH51.setWindowTitle(_translate("BotH51", "BotH51"))
        self.lineUsuario.setPlaceholderText(_translate("BotH51", "Usuário"))
        self.lineSenha.setPlaceholderText(_translate("BotH51", "Senha"))
        self.salvarlogin.setText(_translate("BotH51", "Salvar"))
        self.buttonEntrar.setText(_translate("BotH51", "Entrar"))
        self.buttonEntrar.setShortcut(_translate("BotH51", "Return"))
        self.buttonQrcode.setText(_translate("BotH51", "Grupo"))
#def ler txt e retornar lista


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


def ler_txt(arquivo):
    with open(arquivo, 'r') as f:
        lista = f.readlines()
    return lista


#main
if __name__ == "__main__":
    import sys
    if ler_txt('text.txt'):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        app = QtWidgets.QApplication(sys.argv)
        BotH51 = QtWidgets.QMainWindow()
        ui = Ui_BotH51()
        ui.setupUi(BotH51)
        BotH51.show()
        sys.exit(app.exec_())
