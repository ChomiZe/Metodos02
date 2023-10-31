#Desarrollar un programa que invierta una cadena de caracteres y asu ves esta cadena debera de ser ingresada desde teclado
#requerimientos
#utilizar ciclo bucle for
#no se permite modificar la cadena de caracteres original

string = input("Ingrese una frase para invertirlo: ")
string_reversed = ""

for var1 in string:
    string_reversed = var1 + string_reversed

print(f"Frase invertida: {string_reversed}")
