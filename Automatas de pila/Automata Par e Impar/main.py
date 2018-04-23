from Tkinter import *
from Clases import Automata
from Clases import Entrada
from Clases import EstadoPar
import sys
error=True

#tekiter Ingresar Texto
def mostrar():
    mostrarPalabra=Label(text=entrada.get(), font=("FreeMono",14)).place(x=179,y=388)
    cadena=entrada.get()
    #cadena=input("->  ingrese la palabra : ")
    Palabra=Entrada.Obtener(cadena,error)
    Palabra.validacion()
    #pygame.init()
    #main(cadena)


ventana=Tk()
ventana.geometry("433x433+0+0")
imagen=PhotoImage(file="fondo_Tkinter.png")
MostrarImagen=Label(ventana,image=imagen).place(x=0,y=0)
#ventana.config(bg="blue")
ventana.title("Campos de Texto")
#lblUsuario=Label(text="Ingresar Palabra ", font=("FreeMono",14)).place(x=119,y=117)
#creand un campo de texto

entrada=StringVar()
entrada.set("")
palabraCadena=Entry(ventana,textvariable=entrada,width=30).place(x=94,y=170)

#crear dos botones (ingresa palabra)
btnIngresar=Button(ventana,text="INGRESAR",command = mostrar,font=("FreeMono",14),width=15).place(x=125,y=217)

ventana.mainloop()

    #fin de tkiter


#print("main",Palabra.devolver1())
#print("main2",Palabra.devolver2())
