# Requerimientos

## Funcionales

| ID | Requerimiento | Descripción | Dónde se cumple |
|---|---|---|---|
| RF-01 | Registrar expediente | Registrar código, DNI, nombre, tipo, descripción y fecha | `registro.py` |
| RF-02 | Validar campos | Impedir campos obligatorios vacíos | `validaciones.py` |
| RF-03 | Validar código | Código no vacío ni repetido | `validar_codigo()` |
| RF-04 | Validar identificación | Comprobar el formato del DNI (8 dígitos) | `validar_dni()` |
| RF-05 | Buscar expediente | Localizar por código | `consultas.buscar_expediente()` |
| RF-06 | Informar no encontrado | Mensaje si el código no existe | `main.py` opción 2 |
| RF-07 | Mostrar expedientes | Ver los registros | `consultas.mostrar_expedientes()` |
| RF-08 | Ordenar expedientes | Ordenar por fecha, código o nombre | `ordenamiento.py` |
| RF-09 | Conservar información | Datos disponibles después de cerrar | `persistencia.py` |

## No funcionales

| ID | Categoría | Requerimiento |
|---|---|---|
| RNF-01 | Usabilidad | Menú y mensajes claros |
| RNF-02 | Consistencia | Los campos mantienen el mismo significado en registro y consulta |
| RNF-03 | Persistencia | La información sigue disponible tras cerrar y abrir el programa |
| RNF-04 | Mantenibilidad | Código organizado en módulos |
| RNF-05 | Simplicidad | Complejidad adecuada al curso |
