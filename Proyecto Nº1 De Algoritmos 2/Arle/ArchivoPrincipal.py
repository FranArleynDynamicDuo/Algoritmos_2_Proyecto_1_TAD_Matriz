# Proyecto #1 programa 
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

import matrix_calc

instrucciones = open('instrucciones.txt', 'r')
datos = open('datos.txt', 'r')
salida = open('salida.txt','w')

i = 0
j = 0
w = 0
M = [0]*20


def matricesdeentrada(Oracion):

   if Oracion == 'M0':

      i = 0
      return i

   elif Oracion == 'M1':

      i = 1
      return i

   elif Oracion == 'M2':
      
      i = 2
      return i

   elif Oracion == 'M3':

      i = 3
      return i

   elif Oracion == 'M4':
      
      i = 4
      return i
   
   elif Oracion == 'M5':

      i = 5
      return i

   elif Oracion == 'M6':

      i = 6
      return i

   elif Oracion == 'M7':

      i = 7
      return i

   elif Oracion == 'M8':
      
      i = 8
      return i

   elif Oracion == 'M9':

      i = 9
      return i


for line in instrucciones:

        oracion = line.split()

#-----------------------------Leer----------------------------------#
        
        if (line.startswith( 'READ' )):

            i = matricesdeentrada(oracion[2])

            M[i] = matrix_calc.Matriz()
            
            M[i].leer(oracion[1])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[i].columna + len(M[i].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(M[i].columna + len(M[i].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
                
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#-----------------------------CREAR----------------------------------#
            
        elif (line.startswith( 'NEW' )):

            i = matricesdeentrada(oracion[2])
            
            M[i] = matrix_calc.Matriz()

            M[i].crear(oracion[1],oracion[2])
            
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[i].columna + len(M[i].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')
                      
            salida.write('\n')

            for raya in range(M[i].columna):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#------------------------------OBTENER-------------------------------#
            
        elif (line.startswith( 'GET' )):

            i = matricesdeentrada(oracion[1])

            M[i].obtener(int(oracion[2]),int(oracion[3]))

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            salida.write('\n')

            salida.write(str(M[i].comp[int(oracion[2])][int(oracion[3])]))
                      
            salida.write('\n')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#------------------------------COLOCAR-------------------------------#

        elif (line.startswith( 'SET' )):

            i = matricesdeentrada(oracion[1])

            M[i].colocar(int(oracion[2]),int(oracion[3]),int(oracion[4]))

            print(M[i].comp)

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[i].columna + len(M[i].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(M[i].columna + len(M[i].comp[1]) - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

#-------------------------------SUMA---------------------------------#

        elif (line.startswith( 'ADD' )):

            i = matricesdeentrada(oracion[1])
            j = matricesdeentrada(oracion[2])
            w = matricesdeentrada(oracion[3])

            M[w] = matrix_calc.Matriz()
  
            M[w].crear(M[i].fila,M[j].columna)

            M[w] = M[w].sumar(M[i],M[j])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[w].columna + len(M[w].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[w].fila):
                             
                for col in range(M[w].columna):

                    salida.write(str(M[w].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(M[w].columna + len(M[w].comp[1]) - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#-------------------MULTIPLICACION DE UN ESCALAR---------------------#

        elif (line.startswith( 'SCALAR' )):

            i = matricesdeentrada(oracion[1])
            j = matricesdeentrada(oracion[2])

            M[j] = matrix_calc.Matriz()

            M[j] = M[i].mult_escalar(int(oracion[2]))

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[j].columna + len(M[j].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[1].fila):
                             
                for col in range(M[1].columna):

                    salida.write(str(M[1].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')


            for raya in range(M[j].columna + len(M[j].comp[1]) - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#---------------------------TRASPUESTA-------------------------------#

        elif (line.startswith( 'TRANSPOSE' )):
           
            i = matricesdeentrada(oracion[1])
            j = matricesdeentrada(oracion[2])

            M[j] = matrix_calc.Matriz()

            M[j].crear(M[i].columna,M[i].fila)
             
            M[j] = M[j].trasponer(M[i])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            for raya in range(M[j].columna + len(M[j].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[j].fila):
                             
                for col in range(M[j].columna):

                    salida.write(str(M[j].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(M[j].columna + len(M[j].comp[1]) - 1):

                salida.write('-')

            salida.write('\n')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

#---------------------------MULTIPLICAR------------------------------#

        elif (line.startswith( 'MULTIPLY' )):

            i = matricesdeentrada(oracion[1])
            j = matricesdeentrada(oracion[2])
            w = matricesdeentrada(oracion[3])

            M[w] = matrix_calc.Matriz()

            M[w].crear(M[i].fila,M[j].columna)
            
            M[w] = M[w].multiplicar(M[i],M[j])

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

            
            tamañolinea = [0]*20

            for largo in range(M[w].fila):

                for digitos in M[w].comp[largo]:

                    tamañolinea[largo] = tamañolinea[largo] + len(str(digitos)) - 1


            maximalinea = max(tamañolinea)

            print('probando maxima linea, maxima linea es : ', maximalinea)

            #M[w].columna + len(M[w].comp[1])

            for raya in range((maximalinea) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[w].fila):
                             
                for col in range(M[w].columna):

                    salida.write(str(M[w].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(M[w].columna + len(M[w].comp[1]) - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 
            
        else:

            pass

salida.close()

