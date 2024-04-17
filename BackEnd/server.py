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
    
    def update(self):
        client_socket, client_address = self.server_socket.accept()
        print(f"Accepted connection from {client_address}")
        player = client.Client()
        self.clients.append(player)
        client_handler = threading.Thread(target=self.handle_client, args=(client_socket, player))
        client_handler.start()

    def handle_client(client_socket, player: client.Client):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            # Receive message from client
            message = data.decode('utf-8')
            player.receive(message)
            # Send queued messages to client
            while player.unsent():
                response = player.send()
                client_socket.sendall(response.encode('utf-8'))
        client_socket.close()

