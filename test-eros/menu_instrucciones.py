# Importes
import pygame
import time
import random
import constantes
import powerup
import enemy

# Iniciar pygame
pygame.init()
# Frame
clock = pygame.time.Clock()
# Display size
display_width = constantes.DISPLAY_WIDTH
display_height = constantes.DISPLAY_HEIGHT

size = display_width, display_height

# Powerups
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

arrayPowerups = [powerup.Powerup(powerup_bomb_pass, powerup_bomb_pass_desc), powerup.Powerup(powerup_block_pass, powerup_block_pass_desc), powerup.Powerup(powerup_bomb_up, powerup_bomb_up_desc), powerup.Powerup(powerup_shield, powerup_shield_desc), powerup.Powerup(powerup_fire_up, powerup_fire_up_desc), powerup.Powerup(powerup_heart, powerup_heart_desc), powerup.Powerup(powerup_kick_bomb, powerup_kick_bomb_desc), powerup.Powerup(powerup_speed_up, powerup_speed_up_desc)]


enemy_1 = pygame.image.load('enemy.png')
enemy_1_desc = "Espacio para enemigos"
# arrayEnemies = [enemy.Enemy(enemy_1, enemy_1_desc)]

# Labels
title_font = pygame.font.Font(None, 40)
title = title_font.render("Instrucciones", 0 , (0,0,0))

title_powerups_font = pygame.font.Font(None, 25)
title_powerups = title_powerups_font.render("Powerups", 1 , (0,0,0))

title_enemies_font = pygame.font.Font(None, 25)
title_enemies = title_enemies_font.render("Enemigos", 2 , (0,0,0))


# Tamaño de la ventana
display = pygame.display.set_mode((display_width,display_height))

# Titulo de la ventana
pygame.display.set_caption(constantes.GAME_TITLE)

## x: 20, y: 50 - 10,  images = pygame.transfrom.scale(imagen, (ancho, altura))

def powerups_draw(position_x, position_y):
    pos_x = position_x
    pos_y = position_y
    desc_font = pygame.font.Font(None, 20)

    for powerup in arrayPowerups:
        powerup.image = pygame.transform.scale(powerup.image, (40, 40))
        desc_powerup = desc_font.render(powerup.description , 0 , (0,0,0))

        display.blit(powerup.image,(pos_x, pos_y))
        display.blit(desc_powerup, (pos_x + 50, pos_y + 15))

        pos_y = pos_y + 50

def enemies_draw(position_x, position_y):
    pos_x = position_x
    pos_y = position_y
    desc_font = pygame.font.Font(None, 20)

    for x in range(0,5):
        enemy_image = pygame.transform.scale(enemy_1, (40, 40))
        enemy_desc = desc_font.render(enemy_1_desc , 0 , (0,0,0))

        display.blit(enemy_image,(pos_x, pos_y))
        display.blit(enemy_desc, (pos_x + 50, pos_y + 15))

        pos_y = pos_y + 50

def game_loop():

    gameExit = False
    #para mostrar la ventana
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(constantes.GREEN_COLOR)
        display.blit(title, (300, 30))
        display.blit(title_powerups, (170, 70))
        display.blit(title_enemies, (600, 70))

        powerups_draw(40,100)
        enemies_draw(500, 100)

        pygame.display.update()
        clock.tick(60) #frames por segundo

game_loop()
pygame.quit()
quit()
