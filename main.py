import pygame
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        colour = (0, 0, 0)
        display = pygame.Surface.fill(screen, colour)
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        fps = Clock.tick(60)
        dt = (fps / 1000)
    



if __name__ == "__main__":
    main()
    
