from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from ListaSimple import ListaSimple
from Item import Item


class Menu:

    itemsIngresados= ListaSimple()

    def __init__(self) -> None:
        self.opciones=[
            ' Cargar archivo',
            ' Top 10 de productos con mayo margen de ganancia.',
            ' Top 10 de productos con más valor en el inventario.',
            ' Acerca de',
            ' Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('         __________________________           ')
        print('        |        Practica 1        |          ')
        print('        |        Productos         |          ')
        print('        |--------------------------|          \n')

        i = 0

        
        for opcion in self.opciones:
            i = i + 1
            print("\t",i," - "+opcion)
        
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        self.ejecutarOpcion(opcion)
        
    def pausa(self):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False)

    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            filename = askopenfilename()
            objetoXml = minidom.parse(filename)
            self.procesarInformacion(objetoXml)
            self.pausa()
        elif(opcion=='2'):
            top_margins=self.itemsIngresados.imprimir("margen")
            for item in top_margins["margen1"]:
                print(item.item,item.margen1)
            for item in top_margins["margen2"]:
                print(item.item,item.margen2)
            for item in top_margins["margen3"]:
                print(item.item,item.margen3)
            self.pausa()
        elif(opcion=='3'):
            self.itemsIngresados.imprimir("inventario")
            self.pausa()
        elif(opcion=='4'):
            espera = input('\n\tUSAC - S1\n\tProyecto 1\n\tDesarrollado por Kevin Girón-202010844...')
            self.pausa()  
        elif(opcion=='5'):
            quit()
        else:
            self.mostrar()

    def procesarInformacion(self, objetoXml):
        print('Procesando informacion...')

        itemCode = objetoXml.getElementsByTagName('ItemCode')
        quantity = objetoXml.getElementsByTagName('QuantityOnHand')
        precios1 = objetoXml.getElementsByTagName('PriceLevel1')
        precios2 = objetoXml.getElementsByTagName('PriceLevel2')
        precios3 = objetoXml.getElementsByTagName('PriceLevel3')
        costosUnitario = objetoXml.getElementsByTagName('LastTotalUnitCost')

        posicion = 0
        for numeral in itemCode:
            
            codigos = itemCode[posicion].firstChild.data
            cantidades = float(quantity[posicion].firstChild.data)
            precio1 = float(precios1[posicion].firstChild.data)
            precio2 = float(precios2[posicion].firstChild.data)
            precio3 = float(precios3[posicion].firstChild.data)
            costoUnitario = float(costosUnitario[posicion].firstChild.data)
            posicion = posicion + 1
            print(codigos,cantidades,precio1,precio2,precio3,costoUnitario)


            # Verificar si el elemento ya está presente en la lista
            nodo_actual = self.itemsIngresados.cabeza
            encontrado = False

            
            if cantidades <= 0:
                continue
            while nodo_actual is not None:
                if nodo_actual.dato.item ==  codigos:
                    encontrado = True
                    break
                nodo_actual = nodo_actual.siguiente
            
            if not encontrado:
                nuevoItem = Item(codigos,cantidades,precio1,precio2,precio3,costoUnitario)
                self.itemsIngresados.agregar(nuevoItem)
                print('Item agregado: ', nuevoItem.item)

        
        
if __name__ == '__main__':
    menu = Menu()
    menu.mostrar(False) 
