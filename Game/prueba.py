from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *


ABOUT = ['PygameMenu : menu',
         'Author: Angelo',
         PYGAMEMENU_TEXT_NEWLINE,
         'Codigo: 20140266']
COLOR_BACKGROUND = (0, 0,0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW=(182,198,60)
FPS = 60.0
MENU_BACKGROUND_COLOR = (255,0,0)
WINDOW_SIZE = (640, 480)

##imagen de fondo
fondo=pygame.image.load('fondo.jpeg')
fondo=pygame.transform.scale(fondo,WINDOW_SIZE)
#

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Bomberman Peruvian Deluxe')
clock = pygame.time.Clock()
dt = 1 / FPS


# Global variables

####DIFFICULTY = ['EASY']


# -----------------------------------------------------------------------------
"""
def change_difficulty(d):

    Change difficulty of the game.

    :return:

    print ('Selected difficulty: {0}'.format(d))
    DIFFICULTY[0] = d
"""
"""
def random_color():

    Return random color.

    :return: Color tuple

    return randrange(0, 255), randrange(0, 255), randrange(0, 255)
"""
"""
def play_function(difficulty, font):

    Main game function

    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None

    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    if difficulty == 'EASY':
        f = font.render('Playing as baby', 1, COLOR_WHITE)
    elif difficulty == 'MEDIUM':
        f = font.render('Playing as normie', 1, COLOR_WHITE)
    elif difficulty == 'HARD':
        f = font.render('Playing as god', 1, COLOR_WHITE)
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    bg_color = random_color()
    f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    if main_menu.is_disabled():
                        main_menu.enable()

                        # Quit this function, then skip to loop of main-menu on line 197
                        return

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        surface.fill(bg_color)
        surface.blit(f, ((WINDOW_SIZE[0] - f_width) / 2, WINDOW_SIZE[1] / 2))
        pygame.display.flip()

"""

def main_background():
    """
    Function used by menus, draw on background while menu is active.

    :return: None
    """
    surface.fill(COLOR_BACKGROUND)
    surface.blit(fondo,(0,0))


# -----------------------------------------------------------------------------
# PLAY MENU
play_menu = pygameMenu.Menu(surface,
                            bgfun=main_background,
                            color_selected=COLOR_WHITE,
                            font=pygameMenu.fonts.FONT_8BIT,
                            font_color=COLOR_BLACK,
                            font_size=30,
                            menu_alpha=10,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(WINDOW_SIZE[1]),
                            menu_width=int(WINDOW_SIZE[0] ),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Play menu',
                            window_height=WINDOW_SIZE[1],
                            window_width=WINDOW_SIZE[0]
                            )


# When pressing return -> play(DIFFICULTY[0], font)
"""
play_menu.add_option('Start', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))

play_menu.add_selector('Select difficulty', [('Easy', 'EASY'),
                                             ('Medium', 'MEDIUM'),
                                             ('Hard', 'HARD')],
                       onreturn=None,
                       onchange=change_difficulty)
"""
play_menu.add_option('Return to main menu', PYGAME_MENU_BACK)
#HIGH SCORE MENU
high_score_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_alpha=10,
                                 #menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1]),
                                 menu_width=int(WINDOW_SIZE[0] ),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='High Scores',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )

high_score_menu.add_option('Return to menu', PYGAME_MENU_BACK)


# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 bgfun=main_background,
                                 color_selected=COLOR_WHITE,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=COLOR_BLACK,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_alpha=10,
                                 #menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=COLOR_WHITE,
                                 menu_height=int(WINDOW_SIZE[1]),
                                 menu_width=int(WINDOW_SIZE[0] ),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=COLOR_BLACK,
                                 text_fontsize=20,
                                 title='About',
                                 window_height=WINDOW_SIZE[1],
                                 window_width=WINDOW_SIZE[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
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

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()
