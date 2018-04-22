import Automata
import sys
class Estados():
    def __init__(self,cadena,pila,error,guardar):
        self.cadena=cadena
        self.pila=pila
        self.error=error
        self.guardar=guardar
        self.estadopila=""
        self.mitad=len(cadena)/2

    def retorno(self):
        if self.error==True:
            return True
        else:
            return False

    def devolverEstados(self):
        return self.guardar.mostrarEstado()

    def devolverPila(self):
        return self.guardar.mostrarPila()

    def estado1(self,pila):
        self.error=True
        for i in range(len(self.cadena)):
            print("esto es i =",i)
            if self.cadena[i]=="a" and self.mitad!=i:
                if self.pila.tope()=="#":
                    self.pila.desapilar()
                    self.pila.apilar("#")
                    self.pila.apilar("a")
                    self.guardar.addEstado("a")

                elif self.pila.tope()=="a":
                    self.pila.desapilar()
                    self.pila.apilar("a")
                    self.pila.apilar("a")
                    self.guardar.addEstado("c")

                else:
                    self.pila.desapilar()
                    self.pila.apilar("b")
                    self.pila.apilar("a")
                    self.guardar.addEstado("e")
                print("---------------------------")
                print("la pila",self.pila.mostrar())
                self.estadopila=" ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Como va la Pila que le agrega o quita",self.guardar.mostrarPila())
                print("Identificacion para mostrar las reglas",self.guardar.mostrarEstado())
                print("---------------------------")
            if self.cadena[i]=="b" and self.mitad!=i:
                if self.pila.tope()=="#":
                    self.pila.desapilar()
                    self.pila.apilar("#")
                    self.pila.apilar("b")
                    self.guardar.addEstado("b")

                elif self.pila.tope()=="a":
                    self.pila.desapilar()
                    self.pila.apilar("a")
                    self.pila.apilar("b")
                    self.guardar.addEstado("d")

                else:
                    self.pila.desapilar()
                    self.pila.apilar("b")
                    self.pila.apilar("b")
                    self.guardar.addEstado("f")

                print("---------------------------")
                print("la pila",self.pila.mostrar())
                self.estadopila=" ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Como va la Pila que le agrega o quita",self.guardar.mostrarPila())
                print("Identificacion para mostrar las reglas",self.guardar.mostrarEstado())
                print("---------------------------")

            if i==self.mitad:
                if self.cadena[i]!="a" and self.cadena[i]!="b":
                    self.error=False
                    print("letra erronia",self.cadena[i],self.error)
                    break

                if self.cadena[i]=="a":
                    if self.pila.tope()=="a":
                        self.pila.desapilar()
                        self.guardar.addEstado("h")

                if self.cadena[i]=="b":
                    if self.pila.tope()=="b":
                        self.pila.desapilar()
                        self.guardar.addEstado("g")

                print("---------------------------")
                print("la pila",self.pila.mostrar())
                self.estadopila=" ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Como va la Pila que le agrega o quita",self.guardar.mostrarPila())
                print("Identificacion para mostrar las reglas",self.guardar.mostrarEstado())
                print("---------------------------")
                j=i+1
                while j<len(self.cadena):
                    print("Esto es j",j)
                    self.error=self.estado2(self.cadena[j])
                    if self.error==False:
                        break
                    else:
                        j=j+1
                break

            if self.cadena[i]!="a" and self.cadena[i]!="b":
                self.error=False
                print("letra erronia",self.cadena[i],self.error)
                break

        return self.error

    def estado2(self,cadena):

        self.error=True
        print("cadena de estado2",cadena)

        if cadena=="c":
            print("No pasa nada")

        if cadena=="a":

            if self.pila.tope()=="a":
                self.pila.desapilar()
                print("la pila",self.pila.mostrar())
                self.guardar.addEstado("j")
                print("---------------------------")
                print("la pila",self.pila.mostrar())
                self.estadopila=" ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Como va la Pila que le agrega o quita",self.guardar.mostrarPila())
                print("Identificacion para mostrar las reglas",self.guardar.mostrarEstado())
                print("---------------------------")
            else:
                print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
                self.error=False

        if cadena=="b":
            if self.pila.tope()=="b":
                self.pila.desapilar()
                print("la pila",self.pila.mostrar())
                self.guardar.addEstado("i")
                print("---------------------------")
                print("la pila",self.pila.mostrar())
                self.estadopila=" ".join(self.pila.mostrar())
                self.guardar.addPila(self.estadopila)
                print("Como va la Pila que le agrega o quita",self.guardar.mostrarPila())
                print("Identificacion para mostrar las reglas",self.guardar.mostrarEstado())
                print("---------------------------")
            else:
                print("palabra no es aceptada, por lo tanto no es palindroma",cadena)
                self.error=False

        if cadena != "a" and cadena!="b":
            print(" Palabra no Aceptada, no se encuentran en el lenguaje ",cadena)
            self.error=False

        return self.error
