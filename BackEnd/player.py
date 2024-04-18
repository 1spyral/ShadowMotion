import client
import match
import body

from const import *

class Player:
    def __init__(self, id: int, client: client.Client):
        self.id = id
        self.client = client

        self.commands: dict[str, function] = {
            "name": self.name,
            "ready": self.ready,
            "unready": self.unready,
            "coord": self.coord
        }

        self.name = f"Player {id}"
        self.readied = False
        self.lobby = True

        self.body: body.Body

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

    def join(self, match_id: int):
        '''Upon entering a match'''
        # TODO: tell client that match is joined
        self.lobby = False
        self.match_id = match_id
        self.hp = starting_hp
        self.body = body.Body()
        # TODO: initialize body
    
    def leave(self):
        '''Upon leaving a match'''
        # TODO: tell client that match is left
        self.ready = False
        self.lobby = True
        self.match = None

    def in_lobby(self) -> bool:
        return self.lobby
    
    def is_ready(self) -> bool:
        return self.readied

    def get_body(self) -> body.Body:
        return self.body
    
    #TODO: update details of body

    # Client functions

    def name(self, *args: tuple[str]):
        self.name = " ".join(args)

    def ready(self, *args):
        self.readied = True

    def unready(self, *args):
        # If player is already in match, cannot unready
        self.readied = False or self.fighting
    
    def coord(self, *args: tuple[str, str, str]):
        self.body.update(args[0], (float(args[1]), float(args[2]), float(args[3])))
