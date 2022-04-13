

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_B(object):
    def setupUi(self, B):
        B.setObjectName("B")
        B.resize(375, 600)
        B.setMinimumSize(QtCore.QSize(375, 600))
        B.setMaximumSize(QtCore.QSize(375, 600))
        self.centralwidget = QtWidgets.QWidget(B)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-2, -2, 380, 620))
        self.frame.setMinimumSize(QtCore.QSize(375, 600))
        label_Image = QtGui.QLabel(self.frame)

        image_path = r'a.png'  # path to your image file
        image_profile = QtGui.QImage(image_path)  # QImage object
        # To scale image for example and keep its Aspect Ration
        image_profile = image_profile.scaled(
            250, 250, aspectRatioMode=QtCore.Qt.KeepAspectRatio, transformMode=QtCore.Qt.SmoothTransformation)
        label_Image.setPixmap(QtGui.QPixmap.fromImage(image_profile))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 350, 255, 52))
        font = QtGui.QFont()
        font.setFamily("CocoSharp Trial Extrabold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    boder-radius: 20px;\n"
                                    "    border: 3px solid rgb(255, 211, 94);\n"
                                    "    padding: 7px;\n"
                                    "    color: rgb(255, 211, 94);\n"
                                    "}\n"
                                    "QLineEdit:hover {\n"
                                    "    border: 1.7px solid rgb(255, 211, 94);\n"
                                    "}")
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 414, 255, 52))
        font = QtGui.QFont()
        font.setFamily("CocoSharp Trial Extrabold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
                                      "    boder-radius: 20px;\n"
                                      "    border: 3px solid rgb(255, 211, 94);\n"
                                      "    padding: 7px;\n"
                                      "    color: rgb(255, 211, 94);\n"
                                      "}\n"
                                      "QLineEdit:hover {\n"
                                      "        border: 1.7px solid rgb(255, 211, 94);\n"
                                      "}")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(120, 500, 120, 40))
        font = QtGui.QFont()
        font.setFamily("CocoSharp Trial Extrabold")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 211, 94);\n"
                                      "    backgroundcolor: rgb(255, 211, 94);\n"
                                      "    border: 3px solid rgb(255, 211, 94);\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    border: 5px solid rgb(255, 211, 94);\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    border: 1.7px solid rgb(255, 211, 94);\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(60, 474, 101, 17))
        font = QtGui.QFont()
        font.setFamily("CocoSharp Trial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox.setStyleSheet("color: rgb(255, 211, 94)")
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        B.setCentralWidget(self.centralwidget)

        self.retranslateUi(B)
        QtCore.QMetaObject.connectSlotsByName(B)

    def retranslateUi(self, B):
        _translate = QtCore.QCoreApplication.translate
        B.setWindowTitle(_translate("B", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("B", "USUÁRIO"))
        self.lineEdit_2.setPlaceholderText(_translate("B", "SENHA"))
        self.pushButton.setText(_translate("B", "LOGIN"))
        self.checkBox.setText(_translate("B", "Salvar login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    B = QtWidgets.QMainWindow()
    ui = Ui_B()
    ui.setupUi(B)
    B.show()
    sys.exit(app.exec_())
