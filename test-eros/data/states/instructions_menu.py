import pygame as pg
from ..import settings, tools
from ..libraries import button

class InstructionsMenu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.quit = False
        self.previous = "MAIN_MENU"
        self.title = "INSTRUCTIONS"
        self.bgm = settings.MUSIC["menu"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.font2 = pg.font.Font(settings.FONTS["Fixedsys500c"], 30)
        self.font3 = pg.font.Font(settings.FONTS["Fixedsys500c"], 20)
        self.blink = False
        self.timer = 0.0
        self.load_buttons()

    def startup(self, current_time, persistant):
        return tools._State.startup(self, current_time, persistant)

    def cleanup(self):
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
            self.button_instructions_next.click(mouse_position, self.instructions_next)

    def update(self, surface, keys, current_time, time_delta):
        self.current_time = current_time
        if self.current_time-self.timer > 1000.0/5.0:
            self.blink = not self.blink
            self.timer = self.current_time
        self.draw(surface)

    def draw(self, surface):
        #Draw surface
        surface.fill(settings.BGCOLOR)
        title = self.font.render(self.title , 0 , settings.GREEN)
        player_1 = self.font2.render("Player 1" , 0 , settings.YELLOW)
        player_2 = self.font2.render("Player 2" , 0 , settings.YELLOW)
        surface.blit(title, (250, 25))
        surface.blit(player_1, (150, 100))
        surface.blit(player_2, (550, 100))
        #Draw Buttons
        self.button_back.draw(surface)
        self.button_instructions_next.draw(surface)
        #Draw Keyboard
        self.keyboard_draw(surface)
        #Draw Controls
        self.controls_draw(surface)

    def keyboard_draw(self, surface):
        keyboard_1 = settings.GFX['keyboard2']
        keyboard_1 = pg.transform.scale(keyboard_1, (128, 128))
        keyboard_2 = settings.GFX['keyboard2']
        keyboard_2 = pg.transform.scale(keyboard_2, (128, 128))
        surface.blit(keyboard_1, (150,150))
        surface.blit(keyboard_2, (550,150))

    def controls_draw(self, surface):
        instructions_1 = {"left" : "A = Go left", "right" : "D = Go right",
        "up" : "W = Go up", "down" : "S = Go down", "bomb" : "C = Drop bomb"}
        instructions_2 = {"left" : "Left Arrow = Go left", "right" : "Right Arrow = Go right",
        "up" : "Up Arrow = Go up", "down" : "Down Arrow = Go down", "bomb" : "/ = Drop bomb"}

        y = 300
        for key, value in instructions_1.items():
            insts = self.font3.render(value , 0 , settings.WHITE)
            surface.blit(insts, (150, y))
            y+=40

        y = 300
        for key, value in instructions_2.items():
            insts = self.font3.render(value , 0 , settings.WHITE)
            surface.blit(insts, (530, y))
            y+=40


    def load_buttons(self):
        self.button_back = button.Button("BACK", 150, 550, 140, 50, 30, 15, 2)
        self.button_instructions_next = button.Button("NEXT", 550, 550, 140, 50, 35, 15, 2)

    def go_main_menu(self):
        self.next = "MAIN_MENU"
        self.done = True

    def instructions_next(self):
        self.next = "INSTRUCTIONS_2"
        self.done = True
