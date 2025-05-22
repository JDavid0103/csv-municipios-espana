# csv-municipios-españa
Script de Python para generar un archivo csv de todos los municipios de España incluyendo su provincia y código postal. Datos obtenido de [codigospostales.com](https://www.codigospostales.com)

Descomprimir carpeta de códigos y dejarla en la raíz del proyecto, para una versión mas actualizada descarga el ultimo zip de codigospostales.com [aquí](https://www.codigospostales.com/descarga.html)

Bibliotecas usadas:
 - os
 - csv
 - re

Ejecución:
```
python -m venv venv
```
```
.\venv\scripts\activate
```
```
python export_csv.py
```
