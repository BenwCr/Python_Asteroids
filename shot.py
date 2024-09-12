import pygame
from constants import *
from circleshape import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.position = pygame.Vector2(x, y)
        #self.velocity = pygame.Vector2(0, 0)
        #self.radius = radius
        self.decay = SHOT_DECAY

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt
        self.wrap()
        if self.decay <= 0:
            self.kill()
        self.decay -= dt

