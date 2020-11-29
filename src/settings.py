import os

from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_PATH = config("BASE_PATH")

ENVIRONMENT = config("ENVIRONMENT")
APPLICATION_NAME = config("APPLICATION_NAME")

RABBITMQ_HOST = config("RABBITMQ_HOST")
RABBITMQ_PORT = config("RABBITMQ_PORT", default=5672, cast=int)
RABBITMQ_USERNAME = config("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = config("RABBITMQ_PASSWORD")
RABBITMQ_QUEUE = config("RABBITMQ_QUEUE")
RABBITMQ_PREFETCH_COUNT = config("RABBITMQ_PREFETCH_COUNT", default=1, cast=int)

NLU_THRESHOLD = config("NLU_THRESHOLD", default=0.4, cast=float)

CHATBASE_API_KEY = config("CHATBASE_API_KEY")
CHATBASE_API_URL = config("CHATBASE_API_URL")
