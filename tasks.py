from celery import Celery
from configparser import ConfigParser

config = ConfigParser()
config.read("./rabbitmq.cfg")
config = config['rabbitmq_settings']
