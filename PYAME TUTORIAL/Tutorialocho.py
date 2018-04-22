import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Tutorial Ocho")
Mi_imagen= pygame.image.load("imagenes/ovni.png")
posX,posY=200,100
velocidad=0.5
blanco=(255,255,255)
derecha=True
while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type==pygame.keydown:
            if evento.key=K_LEFT:
                posX-=velocidad
            elif evento.key=K_RIGHT:
                posY+=velocidad
    if derecha==True:
        if posX<400:
            posX+=velocidad
        else:
            derecha=False
    else:
        if posX>1:
            posX-=velocidad
        else:
            derecha=True
    pygame.display.update()
