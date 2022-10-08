from pandas.io.json import json_normalize
import pandas as pd
import json
import os
import logging
from removeFiles import *
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)


with open ("config.json" , "r", encoding ='utf-8-sig') as f:

    config_data= json.loads(f.read() )

#     print(config_data)

db = config_data["StgDatabase"]
user=config_data["USER"]
password=config_data["PASSWORD"]
host=config_data["HOST"]
port=config_data["PORT"]
#my_table=config_data["my_table"]
batch_size=config_data["batch_size"]
jsonRecon=config_data["jsonRecon"]
sqlScriptsPath=config_data["sqlScriptsPath"]

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:

            for a in x:

                flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '.')
                i += 1
        else:

            out[str(name[:-1])] = str(x)

    flatten(y)
    return out

def start_explode(data):

  if type(data) is dict:
    df = pd.DataFrame([flatten_json(data)])
  else:
    df = pd.DataFrame([flatten_json(x) for x in data])

  df = df.astype(str)
  return df



def convertJsonToCsv(fil,filename,table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.info("f==> %s filename ======> %s, table_name ====> %s",fil ,filename,table_name)

    f= open(fil)

    data = json.load(f)

    print(data)

    complex_json=data

    df = start_explode(complex_json[table_name])

    print(df)
    csvpath='../csv-files/'
    df.to_csv (csvpath+table_name+'.csv',mode='a', index = None)
    directory=jsonRecon+table_name
    removeReconJsonfiles(table_name)


# filename='../json/recon/customers/customers_out10.json'


def jsontocsvloop(directory,filename,table_name):
    print(directory,table_name)
    logger.info("directory ======> %s, table_name ====> %s",directory,table_name)
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            print("filename is ===>",f)
            convertJsonToCsv(f,filename,table_name)