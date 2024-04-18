import client

class Player:
    def __init__(self, id: int, client: client.Client):
        self.id = id
        self.client = client

        self.commands: dict[str, function] = {
            "name": self.name,
            "ready": self.ready
        }

        self.name = f"Player {id}"
        self.round: int = None # The round that the player is fighting in. If player is in lobby, None
        self.hp: int
        self.fighting: bool

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

    def in_lobby(self) -> bool:
        return self.round is None

    # Client functions

    def name(self, *args: tuple[str]):
        self.name = args[0]

    def ready(self, *args):
        # ready up for matchmaking
        pass