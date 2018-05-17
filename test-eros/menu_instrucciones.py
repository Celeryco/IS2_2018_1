# Importes
import pygame
import time
import random
import constantes
# Iniciar pygame
pygame.init()

# Display size
display_width = constantes.DISPLAY_WIDTH
display_height = constantes.DISPLAY_HEIGHT

size = display_width, display_height

# Get images of powerups
powerup_bomb_pass = pygame.image.load('bomb-pass.png')
powerup_block_pass= pygame.image.load('block-pass.png')
powerup_bomb_up =   pygame.image.load('bomb-up.png')
powerup_shield =    pygame.image.load('shield.png')
powerup_fire_up =   pygame.image.load('fire-up.png')
powerup_heart =     pygame.image.load('heart.png')
powerup_kick_bomb = pygame.image.load('kick-bomb.png')
powerup_speed_up =  pygame.image.load('speed-up.png')

arrayImages = [powerup_bomb_pass, powerup_block_pass, powerup_bomb_up, powerup_shield, powerup_fire_up, powerup_heart, powerup_kick_bomb, powerup_speed_up]

# Labels
title_font = pygame.font.Font(None, 40)
title = title_font.render("Instrucciones", 0 , (0,0,0))


# Tamaño de la ventana
display = pygame.display.set_mode((display_width,display_height))

# Titulo de la ventana
pygame.display.set_caption(constantes.GAME_TITLE)

## x: 20, y: 50 - 10,  images = pygame.transfrom.scale(imagen, (ancho, altura))

def powerups_draw(position_x, position_y):
    pos_x = position_x
    pos_y = position_y

    for image in arrayImages:
        image = pygame.transform.scale(image, (100, 100))
        display.blit(powerup_image,(pos_x, pos_y))
        pos_y = pos_y - 5

def game_loop():
    #para mostrar la ventana
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(constantes.GREEN_COLOR)
        display.blit(title, (20, 150))

        powerups_draw(20,70)

        pygame.display.update()
        clock.tick(60) #frames por segundo

game_loop()
pygame.quit()
quit()
