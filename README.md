# Del archivador al algoritmo: Mesa de Partes Digital

Prototipo en Python para la **Mesa de Partes de la Municipalidad Distrital de Santa Aurora** (caso simulado con fines académicos).
Curso: **Fundamentos de Programación – CIIN1205P**.

Permite **registrar, validar, buscar, mostrar y ordenar expedientes** y los guarda de forma **permanente en un archivo CSV**, de modo que los datos siguen disponibles al cerrar y volver a abrir el programa.

## Equipo

| Integrante | Rol | Aporte principal |
|---|---|---|
| Aaron | Integrante 1 – Análisis y observación + Base de Datos | `docs/analisis/`, `database/`, `exportar_sql.py` |
| Ana | Integrante 2 – Algoritmos y diseño | `docs/diseno/` |
| Victor | Integrante 3 – Registro y validación | `registro.py`, `validaciones.py` |
| Sebastián (Sebas) | Integrante 4 – Archivos, búsqueda y ordenamiento | `persistencia.py`, `consultas.py`, `ordenamiento.py`, `prueba_persistencia.py` |
| Jhonny | Integrante 5 – Integración y pruebas | `main.py`, `pruebas/` |

## Requisitos

- Python 3.8 o superior. **No se necesita instalar ninguna librería** (solo módulos estándar: `csv`, `os`, `re`, `datetime`, `sys`).
- La base de datos MySQL es **opcional** (complemento).

## Cómo ejecutar

```bash
git clone https://github.com/<tu-usuario>/MESA-DE-PARTES-DIGITAL.git
cd MESA-DE-PARTES-DIGITAL
python main.py
```

Menú del sistema:

```
=================================
   MESA DE PARTES DIGITAL
=================================
1. Registrar expediente
2. Buscar expediente
3. Mostrar expedientes
4. Ordenar expedientes
5. Salir
=================================
```

## Campos del expediente

| Campo | Validación |
|---|---|
| `codigo` | Formato `EXP-AAAA-NNNN`, obligatorio, sin duplicados |
| `dni` | Exactamente 8 dígitos numéricos |
| `nombre` | No vacío, sin números |
| `tipo_documento` | No vacío |
| `descripcion` | No vacía |
| `fecha` | `DD/MM/AAAA`, fecha real (Enter = hoy) |

## Estructura del repositorio

```
MESA-DE-PARTES-DIGITAL/
├── README.md
├── main.py                  # Menú y flujo principal (Integrante 5)
├── registro.py              # Registro de expedientes (Integrante 3)
├── validaciones.py          # Validación de campos (Integrante 3)
├── consultas.py             # Búsqueda y listado (Integrante 4)
├── ordenamiento.py          # Ordenamiento burbuja (Integrante 4)
├── persistencia.py          # Guardar/cargar CSV (Integrante 4)
├── prueba_persistencia.py   # Prueba crítica de persistencia (Integrante 4)
├── exportar_sql.py          # CSV -> INSERT de MySQL (Responsable BD)
├── datos/expedientes.csv    # Almacenamiento permanente
├── database/                # Base de datos complementaria (MySQL)
├── docs/analisis/           # Análisis y observación
├── docs/diseno/             # Alternativas, pseudocódigo, diagrama
└── pruebas/                 # Casos de prueba y resultados
```

## Pruebas

```bash
python -m unittest pruebas.test_sistema -v   # 19 pruebas automáticas
python prueba_persistencia.py                # guardar -> cerrar -> abrir -> cargar
```

Ver `pruebas/casos_prueba.md` y `pruebas/resultados_pruebas.md`.

## Base de datos complementaria (opcional)

La persistencia exigida por la consigna se hace **con archivos**. MySQL se incluye solo como complemento:

```bash
mysql -u root -p < database/crear_bd.sql
mysql -u root -p < database/crear_tablas.sql
mysql -u root -p < database/datos_prueba.sql
python exportar_sql.py            # genera database/exportacion_expedientes.sql con los datos reales
```

## Conceptos del curso aplicados

Estructuras de control (`if`, `while`, `for`), funciones y módulos, listas y diccionarios, cadenas (`strip`, `upper`, `isdigit`), archivos CSV, búsqueda secuencial, ordenamiento burbuja implementado manualmente, validación de datos y pruebas.

## Declaración de uso de IA

Ver [`docs/declaracion_ia.md`](docs/declaracion_ia.md).

## Nota

El caso es **simulado**: no hubo visita física a una mesa de partes ni se presentan documentos reales.
