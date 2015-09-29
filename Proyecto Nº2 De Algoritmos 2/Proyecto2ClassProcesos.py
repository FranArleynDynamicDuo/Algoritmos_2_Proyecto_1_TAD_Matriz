# Proyecto #2 Clase Procesos
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

class proceso:

    """

    Los objetos de esta clase representan un proceso con los que trabajara
    el simulador, tiene 4 atributos y solo la funcion de inicializacion,
    estos seran la unidad basica para todo el proyecto

    """


    def __init__(self):

        #Inicializa las variables

        #El nombre del proceso

        self.nombre = ''

        #El Numero de prioridad del procesos
        
        self.prioridad = 0

        #La cantidad de memoria ocupada por el proceso
        
        self.memoria = 0

        #El tiempo en el que dura el proceso en ejecutarse
        
        self.duracion = 0

        #Numero de subprocesos

        self.subprocesos = 0

        self.ListaSubprocesos = []
