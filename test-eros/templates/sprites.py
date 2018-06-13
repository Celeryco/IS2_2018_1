import pygame as pg
from settings import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.state = 0

    def pause(self, state):
        self.state = state
        self.vx = 0
        self.vy = 0

    def get_keys(self):
        if self.state : return

        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        elif keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        elif keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y


class Bomb(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("../resources/images/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.x = round(x / TILESIZE) * TILESIZE
        self.rect.y = round(y / TILESIZE) * TILESIZE
        self.start = pg.time.get_ticks()
        self.fires = []
        self.level = 4

    def track(self):
        if pg.time.get_ticks() - self.start > 3000:
            self.exploit()

        if pg.time.get_ticks() - self.start > 4000:
            for fire in self.fires:
                fire.kill()

    def exploit(self):
        self.fires.append( Fire(self.game, self.rect.x, self.rect.y) )


        for i in range(self.level):
            self.fires.append( Fire(self.game, self.rect.x, self.rect.y - TILESIZE*i) )
            self.fires.append( Fire(self.game, self.rect.x - TILESIZE*i, self.rect.y) )
            self.fires.append( Fire(self.game, self.rect.x + TILESIZE*i, self.rect.y) )
            self.fires.append( Fire(self.game, self.rect.x, self.rect.y + TILESIZE*i) )
        self.kill()




class Fire(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load("../resources/images/fire.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
