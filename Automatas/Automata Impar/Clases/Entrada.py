import Automata
import Estado
import Lista
import os
class Obtener():
    def __init__(self,cadena,error):
        self.cadena=cadena
        self.error=error
        self.estadoPila=[]
        self.estados=[]
    def devolver1(self):
        return self.estadoPila
    def devolver2(self):
        return self.estados
    def validacion(self):
          if len(self.cadena)%2==0:
              print (' Esta palabra es par y no es aceptada' )
              os.system("pause")
          if len(self.cadena)%2!=0:
              p=Automata.Pila()
              p.apilar("#")
              guardar=Lista.Listas()
              guardar.addPila("#")
              print("la pila",p.mostrar())
              aux=Estado.Estados(self.cadena,p,self.error,guardar)
              aux.estado1(p)
              if aux.retorno():
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("True")
                  #print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  #print(self.estados)
                  print("-> Palabra Acepatada PALINDROMO!!!")
                  print("la pila",p.mostrar())
                  os.system("pause")
              else:
                  self.estadoPila=aux.devolverPila()
                  self.estadoPila.append("False")
                  #print(self.estadoPila)
                  self.estados=aux.devolverEstados()
                  #print(self.estados)
                  print ("-> Palabra no Aceptada, NOOOOO es PALINDROMO!!!!")
                  os.system("pause")
