from snake.box import Box
import random


class AppleGenerator():

    def __init__(self, rows_cols, grid_size, color=(255, 0, 0)):
        self.rows_cols = rows_cols
        self.grid_size = grid_size
        self.color = color
    
    def generate_apple(self, snake):
        x, y = 0, 0

        valid = False
        while not valid:
            x = random.randrange(self.rows_cols) * self.grid_size
            y = random.randrange(self.rows_cols) * self.grid_size
            valid = not snake.collides((x, y))

        return Box((x, y), (self.grid_size, self.grid_size), self.color)
