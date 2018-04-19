import Automata
import Estado
class Obtener():
    def __init__(self,cadena,error):
        self.cadena=cadena
        self.error=error
    def validacion(self):
          if len(self.cadena)%2==0:
              print (' Esta palabra es par y no es aceptada' )
          if len(self.cadena)%2!=0:
              #print("no entraaaaa")
              print("IMPAR")
              p=Automata.Pila()
              aux=Estado.Estados(self.cadena,p,self.error)

              #aux.estado1(p)
              #print(aux.retorno(10,20))
              #print(aux.estado1(p))

              aux.estado1(p)
              if aux.retorno():
                  print("-> Palabra Acepatada PALINDROMO!!!")
                  print(p.mostrar())
              else:
                  print ("-> Palabra no Aceptada, NOOOOO es PALINDROMO!!!!")
              """if aux.estado1(p):
                  print("")
                  print(p.mostrar())
              else:
                  print ("-> Palabra no Aceptada, no se encuentran en el lenguaje")"""
