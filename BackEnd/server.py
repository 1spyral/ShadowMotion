import socket
import threading
from collections import deque

from const import *
import client

# Reference for server:
# https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5

class Server:
    def __init__(self, client_queue: deque[tuple[str, client.Client]]):
        self.client_queue = client_queue
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        client_thread = threading.Thread(target=self.clients_loop)
        client_thread.start()
    

    # Checks for new connections and creates new Client class to handle it
    def update(self):
        '''Deprecated'''
        pass

    def clients_loop(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Add client to client_queue
        self.client_queue.appendleft((str(client_address), client.Client(client_socket)))

    def close(self):
        self.server_socket.close()

