-- consultas.sql
-- Responsable de Base de Datos: Aaron
-- Consultas equivalentes a las operaciones del programa en Python

USE mesa_partes;

-- RF-07: mostrar todos los expedientes
SELECT * FROM expedientes;

-- RF-05 / RF-06: buscar por código (si no hay filas = no encontrado)
SELECT * FROM expedientes WHERE codigo = 'EXP-2026-0001';

-- RF-08: ordenar por fecha (más reciente primero)
SELECT codigo, nombre, fecha FROM expedientes ORDER BY fecha DESC;

-- Ordenar por código
SELECT codigo, nombre, fecha FROM expedientes ORDER BY codigo ASC;

-- Buscar por DNI del solicitante
SELECT * FROM expedientes WHERE dni = '72845136';

-- Contar expedientes por tipo de documento
SELECT tipo_documento, COUNT(*) AS total
FROM expedientes
GROUP BY tipo_documento;

-- Verificar duplicados de código (debe devolver 0 filas)
SELECT codigo, COUNT(*) FROM expedientes GROUP BY codigo HAVING COUNT(*) > 1;
