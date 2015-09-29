# ODD-EVEN SORT

import time

def Oddevensort(Arreglo):

    tiempo_inicial = time.time()
    print("TIEMPO INICIAL ", tiempo_inicial)

    sort = False
    size = len(Arreglo)

    while (not sort):
        sort = True

        for i in range(1,size-1,2):

            if (Arreglo[i] > Arreglo[i+1]):
                
                Temp = Arreglo[i + 1]
                Arreglo[i + 1] = Arreglo[i]
                Arreglo[i] = Temp
                sort = False

        for i in range(0,size-1,2):

            if (Arreglo[i] > Arreglo[i+1]):

                Temp = Arreglo[i + 1]
                Arreglo[i + 1] = Arreglo[i]
                Arreglo[i] = Temp
                sort = False

    tiempo_real = time.time()
    tiempo_final = time.time() - tiempo_inicial
    print("TIEMPO REAL ", tiempo_real)
    print("TIEMPO FINAL ", tiempo_final)
    print(Arreglo)

Arreglo = [5,4,2,1,3]
Oddevensort(Arreglo)



            
