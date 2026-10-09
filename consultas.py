"""
consultas.py
Integrante 4 - Archivos, Búsqueda y Ordenamiento
Proyecto: Mesa de Partes Digital

Responsable de buscar un expediente por su código y de mostrar
el listado de expedientes registrados.
"""

from persistencia import cargar_expedientes


def buscar_expediente(codigo, expedientes=None):
    """
    Busca un expediente por su código.
    Si no se le pasa la lista de expedientes, la carga del archivo.
    Devuelve el expediente (diccionario) si lo encuentra, o None
    si no existe.
    """
    if expedientes is None:
        expedientes = cargar_expedientes()

    codigo_buscado = codigo.strip().upper()

    for expediente in expedientes:
        if expediente["codigo"].strip().upper() == codigo_buscado:
            return expediente

    return None  # No encontrado


def mostrar_expedientes(expedientes=None):
    """
    Muestra en pantalla el listado de expedientes de forma ordenada
    y fácil de leer. Si no se pasa la lista, la carga del archivo.
    """
    if expedientes is None:
        expedientes = cargar_expedientes()

    if not expedientes:
        print("No hay expedientes registrados todavía.")
        return

    print("=" * 70)
    print(f"{'CODIGO':15}{'NOMBRE':25}{'TIPO DOC.':20}{'FECHA':10}")
    print("=" * 70)
    for exp in expedientes:
        print(
            f"{exp['codigo']:15}{exp['nombre'][:24]:25}"
            f"{exp['tipo_documento'][:19]:20}{exp['fecha']:10}"
        )
    print("=" * 70)


def mostrar_todos(expedientes=None):
    """Alias usado por main.py (RF-07): muestra el listado completo."""
    mostrar_expedientes(expedientes)


def mostrar_detalle_expediente(expediente):
    """Muestra todos los campos de un expediente encontrado (RF-05)."""
    print("-" * 50)
    print(f"Código         : {expediente['codigo']}")
    print(f"DNI            : {expediente['dni']}")
    print(f"Nombre         : {expediente['nombre']}")
    print(f"Tipo documento : {expediente['tipo_documento']}")
    print(f"Descripción    : {expediente['descripcion']}")
    print(f"Fecha          : {expediente['fecha']}")
    print("-" * 50)


# --- Prueba rápida de este módulo por separado ---
if __name__ == "__main__":
    mostrar_expedientes()

    codigo_prueba = input("Ingrese un código a buscar: ")
    resultado = buscar_expediente(codigo_prueba)

    if resultado:
        print("Expediente encontrado:")
        print(resultado)
    else:
        print(f"No existe ningún expediente con el código '{codigo_prueba}'.")
