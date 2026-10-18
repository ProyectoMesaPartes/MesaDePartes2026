"""
ordenamiento.py
Integrante 4 - Archivos, Búsqueda y Ordenamiento
Proyecto: Mesa de Partes Digital

Responsable de ordenar los expedientes según el criterio que
defina el equipo (por defecto: fecha). Se implementa el algoritmo
de ordenamiento burbuja de forma manual para evidenciar el uso de
estructuras de control, tal como pide el curso.
"""

from persistencia import cargar_expedientes

# Criterios de ordenamiento permitidos y a qué campo corresponden
CRITERIOS_VALIDOS = {
    "codigo": "codigo",
    "nombre": "nombre",
    "fecha": "fecha",
}


def ordenar_expedientes(expedientes=None, criterio="fecha", ascendente=True):
    """
    Ordena una copia de la lista de expedientes según el criterio
    indicado ("codigo", "nombre" o "fecha") usando el algoritmo de
    ordenamiento burbuja.
    No modifica la lista original ni el archivo.
    """
    if expedientes is None:
        expedientes = cargar_expedientes()

    if criterio not in CRITERIOS_VALIDOS:
        print(f"Criterio '{criterio}' no válido. Se usará 'fecha' por defecto.")
        criterio = "fecha"

    campo = CRITERIOS_VALIDOS[criterio]

    # Se trabaja sobre una copia para no alterar el orden original
    lista = expedientes.copy()
    n = len(lista)

    # Ordenamiento burbuja
    for i in range(n - 1):
        for j in range(n - 1 - i):
            valor_actual = lista[j][campo].strip().lower()
            valor_siguiente = lista[j + 1][campo].strip().lower()

            si_intercambia = (
                valor_actual > valor_siguiente
                if ascendente
                else valor_actual < valor_siguiente
            )

            if si_intercambia:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


# --- Prueba rápida de este módulo por separado ---
if __name__ == "__main__":
    ordenados = ordenar_expedientes(criterio="fecha")
    for exp in ordenados:
        print(exp["codigo"], "-", exp["fecha"], "-", exp["nombre"])
