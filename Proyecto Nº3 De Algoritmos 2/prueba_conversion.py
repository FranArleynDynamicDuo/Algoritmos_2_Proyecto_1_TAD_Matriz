# PRUEBA DE CONVERCION
# Arleyn Goncalves 10-10290
# Francisco Sucre 10-10717

import Ordenamiento   # Importa los algoritmos de ordenamiento

import arbol_binario  # Importa la libreria de arboles

import time           # Importa el time

import random         # Importa el random

import math           # Importa el match

import sys            # Importa el sys

num_pruebas = int(sys.argv[1])     # Numero de pruebas
num_elementos = int(sys.argv[2])   # Numero de elementos del arreglo


print("\n")
print('Se aplicaran',num_pruebas,'pruebas')
print('Y los arreglos tendran',num_elementos,'elementos')
print("\n")

#------------------------------PRINCIPAL-----------------------------#

# Inicializamos un arreglo para almacenar los tiempos de cada algoritmo
# de ordenamiento, conversion del arbol y busqueda en el arbol

TiempoQuickSort = [0]*(num_pruebas)
TiempoMergerSort = [0]*(num_pruebas)
TiempoCombSort = [0]*(num_pruebas)
TiempoOddEvenSort = [0]*(num_pruebas)
TiempoGnomeSort = [0]*(num_pruebas)
TiempoArbol = [0]*(num_pruebas)
TiempoBuscar = [0]*(num_pruebas)


for i in range(num_pruebas):

    # Se crea el arreglo aleatorio

    Arreglo = Ordenamiento.StringAleatorias(num_elementos)
    aux = []
    aux1 = []
    aux2 = []
    aux3 = []
    aux4 = []

    # Guardamos el arreglo en 5 variables auxiliares

    for iteracion in range(len(Arreglo)):

        aux.append(Arreglo[iteracion])
        aux1.append(Arreglo[iteracion])
        aux2.append(Arreglo[iteracion])
        aux3.append(Arreglo[iteracion])
        aux4.append(Arreglo[iteracion])


    
    # Algoritmo de Ordenamiento QUICK SORT

    print("\n")
    print('QUICK SORT')
    print("\n")
    
    tiempo_inicial = time.time()     # Tiempo inicial
    
    izq = 0                          # Inicializamos izquierda
    der = len(Arreglo) - 1           # Inicializamos derecha
    Ordenamiento.QuickSort(aux,izq,der)
    
    tiempo_final = time.time() - tiempo_inicial # Tiempo final
    TiempoQuickSort[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoQuickSort[i])
    print("%.2f" % TiempoQuickSort[i])

    # Algoritmo de Ordenamiento MERGER SORT
    
    print("\n")
    print("MERGER SORT")
    print("\n")
    tiempo_inicial = time.time()      # Tiempo Inicial

    izq = 0                           # Inicializamos izquierda
    der = len(aux1)                   # Inicializamos derecha
    Ordenamiento.MergeSor(aux1,izq,der)

    tiempo_final = time.time() - tiempo_inicial # Tiempo FInal
    TiempoMergerSort[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoMergerSort[i])
    print("%.2f" % TiempoMergerSort[i]) 

    # Algoritmo de Ordenamiento COMB SORT

    print("\n")
    print('COMB SORT')
    print("\n")
    tiempo_inicial = time.time()      # Tiempo Inicial

    Ordenamiento.CombSort(aux2)
    
    tiempo_final = time.time() - tiempo_inicial # Tiempo Final
    TiempoCombSort[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoCombSort[i])
    print("%.2f" % TiempoCombSort[i])


    # Algoritmo de Ordenamiento ODD EVEN SORT
    
    print("\n")
    print('ODD EVEN SORT')
    print("\n")
    tiempo_inicial = time.time()       # Tiempo Inicial

    Ordenamiento.Oddevensort(aux3)
    
    tiempo_final = time.time() - tiempo_inicial # Tiempo Final
    TiempoOddEvenSort[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoOddEvenSort[i])
    print("%.2f" % TiempoOddEvenSort[i])

    # Algoritmo de Ordenamiento GNOME SORT

    print("\n")
    print('Gnome Sort')
    print("\n")
    tiempo_inicial = time.time()        # Tiempo Inicial
    
    Ordenamiento.GnomeSort(aux4)
    
    tiempo_final = time.time() - tiempo_inicial # Tiempo Fibal
    TiempoGnomeSort[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoGnomeSort[i])
    print("%.2f" % TiempoGnomeSort[i])

    # CONVERTIR EN ARBOL BINARIO
    
    start = 0                           # Inicializamos start
    end = len(aux) - 1                  # Inicializamos end
    
    tiempo_inicial = time.time()        # Tiempo Inicial
    
    Arbol = arbol_binario.BinaryTree()
    Arbol.array_to_binary(aux,start,end)
    
    print("\n")
    tiempo_final = time.time() - tiempo_inicial # Tiempo Final
    TiempoArbol[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoArbol[i])
    print("%.2f" % TiempoArbol[i]) 

    # BUSCAR EN UN ARBOL

    tiempo_inicial = time.time()       # Tiempo Inicial

    Elem = random.choice(aux)          # Eligue el elemento random del arreglo
                                       # para buscarlo en el arbol binario
    Encontrado = False
    Arbol.Buscar(Elem,Encontrado)

    tiempo_final = time.time() - tiempo_inicial   # Tiempo Final
    TiempoBuscar[i] = tiempo_final*1000
    print("TIEMPO FINAL", TiempoBuscar[i])
    print("%.2f" % TiempoBuscar[i]) 

