-- Generado por Oracle SQL Developer Data Modeler 18.2.0.179.0756
--   en:        2019-10-02 16:39:57 CEST
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



DROP TABLE producte CASCADE CONSTRAINTS;

DROP TABLE tiquet CASCADE CONSTRAINTS;

DROP TABLE venda CASCADE CONSTRAINTS;

CREATE TABLE producte (
    codibarres   VARCHAR2(6) NOT NULL,
    nom          VARCHAR2(20),
    marca        VARCHAR2(20),
    preu         NUMBER,
    stock        NUMBER
);

ALTER TABLE producte ADD CONSTRAINT producte_pk PRIMARY KEY ( codibarres );

CREATE TABLE tiquet (
    caixer          NUMBER NOT NULL,
    datavenda       DATE NOT NULL,
    formapagament   VARCHAR2(20),
    preutotal       NUMBER
);

ALTER TABLE tiquet ADD CONSTRAINT tiquet_pk PRIMARY KEY ( caixer,
                                                          datavenda );

CREATE TABLE venda (
    producte_codibarres   VARCHAR2(6) NOT NULL,
    tiquet_caixer         NUMBER NOT NULL,
    tiquet_datavenda      DATE NOT NULL,
    unitats               NUMBER
);

ALTER TABLE venda
    ADD CONSTRAINT venda_pk PRIMARY KEY ( producte_codibarres,
                                          tiquet_caixer,
                                          tiquet_datavenda );

ALTER TABLE venda
    ADD CONSTRAINT venda_producte_fk FOREIGN KEY ( producte_codibarres )
        REFERENCES producte ( codibarres );

ALTER TABLE venda
    ADD CONSTRAINT venda_tiquet_fk FOREIGN KEY ( tiquet_caixer,
                                                 tiquet_datavenda )
        REFERENCES tiquet ( caixer,
                            datavenda );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             3
-- CREATE INDEX                             0
-- ALTER TABLE                              5
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
