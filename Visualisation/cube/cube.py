from random import randint


class Cube:
    """class that represent a single cube"""

    def __init__(self, num_sides=6):
        """the hexagon cube is used by default"""
        self.num_sides = num_sides

    def roll(self):
        """return random number from one to the number of faces"""
        return randint(1, self.num_sides)
