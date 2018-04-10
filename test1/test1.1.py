#probando python
import pygame

pygame.init() #iniciar pygame
#display size
display_width=800
display_height=600
ship_width=133

#dar color a la ventana RGB ,en una tupla
white_color=(255,255,255)

display=pygame.display.set_mode((display_width,display_height)) #tamaño de la ventana
pygame.display.set_caption("Hola mundo")   #titulo de la ventana
clock=pygame.time.Clock()

shipImg=pygame.image.load('ship.png')

def ship(x,y):
    display.blit(shipImg,(x,y))

def game_loop():
    x=(display_width*0.4)
    y=(display_height*0.4)

    x_change=0
    y_change=0
    gameExit=False
    #para mostrar la ventana
    while not gameExit:
        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                gameExit=True #cierra el ciclo

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

        display.fill(white_color)
        ship(x,y)

        if x>display_width-ship_width or x<0:
            gameExit=True

        pygame.display.update()
        clock.tick(60) #frames por segundo

game_loop()
pygame.quit()
quit()
