import pygame as pg
from ..settings import *

class PowerupView(pg.sprite.Sprite):
    def __init__(self, powerup, game, x, y):
        self.powerup = powerup
        self.groups = game.all_sprites, game.powerups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.powerup.sprite
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x #* TILESIZE
        self.rect.y = y #* TILESIZE
