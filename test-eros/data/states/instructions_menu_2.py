import pygame as pg

from .. import settings, tools

class InstructionsMenu2(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.next = None

    def cleanup(self):
        print('Cleaning up Menu state stuff')
        pass

    def startup(self, current_time, persistant):
        print('Starting Menu state stuff')
        pass

    def get_event(self, event):
        if event.type == pg.QUIT:
            self.done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.done = True
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
        surface.fill(settings.BGCOLOR)

    def powerups_draw(position_x, position_y):
        pass

    def enemies_draw(position_x, position_y):
        pass
