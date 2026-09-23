import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')


app = Celery('tasks')

app.config_from_object('celery_config')

app.task()
def worker():
    pass
