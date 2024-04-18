import player

class Match:
    def __init__(self, red: player.Player, blue: player.Player, id: int):
        self.id = id
        self.red = red
        self.blue = blue 
        self.red.join(self.id)
        self.blue.join(self.id)
        # TODO: initialize player positions, etc

    def update(self):
        # TODO: update players, player interactions, etc
        self.red.update()
        self.blue.update()
        for body_part, coords in self.red.get_body().get_positions().items():
            self.blue.send_enemy(body_part, coords[0], coords[1], coords[2])
            #print("sent coords to blue")
        for body_part, coords in self.blue.get_body().get_positions().items():
            self.red.send_enemy(body_part, coords[0], coords[1], coords[2])
            #print("sent coords to red")