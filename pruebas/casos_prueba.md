# Casos de prueba

**Responsable:** Integrante 5 – Jhonny · Automatizados en `pruebas/test_sistema.py`

| ID | Caso | Entrada | Resultado esperado | Prueba automática |
|---|---|---|---|---|
| CP-01 | Registro válido | Datos correctos | Expediente registrado | `test_codigo_valido` |
| CP-02 | DNI inválido | `""`, `1234567`, `123456789`, `7284513a` | Se rechaza y se pide de nuevo | `test_dni_invalido` |
| CP-03 | Código vacío | Vacío | Se pide de nuevo | `test_codigo_vacio` |
| CP-04 | Código duplicado | Código existente (cualquier mayúscula/minúscula) | Se rechaza | `test_codigo_duplicado` |
| CP-05 | Búsqueda existente | Código registrado | Expediente encontrado | `test_busqueda_existente` |
| CP-06 | Búsqueda inexistente | Código no registrado | "No encontrado" | `test_busqueda_inexistente` |
| CP-07 | Ordenamiento | Varios expedientes | Orden correcto (fecha cronológica) | `test_ordenar_por_fecha_cronologico` |
| CP-08 | Persistencia | Guardar, cerrar y abrir | Datos conservados | `test_guardar_cerrar_abrir_cargar` |

## Pruebas adicionales

Formato de código, nombre con números, fecha inexistente (31/02), orden descendente, la lista original no se modifica, lista vacía, archivo inexistente (primera ejecución) y textos con comas/comillas en el CSV.

## Cómo ejecutarlas

```bash
python -m unittest pruebas.test_sistema -v
python prueba_persistencia.py
```
