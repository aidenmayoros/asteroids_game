import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60)


if __name__ == "__main__":
    main()
