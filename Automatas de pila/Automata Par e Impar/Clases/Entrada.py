#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
from subprocess import check_output
import sys, pygame
from pygame.locals import *
import Automata
import EstadoPar
import EstadoImpar
import Lista

class Obtener():
    def __init__(self,cadena,error):
        self.cadena=cadena
        self.error=error
        self.estadoPila=[]
        self.estados=[]



    def validacion(self):
          if len(self.cadena)%2==0:
              print("Es par")
              speak=check_output(['espeak',' apila'])
              p=Automata.Pila()
              p.apilar("#")
              guardar=Lista.Listas()
              guardar.addPila("#")
              print("la pila",p.mostrar())
              aux=EstadoPar.EstadosPar(self.cadena,p,self.error,guardar)
              aux.estado1(p)
              print(aux.retorno())
              if(aux.retorno()):
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("#")
                  print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  self.estados.append("True")
                  print(self.estados)
                  print("-> Palabra Acepatada PALINDROMO!!!")
                  print("la pila",p.mostrar())
              else:
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("#")
                  print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  self.estados.append("False")
                  print(self.estados)
                  print ("-> Palabra no Aceptada, NOOOOO es PALINDROMO!!!!")

              #inicio del pygame

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



              def main(cadena,devolverEstados,devolverPila):
                  # Constantes
                  listaPila=devolverPila
                  listaEstado=devolverEstados



                  WIDTH = 903
                  HEIGHT = 542



                  reloj = pygame.time.Clock()
                  screen = pygame.display.set_mode((WIDTH, HEIGHT))
                  pygame.display.set_caption("<-- PALINDROMO PAR --")

                  background_image = load_image("img/Par.png")

                  #imagenes
                  errorTrue = pygame.image.load("img/ERRROR_TRUE.png")
                  errorFalse = pygame.image.load("img/ERRROR_FALSE.png")
                  flecha = pygame.image.load("img/flecha.png")
                  apilar = pygame.image.load("img/APILAR.png")
                  desapilar = pygame.image.load("img/DESAPILAR.png")
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


                  while True and i < len(listaPila):

                      for eventos in pygame.event.get():
                          if eventos.type == QUIT:
                              sys.exit(0)

                      pulsada = pygame.key.get_pressed()
                      #reubica ala imagen apilar y desapilar
                      xapi=1000
                      yapi=1000

                      xdesa=1000
                      ydesa=1000

                      if listaEstado[i] == "f":    #1 b,b/bb -> desaapila b apila bb
                          xFlecha=154
                          yFlecha=107
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72


                      if listaEstado[i] == "e":    #2 a,b/ba -> desaapila b apila ba
                          xFlecha=154
                          yFlecha=137
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "d":    #3 b,a/ab ->desaapila a apila ab
                          xFlecha=154
                          yFlecha=174
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72
                      if listaEstado[i] == "c":    #4 a,a/aa ->desapila a y apila aa
                          xFlecha=154
                          yFlecha=211
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "b":    #5 b,#/#b ->apila b
                          xFlecha=154
                          yFlecha=248
                          #apila
                          xapi=574
                          yapi=72
                      if listaEstado[i] == "a":    #6 a,#/#a ->apila a
                          xFlecha=154
                          yFlecha=280
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "g":    #7 b,b/landa desapila b
                          xFlecha=298
                          yFlecha=362
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "h":    #8  a,a/landa desapila a
                          xFlecha=303
                          yFlecha=424
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "i":   #9 b,b/landa desapila b
                          xFlecha=576
                          yFlecha=283
                          #desapi
                          xdesa=724
                          ydesa=276


                      if listaEstado[i] == "j":   #10 a,a/landa desapila a
                          xFlecha=576
                          yFlecha=326
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "True":     #11 landa/#/# final del
                          xFlecha=571
                          yFlecha=320
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "True":    #4
                          yTrue=129
                          xTrue=183
                      if listaEstado[i] == "False":    #4
                          xFalse=183
                          yFalse=129


                      reloj.tick(0.5)
                      screen.fill((0,0,0))
                      screen.blit(background_image, (0, 0))
                      screen.blit(flecha,(xFlecha,yFlecha))

                      a = fuentea.render(listaPila[i], 0, (0,0,0))
                      screen.blit(a, (348,160))

                      screen.blit(apilar,(xapi,yapi))
                      screen.blit(apilar,(1000,1000))
                      #reloj.tick(0.1)
                      screen.blit(desapilar,(xdesa,ydesa))
                      screen.blit(desapilar,(1000,1000))
                      screen.blit(texto1, (654,427))

                      screen.blit(errorTrue, (xTrue,yTrue))
                      screen.blit(errorFalse, (xFalse,yFalse))

                      pygame.display.update()



                      pygame.display.flip()
                      i=i+1
                  return 0
              pygame.init()
              main(self.cadena,aux.devolverEstados(),aux.devolverPila())
              # FIN DE PYGMAE
          if len(self.cadena)%2!=0:
              #print (' Esta palabra es impar y no es aceptada' )
              p=Automata.Pila()
              p.apilar("#")
              guardar=Lista.Listas()
              guardar.addPila("#")
              #print("pila grajdklm",guardar.mostrarPila())
              print("la pila",p.mostrar())

              aux=EstadoImpar.EstadosImpar(self.cadena,p,self.error,guardar)
              aux.estado1(p)
              print(aux.retorno())
              if aux.retorno():
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("#")
                  #self.estadoPila.append("True")
                  print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  self.estados.append("True")
                  #self.estados.append(" ")
                  print(self.estados)
                  print("-> Palabra Acepatada PALINDROMO!!!")
                  print(p.mostrar())



              else:
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("#")

                  print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  self.estados.append("False")

                  print(self.estados)
                  print ("-> Palabra no Aceptada, NOOOOO es PALINDROMO!!!!")

              # iniciamos el PYGAME
              print("NOJODAAAAAAAAAAAA",aux.devolverEstados())
              print("Diossssssss",aux.devolverPila())



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



              def main(cadena,devolverEstados,devolverPila):
                  # Constantes
                  listaPila=devolverPila
                  listaEstado=devolverEstados



                  WIDTH = 903
                  HEIGHT = 542



                  reloj = pygame.time.Clock()
                  screen = pygame.display.set_mode((WIDTH, HEIGHT))
                  pygame.display.set_caption("<-- PALINDROMO IMPAR --")

                  background_image = load_image("img/impar.png")

                  #imagenes
                  errorTrue = pygame.image.load("img/ERRROR_TRUE.png")
                  errorFalse = pygame.image.load("img/ERRROR_FALSE.png")
                  flecha = pygame.image.load("img/flecha.png")
                  apilar = pygame.image.load("img/APILAR.png")
                  desapilar = pygame.image.load("img/DESAPILAR.png")
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


                  while True and i < len(listaPila):

                      for eventos in pygame.event.get():
                          if eventos.type == QUIT:
                              sys.exit(0)

                      pulsada = pygame.key.get_pressed()
                      #reubica ala imagen apilar y desapilar
                      xapi=1000
                      yapi=1000

                      xdesa=1000
                      ydesa=1000

                      if listaEstado[i] == "f":    #1 b,b/bb -> desaapila b apila bb
                          xFlecha=154
                          yFlecha=107
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72


                      if listaEstado[i] == "e":    #2 a,b/ba -> desaapila b apila ba
                          xFlecha=154
                          yFlecha=137
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "d":    #3 b,a/ab ->desaapila a apila ab
                          xFlecha=154
                          yFlecha=174
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72
                      if listaEstado[i] == "c":    #4 a,a/aa ->desapila a y apila aa
                          xFlecha=154
                          yFlecha=211
                          #desapi
                          xdesa=724
                          ydesa=276
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "b":    #5 b,#/#b ->apila b
                          xFlecha=154
                          yFlecha=248
                          #apila
                          xapi=574
                          yapi=72
                      if listaEstado[i] == "a":    #6 a,#/#a ->apila a
                          xFlecha=154
                          yFlecha=280
                          #apila
                          xapi=574
                          yapi=72

                      if listaEstado[i] == "g":    #7 c,#/#
                          xFlecha=308
                          yFlecha=329
                      if listaEstado[i] == "h":    #8  c,b/b -> apila b
                          xFlecha=308
                          yFlecha=368
                      if listaEstado[i] == "i":    #9  c,a/a -> apila a
                          xFlecha=308
                          yFlecha=415
                      if listaEstado[i] == "j":   #10 b,b/landa -> desapila b
                          xFlecha=570
                          yFlecha=285
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "k":     #11 a,a/landa -> desapila a
                          xFlecha=571
                          yFlecha=320
                          #desapi
                          xdesa=724
                          ydesa=276
                      if listaEstado[i] == "True":     #12 landa/#/# final del
                          xFlecha=532
                          yFlecha=431
                          #desapi
                          xdesa=724
                          ydesa=276

                      if listaEstado[i] == "True":    #4
                          xTrue=183
                          yTrue=129
                      if listaEstado[i] == "False":    #4
                          xFalse=183
                          yFalse=129


                      reloj.tick(0.5)
                      screen.fill((0,0,0))
                      screen.blit(background_image, (0, 0))
                      screen.blit(flecha,(xFlecha,yFlecha))

                      a = fuentea.render(listaPila[i], 0, (0,0,0))
                      screen.blit(a, (348,160))

                      screen.blit(apilar,(xapi,yapi))
                      screen.blit(apilar,(1000,1000))
                      #reloj.tick(0.1)
                      screen.blit(desapilar,(xdesa,ydesa))
                      screen.blit(desapilar,(1000,1000))
                      screen.blit(texto1, (654,427))

                      screen.blit(errorTrue, (xTrue,yTrue))
                      screen.blit(errorFalse, (xFalse,yFalse))

                      pygame.display.update()



                      pygame.display.flip()
                      i=i+1
                  return 0
              pygame.init()
              main(self.cadena,aux.devolverEstados(),aux.devolverPila())
              # FIN DE PYGMAE
