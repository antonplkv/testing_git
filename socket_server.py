import socket
from threading import Thread

HOST = '127.0.0.1'
PORT = 9003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)

s.bind((HOST, PORT))

s.listen(5)


def handle_client_socket(client_socket: socket.socket):

    while True:

        data = client_socket.recv(1024)

        if not data:
            break
        client_socket.send(data[::-1])
        print(data)


while True:

    conn, addr = s.accept()
    Thread(target=handle_client_socket, args=(conn, )).start()
