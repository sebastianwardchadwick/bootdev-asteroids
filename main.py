import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    print("Initialising Groups...")
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    print("Initialising Player...")
    Player.containers = (updateables, drawables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Visualising Bullets...")
    Shot.containers = (shots, updateables, drawables)
    print("Initialising Asteroids...")
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    AsteroidField()
    print("Done!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateables.update(dt)
        for a in asteroids:
            if a.DetectCollisions(player):
                print("Game over!")
                return
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        # print(f"fps: {clock.get_fps()}")

if __name__ == "__main__":
    main()
