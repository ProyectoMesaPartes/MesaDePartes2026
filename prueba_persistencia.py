"""
prueba_persistencia.py
Integrante 4 - Archivos, Búsqueda y Ordenamiento
Proyecto: Mesa de Partes Digital

Prueba crítica pedida en el plan del equipo:
Registrar expediente -> Guardar archivo -> Cerrar programa
-> Abrir programa -> Cargar archivo -> Comprobar datos

Aquí se simula el "cerrar y abrir el programa" guardando primero,
y luego cargando en una variable completamente nueva.
"""

import os

from persistencia import guardar_expedientes, cargar_expedientes
from consultas import buscar_expediente, mostrar_expedientes
from ordenamiento import ordenar_expedientes

RUTA_PRUEBA = os.path.join("datos", "prueba_expedientes.csv")


def ejecutar_prueba():
    print("\n--- PASO 1: Registrar expedientes de prueba ---")
    expedientes_originales = [
        {
            "codigo": "EXP-2026-0001",
            "dni": "72845136",
            "nombre": "Maria Fernanda Quispe Rojas",
            "tipo_documento": "Solicitud de constancia",
            "descripcion": "Constancia de no adeudo municipal",
            "fecha": "02/10/2026",
        },
        {
            "codigo": "EXP-2026-0002",
            "dni": "71234567",
            "nombre": "Luis Alberto Torres Vega",
            "tipo_documento": "Reclamo",
            "descripcion": "Reclamo por ruido de obra cercana",
            "fecha": "01/10/2026",
        },
    ]
    print(f"Se registraron {len(expedientes_originales)} expedientes en memoria.")

    # Se usa un archivo aparte para NO sobrescribir datos/expedientes.csv real
    print("\n--- PASO 2: Guardar en archivo (datos/prueba_expedientes.csv) ---")
    guardar_expedientes(expedientes_originales, RUTA_PRUEBA)
    print("Guardado correctamente.")

    print("\n--- PASO 3: Simular cierre del programa ---")
    del expedientes_originales
    print("Variable eliminada de memoria (simula cerrar el programa).")

    print("\n--- PASO 4: 'Reabrir' el programa y cargar desde archivo ---")
    expedientes_cargados = cargar_expedientes(RUTA_PRUEBA)

    print("\n--- PASO 5: Comprobar que los datos persistieron ---")
    if len(expedientes_cargados) == 2:
        print("OK: se recuperaron los 2 expedientes guardados.")
    else:
        print("ERROR: no coincide la cantidad de expedientes esperada.")

    mostrar_expedientes(expedientes_cargados)

    print("\n--- PASO 6: Probar búsqueda por código ---")
    resultado = buscar_expediente("EXP-2026-0002", expedientes_cargados)
    print("Encontrado:" if resultado else "No encontrado:", resultado)

    print("\n--- PASO 7: Probar ordenamiento por fecha ---")
    ordenados = ordenar_expedientes(expedientes_cargados, criterio="fecha")
    for exp in ordenados:
        print(exp["fecha"], "-", exp["codigo"])

    # Limpieza: se borra el archivo temporal de la prueba
    os.remove(RUTA_PRUEBA)
    print("\nArchivo de prueba eliminado. Prueba finalizada.")


if __name__ == "__main__":
    ejecutar_prueba()
