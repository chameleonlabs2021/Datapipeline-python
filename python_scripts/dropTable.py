# ----- Example Python Program to remove a PostgreSQL database table

import psycopg2

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import pandas as pd
import json
import psycopg2
from psycopg2 import sql
import logging
json_path = "config.json"
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)


def droptable(table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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

    psqlCon = psycopg2.connect(database=db,

                            user=user, password=password,

                            host=host, port=port
          )


    # Start a PostgreSQL database session

    # psqlCon         = psycopg2.connect("dbname=postgres user=staging password=1234");

    psqlCon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);



    # Open a database cursor

    psqlCursor      = psqlCon.cursor();



    logger.info("Dropping the %s ",table_name)
    # Name of the table to be deleted
    tableName       = table_name;



    # Form the SQL statement - DROP TABLE

    dropTableStmt   = "DROP TABLE %s;"%tableName;



    # Execute the drop table command
    try:
        psqlCursor.execute(dropTableStmt);
    except :
      logger.info("%s table does not exist ",table_name)

    logger.info("%s dropped ",table_name)


    # Free the resources

    psqlCursor.close();

    psqlCon.close();