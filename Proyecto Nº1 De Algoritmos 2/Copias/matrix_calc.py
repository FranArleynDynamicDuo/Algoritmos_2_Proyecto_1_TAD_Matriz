# Proyecto #1 Definiciones y operaciones
#
# Nombre: Arleyn Goncalves, Carnet: 10-10290
# Nombre: Francisco Sucre, Carnet: 10-10717

class Matriz():


#-----------------------------CREAR----------------------------------#

   def crear(self,fi,co):

      # Crea la matriz vacia, donde fi es el numero de filas y
      # co es el numero de columnas y comp son los componentes que
      # contiene la matriz

      self.fila = fi
      self.columna = co
      self.comp = []

      for i in range(fi):

         self.comp.append([0]*co)

#-----------------------------Leer----------------------------------#

   def leer(self,NombreTexto):

      # Extrae una matriz de un archivo .txt y la guarda en una
      # variable

      data = open(NombreTexto,'r')

      medidaJuntas = data.readline()

      medidaSep = medidaJuntas.split()

      filaT = int(medidaSep[0])

      columnaT = int(medidaSep[1])

      self.crear(filaT,columnaT)

      print(self.fila)
      print(self.columna)

      
      iter1 = 0

      for line in data:

         lineas = line.split()

         for iter2 in range(self.columna):

            self.comp[iter1][iter2] = int(lineas[iter2])

         iter1 = iter1 + 1

      print(self.comp)

#------------------------------OBTENER-------------------------------#

   def obtener(self,fi,co):

      # Procedimiento donde entra en numero de la fila nombrado como
      # fi y el numero de la columna nombrado como co, y se muestra
      # que valor se encuentra en dicha posicion

      valor = self.comp[fi - 1][co - 1]
      print(" El valor buscado es: ", valor)
      print()
      return valor

#------------------------------COLOCAR-------------------------------#

   def colocar(self,fi,co,ing):

      # Procedimiento donde fi es la posicion de la fila y co es la
      # posicion de la columna y ing es el valor que se va a ingresar
      # en dicha posicion

      self.comp[fi - 1][co - 1] = ing
      print(" La matriz queda :", self.comp)
      print()
      return self

#-------------------------------SUMA---------------------------------#

   def sumar(self,N,F):

      # Procedimiento en donde se suman dos matrices

      if (self.fila != N.fila) or (F.columna != N.columna):

         print("Las dimensiones de las matrices deben ser iguales")

      else:

         for i in range(self.fila):

            for j in range(self.columna):

               self.comp[i][j] = N.comp[i][j] + F.comp[i][j]
               Ms = self.comp

         print(" El resultado de la suma de dos matrices", Ms)
         print()
         return Ms

#-------------------MULTIPLICACION DE UN ESCALAR---------------------#

   def multiplicar(self,N,F):

      # Procedimiento en donde se multiplican dos matrices.

      Mx = Matriz()
      Mx.crear(N.fila,F.columna)

      for i in range(N.fila):

         for j in range(F.columna):

            for k in range(N.columna):

               Mx.comp[i][j] = Mx.comp[i][j] + (N.comp[i][k]*F.comp[k][j])

      print(" La multiplicacion de matrices es: ", Mx.comp)
      print()
      return Mx


#---------------------------TRASPUESTA-------------------------------#

   def trasponer(self,F):

      # Procedimiento donde se calcula la traspuesta de una matriz

      Mt = Matriz()
      Mt.crear(F.columna,F.fila)

      for i in range(F.columna):

         for j in range(F.fila):

            Mt.comp[i][j] = F.comp[j][i]

      print(" La traspuesta de la matriz es: ", Mt.comp)
      print()
      return Mt

#---------------------------MULTIPLICAR------------------------------#

   def multiplicar(self,N,F):

      # Procedimiento en donde se multiplican dos matrices.

      Mx = Matriz()
      Mx.crear(N.fila,F.columna)

      for i in range(N.fila):

         for j in range(F.columna):

            for k in range(N.columna):

               Mx.comp[i][j] = Mx.comp[i][j] + (N.comp[i][k]*F.comp[k][j])

      print(" La multiplicacion de matrices es: ", Mx.comp)
      print()
      return Mx

#---------------------------Pruebas----------------------------------#



M0 = Matriz()
M1 = Matriz()

M0.crear(2,4)
M1.crear(4,2) 
M0.colocar(0,0,1)
M0.colocar(0,1,1)
M0.colocar(0,2,1)
M0.colocar(0,3,1)
M0.colocar(1,0,1)
M0.colocar(1,1,1)
M0.colocar(1,2,1)
M0.colocar(1,3,1)

M1.colocar(0,0,1)
M1.colocar(0,1,1)
M1.colocar(1,0,1)
M1.colocar(1,1,1)
M1.colocar(2,0,1)
M1.colocar(2,1,1)
M1.colocar(3,0,1)
M1.colocar(3,1,1)
M0.multiplicar(M0,M1)



# Ojo: Haremos un matriz memoria que no va ha tener objetos
