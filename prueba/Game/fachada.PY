import pygame
import screen_menu
import screen_tablero
#size display
display_width=800
display_height=600

class ScreenManager:
    #Functions
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((display_width,display_height))
        self.title =pygame.display.set_caption("Bomberman Peruvian Deluxe")   #titulo de la ventana
        self.surface = pygame.Surface(self.screen.get_size())
        self.screen_actual = screen_menu.ScreenMenu(self)

    def mostrar_tablero(self):
        self.screen_actual.mostrar_tablero()

    def comenzar(self):

        while True:
            # Obtener el input
            self.screen_actual.get_input()
            # Actualizar la logica
            self.screen_actual.update()
            # Render
            self.screen_actual.render()

def main():
    screenManager = ScreenManager()
    screenManager.comenzar()


if __name__ == '__main__':
    main()
