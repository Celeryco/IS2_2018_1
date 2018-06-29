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
display_width=800
display_height=600
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

pequenafuente=pygame.font.Font(None,25)
red_color=(255,0,0)
blue_color=(0,0,255)
black_color=(0,0,0)
##datos de boton
TamBoton=[200,45]
#boton1
PosicionBoton1=[200,360]
ColorBoton1=[red_color,blue_color]
#boton2
PosicionBoton2=[200,420]
ColorBoton2=[red_color,blue_color]

def textBoton(msg,color,BotonX,BotonY,Ancho,Alto,tamano="pequeno"):
    textoSuperficie,textoRect=objetotexto(msg,color,tamano)
    textoRect.center=(BotonX+(Ancho/2),BotonY+(Alto/2))
    surface.blit(textoSuperficie,textoRect)

def objetotexto(texto,color,tamano):
    if tamano=="pequeno":
        textoSuperficie=pequenafuente.render(texto,True,color)
    return textoSuperficie,textoSuperficie.get_rect()

def botones(texto,superficie,estado,posicionamiento,tam,identidad=None):
    cursor= pygame.mouse.get_pos()
    click =pygame.mouse.get_pressed()


    if posicionamiento[0]+tam[0] >cursor[0] > tam[0] and posicionamiento[1] + tam[1] > cursor[1] >tam[1] and posicionamiento[1] + tam[1] < cursor [1] + tam[1]:
        if click[0]==1:
            if identidad=="instrucciones":
                instructions()
            elif identidad=="backMenu":
                if main_menu.is_disabled():
                    main_menu.enable()

        boton= pygame.draw.rect(superficie,estado[1],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
    else:
        boton= pygame.draw.rect(superficie,estado[0],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
    textBoton(texto,black_color,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
    return boton

##empieza
def description():

    bg_color = COLOR_WHITE
    ##

    mifuente=pygame.font.Font(None,50)
    miTexto=mifuente.render("DESCRIPCIÓN",0,(0,0,0))

    fuentePlayer=pygame.font.Font(None,30)
    textoPlayer1=fuentePlayer.render("Jugador 1",1,(0,0,0))
    textoPlayer2=fuentePlayer.render("Jugador 2",2,(0,0,0))

    control1Img=pygame.image.load('wasd.png')
    control1Img=pygame.transform.scale(control1Img,(220,170))

    control2Img=pygame.image.load('flechas.jpg')
    control2Img=pygame.transform.scale(control2Img,(220,170))


    main_menu.disable()
    main_menu.reset(1)

    #################################################################


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
        #pygame.draw.rect(surface,red_color,(50,400,150,45))
        botones("Instrucciones",surface,ColorBoton1,PosicionBoton1,TamBoton,identidad="instrucciones")

        botones("Regresar al Menu",surface,ColorBoton2,PosicionBoton2,TamBoton,identidad="backMenu")

        surface.blit(miTexto,(display_height*0.38,display_width*0.07))
        surface.blit(textoPlayer1,(20,150))
        surface.blit(textoPlayer2,(360,150))
        surface.blit(control1Img,(20,180))
        surface.blit(control2Img,(360,180))
        pygame.display.flip()

##clases
class Powerup():
    def __init__(self, image, description):
        self.image = image
        self.description = description

class Enemy():
    def __init__(self, image, description):
        self.image = image
        self.description = description

##
powerup_bomb_pass = pygame.image.load('bomb-pass.png')
powerup_block_pass= pygame.image.load('block-pass.png')
powerup_bomb_up =   pygame.image.load('bomb-up.png')
powerup_shield =    pygame.image.load('shield.png')
powerup_fire_up =   pygame.image.load('fire-up.png')
powerup_heart =     pygame.image.load('heart.png')
powerup_kick_bomb = pygame.image.load('kick-bomb.png')
powerup_speed_up =  pygame.image.load('speed-up.png')

powerup_bomb_pass_desc = "Te permite caminar a traves de las bombas."
powerup_block_pass_desc = "Te permite caminar a traves de las bombas."
powerup_bomb_up_desc = "Te permite colocar una bomba mas en el mapa."
powerup_shield_desc = "Te permite poder resistir el impacto de una bomba una vez."
powerup_fire_up_desc = "Incrementa el rango de alcance de tus bombas."
powerup_heart_desc = "Te devuelve una vida."
powerup_kick_bomb_desc = "Te permite poder patear bombas fuera de tu camino."
powerup_speed_up_desc = "Te hace más rapido"

arrayPowerups = [Powerup(powerup_bomb_pass, powerup_bomb_pass_desc), Powerup(powerup_block_pass, powerup_block_pass_desc), Powerup(powerup_bomb_up, powerup_bomb_up_desc), Powerup(powerup_shield, powerup_shield_desc),Powerup(powerup_fire_up, powerup_fire_up_desc), Powerup(powerup_heart, powerup_heart_desc),Powerup(powerup_kick_bomb, powerup_kick_bomb_desc),Powerup(powerup_speed_up, powerup_speed_up_desc)]


enemy_1 = pygame.image.load('enemy.png')
enemy_1_desc = "Espacio para enemigos"
# arrayEnemies = [enemy.Enemy(enemy_1, enemy_1_desc)]

# Labels
title_font = pygame.font.Font(None, 40)
title = title_font.render("Instrucciones", 0 , (0,0,0))

title_powerups_font = pygame.font.Font(None, 15)
title_powerups = title_powerups_font.render("Powerups", 1 , (0,0,0))

title_enemies_font = pygame.font.Font(None, 15)
title_enemies = title_enemies_font.render("Enemigos", 2 , (0,0,0))
##funciiones de eros
def powerups_draw(position_x, position_y):
    pos_x = position_x
    pos_y = position_y
    desc_font = pygame.font.Font(None, 15)

    for powerup in arrayPowerups:

        powerup.image = pygame.transform.scale(powerup.image, (20, 40))
        desc_powerup = desc_font.render(powerup.description , 0 , (0,0,0))

        surface.blit(powerup.image,(pos_x, pos_y))
        surface.blit(desc_powerup, (pos_x + 33, pos_y + 15))

        pos_y = pos_y + 33

def enemies_draw(position_x, position_y):
    pos_x = position_x
    pos_y = position_y
    desc_font = pygame.font.Font(None, 20)

    for x in range(0,5):
        enemy_image = pygame.transform.scale(enemy_1, (20, 40))
        enemy_desc = desc_font.render(enemy_1_desc , 0 , (0,0,0))

        surface.blit(enemy_image,(pos_x, pos_y))
        surface.blit(enemy_desc, (pos_x + 32, pos_y + 15))

        pos_y = pos_y + 32


##
def instructions():

    main_menu.disable()
    main_menu.reset(1)

    pygame.mixer.music.load("bensound-extremeaction.mp3")
    pygame.mixer.music.play()

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
        surface.fill(red_color)
        surface.blit(title, (100, 30))
        surface.blit(title_powerups, (170, 70))
        surface.blit(title_enemies, (400, 70))

        powerups_draw(40,100)
        enemies_draw(400, 100)

        pygame.display.flip()


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
"""
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
"""
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
main_menu.add_option('Description', description)
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
