import pygame as pg
import sys
import random
from os import path
from ..import settings, tools
from ..models import player, character, bomb, map, wall, powerup, enemy
from ..views import character_view, bomb_view, fire_view, map_view, wall_view, powerup_view, enemy_view


class Game(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.dt = 0
        self.next = None
        self.bgm = settings.MUSIC["battle"]
        self.font = pg.font.Font(settings.FONTS["Fixedsys500c"], 50)
        self.blink = False
        self.timer = 0.0
        self.bombs = []
        self.stopped = 0
        self.stopped_time = 0
        self.player = player.Player("Quintana")
        self.load_data()
        self.new()

    # def play_music(self):
    #     pg.mixer.music.load('../resources/music/battle.wav')
    #     pg.mixer.music.set_volume(.2)
    #     pg.mixer.music.play(-1)

    def startup(self, current_time, persistant):
        self.load_data()
        pg.mixer.music.load(self.bgm)
        pg.mixer.music.play(-1)
        return tools._State.startup(self, current_time, persistant)

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = map_view.MapView(path.join(game_folder, 'map.txt'))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    breakable = bool(random.getrandbits(1))
                    wall_model = wall.Wall(breakable)
                    wall_view.WallView(wall_model, self, col, row)
                if tile == 'P':
                    self.character = character.Character(settings.GFX['quintana'])
                    self.character_view = character_view.CharacterView(self.character, self, col, row)
                if tile == 'F':
                    powerup_model = powerup.Powerup(settings.GFX['fire-up'], "fire", 1)
                    powerup_view.PowerupView(powerup_model, self, col, row)
                if tile == 'S':
                    powerup_model = powerup.Powerup(settings.GFX['speed-up'], "speed", 10)
                    powerup_view.PowerupView(powerup_model, self, col, row)
                if tile == 'E':
                    self.enemy = enemy.Enemy(settings.GFX['inca'])
                    self.enemy_v = enemy_view.EnemyView(self.enemy, self, col, row)


    def get_event(self, event):
        # catch all events here
        if event.type == pg.QUIT:
            self.state.done = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z and not self.stopped:
                # View
                bomb_model = bomb.Bomb(settings.GFX['bomb'], self.character.fire_lvl)
                new_bomb = bomb_view.BombView(bomb_model, self, self.character_view.rect.x, self.character_view.rect.y)
                self.bombs.append(new_bomb)

            if event.key == pg.K_p:
                self.stopped = not self.stopped
                self.player.pause(self.stopped)
                if self.stopped:
                    self.stopped_time = pg.time.get_ticks()
                else:
                    self.update_bombs_start()

    def update(self, surface, keys, current_time, dt):
        self.dt = dt
        self.all_sprites.update()
        self.draw(surface)

    def draw(self, surface):
        surface.fill(settings.BGCOLOR)
        self.draw_grid(surface)
        self.all_sprites.draw(surface)
        if self.stopped:
            pause_text = pg.font.SysFont('Consolas', 32).render('Pause', True, pg.color.Color('White'))
            surface.blit(pause_text, (480, 374))
        else:
            self.track_bombs()

        button_text = pg.font.SysFont('Consolas', 32).render("Player1: " + self.player.name, True, (0, 0, 0))
        surface.blit(button_text, (10, 5))
        pg.display.flip()

    def draw_grid(self, surface):
        for x in range(0, settings.WIDTH, settings.TILESIZE):
            pg.draw.line(surface, settings.LIGHTGREY, (x, 0), (x, settings.HEIGHT))
        for y in range(0, settings.HEIGHT, settings.TILESIZE):
            pg.draw.line(surface, settings.LIGHTGREY, (0, y), (settings.WIDTH, y))

    def track_bombs(self):
        for bomb in self.bombs:
            bomb.track()

    def update_bombs_start(self):
        for bomb in self.bombs:
            bomb.start = pg.time.get_ticks() - (self.stopped_time  - bomb.start)
