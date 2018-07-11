import pygame as pg
from ..import settings, tools
from ..libraries import button, input

class MainMenu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.quit = False
        self.next = None
        self.title = "Peruvian Heart"
        self.title2 = "Deluxe Edition"
        self.bgm = settings.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.load_buttons(300, 250)
        # self.load_music()

    def load_music(self):
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)

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
            if event.key == pg.K_BACKSPACE:
                self.input_box.delete()
            else:
                self.input_box.add(event.unicode)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            print(mouse_position)
            self.button_start.click(mouse_position, self.start_game)
            self.button_instructions.click(mouse_position, self.instructions)
            self.button_high_score.click(mouse_position, self.high_score)
            self.button_options.click(mouse_position, self.options)
            self.button_quit.click(mouse_position, self.end_game)

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        surface.fill(settings.BGCOLOR)
        title = self.font.render(self.title , 0 , settings.GREEN)
        title2 = self.font.render(self.title2 , 0 , settings.GREEN)
        surface.blit(title, (230, 25))
        surface.blit(title2, (230, 75))

        #Draw Buttons
        self.input_box.draw(surface)
        self.button_start.draw(surface)
        self.button_instructions.draw(surface)
        self.button_high_score.draw(surface)
        self.button_options.draw(surface)
        self.button_quit.draw(surface)

    def update(self, surface, keys, current_time, time_delta):
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def load_buttons(self, x, y):
        self.input_box = input.Input("", x - 20, y , 250, 40, 20, 5, 2, 15)
        self.button_start = button.Button("START", x, y + (60*1), 220, 45, 70, 15, 2)
        self.button_instructions = button.Button("INSTRUCTIONS", x, y + (60*2), 220, 50, 20, 15, 2)
        self.button_high_score = button.Button("HIGHSCORES", x, y + (60*3), 220, 50, 35, 15, 2)
        self.button_options = button.Button("OPTIONS", x, y + (60*4), 220, 50, 55, 15, 2)
        self.button_quit = button.Button("QUIT", x, y + (60*5), 220, 50, 75, 15, 2)

    def start_game(self):
        self.next = "GAME_SETTINGS"
        self.persist = {"player_name" : self.input_box.text}
        self.done = True

    def instructions(self):
        self.next = "INSTRUCTIONS"
        self.done = True

    def high_score(self):
        self.next = "HIGH_SCORE"
        self.done = True

    def options(self):
        self.next = "OPTIONS"
        self.done = True

    def end_game(self):
        self.quit = True
