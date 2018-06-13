import pygame as pg

from ..import settings, tools
from ..libraries import PygButton as pygbutton

class MainMenu(tools._State):
    """Scene that plays our intro movie."""
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.play_button = pygbutton.PygButton((settings.WIDTH/2, settings.HEIGHT / 2, settings.WIDTH/2, settings.HEIGHT / 2), 'Jugar')
        self.highscore_button = pygbutton.PygButton((50, 150, 60, 30), 'Highscore')
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0

    def startup(self, current_time, persistant):
        """Load and play the movie on scene start."""
        # movie_name = settings.MOV["test-mpeg"]
        # self.movie = movie.Movie(movie_name, (0,0), 3)
        # self.movie.rect.center = settings.SCREEN_RECT.center
        # return tools._State.startup(self, current_time, persistant)
        pass

    def cleanup(self):
        """Stop the movie when scene is done."""
        # self.movie.stop(delete=True)
        # return tools._State.cleanup(self)
        pass

    def get_event(self, event):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                    
            if 'click' in self.play_button.handleEvent(event):
                settings.BGCOLOR = settings.GREEN
            if 'click' in self.highscore_button.handleEvent(event):
                print("Click en boton highscore")

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        self.play_button.draw(settings.SCREEN)
        self.highscore_button.draw(settings.SCREEN)



    def update(self, surface, keys, current_time, time_delta):
        """Update blink; end scene if intro movie is done; draw everything."""
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

# def define_text(self, msg, color, position_x, position_y, width, height, dimension = "pequeno"):
#     surface_text, rect_text = create_text(msg, color, dimension)
#     textoRect.center=(BotonX+(Ancho/2),BotonY+(Alto/2))
#     surface.blit(textoSuperficie,textoRect)
#
# def create_text(self, text, color, dimension):
#     if dimension == "pequeno":
#         surface_text = pequenafuente.render(texto,True,color)
#     return textoSuperficie,textoSuperficie.get_rect()
#
# def create_buttons(text,surface, state, position, dimension, identity=None):
#     mouse = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#
#     if position[0]+dimension[0] >mouse[0] > dimension[0] and position[1] + dimension[1] > mouse[1] >dimension[1] and position[1] + dimension[1] < mouse [1] + dimension[1]:
#         if click[0]==1:
#             if identity =="INSTRUCTIONS":
#                 instructions()
#             elif identity =="MAIN_MENU":
#                 if main_menu.is_disabled():
#                     main_menu.enable()
#
#         button = pygame.draw.rect(surface,state[1],(position[0],position[1],dimension[0],dimension[1]))
#     else:
#         button = pygame.draw.rect(surface,state[0],(position[0],position[1],dimension[0],dimension[1]))
#
#     define_text(texto, black_color,position[0],position[1],dimension[0],dimension[1])
#
#     return boton
