import pygame as pg

from ..import settings, tools

class MainMenu(tools._State):
    """Scene that plays our intro movie."""
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.bgm = prepare.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.play_music()
        self.load_buttons()

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
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.input.delete()
                else:
                    self.input.add(event.unicode)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_position = pg.mouse.get_pos()
                self.button_start.click(mouse_position, self.start)
                self.button_instructions.click(mouse_position, self.instructions)
                self.button_high_score.click(mouse_position, self.high_score)
                self.button_quit.click(mouse_position, self.quit)

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        self.screen.fill(settings.BGCOLOR)
        #Draw Button
        self.button_start.draw()
        self.button_instructions.draw()
        self.button_high_score.draw()
        self.button_quit.draw()
        self.input.draw()
        pg.display.flip()


    def update(self, surface, keys, current_time, time_delta):
        """Update blink; end scene if intro movie is done; draw everything."""
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def load_buttons(self):
        self.button_start = Button(self.screen, "START", 450, 340, 140, 50, 25, 15, 2)
        self.button_instructions = Button(self.screen, "INSTRUCTIONS", 425, 420, 230, 50, 10, 15, 2)
        self.button_high_score = Button(self.screen, "HIGH SCORE", 440, 500, 200, 50, 10, 15, 2)
        self.button_quit = Button(self.screen, "QUIT", 450, 580, 140, 50, 35, 15, 2)
        self.input = Input(self.screen, "", 425, 250, 190, 50, 20, 15, 2, 11)
