import os
from cleanse import *
import logging
import shutil
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
jsonRecon=config_data["jsonRecon"]
sqlScriptsPath=config_data["sqlScriptsPath"]


def removeOutJsonfiles(table_name):
    os.remove(table_name)

def removeReconJsonfiles(table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    foldername=jsonRecon+'/'+table_name
    try:
        shutil.rmtree(foldername)
    except:
        logger.info("Unable to delete the folder %s",foldername)

    try:
        os.makedirs(foldername)
    except:
        logger.info("Unable to create the folder %s",foldername)



