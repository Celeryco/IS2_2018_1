"""
This module initializes the display and creates dictionaries of resources.
"""
import os
import pygame as pg
from . import tools

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 800   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 608 # 16 * 48 or 32 * 24 or 64 * 12
SCREEN_SIZE = (WIDTH, HEIGHT)
FPS = 60
TITLE = "Peruvian Heart Deluxe Edition"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# Player settings
PLAYER_SPEED = 200

#Initialization
pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(TITLE)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN.fill(BGCOLOR)
SCREEN_RECT = SCREEN.get_rect()

#Resource loading (Fonts and music just contain path names).
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
GFX   = tools.load_all_gfx(os.path.join("resources", "graphics"))
# SFX   = tools.load_all_sfx(os.path.join("resources", "sounds"))
# MOV   = tools.load_all_movies(os.path.join("resources", "movies"))