# CALCULAR EL PROMEDIO

# Inicializa las variables que almacenan el promedio

PromQuickSort = 0
PromMergerSort = 0
PromCombSort = 0
PromOddEvenSort = 0
PromGnomeSort = 0
PromArbol = 0
PromBuscar = 0

# Se suman todos los valores de tiempo obtenidos

for i in range(num_pruebas):

    PromQuickSort += TiempoQuickSort[i]
    PromMergerSort += TiempoMergerSort[i]
    PromCombSort += TiempoCombSort[i]
    PromOddEvenSort += TiempoOddEvenSort[i]
    PromGnomeSort += TiempoGnomeSort[i]
    PromArbol += TiempoArbol[i]
    PromBuscar += TiempoBuscar[i]

# Se divide la suma de todos los tiempos obtenidos entre el numero de
# pruebas para obtener el promedido de tiempo
    
PromQuickSort = PromQuickSort/num_pruebas
PromMergerSort = PromMergerSort/num_pruebas
PromCombSort = PromCombSort/num_pruebas
PromOddEvenSort = PromOddEvenSort/num_pruebas
PromGnomeSort = PromGnomeSort/num_pruebas
PromArbol = PromArbol/num_pruebas
PromBuscar = PromBuscar/num_pruebas

print("\n")
print("Promedio de QuickSort = ", "%.2f" % PromQuickSort)
print("Promedio de MergerSort= ", "%.2f" % PromMergerSort)
print("Promedio de CombSort = ", "%.2f" % PromCombSort)
print("Promedio de OddEvenSort = ", "%.2f" % PromOddEvenSort)
print("Promedio de GnomeSort = ", "%.2f" % PromGnomeSort)
print("Promedio de Conv. Arbol = ", "%.2f" % PromArbol)
print("Promedio de Busc. Arbol = ", "%.2f" % PromBuscar)


# DESVIACION ESTANDAR

# Se inicializa la variable para calcular la desviacion estandar

DesvQuickSort = 0
DesvMergerSort = 0
DesvCombSort = 0
DesvOddEvenSort = 0
DesvGnomeSort = 0
DesvArbol = 0
DesvBuscar = 0

# Se realizan los calculos para la desviacion estandar
# (Promedio - Tiempo[i])^2

for i in range(num_pruebas):
    
    DesvQuickSort += (PromQuickSort - TiempoQuickSort[i])**2
    DesvMergerSort += (PromMergerSort - TiempoMergerSort[i])**2
    DesvCombSort += (PromCombSort - TiempoCombSort[i])**2
    DesvOddEvenSort += (PromOddEvenSort - TiempoOddEvenSort[i])**2
    DesvGnomeSort += (PromGnomeSort - TiempoGnomeSort[i])**2
    DesvArbol += (PromArbol - TiempoArbol[i])**2
    DesvBuscar += (PromBuscar - TiempoBuscar[i])**2

# Al valor obtenido anteriormente se divide entre el numero de valores
# y se calcula la raiz cuadrada y asi obtenemos la desviacion estandar

DesvQuickSort = math.sqrt(DesvQuickSort/num_pruebas)
DesvMergerSort = math.sqrt(DesvMergerSort/num_pruebas)
DesvCombSort = math.sqrt(DesvCombSort/num_pruebas)
DesvOddEvenSort = math.sqrt(DesvOddEvenSort/num_pruebas)
DesvGnomeSort = math.sqrt(DesvGnomeSort/num_pruebas)
DesvArbol = math.sqrt(DesvArbol/num_pruebas)
DesvBuscar = math.sqrt(DesvBuscar/num_pruebas)

print("\n")
print("Desviacion de QuickSort = ", "%.2f" % DesvQuickSort)
print("Desviacion de MergerSort = ", "%.2f" % DesvMergerSort)
print("Desviacion de CombSort = ", "%.2f" % DesvCombSort)
print("Desviacion de OddEvenSort = ", "%.2f" % DesvOddEvenSort)
print("Desviacion de GnomeSort = ", "%.2f" % DesvGnomeSort)
print("Desviacion de Conv. Arbol = ", "%.2f" % DesvArbol)
print("Desviacion de Busq. Arbol = ", "%.2f" % DesvBuscar)

#------------------------IMPRIMIR CONSOLA----------------------------#

# Se imprime en la consola los valores de tiempo y desviacion estandar
# Obtenidos

print("\n")
print(" Quick Sort ", "%.2f" %PromQuickSort , " " , "%.2f" %DesvQuickSort)
print(" MergerSort ", "%.2f" %PromMergerSort , " " , "%.2f" %DesvMergerSort)
print(" Comp Sort ", "%.2f" %PromCombSort , " " , "%.2f" %DesvCombSort)
print(" Odd-even Sort ", "%.2f" %PromOddEvenSort , " " , "%.2f" %DesvOddEvenSort)
print(" Gnome Sort ", "%.2f" %PromGnomeSort , " " , "%.2f" %DesvGnomeSort)
print("\n")
print(" Conv. Arbol ", "%.2f" %PromArbol , " " , "%.2f" %DesvArbol)
print(" Busq. Arbol ", "%.2f" %PromBuscar , " " , "%.2f" %DesvBuscar)
