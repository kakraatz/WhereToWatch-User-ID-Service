# Source - https://realpython.com/python-sockets/

import socket
import json


def microservice(name, service):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.connect(("127.0.0.1", 5000))
        info = json.dumps({"name": name, "service": service})
        my_socket.sendall(bytes(info.encode()))
        response = my_socket.recv(1024)
        response = response.decode()
        user_data = response.strip("][").split(", ")
    message = ("Login ID created for user: " + user_data[0] + ", Service: " + user_data[1] + ", ID: " + str(user_data[2]))
    print(message)
    return user_data


microservice("testuser", "Netflix")
