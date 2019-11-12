import tkinter as tk
from tkinter import messagebox

import pygame
from pygame import display, draw
from pygame.time import Clock, delay

from snake.apple import AppleGenerator
from snake.snake import Snake


class Game:

    def __init__(self):
        pygame.init()
        self.CLOCK = Clock()
        self.ROWS_COLS = 15
        self.GRID_SIZE = 50
        self.SCREEN_SIZE = self.GRID_SIZE * self.ROWS_COLS
        self.DISPLAY = display.set_mode((self.SCREEN_SIZE, self.SCREEN_SIZE))
        self.BACKGROUND_COLOR = (0, 0, 0)
        self.GRID_COLOR = (100, 100, 100)
        self.SNAKE_COLOR = (0, 255, 0)
        self.apple_generator = AppleGenerator(self.ROWS_COLS, self.GRID_SIZE)
        self.apple = self.apple_generator.generate_apple(self.snake)
        mid = (self.ROWS_COLS // 2) * self.GRID_SIZE
        self.start_x_y = (mid, mid)
        self.snake = Snake(self.start_x_y, self.GRID_SIZE, self.SCREEN_SIZE, self.SNAKE_COLOR, self.spawn_apple)
        self.exit_clicked = None
        self.playing = None

    def start(self):
        self.playing = True
        self.exit_clicked = False
        self.reset()
        while self.playing:
            self.CLOCK.tick(10)
            delay(50)

            if not self.exit_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        # noinspection PyAttributeOutsideInit
                        self.exit_clicked = True
                        self.playing = False
                        # Doesn't close immediately. Will still run a few cycles.
                        pygame.quit()

            if not self.exit_clicked:
                self.snake.move()
                self.playing = self.playing and not self.snake.has_collided

                if self.playing:
                    self.draw_game()
                elif not self.exit_clicked:
                    print('Score: ', len(self.snake.body) + 1)
                    self.message_box('You lost!', 'Play again?')
                    self.reset()
                    # noinspection PyAttributeOutsideInit
                    self.playing = True

    def spawn_apple(self):
        self.apple = self.apple_generator.generate_apple(self.snake)
        self.snake.set_apple(self.apple)

    def reset(self):
        self.snake = Snake(self.start_x_y, self.GRID_SIZE, self.SCREEN_SIZE, self.SNAKE_COLOR, self.spawn_apple)
        self.spawn_apple()

    def draw_game(self):
        self.DISPLAY.fill(self.BACKGROUND_COLOR)
        self.draw_grid()
        self.snake.draw(self.DISPLAY)
        self.apple.draw(self.DISPLAY)
        display.update()

    def draw_grid(self):
        x, y = 0, 0

        for i in range(self.ROWS_COLS):
            x += self.GRID_SIZE
            y += self.GRID_SIZE

            draw.line(self.DISPLAY, self.GRID_COLOR, (x, 0), (x, self.SCREEN_SIZE))
            draw.line(self.DISPLAY, self.GRID_COLOR, (0, y), (self.SCREEN_SIZE, y))

    @staticmethod
    def message_box(subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        # noinspection PyBroadException
        try:
            root.destroy()
        except:
            pass
