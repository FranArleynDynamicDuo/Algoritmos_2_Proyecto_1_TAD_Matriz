# Proyecto #2 Clase Simulador
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

import Proyecto2ClassProcesador
    #Archivo donde esta definida la clase de procesador

import Proyecto2ClassColaPrio
    #Archivo donde esta definida la clase de la cola de prioridad

import Proyecto2ClassProcesos
    #Archivo donde esta definida la clase de los procesos

import Pila
    #Archivo donde esta definida la clase de la pila de procesos

#import sys

#entrada = open(sys.argv[1],'r')
#salida = open(sys.argv[2],'w')

class simulador:

#---------------------------_init__----------------------------------#

    """
    Inicializa los parametros de cualquier objeto perteneciente a la
    clase "simulador"
    """

    def __init__(self):

        self.MemoriaSimu = 0 #Memoria Actual en uso del procesador
        self.ListaProcesadores = [] #Lista de los procesadores del
                                    #simulador

        #Inicalizamos los 4 procesadores y los colocamos en una lista
        #para facilitar el acceso durante el resto del programam e
        #inicializamos sus atributos

        self.subprocesosencurso = []

        self.ListaProcesadores = [None]*4

        for i in range(4):

            self.ListaProcesadores[i] = \
                                      (Proyecto2ClassProcesador.
                                       procesador())
            self.ListaProcesadores[i].identificador = i + 1
            self.ListaProcesadores[i].procesosEmpilados = Pila.Pila()
            self.ListaProcesadores[i].EstadoMemoria = 0
            
#-----------------------------Leer----------------------------------#

    def leer(self,NombreTexto,p):

        #Extrae un proceso de un archivo .txt y lo inserta en la
        #cola de prioridades
        
        data = open(NombreTexto,'r')
        lineas = len(open(NombreTexto).readlines())
        print('Se iniciaran ',lineas,' procesos nuevos')
        print()

        p = [None]*lineas

        for iter in range(lineas):

            p[iter] = Proyecto2ClassProcesos.proceso()

        for j in range(lineas):
                
            medidaJuntas = data.readline()
            medidaSep = medidaJuntas.split()
            p[j].nombre = str(medidaSep[1])
            p[j].prioridad = int(medidaSep[2])
            p[j].memoria = int(medidaSep[3])
            p[j].duracion = int(medidaSep[4])
            p[j].subprocesos = int(medidaSep[5])
                
            print('Proceso :',p[j].nombre )
            print()
            print('Prioridad: ',p[j].prioridad)
            print('Memoria usada',p[j].memoria)
            print('Duracion',p[j].duracion)
            print('Numero de subprocesos',p[j].subprocesos)
            print()

        

#------------------------COLA PRIORIDAD-----------------------------#

    # Organiza los procedimientos por prioridad utilizando un TAD
    # cola implementado en otro archivo.py

        #Asignamos la clase cola prioridad a ProcOrd para poder
        #utilizar los procesos del tad y ordenarlos

        ProcOrd = Proyecto2ClassColaPrio.ColaPrio(len(p))

        #Depositamos nuestra cola ordenada en un arreglo, elemento
        #por elemento
        
        for j in range(lineas):

            ArregloProcOrd = ProcOrd.proc_encolar(p[j],
                                                  p[j].prioridad) 

        #Comprobamos que se guardaron los elementos imprimiendolos
        #junto a sus prioridades para comprobar que se ordenaron de
        #manera correcta

        """
        
        for elemento in ArregloProcOrd:

            print(elemento.nombre,'-',elemento.prioridad)

        print()

        """
            
        return ArregloProcOrd

