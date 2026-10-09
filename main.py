"""
main.py
Integrante 5 - Integración y Pruebas
Proyecto: Mesa de Partes Digital - Municipalidad Distrital de Santa Aurora
Curso: Fundamentos de Programación (CIIN1205P)

Módulo central: carga los expedientes del CSV, muestra el menú y
conecta registro, validaciones, consultas, ordenamiento y persistencia.
"""

import sys

import registro as reg
import consultas as con
import ordenamiento as ord_mod
import persistencia as per


def mostrar_menu():
    """Muestra el menú principal en consola (RNF-01)."""
    print("\n=================================")
    print("   MESA DE PARTES DIGITAL")
    print("=================================")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Mostrar expedientes")
    print("4. Ordenar expedientes")
    print("5. Salir")
    print("=================================")


def pedir_criterio_orden():
    """Pregunta por qué campo y en qué sentido ordenar."""
    print("Ordenar por: 1) Fecha  2) Código  3) Nombre")
    opcion = input("Criterio [Enter = fecha]: ").strip()
    criterios = {"1": "fecha", "2": "codigo", "3": "nombre", "": "fecha"}
    criterio = criterios.get(opcion, "fecha")

    sentido = input("Sentido: 1) Ascendente  2) Descendente [Enter = ascendente]: ").strip()
    ascendente = sentido != "2"
    return criterio, ascendente


def ejecutar_sistema():
    """Bucle principal: carga, interacción con el usuario y guardado."""
    # Carga inicial desde el archivo (RF-09, RNF-03)
    expedientes = per.cargar_expedientes()
    print(f"Se cargaron {len(expedientes)} expediente(s) desde el archivo.")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
            nuevo = reg.registrar_expediente(expedientes)
            if nuevo:
                expedientes.append(nuevo)
                per.guardar_expedientes(expedientes)
                print("Expediente registrado y guardado permanentemente.")

        elif opcion == "2":
            print("\n--- BÚSQUEDA DE EXPEDIENTE ---")
            codigo = input("Ingrese el código (ej. EXP-2026-0001): ").strip()
            encontrado = con.buscar_expediente(codigo, expedientes)
            if encontrado:
                con.mostrar_detalle_expediente(encontrado)
            else:
                print(f"(x) No se encontró ningún expediente con el código '{codigo.upper()}'.")

        elif opcion == "3":
            print("\n--- LISTADO GENERAL DE EXPEDIENTES ---")
            con.mostrar_todos(expedientes)

        elif opcion == "4":
            print("\n--- ORDENAMIENTO DE EXPEDIENTES ---")
            if not expedientes:
                print("(x) No existen registros para ordenar.")
            else:
                criterio, ascendente = pedir_criterio_orden()
                ordenados = ord_mod.ordenar_expedientes(expedientes, criterio, ascendente)
                con.mostrar_todos(ordenados)

        elif opcion == "5":
            print("\nGuardando expedientes...")
            per.guardar_expedientes(expedientes)
            print("¡Sesión finalizada correctamente!")
            sys.exit()

        else:
            print("(x) Opción no válida. Ingrese un número entre 1 y 5.")


if __name__ == "__main__":
    ejecutar_sistema()
