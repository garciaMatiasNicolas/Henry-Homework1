import json
import os
from dotenv import load_dotenv
load_dotenv()

data_folder = os.getenv("DATA_FOLDER")
users_file = os.getenv("USERS_FILE")

actual_dir = os.path.dirname(os.path.abspath(__file__))
json_route = os.path.join(actual_dir, "..", data_folder, users_file)
data_route = os.path.normpath(json_route)

def read_json_file():
    with open(data_route, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def write_json_file(data, from_scratch: bool):
    if from_scratch:
        
        if not isinstance(data, list):
            raise ValueError("La informacion debe ser una lista")
        
        with open(data_route, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    
    else:
        current_data = read_json_file()
        
        if not isinstance(data, dict):
            raise ValueError("La informacion debe ser un diccionario")
        
        current_data.append(data)
        
        with open(data_route, "w", encoding="utf-8") as file:
            json.dump(current_data, file, indent=4, ensure_ascii=False)

