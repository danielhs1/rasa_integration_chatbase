from flask import Flask
from healthcheck import HealthCheck
import logging
from src.settings import BASE_PATH

log = logging.getLogger('werkzeug')
log.disabled = True

app = Flask(__name__)

health = HealthCheck()


def app_available():
    return True, "application ok"


health.add_check(app_available)
app.add_url_rule(f"{BASE_PATH}/health-check", "healthcheck", view_func=lambda: health.run())
