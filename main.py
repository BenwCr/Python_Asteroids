import pygame
from constants import *
from player import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    plyr = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    timeClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen,(0,0,0)) #fill black
        plyr.draw(screen) #draw Player
        plyr.update(dt)
        pygame.display.flip() #screen refresh/update
        dt = timeClock.tick(60)/1000


        for event in pygame.event.get(): #quit if window is closed
            if event.type == pygame.QUIT:
                return
            
















if __name__ == "__main__":
    main() 
