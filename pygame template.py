import pygame
import random
import time

WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Ggame")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game loop
running = True
while running:
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw / rendrer
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.QUIT()






