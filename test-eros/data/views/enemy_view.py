import pygame as pg
from .. import settings
vec = pg.math.Vector2

class EnemyView(pg.sprite.Sprite):
    def __init__(self, enemy, game, x, y):
        self.enemy = enemy
        self.groups = game.all_sprites, game.enemies
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_alpha = self.enemy.sprite
        #self.image_alpha.set_clip(pg.Rect(0, 0, 52, 76))
        self.image_alpha.set_clip(pg.Rect(0, 0, 26, 38))#
        self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0

#        self.right_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
#        self.left_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
#        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
#        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }

        self.right_states = { 0: (0, 38, 26, 38), 1: (26, 38, 26, 38), 2: (78, 38, 26, 38) } #
        self.left_states = { 0: (0, 76, 26, 38), 1: (26, 76, 26, 38), 2: (78, 76, 26, 38) } #
        self.up_states = { 0: (0, 114, 26, 38), 1: (26, 114, 26, 38), 2: (78, 114, 26, 38) } #
        self.down_states = { 0: (0, 0, 26, 38), 1: (26, 0, 26, 38), 2: (78, 0, 26, 38) } #


        self.vel = vec(0, 0)
        self.pos = vec(x, y) #* settings.TILESIZE
        self.state = 0

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.image_alpha.set_clip(pg.Rect(self.get_frame(clipped_rect)))
        else:
            self.image_alpha.set_clip(pg.Rect(clipped_rect))
        return clipped_rect

    def get_keys(self):
        # if self.state : return
        # self.vel=vec(0,0)
        # keys = pg.key.get_pressed()
        pass

    def update(self):
        self.get_keys()
        self.pos+= self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
