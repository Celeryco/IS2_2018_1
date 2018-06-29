import screen_tablero
import pygame
class ScreenMenu:
    def __init__(self, manager):
        self.manager = manager
    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Cambiar de pantalla
                    self.manager.mostrar_tablero()
    def update(self):
        pass
    def render(self):
        self.manager.surface.fill((200,200,200))
        self.manager.screen.blit(self.manager.surface, (0,0))
        pygame.display.update()

    def mostrar_tablero(self):
        self.manager.screen_actual = screen_tablero.ScreenTablero(self.manager)
