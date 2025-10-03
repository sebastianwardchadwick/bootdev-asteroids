import pygame
from constants import *
from player import Player

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
    print("Initialising Player...")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Done!")
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                            return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(f"fps: {clock.get_fps()}")

if __name__ == "__main__":
    main()
