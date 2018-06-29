import pygame

##
display_width=800
display_height=600
size=display_width,display_height

black_color=(0,0,0)
red_color=(255,0,0)
##


display=pygame.display.set_mode((display_width,display_height)) #tamaño de la ventana

clock=pygame.time.Clock()

crashed=False
#para mostrar la ventana
while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True #cierra el ciclo

    display.fill(red_color)#color de fondo

    pygame.display.update()

    clock.tick(60) #frames

pygame.quit()
quit()
