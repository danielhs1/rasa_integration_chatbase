from src.contracts.event_consumer import EventConsumer
from src.connectors.rabbit_consumer import RabbitConsumer
from src.services.process import process_events


def main(event_consumer: EventConsumer, callback_func):
    event_consumer.start_consumption(callback_func)


if __name__ == "__main__":
    main(RabbitConsumer(), process_events)
