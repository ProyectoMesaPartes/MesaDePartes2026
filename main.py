"""
main.py
Proyecto: Mesa de Partes Digital
Necesita en la misma carpeta: persistencia.py, consultas.py, ordenamiento.py
"""

import os
from datetime import datetime

from persistencia import cargar_expedientes, guardar_expedientes
from consultas import buscar_expediente, mostrar_expedientes
from ordenamiento import ordenar_expedientes

TIPOS_DOCUMENTO = [
    "Solicitud de constancia",
    "Reclamo",
    "Solicitud de licencia",
    "Queja",
    "Otro",
]


# ---------------- Donde se guardan los archivos ----------------
def elegir_carpeta():
    """Usa la carpeta del programa. Si no deja escribir, usa Documentos."""
    base = os.path.dirname(os.path.abspath(__file__))
    opciones = [
        os.path.join(base, "datos"),
        os.path.join(os.path.expanduser("~"), "Documents", "MesaDePartes", "datos"),
    ]
    for carpeta in opciones:
        try:
            os.makedirs(carpeta, exist_ok=True)
            prueba = os.path.join(carpeta, "prueba.tmp")
            archivo = open(prueba, "w")
            archivo.close()
            os.remove(prueba)
            return carpeta
        except Exception:
            pass
    return opciones[0]


CARPETA = elegir_carpeta()
RUTA_CSV = os.path.join(CARPETA, "expedientes.csv")
RUTA_TXT = os.path.join(CARPETA, "registro.txt")


# ---------------- Funciones de ayuda ----------------
def cargar_datos():
    """Carga los expedientes guardados."""
    try:
        datos = cargar_expedientes(RUTA_CSV)
    except Exception as error:
        print("No se pudo leer el archivo:", error)
        return []

    # Limpia nombres de columnas raros (por si se edito en Excel)
    lista = []
    for fila in datos:
        limpia = {}
        for clave in fila:
            limpia[str(clave).lstrip("\ufeff").strip()] = fila[clave]
        lista.append(limpia)
    return lista


def guardar_datos(expedientes):
    """Guarda en el CSV. Devuelve True si salio bien."""
    try:
        guardar_expedientes(expedientes, RUTA_CSV)
        return True
    except Exception as error:
        print("ERROR al guardar en", RUTA_CSV)
        print("Detalle:", error)
        print("Si el archivo esta abierto en Excel, cierrelo.")
        return False


def guardar_en_txt(exp, hora):
    """Agrega una linea al registro.txt (historial legible)."""
    caso_en_una_linea = exp["caso"].replace("\n", " ")
    linea = (
        exp["codigo"] + " | DNI: " + exp["dni"]
        + " | Nombre: " + exp["nombre"]
        + " | Hora: " + hora
        + " | Fecha: " + exp["fecha"]
        + " | Tipo: " + exp["tipo_documento"]
        + " | Descripcion: " + exp["descripcion"]
        + " | Caso: " + caso_en_una_linea
        + "\n"
    )
    try:
        archivo = open(RUTA_TXT, "a", encoding="utf-8")
        archivo.write(linea)
        archivo.close()
    except Exception as error:
        print("No se pudo escribir registro.txt:", error)


def generar_codigo(expedientes):
    """Crea el siguiente codigo: EXP-2026-0001, EXP-2026-0002..."""
    anio = datetime.now().year
    mayor = 0
    for exp in expedientes:
        partes = str(exp.get("codigo", "")).split("-")
        if len(partes) == 3 and partes[1] == str(anio) and partes[2].isdigit():
            if int(partes[2]) > mayor:
                mayor = int(partes[2])
    return "EXP-" + str(anio) + "-" + str(mayor + 1).zfill(4)


def pedir_texto(mensaje, minimo=3):
    while True:
        valor = input(mensaje).strip()
        if len(valor) >= minimo:
            return valor
        print("  Debe tener al menos", minimo, "caracteres.")


def pedir_dni(mensaje):
    while True:
        dni = input(mensaje).strip()
        if dni.isdigit() and len(dni) == 8:
            return dni
        print("  El DNI debe tener 8 digitos numericos.")


def elegir_tipo():
    print("Tipo de documento:")
    for i in range(len(TIPOS_DOCUMENTO)):
        print("  " + str(i + 1) + ".", TIPOS_DOCUMENTO[i])
    while True:
        op = input("Elija una opcion: ").strip()
        if op.isdigit() and 1 <= int(op) <= len(TIPOS_DOCUMENTO):
            return TIPOS_DOCUMENTO[int(op) - 1]
        print("  Opcion no valida.")


