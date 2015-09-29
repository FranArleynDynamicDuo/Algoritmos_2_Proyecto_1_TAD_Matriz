# Proyecto #2 Clase Cola de Prioridad
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

"""
Esta es la implementacion de una cola de prioridad que usaremos para
guardar y ordenar todos los procesos extraidos del documento .txt,
consta de 3 atributos y 5 funciones. En esta cola los elementos que
se le almacenen son ordenados usando como referencia su numero de
prioridad
"""

class ColaPrio():

    """
    Funcion que inicializa los atributos de los elementos que
    pertenecen a la clase ColaPrio
    """

    def __init__ (self,m):

        self.elementos = []
        self.prioridad = []
        self.MAX = m

    """
    Funcion que agrega un elemento al final de la cola
    {Pre:}
    {Post:}
    """

    def proc_encolar(self,elemento,priori):

        
        pos = 0

        #Si la cola es vacia, agregamos un elemento a la primera
        #posicion
        
        if (len(self.elementos) == 0):

            self.elementos.append(elemento)
            self.prioridad.append(priori)

        #Si no es vacia entonces buscamos

        elif (len(self.elementos) >= 0):


            for P in (self.prioridad):
                pos += 1
                if priori <= P:
                    self.elementos.insert(pos-1,elemento)
                    self.prioridad.insert(pos-1,priori)
                    return self.elementos
                    break

                elif ( pos == len(self.prioridad)):
                    self.elementos.insert(1 + len(self.elementos),elemento)
                    self.prioridad.insert(1 + len(self.elementos),priori)
                    return self.elementos
                    break       
                
    """
    Funcion que extrae el primer elemento de la cola
    """

    def proc_desencolar (self):

        if (len(self.elementos) != 0):

            self.elementos.pop(0)
            self.prioridad.pop(0)
            print("Lista de elementos",self.elementos,"  Lista Prioridad", self.prioridad)

        elif (len(self.elementos) == 0):

            print("La cola esta vacia no hay elementos que eliminar")

    """
    Funcion que nos devuelve el primer elemento de la cola
    """
            
    def proc_primero (self):

        if (len(self.elementos) != 0):

            primero = self.elementos[0]
            print(primero)

        elif (len(self.elementos) == 0):

            print("La cola esta vacia no hay elementos que mostrar")

    def proc_vacio (self):

        vacio = (self.elementos == [] and self.prioridad == [])
        print(vacio)



        

    
