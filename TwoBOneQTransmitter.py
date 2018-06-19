import sys
from PyQt5.QtWidgets import *
#from PyQt5.QtCore import *

import Receiver
import Sender
import Interface.mainWindow


class TwoBOneQTransmitter(QDialog):
    def __init__(self):
        self.q_dialog = QDialog()
        self.sender = Sender.Sender(self)
        self.receiver = Receiver.Receiver(self)
        self.mainwindow = Interface.mainWindow.Ui_mainwindow()
        self.mainwindow.setupUi(self.q_dialog)
        self.mainwindow.receive_button.clicked.connect(lambda:self.showReceiver())
        self.mainwindow.send_button.clicked.connect(lambda:self.showSender())
        self.q_dialog.show()

    def showReceiver(self):
        self.receiver.showWindow()
        self.q_dialog.hide()

    def showSender(self):
        self.sender.showWindow()
        self.q_dialog.hide()

    def showWindow(self):
        self.q_dialog.show()

app = QApplication(sys.argv)
transmitter = TwoBOneQTransmitter()
sys.exit(app.exec_())
