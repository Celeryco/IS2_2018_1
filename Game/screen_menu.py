import screen_tablero
import pygame
import constantes
# Obtener imagen del fondo

# Tamano de la ventana y foto background
size = constantes.DISPLAY_WIDTH, constantes.DISPLAY_HEIGHT
fondo = pygame.image.load('fondo.jpeg')
fondo = pygame.transform.scale(fondo, size)

class ScreenMenu:
    def __init__(self, manager):
        self.manager = manager

    def get_input(self):
        pass
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     elif event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RIGHT:
        #             # Cambiar de pantalla
        #             self.manager.mostrar_tablero()
    def update(self):
        pass

    def render(self):
        self.manager.surface.fill((200,200,200))
        self.manager.screen.blit(self.manager.surface, (0,0))

        pygame.display.update()

    def mostrar_tablero(self):
        self.manager.screen_actual = screen_tablero.ScreenTablero(self.manager)

    def cargar_botones(self):
        botones("Start",display,ColorBoton1,Boton1,TamBoton,identidad="start")
        botones("High Scores",display,ColorBoton2,Boton2,TamBoton,identidad="high_scores")
        botones("Description",display,ColorBoton3,Boton3,TamBoton,identidad="description")
        botones("Exit",display,ColorBoton4,Boton4,TamBoton,identidad="exit")
