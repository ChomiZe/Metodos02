#Count()se encarga de buscar una subcadena en particular
#requiere argumentos: 1 substring 2 int 3 int

var1= 'Mi mamá me mima'
contador = 0

print(var1.center(40, '-'))
contador = var1.count('M')
print(f'\nLa letra M se encontro {contador} veces en la cadena: {var1}')

contador = var1.count('m')
print(f'\nLa letra m se encontro {contador} veces en la cadena: {var1}')

contador = var1.count('mamá')
print(f'\nLa palabra mamá se encontro {contador} veces en la cadena: {var1}')

contador = var1.count('me mima')
print(f'\nLa frase me mima se encontro {contador} veces en la cadena: {var1}')

contador = var1.count('m', 13)
print(f'\nLa letra m se encontro {contador} veces en la cadena, desde la posicion 13: {var1}')


