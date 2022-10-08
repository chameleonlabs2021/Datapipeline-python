#script  used the transform the data to proper json format.
import re
import sys
import subprocess
import os
import json
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
jsonRecon=config_data["jsonRecon"]
sqlScriptsPath=config_data["sqlScriptsPath"]


def clean(table_name):
    filename=jsonOut +table_name+".json"
    filename_out=jsonOut +table_name+"_out.json"
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("==============Clean job started===============")
    logger.info("opening the json file %s",filename)
    fin = open(filename, "rt")
    #read file contents to string
    data = fin.read()
    #replace all occurrences of the required string
    logger.info("replacing the occurrences of junk character from %s",filename)
    data = data.replace('\\n', '')
    data = data.replace('\\t', '')
    data = data.replace("('{","{")
    data = data.replace("}',)","},")
    data = data.replace("}                                    ',)","},")
#     print("check data part 2" , data)
    
    #close the input file
    fin.close()
    #open the input file in write mode
    fin = open(filename, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    fin.close()

    fin = open(filename , "rt")
    data1 = fin.read()
    #remove the last character from file
    logger.info("remove the last character from file from %s",filename)

    data1=data1.rstrip(data[-1])
    data1="[" + data1
    print(data1)
    data1 = data1 + "]"
    print(data1)

    #truncate file and using the same file
    if os.path.exists(filename_out):
        os.remove(filename_out)
        print("The file has been deleted successfully")
    else:
        print("The file does not exist!")
    fin = open(filename_out, "w")
    fin.write(data1)

    logger.info("cleansing completed and new file has been created %s",filename_out)
    try:
        removeOutJsonfiles(filename)
    except:
        logger.info("%s.json file not available",filename)
    logger.info("%s file is deleted",filename)


def main():
    print("Hello World!")
    clean("customers")

if __name__ == "__main__":
    main()