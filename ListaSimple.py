class ListaSImple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        if self.cabeza == None:
            self.cabeza = Nodo(dato)
        else:
            aux = self.cabeza
            while aux.siguiente != None:
                aux = aux.siguiente
            aux.siguiente = Nodo(dato)
    
    def ordenar(self):
        aux = self.cabeza
        while aux.siguiente != None:
            aux2 = aux.siguiente
            while aux2 != None:
                if aux.dato.valorInventario < aux2.dato.valorInventario:
                    aux.dato, aux2.dato = aux2.dato, aux.dato
                aux2 = aux2.siguiente
            aux = aux.siguiente
    
    def imprimir(self):
        aux = self.cabeza
        while aux != None:
            print(aux.dato.item)
            aux = aux.siguiente

class Nodo():
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente