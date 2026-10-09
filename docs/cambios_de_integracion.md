# Cambios de integración

Al unir los aportes aparecieron diferencias entre módulos. Esto es lo que se ajustó:

| # | Problema | Solución |
|---|---|---|
| 1 | `main.py` llamaba `buscar_expediente(expedientes, codigo)`, pero `consultas.py` define `buscar_expediente(codigo, expedientes=None)` | Se corrigió la llamada en `main.py` |
| 2 | `main.py` usaba `con.mostrar_todos()` y `con.mostrar_detalle_expediente()`, que no existían | Se agregaron a `consultas.py` |
| 3 | `main.py` importaba `validaciones` y `registro`, que no estaban | Se crearon `validaciones.py` y `registro.py` |
| 4 | El diccionario de datos decía `tipo_doc`, pero el CSV usa `tipo_documento` | Se usa `tipo_documento` en todo el proyecto |
| 5 | El orden por fecha comparaba texto `DD/MM/AAAA` (ej. 15/01/2026 quedaba antes que 02/10/2025) | `ordenamiento.py` convierte a `AAAA/MM/DD` al comparar (`clave_orden`) |
| 6 | `prueba_persistencia.py` sobrescribía `datos/expedientes.csv` real | Ahora usa `datos/prueba_expedientes.csv` y lo borra al terminar |
| 7 | `main.py` ordenaba y guardaba la lista reordenada, alterando el archivo | Ahora solo muestra el orden; el archivo no se reescribe al ordenar |
| 8 | El diseño de Ana usaba otros nombres de módulos | Tabla de equivalencias en `docs/diseno/estructura_modulos.md` |
