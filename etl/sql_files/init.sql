-- DROP DATABASE IF EXISTS etl_bitcoins;

-- CREATE DATABASE etl_bitcoins;

CREATE SCHEMA etl_bitcoins_schema;

CREATE TABLE etl_bitcoins_schema.productos (
    id INTEGER PRIMARY KEY,  
    titulo VARCHAR(255), 
    precio DECIMAL(10, 2),  
    descripcion VARCHAR(MAX), 
    categoria VARCHAR(255),  
    imagen VARCHAR(255), 
    fecha TIMESTAMP 
);