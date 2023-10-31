#Metodos istitle(retorna un valor booleano(true false) revisa si las primeras letras estan en mayusculas y el resto en minuscula)
#title(Hace que inicie cada palabra en mayuscula y el resto en minuscula)

name = input("Nombre: ")
lastname = input("Apellido: ")
full_name = f"{name} {lastname}"

print()
print(f"El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Aplicando el metodo title(): {full_name.title()}")
print(f"Volvemos a imprimir el nombre: {full_name}")

#MODIFICA EL CONTENIDO EL CONTENIDO DE LA VARIABLE FULL_NAME
print()
full_name = full_name.title()
print(f"El formato del metodo title() se ha aplicado?: {full_name.istitle()}")
print(f"Se ha aplicado del metodo title() de manera permanente: {full_name}")