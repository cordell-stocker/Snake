from snake.movement.movement import Movement
import pygame


class PygameMovement(Movement):

    @staticmethod
    def get_direction():
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            return "LEFT"
        if keys[pygame.K_RIGHT]:
            return "RIGHT"
        if keys[pygame.K_UP]:
            return "UP"
        if keys[pygame.K_DOWN]:
            return "DOWN"
