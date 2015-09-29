def mezclar(array,izq,med,der):
    
    barray = [None]*(der-izq + 1)
    i = izq
    j = med 
    k = 0

    print('Entrando al primer while')
    print()
    
    while (i < med) and (j < der):

        print('Control de variables, INICIO DE CICLO')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)

    # Factor de ordenamiento, donde se decide la posicion del elemento
    # arreglo[i] basado en su valor
    
        if array[i] <= array[j]:
        
            barray[k] = array[i]
            i = i + 1
            
        elif array[i] > array[j]:
        
            barray[k] = array[j]
            j = j + 1

        k = k + 1

        print('Control de variables, FINAL DE CICLO')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)
        
    print()
    print('Entrando al segundo while')
    print()
    
    while (i < med):

        print('Control de variables')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)
    
        barray[k] = array[i]
        i = i + 1
        k = k + 1

        print('Control de variables, FINAL DE CICLO')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)        
    print()        
    print('Entrando al tercer while')
    print()
    
    while j < der: 
        
        print('Control de variables')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)
        
        barray[k] = array[j]
        j = j + 1
        k = k + 1
        print('Control de variables, FINAL DE CICLO')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)

        
    k = 0
    print()   
    print('Entrando al 4to while')
    print()

    #Insertar los elementos de Barray(previamente ordenados) al
    #arreglo original
    
    while k < (der - izq):

        print('Control de variables')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        array[izq + k] = barray[k]
        print('Array es: ',array)
        print('barray es: ',barray)
        
        k = k + 1
        print('Control de variables, FINAL DE CICLO')
        print()
        print('i es: ',i)
        print('j es: ',j)
        print('k es : ',k)
        print()
        print('Array es: ',array)
        print('barray es: ',barray)

    return array

def MergeSor(array,izq,der):
    
    if (der - izq) < 2:
        
        pass
    
    elif der - izq >= 2:
        
        med = ((izq + der) // 2)
        print('Antes de entrar en recursion med es: ',med)
        print('Empezaremos el mergesort utilizando ',izq,'como izq')
        print(med,'como med y ',der,'como der')
        print()
        array = MergeSor(array,izq,med)
        print()
        print('Antes de entrar en recursion med es: ',med)
        print('Empezaremos el mergesort utilizando ',izq,'como izq')
        print(med,'como med y ',der,'como der')
        print()
        array = MergeSor(array,med,der)
        mezclar(array,izq,med,der)

    return array    

array = [12,23,625,45,267,13,2,51,31,582,432,1,57,746,632,252]
derecha = len(array)
array = MergeSor(array,0,derecha)
print()
print('El resultado final es: ',array)
