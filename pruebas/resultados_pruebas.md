# Resultados de pruebas

Fecha de ejecución: 09/10/2026 · Python 3.13.16

## Pruebas automáticas (`python -m unittest pruebas.test_sistema -v`)

```
test_busqueda_existente (pruebas.test_sistema.TestBusqueda.test_busqueda_existente) ... ok
test_busqueda_ignora_mayusculas_y_espacios (pruebas.test_sistema.TestBusqueda.test_busqueda_ignora_mayusculas_y_espacios) ... ok
test_busqueda_inexistente (pruebas.test_sistema.TestBusqueda.test_busqueda_inexistente) ... ok
test_lista_vacia_o_un_elemento (pruebas.test_sistema.TestOrdenamiento.test_lista_vacia_o_un_elemento) ... ok
test_no_modifica_original (pruebas.test_sistema.TestOrdenamiento.test_no_modifica_original) ... ok
test_ordenar_descendente (pruebas.test_sistema.TestOrdenamiento.test_ordenar_descendente) ... ok
test_ordenar_por_fecha_cronologico (pruebas.test_sistema.TestOrdenamiento.test_ordenar_por_fecha_cronologico) ... ok
test_archivo_inexistente_devuelve_lista_vacia (pruebas.test_sistema.TestPersistencia.test_archivo_inexistente_devuelve_lista_vacia) ... ok
test_guardar_cerrar_abrir_cargar (pruebas.test_sistema.TestPersistencia.test_guardar_cerrar_abrir_cargar) ... ok
test_texto_con_comas_y_comillas (pruebas.test_sistema.TestPersistencia.test_texto_con_comas_y_comillas) ... ok
test_campos_obligatorios (pruebas.test_sistema.TestValidaciones.test_campos_obligatorios) ... ok
test_codigo_duplicado (pruebas.test_sistema.TestValidaciones.test_codigo_duplicado) ... ok
test_codigo_formato_incorrecto (pruebas.test_sistema.TestValidaciones.test_codigo_formato_incorrecto) ... ok
test_codigo_vacio (pruebas.test_sistema.TestValidaciones.test_codigo_vacio) ... ok
test_codigo_valido (pruebas.test_sistema.TestValidaciones.test_codigo_valido) ... ok
test_dni_invalido (pruebas.test_sistema.TestValidaciones.test_dni_invalido) ... ok
test_dni_valido (pruebas.test_sistema.TestValidaciones.test_dni_valido) ... ok
test_fecha (pruebas.test_sistema.TestValidaciones.test_fecha) ... ok
test_nombre_vacio_o_con_numeros (pruebas.test_sistema.TestValidaciones.test_nombre_vacio_o_con_numeros) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.008s

OK
```

## Prueba crítica de persistencia (`python prueba_persistencia.py`)

```

--- PASO 1: Registrar expedientes de prueba ---
Se registraron 2 expedientes en memoria.

--- PASO 2: Guardar en archivo (datos/prueba_expedientes.csv) ---
Guardado correctamente.

--- PASO 3: Simular cierre del programa ---
Variable eliminada de memoria (simula cerrar el programa).

--- PASO 4: 'Reabrir' el programa y cargar desde archivo ---

--- PASO 5: Comprobar que los datos persistieron ---
OK: se recuperaron los 2 expedientes guardados.
======================================================================
CODIGO         NOMBRE                   TIPO DOC.           FECHA     
======================================================================
EXP-2026-0001  Maria Fernanda Quispe Ro Solicitud de consta 02/10/2026
EXP-2026-0002  Luis Alberto Torres Vega Reclamo             01/10/2026
======================================================================

--- PASO 6: Probar búsqueda por código ---
Encontrado: {'codigo': 'EXP-2026-0002', 'dni': '71234567', 'nombre': 'Luis Alberto Torres Vega', 'tipo_documento': 'Reclamo', 'descripcion': 'Reclamo por ruido de obra cercana', 'fecha': '01/10/2026'}

--- PASO 7: Probar ordenamiento por fecha ---
01/10/2026 - EXP-2026-0002
02/10/2026 - EXP-2026-0001

Archivo de prueba eliminado. Prueba finalizada.
```

## Resumen

| Caso | Esperado | Obtenido |
|---|---|---|
| CP-01 | Ver casos_prueba.md | ✅ Correcto |
| CP-02 | Ver casos_prueba.md | ✅ Correcto |
| CP-03 | Ver casos_prueba.md | ✅ Correcto |
| CP-04 | Ver casos_prueba.md | ✅ Correcto |
| CP-05 | Ver casos_prueba.md | ✅ Correcto |
| CP-06 | Ver casos_prueba.md | ✅ Correcto |
| CP-07 | Ver casos_prueba.md | ✅ Correcto |
| CP-08 | Ver casos_prueba.md | ✅ Correcto |
