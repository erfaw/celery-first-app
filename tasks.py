from celery import Celery
from configparser import ConfigParser

config = ConfigParser(interpolation=None)
config.read("./rabbitmq.ini")
config = config['rabbitmq_settings']
config['password'] = config['password'].replace('@', '%40')

broker_url = f"pyamqp://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['vhost']}"

app = Celery(
    "tasks", 
    broker=broker_url,
)

@app.task
def add(x, y):
    """
    A Simple Celery task to be done with Celery worker through RabbitMQ message broker.

    Args:
        x (int):
        y (int):
    
    Returns:
        int
    """
    return x + y
