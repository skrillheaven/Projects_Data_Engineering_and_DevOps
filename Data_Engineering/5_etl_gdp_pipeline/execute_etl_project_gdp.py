from etl_project_gdp import extract, transform, load_to_csv, load_to_db,run_query ,log_progress
import sqlite3

url = 'https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country","GDP_USD_millions"]
db_name = "World_Economies.db"
table_name = "Countries_by_GDP"
csv_path = "Countries_by_GDP.csv"
query_statement = f"SELECT * from {table_name} WHERE GDP_USD_billions >= 100"

log_progress('\n----------NEW LOG------------\nPreliminaries complete\nInitiating ETL Process')
df = extract(url, table_attribs)

log_progress('Data extraction complete.\nInitiating Transformation process.')
df = transform(df,table_attribs)

log_progress('Data transformation complete.\nInitiating loading process.')
load_to_csv(df, csv_path)

log_progress('Data saved to CSV file.')
sql_connection = sqlite3.connect(db_name)

log_progress('SQL Connection initiated.')
load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table.\nRunning the query.')
run_query(query_statement, sql_connection)

log_progress('Process Complete.')
sql_connection.close()
