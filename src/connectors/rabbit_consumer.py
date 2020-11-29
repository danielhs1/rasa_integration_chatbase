import pika

from src.settings import RABBITMQ_HOST, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_QUEUE, \
    RABBITMQ_PREFETCH_COUNT
from src.contracts.event_consumer import EventConsumer


class RabbitConsumer(EventConsumer):
    def start_consumption(self, callback):
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            port=RABBITMQ_PORT,
            credentials=credentials
        ))
        channel = connection.channel()

        channel.basic_qos(prefetch_count=RABBITMQ_PREFETCH_COUNT)
        channel.basic_consume(on_message_callback=callback,
                              queue=RABBITMQ_QUEUE)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
