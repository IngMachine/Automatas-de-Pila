# crear una ventana y finalizar cuando la cerremos
import pygame,sys
from pygame.locals import *
from Clases import Nave
from Clases import Invasor as Enemigo
#variables globales
ancho=900
alto=480
listaEnemigo = []

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
        enemigo.conquista=True

def cargarEnemigos():
    posx=100
    for x in range(1,5):
        enemigo = Enemigo(posx,100,40,"imagenes/marcianoA.jpg","imagenes/MarcianoB.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo = Enemigo(posx,0,40,"imagenes/Marciano2A.jpg","imagenes/Marciano2B.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200
    posx=100
    for x in range(1,5):
        enemigo = Enemigo(posx,-100,40,"imagenes/Marciano3A.jpg","imagenes/Marciano3B.jpg")
        listaEnemigo.append(enemigo)
        posx=posx+200

def SpaceInvader():
    pygame.init()
    ventana = pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")

    ImagenFondo=pygame.image.load("imagenes/Fondo.jpg")

    pygame.mixer.music.load("Sonidos/Intro.mp3")
    pygame.mixer.music.play(3)

    miFuenteSistema = pygame.font.SysFont("Arial",38)
    Texto = miFuenteSistema.render("Fin del juego",0,(120,100,40))

    cargarEnemigos()
    jugador = Nave.naveEspacial(ancho,alto)

    enjuego=True

    reloj = pygame.time.Clock()

    while True:
        reloj.tick(60)
        #jugador.movimiento()
        tiempo=pygame.time.get_ticks()/1000
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
            if enjuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif  evento.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif evento.key==K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)

        ventana.blit(ImagenFondo,(0,0))


        jugador.dibujar(ventana)


        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top < -10:
                    jugador.listaDisparo.remove(x)
                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)

        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamento(tiempo)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enjuego=False
                    detenerTodo()

                if (len(enemigo.listaDisparo)>0):
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()
                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enjuego=False
                            detenerTodo()

                        if x.rect.top > 900:
                            enemigo.listaDisparo.remove(x)
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)

        if enjuego==False:
            pygame.mixer.music.fadeout(3000)
            ventana.blit(Texto,(300,300))

        pygame.display.update()

SpaceInvader()
