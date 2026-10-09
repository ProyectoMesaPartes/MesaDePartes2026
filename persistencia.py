"""
persistencia.py
Integrante 4 - Archivos, Búsqueda y Ordenamiento
Proyecto: Mesa de Partes Digital

Responsable de guardar y cargar los expedientes de forma permanente
usando un archivo CSV como exige el desafío del curso.
"""

import csv
import os

# Campos acordados con el equipo (Integrante 3 define el registro,
# aquí solo se usan los mismos nombres para que coincidan)
CAMPOS = ["codigo", "dni", "nombre", "tipo_documento", "descripcion", "fecha"]

# Carpeta y archivo donde se guardan los datos
CARPETA_DATOS = "datos"
RUTA_ARCHIVO = os.path.join(CARPETA_DATOS, "expedientes.csv")


def guardar_expedientes(expedientes, ruta=RUTA_ARCHIVO):
    """
    Guarda la lista completa de expedientes en el archivo CSV.
    Sobrescribe el archivo cada vez que se llama (se usa después
    de registrar, editar o eliminar un expediente).
    """
    # Crea la carpeta "datos" si todavía no existe
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
    """
    Carga los expedientes guardados en el archivo CSV y los
    devuelve como una lista de diccionarios.
    Si el archivo todavía no existe (primera vez que se usa el
    programa), devuelve una lista vacía en vez de dar error.
    """
    expedientes = []

    if not os.path.exists(ruta):
        return expedientes

    with open(ruta, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            expedientes.append(dict(fila))

    return expedientes


# --- Prueba rápida de este módulo por separado ---
if __name__ == "__main__":
    prueba = [
        {
            "codigo": "EXP-2026-0001",
            "dni": "72845136",
            "nombre": "Maria Fernanda Quispe Rojas",
            "tipo_documento": "Solicitud de constancia",
            "descripcion": "Constancia de no adeudo municipal",
            "fecha": "02/10/2026",
        }
    ]
    guardar_expedientes(prueba)
    print("Guardado. Ahora cargando desde el archivo...")
    cargados = cargar_expedientes()
    print(cargados)
