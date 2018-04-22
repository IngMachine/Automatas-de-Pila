
from automata import Pila
import sys
global error



def  cantC(cadena):
    conta=0
    for i in range(len(cadena)):
        if cadena[i] != "c":
            conta=conta+1
        if cadena[i] == "c":
            break
    return conta

def estado1(cadena):
    error = True
    for i in range(len(cadena)):


        if cadena[i]=="a":
            if p.estaVacia():
                p.apilar(cadena[i])
                print ("APILADO vacio ",p.tope())

            else:
                p.apilar(cadena[i])
                print ("APILADO  ",p.tope())

        if cadena[i]=="b":
            if p.estaVacia():
                p.apilar(cadena[i])
                print ("APILADO vacio ",p.tope())

            else:
                p.apilar(cadena[i])
                print ("APILADO  ",p.tope())
        c=cadena.count("c")

        if cadena[i] == "c":

            despuesC=(len(cadena)- cantC(cadena))
            print("antes de c vale->",cantC(cadena))
            print("depues de c vale->",despuesC)
            print("i vale -> ", i)
            print("valor de c",c)
            if cantC(cadena) > (despuesC-1):
                error=False
                print("palabra no es aceptada",error)
                break
            j=i+1
            if c == 1:
                #if cadena[len(cadena)-1] =="c":
                    #error=False
                    #print("palabra no es aceptada papuuu",error)
                    #break

                while (j < 2*despuesC-1):
                    print("depues ->",j)
                    error =estado2(cadena[j])
                    j=j+1

                break
            else:
                error=False
                print("palabra no es aceptada",error)
                break

        if cadena[i] != "a" and cadena[i] != "b":
            error=False
            print("letra erronia",cadena[i],error)
            break
        if c==0:
            error=False
            print("palabra no es aceptada",error)
            break

    return error


def estado2(cadena):
    error=True

    if cadena == "c":
        print("no pasa nada")


    if cadena =="a":
        if  cadena == p.tope():
            p.desapilar()
            print("Desapilo -> ",cadena)
        else:
            print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
            error=False
            #sys.exit()

    if cadena =="b":
        if  cadena == p.tope():
            p.desapilar()
            print("Desapilo -> ",cadena)
        else:
            print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
            error=False
            #sys.exit()


    if cadena != "a" and cadena !="b" and cadena != "c":
        print(" Palabra no Aceptada, no se encuentran en el lenguaje ",cadena)
        error=False
        #sys.exit()


    return error


cadena=input("->  ingrese la palabra : ")
print(cadena)
print(len(cadena))

if len(cadena)%2 == 0:
    print (' Esta palabra es par y no es aceptada' )

if len(cadena)%2 != 0:
    p = Pila()


    aux=estado1(cadena)

    print (" impar ")
    if aux:

        print("-> Palabra Acepatada PALINDROMO!!!")
        print(p.mostrar())
    else:
        print ("-> Palabra no Aceptada, No!! es PALINDROMO")
