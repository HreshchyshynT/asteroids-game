# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    pygame.font.init()

    screen = pygame.display.set_mode(
        size=(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT),
    )
    my_font = pygame.font.SysFont("Comic Sans MS", 30)
    updatable, drawable, asteroids, shots = (
        pygame.sprite.Group(),
        pygame.sprite.Group(),
        pygame.sprite.Group(),
        pygame.sprite.Group(),
    )
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(
        constants.SCREEN_WIDTH / 2,
        constants.SCREEN_HEIGHT / 2,
    )

    scores = 0

    _ = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.is_collision(bullet):
                    scores += asteroid.radius / constants.ASTEROID_MIN_RADIUS

                    asteroid.split()
                    bullet.kill()
                    break

            if asteroid.is_collision(player):
                print("Game over!")
                print(f"Total score: {scores}")
                exit()

        score_surface = my_font.render(f"Score: {scores}", False, "white")
        screen.blit(
            score_surface, (screen.get_width() - score_surface.get_width() - 16, 16)
        )
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
