import sys,pygame
from pygame.locals import *
pygame.init()
ventana=pygame.display.set_mode((1181,709))
fondo=pygame.image.load("imagenes de automata impar/impar.png")
pygame.display.set_caption("Palindromo Impar _ Automata de Pila")
while True:
    ventana.blit(fondo,(0,0))
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
