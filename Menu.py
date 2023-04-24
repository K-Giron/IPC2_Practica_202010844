from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom


class Menu:
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
            #self.graficarMuestra(self.muestraAnalizada)
            self.pausa()
        elif(opcion=='3'):
            #self.analizarMuestra()
            self.pausa()
        elif(opcion=='4'):
            espera = input('\n\tUSAC - S1\n\tProyecto 1\n\tDesarrollado por Kevin Girón-202010844...')
            self.pausa()  
        elif(opcion=='5'):
            quit()
        else:
            self.mostrar()
