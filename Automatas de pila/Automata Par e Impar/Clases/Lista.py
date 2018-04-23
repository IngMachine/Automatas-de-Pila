class Listas():
    def __init__(self):
        self.ListaEstado =[]
        self.ListaEstadoPila =[]

    def addPila(self, item):
        self.ListaEstadoPila.append(item)

    def addEstado(self, item):
        self.ListaEstado.append(item)

    def mostrarPila(self):
        return self.ListaEstadoPila

    def mostrarEstado(self):
        return self.ListaEstado

    def tamanoEstado(self):
        return len(self.ListaEstado)

    def tamanoPila(self):
        return len(self.ListaEstadoPila)
