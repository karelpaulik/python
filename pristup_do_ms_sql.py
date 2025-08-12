# Připojení do databáze přes: pyodbc--------------------------------------------------------
import pandas as pd
import pyodbc

conn_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=juli-sql;"
    "DATABASE=JULI_Warehouse;"
    "UID=jpm_user;"
    "PWD=jpm;"
)
conn = pyodbc.connect(conn_string)


query = "SELECT * FROM MSP28"
df = pd.read_sql(query, conn)

# spojení uzavřít
conn.close()

print(df.head())

# Připojení do databáze přes: sqlalchemy-------------------------------------------------------
import pandas as pd
from sqlalchemy import create_engine

# Vytvoření připojovacího řetězce
# Formát: "mssql+pyodbc://uživatel:heslo@server/databáze?driver=ODBC+Driver+17+for+SQL+Server"
# Důležité: Místo "@" a ":" použijte URL-escapované znaky, pokud je máte v heslu nebo uživ. jménu

server_name = 'juli-sql'
database_name = 'JULI_Warehouse'
username = 'jpm_user'
password = 'jpm'

connection_string = f"mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(connection_string)
query = "SELECT TOP 10 * FROM MSP28"
df = pd.read_sql(query, engine)
print("Data byla úspěšně načtena:")
print(df.head())
#engine.dispose()  # Zavření spojení zde není nutné