from PyQt5 import QtCore, QtGui, QtWidgets

import Interface.sendWindow
import codec2b1q
import signalGraph
import networkCommunication as nC

class Sender(QtWidgets.QDialog):
    def __init__(self, main_window):
        super(Sender, self).__init__()
        self.main_window = main_window
        self.sender_window = Interface.sendWindow.Ui_SendWindow()
        self.sender_window.setupUi(self)
        self.sender_window.back_button.clicked.connect(lambda:self.closeWindow())
        self.sender_window.encode_button.clicked.connect(lambda:self.encodeMessageAndGraph())
        self.sender_window.send_button.clicked.connect(lambda: nC.sendNumberList(self.encoded_list, hostname=self.sender_window.hostname_box.text()))
        self.bin_list = []
        self.encoded_list = []
        self.sender_window.twoboneq_box.setReadOnly(True)
        self.sender_window.binary_box.setReadOnly(True)
        self.bin_graph_path = "sender_binary_graph.png"
        self.encoded_graph_path = "sender_encoded_graph.png"
        self.sender_window.twoboneq_box.setText("")
        self.sender_window.binary_box.setText("")
        self.sender_window.message_box.setText("")
        self.sender_window.hostname_box.setText("")
        self.sender_window.encoded_wave.setText("")
        self.sender_window.binary_wave.setText("")


    def closeEvent(self, event):
        self.main_window.closeEvent(event)

    def showWindow(self):
        self.show()

    def closeWindow(self):
        self.close()
        self.main_window.showWindow()
        self.deleteGraphs()
        self.sender_window.twoboneq_box.setText("")
        self.sender_window.binary_box.setText("")
        self.sender_window.message_box.setText("")
        self.sender_window.hostname_box.setText("")
        self.sender_window.encoded_wave.setPixmap(QtGui.QPixmap(""))
        self.sender_window.binary_wave.setPixmap(QtGui.QPixmap(""))

    def encodeMessageAndGraph(self):
        self.bin_list = []
        self.encoded_list = []
        # Converts the message to a list of binaries
        for str_char in self.sender_window.message_box.text():
            # Converts a character to a string of '1's and '0's
            str_char_in_bin = format(ord(str_char), '08b')
            # Converts that string of '1's and '0's to a list of 1s and 0s and appends it to the rest
            for bin_char in str_char_in_bin:
                self.bin_list.append(int(bin_char))
        #
        bin_text = ''.join(list(map(str,self.bin_list)))
        self.sender_window.binary_box.setText(bin_text)

        # Encodes the binary list message to a 2B1Q binary list
        self.encoded_list = codec2b1q.encode2b1q(self.bin_list)

        # Converts the 2B1Q binary list to a string of '0's and '1's
        encoded_text = ' '.join(list(map(str,self.encoded_list)))
        self.sender_window.twoboneq_box.setText(encoded_text)

        # Plot the graph, save to a file, and load the image in the window
        signalGraph.PlotWaveformToFile(self.encoded_list, self.encoded_graph_path, wave_type='2b1q')
        self.sender_window.encoded_wave.setPixmap(QtGui.QPixmap(self.encoded_graph_path))
        signalGraph.PlotWaveformToFile(self.bin_list, self.bin_graph_path, wave_type='binary')
        self.sender_window.binary_wave.setPixmap(QtGui.QPixmap(self.bin_graph_path))

    def deleteGraphs(self):
        signalGraph.removeImage(self.encoded_graph_path)
        signalGraph.removeImage(self.bin_graph_path)
