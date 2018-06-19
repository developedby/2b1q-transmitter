from PyQt5.QtWidgets import *

import Interface.receiveWindow
import networkCommunication as nc
import codec2b1q

class Receiver(QDialog):
    def __init__(self, main_window):
        self.main_window = main_window
        self.q_dialog = QDialog()
        self.receive_window = Interface.receiveWindow.Ui_ReceiveWindow()
        self.receive_window.setupUi(self.q_dialog)
        self.receive_window.back_button.clicked.connect(lambda: self.closeWindow())
        self.receive_window.listen_button.clicked.connect(lambda: self.listen())
        self.receive_window.twoboneq_box.setReadOnly(True)
        self.receive_window.binary_box.setReadOnly(True)
        self.receive_window.message_box.setReadOnly(True)

    def showWindow(self):
        self.q_dialog.show()

    def closeWindow(self):
        self.main_window.showWindow()
        self.q_dialog.close()

    def listen(self):
        encoded_bytes = nc.listenForNumberList()
        encoded_list = []
        for byte in encoded_bytes:
            if int(byte) <= 127:
                encoded_list.append(int(byte))
            else:
                encoded_list.append(int(byte)-256)
        encoded_message = ' '.join(list(map(str,encoded_list)))

        decoded_list = codec2b1q.decode2b1q(encoded_list)
        decoded_message = ''.join(list(map(str,decoded_list)))

        original_message = ""
        temp_byte = 0
        for i, bit in enumerate(decoded_list):
            temp_byte = temp_byte*2 + bit
            if i%8 == 7:
                original_message.append(chr(temp_byte))
