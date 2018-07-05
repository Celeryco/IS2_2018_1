import pygame as pg
from .. import settings
vec = pg.math.Vector2

class CharacterView(pg.sprite.Sprite):
    def __init__(self, character, game, x, y):
        self.character = character
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image_alpha = self.character.character_img
        #self.image_alpha.set_clip(pg.Rect(0, 0, 63, 50))
        self.image_alpha.set_clip(pg.Rect(0, 0, 21, 25))#

        self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())
        self.rect = self.image.get_rect()
        self.frame = 0

        #self.right_states = { 0: (0, 50, 63, 50), 1: (63, 50, 63, 50), 2: (156, 50, 63, 50) }
        #self.left_states = { 0: (0, 163, 63, 50), 1: (63, 163, 63, 50), 2: (156, 163, 63, 50) }
        #self.up_states = { 0: (0, 218, 63, 50), 1: (63, 218, 63, 50), 2: (156, 218, 63, 50) }
        #self.down_states = { 0: (0, 0, 63, 50), 1: (63, 0, 63, 50), 2: (156, 0, 63, 50) }
        self.right_states = { 0: (0, 25, 21, 25), 1: (21, 25, 21, 25), 2: (63, 25, 21, 25) } #
        self.left_states = { 0: (0, 50, 21, 25), 1: (21, 50, 21, 25), 2: (63, 50, 21, 25) } #
        self.up_states = { 0: (0, 75, 21, 25), 1: (21, 75, 21, 25), 2: (63, 75, 21, 25) } #
        self.down_states = { 0: (0, 0, 21, 25), 1: (21, 0, 21, 25), 2: (63, 0, 21, 25) } #

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

    def pause(self, state):
        self.state = state
        self.vx = 0
        self.vy = 0

    def get_keys(self):
        if self.state : return
        self.vel=vec(0,0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.clip(self.left_states)
            self.vel.x = -(settings.PLAYER_SPEED)
            self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.clip(self.right_states)
            self.vel.x = settings.PLAYER_SPEED
            self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.clip(self.up_states)
            self.vel.y = -(settings.PLAYER_SPEED)
            self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.clip(self.down_states)
            self.vel.y = settings.PLAYER_SPEED
            self.image = self.image_alpha.subsurface(self.image_alpha.get_clip())

    def update(self):
        self.get_keys()
        self.pos+= self.vel * self.game.dt
        self.rect.x = self.pos.x
        self.collide_with_powerup()
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        self.collied_with_enemy()

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x  = hits[0].rect.left - self.rect.width
                if self.vel.x < 0:
                    self.pos.x  = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def collide_with_powerup(self):
        hits = pg.sprite.spritecollide(self, self.game.powerups, True)
        if hits:
            if hits[0].powerup.type == "fire":
                self.character.fire_lvl += hits[0].powerup.modifier
                # hits[0].kill()
            if hits[0].powerup.type == "speed":
                self.character.speed_lvl += hits[0].powerup.modifier
                # hits[0].kill()

    def collied_with_enemy(self):
        hits = pg.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            # pg.mixer.music.load(self.character.character_scream)
            # pg.mixer.music.play(-1)
            self.kill()
