"""
exportar_sql.py
Complemento de Base de Datos (Responsable BD: Aaron)
Proyecto: Mesa de Partes Digital

Convierte datos/expedientes.csv en sentencias INSERT de MySQL
(database/exportacion_expedientes.sql). Así la BD complementaria
se puede poblar con los datos reales del programa sin necesidad
de instalar ningún conector: solo se ejecuta el .sql generado.

Uso:  python exportar_sql.py
"""

import os
from datetime import datetime

from persistencia import cargar_expedientes

SALIDA = os.path.join("database", "exportacion_expedientes.sql")


def escapar(texto):
    """Escapa comillas simples y barras para SQL."""
    return texto.replace("\\", "\\\\").replace("'", "''")


def exportar():
    expedientes = cargar_expedientes()
    lineas = ["USE mesa_partes;", ""]

    for exp in expedientes:
        fecha_sql = datetime.strptime(exp["fecha"], "%d/%m/%Y").strftime("%Y-%m-%d")
        lineas.append(
            "INSERT INTO expedientes (codigo, dni, nombre, tipo_documento, descripcion, fecha) "
            f"VALUES ('{escapar(exp['codigo'])}', '{escapar(exp['dni'])}', "
            f"'{escapar(exp['nombre'])}', '{escapar(exp['tipo_documento'])}', "
            f"'{escapar(exp['descripcion'])}', '{fecha_sql}');"
        )

    with open(SALIDA, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(lineas) + "\n")

    print(f"Se exportaron {len(expedientes)} expediente(s) a {SALIDA}")


if __name__ == "__main__":
    exportar()
