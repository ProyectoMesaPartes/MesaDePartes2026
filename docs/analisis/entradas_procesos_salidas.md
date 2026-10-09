# Entradas, procesos y salidas

| Entradas | Procesos | Salidas |
|---|---|---|
| Código del expediente | Validar que exista y no esté duplicado | Código aceptado o mensaje de corrección |
| DNI / identificación | Validar formato y registrar | Identificación validada |
| Nombre | Comprobar que no esté vacío | Nombre registrado |
| Tipo de documento | Registrar el tipo de solicitud | Tipo de documento almacenado |
| Descripción | Comprobar y registrar | Descripción registrada |
| Fecha | Registrar la fecha del expediente | Fecha almacenada |
| Código de consulta | Buscar coincidencia entre expedientes | Expediente encontrado / no encontrado |
| Lista de expedientes | Mostrar y organizar los registros | Listado de expedientes |

## Definiciones acordadas con el equipo

| Elemento | Definición |
|---|---|
| Entidad principal | Expediente |
| Identificador | Código del expediente |
| Datos | `codigo, dni, nombre, tipo_documento, descripcion, fecha` |
| Operaciones | Registrar, validar, buscar, mostrar, ordenar y conservar |
