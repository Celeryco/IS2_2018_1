#probando python
import pygame

pygame.init() #iniciar pygame
#tamaño de fuentes
pequenafuente=pygame.font.SysFont("comicsansms",15)
#display size
display_width=800
display_height=600
size=display_width,display_height
#dar color a la ventana RGB ,en una tupla
white_color=(255,255,255)
black_color=(0,0,0)
red_color=(255,0,0)
blue_color=(0,0,255)
green_color=(0,255,0)
yellow_color=(255,255,0)

display=pygame.display.set_mode((display_width,display_height)) #tamaño de la ventana
pygame.display.set_caption("Hola mundo")   #titulo de la ventana
clock=pygame.time.Clock()
##
#obtener imagen del fondo
fondo=pygame.image.load('fondo.jpeg')
fondo=pygame.transform.scale(fondo,size)

####Datos de los botones
#tamaño de botones
TamBoton=[300,45]
##Boton 1
Boton1=[300,280]
ColorBoton1=[red_color,blue_color]
##Boton 2
Boton2=[300,340]
ColorBoton2=[yellow_color,green_color]
##Boton 3
Boton3=[300,400]
ColorBoton3=[black_color,blue_color]
##Boton 4
Boton4=[300,460]
ColorBoton4=[green_color,red_color]

##crear botones aleatorios
def botones(texto,superficie,estado,posicionamiento,tam,identidad=None):
    cursor= pygame.mouse.get_pos()
    click =pygame.mouse.get_pressed()


    if posicionamiento[0]+tam[0] >cursor[0] > tam[0] and posicionamiento[1] + tam[1] > cursor[1] >tam[1] and posicionamiento[1] + tam[1] < cursor [1] + tam[1]:
        if click[0]==1:
            if identidad=="start":
                pass
            elif identidad=="high_scores":
                pass
            elif identidad=="description":
                pass
            elif identidad=="exit":
                quit()
        boton= pygame.draw.rect(superficie,estado[1],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
    else:
        boton= pygame.draw.rect(superficie,estado[0],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
    textBoton(texto,black_color,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
    return boton
##crear el mensaje dentro de los botones
def textBoton(msg,color,BotonX,BotonY,Ancho,Alto,tamano="pequeno"):
    textoSuperficie,textoRect=objetotexto(msg,color,tamano)
    textoRect.center=(BotonX+(Ancho/2),BotonY+(Alto/2))
    display.blit(textoSuperficie,textoRect)

def objetotexto(texto,color,tamano):
    if tamano=="pequeno":
        textoSuperficie=pequenafuente.render(texto,True,color)
    return textoSuperficie,textoSuperficie.get_rect()


crashed=False
#para mostrar la ventana
while not crashed:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True #cierra el ciclo

    display.fill(black_color)#color de fondo
    ##
    display.blit(fondo,(0,0))


    botones("Start",display,ColorBoton1,Boton1,TamBoton,identidad="start")
    botones("High Scores",display,ColorBoton2,Boton2,TamBoton,identidad="high_scores")
    botones("Description",display,ColorBoton3,Boton3,TamBoton,identidad="description")
    botones("Exit",display,ColorBoton4,Boton4,TamBoton,identidad="exit")

    pygame.display.update()

    clock.tick(60) #frames

pygame.quit()
quit()
