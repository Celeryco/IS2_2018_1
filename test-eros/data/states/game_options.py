import pygame as pg

from ..import settings, tools
from ..libraries import button

class GameOptionsMenu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.quit = False
        self.previous = "MAIN_MENU"
        self.title = "OPTIONS"
        self.bgm = settings.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.load_buttons(320, 550)

    def startup(self, current_time, persistant):
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
        pg.mixer.music.stop()
        return tools._State.cleanup(self)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.quit = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            self.button_back.click(mouse_position, self.go_main_menu)

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        surface.fill(settings.BGCOLOR)

        # Draw buttons
        self.button_back.draw(surface)

        # Draw scores
        title = self.font.render(self.title , 0 , settings.GREEN)
        surface.blit(title, (290, 25))

    def update(self, surface, keys, current_time, time_delta):
        self.current_time = current_time
        if self.current_time - self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def load_buttons(self, x, y):
        self.button_back = button.Button("BACK", x, y, 140, 50, 30, 15, 2)

    def go_main_menu(self):
        # UTILIZAR PERSIST PARA EL NOMBRE DEL JUGADOR Y POSIBLEMENTE EL MAPA
        self.next = "MAIN_MENU"
        self.done = True

    def quit(self):
        self.quit = True
