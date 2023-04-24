class Item:
    def __init__(self,item, cantidad, precio1, precio2, precio3, costoUnitario, margen1, margen2,margen3,valorInventario) -> None:
        self.item = item
        self.cantidad = cantidad
        self.precio1 = precio1
        self.precio2 = precio2
        self.precio3 = precio3
        self.costoUnitario = costoUnitario
        self.margen1 = margen1
        self.margen2 = margen2
        self.margen3 = margen3
        self.valorInventario = valorInventario

    def calcularMargen(self,precio, costo):
        return (precio-costo)/precio
    
    def calcularValorInventario(self,cantidad, costo):
        return cantidad*costo


