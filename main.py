import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Creating the Screen...")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting clock...")
    clock = pygame.time.Clock()
    dt = 0
    print("Done!")
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        screen.fill("black")
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(f"fps: {clock.get_fps()}")

if __name__ == "__main__":
    main()
