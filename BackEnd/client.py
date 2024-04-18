from collections import deque
import threading
import socket

from const import *

class Client:
    def __init__(self, socket: socket.socket):
        self.socket = socket

        # Received messages queue
        self.received = deque([])
        # Sent messages queue
        self.response = deque([])

        client_handler = threading.Thread(target=self.loop)
        client_handler.start()


    def loop(self):
        while True:
            # TODO: read a boolean variable from Client telling us to terminate the client socket


            # Check for messages from client
            data = self.socket.recv(packet_size)
            if not data:
                break
            # Receive message from client
            message = data.decode('utf-8')
            self.receive(message)
            # Send queued messages to client
            while self.unsent():
                response = self.send()
                self.socket.sendall(response.encode('utf-8'))
        self.socket.close()

    
    def unread(self) -> bool:
        '''Check if there are unread received messages'''
        return bool(self.received)

    def receive(self, text: str) -> None:
        '''Receive a message'''
        self.received.appendleft(text)

    def read(self) -> str:
        '''Read the oldest received message'''
        return self.received.pop()

    def unsent(self) -> bool:
        '''Check if there are unsent response messages'''
        return bool(self.response)

    def write(self, text: str) -> None:
        '''Respond with a message to write to client'''
        self.response.appendleft(text)
    
    def send(self) -> str:
        '''Return the oldest response message to write to client'''
        return self.response.pop()
