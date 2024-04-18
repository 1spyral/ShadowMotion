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
                print(response)
                self.socket.sendall(response.encode('utf-8'))
        self.socket.close()


    # Check if there are unread received messages
    def unread(self) -> bool:
        return bool(self.received)

    # Receive a message
    def receive(self, text: str) -> None:
        self.received.appendleft(text)

    # Read the oldest received message
    def read(self) -> str:
        return self.received.pop()

    # Check if there are unsent response messages
    def unsent(self) -> bool:
        return bool(self.response)

    # Respond with a message to send to client
    def respond(self, text: str) -> None:
        self.response.appendleft(text)
    
    # Return the oldest response message to send to client
    def send(self) -> str:
        return self.response.pop()
