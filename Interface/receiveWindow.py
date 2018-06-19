# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receivewindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReceiveWindow(object):
    def setupUi(self, ReceiveWindow):
        ReceiveWindow.setObjectName("ReceiveWindow")
        ReceiveWindow.resize(730, 531)
        self.graph_groupbox = QtWidgets.QGroupBox(ReceiveWindow)
        self.graph_groupbox.setGeometry(QtCore.QRect(9, 182, 701, 261))
        self.graph_groupbox.setTitle("")
        self.graph_groupbox.setObjectName("graph_groupbox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.graph_groupbox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.encoded_wave = QtWidgets.QLabel(self.graph_groupbox)
        self.encoded_wave.setText("")
        self.encoded_wave.setObjectName("encoded_wave")
        self.gridLayout_2.addWidget(self.encoded_wave, 0, 0, 1, 1)
        self.binary_wave = QtWidgets.QLabel(self.graph_groupbox)
        self.binary_wave.setText("")
        self.binary_wave.setObjectName("binary_wave")
        self.gridLayout_2.addWidget(self.binary_wave, 0, 1, 1, 1)
        self.boxes_groupbox = QtWidgets.QGroupBox(ReceiveWindow)
        self.boxes_groupbox.setGeometry(QtCore.QRect(9, 9, 711, 162))
        self.boxes_groupbox.setTitle("")
        self.boxes_groupbox.setObjectName("boxes_groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.boxes_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.message_label = QtWidgets.QLabel(self.boxes_groupbox)
        self.message_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.message_label.setObjectName("message_label")
        self.gridLayout.addWidget(self.message_label, 0, 0, 1, 1)
        self.message_box = QtWidgets.QLineEdit(self.boxes_groupbox)
        self.message_box.setReadOnly(False)
        self.message_box.setObjectName("message_box")
        self.gridLayout.addWidget(self.message_box, 0, 1, 1, 1)
        self.binary_label = QtWidgets.QLabel(self.boxes_groupbox)
        self.binary_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.binary_label.setObjectName("binary_label")
        self.gridLayout.addWidget(self.binary_label, 1, 0, 1, 1)
        self.twoboneq_box = QtWidgets.QLineEdit(self.boxes_groupbox)
        self.twoboneq_box.setObjectName("twoboneq_box")
        self.gridLayout.addWidget(self.twoboneq_box, 2, 1, 1, 1)
        self.binary_box = QtWidgets.QLineEdit(self.boxes_groupbox)
        self.binary_box.setObjectName("binary_box")
        self.gridLayout.addWidget(self.binary_box, 1, 1, 1, 1)
        self.twoboneq_label = QtWidgets.QLabel(self.boxes_groupbox)
        self.twoboneq_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.twoboneq_label.setObjectName("twoboneq_label")
        self.gridLayout.addWidget(self.twoboneq_label, 2, 0, 1, 1)
        self.button_groupbox = QtWidgets.QGroupBox(ReceiveWindow)
        self.button_groupbox.setGeometry(QtCore.QRect(9, 445, 701, 71))
        self.button_groupbox.setTitle("")
        self.button_groupbox.setObjectName("button_groupbox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.button_groupbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.back_button = QtWidgets.QPushButton(self.button_groupbox)
        self.back_button.setObjectName("back_button")
        self.gridLayout_4.addWidget(self.back_button, 0, 1, 1, 1)
        self.listen_button = QtWidgets.QPushButton(self.button_groupbox)
        self.listen_button.setObjectName("listen_button")
        self.gridLayout_4.addWidget(self.listen_button, 0, 0, 1, 1)

        self.retranslateUi(ReceiveWindow)
        QtCore.QMetaObject.connectSlotsByName(ReceiveWindow)

    def retranslateUi(self, ReceiveWindow):
        _translate = QtCore.QCoreApplication.translate
        ReceiveWindow.setWindowTitle(_translate("ReceiveWindow", "2B1Q Receiver "))
        self.message_label.setText(_translate("ReceiveWindow", "Message"))
        self.binary_label.setText(_translate("ReceiveWindow", "Binary Encoded"))
        self.twoboneq_label.setText(_translate("ReceiveWindow", "2B/1Q Encoded"))
        self.back_button.setText(_translate("ReceiveWindow", "Back"))
        self.listen_button.setText(_translate("ReceiveWindow", "Listen"))

