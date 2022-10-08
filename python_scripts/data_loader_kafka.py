# third party
from confluent_kafka import Consumer, KafkaError, Producer
from typing import Any, Callable, Dict, List, Optional, Union
import json
import logging

log = logging.getLogger(__name__)

DEFAULT_PRODUCER_CONFIG: Dict[str, Union[bool, int, str]] = {
    "bootstrap.servers": "kafka.kafka-v2-demo.sparrow.tmachine.io",
    "security.protocol": "ssl"}
DATA_LOADER_REQUEST_TOPIC = "vault.data_loader_api.v1.data_loader.resource_batch.create.requests"

def initialise_producer(
    config: Optional[Dict[str, Union[bool, int, str]]] = None,
) -> Producer:
    """
    Initialises a kafka producer relying on default config that can be overriden
    :param kafka_config: the kafka config to use. If the KafkaConfig.config is specified,
     the default config is updated with the contents of this dictionary. This means it takes
     precedence over any default config or other parameters
    :param client_id: the client id that the producer will use
    :return: the initialised kafka producer
    """

    final_config = DEFAULT_PRODUCER_CONFIG.copy()
    if config:
        final_config.update(config)
    return Producer(final_config)

def acked(err, msg):
    print("ack")
    if err is not None:
        print("if")
        log.exception(f"Failed to deliver message: {msg.value()}: {err.str()}")
    else:
        print("else")
        print("Message produced: {0}".format(msg.value()))
        log.debug("Message produced: {0}".format(msg.value()))

def produce_message(
    producer: Producer,
    topic: str,
    message: str,
    key: Optional[str] = None,
    on_delivery: Callable = acked,
):
    print("start")
    #print("message:"+message)
    producer.produce(topic=topic, key=key, value=message, on_delivery=on_delivery)
    producer.poll(1)
    print("end")


# Opening JSON file
f = open('sample_payload.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
f.close()
#print(data)

producer = initialise_producer()
produce_message(producer, DATA_LOADER_REQUEST_TOPIC, json.dumps(data))
producer.flush()

