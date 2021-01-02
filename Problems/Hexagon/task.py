import math


class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    # create get_area here
    def get_area(self):
        s = (3 * math.sqrt(3) * self.side_length ** 2) / 2
        return round(s, 3)