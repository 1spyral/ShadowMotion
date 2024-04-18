class Body:

    def __init__(self):
        
        self.positions: dict[str, tuple[float, float, float]] = {
            "right_fist": (0,0,0),
            "right_elbow": (0,0,0),
            "right_shoulder":(0,0,0),
            "left_fist": (0,0,0),
            "left_elbow": (0,0,0),
            "left_shoulder": (0,0,0),
            "head_end":(0,0,0),
            "head_start": (0,0,0),
            "chest": (0,0,0),
        }
    
    def update(self, body_part: str, coords: tuple[float, float, float]) -> None:
        self.positions[body_part] = coords

    def get_positions(self) -> dict[str, tuple[float, float, float]]:
        return self.positions

    # if a body part collides with another body part
    def collides_with(self, this: tuple, other: tuple) -> bool:

        # if the x values and y values are similar enough, and the absolute difference between the z values are small enough
        # register a collision
        offset = 1000
        this_x = this[0] * offset
        this_y = this[1] * offset
        this_z = this[2] * offset

        other_x = other[0] * offset
        other_y = other[1] * offset
        other_z = other[2] * offset

        x_diff = abs(this_x - other_x)
        y_diff = abs(this_y - other_y)
        z_diff = abs(this_z - other_z)

        if x_diff <= 75 and y_diff <= 75 and z_diff <= 150:
            return True
        else:
            return False

    # if a player's fist collides with another player's head
    def hits_player(self, other):
        
        rf_h = self.collides_with(self.get_positions()["right_fist"], other.get_positions()["head_start"])
        rf_rf = self.collides_with(self.get_positions()["right_fist"], other.get_positions()["right_fist"])
        rf_lf = self.collides_with(self.get_positions()["right_fist"], other.get_positions()["left_start"])
        lf_h = self.collides_with(self.get_positions()["left_fist"], other.get_positions()["head_start"])
        lf_rf = self.collides_with(self.get_positions()["left_fist"], other.get_positions()["right_fist"])
        lf_lf = self.collides_with(self.get_positions()["left_fist"], other.get_positions()["left_fist"])
        
        if rf_h and not (rf_rf or rf_lf): 
            return True
        elif lf_h and not(lf_lf or lf_rf):
            return True
        else:
            return False





