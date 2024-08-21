import pygame
import math

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_coliding(self, csObj):
        distance = self.position.distance_to(csObj.position)
        objSize = self.radius + csObj.radius
        if distance < objSize:
            return True
        return False
    
    def get_circle_coordinates(t):
        x = math.cos(t)
        y = math.sin(t)
        return x, y