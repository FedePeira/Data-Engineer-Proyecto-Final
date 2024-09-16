DROP TABLE IF EXISTS fedepr2345_coderhouse.productos;

CREATE TABLE fedepr2345_coderhouse.productos (
    id INTEGER PRIMARY KEY,  
    titulo VARCHAR(255), 
    precio DECIMAL(10, 2),  
    descripcion VARCHAR(MAX), 
    categoria VARCHAR(255),  
    imagen VARCHAR(255), 
    fecha TIMESTAMP 
);