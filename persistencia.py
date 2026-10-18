"""
persistencia.py
Guarda y carga los expedientes en un archivo CSV.
"""

import csv
import os

# Campos de cada expediente (ahora incluye "caso")
CAMPOS = ["codigo", "dni", "nombre", "tipo_documento", "descripcion", "caso", "fecha"]

CARPETA_DATOS = "datos"
RUTA_ARCHIVO = os.path.join(CARPETA_DATOS, "expedientes.csv")


def guardar_expedientes(expedientes, ruta=RUTA_ARCHIVO):
    """Guarda toda la lista de expedientes en el CSV."""
    carpeta = os.path.dirname(ruta)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=CAMPOS)
        escritor.writeheader()
        for expediente in expedientes:
            escritor.writerow(expediente)

    return True


def cargar_expedientes(ruta=RUTA_ARCHIVO):
    """Carga los expedientes del CSV. Si no existe, devuelve lista vacia."""
    expedientes = []

    if not os.path.exists(ruta):
        return expedientes

    with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            expedientes.append(dict(fila))

    return expedientes
