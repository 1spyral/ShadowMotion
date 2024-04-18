import client

class Player:
    def __init__(self, id: int, client: client.Client):
        self.id = id
        self.client = client

        self.commands: dict[str, function] = {
            "name": self.name,
            "ready": self.ready
        }

        self.hp = 100
        self.name = f"Player {id}"
        self.fighting = False

    def update(self):
        # TODO: maybe differentiate update method between in game and out-of-game player?
        # Read client messages
        while self.client.unread():
            message = self.client.read().split()
            command = message[0]
            try:
                args = message[1:]
            except IndexError:
                args = ()
            self.commands[command](args)
        # TODO: update player and send messages back to client

    # Client functions

    def name(self, *args: tuple[str]):
        self.name = args[0]

    def ready(self, *args):
        # ready up for matchmaking
        pass