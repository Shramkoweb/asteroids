import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, TICK_TIME

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            dt = clock.tick(TICK_TIME) / 1000
            print(dt)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()