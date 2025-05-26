# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
    )
    clock = pygame.time.Clock()
    dt = 0
    player = Player(
        constants.SCREEN_WIDTH / 2,
        constants.SCREEN_HEIGHT / 2,
    )
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
