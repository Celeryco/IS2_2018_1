# En init de View se mete una clas player. Debe tener un atributo Player
import pygame as pg
from ..settings import *
from ..models.fire import Fire
from . import fire_view
import math

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

    def track(self, bomb_list, index):
        if pg.time.get_ticks() - self.start > 3000:
            self.kill()
            self.exploit()

        if pg.time.get_ticks() - self.start > 4000:
            for fire in self.fires:
                fire.kill()
            self.fires.clear()
            bomb_list.pop(index)

    # MODIFICAR EL FIRE
    def exploit(self):
        fire_model = Fire(GFX['fire'])
        fire = fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y)
        self.fires.append(fire)
        # dist_right = math.hypot(self.game.walls.rect.x - self.rect.x, self.game.walls.rect.y - self.rect.y)
        # print(dist_right)
        for i in range(self.level):
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y - TILESIZE * i))
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x - TILESIZE * i, self.rect.y))
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x + TILESIZE * i, self.rect.y))
            self.fires.append(fire_view.FireView(fire_model, self.game, self.rect.x, self.rect.y + TILESIZE * i))
            for fire in self.fires:
                # pg.sprite.spritecollide(fire, self.game.all_sprites, True)
                pg.sprite.spritecollide(fire, self.game.enemies, True)
                hits = pg.sprite.spritecollide(fire, self.game.walls, False)
                print(hits)
                for hit in hits:
                    if hit.type == 'cabeza':
                        hit.kill()
