import Automata
import sys
class Estados():
    def __init__(self,cadena,pila,error):
        self.cadena=cadena
        self.pila=pila
        self.error=error
    def retorno(self):
        if self.error==True:
            return True
        else:
            return False
    def cantC(self):
        conta=0
        for i in range(len(self.cadena)):
            if self.cadena[i] != "c":
                conta=conta+1
            if self.cadena[i] == "c":
                break
        return conta

    def estado1(self,pila):
        print (self.cadena+"\n------------\n")
        self.error=True
        for i in range(len(self.cadena)):
            if self.cadena[i]=="a":
                if self.pila.estaVacia():
                    self.pila.apilar(self.cadena[i])
                    print("APILADO vacio",self.pila.tope())
                else:
                    self.pila.apilar(self.cadena[i])
                    print("APILADO",self.pila.tope())
            if self.cadena[i]=="b":
                if self.pila.estaVacia():
                    self.apilar(self.cadena[i])
                    print("APILADO vacio",self.pila.tope())
                else:
                    self.pila.apilar(self.cadena[i])
                    print("APILADO ",self.pila.tope())
            c=self.cadena.count("c")
            print(c)
            if self.cadena[i] == "c":
                despuesC=(len(self.cadena)-self.cantC())
                print("antes de c vale->",self.cantC())
                print("depues de c vale->",despuesC)
                print("i vale -> ", i)
                print("valor de c",c)
                if self.cantC() > (despuesC-1):
                    self.error=False
                    print("palabra no es aceptada",self.error)
                    break
                j=i+1
                if c==1:
                    while(j < 2*despuesC-1):
                        print("despues",j)
                        self.error=self.estado2(self.cadena[j])
                        j=j+1
                    break
                else:
                    self.error=False
                    print("palabra no es aceptada",self.error)

            if self.cadena[i] != "a" and self.cadena[i]!="b":
                self.error=False
                print("letra erronia",self.cadena[i],self.error)
                break

            if c==0:
                self.error=False
                #print("palabra no es aceptada",self.error)
                break

        return self.error

    def estado2(self,cadena):
        self.error=True
        #print(self.error)
        if cadena=="c":
            print("No pasa nada")
        #print(self.pila.mostrar())
        #print(self.pila.tope())
        #print(cadena)
        if cadena=="a":
            if cadena == self.pila.tope():
                self.pila.desapilar()
                print("Desapilo -> ",cadena)
            else:
                print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
                self.error=False
        if cadena=="b":
            if cadena==self.pila.tope():
                self.pila.desapilar()
                print("Desapilo -> ",cadena)
            else:
                print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
                self.error=False
        if cadena != "a" and cadena !="b" and cadena != "c":
            print(" Palabra no Aceptada, no se encuentran en el lenguaje ",cadena)
            self.error=False
        return self.error
