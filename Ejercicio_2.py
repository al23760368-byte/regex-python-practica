import re

texto = input("Ingresa el texto: ")

patron = r'\(\d{3}\)\s?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{3}\s\d{3}\s\d{4}|\d{10}'

telefonos = re.findall(patron, texto)

print("Teléfonos encontrados:", telefonos)