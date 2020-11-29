from src.settings import CHATBASE_API_URL, CHATBASE_API_KEY
import requests


def send_event(data):
    data["api_key"] = CHATBASE_API_KEY
    response = requests.post(url=CHATBASE_API_URL, json=data)
    return response
