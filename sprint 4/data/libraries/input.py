import pygame as pg

class Input():
    def __init__(self, text, x, y, width, height, padding_x, padding_y, border, limit):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.border = border
        self.limit = limit

    def draw(self, surface):
        self.rect = pg.draw.rect(surface, (247, 177, 33),(self.x, self.y, self.width, self.height), self.border)
        self.button_text = pg.font.SysFont('Consolas', 32).render(self.text, True, (247, 177, 33))
        surface.blit(self.button_text, (self.x + self.padding_x, self.y + self.padding_y))


    def add(self, character):
        if len(self.text) <= self.limit:
            self.text = self.text + character

    def delete(self):
        self.text = self.text[:-1]
