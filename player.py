from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame
import math

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        #self.position = pygame.Vector2(x, y)
        #self.velocity = pygame.Vector2(0, 0)
        #self.radius = radius
        self.shotTimer = 0
        self.acceleration = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen,(255,255,255), self.triangle(),2)

    def rotate(self, dt):
        self.rotation += PLAYER_TRUN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        
        self.shotTimer -= dt #shot timeout
        
        self.position += self.velocity  * dt #move them based on Velocity every tick
        self.wrap()



    def move(self,dt, player=True):
        newVelocity = pygame.Vector2(self.get_circle_coordinates(self.rotation))
        if player == True: #Move called by keys pressed
            self.velocity += newVelocity * PLAYER_SPEED
        else: #Move called by shots fired
            self.velocity -= newVelocity * PLAYER_SHOT_VELOCITY

    def get_circle_coordinates(self,t): #Used in self.move
        t = t + 90 # 90 degree correction
        t = t * (math.pi / 180)
        x = math.cos(t)
        y = math.sin(t)
        return x, y

    def shoot(self,dt):
        if self.shotTimer <= 0:
            singleShot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            singleShot.velocity = pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.shotTimer = PLAYER_SHOT_TIMEOUT
            self.move(dt, player=False)

        
        