#-------------------------AsignarProceso-----------------------------#
      
    def AsignarProceso(self,proceso,Tiempo):

        """
        Busca el procesador con menos procesos en su pila de procesos
        empilados y empilamos "proceso" a la pila de ese procesador
        {Pre: "proceso" pertenece a la clase proceso}
        {Post: ProcMnOC.}
        """

        #print('Se asignara el proceso: -',proceso.nombre,'-')

        #Inicializamos nuestra variable de comparacion para empezar
        #a comparar el tamaño de todas las pilas de los procesadores

        ProcMnOc = len(self.ListaProcesadores[0].
                       procesosEmpilados.elementos)
        #print()

        #Comparamos el tamaño de cada pila de procesos empilados y
        #elegimos la meor de todas ellas
        
        for Comparacion in range(len(self.ListaProcesadores)- 1):

            comp2 = len(self.ListaProcesadores[Comparacion + 1].
                        procesosEmpilados.elementos)
            ProcMnOc = min(ProcMnOc,comp2)

        #Efectuamos la asignacion al procesador con menos procesos
        #con un proceso de "empilar"
        
        if (((ProcMnOc == len(self.ListaProcesadores[0].
                            procesosEmpilados.elementos))) and
            self.ListaProcesadores[0].procesosEmpilados.elementos == []):

            self.ListaProcesadores[0].procesosEmpilados.proc_empilar(proceso)
            self.MemoriaSimu = self.MemoriaSimu + proceso.memoria
            self.ListaProcesadores[0].EstadoMemoria = (
                self.ListaProcesadores[0].EstadoMemoria
                + proceso.memoria)
            salida.write('\n')
            salida.write(str(Tiempo))
            salida.write(' Inicializando proceso ')
            salida.write(p[reparte].nombre)
            salida.write(' en el procesador 1')
            salida.write('\n')

            if proceso.subprocesos > 0:
                   
                self.subprocesosencurso = [None]*proceso.subprocesos
                
                for iter in range(proceso.subprocesos):
                    self.subprocesosencurso[iter] = (
                       (Proyecto2ClassProcesos.proceso()))
                    self.subprocesosencurso[iter].nombre = (((proceso.nombre) +'[' + str(iter) + '}'))
                    self.subprocesosencurso[iter].prioridad = (
                       (proceso.prioridad))
                    self.subprocesosencurso[iter].duracion = (
                       (proceso.duracion))
                    self.subprocesosencurso[iter]
                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Iniciando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' - ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' en el procesador 1')
            
        elif (((ProcMnOc == len(self.ListaProcesadores[1].
                            procesosEmpilados.elementos))) and
            self.ListaProcesadores[1].procesosEmpilados.elementos == []):

            self.ListaProcesadores[1].procesosEmpilados.proc_empilar(proceso)
            self.MemoriaSimu = self.MemoriaSimu + proceso.memoria
            self.ListaProcesadores[1].EstadoMemoria = (
                self.ListaProcesadores[1].EstadoMemoria + proceso.memoria)
            
            salida.write('\n')
            salida.write(str(Tiempo))
            salida.write(' Inicializando proceso ')
            salida.write(p[reparte].nombre)
            salida.write(' en el procesador 2')
            salida.write('\n')


            if proceso.subprocesos > 0:
                   
                self.subprocesosencurso = [None]*proceso.subprocesos
                
                for iter in range(proceso.subprocesos):
                    self.subprocesosencurso[iter] = (
                       (Proyecto2ClassProcesos.proceso()))
                    self.subprocesosencurso[iter].nombre = (((proceso.nombre) +'[' + str(iter) + '}'))
                    self.subprocesosencurso[iter].prioridad = (
                       (proceso.prioridad))
                    self.subprocesosencurso[iter].duracion = (
                       (proceso.duracion))
                    self.subprocesosencurso[iter]
                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Iniciando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' - ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' en el procesador 2')
                
        elif (((ProcMnOc == len(self.ListaProcesadores[2].
                            procesosEmpilados.elementos))) and
            self.ListaProcesadores[2].procesosEmpilados.elementos == []):

            self.ListaProcesadores[2].procesosEmpilados.proc_empilar(proceso)
            self.MemoriaSimu = self.MemoriaSimu + proceso.memoria
            self.ListaProcesadores[2].EstadoMemoria = (
                self.ListaProcesadores[2].EstadoMemoria + proceso.memoria)
            salida.write('\n')
            salida.write(str(Tiempo))
            salida.write(' Inicializando proceso ')
            salida.write(p[reparte].nombre)
            salida.write(' en el procesador 3')
            salida.write('\n')

            if proceso.subprocesos > 0:
                   
                self.subprocesosencurso = [None]*proceso.subprocesos
                
                for iter in range(proceso.subprocesos):
                    self.subprocesosencurso[iter] = (
                       (Proyecto2ClassProcesos.proceso()))
                    self.subprocesosencurso[iter].nombre = (((proceso.nombre) +'[' + str(iter) + '}'))
                    self.subprocesosencurso[iter].prioridad = (
                       (proceso.prioridad))
                    self.subprocesosencurso[iter].duracion = (
                       (proceso.duracion))
                    self.subprocesosencurso[iter]
                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Iniciando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' - ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' en el procesador 3')
            
        elif (((ProcMnOc == len(self.ListaProcesadores[3].
                            procesosEmpilados.elementos))) and
            self.ListaProcesadores[3].procesosEmpilados.elementos == []):

            self.ListaProcesadores[3].procesosEmpilados.proc_empilar(proceso)
            self.MemoriaSimu = self.MemoriaSimu + proceso.memoria
            self.ListaProcesadores[3].EstadoMemoria = (
                self.ListaProcesadores[3].EstadoMemoria + proceso.memoria)
            salida.write('\n')
            salida.write(str(Tiempo))
            salida.write(' Inicializando proceso ')
            salida.write(p[reparte].nombre)
            salida.write(' en el procesador 4')
            salida.write('\n')

            if proceso.subprocesos > 0:
                   
                self.subprocesosencurso = [None]*proceso.subprocesos
                
                for iter in range(proceso.subprocesos):
                    self.subprocesosencurso[iter] = (
                       (Proyecto2ClassProcesos.proceso()))
                    self.subprocesosencurso[iter].nombre = (((proceso.nombre) +'[' + str(iter) + '}'))
                    self.subprocesosencurso[iter].prioridad = (
                       (proceso.prioridad))
                    self.subprocesosencurso[iter].duracion = (
                       (proceso.duracion))
                    self.subprocesosencurso[iter]
                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Iniciando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' - ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' en el procesador 4')
        
        for imprimir in range(4):

            for imprimir2 in self.ListaProcesadores[imprimir].procesosEmpilados.elementos:
            

                print('Los procesos del procesador ',imprimir + 1,
                      'son : ',imprimir2.nombre,
                      '- prioridad: ',imprimir2.prioridad)

 
        #print()
 
