# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
from datetime import datetime
import sqlite3


def log_progress(log_file, message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # toma el tiempo actual 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ':' + message + '\n') 
''' This function logs the mentioned message of a given stage of the
code execution to a log file. Function returns nothing'''

def extract(url, table_attribs):
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    df = pd.DataFrame(columns=table_attribs)
    for row in rows:
        col = row.find_all('td')

        if len(col) != 0:
            #print(repr(col[1].text))
            data_dict = {
                table_attribs[0]: col[1].get_text(strip=True), #eliminamos salto de lineas
                table_attribs[1]: col[2].get_text(strip=True)
            }
            #print(data_dict)
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            #print(df)
    return df 
''' This function aims to extract the required
information from the website and save it to a data frame. The
function returns the data frame for further processing. '''

def transform(df,csv_path,table_attribs):
    df_exchange_rate = pd.read_csv(csv_path)
    #Convierte esa columna en el índice del DataFrame // seleccionamos la otra columna 
    data_dict = df_exchange_rate.set_index(df_exchange_rate.columns[0]).to_dict()[df_exchange_rate.columns[1]]
    #TRANSFORM DATA
    df["MC_GBP_Billion"]= df[table_attribs[1]].astype(float) * data_dict["GBP"]
    df["MC_EUR_Billion"]= df[table_attribs[1]].astype(float) * data_dict["EUR"] 
    df["MC_INR_Billion"]= df[table_attribs[1]].astype(float) * data_dict["INR"]
    return df
''' This function accesses the CSV file for exchange rate
information, and adds three columns to the data frame, each
containing the transformed version of Market Cap column to
respective currencies'''

def load_to_csv(df, output_path):
    df.to_csv(output_path)
''' This function saves the final data frame as a CSV file in
the provided path. Function returns nothing.'''

def load_to_db(df, db_name, table_name):
    sql_connection = sqlite3.connect(db_name)
    df.to_sql(table_name, sql_connection, if_exists = 'replace',index=False)
    return sql_connection
''' This function saves the final data frame to a database
table with the provided name. Function returns nothing.'''

def run_query(query_statement, sql_connection):
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_statement)
    print(query_output)

''' This function runs the query on the database table and
prints the output on the terminal. Function returns nothing. '''

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

log_file = "code_log.txt"
url = "https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attribs= ["Name","MC_USD_Billon"]
csv_path = "exchange_rate.csv"
output_path = "Largest_banks_data.csv"
db_name = "Banks.db" 
table_name = "Largest_banks"
query_statement_1 = f"SELECT * FROM {table_name}"
query_statement_2 = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
query_statement_3 = f"SELECT name from {table_name} LIMIT 5"
#proceso
log_progress(log_file,'\n----------NEW LOG------------\nPreliminaries complete\nInitiating ETL Process')
df = extract(url, table_attribs)
log_progress(log_file,'Data extraction complete.\nInitiating Transformation process.')
df = transform(df, csv_path,table_attribs)
log_progress(log_file,'Data transformation complete.\nInitiating loading process.')
load_to_csv(df,output_path)
log_progress(log_file,'Data saved to CSV file.')
log_progress(log_file,'SQL Connection initiated.')
sql_connection =  load_to_db(df, db_name, table_name)
log_progress(log_file,'Data loaded to Database as table.\nRunning the query.')
log_progress(log_file,f"\nQuery 1 + {query_statement_1}")
run_query(query_statement_1, sql_connection)
log_progress(log_file,f"\nQuery 2 + {query_statement_2} ")
run_query(query_statement_2, sql_connection)
log_progress(log_file,f"\nQuery 3 + {query_statement_3}")
run_query(query_statement_3, sql_connection)
log_progress(log_file,'Process Complete.')
sql_connection.close()