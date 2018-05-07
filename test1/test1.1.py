#probando python
import pygame
import time
import random

pygame.init() #iniciar pygame
#display size
display_width=800
display_height=600
size=display_width,display_height
#ancho del barco
ship_width=140
ship_height=83
#dar color a la ventana RGB ,en una tupla
white_color=(255,255,255)
black_color=(0,0,0)
#########################################
display=pygame.display.set_mode((display_width,display_height)) #tamaño de la ventana
pygame.display.set_caption("Prueba 1.1")   #titulo de la ventana
clock=pygame.time.Clock()
#obtener imgaen del barco
shipImg=pygame.image.load('ship.png')
#obtener imagen del fondo
fondo=pygame.image.load('fondo.jpeg')
fondo=pygame.transform.scale(fondo,size)
##
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(display,color,[thingx,thingy,thingw,thingh])

def ship(x,y):
    display.blit(shipImg,(x,y))

def text_objects(text,font):
    textSurface=font.render(text,True,black_color)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    display.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)
    #para resetear el pygame
    pygame.event.clear()
    #
    game_loop()

def crash():
    message_display("you crashed")

def game_loop():
    x=(display_width*0.4)
    y=(display_height*0.4)

    x_change=0
    y_change=0

    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_width=100
    thing_height=100

    gameExit=False
    #para mostrar la ventana
    while not gameExit:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #gameExit=True #cierra el ciclo

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change+=-5
                elif event.key==pygame.K_RIGHT:
                    x_change+=5
                elif event.key==pygame.K_UP:
                    y_change+=-5
                elif event.key==pygame.K_DOWN:
                    y_change+=5

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change+=5
                elif event.key==pygame.K_RIGHT:
                    x_change+=-5
                elif event.key==pygame.K_UP:
                    y_change+=5
                elif event.key==pygame.K_DOWN:
                    y_change+=-5

        x+=x_change
        y+=y_change

        display.fill(black_color)#color de fondo
        ##
        display.blit(fondo,(0,0))

        things(thing_startx,thing_starty,thing_width,thing_height,black_color)
        thing_starty+=thing_speed

        ship(x,y)

        if x>display_width-ship_width or x<0 or y>display_height-ship_height or y<0:
            crash()

        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)

        if y < thing_starty + thing_height:
            print("y crossover")

            if x> thing_startx and x < thing_startx + thing_width or x + ship_width> thing_startx and x + ship_width < thing_startx + ship_width:
                print("cross")
                crash()


        pygame.display.update()
        clock.tick(60) #frames por segundo

game_loop()
pygame.quit()
quit()
