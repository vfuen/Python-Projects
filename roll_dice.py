


from random import randint

class A_Die:
    """"THis class represents one die."""

    def __init__(self, num_sides=8):
        """A die with 6 numbers 1 through 8"""
        self.num_sides = num_sides

    def roll(self):
        """"Returns a random number between 1 and 8."""
        return randint(1, self.num_sides)


