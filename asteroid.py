from circleshape import CircleShape
import pygame
import random
import constants


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_velocity_left = self.velocity.rotate(-angle)
        new_velocity_right = self.velocity.rotate(angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = new_velocity_left * 1.2
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = new_velocity_right * 1.2
