import pygame as pg
from ..import settings, tools
from ..libraries import button

class HighScore(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.quit = False
        self.previous = "MAIN_MENU"
        self.title = "HIGHSCORES"
        self.bgm = settings.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.list_highscores = []
        self.load_buttons()

    def startup(self, current_time, persistant):
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
        pg.mixer.music.stop()
        return tools._State.cleanup(self)

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.done = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_position = pg.mouse.get_pos()
            self.button_back.click(mouse_position, self.go_main_menu)

    def draw(self, surface):
        """Blit all items to the surface including the movie."""
        surface.fill(settings.BGCOLOR)

        # Draw rectangles
        # pg.draw.rect(surface, settings.GREEN, ((50,150),(300, 300)), 5)
        # pg.draw.rect(surface, settings.GREEN, ((450,150),(300, 300)), 5)
        pg.draw.rect(surface, settings.GREEN, ((275,150),(300, 300)), 5)

        # Draw buttons
        self.button_back.draw(surface)

        # Draw scores
        desc_font = pg.font.Font(settings.FONTS["Fixedsys500c"], 20)
        # for score in self.list_highscores:
        #     score_name = desc_font.render(self.list_highscores.player.name , 0 , (0,0,0))
        #     score_map = desc_font.render(self.list_highscores.player.map , 0 , (0,0,0))
        #     score_points = desc_font.render(self.list_highscores.player.points , 0 , (0,0,0))
        #     display.blit(score_name,(pos_x, pos_y))
        #     display.blit(score_map, (pos_x + 50, pos_y + 15))
        #     pos_y = pos_y + 50
        title = self.font.render(self.title , 0 , (185, 204, 81))
        surface.blit(title, (290, 70))

        name = desc_font.render("Name" , 0 , (255,255,255))
        map = desc_font.render("Map" , 0 , (255,255,255))
        score = desc_font.render("Score" , 0 , (255,255,255))

        surface.blit(name, (300, 160))
        surface.blit(map, (410, 160))
        surface.blit(score, (500, 160))

        desc_name = desc_font.render("Angelo" , 0 , (255,255,255))
        desc_map = desc_font.render("Mapa_1" , 0 , (255,255,255))
        desc_score = desc_font.render("9999" , 0 , (255,255,255))

        surface.blit(desc_name, (300, 200))
        surface.blit(desc_map, (400, 200))
        surface.blit(desc_score, (510, 200))




    def update(self, surface, keys, current_time, time_delta):
        self.current_time = current_time
        if self.current_time - self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def load_buttons(self):
        self.button_back = button.Button("BACK", 350, 500, 140, 50, 30, 15, 2)

    def go_main_menu(self):
        self.next = "MAIN_MENU"
        self.done = True

    def quit(self):
        self.quit = True
