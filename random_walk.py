from random import choice

class Walks:
    def __init__(self, num_points=10000):
        """"Initialize Random Walk."""
        self.num_points = num_points

        #Walks Starting at (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def desired_walks(self):
        """Keep Walking until reaches end of points."""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
            y_step = y_direction*y_distance

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)