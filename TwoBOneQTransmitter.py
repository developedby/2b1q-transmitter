import sys
import PyQt5.QtWidgets as qtw

import Receiver
import Sender
import Interface.mainWindow
import signalGraph


class TwoBOneQTransmitter(qtw.QDialog):
    def __init__(self):
        super(TwoBOneQTransmitter, self).__init__()
        self.sender = Sender.Sender(self)
        self.receiver = Receiver.Receiver(self)
        self.mainwindow = Interface.mainWindow.Ui_mainwindow()
        self.mainwindow.setupUi(self)
        self.mainwindow.receive_button.clicked.connect(lambda:self.showReceiver())
        self.mainwindow.send_button.clicked.connect(lambda:self.showSender())
        self.show()

    def showReceiver(self):
        self.receiver.showWindow()
        self.hide()

    def showSender(self):
        self.sender.showWindow()
        self.hide()

    def showWindow(self):
        self.show()
        
    def closeEvent(self, event):
        self.sender.deleteGraphs()
        self.receiver.deleteGraphs()

app = qtw.QApplication(sys.argv)
transmitter = TwoBOneQTransmitter()
sys.exit(app.exec_())