def pedir_caso():
    """Pide el caso en varias lineas. Termina cuando se escribe FIN."""
    print("\nEscriba el CASO con todo el detalle que quiera.")
    print("Puede escribir varias lineas. Al terminar, escriba FIN y presione Enter.")
    while True:
        lineas = []
        while True:
            linea = input("> ")
            if linea.strip().upper() == "FIN":
                break
            lineas.append(linea)
        texto = "\n".join(lineas).strip()
        if texto != "":
            return texto
        print("El caso no puede estar vacio. Intente de nuevo.")


def imprimir_expediente(exp):
    print("  Codigo      :", exp["codigo"])
    print("  DNI         :", exp["dni"])
    print("  Nombre      :", exp["nombre"])
    print("  Tipo        :", exp["tipo_documento"])
    print("  Descripcion :", exp["descripcion"])
    print("  Fecha       :", exp["fecha"])
    print("  CASO:")
    caso = exp.get("caso", "")
    if caso:
        print(caso)
    else:
        print("  (sin caso registrado)")


def buscar_por_dni(dni, expedientes):
    """Devuelve la lista de expedientes que tienen ese DNI."""
    encontrados = []
    for exp in expedientes:
        if str(exp.get("dni", "")).strip() == dni:
            encontrados.append(exp)
    return encontrados


# ---------------- Opciones del menu ----------------
def registrar(expedientes):
    print("\n--- REGISTRAR EXPEDIENTE ---")
    dni = pedir_dni("DNI (8 digitos): ")

    # Revisa si la persona ya esta registrada
    previos = buscar_por_dni(dni, expedientes)
    if len(previos) > 0:
        nombre = previos[0]["nombre"]
        print("\n*** El usuario ya esta registrado:", nombre, "***")
        for p in previos:
            print("    Expediente previo:", p["codigo"])
        respuesta = input("Registrar un nuevo expediente para esta persona? (s/n): ")
        if respuesta.strip().lower() != "s":
            print("Registro cancelado.")
            return
    else:
        nombre = pedir_texto("Nombre completo: ")

    tipo = elegir_tipo()
    descripcion = pedir_texto("Descripcion corta (resumen): ", 5)
    caso = pedir_caso()

    nuevo = {
        "codigo": generar_codigo(expedientes),
        "dni": dni,
        "nombre": nombre,
        "tipo_documento": tipo,
        "descripcion": descripcion,
        "caso": caso,
        "fecha": datetime.now().strftime("%d/%m/%Y"),
    }

    expedientes.append(nuevo)
    if guardar_datos(expedientes):
        guardar_en_txt(nuevo, datetime.now().strftime("%H:%M"))
        print("\nExpediente guardado con codigo:", nuevo["codigo"])
    else:
        expedientes.remove(nuevo)  # no se pudo guardar, se deshace


def listar(expedientes):
    print("\n--- LISTADO DE EXPEDIENTES ---")
    mostrar_expedientes(expedientes)


def buscar(expedientes):
    print("\n--- BUSCAR EXPEDIENTE ---")
    print("1. Por codigo")
    print("2. Por DNI")
    modo = input("Buscar por: ").strip()

    if modo == "1":
        codigo = input("Codigo (ej. EXP-2026-0001): ")
        exp = buscar_expediente(codigo, expedientes)
        if exp:
            print("\nExpediente encontrado:")
            imprimir_expediente(exp)
        else:
            print("No existe el codigo", codigo)
    elif modo == "2":
        dni = pedir_dni("DNI (8 digitos): ")
        encontrados = buscar_por_dni(dni, expedientes)
        if len(encontrados) > 0:
            print("\nSe encontraron", len(encontrados), "expediente(s):")
            for exp in encontrados:
                print("-" * 40)
                imprimir_expediente(exp)
        else:
            print("No hay expedientes con el DNI", dni)
    else:
        print("Opcion no valida.")


def ordenar(expedientes):
    print("\n--- ORDENAR EXPEDIENTES ---")
    print("1. Por fecha")
    print("2. Por codigo")
    print("3. Por nombre")
    opcion = input("Criterio: ").strip()
    criterios = {"1": "fecha", "2": "codigo", "3": "nombre"}
    if opcion not in criterios:
        print("Opcion no valida.")
        return
    asc = input("Ascendente? (s/n): ").strip().lower() != "n"
    mostrar_expedientes(ordenar_expedientes(expedientes, criterios[opcion], asc))


