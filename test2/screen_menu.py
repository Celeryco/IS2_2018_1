from pygame.locals import *
from random import randrange
import os

import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

##
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW=(182,198,60)
FPS = 60.0
WINDOW_SIZE = (640, 480)

##imagen de fondo
FONDO=pygame.image.load('fondo.jpeg')
FONDO=pygame.transform.scale(FONDO,WINDOW_SIZE)
#

class ScreenMenu:
    def __init__(self,manager):
        self.manager=manager

    def get_input(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    def update(self):
        pass

    def render(self):
        main_menu = pygameMenu.Menu(surface,
                                    bgfun=main_background,
                                    color_selected=COLOR_WHITE,
                                    font=pygameMenu.fonts.FONT_BEBAS,
                                    font_color=COLOR_YELLOW,
                                    font_size=30,
                                    menu_alpha=10,
                                    #menu_color=MENU_BACKGROUND_COLOR,
                                    menu_height=int(WINDOW_SIZE[1]),
                                    menu_width=int(WINDOW_SIZE[0] ),
                                    onclose=PYGAME_MENU_DISABLE_CLOSE,
                                    option_shadow=False,
                                    title='Menu Principal',
                                    window_height=WINDOW_SIZE[1],
                                    window_width=WINDOW_SIZE[0]
                                    )
        main_menu.add_option('Start', play_menu)
        main_menu.add_option('High Scores',high_score_menu)
        main_menu.add_option('Description', about_menu)
        main_menu.add_option('Exit', PYGAME_MENU_EXIT)


    def mostrar_tablero(self):
        pass
