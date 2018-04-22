from Clases import Automata
from Clases import Entrada
from Clases import Estado
import sys
error=True

cadena=input("->  ingrese la palabra : ")
Palabra=Entrada.Obtener(cadena,error)
Palabra.validacion()
"""print("main",Palabra.devolver1())
print("main2",Palabra.devolver2())"""
