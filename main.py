import pygame
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while 2 == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        colour = (0, 0, 0)
        display = pygame.Surface.fill(screen, colour)
        pygame.display.flip()
    return display



if __name__ == "__main__":
    main()
    