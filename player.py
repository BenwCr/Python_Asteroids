from circleshape import CircleShape
import pygame
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        #self.position = pygame.Vector2(x, y)
        self.rotation = 0
        #self.position = pygame.Vector2(x, y)
        #self.velocity = pygame.Vector2(0, 0)
        #self.radius = radius

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(),20)
        print(self.triangle())