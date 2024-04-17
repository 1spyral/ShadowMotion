from collections import deque

class Client:
    def __init__(self):
        self.received = deque([])
        self.response = deque([])

    def unread(self) -> bool:
        return bool(self.received)

    def receive(self, text: str) -> None:
        self.received.appendleft(text)

    def read(self) -> str:
        self.received.pop()

    def unsent(self) -> bool:
        return bool(self.response)

    def respond(self, text: str) -> None:
        self.response.appendleft(text)
    
    def send(self) -> str:
        self.response.pop()
