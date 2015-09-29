# Codigo para convertir arreglos ordenados en arboles binarios

import time

class BinaryTree():

    def __init__(self):

        self.left = None
        self.right = None
        self.dato = None

    def array_to_binary(self,arreglo,start,end):
        """
        tiempo_inicial = time.time()
        print("TIEMPO INICIAL ", tiempo_inicial)
        """
        
        if (start > end):

            self.dato = None

        else:

            #print()
            mid = int((start + end) // 2)
            #print('Mid es: ',mid)
            #print('Se Agregara al arbol: ',arreglo[mid])
            #print()
            self.dato = arreglo[mid]
            self.left = BinaryTree()
            self.right = BinaryTree()
            self.left.array_to_binary(arreglo,start,mid - 1)
            self.right.array_to_binary(arreglo,mid + 1,end)
            
        """
        tiempo_real = time.time()
        tiempo_final = time.time() - tiempo_inicial
        print("TIEMPO REAL ", tiempo_real)
        print("TIEMPO FINAL ", tiempo_final)
        """
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

                
    def Buscar(self,elemento,Encontrado):

        if self.dato == None:

            Encontrado = False
            return Encontrado

        elif self.dato != None:
            
            #print('La raiz que entra es: ',self.dato)
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

"""
Array = [1,2,3,4,5,6,7]
ArbolPrueba = BinaryTree()
ArbolPrueba.array_to_binary(Array,0,len(Array) - 1)
print('Impresion en el programa general')
print('El arbol recorrido en PREORDEN es: ')
print()
ArbolPrueba.printTree()
print()
Encontrado = False
Encontrado = ArbolPrueba.Buscar(7,Encontrado)
print()
"""

