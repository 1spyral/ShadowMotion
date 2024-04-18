class Body:

    def __init__(self):
        
        self.positions: dict[str, tuple[float, float, float]] = {
            "right_fist": None,
            "right_elbow": None,
            "right_shoulder":None,
            "left_fist": None,
            "left_elbow": None,
            "left_shoulder": None,
            "head_end":None,
            "head_start": None,
            "chest": None,
        }
    
    def update(self, body_part: str, coords: tuple[float, float, float]) -> None:
        self.positions[body_part] = coords

    def get_positions(self) -> dict[str, tuple[float, float, float]]:
        return self.positions

    # if a body part collides with another body part
    def collides_with(this: tuple, other: tuple) -> bool:

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




