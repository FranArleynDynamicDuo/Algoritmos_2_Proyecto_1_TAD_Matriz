# Proyecto #2 Clase Procesador
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

class procesador:

    """

    Esta clase es la de los procesadores del simulador, estos procesadores
    son los que trabajan los "procesos" que se extraen del archivo.txt y
    descartan los que se han terminado, son los trabajadores del simulador

    Consta de 3 atributos(identificador,procesosEmpilados y EstadoMemoria)
    y de 1 proceso de inicializacion

    """

#----------------------------crear-----------------------------------#

    """
    Proceso de inicializacion para las variables pertenecientes a la clase
    {Pre: True}
    {Post: self.identificador = " " ^ self.procesosEmpilados = [] ^
       self.EstadoMemoria = 0}
       
    """

    def crear(self):

        self.identificador = " "            #Identificacion de cada
                                            #procesador
        
        self.procesosEmpilados = []         #Procesos en la pila por
                                            #trabajar
        
        self.EstadoMemoria = 0              #Memoria usada por el
                                            #procesador actualmente

        self.subprocesos = []
