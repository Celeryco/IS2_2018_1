# En init de View se mete una clas player. Debe tener un atributo Player
import pygame as pg
from ..settings import *
from ..models.fire import Fire
from . import fire_view

class BombView(pg.sprite.Sprite):
    def __init__(self, bomb, game, x, y):
        self.bomb = bomb
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = self.bomb.sprite
        self.rect = self.image.get_rect()
        self.rect.x = round(x / TILESIZE) * TILESIZE
        self.rect.y = round(y / TILESIZE) * TILESIZE
        self.start = pg.time.get_ticks()
        self.fires = []
        self.level = self.bomb.fire_lvl

    def track(self):
        if pg.time.get_ticks() - self.start > 3000:
            self.exploit()

        if pg.time.get_ticks() - self.start > 4000:
            for fire in self.fires:
                fire.kill()

    # MODIFICAR EL FIRE
    def exploit(self):
        fire_model = Fire(GFX['fire'])
        self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y))
        for i in range(self.level):
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y - TILESIZE * i) )
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x - TILESIZE * i, self.rect.y) )
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x + TILESIZE * i, self.rect.y) )
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y + TILESIZE * i) )
        self.kill()
