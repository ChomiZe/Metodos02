#METODOS
#STARWITH()COMPRUEBA SI COMIENZA CON UNA SUBCADENA EN PARTICULAR
var1 = 'Diana se peina sola'
resultado = 0
starts_with = 'Ejemplo com startswith()'
print(f'\nstarts_with.rjust(50, "-")')
resultado = var1.startswith('D')
print(f'\n{var1} comienza con la subcadena D: {resultado}')

resultado = var1.startswith('d')
print(f'\n{var1} comienza con la subcadena d: {resultado}')

resultado = var1.startswith('Diana')
print(f'\n{var1} comienza con la subcadena Diana: {resultado}')

resultado = var1.startswith('se, 6')
print(f'\n{var1} comienza con la subcadena se desde la posicion 6: {resultado}')

resultado = var1.startswith('se, 6, 7')
print(f'\n{var1} comienza con la subcadena se desde la posicion 6 hasta la posicion 7: {resultado}')

resultado = var1.startswith('se, 100, 100')
print(f'\n{var1} comienza con la subcadena se desde la posicion 100 hasta la posicion 100: {resultado}')

resultado = var1.startswith('se, -4, -1')
print(f'\n{var1} comienza con la subcadena se desde la posicion -4 hasta la posicion -1: {resultado}')


#ENDWITH()COMPRUEBA SI TERMINA CON UNA SUBCADENA EN PARTICULAR
ends_with = 'Ejemplo con endswith()'
print(f'\nends_with.ljust(50, "-")')
resultado = var1.endswith('A')
print(f'\n{var1} Termina con la subcadena A: {resultado}')

resultado = var1.endswith('a')
print(f'\n{var1} Termina con la subcadena a: {resultado}')

resultado = var1.endswith('sola')
print(f'\n{var1} Termina con la subcadena sola: {resultado}')

resultado = var1.endswith('sola', 10)
print(f'\n{var1} Termina con la subcadena sola desde la posicion 10: {resultado}')

resultado = var1.endswith('s', 9, 14)
print(f'\n{var1} Termina con la subcadena s desde la posicion 9 hasta la posicion 14: {resultado}')

resultado = var1.endswith('s', 100, 100)
print(f'\n{var1} Termina con la subcadena s desde la posicion 100 hasta la posicion 100: {resultado}')

resultado = var1.endswith('s', -4, -2)
print(f'\n{var1} Termina con la subcadena s desde la posicion -4 hasta la posicion -4: {resultado}')









