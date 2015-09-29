# Proyecto #2 Clase Pila
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

"""
Esta clase es la implementacion de un TAD pila generico que usaremos
para juntar los procesos que esten asignados a cada procesaor y para
desechar los que ya estan terminados

Consta con un solo atributo(Elementos) y 6 funciones, desde la
inicializacion de la cola hasta la empilacion y desempilacion de
elementos de la cola
"""

class Pila():

        def __init__ (self):

            #Esta funcion inicializa los elementos pertenecientes a
            #esta clase

            self.elementos = [] #Son los elementos que estan en la pila

        def __repr__(self):

            #Funcion utilizada para la impresion de los elementos
            #de la cola

            return(self.elementos)

	
        def proc_empilar (self,x):

            #Funcion que toma un elemento y lo coloca en el tope de la
            #pila

            self.elementos.append(x)
		
        def proc_desempilar (self):

            #Funcion que toma el elemento que esta en el tope de la
            #cola y lo extrae de la cola

            self.elementos.pop()

        def proc_tope (self):

            #Funcion que imprime el elemento en el tope de la cola

            #Calculamos la longitud de la cola

            top = len(self.elementos)

            #Imprimos el elemeto en esa posicion
            
            tope = self.elementos[top - 1]
            print(tope)
	
        def proc_vacio (self):

            #Funcion que comprueba si la cola es vacia

            Vacio = (self.elementos == [])
            print(Vacio)
               

"""
Secuencia = Pila("100")
Secuencia.proc_empilar(13)
Secuencia.proc_tope()
Secuencia.proc_empilar(100)
Secuencia.proc_tope()
Secuencia.proc_vacio()
"""
