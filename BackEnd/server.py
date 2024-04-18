import socket
import threading

from const import const as c
import client

# Reference for server:
# https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5

class Server:
    def __init__(self, clients):
        self.clients = clients
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        host = c[0]
        port = c[1]
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")
    

    # Checks for new connections and creates new Client class to handle it
    def update(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Create new player
        player = client.Client(client_socket)
        self.clients.append(player)


    def close(self):
        self.server_socket.close()

