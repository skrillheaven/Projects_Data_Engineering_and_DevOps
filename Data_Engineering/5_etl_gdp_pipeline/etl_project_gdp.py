# Code for ETL operations on Country-GDP data

# Importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime 

log_file = "etl_project_log.txt"
def extract(url, table_attribs):

    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')

    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')

    df = pd.DataFrame(columns=table_attribs)

    for row in rows:
        col = row.find_all('td')

        if len(col) != 0 and col[0].find('a') and col[2].text.strip() != '—':

            data_dict = {
                table_attribs[0]: col[0].a.contents[0],
                table_attribs[1]: col[2].contents[0]
            }

            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

    return df

def transform(df,table_attribs):
    df[table_attribs[1]] = df[table_attribs[1]].str.replace(',', '').astype(float)
    df[table_attribs[1]] = round(df[table_attribs[1]]/1000,2)
    df = df.rename(columns={table_attribs[1]: 'GDP_USD_billions'})
    return df
''' This function converts the GDP information from Currency
	format to float value, transforms the information of GDP from
	USD (Millions) to USD (Billions) rounding to 2 decimal places.
	The function returns the transformed dataframe.'''
    

def load_to_csv(df, csv_path):
    df.to_csv(csv_path)
''' This function saves the final dataframe as a `CSV` file 
	in the provided path. Function returns nothing.'''
    

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists = 'replace',index=False)
''' This function saves the final dataframe as a database table
	with the provided name. Function returns nothing.'''
    

def run_query(query_statement, sql_connection):
    #--Viewing all the data in the table--
    #query_statement = f"SELECT * FROM {table_name}"
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)
''' This function runs the stated query on the database table and
	prints the output on the terminal. Function returns nothing. '''
    

def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # toma el tiempo actual 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
        f.write(timestamp + ':' + message + '\n') 
''' This function logs the mentioned message at a given stage of the code execution to a log file. Function returns nothing'''

''' Here, you define the required entities and call the relevant 
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''
