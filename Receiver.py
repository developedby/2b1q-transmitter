from PyQt5 import QtCore, QtGui, QtWidgets

import Interface.receiveWindow
import networkCommunication as nc
import codec2b1q
import signalGraph

class Receiver(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(Receiver, self).__init__()
        self.main_window = main_window
        self.receive_window = Interface.receiveWindow.Ui_ReceiveWindow()
        self.receive_window.setupUi(self)
        self.receive_window.back_button.clicked.connect(lambda: self.closeWindow())
        self.receive_window.listen_button.clicked.connect(lambda: self.listen())
        self.receive_window.twoboneq_box.setReadOnly(True)
        self.receive_window.binary_box.setReadOnly(True)
        self.receive_window.message_box.setReadOnly(True)
        self.bin_graph_path = "receiver_binary_graph.png"
        self.encoded_graph_path = "receiver_encoded_graph.png"

    def closeEvent(self, event):
        self.main_window.closeEvent(event)

    def showWindow(self):
        self.show()

    def closeWindow(self):
        self.main_window.showWindow()
        self.close()
        self.deleteGraphs()
        self.receive_window.twoboneq_box.setText("")
        self.receive_window.binary_box.setText("")
        self.receive_window.message_box.setText("")
        self.receive_window.encoded_wave.setPixmap(QtGui.QPixmap(""))
        self.receive_window.binary_wave.setPixmap(QtGui.QPixmap(""))

    def listen(self):
        encoded_bytes = nc.listenForNumberList()
        encoded_list = []
        for byte in encoded_bytes:
            if int(byte) <= 127:
                encoded_list.append(int(byte))
            else:
                encoded_list.append(int(byte)-256)
        encoded_message = ' '.join(list(map(str,encoded_list)))

        bin_list = codec2b1q.decode2b1q(encoded_list)
        bin_message = ''.join(list(map(str, bin_list)))

        original_message = ""
        temp_byte = 0
        for i, bit in enumerate(bin_list):
            temp_byte = temp_byte*2 + bit
            if i%8 == 7:
                original_message += chr(temp_byte)
                temp_byte = 0

        self.receive_window.binary_box.setText(bin_message)
        self.receive_window.twoboneq_box.setText(encoded_message)
        self.receive_window.message_box.setText(original_message)

        signalGraph.PlotWaveformToFile(encoded_list, self.encoded_graph_path, wave_type='2b1q')
        self.receive_window.encoded_wave.setPixmap(QtGui.QPixmap(self.encoded_graph_path))
        signalGraph.PlotWaveformToFile(bin_list, self.bin_graph_path, wave_type='binary')
        self.receive_window.binary_wave.setPixmap(QtGui.QPixmap(self.bin_graph_path))

    def deleteGraphs(self):
        signalGraph.removeImage(self.encoded_graph_path)
        signalGraph.removeImage(self.bin_graph_path)
