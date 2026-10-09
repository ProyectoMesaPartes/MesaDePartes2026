# Pseudocódigo

Coincide con `main.py`. (El diseño original de Ana incluía una opción de consulta SQL; en la versión final la BD se consulta directamente con `database/consultas.sql` y los datos se exportan con `exportar_sql.py`.)

```
INICIO
  expedientes <- cargar_expedientes() desde datos/expedientes.csv
  REPETIR
    Mostrar menú
    Leer opción
    SI opción = 1 ENTONCES
      Solicitar código, DNI, nombre, tipo, descripción, fecha
      REPETIR cada pregunta HASTA que el dato sea válido
      Agregar expediente a la lista
      Guardar en archivo
      Mostrar "registro exitoso"
    SI opción = 2 ENTONCES
      Solicitar código
      Buscar en la lista
      SI existe ENTONCES mostrar detalle
      SINO mostrar "no encontrado"
    SI opción = 3 ENTONCES
      Mostrar todos los expedientes
    SI opción = 4 ENTONCES
      Solicitar criterio (fecha / código / nombre) y sentido
      Ordenar copia de la lista (burbuja)
      Mostrar expedientes ordenados
    SI opción = 5 ENTONCES
      Guardar información en archivo
  HASTA opción = 5
FIN
```

## Ordenamiento burbuja

```
PARA i DESDE 0 HASTA n-2
  PARA j DESDE 0 HASTA n-2-i
    SI clave(lista[j]) > clave(lista[j+1]) ENTONCES
      intercambiar lista[j] y lista[j+1]
```

La clave de `fecha` se convierte de DD/MM/AAAA a AAAA/MM/DD para que el orden sea cronológico.
