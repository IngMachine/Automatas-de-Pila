import pygame
from pygame.locals import *

pygame.init()

pantalla = pygame.display.set_mode((450,300),0,32)
pygame.display.set_caption("Modulo de fuentes")

reloj = pygame.time.Clock()

fuente = pygame.font.Font(None, 30)
texto1 = fuente.render("<- RICARDO PELAEZ ->", 0, (0, 0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    reloj.tick(20)
    pantalla.blit(texto1, (100,100))
    pygame.display.update()
