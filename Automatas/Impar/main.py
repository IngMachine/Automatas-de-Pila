from Clases import Automata
from Clases import Entrada
from Clases import Estado
import sys
error=True

cadena=input("->  ingrese la palabra : ")
#print("------------\n"+cadena)
#print(repr(len(cadena))+ "\n------------")
Palabra=Entrada.Obtener(cadena,error)
Palabra.validacion()
"""


if len(cadena)%2 != 0:
    p = Pila()


    aux=estado1(cadena)

    print (" impar ")
    if aux:

        print("-> Palabra Acepatada PALINDROMO!!!")
        print(p.mostrar())
    else:
        print ("-> Palabra no Aceptada, no se encuentran en el lenguaje")
"""
