import json  
import requests  
import pandas as pd  
from datetime import datetime  

def extraer_data_api(exec_date, path):  
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")  
    json_path = (  
        f"{path}/raw_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.json"  
    )  
    url = "https://fakestoreapi.com/products"  
    headers = {"Accept-Encoding": "gzip, deflate"}  

    try:  
        print(f"Adquiriendo data para la fecha: {exec_date} desde la API")  
        response = requests.get(url, headers=headers)  
        if response:  
            print("Success!")  
            data = response.json()  
            with open(json_path, "w") as json_file:  
                json.dump(data, json_file)  
            print("JSON File guardado")  
        else:  
            print("Ocurrió un error adquiriendo la data para la fecha.")  
    except ValueError as e:  
        print("Formato datetime debería ser %Y-%m-%d %H", e)  
        raise e  

def extraer_data_csv(exec_date, path):  
    date = datetime.strptime(exec_date, "%Y-%m-%d %H")  
    csv_path = f"{path}/static_data/data_{date.year}-{date.month}-{date.day}-{date.hour}.csv"  
    
    try:  
        print(f"Adquiriendo data para la fecha: {exec_date} desde el archivo CSV")  
        data = pd.read_csv(csv_path)  
        print("Data del CSV cargada exitosamente")  
        return data  
    except Exception as e:  
        print("Error al leer el archivo CSV:", e)  
        raise e  

def extraer_data(exec_date, path):  
    extraer_data_api(exec_date, path)  
    
    data_csv = extraer_data_csv(exec_date, path)  
    
    return data_csv