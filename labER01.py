import re
import matplotlib.pyplot as plt

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, correo) is not None

validos = 0
invalidos = 0

with open('correos.txt', 'r') as f:
    for linea in f:
        linea = linea.strip()
        if re.match(r'^\d+\.\s+', linea):
            correo = re.sub(r'^\d+\.\s+', '', linea)
            if validar_correo(correo):
                validos += 1
            else:
                invalidos += 1

print("Correos validos:", validos)
print("Correos invalidos:", invalidos)

categorias = ['Validos', 'Invalidos']
cantidades = [validos, invalidos]

plt.bar(categorias, cantidades, color=['green', 'red'])
plt.ylabel('Cantidad')
plt.title('Correos Electronicos')
plt.show()