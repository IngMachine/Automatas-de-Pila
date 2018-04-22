from Tkinter import *
#tekiter Ingresar Texto
def mostrar():
    mostrarPalabra=Label(text=entrada.get(), font=("FreeMono",14)).place(x=179,y=388)

ventana=Tk()
ventana.geometry("500x500+0+0")
imagen=PhotoImage(file="fondo tkinter.png")
MostrarImagen=Label(ventana,image=imagen).place(x=0,y=0)
#ventana.config(bg="blue")
ventana.title("Campos de Texto")
lblUsuario=Label(text="Ingresar Palabra ", font=("FreeMono",14)).place(x=119,y=117)
#creand un campo de texto

entrada=StringVar()
entrada.set("ricardo")
txtUsuario=Entry(ventana,textvariable=entrada,width=25).place(x=117,y=142)

#crear dos botones
btnSaludar=Button(ventana,text="Ingresar",command = mostrar,font=("FreeMono",14),width=5).place(x=199,y=266)

#montar la imagen

ventana.mainloop()

#fin de tkiter 
