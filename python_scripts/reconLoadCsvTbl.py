##*************uncomment drop table line in the script and add path for csv file*********
import re
import pandas as pd
import json
import psycopg2
from psycopg2 import sql
#from dropTable import droptable
import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)




def csvToDbLoad(table_name):
    with open ("config.json" , "r") as f:
        config_data= json.loads(f.read() )

    db = config_data["ReconDatabase"]  #change to staging for your database
    user=config_data["USER"]
    password=config_data["PASSWORD"]
    host=config_data["HOST"]
    port=config_data["PORT"]

    # table_name = "recon_customers"

    conn = psycopg2.connect(database=db,

                            user=user, password=password,

                            host=host, port=port
          )

    cursor = conn.cursor()
    logger.info("************===========Starting to load TM response to recon table========************")

    droptable(table_name)
#*****************change the path for generated csv******************
    df = pd.read_csv('../csv-files/'+table_name+'.csv')
#     df = pd.read_csv('../python_scripts/customers_out10.csv')
    df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces
    from sqlalchemy import create_engine
    engine = create_engine('postgresql://'+user+':'+password+'@'+host+':'+port+'/'+db)
    ##remove additional column and rename the column
    df=df.rename(columns={"id": "recon_id", "status" :"recon_status", "tm_load_timestamp": "recon_tm_load_timestamp", "load_tm_status": "recon_load_tm_status"})
    df = df[df.sequence_id != "sequence_id"]
    df.to_sql(table_name, engine,index=False)

    # csvToDbLoad()

    cursor.execute('select count(*) from  recon_customers')
    recon_count=cursor.fetchone()
    print("recon_count",recon_count[0])

    #*********add the table name of staging table***********
    with open ("config.json" , "r") as f:
        config_data= json.loads(f.read() )

    db = config_data["StgDatabase"]  #change to staging for your database
    user=config_data["USER"]
    password=config_data["PASSWORD"]
    host=config_data["HOST"]
    port=config_data["PORT"]

    # table_name = "recon_customers"

    conn = psycopg2.connect(database=db,

                            user=user, password=password,

                            host=host, port=port
          )

    cursor = conn.cursor()

    cursor.execute('select count(*) from  customers')
    staging_count=cursor.fetchone()
    print("staging count" ,staging_count[0])


    if recon_count == staging_count:
        print("Records matching after reconciliation from TM kafka API ")
    else :
        print("Records not matching after reconciliation from TM kafka API")
