import sys
import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        for asteroid in asteroids:
            if player.isColliding(asteroid):
                sys.exit("Game Over!")
            for shot in shots:
                if shot.isColliding(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.Surface.fill(screen, (0,0,0))
        
        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip()
        
        # set to 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()