import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        pygame.Surface.fill(screen,(0,0,0)) #fill black
        pygame.display.flip() #screen refresh/update
















if __name__ == "__main__":
    main() 
