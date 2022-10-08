#script to fetch the DB connection from config file
#and excecute the sql scripts to convert it into json object.
from asyncore import loop
from math import ceil
import psycopg2
from psycopg2 import sql
import json
import os
from cleanse import *
from removeFiles import *
import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)


json_path = "config.json"

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


def gen_json(table_name):
    logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("==============Generate json job started ==============")

    f = open(sqlScriptsPath +table_name+".sql", "r",  encoding ='utf-8-sig')
#     new_text=str(config_data)+"limit 10;"
    config_data=f.read()
    new_text=str(config_data+"limit "+str(batch_size)+";")
#     new_text=config_data
#     print(new_text)
    cursor.execute(new_text)
    delTableOut=table_name+'_out'
    logger.info("%s.json file is deleted",delTableOut)
    try:
        removeOutJsonfiles(delTableOut)
    except:
        logger.info("%s.json file not available",delTableOut)
    for i in cursor.fetchall():
        print(i)
        with open(jsonOut +table_name+'.json', 'a') as outfile:
          outfile.write(str(i))
#     clean(table_name)



def main():
    print("Hello World!")
    gen_json("customers")

if __name__ == "__main__":
    main()