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
    print("Tama-o de los elementos ", Tam)

    for i in range(NumPalabras):

        x = id_generator ( Tam ,  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
        string.append(x)

    return string

#------------------------------QUICK SORT----------------------------#

def QuickSort(array,izq,der):
    
    if (izq > der):
        pass

    elif (izq < der):
        pivote = Particionar(array,izq,der)
        QuickSort(array,izq,pivote - 1)
        QuickSort(array,pivote+1,der)

def Particionar(array,izq,der):

    pivote = array[der]
    bottom = izq - 1
    top = der

    done = False

    while (not done):

        while not done:
            bottom += 1

            if bottom == top:
                done = True
                break

            if array[bottom] > pivote:
                array[top] = array[bottom]
                break

        while not done:
            top -= 1

            if top == bottom:                  
                done = True                    
                break

            if array[top] < pivote:              
                array[bottom] = array[top]      
                break

    array[top] = pivote
    return top

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

def CombSort(Arreglo):

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

