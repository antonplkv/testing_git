import socket
import time

HOST = "127.0.0.1"
PORT = 9003


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))


while True:
    s.send(b'Hello server')
    data = s.recv(2048)
    print(data)
    time.sleep(2)
