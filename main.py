import pygame
import sys

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, TICK_TIME
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        # limit the frame rate to 60 FPS
        dt = clock.tick(TICK_TIME) / 1000


if __name__ == "__main__":
    main()
