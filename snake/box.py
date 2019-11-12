from pygame.draw import rect


class Box:

    def __init__(self, start_x_y, width_height, color):
        self.location = start_x_y
        self.width_height = width_height
        self.color = color
    
    def move(self, new_x_y):
        self.location = new_x_y
    
    def draw(self, window):
        x, y = self.location
        width, height = self.width_height
        rect(window, self.color, (x, y, width, height))