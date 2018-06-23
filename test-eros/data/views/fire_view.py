import pygame as pg
from settings import *

class FireView(pg.sprite.Sprite):
    def __init__(self, fire, game, x, y):
        self.fire = fire
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(self.fire.sprite_url)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
