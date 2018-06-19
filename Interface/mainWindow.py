# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(248, 226)
        self.gridLayout = QtWidgets.QGridLayout(mainwindow)
        self.gridLayout.setObjectName("gridLayout")
        self.send_button = QtWidgets.QPushButton(mainwindow)
        self.send_button.setEnabled(True)
        self.send_button.setObjectName("send_button")
        self.gridLayout.addWidget(self.send_button, 0, 0, 1, 1)
        self.receive_button = QtWidgets.QPushButton(mainwindow)
        self.receive_button.setObjectName("receive_button")
        self.gridLayout.addWidget(self.receive_button, 1, 0, 1, 1)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "2B1Q Transmitter"))
        self.send_button.setText(_translate("mainwindow", "Send"))
        self.receive_button.setText(_translate("mainwindow", "Receive"))

