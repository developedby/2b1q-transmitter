import socket

def sendBytes (data, hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((hostname, port))
    except:
        print("Unable to connect to hostname")
        return
    s.sendall(data)
    s.shutdown(socket.SHUT_WR)
    s.close()

# Converts binary list and sends to <hostname>
def sendBinaryList (bin_list, hostname='localhost', port=3030):
    data = []
    temp_byte = 0
    for i,bit in enumerate(bin_list):
        temp_byte = (temp_byte*2) + bin_list[i]
        if i%8 == 7:
            data.append(temp_byte)
            temp_byte = 0
    data = bytes(data)
    #return data
    sendBytes(hostname, port, data)

# Sends a list of numbers encoded as bytes to <hostname>
def sendNumberList (num_list, hostname='localhost', port=3030):
    data = []
    for num in num_list:
        if num >= 0:
            data.append(bytes([num]))
        else:
            data.append(bytes([256+num]))
    data = b''.join(data)
    sendBytes(data, hostname, port)

def listenForNumberList (port=3030):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(1)
    addr = None
    while not addr:
        connection, addr = s.accept()

    received_data = []
    temp_data = True
    while temp_data:
        print('t')
        temp_data = connection.recv(128)
        received_data.append(temp_data)
    connection.close()
    return received_data[0]
