from collections import deque

import client
import match
import player

class Game:
    def __init__(self, client_queue: deque[tuple[str, client.Client]]):
        self.client_queue = client_queue

        self.players: dict[int, player.Player] = {}
        self.matches: list[match.Match] = []
        

    def update(self):
        while self.client_queue:
            self.add_player(self.client_queue.pop())

        waiting: list[int] = []
        for id, p in self.players.items():
            # Manages players that are in the lobby. Players currently in a game are managed during match.update()
            if p.in_lobby():
                p.update()
                # If player is ready, add to waiting list
                if p.is_ready():
                    waiting.append(id)
                    # If waiting list has two members, start a match
                    if len(waiting) == 2:
                        self.create_match(waiting)
                        # Reset waiting list
                        waiting = []

        for match in self.matches:
            match.update()
            # TODO: Check if match is done, so we can add it to an array to remove finished matches at the end of loop

    def add_player(self, client_info: tuple[str, client.Client]) -> player.Player:
        client_address, client = client_info
        id = hash(client_address)
        new_player = player.Player(id, client)
        self.players[id] = new_player
        return new_player

    def create_match(self, waiting: list[int]) -> match.Match:
        new_match = match.Match(self.players[waiting[0]], self.players[waiting[1]], 1)
        self.matches.append(new_match)
        return new_match