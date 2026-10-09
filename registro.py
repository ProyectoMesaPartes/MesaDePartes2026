"""
registro.py
Integrante 3 - Python: Registro y Validación
Proyecto: Mesa de Partes Digital

Solicita los datos del expediente por teclado, valida cada campo
(repitiendo la pregunta hasta que sea correcto) y devuelve el
expediente como diccionario con los mismos campos que usa el CSV.
"""

from datetime import date

import validaciones as val


def _pedir_dato(mensaje, funcion_validar, *extra):
    """Pide un dato por teclado y repite hasta que pase la validación."""
    while True:
        valor = input(mensaje).strip()
        es_valido, error = funcion_validar(valor, *extra)
        if es_valido:
            return valor
        print(f"  (x) {error}")


def generar_codigo_sugerido(expedientes):
    """Sugiere el siguiente código libre del año actual (EXP-AAAA-NNNN)."""
    anio = date.today().year
    mayor = 0
    for exp in expedientes:
        partes = exp["codigo"].split("-")
        if len(partes) == 3 and partes[1] == str(anio) and partes[2].isdigit():
            if int(partes[2]) > mayor:
                mayor = int(partes[2])
    return f"EXP-{anio}-{mayor + 1:04d}"


def registrar_expediente(expedientes):
    """
    RF-01: registra un expediente nuevo.
    Devuelve el diccionario del expediente (ya validado) o None si
    el usuario cancela escribiendo 'salir' en el código.
    """
    sugerido = generar_codigo_sugerido(expedientes)
    print(f"(Código sugerido: {sugerido}. Escriba 'salir' para cancelar)")

    # Código: se permite Enter para aceptar el sugerido
    while True:
        codigo = input("Código del expediente [Enter = sugerido]: ").strip().upper()
        if codigo.lower() == "salir":
            print("Registro cancelado.")
            return None
        if codigo == "":
            codigo = sugerido
        es_valido, error = val.validar_codigo(codigo, expedientes)
        if es_valido:
            break
        print(f"  (x) {error}")

    dni = _pedir_dato("DNI (8 dígitos): ", val.validar_dni)
    nombre = _pedir_dato("Nombre completo: ", val.validar_nombre)
    tipo = _pedir_dato("Tipo de documento (Solicitud, Oficio, Reclamo...): ",
                       val.validar_tipo_documento)
    descripcion = _pedir_dato("Descripción del trámite: ", val.validar_descripcion)

    hoy = date.today().strftime("%d/%m/%Y")
    while True:
        fecha = input(f"Fecha DD/MM/AAAA [Enter = hoy {hoy}]: ").strip()
        if fecha == "":
            fecha = hoy
        es_valido, error = val.validar_fecha(fecha)
        if es_valido:
            break
        print(f"  (x) {error}")

    return {
        "codigo": codigo,
        "dni": dni,
        "nombre": nombre,
        "tipo_documento": tipo,
        "descripcion": descripcion,
        "fecha": fecha,
    }
