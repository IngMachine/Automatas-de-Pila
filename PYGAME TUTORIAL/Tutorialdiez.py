import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Tutorial Ocho")
Mi_imagen= pygame.image.load("imagenes/ovni.png")
posX,posY=200,100
velocidad=5
blanco=(255,255,255)
derecha=True
while True:
    ventana.fill(blanco)
    ventana.blit(Mi_imagen,(posX,posY))
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type==pygame.KEYDOWN:
            if evento.key==K_LEFT:
                posX-=velocidad
            elif evento.key==K_RIGHT:
                posX+=velocidad
        elif evento.type==pygame.KEYUP:
            if evento.key==K_LEFT:
                print "tecla Izquierda Liberada"
            elif evento.key==K_RIGHT:
                print "tecla Derecha Liberada"
    posX,posY = pygame.mouse.get_pos()
    posX=posX-70
    posY=posY-60
    pygame.display.update()
