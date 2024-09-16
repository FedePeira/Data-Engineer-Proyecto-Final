import json  
import pandas as pd  
from datetime import datetime  

def transformar_data(exec_date, path):  
    print(f"Transformando la data para la fecha: {exec_date}")  

    date = datetime.strptime(exec_date, "%Y-%m-%d %H")  
    json_path = (  
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.json"  
    )  
    csv_path = (  
        f"{path}/processed_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"  
    )  

    with open(json_path, "r") as json_file:  
        loaded_data = json.load(json_file)  

    datax = loaded_data  
    data = pd.DataFrame.from_dict(datax, orient="index")  

    if isinstance(data, pd.DataFrame):  
        extracted_data = data[['id', 'titulo', 'precio', 'descripcion', 'categoria', 'imagen']]  
        extracted_data['fecha'] = loaded_data.get("fecha", datetime.now())  # Ajusta según tu estructura  

        extracted_data.to_csv(csv_path, index=False, mode="a", header=False)  
    else:  
        print("No se encontró la estructura esperada en los datos JSON.")  
        return  

    csv_data_path = f"{path}/static_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"  
    
    try:  
        csv_data = pd.read_csv(csv_data_path)  
        csv_data['fecha'] = datetime.now()    
        csv_data.to_csv(csv_path, index=False, mode="a", header=False)  
    except Exception as e:  
        print(f"Error al cargar el archivo CSV: {e}")  

    print(f"Datos transformados y guardados en {csv_path}")