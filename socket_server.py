# Source - https://realpython.com/python-sockets/

import socket
import random
import json


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
    my_socket.bind(("127.0.0.1", 5000))
    my_socket.listen()
    while True:
        conn, addr = my_socket.accept()
        data = conn.recv(1024)
        data = json.loads(data.decode())
        name = data.get("name")
        service = data.get("service")
        unique_id = random.getrandbits(16)
        response = bytes(str([name, service, unique_id]).encode())
        db = open("./logins.txt", "a")
        db.write("Login: " + str(name) + ", Service: " + str(service) + ", ID: " + str(unique_id) + "\n")
        db.close()
        conn.sendall(response)
