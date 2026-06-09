import pygame

import logger
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0.0
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True:
        logger.log_state()
        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
