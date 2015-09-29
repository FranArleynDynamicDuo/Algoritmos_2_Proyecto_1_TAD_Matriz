# Quick Sort

def QuickSort(array,izq,der):


    if (izq > der):
        pass

    elif (izq < der):
        pivote = Particionar(array,izq,der)
        QuickSort(array,izq,pivote - 1)
        QuickSort(array,pivote+1,der)

    return array

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
    
array = [4,5,1,2,3]
izq = 0
der = len(array)-1
print(QuickSort(array,izq,der))
