# Source - https://realpython.com/python-sockets/

import socket
import random

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.bind(("127.0.0.1", 50000))
    my_socket.listen()
    while True:
        conn, addr = my_socket.accept()
        login = conn.recv(1024).decode()
        unique_id = random.getrandbits(16)
        data = bytes(str([login, unique_id]).encode())
        db = open("./logins.txt", "a")
        db.write("Login: " + str(login) + ", ID: " + str(unique_id) + "\n")
        db.close()
        conn.sendall(data)
