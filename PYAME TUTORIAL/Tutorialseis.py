import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((700,600))
pygame.display.set_caption("Tutorial seis")
Mi_imagen= pygame.image.load("imagenes/ovni.png")
posX,posY=130,70
ventana.blit(Mi_imagen,(posX,posY))
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
