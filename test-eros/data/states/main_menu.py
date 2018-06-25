import pygame as pg

from ..import settings, tools
from ..libraries import button, input

class MainMenu(tools._State):
    """Scene that plays our intro movie."""
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.bgm = settings.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.startup(self.timer, None)
        self.load_buttons()

    def startup(self, current_time, persistant):
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
        pg.mixer.music.stop()
        return tools._State.cleanup(self)

    def get_event(self, event):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.input_box.delete()
                else:
                    self.input_box.add(event.unicode)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_position = pg.mouse.get_pos()
                self.button_start.click(mouse_position, self.start)
                self.button_instructions.click(mouse_position, self.instructions)
                self.button_high_score.click(mouse_position, self.high_score)
                self.button_quit.click(mouse_position, self.quit)

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        surface.fill(settings.BGCOLOR)
        #Draw Buttons
        self.button_start.draw(surface)
        self.button_instructions.draw(surface)
        self.button_high_score.draw(surface)
        self.button_quit.draw(surface)
        self.input_box.draw(surface)

    def update(self, surface, keys, current_time, time_delta):
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def load_buttons(self):
        self.button_start = button.Button("START", 450, 340, 140, 50, 25, 15, 2)
        self.button_instructions = button.Button("INSTRUCTIONS", 425, 420, 230, 50, 10, 15, 2)
        self.button_high_score = button.Button("HIGH SCORE", 440, 500, 200, 50, 10, 15, 2)
        self.button_quit = button.Button("QUIT", 450, 580, 140, 50, 35, 15, 2)
        self.input_box = input.Input("", 425, 250, 190, 50, 20, 15, 2, 11)

    def high_score(self):
        pass

    def instructions(self):
        pass

    def quit(self):
        self.done = True
