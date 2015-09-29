# Proyecto #1 programa 
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

import matrix_calc

instrucciones = open('instrucciones.txt', 'r')
datos = open('datos.txt', 'r')
salida = open('salida.txt','w')
salida = open('salida.txt', 'a')
i = 0
M = [0]*30

for line in instrucciones:

        oracion = line.split()
        
        if (line.startswith( 'READ' )):

            M[i] = matrix_calc.Matriz()
            
            M[i].leer(oracion[1])

            i = i + 1

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[0].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(str(M[0].comp))
            salida.write('\n')

            for raya in range(M[0].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 


        elif (line.startswith( 'NEW' )):
            
            salida.write()
            
            M[i] = matrix_calc.Matriz()

            M[i].crear(oracion[1],oracion[2])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
            
            """

            for raya in range():

                salida.write('-')

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')
                
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """
            
            i = i +1
            
        elif (line.startswith( 'GET' )):

            M[i] = matrix_calc.Matriz()

            M[0].obtener(int(oracion[2]),int(oracion[3]))

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range():

                salida.write('-')

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 


        elif (line.startswith( 'SET' )):

            M[i] = matrix_calc.Matriz()

            M[i].colocar(oracion[1],oracion[2],oracion[3])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range():

                salida.write('-')           

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """         

        elif (line.startswith( 'ADD' )):

            M[i] = matrix_calc.Matriz()

            M[i] = M[i].sumar(oracion[1],oracion[2])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range():

                salida.write('-')           

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            i = i +1

        elif (line.startswith( 'SCALAR' )):

            M[i] = matrix_calc.Matriz()

            M[i] = M[i].mult_escalar(oracion[1],oracion[2])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range():

                salida.write('-')           

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            i = i +1

        elif (line.startswith( 'TRANSPOSE' )):

            #M[i] = matrix_calc.Matriz()

            M[1] = matrix_calc.Matriz()

            M[1].crear(M[0].columna,M[0].fila)
             
            M[1] = M[1].trasponer(M[0])

            print(M[1].comp)

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[1].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(str(M[1].comp))
            salida.write('\n')

            for raya in range(M[1].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            i = i +1            

        elif (line.startswith( 'MULTIPLY' )):

            M[2] = matrix_calc.Matriz()

            M[2].crear(M[0].fila,M[1].columna)
            
            #M[i] = matrix_calc.Matriz()
            
            #M[2] = M[2].multiplicar(oracion[1],oracion[2])

            M[2] = M[2].multiplicar(M[0],M[1])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range():

                salida.write('-')           

            for raya in range(M[i].columna):

                salida.write('-')

            salida.write('\n')
            salida.write('La Matriz creada es: ')    
            salida.write('\n')
            salida.write(M[i])
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            i = i +1
            
        else:

            pass

