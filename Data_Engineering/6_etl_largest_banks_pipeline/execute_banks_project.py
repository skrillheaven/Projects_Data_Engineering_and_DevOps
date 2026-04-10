from banks_project import sqlite3, extract, transform, load_to_csv, load_to_db,run_query ,log_progress,sqlite3
#variables
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