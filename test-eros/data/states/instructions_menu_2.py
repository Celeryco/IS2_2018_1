import pygame as pg
from ..import settings, tools
from ..libraries import button

class InstructionsMenu2(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = None
        self.quit = False
        self.previous = "INSTRUCTIONS"
        self.title = "INSTRUCTIONS 2"
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
        powerups = self.font2.render("Powerups" , 0 , settings.YELLOW)
        surface.blit(title, (250, 25))
        surface.blit(powerups, (150, 100))
        #Draw Buttons
        self.button_back.draw(surface)
        self.button_instructions_next.draw(surface)
        #Draw Powerups
        self.powerups_draw(surface, 75, 150, 70)
        #Draw Characters
        # self.characters_draw(surface, 75, 150, 70)

    def powerups_draw(self, surface, x, y, spacing):
        bomb_up = pg.transform.scale(settings.GFX['bomb-up'], (48, 48))
        fire_up = pg.transform.scale(settings.GFX['fire-up'], (48, 48))
        heart = pg.transform.scale(settings.GFX['heart'], (48, 48))
        shield = pg.transform.scale(settings.GFX['shield'], (48, 48))
        speed_up = pg.transform.scale(settings.GFX['speed-up'], (48, 48))

        surface.blit(bomb_up, (x, y))
        surface.blit(fire_up, (x, y + spacing))
        surface.blit(heart, (x, y + (spacing*2)))
        surface.blit(shield, (x, y + (spacing*3)))
        surface.blit(speed_up, (x, y + (spacing*4)))

        power_ups_desc = {"bomb" : "Bomb count +1", "fire" : "Fire power +1",
        "heart" : "Gives you one extra life", "shield" : "Protects you from bombs once", "speed" : "Speed +1"}

        for key, value in power_ups_desc.items():
            insts = self.font3.render(value , 0 , settings.WHITE)
            surface.blit(insts, (x + 60, y + 15))
            y+=spacing

    # def controls_draw(self, surface, x, y):
    #     power_ups_img = {}
    #     power_ups_desc = {"left" : "Left Arrow = Go left", "right" : "Right Arrow = Go right",
    #     "up" : "Up Arrow = Go up", "down" : "Down Arrow = Go down", "bomb" : "/ = Drop bomb"}
    #
    #     y = 300
    #     for key, value in instructions_1.items():
    #         insts = self.font3.render(value , 0 , settings.WHITE)
    #         surface.blit(insts, (150, y))
    #         y+=40
    #
    #     y = 300
    #     for key, value in instructions_2.items():
    #         insts = self.font3.render(value , 0 , settings.WHITE)
    #         surface.blit(insts, (530, y))
    #         y+=40

    def load_buttons(self):
        self.button_back = button.Button("BACK", 150, 550, 140, 50, 30, 15, 2)
        self.button_instructions_next = button.Button("NEXT", 550, 550, 140, 50, 35, 15, 2)

    def go_main_menu(self):
        self.next = "MAIN_MENU"
        self.done = True

    def instructions_next(self):
        self.next = "INSTRUCTIONS"
        self.done = True
