import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from highscore import *

def printResults(time, score):
    pygame.quit()
    print("------------\n------------")
    print("Game over!")
    print (f"You Survived {int(time)} seconds")
    print (f"{score} Asteroids destroyed!")
    HSindex = is_highscore(score)
    if HSindex != -1:
        pygame.quit()
        print("--------------------NEW HIGH SCORE---------------------")
        name = input("What is your name?: ")
        open_doc()('write',score,int(time),name,HSindex)
    n = 0
    for e in open_doc()('read'):
        n += 1
        obj = e.split('/')
        if len(obj) == 3:
            print(f"{n}.  {obj[0]} asteroids destroyed, {obj[1]} seconds alive -------------------- {obj[2]}")
    

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    timeClock = pygame.time.Clock()
    totalTime = 0
    dt = 0
    score = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = updateable
    Shot.containers = (updateable, drawable, shots)

    plyr = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asterfield = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for obj in updateable:
            obj.update(dt)
        for obj in asteroids:
            if obj.is_coliding(plyr) is True:
                screen =pygame.display.set_mode((0,0),flags=pygame.HIDDEN)
                pygame.display.quit()
                pygame.quit()
                printResults(totalTime,score)
                sys.exit()
            for shot in shots:
                if shot.is_coliding(obj) is True:
                   obj.split()
                   shot.kill()
                   score += 1
        pygame.Surface.fill(screen,(0,0,0)) #fill black
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip() #screen refresh/update
        dt = timeClock.tick(60)/1000
        totalTime += dt


        for event in pygame.event.get(): #quit if window is closed
            if event.type == pygame.QUIT:
                printResults(totalTime,score)
                return
            
















if __name__ == "__main__":
    main() 
