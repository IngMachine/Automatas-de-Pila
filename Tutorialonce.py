import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((600,300))
pygame.display.set_caption("Tutorial Ocho")
rectangulo_dos = pygame.Rect(200,200,100,50)
posX,posY=200,100
velocidad=0.5
i=0
blanco=(255,255,255)
derecha=True
rectangulo = pygame.Rect(0,0,100,50)
while True:
    i=i+1
    ventana.fill(blanco)
    pygame.draw.rect(ventana,(180,70,70),rectangulo_dos)
    pygame.draw.rect(ventana,(180,70,70),rectangulo)
    rectangulo.left, rectangulo.top = pygame.mouse.get_pos()
    if rectangulo.colliderect(rectangulo_dos):
        velocidad=0
        print "colisiono",i
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    if derecha==True:
        if posX<400:
            posX+=velocidad
            rectangulo_dos.left = posX
        else:
            derecha=False
    else:
        if posX>1:
            posX-=velocidad
            rectangulo_dos.left=posX
        else:
            derecha=True
    pygame.display.update()
