# Comb Sort

import time

def CombSort(Arreglo):

    tiempo_inicial = time.time()
    print("TIEMPO INICIAL ", tiempo_inicial)
    
    gap = len ( Arreglo )
    shrink = 1.3
    swaps = True

    while (gap > 1 or (swaps)):
        
        gap = int(gap/shrink)
        swaps = False
    
        for i in range(len(Arreglo) - gap):
            if Arreglo[ i ] > Arreglo[ i + gap] :
                Temp = Arreglo[ i ] 
                Arreglo[ i ] = Arreglo[ i + gap ]
                Arreglo[ i + gap] = Temp
                swaps = True
    
    tiempo_real = time.time()
    tiempo_final = time.time() - tiempo_inicial
    print("TIEMPO REAL ", tiempo_real)
    print("TIEMPO FINAL ", tiempo_final)
    print(Arreglo)

Arreglo = [5,4,2,1,3]
CombSort(Arreglo)
