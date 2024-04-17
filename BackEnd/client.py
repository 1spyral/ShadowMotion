from collections import deque

class Client:
    def __init__(self):
        # Received messages queue
        self.received = deque([])
        # Sent messages queue
        self.response = deque([])

    # Check if there are unread received messages
    def unread(self) -> bool:
        return bool(self.received)

    # Receive a message
    def receive(self, text: str) -> None:
        self.received.appendleft(text)

    # Read the oldest received message
    def read(self) -> str:
        self.received.pop()

    # Check if there are unsent response messages
    def unsent(self) -> bool:
        return bool(self.response)

    # Respond with a message to send to client
    def respond(self, text: str) -> None:
        self.response.appendleft(text)
    
    # Return the oldest response message to send to client
    def send(self) -> str:
        self.response.pop()
