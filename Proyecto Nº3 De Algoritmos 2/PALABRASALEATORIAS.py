# Genera palabras alegatorias


import string
import random

def id_generator ( size, chars = string.ascii_uppercase): 
   return  '' . join ( random . choice ( chars )  for _ in range ( size ))

string = []

for i in range(10):

    x = id_generator ( 3 ,  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" )
    print(x)
    string.append(x)
    print(string)
