import pygame
import random
import time
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
print(img_folder)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.abspath(os.path.join(img_folder, "p2.png")))
        # self.image = pygame.image.load('p1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My Ggame")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
palyer = Player()
all_sprites.add(palyer)

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






