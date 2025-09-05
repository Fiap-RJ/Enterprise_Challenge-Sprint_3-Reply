-- Gerado por Oracle SQL Developer Data Modeler 24.3.1.351.0831
--   em:        2025-09-05 00:18:13 BRT
--   site:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE T_MAQUINA CASCADE CONSTRAINTS 
;

DROP TABLE T_MEDICAO CASCADE CONSTRAINTS 
;

DROP TABLE T_SENSOR CASCADE CONSTRAINTS 
;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE T_MAQUINA 
    ( 
     cd_maq           CHAR (5)  NOT NULL , 
     tipo             VARCHAR2 (20)  NOT NULL , 
     modelo           VARCHAR2 (30)  NOT NULL , 
     ano              NUMBER (4)  NOT NULL , 
     inicio_opercacao DATE  NOT NULL , 
     termino_operacao DATE 
    ) 
;

ALTER TABLE T_MAQUINA 
    ADD CONSTRAINT CK_PRAZO 
    CHECK (termino_operacao>inicio_operacao)
;
ALTER TABLE T_MAQUINA 
    ADD CONSTRAINT PK_T_MAQUINA PRIMARY KEY ( cd_maq ) ;

CREATE TABLE T_MEDICAO 
    ( 
     cd_medicao VARCHAR2 (60)  NOT NULL , 
     cd_sensor  CHAR (6)  NOT NULL , 
     data       TIMESTAMP WITH TIME ZONE  NOT NULL , 
     temp       NUMBER (3) , 
     umid       NUMBER (3,3) 
    ) 
;

ALTER TABLE T_MEDICAO 
    ADD CONSTRAINT PK_T_MEDICAO PRIMARY KEY ( cd_medicao ) ;

CREATE TABLE T_SENSOR 
    ( 
     cd_sensor         CHAR (6)  NOT NULL , 
     cd_maq            CHAR (5)  NOT NULL , 
     tipo              VARCHAR2 (20)  NOT NULL , 
     modelo            VARCHAR2 (30)  NOT NULL , 
     ano               NUMBER (4)  NOT NULL , 
     inicio_operacao   DATE  NOT NULL , 
     termino_opercacao DATE 
    ) 
;

ALTER TABLE T_SENSOR 
    ADD CONSTRAINT CK_SENSOR_OP 
    CHECK (tremino_operacao>inicio_operacao)
;
ALTER TABLE T_SENSOR 
    ADD CONSTRAINT PK_T_SENSOR PRIMARY KEY ( cd_sensor ) ;

ALTER TABLE T_SENSOR 
    ADD CONSTRAINT UN_T_SENSOR_ UNIQUE ( cd_maq ) ;

ALTER TABLE T_MEDICAO 
    ADD CONSTRAINT FK_MEDICAO_SENSOR FOREIGN KEY 
    ( 
     cd_sensor
    ) 
    REFERENCES T_SENSOR 
    ( 
     cd_sensor
    ) 
;

ALTER TABLE T_SENSOR 
    ADD CONSTRAINT FK_SENSOR_MAQ FOREIGN KEY 
    ( 
     cd_maq
    ) 
    REFERENCES T_MAQUINA 
    ( 
     cd_maq
    ) 
;



-- Relatório do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              8
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
