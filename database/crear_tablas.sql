-- crear_tablas.sql
-- Responsable de Base de Datos: Aaron

USE mesa_partes;

CREATE TABLE expedientes (
    id_expediente  INT AUTO_INCREMENT PRIMARY KEY,
    codigo         VARCHAR(13)  NOT NULL UNIQUE,          -- EXP-AAAA-NNNN
    dni            CHAR(8)      NOT NULL,
    nombre         VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(60)  NOT NULL,
    descripcion    TEXT         NOT NULL,
    fecha          DATE         NOT NULL,
    CONSTRAINT chk_codigo CHECK (codigo REGEXP '^EXP-[0-9]{4}-[0-9]{4}$'),
    CONSTRAINT chk_dni    CHECK (dni REGEXP '^[0-9]{8}$')
);

CREATE INDEX idx_expedientes_dni   ON expedientes (dni);
CREATE INDEX idx_expedientes_fecha ON expedientes (fecha);
