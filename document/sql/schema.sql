-- Script de Criação de Tabelas para o Projeto FarmTech
-- Este script define a estrutura do banco de dados para armazenar dados de sensores de máquinas.

-- Tabela de Máquinas
-- Armazena informações sobre cada máquina monitorada.
CREATE TABLE T_MAQUINA (
    cd_maq VARCHAR(5) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano NUMBER(4) NOT NULL,
    inicio_operacao DATE NOT NULL,
    termino_operacao DATE,
    CONSTRAINT pk_maquina PRIMARY KEY (cd_maq)
);

-- Tabela de Sensores
-- Armazena informações sobre cada sensor, associado a uma máquina.
CREATE TABLE T_SENSOR (
    cd_sensor VARCHAR(6) NOT NULL,
    cd_maq VARCHAR(5) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano NUMBER(4) NOT NULL,
    inicio_operacao DATE NOT NULL,
    termino_opercao DATE,
    CONSTRAINT pk_sensor PRIMARY KEY (cd_sensor),
    CONSTRAINT fk_sensor_maquina FOREIGN KEY (cd_maq) REFERENCES T_MAQUINA(cd_maq)
);

-- Tabela de Medições
-- Armazena as leituras de cada sensor ao longo do tempo.
CREATE TABLE T_MEDICAO (
    cd_medicao VARCHAR(10) NOT NULL,
    cd_sensor VARCHAR(6) NOT NULL,
    data TIMESTAMP NOT NULL,
    temp NUMBER(5, 2) NOT NULL,
    umid NUMBER(4, 3) NOT NULL,
    CONSTRAINT pk_medicao PRIMARY KEY (cd_medicao),
    CONSTRAINT fk_medicao_sensor FOREIGN KEY (cd_sensor) REFERENCES T_SENSOR(cd_sensor)
);

-- Comentários sobre a modelagem:
-- 1. Normalização: A estrutura está na Terceira Forma Normal (3FN), evitando redundância de dados.
-- 2. Chaves: Chaves primárias (PK) e estrangeiras (FK) garantem a integridade referencial entre as tabelas.
-- 3. Tipos de Dados: Foram escolhidos tipos de dados adequados para cada campo (ex: NUMBER para valores numéricos, DATE/TIMESTAMP para datas).
