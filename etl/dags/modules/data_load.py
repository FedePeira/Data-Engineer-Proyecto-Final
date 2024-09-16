from datetime import datetime

import pandas as pd
import psycopg2
from psycopg2.extras import execute_values
from .utils import get_credentials
from .utils import get_schema


def create_table_if_not_exists(conn):
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {get_schema()}.productos (
        id INTEGER PRIMARY KEY,  
        titulo VARCHAR(255), 
        precio DECIMAL(10, 2),  
        descripcion VARCHAR(MAX), 
        categoria VARCHAR(255),  
        imagen VARCHAR(255), 
        fecha TIMESTAMP 
    );
    """
    with conn.cursor() as cur:
        cur.execute(create_table_query)
        conn.commit()
    print(f"Tabla {get_schema()}.productos esta lista.")



def cargar_data(exec_date, path):

    print(f"Cargando la data para la fecha: {exec_date}")
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")
    csv_path = (
        f"{path}/processed_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"
    )

    records = pd.read_csv(csv_path, sep=",").fillna(0)

    print(records.shape)
    print(records.head())

    credentials = get_credentials()
    print(credentials)
    conn = psycopg2.connect(**credentials)
    create_table_if_not_exists(conn)
    
    columns = [
        "id",
        "titulo",
        "precio",
        "descripcion",
        "categoria",
        "attack_appeal",
        "imagen",
        "fecha",
    ]
    cur = conn.cursor()
    # Define el nombre de la tabla
    table_name = "productos"
    # Define las columnas que queremos insertar
    columns = columns
    # Genera
    values = [tuple(x) for x in records.to_numpy()]
    insert_sql = f"INSERT INTO {get_schema()}.{table_name} ({', '.join(columns)}) VALUES %s"
    # Ejecuta el INSERT usando execute_values
    cur.execute("BEGIN")
    execute_values(cur, insert_sql, values)
    cur.execute("COMMIT")