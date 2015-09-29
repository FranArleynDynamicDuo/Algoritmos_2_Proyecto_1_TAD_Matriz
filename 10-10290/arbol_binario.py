# Codigo para convertir arreglos ordenados en arboles binarios y
# para buscar un elemento en el arbol binario
# Arleyn Goncalves 10-10290
# Francisco Sucre 10-10717

import time

class BinaryTree():

    # Iniciamos los atributos del arbol binario
    
    def __init__(self):

        self.left = None       # hijo izquierda
        self.right = None      # hijo derecha
        self.dato = None       # Raiz

    # Construye el arbol binario de busqueda

    def array_to_binary(self,arreglo,start,end):
        
        if (start > end):

            self.dato = None

        else:

            mid = int((start + end) // 2)
            self.dato = arreglo[mid]
            self.left = BinaryTree()
            self.right = BinaryTree()
            self.left.array_to_binary(arreglo,start,mid - 1)
            self.right.array_to_binary(arreglo,mid + 1,end)
            
        return self

    # Busca en el arbol un elemento escogido de manera aleatorio
                
    def Buscar(self,elemento,Encontrado):

        if self.dato == None:

            Encontrado = False
            return Encontrado

        elif self.dato != None:
            
            Encontrado = (self.dato == elemento)
            
            if Encontrado == False:

                if elemento > self.dato:

                    Encontrado = self.right.Buscar(elemento,Encontrado)

                elif elemento <= self.dato:

                     Encontrado = self.left.Buscar(elemento,Encontrado)
                        
            elif Encontrado == True:

                pass

        if Encontrado == False:

            pass
                    
        return Encontrado


