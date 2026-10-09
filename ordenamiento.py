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


def clave_orden(expediente, campo):
    """
    Devuelve el valor con el que se compara un expediente.
    Las fechas DD/MM/AAAA se convierten a AAAA/MM/DD para que el
    orden alfabético coincida con el orden cronológico real
    (si no, "15/01/2026" quedaría antes que "02/10/2025").
    """
    valor = expediente[campo].strip().lower()
    if campo == "fecha":
        partes = valor.split("/")
        if len(partes) == 3:
            valor = partes[2] + "/" + partes[1] + "/" + partes[0]
    return valor


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
            valor_actual = clave_orden(lista[j], campo)
            valor_siguiente = clave_orden(lista[j + 1], campo)

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
