import socket
import threading
from collections import deque

from const import *

# Reference for client:
# https://pandeyshikha075.medium.com/building-a-chat-server-and-client-in-python-with-socket-programming-c76de52cc1d5

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        
        self.messages = deque([])

        # Thread for receiving server messages
        server_handler = threading.Thread(target=self.loop)
        server_handler.start()
        
    def loop(self):
        while True:
            # TODO: read a boolean variable from server telling us to terminate the client socket


            # Check for messages from server
            data = self.client_socket.recv(packet_size)
            if not data:
                break
            # Receive message from server
            message = data.decode('utf-8')
            self.messages.appendleft(message)
        self.client_socket.close()

    def unread(self) -> bool:
        '''Check if there are unread messages'''
        return bool(self.messages)

    def read(self) -> str | None:
        '''Read the oldest unread message'''
        return self.messages.pop() if self.messages else None

    def send(self, text: str) -> None:
        '''Send message to server'''
        text += "\n"
        self.client_socket.sendall(text.encode("utf-8"))