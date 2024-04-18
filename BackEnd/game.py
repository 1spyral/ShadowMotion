import client
import round

class Game:
    def __init__(self, clients: dict[str, client.Client]):
        self.clients = clients
        self.rounds: list[round.Round] = []
        

    def update(self):
        # TODO: player info, matchmaking

        for round in self.rounds:
            round.update()