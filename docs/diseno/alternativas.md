# Alternativas de solución

**Responsable:** Integrante 2 – Ana

## Alternativa 1: Python + archivos
- ✅ Implementación sencilla, pocos recursos.
- ✅ Cumple directamente la persistencia mediante archivos exigida por la consigna.
- ✅ Fácil de entender y mantener.
- ❌ Menor escalabilidad; búsquedas menos eficientes con muchos datos; datos menos estructurados.

## Alternativa 2: Python + SQL/MySQL
- ✅ Datos organizados en tablas, consultas eficientes, mayor escalabilidad, restricciones.
- ❌ Mayor complejidad; requiere instalar y administrar una base de datos.
- ❌ Por sí sola no cumple la persistencia mediante archivos de la consigna.

## Alternativa 3: Python + archivos + SQL/MySQL (seleccionada)
- Python: lógica, menú, validación, búsqueda, ordenamiento e integración.
- Archivos (CSV): persistencia exigida por la consigna.
- MySQL: complemento para almacenamiento y consulta estructurada.
- No reemplaza los archivos por SQL: integra ambos mecanismos.
