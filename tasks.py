from celery import Celery
from configparser import ConfigParser

config = ConfigParser()
config.read("./rabbitmq.cfg")
config = config['rabbitmq_settings']

app = Celery(
    "tasks", 
    f"pyamqp://{config["username"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["vhost"]}",
)
