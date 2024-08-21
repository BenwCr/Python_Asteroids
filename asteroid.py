from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    
    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        randomAngle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(randomAngle)
        vel2 = self.velocity.rotate(-randomAngle)
        newR = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x,self.position.y,newR) 
        asteroid2 = Asteroid(self.position.x,self.position.y,newR)
        asteroid1.velocity = vel1 * 1.2
        asteroid2.velocity = vel2 * 1.2


        
        

   