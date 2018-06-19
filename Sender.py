from PyQt5 import QtCore, QtGui, QtWidgets

import Interface.sendWindow
import codec2b1q
import signalGraph
import networkCommunication as nC

class Sender(QtWidgets.QDialog):
    def __init__(self, main_window):
        self.main_window = main_window
        self.q_dialog = QtWidgets.QDialog()
        self.sender_window = Interface.sendWindow.Ui_SendWindow()
        self.sender_window.setupUi(self.q_dialog)
        self.sender_window.back_button.clicked.connect(lambda:self.closeWindow())
        self.sender_window.encode_button.clicked.connect(lambda:self.encodeMessageAndGraph())
        self.sender_window.send_button.clicked.connect(lambda: nC.sendNumberList(self.encoded_list, hostname=self.sender_window.hostname_box.text()))
        self.bin_list = []
        self.encoded_list = []
        self.sender_window.twoboneq_box.setReadOnly(True)
        self.sender_window.binary_box.setReadOnly(True)

    def showWindow(self):
        self.q_dialog.show()

    def closeWindow(self):
        self.q_dialog.close()
        self.main_window.showWindow()

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
        encoded_message_graph = signalGraph.PlotWaveformToFile(self.encoded_list, "encoder_grafic.png")
        self.sender_window.encoded_wave.setPixmap(QtGui.QPixmap(encoded_message_graph))
        bin_message_graph = signalGraph.PlotWaveformToFile(self.bin_list, "binary_grafic.png")
        self.sender_window.binary_wave.setPixmap(QtGui.QPixmap(bin_message_graph))

