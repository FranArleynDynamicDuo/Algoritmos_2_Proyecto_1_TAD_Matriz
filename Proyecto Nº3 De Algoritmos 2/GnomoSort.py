# Gnome Sort

import time

def GnomeSort(Arreglo):

    tiempo_inicial = time.time()
    print("TIEMPO INICIAL ", tiempo_inicial)

    pos = 1

    while ( pos < len(Arreglo) ):

        if (Arreglo[pos] >= Arreglo[pos - 1]):

            pos += 1

        else:

            Temp = Arreglo[pos]
            Arreglo[pos] = Arreglo[pos - 1]
            Arreglo[pos - 1] = Temp

            if (pos > 1):

                pos -= 1

    tiempo_real = time.time()
    tiempo_final = time.time() - tiempo_inicial
    print("TIEMPO REAL ", tiempo_real)
    print("TIEMPO FINAL ", tiempo_final)
    print(Arreglo)

Arreglo = [5,4,2,1,3]
GnomeSort(Arreglo)
