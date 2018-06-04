## Pygame template - skeleton for a new python project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

## Useful colors
WHITE = (255 ,255 ,255)
BLACK = (0 ,0 ,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0 ,0 ,255)

## Initialize pygame and create window
pygame.init()
# Initialize Sounds
pygame.mixer.init()

screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

## Game Loop
running = True
while running:
    clock.running(FPS)
    # Process input(events)
    if event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw / render
    screen.fill(BLACK)
    # to avoid lag. After finishing drawing
    pygame.display.flip()

pygame.quit()
