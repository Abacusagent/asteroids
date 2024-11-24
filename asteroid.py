from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0,0)


    def draw(self, screen):
        colour = (255, 255, 255)
        pygame.draw.circle(screen, colour, (int(self.position.x), int(self.position.y)), 2)

    def update(self, dt):
        self.position += self.velocity * dt

        
        