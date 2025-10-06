import re

meses = {
    'Ene': '01', 'Feb': '02', 'Mar': '03', 'Abr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Ago': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dic': '12',
    'Enero': '01', 'Febrero': '02', 'Marzo': '03', 'Abril': '04', 'Mayo': '05', 'Junio': '06',
    'Julio': '07', 'Agosto': '08', 'Septiembre': '09', 'Octubre': '10', 'Noviembre': '11', 'Diciembre': '12'
}

texto = input("Ingresa el texto: ")

patron1 = r'\b(\d{2})/(\d{2})/(\d{4})\b'
patron2 = r'\b(\d{4})-(\d{2})-(\d{2})\b'
patron3 = r'\b(\d{2})-([A-Za-z]{3})-(\d{4})\b'
patron4 = r'\b([A-Za-z]+)\s+(\d{1,2}),\s*(\d{4})\b'

fechas_encontradas = []

fechas1 = re.findall(patron1, texto)
for fecha in fechas1:
    fechas_encontradas.append(('DD/MM/YYYY', f"{fecha[0]}/{fecha[1]}/{fecha[2]}", f"{fecha[2]}-{fecha[1]}-{fecha[0]}"))

fechas2 = re.findall(patron2, texto)
for fecha in fechas2:
    fechas_encontradas.append(('YYYY-MM-DD', f"{fecha[0]}-{fecha[1]}-{fecha[2]}", f"{fecha[0]}-{fecha[1]}-{fecha[2]}"))

fechas3 = re.findall(patron3, texto)
for fecha in fechas3:
    mes = meses.get(fecha[1].title(), '00')
    fechas_encontradas.append(('DD-MMM-YYYY', f"{fecha[0]}-{fecha[1]}-{fecha[2]}", f"{fecha[2]}-{mes}-{fecha[0]}"))

fechas4 = re.findall(patron4, texto)
for fecha in fechas4:
    mes = meses.get(fecha[0].title(), '00')
    dia = fecha[1].zfill(2)
    fechas_encontradas.append(('Mes DD, YYYY', f"{fecha[0]} {fecha[1]}, {fecha[2]}", f"{fecha[2]}-{mes}-{dia}"))

print("Fechas encontradas y convertidas:")
for i, (formato, original, estandar) in enumerate(fechas_encontradas, 1):
    print(f"- Formato original: {original} → Estándar: {estandar}")