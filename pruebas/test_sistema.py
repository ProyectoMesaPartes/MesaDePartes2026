"""
test_sistema.py
Integrante 5 - Integración y Pruebas
Proyecto: Mesa de Partes Digital

Casos de prueba automáticos (ver pruebas/casos_prueba.md).
Ejecutar desde la carpeta raíz del proyecto:

    python -m unittest pruebas.test_sistema -v
"""

import os
import sys
import tempfile
import unittest

# Permite importar los módulos de la carpeta raíz
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import validaciones as val
from persistencia import guardar_expedientes, cargar_expedientes
from consultas import buscar_expediente
from ordenamiento import ordenar_expedientes


def exp(codigo, nombre="Ana Perez", fecha="01/01/2026"):
    return {"codigo": codigo, "dni": "12345678", "nombre": nombre,
            "tipo_documento": "Solicitud", "descripcion": "Prueba", "fecha": fecha}


class TestValidaciones(unittest.TestCase):
    def test_codigo_valido(self):                      # CP-01
        self.assertTrue(val.validar_codigo("EXP-2026-0001", [])[0])

    def test_codigo_vacio(self):                       # CP-03
        self.assertFalse(val.validar_codigo("   ", [])[0])

    def test_codigo_formato_incorrecto(self):
        self.assertFalse(val.validar_codigo("ABC-1", [])[0])

    def test_codigo_duplicado(self):                   # CP-04
        self.assertFalse(val.validar_codigo("exp-2026-0001", [exp("EXP-2026-0001")])[0])

    def test_dni_valido(self):
        self.assertTrue(val.validar_dni("72845136")[0])

    def test_dni_invalido(self):                       # CP-02
        for malo in ["", "1234567", "123456789", "7284513a"]:
            self.assertFalse(val.validar_dni(malo)[0], malo)

    def test_nombre_vacio_o_con_numeros(self):
        self.assertFalse(val.validar_nombre("")[0])
        self.assertFalse(val.validar_nombre("Juan2")[0])
        self.assertTrue(val.validar_nombre("María Quispe")[0])

    def test_campos_obligatorios(self):
        self.assertFalse(val.validar_tipo_documento(" ")[0])
        self.assertFalse(val.validar_descripcion("")[0])

    def test_fecha(self):
        self.assertTrue(val.validar_fecha("02/10/2026")[0])
        self.assertFalse(val.validar_fecha("31/02/2026")[0])
        self.assertFalse(val.validar_fecha("2026-10-02")[0])


class TestBusqueda(unittest.TestCase):
    def setUp(self):
        self.lista = [exp("EXP-2026-0001"), exp("EXP-2026-0002")]

    def test_busqueda_existente(self):                 # CP-05
        self.assertEqual(buscar_expediente("EXP-2026-0002", self.lista)["codigo"],
                         "EXP-2026-0002")

    def test_busqueda_ignora_mayusculas_y_espacios(self):
        self.assertIsNotNone(buscar_expediente("  exp-2026-0001 ", self.lista))

    def test_busqueda_inexistente(self):               # CP-06
        self.assertIsNone(buscar_expediente("EXP-2026-9999", self.lista))


class TestOrdenamiento(unittest.TestCase):
    def test_ordenar_por_fecha_cronologico(self):      # CP-07
        lista = [exp("EXP-2026-0001", fecha="15/01/2026"),
                 exp("EXP-2026-0002", fecha="02/10/2025"),
                 exp("EXP-2026-0003", fecha="01/12/2025")]
        r = ordenar_expedientes(lista, "fecha")
        self.assertEqual([e["fecha"] for e in r],
                         ["02/10/2025", "01/12/2025", "15/01/2026"])

    def test_ordenar_descendente(self):
        lista = [exp("EXP-2026-0001"), exp("EXP-2026-0003"), exp("EXP-2026-0002")]
        r = ordenar_expedientes(lista, "codigo", ascendente=False)
        self.assertEqual([e["codigo"] for e in r],
                         ["EXP-2026-0003", "EXP-2026-0002", "EXP-2026-0001"])

    def test_no_modifica_original(self):
        lista = [exp("EXP-2026-0002"), exp("EXP-2026-0001")]
        ordenar_expedientes(lista, "codigo")
        self.assertEqual(lista[0]["codigo"], "EXP-2026-0002")

    def test_lista_vacia_o_un_elemento(self):
        self.assertEqual(ordenar_expedientes([], "fecha"), [])
        self.assertEqual(len(ordenar_expedientes([exp("EXP-2026-0001")], "fecha")), 1)


class TestPersistencia(unittest.TestCase):
    def test_guardar_cerrar_abrir_cargar(self):        # CP-08
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "datos", "expedientes.csv")
            original = [exp("EXP-2026-0001", nombre="María Fernanda Quispe Rojas"),
                        exp("EXP-2026-0002")]
            guardar_expedientes(original, ruta)
            copia = list(original)
            del original                       # "cierra" el programa
            self.assertEqual(cargar_expedientes(ruta), copia)

    def test_archivo_inexistente_devuelve_lista_vacia(self):
        self.assertEqual(cargar_expedientes("no_existe/archivo.csv"), [])

    def test_texto_con_comas_y_comillas(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "e.csv")
            e = exp("EXP-2026-0001")
            e["descripcion"] = 'Solicitud, urgente: "constancia"'
            guardar_expedientes([e], ruta)
            self.assertEqual(cargar_expedientes(ruta)[0]["descripcion"], e["descripcion"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
