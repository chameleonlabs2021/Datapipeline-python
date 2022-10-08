##*************uncomment drop table line in the script and add path for csv file*********
import re
import pandas as pds
import json
import psycopg2
from psycopg2 import sql
#from dropTable import droptable
import logging
# from deepchecks.tabular import Dataset
# from deepchecks.tabular.suites import data_integrity
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)




def dataValidate(table_name):
    with open ("config.json" , "r") as f:
        config_data= json.loads(f.read() )

    db = config_data["StgDatabase"]  #change to staging for your database
    user=config_data["USER"]
    password=config_data["PASSWORD"]
    host=config_data["HOST"]
    port=config_data["PORT"]
    reconCsvPath=config_data["reconCsvPath"]

    # table_name = "recon_customers"

    conn = psycopg2.connect(database=db,

                            user=user, password=password,

                            host=host, port=port
          )

    cursor = conn.cursor()
    logger.info("************===========Starting to validate the staging %s========************",table_name)

    from sqlalchemy import create_engine
    engine = create_engine('postgresql://'+user+':'+password+'@'+host+':'+port+'/'+db)
    # Connect to PostgreSQL server

    dbConnection    = engine.connect();

    #Create dataframe to write the validation results


    # Read data from PostgreSQL database table and load into a DataFrame instance

    logger.info("************===========Querying the  %s table========************",table_name)
    QUERY = 'SELECT * FROM '+ table_name +';'
    with engine.connect() as connection:
        dataFrame = pds.read_sql(sql=QUERY, con=connection)


    pds.set_option('display.expand_frame_repr', False);
    def report(new_row,table_name,colvalues,text):
        df_results = pds.DataFrame(columns=['Tablename','Column_name','Remarks'])
#         text= table_name + ' is not empty'
        new_row = {'Tablename':table_name, 'Column_name':colvalues, 'Remarks':text}
        df_results=df_results.append(new_row, ignore_index=True)
        df_results.to_csv(reconCsvPath+'data_validation_report.csv', mode='a', index=False, header=False)

    def checkcolmns(table_name):
        for col in dataFrame.columns:
            miss = dataFrame[col].isnull().sum()
            if miss>0:
                print("{} has {} missing value(s)".format(col,miss))
                logger.info("{} has {} missing value(s)".format(col,miss))
                text= str(col) +' has '+ str(miss) + ' missing value(s)'
                new_row = {'Tablename':table_name, 'Column_name':col, 'Remarks':text}
                report(new_row,table_name,col,text)
            else:
                print("{} has NO missing value!".format(col))
                logger.info("{} has NO missing value!".format(col))
                text= str(col) +' has '+str(miss)+ ' NO missing value!'
                new_row = {'Tablename':table_name, 'Column_name':col, 'Remarks':text}
                report(new_row,table_name,col,text)
    logger.info("************===========Checking if the table %s is empty========************",table_name)
    if(dataFrame.empty):
        print ('CSV file is empty')
        text= table_name + ' is empty'
        col=""

        new_row = {'Tablename':table_name, 'Column_name':col, 'Remarks':text}
        df_results = pds.DataFrame(columns=['Tablename','Column_name','Remarks'])

        df_results=df_results.append(new_row, ignore_index=True)
        df_results.to_csv(reconCsvPath+'data_validation_report.csv', mode='a', index=False, header=True)
        checkcolmns(table_name)
        logger.info("************===========table %s is empty========************",table_name)
    else:
        print ('CSV file is not empty')
        text= table_name + ' is not empty'
        col=""
#         df_results = pds.DataFrame(columns=['Tablename','Column_name','Remarks'])
        new_row = {'Tablename':table_name, 'Column_name':col, 'Remarks':text}
        df_results = pds.DataFrame(columns=['Tablename','Column_name','Remarks'])

        df_results=df_results.append(new_row, ignore_index=True)
        df_results.to_csv(reconCsvPath+'data_validation_report.csv', mode='a', index=False, header=True)
        checkcolmns(table_name)
        logger.info("************===========table %s is not empty========************",table_name)

    # Print the DataFrame

#     print(dataFrame);
    logger.info("************===========Writing %s  validation reports to csv files========************",table_name)
    a = pds.read_csv(reconCsvPath+"data_validation_report.csv")
    a.to_html(reconCsvPath+"data_validation_report.html")




    # Close the database connection

    dbConnection.close();


def main():
    print("Main function called!")
    dataValidate("accounts")

if __name__ == "__main__":
    main()