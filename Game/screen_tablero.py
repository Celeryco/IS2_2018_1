import pygame
import sys

class ScreenTablero:
    def __init__(self, manager):
        self.manager = manager
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass
    def render(self):
        self.manager.surface.fill((255,0,0))
        self.manager.screen.blit(self.manager.surface, (0,0))
        pygame.display.update()
    def mostrar_tablero(self):
        pass
