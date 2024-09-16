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
    print(f"Tabla {get_schema()}.productos está lista.")  

def cargar_data(exec_date, path):  
    print(f"Cargando la data para la fecha: {exec_date}")  

    data_api = pd.read_json(f"{path}/raw_data/data_{exec_date}.json")  
    
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")  
    csv_path = f"{path}/static_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"  
    data_csv = pd.read_csv(csv_path).fillna(0)  

    combined_data = pd.concat([data_api, data_csv], ignore_index=True)  

    print(combined_data.shape)  
    print(combined_data.head())  

    credentials = get_credentials()  
    conn = psycopg2.connect(**credentials)  
    create_table_if_not_exists(conn)  

    columns = [  
        "id",  
        "titulo",  
        "precio",  
        "descripcion",  
        "categoria",  
        "imagen",  
        "fecha",  
    ]  
    cur = conn.cursor()  
    table_name = "productos"  
    values = [tuple(x) for x in combined_data[columns].to_numpy()]  
    insert_sql = f"INSERT INTO {get_schema()}.{table_name} ({', '.join(columns)}) VALUES %s"  
    cur.execute("BEGIN")  
    execute_values(cur, insert_sql, values)  
    cur.execute("COMMIT")  