import requests
import pandas as pd
import sys

datos = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}
try:
    rta = requests.get("https://remoteok.com/api",headers=headers)
    rta.raise_for_status()
    empleos = rta.json()
except Exception as e:
    print(f'Error al ingresar en la web. Codigo de error: {e}')
    sys.exit(1) 


for empleo in empleos[1:]: #saltea el primer item (un aviso legal)
    try:        
        pos = empleo.get('position')
        com = empleo.get('company')
        tag = empleo.get('tags')
        salario_min = empleo.get('salary_min')
        salario_max = empleo.get('salary_max')
        location = empleo.get('location')
        fecha = empleo.get('date')

        datos.append({
            'Posicion': pos,
            'Compañia': com,
            'Tag': tag,
            'Salario mínimo': salario_min,
            'Salario máximo': salario_max,
            'Localización' : location,
            'Fecha': fecha
        })       
    except Exception as e:
        print(f'Error al obtener los datos.\nCodigo de Error: {e}')
        continue
if datos:
    tabla = pd.DataFrame(datos)
    tabla.to_csv('remote_ok.csv',index=False,encoding='utf-8-sig')
else:
    print('No se extrajeron datos')


