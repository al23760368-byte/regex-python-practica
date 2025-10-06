import re

while True:
    contraseña = input("Ingresa tu contraseña (o 'salir' para terminar): ")
    
    if contraseña.lower() == "salir":
        break
    
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
    else:
        print("✓ Longitud mínima de 8 caracteres")

    if not re.search(r'[A-Z]', contraseña):
        print("La contraseña debe tener al menos una mayúscula")
    else:
        print("✓ Al menos una mayúscula")

    if not re.search(r'[a-z]', contraseña):
        print("La contraseña debe tener al menos una minúscula")
    else:
        print("✓ Al menos una minúscula")

    if not re.search(r'\d', contraseña):
        print("La contraseña debe tener al menos un número")
    else:
        print("✓ Al menos un número")

    if not re.search(r'[@$!%*?&#]', contraseña):
        print("La contraseña debe tener al menos un carácter especial (@$!%*?&#)")
    else:
        print("✓ Al menos un carácter especial")

    if len(contraseña) >= 8 and re.search(r'[A-Z]', contraseña) and re.search(r'[a-z]', contraseña) and re.search(r'\d', contraseña) and re.search(r'[@$!%*?&#]', contraseña):
        print("Contraseña VÁLIDA")
    else:
        print("Contraseña INVÁLIDA")
    
    print()