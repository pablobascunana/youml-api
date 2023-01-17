import json
from typing import Dict

import pika
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel


class RabbitMQProducer:

    def __init__(self, rabbit_config: Dict[str, str]):
        self.queue_name = rabbit_config["queue_name"]
        self.connection = self.create_connection(rabbit_config)
        self.channel = self.create_channel(self.connection)
        self.queue_declare(self.channel, self.queue_name)

    @staticmethod
    def create_connection(rabbit_config: Dict[str, str]) -> BlockingConnection:
        credentials = pika.PlainCredentials(rabbit_config["user"], rabbit_config["password"])
        connection_params = pika.ConnectionParameters(host=rabbit_config["host"], credentials=credentials,
                                                      virtual_host=rabbit_config["vhost"])
        return pika.BlockingConnection(connection_params)

    @staticmethod
    def create_channel(connection: BlockingConnection) -> BlockingChannel:
        return connection.channel()

    @staticmethod
    def queue_declare(channel: BlockingChannel, queue_name: str):
        channel.queue_declare(queue=queue_name)

    def publish_message(self, message: Dict):
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=json.dumps(message).encode('utf-8'))
        print("mensaje enviado")
        self.close_connection(self.connection)

    @staticmethod
    def close_connection(connection: BlockingConnection):
        connection.close()
