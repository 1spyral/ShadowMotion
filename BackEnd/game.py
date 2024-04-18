from collections import deque

import client
import round
import player

class Game:
    def __init__(self, client_queue: deque[tuple[str, client.Client]]):
        self.client_queue = client_queue

        self.players: dict[int, player.Player] = []
        self.rounds: list[round.Round] = []
        

    def update(self):
        while self.client_queue:
            self.add_player(self.client_queue.pop())

        waiting: list[int] = []
        for id, p in self.players.items():
            # Manages players that are in the lobby. Players currently in a game are managed during round.update()
            if p.in_lobby():
                p.update()
                # If player is ready, add to waiting list
                if p.is_ready():
                    waiting.append(id)
                    # If waiting list has two members, start a round
                    if len(waiting) == 2:
                        self.create_round(waiting)
                        # Reset waiting list
                        waiting = []

        for round in self.rounds:
            round.update()

    def add_player(self, client_info: tuple[str, client.Client]) -> player.Player:
        client_address, client = client_info
        id = hash(client_address)
        new_player = player.Player(id, client)
        self.players[id] = new_player
        return new_player

    def create_round(self, waiting: list[int, int]) -> round.Round:
        new_round = round.Round(waiting[0], waiting[1])
        self.rounds.append(new_round)
        return new_round