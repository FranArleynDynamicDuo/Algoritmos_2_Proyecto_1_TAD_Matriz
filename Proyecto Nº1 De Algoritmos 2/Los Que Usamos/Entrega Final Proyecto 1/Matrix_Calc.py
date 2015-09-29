# Proyecto #1 programa 
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

def matricesdeentrada(Oracion):

   #Proceso que lee el archivo y traduce cual matriz se usara para
   #los calculos

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

import matrix_def

#Abrimos todos nuestros archivos de texto necesarios, instrucciones
#nos dira que operaciones hacer, datos contiene alguna matriz que
#se extraera y salida es el archivo donde escribiremos todos los
#los resultados

instrucciones = open('instrucciones.txt', 'r')
datos = open('datos.txt', 'r')
salida = open('salida.txt','w')

#Inicializamos varias variables que necesitaremos incluyendo un
#arreglo para guardar las matrices que usen o calculen

i = 0
j = 0
w = 0
M = [0]*9

#Leemos instrucciones linea por linea el documento instrucciones
#y dependiendo de como comience cada linea, aplicaremos una de
#las operaciones ya definidas en matrix_def.py

for line in instrucciones:

        oracion = line.split()

#-----------------------------Leer-----------------------------------#
       
        if (line.startswith( 'READ' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido
            
            i = matricesdeentrada(oracion[2])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz
            
            M[i] = matrix_def.Matriz()

            #Extraemos la matriz del texto con el procedimiento ya
            #definido en matrix_def.py
            
            M[i].leer(oracion[1])

            #Imprimimos el resultado en el archivo salida.txt
            
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos

            for largo in range(M[i].fila):

                for digitos in range(M[i].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[i].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                             
            maximalinea = max(tamañolinea) + len(M[i].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt
            
            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
                
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#-----------------------------CREAR----------------------------------#
            
        elif (line.startswith( 'NEW' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido

            i = matricesdeentrada(oracion[2])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz
            
            M[i] = matrix_def.Matriz()

            #Creamos la matriz usando el procedimiento definido en
            #matrix_def, usando de parametros de entrada los datos
            #proporcionados en instrucciones.txt

            M[i].crear(oracion[1],oracion[2])

            #Imprimimos el resultado en el archivo salida.txt
            
            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """
            
            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos
            
            for largo in range(M[i].fila):

                for digitos in range(M[i].columna):

                    tamañolinea[largo] = tamañolinea[largo]
                    + len(str(M[i].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[i].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')
                      
            salida.write('\n')

            for raya in range(maximalinea - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#------------------------------OBTENER-------------------------------#
            
        elif (line.startswith( 'GET' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido

            i = matricesdeentrada(oracion[1])

            #Obtenemos el valor de la posicion que nos dice
            #el documento de instrucciones utilizando el
            #procedimiento definido previamente en
            #matrix_def.py

            M[i].obtener(int(oracion[2]),int(oracion[3]))

            #Imprimimos el resultado en el archivo salida.txt

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

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido

            i = matricesdeentrada(oracion[1])

            #Modificamos el valor de la posicion que nos dice
            #el documento de instrucciones utilizando el
            #procedimiento definido previamente en
            #matrix_def.py

            M[i].colocar(int(oracion[2]),int(oracion[3]),int(oracion[4]))

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """
            
            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos
            
            for largo in range(M[i].fila):

                for digitos in range(M[i].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[i].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[i].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[i].fila):
                             
                for col in range(M[i].columna):

                    salida.write(str(M[i].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(maximalinea - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

#-------------------------------SUMA---------------------------------#

        elif (line.startswith( 'ADD' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la primera matriz que se usara en
            #la operacion, usando el procedimiento previamente
            #definido

            i = matricesdeentrada(oracion[1])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la segunda matriz que se usara en
            #la operacion
            
            j = matricesdeentrada(oracion[2])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido
            
            w = matricesdeentrada(oracion[3])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz   
            
            M[w] = matrix_def.Matriz()

            #Usamos el procedimiento crear para convertir a la
            #variable que acabamos de asignar en una matriz con
            #las dimensiones necesarias para almacenar el
            #resultado de la operacion
  
            M[w].crear(M[i].fila,M[j].columna)

            #Sumamos las matrices que nos dice el documento
            #instrucciones

            M[w] = M[w].sumar(M[i],M[j])

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """
            
            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos

            for largo in range(M[w].fila):

                for digitos in range(M[w].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[w].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[w].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[w].fila):
                             
                for col in range(M[w].columna):

                    salida.write(str(M[w].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(maximalinea - 1):

                salida.write('-')

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#-------------------MULTIPLICACION DE UN ESCALAR---------------------#

        elif (line.startswith( 'SCALAR' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la primera matriz que se usara en
            #la operacion, usando el procedimiento previamente
            #definido

            i = matricesdeentrada(oracion[1])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido
            
            j = matricesdeentrada(oracion[2])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz

            M[j] = matrix_def.Matriz()

            #Usamos el procedimiento crear para convertir a la
            #variable que acabamos de asignar en una matriz con
            #las dimensiones necesarias para almacenar el
            #resultado de la operacion

            M[j].crear(M[i].fila,M[i].columna)

            #Calculamos la multiplicacion con nuestro procedimiento
            
            M[j] = M[i].mult_escalar(int(oracion[2]))

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """
            
            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos

            for largo in range(M[j].fila):

                for digitos in range(M[j].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[j].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[j].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[1].fila):
                             
                for col in range(M[1].columna):

                    salida.write(str(M[1].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')


            for raya in range(maximalinea - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 

#---------------------------TRASPUESTA-------------------------------#

        elif (line.startswith( 'TRANSPOSE' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la primera matriz que se usara en
            #la operacion, usando el procedimiento previamente
            #definido

            i = matricesdeentrada(oracion[1])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido
            
            j = matricesdeentrada(oracion[2])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz

            M[j] = matrix_def.Matriz()

            #Usamos el procedimiento crear para convertir a la
            #variable que acabamos de asignar en una matriz con
            #las dimensiones necesarias para almacenar el
            #resultado de la operacion

            M[j].crear(M[i].columna,M[i].fila)

            #Calcularemos la traspuesta con nuestro procedimiento
             
            M[j] = M[j].trasponer(M[i])

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo

            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos

            for largo in range(M[j].fila):

                for digitos in range(M[j].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[j].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[j].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[j].fila):
                             
                for col in range(M[j].columna):

                    salida.write(str(M[j].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range(maximalinea - 1):

                salida.write('-')

            salida.write('\n')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

#---------------------------MULTIPLICAR------------------------------#

        elif (line.startswith( 'MULTIPLY' )):

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la primera matriz que se usara en
            #la operacion, usando el procedimiento previamente
            #definido
            
            i = matricesdeentrada(oracion[1])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se encuentra la segunda matriz que se usara en
            #la operacion
            
            j = matricesdeentrada(oracion[2])

            #Buscamos el lugar en el arreglo de memoria de matrices
            #en que se guardara la matriz resultante del procedimiento
            #usando el procedimiento previamente definido
            
            w = matricesdeentrada(oracion[3])

            #Le Asignamos a la variable donde se guardara el
            #resultado la clase matriz

            M[w] = matrix_def.Matriz()

            #Usamos el procedimiento crear para convertir a la
            #variable que acabamos de asignar en una matriz con
            #las dimensiones necesarias para almacenar el
            #resultado de la operacion

            M[w].crear(M[i].fila,M[j].columna)

            #Calculamos la multiplicacion con nuestro procedimiento
            
            M[w] = M[w].multiplicar(M[i],M[j])

            #Imprimimos el resultado en el archivo salida.txt

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """

            #Inicializamos una secuencia para almacenar el tamaño
            #de todas las lineas del arreglo
            
            tamañolinea = [0]*20

            #Calculamos el tamaño de las lineas y lo almacenamos

            for largo in range(M[w].fila):

                for digitos in range(M[w].columna):

                    tamañolinea[largo] = tamañolinea[largo] + len(str(M[w].comp[largo][digitos]))

            #Comparamos todos los tamaños y tomamos el mas grande
                    
            maximalinea = max(tamañolinea) + len(M[w].comp[1])

            #Imprimimos los guiones y los resultados en salida.txt

            for raya in range((maximalinea) - 1):

                salida.write('-')

            salida.write('\n')
            
            for fil in range(M[w].fila):
                             
                for col in range(M[w].columna):

                    salida.write(str(M[w].comp[fil][col]))
                    salida.write(' ')

                salida.write('\n')

            for raya in range((maximalinea) - 1):

                salida.write('-')

            """

            Algoritmo para imprimir la respuesta de manera ordenada
             
            """ 
            
        else:

            pass

salida.close()

