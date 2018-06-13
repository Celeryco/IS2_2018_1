import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:


    def __init__(self, player_name):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()
        self.bombs = []
        self.stopped = 0
        self.stopped_time= 0
        self.player_name = player_name

        self.play_music()

    def play_music(self):
        pg.mixer.music.load('../resources/music/battle.wav')
        pg.mixer.music.set_volume(.2)
        pg.mixer.music.play(-1)

        # self.music = pg.mixer.Sound('../resources/music/battle.wav')
        # self.music.set_volume(.2)
        # self.music.play(-1)

    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map = Map(path.join(game_folder, 'map.txt'))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        self.dt = self.clock.tick(FPS) / 200

        while self.playing:
            self.events()
            self.update()
            self.draw()


    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):

        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        if self.stopped:
            pause_text = pg.font.SysFont('Consolas', 32).render('Pause', True, pg.color.Color('White'))
            self.screen.blit(pause_text, (480, 374))
        else:
            self.track_bombs()

        button_text = pg.font.SysFont('Consolas', 32).render("Player1: " + self.player_name, True, (0, 0, 0))
        self.screen.blit(button_text, (10, 5))

        pg.display.flip()


    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

                if event.key == pg.K_z and not self.stopped:
                    bomb = Bomb(self, self.player.rect.x, self.player.rect.y)
                    self.bombs.append(bomb)

                if event.key == pg.K_p:
                    self.stopped = not self.stopped
                    self.player.pause(self.stopped)
                    if self.stopped:
                        self.stopped_time = pg.time.get_ticks()
                    else:
                        self.update_bombs_start()


    def track_bombs(self):
        for bomb in self.bombs:
            bomb.track()

    def update_bombs_start(self):
        for bomb in self.bombs:
            bomb.start = pg.time.get_ticks() - (self.stopped_time  - bomb.start)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass


class Menu:


    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE_MENU)
        self.clock = pg.time.Clock()
        self.play_music()
        self.load_buttons()


    def load_buttons(self):
        self.button_start = Button(self.screen, "START", 450, 340, 140, 50, 35, 15, 2)
        self.button_instructions = Button(self.screen, "INSTRUCTIONS", 425, 420, 190, 50, 10, 15, 2)
        self.button_high_score = Button(self.screen, "HIGH SCORE", 440, 500, 160, 50, 10, 15, 2)
        self.button_quit = Button(self.screen, "QUIT", 450, 580, 140, 50, 45, 15, 2)
        self.input = Input(self.screen, "", 425, 250, 190, 50, 20, 15, 2, 11)

    def play_music(self):
        pg.mixer.music.load('../resources/music/menu.wav')
        pg.mixer.music.set_volume(.2)
        pg.mixer.music.play(-1)

    def run(self):
        self.draw()
        self.events()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()


            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.input.delete()
                else:
                    self.input.add(event.unicode)

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_position = pg.mouse.get_pos()
                self.button_start.click(mouse_position, self.start)
                self.button_instructions.click(mouse_position, self.instructions)
                self.button_high_score.click(mouse_position, self.high_score)
                self.button_quit.click(mouse_position, self.quit)


    def draw(self):
        self.screen.fill(BGCOLOR)

        #Draw Button
        self.button_start.draw()
        self.button_instructions.draw()
        self.button_high_score.draw()
        self.button_quit.draw()
        self.input.draw()


        pg.display.flip()


    def start(self):
        player_name = self.input.text
        g = Game(player_name)
        g.new()
        g.run()

    def quit(self):
        pg.quit()
        sys.exit()

    def high_score(self):
        pass

    def instructions(self):
        pass


class Button():

    def __init__(self, screen, text, x, y, width, height, padding_x, padding_y, border):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.border = border

    def draw(self):
        self.rect = pg.draw.rect(self.screen, (247, 177, 33),(self.x, self.y, self.width, self.height), self.border)
        self.button_text = pg.font.SysFont('Consolas', 32).render(self.text, True, (247, 177, 33))
        self.screen.blit(self.button_text, (self.x + self.padding_x, self.y + self.padding_y))

    def click(self, mouse_position, function):
        if self.rect.collidepoint(mouse_position):
            function()


class Input():

    def __init__(self, screen, text, x, y, width, height, padding_x, padding_y, border, limit):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.border = border
        self.limit = limit

    def draw(self):
        self.rect = pg.draw.rect(self.screen, (247, 177, 33),(self.x, self.y, self.width, self.height), self.border)
        self.button_text = pg.font.SysFont('Consolas', 32).render(self.text, True, (247, 177, 33))
        self.screen.blit(self.button_text, (self.x + self.padding_x, self.y + self.padding_y))


    def add(self, character):
        if len(self.text) <= self.limit:
            self.text = self.text + character


    def delete(self):
        self.text = self.text[:-1]


# create the game object
# g = Game()
# g.new()

pg.init()
m = Menu()

while True:
    m.run()


    # g.run()
    # g.show_go_screen()