#-------------------------EstadoMemoria------------------------------#

    def EstadoMemoria(self):

        """
        Imprime el estado actual de la memoria del simulador,
        incluyendo la memoria utilizada en el sistema y la
        memoria utilizada por cada procesador
        {Pre: True }
        {Post: Se imprime la memoria usada por cada procesador,
               la memoria utilizada en el sistema y la memoria
               disponible}
        """

        #Imprimimos la memoria usada por cada procesador
        
        for iter in range(4):

            print('El procesador ',iter + 1,'esta utilizando ',
                  self.ListaProcesadores[iter].EstadoMemoria,
                  ' bytes de memoria')

        #Imprimimos la memoria utilizada por el sistema y la restante
        
        print('El simulador esta utilizando ',\
              self.MemoriaSimu,'de 1024 bytes de memoria')
        print('Quedan ',1024 - self.MemoriaSimu,'bytes de memoria')
        print()

#-------------------------ListaProcesos------------------------------#
        
    def ListaProcesos(self):

        #Imprime la lista actual de procesos y subprocesos

        for imprimir in range(4):

            for imprimir2 in self.ListaProcesadores[imprimir].procesosEmpilados.elementos:

                salida.write(imprimir2.nombre)
                salida.write(' ')
                salida.write(str(imprimir2.prioridad))
                salida.write(' ')
                salida.write(str(imprimir2.memoria))
                salida.write(' ')
                salida.write(str(imprimir2.duracion))
                salida.write(' en el procesador ')
                salida.write(str(imprimir + 1))
                salida.write('\n')

#--------------------------Principal---------------------------------#

#Asignamos a una variable la clase de simulador con su proceso de
#inicializacion

sim1 = simulador()

#Creamos un arreglo y utilizamos nuestro proceso de lectura para
#guardar en el todos los procesos encontrados en el archivo.txt
#y estos se ordenan en la cola de prioridades

