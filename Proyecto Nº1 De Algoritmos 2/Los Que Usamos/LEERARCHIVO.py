def leertxt():
   archi=open('instrucciones.txt','r')
   linea=archi.readline()
   while linea !="":
      print(linea)
      linea=archi.readline()
   archi.close()

def creartxt():
   archi=open('Salida.txt','w')
   archi.close()

def grabartxt():
   archi=open('Salida.txt','a')
   archi.write('Linea 1\n')
   archi.write('Linea 2\n')
   archi.write('Linea 3\n')
   archi.close()

leertxt()
creartxt()
grabartxt()

