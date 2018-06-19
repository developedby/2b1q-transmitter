import socket
import subprocess

def netcat (data, hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(data)
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(1024)
        if data == None or data == b'':
            break
        print ("Received:", repr(data))
    print ("Connection closed.")
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
    netcat(hostname, port, data)

# Sends a list of numbers encoded as bytes to <hostname>
def sendNumberList (num_list, hostname='localhost', port=3030):
    data = []
    for num in num_list:
        if num >= 0:
            data.append(bytes([num]))
        else:
            data.append(bytes([256+num]))
    data = b''.join(data)
    netcat(data, hostname, port)

def listenForNumberList (port):
    process = subprocess.Popen('nc -l -p %s' %(port,), shell=True, stdout=subprocess.PIPE)
    return process.stdout.read()
