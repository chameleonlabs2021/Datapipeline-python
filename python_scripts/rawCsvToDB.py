import pandas as pd
import json
import psycopg2
from psycopg2 import sql
json_path = "config.json"
from dropTable import droptable
import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)


with open ("config.json" , "r") as f:
    config_data= json.loads(f.read() )

db = config_data["StgDatabase"]
user=config_data["USER"]
password=config_data["PASSWORD"]
host=config_data["HOST"]
port=config_data["PORT"]
batch_size=config_data["batch_size"]
jsonOut=config_data["jsonOut"]
sqlScriptsPath=config_data["sqlScriptsPath"]

conn = psycopg2.connect(database=db,

                        user=user, password=password,

                        host=host, port=port
      )

cursor = conn.cursor()

def csvToDbLoad(table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("************===========Starting to load raw files to raw tables========************")

    droptable(table_name)

    df = pd.read_csv('../resources/'+table_name+'.csv')
    df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces

    from sqlalchemy import create_engine
    engine = create_engine('postgresql://'+user+':'+password+'@'+host+':'+port+'/'+db)

    df.to_sql(table_name, engine)


def csvToDbLd():
    csvToDbLoad("product_details")
    csvToDbLoad("customer_details")
    csvToDbLoad("customer_transaction")
    csvToDbLoad("customer_payment")