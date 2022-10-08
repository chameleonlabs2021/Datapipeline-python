import logging
logger = logging.getLogger('mylog')
logger.setLevel(logging.DEBUG)

# logging.basicConfig(filename=fname, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def kafka_push_func():
    logger.info("==============Kafka job started==============")
    return_value =0
    return return_value 


# kafka_push_func()