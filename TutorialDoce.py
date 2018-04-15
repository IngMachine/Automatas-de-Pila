import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Tutorial Doce")
miFuente =pygame.font.Font(None,30)
miTexto = miFuente.render("prueba fuente",0,(200,60,80),(100,70,120))

miFuenteSistema=pygame.font.SysFont("Arial",30)
miTextoSistema=miFuenteSistema.render("prueba fuente Sistema",0,(200,60,80))
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    ventana.blit(miTexto,(100,100))
    ventana.blit(miTextoSistema,(0,0))
    pygame.display.update()
