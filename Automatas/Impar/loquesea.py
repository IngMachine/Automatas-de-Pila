from automata import Pila
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
        if cadena[i] == "c":
            despuesC=(len(cadena)- cantC(cadena))
            print("depues vale->",despuesC)
            print("i vale -> ", i)

            j=i+1
            while (j < 2*despuesC-1):
                print("depues ->",j)
                error =estado2(cadena[j])
                j=j+1

            break
        if cadena[i] != "a" and cadena[i] != "b":
            error=False
            print("letra erronia",cadena[i],error)
            break
    return error


def estado2(cadena):
    error=True

    if cadena == "c" and p.estaVacia():
        print("no pasa nada")

    if cadena =="a":
        if  cadena == p.tope():
            p.desapilar()
            print("Desapilo -> ",cadena)
        else:
            print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
            error=False
            sys.exit()

    if cadena =="b":
        if  cadena == p.tope():
            p.desapilar()
            print("Desapilo -> ",cadena)
        else:
            print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
            error=False
            return error
            sys.exit()

    if cadena != "a" and cadena !="b" and cadena != "c":
        print(" Palabra no Aceptada, no se encuentran en el lenguaje ",cadena)
        error=False
        return error
        sys.exit()
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
        print ("-> Palabra no Aceptada, no se encuentran en el lenguaje")
