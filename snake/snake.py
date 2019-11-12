from snake.box import Box
from snake.movement.pygame import PygameMovement

class Snake:

    def __init__(self, start_X_Y, grid_size, screen_size, color, spawn_apple, starting_size=1, movement=PygameMovement()):
        self.color = color
        self.spawn_apple = spawn_apple
        self.screen_size = screen_size
        self.movement = movement
        self.grid_size = grid_size
        self.box_size = (grid_size, grid_size)
        self.head = Box(start_X_Y, self.box_size, color)
        self.body = []
        self.xvel = 1 # move right
        self.yvel = 0
        for i in range(starting_size - 1):
            self.grow((self.head.x - (grid_size * i), self.head.y))
    
    def grow(self, location):
        self.body.insert(0, Box(location, self.box_size, self.color))
    
    def draw(self, window):
        self.head.draw(window)

        for box in self.body:
            box.draw(window)
    
    def set_apple(self, apple):
        self.apple = apple
    
    def move(self):
        old_head_x_y = self.head.location
        old_tail_x_y = (0, 0)
        if len(self.body) > 0:
            old_tail_x_y = self.body[0].location

        temp = 0
        new_location = (0, 0)
        direction = self.movement.get_direction()
        if direction == "LEFT":
            self.xvel = -1
            self.yvel = 0
        if direction == "RIGHT":
            self.xvel = 1
            self.yvel = 0
        if direction == "UP":
            self.xvel = 0
            self.yvel = -1
        if direction == "DOWN":
            self.xvel = 0
            self.yvel = 1
        
        if self.xvel != 0:
            temp = old_head_x_y[0] + (self.xvel * self.grid_size)
            new_location = (temp, old_head_x_y[1])
        if self.yvel != 0:
            temp = old_head_x_y[1] + (self.yvel * self.grid_size)
            new_location = (old_head_x_y[0], temp)
        
        self.has_collided = self.will_collide(new_location)
        
        for i, box in enumerate(self.body):
            if i == len(self.body) - 1:
                box.move(old_head_x_y)
            else:
                box.move(self.body[i+1].location)
        
        self.head.move(new_location)

        if self.head.location == self.apple.location:
            self.spawn_apple()
            if len(self.body) > 0:
                self.grow(old_tail_x_y)
            else:
                self.grow(old_head_x_y)
    
    def will_collide(self, new_location):
        x, y = new_location
        valid = (0 <= x < self.screen_size) and (0 <= y < self.screen_size)
        if valid:
            for box in self.body:
                if box.location == new_location:
                    return True
        return not valid
    
    def collides(self, location):
        collides = self.head.location == location
        if not collides:
            for box in self.body:
                if box.location == location:
                    collides = True
                    break
        return collides
