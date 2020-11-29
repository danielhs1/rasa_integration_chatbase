import logging

import ujson

from src.connectors.chatbase import send_event
from src.settings import NLU_THRESHOLD


def process_events(ch, method, properties, body):
    try:
        message = ujson.loads(body)

        chatbase_data = {
            "type": message.get("event"),
            "user_id": message.get("sender_id"),
            "time_stamp": int(message.get("timestamp") * 1000),
            "platform": "rasa",
            "message": message.get("text")
        }
        nlu_threshold = NLU_THRESHOLD
        if message.get("event") == "user":
            intent = message.get("parse_data", {}).get("intent", {})
            chatbase_data["type"] = "user"
            chatbase_data["intent"] = intent.get("name")
            chatbase_data["not_handled"] = True if intent.get("confidence") < nlu_threshold else False
            send_event(chatbase_data)

        if message.get("event") == "bot":
            chatbase_data["type"] = "agent"
            send_event(chatbase_data)

    except Exception as exc:
        logging.error(str(exc))

    ch.basic_ack(delivery_tag=method.delivery_tag)
