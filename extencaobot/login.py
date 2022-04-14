# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import os
import subprocess
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    count = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(412, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(9, 160, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 160, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Fluent Icons")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2.setStyleSheet("backgroud-color: rgb(39, 255, 147)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.checkBox.setObjectName("checkBox")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(160, 50, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(160, 70, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 70, 91, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 10, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 115, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "iniciar"))
        self.pushButton_2.setText(_translate("MainWindow", "pausar criacao"))
        self.checkBox.setText(_translate("MainWindow", "navegador oculto"))
        self.radioButton.setText(_translate("MainWindow", "fakemail"))
        self.radioButton_2.setText(_translate("MainWindow", "lyonsemail"))
        self.checkBox_2.setText(_translate("MainWindow", "modo anonimo"))
        self.lineEdit.setText(_translate("MainWindow", "gen1122"))
        self.label.setText(_translate(
            "MainWindow", "quantidades de programas em execucao " + str(self.count)))
        self.label_2.setText(_translate("MainWindow", "Senha:"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

    def counte(self):
        self.count += 1
        self.label.setText(
            "quantidades de programas em execucao " + str(self.count))

    def criacao_config(self):
        try:
            simp_path = r'config\\config.txt'
            abs_path = os.path.abspath(simp_path)
            nome_arquivo = abs_path
            arquivo = open(nome_arquivo, 'r+')
        except FileNotFoundError:
            arquivo = open(nome_arquivo, 'w+')
        arquivo.close()
        f = open(abs_path, 'r')
        conteudo = f.readlines()
        if self.radioButton.isChecked():
            conteudo.append(f'\nemail = 1')
        else:
            conteudo.append(f'\nemail = 0')
        if self.checkBox.isChecked():
            conteudo.append(f'\nanonimo = 1')
        else:
            conteudo.append(f'\nanonimo = 0')
        conteudo.append(f'\nnavsemimages = 1')
        if self.checkBox_2.isChecked():
            conteudo.append(f'\nnavocultos = 1')
        else:
            conteudo.append(f'\nnavocultos = 0')
        conteudo.append(f'\nsenha = {self.lineEdit.text()}')
        f2 = open(abs_path, 'w')
        f2.writelines(conteudo)
        f2 = open(abs_path, 'r')
        arquivo.close()
        sleep(1)
        simp_path = r'criador.exe'
        abs_path = os.path.abspath(simp_path)
        os.system(f"start {abs_path}")


def fechar():
    os.system("taskkill /f /im chrome.exe")
    sleep(1)
    os.system("taskkill /f /im criador.exe")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(lambda: ui.counte())
    ui.pushButton_2.clicked.connect(
        lambda: fechar())

    sys.exit(app.exec_())