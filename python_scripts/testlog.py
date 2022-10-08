import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)
my_table='accounts1'
fname='../logs/'+my_table+'.log'
print(fname)
logging.basicConfig(filename=fname, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.info("************===========Starting the Data migration process========************")
