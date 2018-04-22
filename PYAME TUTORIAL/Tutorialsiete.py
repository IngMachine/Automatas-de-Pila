import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption("Tutorial seis")
Mi_imagen= pygame.image.load("imagenes/ovni.png")
posX,posY=randint(10,400),randint(10,300)
ventana.blit(Mi_imagen,(posX,posY))
print posX
print posY
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
