

class ListaSimple:
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
    
    def imprimir(self, instruccion):
        if instruccion == "margen":
            top_margins = {
                'margen1': [],
                'margen2': [],
                'margen3': []
            }

            # Inicializar los elementos del top 10 con margen de ganancia más bajo
            for level in top_margins:
                for i in range(10):
                    top_margins[level].append(None)

            # Obtener los márgenes más altos en cada nivel a través de todos los elementos
            max_margins = {'margen1': 0, 'margen2': 0, 'margen3': 0}
            current = self.cabeza
            while current is not None:
                for level in max_margins:
                    margin_value = getattr(current.dato, level)
                    if margin_value > max_margins[level]:
                        max_margins[level] = margin_value
                current = current.siguiente

            # Recorrer la lista enlazada y actualizar el top 10 para cada nivel según corresponda
            current = self.cabeza
            while current is not None:
                for level in top_margins:
                    margin_value = getattr(current.dato, level)
                    if margin_value >= max_margins[level]:
                        for i in range(10):
                            if top_margins[level][i] is None or \
                                    getattr(top_margins[level][i], level) < margin_value:
                                # Insertar el elemento actual en el top 10 y desplazar los elementos inferiores
                                j = 9
                                while j > i:
                                    top_margins[level][j] = top_margins[level][j-1]
                                    j -= 1
                                top_margins[level][i] = current
                                break
                current = current.siguiente

            return top_margins
            
        elif instruccion == "inventario":
            pass
        


        

class Nodo():
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente