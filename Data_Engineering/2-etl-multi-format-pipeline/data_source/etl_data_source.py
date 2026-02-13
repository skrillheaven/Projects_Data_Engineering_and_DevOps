#importar todas las bibliotecas
import glob #lista de archivos
import pandas as pd
import xml.etree.ElementTree as ET #manejo de archivos xml
from datetime import datetime

log_file = "log_file_data_source.txt" #registro de logs
target_file = "transformed_data_source.csv"  #almacenar datos de salida

#funciones de extraccion
def extract_from_csv(file_to_process): 
    dataframe = pd.read_csv(file_to_process) 
    return dataframe 

def extract_from_json(file_to_process): 
    dataframe = pd.read_json(file_to_process, lines=True) 
    return dataframe 

def extract_from_xml(file_to_process): 
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price","fuel"]) #necesitas saber los encabezados
    tree = ET.parse(file_to_process) #analizar los datos del archivo utilizando la funcion ElementTree
    root = tree.getroot() #navega desde la raiz
    for car in root: 
        car_model = car.find("car_model").text 
        year_of_manufacture = float(car.find("year_of_manufacture").text) 
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = pd.concat([dataframe, pd.DataFrame([{"car_model":car_model, "year_of_manufacture":year_of_manufacture, "price":price, "fuel":fuel}])], ignore_index=True) 
    return dataframe 
def extract(): 
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price','fuel']) # creando dataframe vacio a espera de la extraccion de datos
     
    #procesar todos los archivos csv, excepto el archivo de destino
    for csvfile in glob.glob("*.csv"): 
        if csvfile != target_file:  # revisa si no es el archivo destino
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True) 

	#procesa todos los archivos json
    for jsonfile in glob.glob("*.json"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)  
	#procesa todos los archivos xml
    for xmlfile in glob.glob("*.xml"): 
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlfile))], ignore_index=True) 
            
    return extracted_data 
#seccion de TRANSFORM en ETL
def transform(data): 
	#redondeamos valores
	data['price'] = round(data.price,2) 
	return data

def load_data(target_file,transformed_data): #carga y almacen de datos listos para almacenar
	transformed_data.to_csv(target_file)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # toma el tiempo actual 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ',' + message + '\n') 
