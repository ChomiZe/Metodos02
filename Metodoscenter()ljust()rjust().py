#Metodos center() ljust() rjust() para alienear textos
#estos metodos trabajan con argumentos, siempre debe ser un nuemro entero,
#este numero debera ser mayor a la string que esta en tu variable

#Center
string ="Menú"

print('METODOS CENTER, LJUST, RJUST')
print (string.center(10, '♦')) #si solo queremos espacios no es necesario poner el caracter solo el numero
print (string.center(10))

#ljust()
print (string.ljust(10, '♦'))
print (string.ljust(10))

#rjust()
print (string.rjust(10, '♦'))
print (string.rjust(10))