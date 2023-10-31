#Metodo strip(), final e inicial de cadena
#\t = tabulacion \n = salto de linea

cadena = '\tHola Romina\n'
print(cadena)

cadena = cadena.strip() #elimino la tabaulacion y el salto de linea
print(cadena)

cadena = cadena.strip('i nHo a \t \n') 
print(cadena)