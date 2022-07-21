# Source - https://realpython.com/python-sockets/

import socket


def microservice(login):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_socket:
        my_socket.connect(("127.0.0.1", 50000))
        my_socket.sendall(bytes(login.encode()))
        response = my_socket.recv(1024).decode()
        user_data = response.strip("][").split(", ")

    message = ("Login ID created for user: " + str(user_data[0]) + ", ID: " + str(user_data[1]))
    return message


microservice("testuser")