def modificar(exp, expedientes):
    """Permite cambiar los datos de UN expediente ya seleccionado."""
    while True:
        print("\n--- MODIFICAR", exp["codigo"], "---")
        print("1. Nombre")
        print("2. Tipo de documento")
        print("3. Descripcion corta")
        print("4. Caso")
        print("0. Terminar de modificar")
        op = input("Que desea cambiar: ").strip()

        if op == "1":
            exp["nombre"] = pedir_texto("Nuevo nombre completo: ")
        elif op == "2":
            exp["tipo_documento"] = elegir_tipo()
        elif op == "3":
            exp["descripcion"] = pedir_texto("Nueva descripcion corta: ", 5)
        elif op == "4":
            print("\nCaso actual:")
            print(exp.get("caso", ""))
            exp["caso"] = pedir_caso()
        elif op == "0":
            break
        else:
            print("Opcion no valida.")
            continue

        if guardar_datos(expedientes):
            print("Cambio guardado.")


def seleccionar(expedientes):
    """Elegir UN expediente de una lista numerada y trabajar con el."""
    print("\n--- SELECCIONAR EXPEDIENTE ---")
    if len(expedientes) == 0:
        print("No hay expedientes registrados todavia.")
        return

    # Filtro opcional para no ver una lista enorme
    print("Puede escribir parte del DNI, nombre o codigo para filtrar.")
    filtro = input("Filtro (Enter para ver todos): ").strip().lower()

    coincidencias = []
    for exp in expedientes:
        texto = (exp["dni"] + " " + exp["nombre"] + " " + exp["codigo"]).lower()
        if filtro in texto:
            coincidencias.append(exp)

    if len(coincidencias) == 0:
        print("No se encontraron expedientes con ese filtro.")
        return

    # Lista numerada
    print()
    print("N\u00b0  CODIGO         DNI        NOMBRE                   TIPO")
    print("-" * 70)
    for i in range(len(coincidencias)):
        e = coincidencias[i]
        print(str(i + 1).ljust(4) + e["codigo"].ljust(15) + e["dni"].ljust(11)
              + e["nombre"][:23].ljust(25) + e["tipo_documento"][:20])

    # Elegir numero
    while True:
        numero = input("\nNumero del expediente (0 para cancelar): ").strip()
        if numero == "0":
            return
        if numero.isdigit() and 1 <= int(numero) <= len(coincidencias):
            exp = coincidencias[int(numero) - 1]
            break
        print("Numero no valido.")

    # Que hacer con el expediente elegido
    while True:
        print("\n=== Expediente seleccionado:", exp["codigo"], "-", exp["nombre"], "===")
        print("1. Ver detalle completo")
        print("2. Modificar")
        print("3. Eliminar")
        print("0. Volver al menu")
        op = input("Elija una opcion: ").strip()

        if op == "1":
            print()
            imprimir_expediente(exp)
        elif op == "2":
            modificar(exp, expedientes)
        elif op == "3":
            if input("Seguro que desea eliminarlo? (s/n): ").strip().lower() == "s":
                expedientes.remove(exp)
                if guardar_datos(expedientes):
                    print("Expediente eliminado.")
                return
        elif op == "0":
            return
        else:
            print("Opcion no valida.")


# ---------------- Programa principal ----------------
def main():
    print("Los datos se guardan en:", CARPETA)
    expedientes = cargar_datos()

    while True:
        print("\n" + "=" * 40)
        print("   MESA DE PARTES DIGITAL")
        print("=" * 40)
        print("1. Registrar expediente")
        print("2. Listar expedientes")
        print("3. Buscar por codigo o DNI")
        print("4. Ordenar expedientes")
        print("5. Seleccionar expediente (ver / modificar / eliminar)")
        print("0. Salir")
        opcion = input("Elija una opcion: ").strip()

        try:
            if opcion == "1":
                registrar(expedientes)
            elif opcion == "2":
                listar(expedientes)
            elif opcion == "3":
                buscar(expedientes)
            elif opcion == "4":
                ordenar(expedientes)
            elif opcion == "5":
                seleccionar(expedientes)
            elif opcion == "0":
                print("Hasta pronto.")
                break
            else:
                print("Opcion no valida.")
        except Exception as error:
            # Si algo falla, el programa muestra el error y sigue funcionando
            print("Ocurrio un error:", error)


main()
