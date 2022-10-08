from asyncore import loop
from math import ceil
import psycopg2
from psycopg2 import sql
import json
import os
from cleanse import clean
import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)


json_path = "config.json"

with open ("config.json" , "r") as f:

    config_data= json.loads(f.read() )

#     print(config_data)

db = config_data["StgDatabase"]
user=config_data["USER"]
password=config_data["PASSWORD"]
host=config_data["HOST"]
port=config_data["PORT"]
#my_table=config_data["my_table"]
batch_size=config_data["batch_size"]
jsonOut=config_data["jsonOut"]
sqlScriptsPath=config_data["sqlScriptsPath"]
try:
  conn = psycopg2.connect(database=db,

                        user=user, password=password,

                        host=host, port=port

      )
except psycopg2.OperationalError:
  print("Connection Error - please check the database credentials")


cursor = conn.cursor()


def rawToStg(table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("==============Raw tables to staging table load started==============")
    print("function is gen_json" , table_name)
    rawToStgfile=sqlScriptsPath + table_name+"RawToStg.sql"
    logger.info("Raw tables to %s table load started%s ",table_name,rawToStgfile)
    f = open(rawToStgfile, "r",  encoding ='utf-8-sig')
    config_data=f.read()
    cursor.execute(config_data)
    logger.info("Raw tables to %s table load completed",table_name)

def main():
    print("Main function called!")
    rawToStg(my_table)

if __name__ == "__main__":
    main()