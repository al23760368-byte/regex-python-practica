import re

texto = input("Ingresa el texto: ")

patron = r'(https?://)?(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(/[a-zA-Z0-9-./?=]*)?'

urls = re.findall(patron, texto)

contador = 1
for url in urls:
    protocolo = url[0] if url[0] else 'No especificado'
    dominio = url[2]
    ruta = url[3] if url[3] else 'No especificada'
    
    if protocolo == 'No especificado' and not url[1]:
        dominio_completo = dominio
    else:
        dominio_completo = (url[1] or '') + dominio
    
    print(f"URL {contador}: {protocolo}{dominio_completo}{ruta}")
    print(f"  Protocolo: {protocolo.replace('://', '')}")
    print(f"  Dominio: {dominio_completo}")
    if ruta != 'No especificada':
        print(f"  Ruta: {ruta}")
    print()
    contador += 1