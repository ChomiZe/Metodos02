#METODOS
#ISLOWER(Retorna el valor booleano(true or false))#LOWER() IDENTIFICA CADENAS DE MINUSCULAS PARA CONVERTIR A MAYUSCULA
string = input("Introduce un String: ")
print(f"\nTodas las letras estan en minuscula?: {string.islower()}")
string = string.lower()
print(f"String en minusculas: {string}")

#ISUPPER(retorna valor booleano)#UPPER() Indentifica cadeanas de caracateres en mayusculas para convertir en minusculas
print(f"\nTodas las letras estan en mayusculas: {string.isupper()} ?")
print(f"String en mayusculas: {string.upper()}")
print(f"\nString original: {string}")