## Pygame template - skeleton for a new python project
import pygame
import random
import settings
from settings import *

## Initialize pygame and create window
pygame.init()
# Initialize Sounds
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

## Game Loop
running = True
while running:
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # to avoid lag. After finishing drawing
    pygame.display.flip()

pygame.quit()
