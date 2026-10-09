# Comparación de alternativas

| Criterio | Python + archivos | Python + SQL/MySQL | Python + archivos + SQL/MySQL |
|---|---|---|---|
| Complejidad | Baja | Media/Alta | Media/Alta |
| Recursos | Bajos | Mayores | Mayores |
| Implementación | Simple | Más compleja | Completa e integrada |
| Persistencia | Archivos | Base de datos | Archivos + base de datos |
| Organización de datos | Básica | Estructurada | Estructurada y complementaria |
| Búsqueda | Básica | Eficiente (SQL) | Eficiente (SQL y archivos) |
| Escalabilidad | Limitada | Alta | Mayor flexibilidad |
| Cumplimiento de la consigna | Directo | Parcial/Complementario | Directo y complementario |
| Mantenimiento | Sencillo | Requiere conocimientos de BD | Requiere coordinación entre componentes |
| Integración | Baja | Media | Alta |

## Solución seleccionada

**Alternativa 3.** Cumple la persistencia con archivos y añade una BD SQL como complemento estructurado.

> En la implementación, el programa funciona completamente con Python + CSV. La BD MySQL se entrega como scripts (`database/`) y se puebla desde el CSV con `exportar_sql.py`, de modo que el programa no depende de tener MySQL instalado.