p = []
salida = open('salida','w')
p = sim1.leer('Proc.txt',p)
Tiempo = 1

#Repartimos los procesos que tenemos en la cola de prioridades entre
#las pilas de los procesadores, colocando a los procesos mas
#prioritarios en el tope de la pila para que sean terminados primero


"""
PROGRAMA PRINCIPAL
"""
        
while (p != [] or
       (sim1.ListaProcesadores[0].procesosEmpilados.elementos != [] or
       sim1.ListaProcesadores[1].procesosEmpilados.elementos != [] or
       sim1.ListaProcesadores[2].procesosEmpilados.elementos != [] or
       sim1.ListaProcesadores[3].procesosEmpilados.elementos != [])
       ):

    if (Tiempo % 100 == 0) and (Tiempo != 1) and (Tiempo != 0):
        
        salida.write(str(Tiempo) + ' Listado')
        salida.write('\n')
        sim1.ListaProcesos()

        if (len(p) != 0):

            for i in range(len(p)):

                salida.write(p[i].nombre)
                salida.write(' ')
                salida.write(str(p[i].prioridad))
                salida.write(' ')
                salida.write(str(p[i].memoria))
                salida.write(' ')
                salida.write(str(p[i].duracion))
                salida.write(' Cola de Prioridades ')
                salida.write('\n')
                
        salida.write('Fin Listado')
        salida.write('\n')
        
    for reparte in range(len(p)):

        if ((sim1.MemoriaSimu + p[reparte].memoria <= 1024)):

            sim1.AsignarProceso(p[reparte],Tiempo)

            """
            if (p[reparte].subprocesos == 0):

                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Inicializando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' en el procesador ')
            
            
            elif (p[reparte].subprocesos != 0):

                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Empilando ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' subprocesos del proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' en el procesador ')

            """

            print('-',Tiempo,'-','se esta empilando el proceso',
                  p[reparte].nombre)

            """
            if (p[reparte].subprocesos > 0):

                salida.write('\n')
                salida.write(str(Tiempo))
                salida.write(' Iniciando proceso ')
                salida.write(p[reparte].nombre)
                salida.write(' - ')
                salida.write(str(p[reparte].subprocesos))
                salida.write(' en el procesador ')
                
                subprocesos = []
                subprocesos = [None]*(p[reparte].subprocesos)

            """
            """
                for i in range(p[reparte].subprocesos):
                    print('-',Tiempo,'-','Se esta empilando el subproceso',
                          p[reparte].nombre,'[',i,']')
                    
                    subprocesos[i] = Proyecto2ClassProcesos.proceso()
                    subprocesos[i].memoria = 0
                    subprocesos[i].prioridad = 1
                    subprocesos[i].duracion = p[reparte].duracion
                    subprocesos[i].nombre = (str(p[reparte].nombre + '[' + str(i) + ']'))
                    sim1.AsignarProceso(subprocesos[i])
                    print()

            """
            """
            """
            p.pop(reparte)        
            #sim1.AsignarProceso(p[reparte])
            #p.pop(reparte)
            Tiempo += -1
            
            for PT in sim1.ListaProcesadores:
                for PC in PT.procesosEmpilados.elementos:
                    PC.duracion += 1      
            break
        
    #Tiempo += 1

    for PT in sim1.ListaProcesadores:
        
        for PC in PT.procesosEmpilados.elementos:
            PC.duracion += -1
            if PC.duracion == 0:
                PT.procesosEmpilados.elementos = []

                salida.write(str(Tiempo))
                salida.write(' Finalizado proceso ')
                salida.write(PC.nombre)
                salida.write(' en el procesador ')
                salida.write(str(PT.identificador))
                salida.write('\n')
            
                print('-',Tiempo,'-','Termino el procesos',PC.nombre)
                salida.write('\n')
                sim1.MemoriaSimu = sim1.MemoriaSimu - PC.memoria
                PT.EstadoMemoria = PT.EstadoMemoria - PC.memoria
            break
        
    Tiempo += 1
                
salida.write(str(Tiempo + 1))
salida.write(' ')
salida.write('Fin ')
salida.close()
