from confluent_kafka import Producer

from pysense.logger import pysense_logger
from pysense.memories import remind


def __log_error(err, msg):
    if err is not None:
        pysense_logger.error(err)


def send_message(topic, message):
    broker = remind('broker')
    producer = Producer({'bootstrap.servers': broker})
    producer.poll(0)
    producer.produce(topic, message, callback=__log_error)
    producer.flush()
