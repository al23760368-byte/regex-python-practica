import re

def validar_email(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, email):
        return True
    else:
        return False

print("Validador de Correos Electronicos")
print("----------------------------------")

print("Prueba tu email:")
while True:
    prueba = input("Ingresa un email (o 'salir' para terminar): ")
    if prueba.lower() == 'salir':
        break
    if validar_email(prueba):
        print("-> Email VALIDO")
    else:
        print("-> Email INVALIDO")