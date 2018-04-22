import pygame
from Tkinter import *
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((903,542),0,32)
imagen = pygame.image.load("flecha.png")
fondo = pygame.image.load("impar.png")

x = 10
y = 10

reloj = pygame.time.Clock()
while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()

    if pulsada[K_w]:
        y -= 5
    if pulsada[K_s]:
        y += 5
    if pulsada[K_a]:
        x -= 5
    if pulsada[K_d]:
        x += 5
    reloj.tick(25)
    pantalla.fill((0,0,0))
    pantalla.blit(fondo,(0,0))
    pantalla.blit(imagen,(x,y))

    pygame.display.update()
