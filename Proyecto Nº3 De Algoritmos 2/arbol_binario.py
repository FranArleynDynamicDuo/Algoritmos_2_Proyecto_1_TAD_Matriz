# Codigo para convertir arreglos ordenados en arboles binarios

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
        

    def printTree(self):

        if self.dato == None:
            pass
        elif self.dato != None:
            print(self.dato)
            if self.left.dato != None:
                print('<--')
            elif self.left.dato == None:
                print('----')    
            self.left.printTree()
            if self.right.dato != None:
                print('-->')
            elif self.right.dato == None:
                print('----')
            self.right.printTree()

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

                print('Se Encontro el elemento "',elemento,'" en el ABB')

        if Encontrado == False:

            print()
            print('No existe el elemento "',elemento,' en el ABB')
            print()
                    
        return Encontrado


