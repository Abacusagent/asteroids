import pygame
from constants import *
from circleshape import CircleShape
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        colour = (255, 255, 255)
        pygame.draw.polygon(screen, colour, self.triangle(), 2)

    def rotate(self, dt, direction = 1):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):    
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)

    
