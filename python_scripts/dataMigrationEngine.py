from asyncore import loop
from math import ceil
import psycopg2
from psycopg2 import sql
from kafkapush import kafka_push_func
# import configparser
from generate_json import *
import json
from rawToStagingLoad import rawToStg
from rawCsvToDB import *
from reconJsonToSmallJson import *
import sys
import logging
from reconLoadCsvTbl import *
from dataValidation import *
logger1 = logging.getLogger('mylog')
logger1.setLevel(logging.DEBUG)
from datetime import datetime


try:
    my_table = sys.argv[1]
except IndexError:
    print("please provide the table name as an argument")
    exit()
json_path = "config.json"

with open ("config.json" , "r") as f:

    config_data= json.loads(f.read() )
    print(config_data)

db = config_data["StgDatabase"]
user=config_data["USER"]
password=config_data["PASSWORD"]
host=config_data["HOST"]
port=config_data["PORT"]
#my_table=config_data["my_table"]
batch_size=config_data["batch_size"]
date = datetime. now(). strftime("%Y_%m_%d-%I-%M-%S_%p")
fname='../logs/'+my_table+ date+'.log'
logging.basicConfig(filename=fname,level=logging.DEBUG, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger1.info("************===========Starting the Data migration process========************")


try:
    conn = psycopg2.connect(database=db,

                        user=user, password=password,

                        host=host, port=port

   )
except psycopg2.OperationalError:
  print("Connection Error - please check the database credentials")

print("Load raw files to raw tables")
logger.info("Calling the script to  Load raw files to raw tables")
csvToDbLd()

print("Load raw tables to Stg tables")
logger.info("Calling the script to Load raw tables to Stg tables")
rawToStg(my_table)

logger.info("Calling the data validation script")
dataValidate(my_table)
logger.info("select count(*) from  %s where load_TM_status <> 'Success'",my_table)
cursor = conn.cursor()
cursor.execute(
    sql.SQL("select count(*) from  {table} where load_TM_status <> 'Success'")
        .format(table=sql.Identifier(my_table)),
    )
  
for i in cursor.fetchall():

    numberofrecords = i[0]

    logger.info("Total %s count: %s", my_table,numberofrecords)

    logger.info("Batch size: %s", batch_size)
    if numberofrecords > batch_size:
        numberofloop=numberofrecords/batch_size
    elif numberofrecords != 0:
        numberofloop=1
    else:
        print("Table count is 0")
        logger.info("Table count is 0")
        numberofloop=0
        break

records=0
nfloop=ceil(numberofloop)
print("Number of nfloop:",nfloop)
logger.info("Number of nfloop: %s",nfloop)
for i in range(nfloop):
    logger.info("==============Batch  %s started ============== ",i)
    prerecords=records
    records=records+batch_size
    logger.info("Generating the json for the batch size %s loaded records between %s and %s",batch_size,prerecords,records)

    gen_json(my_table)
    logger.info("Push json for the batch size %s loaded records between %s and %s to kafka",batch_size,prerecords,records)

#     print("kafka_push:",kafka_push_func())

    if kafka_push_func()==0:
#
        # update the customer table as success
        cursor.execute(
            sql.SQL('''update  {table} set load_TM_status = 'Success' where sequence_id in (
                                         select
                                             sequence_id
                                         from
                                             {table}
                                         where
                                             load_TM_status <> 'Success'
                                         order by
                                             sequence_id
                                         limit %s )''')
                .format(table=sql.Identifier(my_table)),[batch_size]
            )
        cursor.execute(
                    sql.SQL('''commit''')
#                         .format(table=sql.Identifier(my_table)),[batch_size]
                    )
#     continue
        logger.info("%s kafka push successes for the records between %s and %s",my_table,prerecords,records)
        logger.info("==============Batch  %s completed ==============",i)

    else:

        logger.info("%s kafka push failed for the records between %s and %s",my_table,prerecords,records)

        #update the status to table to failed
        cursor.execute(
                   sql.SQL('''update  {table} set load_TM_status = 'Success' where sequence_id in (
                                                select
                                                    sequence_id
                                                from
                                                    {table}
                                                where
                                                    load_TM_status <> 'Failed'
                                                order by
                                                    sequence_id
                                                limit batch_size )''')
                       .format(table=sql.Identifier(my_table)),                   )
    # exit the loop
        logger.info("==============Batch  %s failed ==============",i)
        break
    
  
conn.commit()
conn.close()
splitBigToSmall(my_table)


def main():
    print("Main function called!")
    csvToDbLoad(my_table)

if __name__ == "__main__":
    main()