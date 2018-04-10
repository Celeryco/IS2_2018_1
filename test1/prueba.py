#probando python
import pygame

pygame.init() #iniciar pygame
#display size
display_width=800
display_height=600
#dar color a la ventana RGB ,en una tupla
white_color=(255,255,255)

display=pygame.display.set_mode((display_width,display_height)) #tamaño de la ventana
pygame.display.set_caption("Hola mundo")   #titulo de la ventana
clock=pygame.time.Clock()

shipImg=pygame.image.load('ship.png')

def ship(x,y):
    display.blit(shipImg,(x,y))
x=(display_width*0.45)
y=(display_height*0.8)

crashed=False
#para mostrar la ventana
while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True #cierra el ciclo

    display.fill(white_color)
    ship(x,y)

    pygame.display.update()

    clock.tick(60) #frames

pygame.quit()
quit()
