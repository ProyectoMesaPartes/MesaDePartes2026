-- datos_prueba.sql
-- Responsable de Base de Datos: Aaron

USE mesa_partes;

INSERT INTO expedientes (codigo, dni, nombre, tipo_documento, descripcion, fecha) VALUES
('EXP-2026-0001', '72845136', 'María Fernanda Quispe Rojas', 'Solicitud de constancia',
 'Solicitud de constancia de no adeudo municipal', '2026-10-02'),
('EXP-2026-0002', '71234567', 'Luis Alberto Torres Vega', 'Reclamo',
 'Reclamo por ruido de obra cercana', '2026-10-01'),
('EXP-2026-0003', '70123456', 'Rosa Elena Huamán Díaz', 'Oficio',
 'Oficio de solicitud de licencia de funcionamiento', '2026-09-28');
