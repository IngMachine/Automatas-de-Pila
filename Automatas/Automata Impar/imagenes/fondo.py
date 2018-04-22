#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
from Tkinter import *
from pygame.locals import *


# Clases
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# Funciones


# ---------------------------------------------------------------------


def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

# ---------------------------------------------------------------------

def palabraA(xa,ya,screen):
    a= pygame.image.load("a.png")
    screen.blit(a,(xa,ya))

def palabraB(xb,yb):
    b= pygame.image.load("b.png")
    screen.blit(b,(xb,yb))

def main(cadena):
    # Constantes
    listaPila=[]
    listaPila.append("a")
    listaPila.append("ab")
    listaPila.append("abb")
    listaPila.append("abba")
    listaPila.append("abb")
    listaPila.append("ab")
    listaPila.append("a")
    listaPila.append("TRUE")



    listaEstado=[]

    listaEstado.append("a")
    listaEstado.append("b")
    listaEstado.append("c")
    listaEstado.append("d")
    listaEstado.append("TRUE")


    WIDTH = 903
    HEIGHT = 542



    reloj = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("<-- PALINDROMO PAR --")

    background_image = load_image('/home/ricaardo/Documentos/COMPILADORES/PYGAM/impar.png')

    #imagenes
    errorTrue = pygame.image.load("ERRROR_TRUE.png")
    errorFalse = pygame.image.load("ERRROR_FALSE.png")
    flecha = pygame.image.load("flecha.png")
    apilar = pygame.image.load("APILAR.png")
    desapilar = pygame.image.load("DESAPILAR.png")
    fuente = pygame.font.Font(None, 26)
    texto1 = fuente.render(cadena, 0, (9,104, 146))
    fuentea = pygame.font.Font(None, 60)



#coordenadas de imagenes

    #flecha
    xFlecha = 293
    yFlecha = 233


    #apilar1
    xapi=1000
    yapi=1000

    #desapilar
    xdesa=1000
    ydesa=1000
    i=0

    #errorTrue
    xTrue=1000
    yTrue=1000

    #errorFalse
    xFalse=1000
    yFalse=1000


    while True and i < 5:

        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        pulsada = pygame.key.get_pressed()
        #reubica ala imagen apilar y desapilar
        xapi=1000
        yapi=1000

        xdesa=1000
        ydesa=1000

        if listaEstado[i] == "a":    #1 b,b/bb -> apila b
            xFlecha=154
            yFlecha=107


        if listaEstado[i] == "b":    #2 a,b/ba ->apila a
            xFlecha=154
            yFlecha=137

        if listaEstado[i] == "c":    #3 b,a/ab ->apila b
            xFlecha=154
            yFlecha=174
        if listaEstado[i] == "d":    #4 a,a/aa ->apila a
            xFlecha=154
            yFlecha=211
        if listaEstado[i] == "TRUE":    #4 a,a/aa ->apila a
            xTrue=183
            yTrue=129
        if listaEstado[i] == "FALSE":    #4 a,a/aa ->apila a
            xTrue=183
            yTrue=129


        reloj.tick(0.5)
        screen.fill((0,0,0))
        screen.blit(background_image, (0, 0))
        screen.blit(flecha,(xFlecha,yFlecha))

        a = fuentea.render(listaPila[i], 0, (0,0,0))
        screen.blit(a, (348,160))

        screen.blit(apilar,(xapi,yapi))
        screen.blit(desapilar,(xdesa,ydesa))
        screen.blit(texto1, (654,427))

        screen.blit(errorTrue, (xTrue,yTrue))
        screen.blit(errorFalse, (xFalse,yFalse))

        pygame.display.update()



        pygame.display.flip()
        i=i+1
    return 0

if __name__ == '__main__':
    #cadena=input("->  ingrese la palabra : ")
    #print(cadena)
    #print(len(cadena))

#tekiter Ingresar Texto
    def mostrar():
        mostrarPalabra=Label(text=entrada.get(), font=("FreeMono",14)).place(x=179,y=388)
        cadena=entrada.get()
        pygame.init()
        main(cadena)


    ventana=Tk()
    ventana.geometry("433x433+0+0")
    imagen=PhotoImage(file="fondo_Tkinter.png")
    MostrarImagen=Label(ventana,image=imagen).place(x=0,y=0)
    #ventana.config(bg="blue")
    ventana.title("Campos de Texto")
    #lblUsuario=Label(text="Ingresar Palabra ", font=("FreeMono",14)).place(x=119,y=117)
    #creand un campo de texto

    entrada=StringVar()
    entrada.set("  ejemplo:  'abcba' ")
    palabraCadena=Entry(ventana,textvariable=entrada,width=30).place(x=94,y=170)

    #crear dos botones (ingresa palabra)
    btnIngresar=Button(ventana,text="INGRESAR",command = mostrar,font=("FreeMono",14),width=15).place(x=125,y=217)



    ventana.mainloop()

    #fin de tkiter
