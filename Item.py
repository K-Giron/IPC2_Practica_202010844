class Item:
    def __init__(self,item, cantidad, precio1, precio2, precio3, costoUnitario) -> None:
        self.item = item
        self.cantidad = cantidad
        self.precio1 = precio1
        self.precio2 = precio2
        self.precio3 = precio3
        self.costoUnitario = costoUnitario
        self.margen1= self.calcularMargen(self.precio1, self.costoUnitario)
        self.margen2= self.calcularMargen(self.precio2, self.costoUnitario)
        self.margen3= self.calcularMargen(self.precio3, self.costoUnitario)
        self.valorInventario= self.calcularValorInventario(self.cantidad, self.costoUnitario)

    def calcularMargen(self,precio, costo):
        return ((precio-costo)/costo)*100
    
    def calcularValorInventario(self,cantidad, costo):
        return cantidad*costo


