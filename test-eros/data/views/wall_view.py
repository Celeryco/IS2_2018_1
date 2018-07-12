import pygame as pg
from ..settings import *

# class WallView(pg.sprite.Sprite):
    # def __init__(self, wall, game, x, y):
    #     self.wall = wall
    #     self.groups = game.all_sprites, game.walls
    #     pg.sprite.Sprite.__init__(self, self.groups)
    #     self.game = game
    #     # self.image = pg.Surface((TILESIZE, TILESIZE))
    #     # self.image.fill(GREEN)
    #     # self.rect = self.image.get_rect()
    #     #self.image = self.check_breakability()
    #     self.rect = self.image.get_rect()
    #     self.x = x
    #     self.y = y
    #     self.rect.x = x * TILESIZE
    #     self.rect.y = y * TILESIZE

#    def check_breakability(self):
#        self.image = pg.Surface((TILESIZE, TILESIZE))
#        if self.wall.isBreakable:
#            self.image.fill(YELLOW)
#        else:
#            self.image.fill(GREEN)
#        return self.image

class ObstacleView(pg.sprite.Sprite):
    def __init__(self, type ,game, x, y, w, h):
        self.groups =  game.walls
        self.type = type
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
