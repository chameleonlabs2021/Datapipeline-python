import json
from reconSmallJsonCsv import *
import logging
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

import sys
table_name =sys.argv[1]
#
# def splitBigToSmall(table_name):
#     logger.info("==============Splitting recon JSON files to smaller chunks==============")
#     print("function is gen_json" , table_name)
#     if table_name == "posting_instruction_batch":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'posting_instruction_batch.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'posting_instruction_batch/posting_instruction_batch_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'posting_instruction_batch/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "restriction_set":
#         #logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'restriction_set.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'restriction_set/restriction_set_out'
#             #convertJsonToCsv(filename)
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'restriction_set/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "payment_device":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'payment_device.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'payment_device/payment_device_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'/payment_device_link/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "payment_device_link":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'payment_device_link.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'payment_device_link/payment_device_link_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'/payment_device_link/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "customers":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'customers.json') as f:
#           data = json.load(f)
#           print(data)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'customers/customers_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               jsonfile = filename+ str(i)  + '.json'
#               print(jsonfile)
#               json.dump(x, f_out)
#               #convertJsonToCsv(jsonfile)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'customers/'
#         jsontocsvloop(directory,table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "accounts":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'accounts.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'accounts/accounts_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'/accounts/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "account_plan_assocs":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'account_plan_assocs.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'account_plan_assocs/account_plan_assocs_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         directory=jsonRecon +'/account_plan_assocs/'
#         jsontocsvloop(directory,filename)
#     elif table_name == "flags":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'flags.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'flags/flags_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'/flags/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     elif table_name == "plan":
#         logger.info("Splitting %s json file started",table_name)
#         with open(jsonRecon+'plan.json') as f:
#           data = json.load(f)
#           for i, x in enumerate(data):
#             filename= jsonRecon +'plan/Plan_out'
#             with open(filename+ str(i) + '.json', 'w') as f_out:
#               json.dump(x, f_out)
#         logger.info("Splitting %s json file Completed",table_name)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
#         directory=jsonRecon +'/plan/'
#         jsontocsvloop(directory,filename)
#         logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
#     else:
#         print("Table name does not exist")




def splitBigToSmall(table_name):
#     logging.basicConfig(filename='../logs/'+table_name+'.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info("==============Splitting recon JSON files to smaller chunks==============")
    print("function is gen_json" , table_name)

    logger.info("Splitting %s json file started",table_name)
    with open(jsonRecon+table_name+'.json') as f:
      data = json.load(f)
      for i, x in enumerate(data):
        filename= jsonRecon +table_name+'/'+table_name+'_out'
        with open(filename+ str(i) + '.json', 'w') as f_out:
          json.dump(x, f_out)
    logger.info("Splitting %s json file Completed",table_name)
    logger.info("==============Converting recon JSON smaller chunks to CSV files started ==============")
    directory=jsonRecon + table_name +'/'
    jsontocsvloop(directory,filename,table_name)
    logger.info("==============Converting recon JSON smaller chunks to CSV files completed==============")
