import client

class Player:
    def __init__(self, client: client.Client):
        self.client = client
        self.hp = 100

