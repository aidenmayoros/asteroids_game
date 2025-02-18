import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        random_angle = random.uniform(20, 50)

        left_velocity = self.velocity.rotate((-random_angle) * 1.2)
        right_velocity = self.velocity.rotate((random_angle) * 1.2)

        new_radius = max(self.radius // 2, ASTEROID_MIN_RADIUS)
        left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        left_asteroid.velocity = left_velocity
        right_asteroid.velocity = right_velocity

        for container in self.containers:
            container.add(left_asteroid, right_asteroid)

        self.kill()
