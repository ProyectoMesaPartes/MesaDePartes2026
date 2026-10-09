"""
validaciones.py
Integrante 3 - Python: Registro y Validación
Proyecto: Mesa de Partes Digital

Funciones de validación de cada campo del expediente.
Cada función devuelve una tupla (es_valido, mensaje):
  - es_valido: True si el dato es correcto, False si no.
  - mensaje:   texto para mostrar al usuario cuando hay error ("" si es válido).
"""

import re
from datetime import datetime

# Formato del código: EXP-AAAA-NNNN  (ej. EXP-2026-0001)
PATRON_CODIGO = re.compile(r"^EXP-\d{4}-\d{4}$")


def validar_codigo(codigo, expedientes=None):
    """RF-03: el código no puede estar vacío, debe tener el formato
    EXP-AAAA-NNNN y no debe repetirse en la lista de expedientes."""
    codigo = codigo.strip().upper()

    if codigo == "":
        return False, "El código no puede estar vacío."

    if not PATRON_CODIGO.match(codigo):
        return False, "Formato inválido. Use EXP-AAAA-NNNN (ej. EXP-2026-0001)."

    if expedientes:
        for exp in expedientes:
            if exp["codigo"].strip().upper() == codigo:
                return False, f"El código {codigo} ya existe (duplicado)."

    return True, ""


def validar_dni(dni):
    """RF-04: el DNI debe tener exactamente 8 dígitos numéricos."""
    dni = dni.strip()

    if dni == "":
        return False, "El DNI no puede estar vacío."

    if not dni.isdigit():
        return False, "El DNI solo debe contener números."

    if len(dni) != 8:
        return False, "El DNI debe tener exactamente 8 dígitos."

    return True, ""


def validar_nombre(nombre):
    """RF-02: el nombre no puede estar vacío y no debe contener números."""
    nombre = nombre.strip()

    if nombre == "":
        return False, "El nombre no puede estar vacío."

    for caracter in nombre:
        if caracter.isdigit():
            return False, "El nombre no debe contener números."

    return True, ""


def validar_tipo_documento(tipo):
    """RF-02: el tipo de documento no puede estar vacío."""
    if tipo.strip() == "":
        return False, "El tipo de documento no puede estar vacío."
    return True, ""


def validar_descripcion(descripcion):
    """RF-02: la descripción no puede estar vacía."""
    if descripcion.strip() == "":
        return False, "La descripción no puede estar vacía."
    return True, ""


def validar_fecha(fecha):
    """La fecha debe tener formato DD/MM/AAAA y ser una fecha real."""
    fecha = fecha.strip()

    if fecha == "":
        return False, "La fecha no puede estar vacía."

    try:
        datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        return False, "Fecha inválida. Use DD/MM/AAAA (ej. 02/10/2026)."

    return True, ""


# --- Prueba rápida de este módulo por separado ---
if __name__ == "__main__":
    print(validar_codigo("EXP-2026-0001"))
    print(validar_codigo(""))
    print(validar_dni("72845136"))
    print(validar_dni("123"))
    print(validar_fecha("31/02/2026"))
