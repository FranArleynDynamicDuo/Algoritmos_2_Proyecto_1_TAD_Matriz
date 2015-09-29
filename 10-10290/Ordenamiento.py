# ORDENACION
# Arleyn Goncalves 10-10290
# Francisco Sucre 10-10717

import string
import random

#--------------------------PALABRAS ALEATORIAS-----------------------#

# Crea un arreglo con elementos aleatorios de tipo string

def id_generator ( size, chars = string.ascii_uppercase): 
   return  '' . join ( random . choice ( chars )  for _ in range ( size ))

def StringAleatorias(NumPalabras):

    string = []
    Tam = random.choice(range(1,1001))

    for i in range(NumPalabras):

        x = id_generator ( Tam ,  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
        string.append(x)

    return string

#------------------------------QUICK SORT----------------------------#

def QuickSort(array,izq,der):

    if (der - izq < 2):
        pass

    elif (der - izq >= 2):

        pivote = particionar(array,izq,der)
        QuickSort(array,izq,pivote)
        QuickSort(array,pivote+1,der)

    return array

def particionar(array,izq,der):

    i = izq + 1
    j = izq + 1

    while (j != der):

        if (array[j] <= array[izq]):

            Temp = array[i]
            array[i] = array[j]
            array[j] = Temp
            i += 1

        elif (array[j] > array[izq]):

            pass

        j += 1

    Temp = array[izq]
    array[izq] = array[i-1]
    array[i-1] = Temp
    pivote = i-1

    return pivote

#-----------------------------MERGER SORT----------------------------#

def mezclar(array,izq,med,der):
    
    barray = [None]*(der-izq + 1)
    i = izq
    j = med 
    k = 0

    while (i < med) and (j < der):

        if array[i] <= array[j]:
            
            barray[k] = array[i]
            i = i + 1
            
        elif array[i] > array[j]:
        
            barray[k] = array[j]
            j = j + 1

        k = k + 1
    
    while (i < med):
    
        barray[k] = array[i]
        i = i + 1
        k = k + 1

    while j < der: 
        
        barray[k] = array[j]
        j = j + 1
        k = k + 1
       
    k = 0

    while k < (der - izq):

        array[izq + k] = barray[k]
        k = k + 1

    return array

def MergeSor(array,izq,der):
    
    if (der - izq) < 2:
        pass
    
    elif der - izq >= 2:
        
        med = ((izq + der) // 2)
        array = MergeSor(array,izq,med)
        array = MergeSor(array,med,der)
        mezclar(array,izq,med,der)

    return array 
   
#------------------------------COMB SORT-----------------------------#

def CombSort(arreglo):

    gap = len(arreglo)
    shrink = 1.3
    swap = False

    while gap != 1 or swap == True:
        gap = int(gap/shrink)

        if gap < 1 :
            gap = 1

        i = 0
        swap = False

        while i + gap < len(arreglo) :
            if arreglo[i] > arreglo[ i + gap]:
                Temp = arreglo[i]
                arreglo[i] = arreglo[i+gap]
                arreglo[i+gap] = Temp
                swap = True
            i += 1

#--------------------------ODD EVEN SORT-----------------------------#

def Oddevensort(Arreglo):

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

#-----------------------------GNOME SORT-----------------------------#

def GnomeSort(Arreglo):

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

