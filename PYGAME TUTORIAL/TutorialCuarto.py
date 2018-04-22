"""Creamos una linea en la ventana con la funcion draw.line() que recibe
como parametro la ventana ,el color de la figura en este caso la linea,
el punto inicial y el punto final, hay otro parametros que ya tendria que
ver la documentacion pero por ejemplo se puede aaumentar o dismunir los
pixeles de la linea en el quinto parametro"""
import pygame,sys
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Tutorial Cuarto")
Color=pygame.Color(70,80,150)
pygame.draw.line(ventana,Color,(60,80),(160,100),8)
print Color.r
print Color.g
print Color.b
while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
