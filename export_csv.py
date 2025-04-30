import os
import csv
import re

# https://www.codigospostales.com/descarga.html
ruta_script = os.path.dirname(os.path.abspath(__file__))
carpeta_codigos = os.path.join(ruta_script, "codigos")

nombres_especiales = {
  "Vitoria-Gasteiz": "Vitoria-Gasteiz",
  "Araba-Álava": "Álava (Araba)",
  "Alacant-Alicante": "Alicante (Alacant)",
  "Alcoi-Alcoy": "Alcoy (Alcoi)",
  "Elx-Elche": "Elche (Elx)",
  "Castelló-Castellón de la Plana": "Castellón de la Plana (Castelló)",
  "Donostia - San Sebastian": "San Sebastián (Donostia)",
  "Rivas-Vaciamadrid": "Rivas-Vaciamadrid",
  "Pamplona-Iruña": "Pamplona (Iruña)"
}

# Función para limpiar y transformar nombres (provincias y municipios)
def formatear_nombre(nombre):
  nombre = re.sub(r"\s*\(.*?\)", "", nombre).strip()  # Eliminar paréntesis
  if "," in nombre:
    partes = [parte.strip().capitalize() for parte in nombre.split(",")]
    nombre = f"{partes[1]} {partes[0]}"
  else:
    nombre = nombre.capitalize()
  return nombre

# Leer codciu.txt para mapear códigos a provincias
provincia_por_codigo = {}
with open(os.path.join(carpeta_codigos, "codciu.txt"), encoding="utf-8") as f:
  for linea in f:
    codigo = linea[:3]
    provincia_raw = linea[3:].strip()
    provincia_raw = re.sub(r"\s*\(.*?\)", "", provincia_raw).strip()  # Quitar paréntesis

    # Usar nombre especial si aplica
    provincia = nombres_especiales.get(provincia_raw, provincia_raw)

    # Reordenar si hay coma y no está en especiales
    if provincia == provincia_raw and "," in provincia_raw:
      partes = [parte.strip().capitalize() for parte in provincia_raw.split(",")]
      provincia = f"{partes[1]} {partes[0]}"

    provincia_por_codigo[codigo] = provincia

datos = []
codigos_excluir = {"01071", "01080"}

for archivo in os.listdir(carpeta_codigos):
  if archivo.endswith(".txt") and archivo != "codciu.txt":
    ruta_archivo = os.path.join(carpeta_codigos, archivo)
    codigo_provincia = archivo[:3]
    provincia = provincia_por_codigo.get(codigo_provincia, "Desconocida")

    with open(ruta_archivo, encoding="utf-8") as f:
      for linea in f:
        if ":" not in linea:
          continue
        cod_postal, municipio_raw = linea.strip().split(":", 1)
        if cod_postal in codigos_excluir:
          continue
        municipio = formatear_nombre(municipio_raw)
        datos.append((cod_postal, municipio, provincia))

with open(os.path.join(ruta_script, "export.csv"), "w", newline="", encoding="utf-8") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(["codigo_postal", "municipio", "provincia"])
  writer.writerows(datos)

print("CSV generado correctamente como 'export.csv'")