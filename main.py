import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    timeClock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen,(0,0,0)) #fill black
        pygame.display.flip() #screen refresh/update
        dt = timeClock.tick(60)/1000
        print(dt)


        for event in pygame.event.get(): #quit if window is closed
            if event.type == pygame.QUIT:
                return
            
















if __name__ == "__main__":
    main() 
