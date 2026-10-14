from celery import shared_task
from config.celery_base import app
import time

#@shared_task(queue = "tasks")
@app.task(queue='tasks', time_limit = 5)
def send_email_to_user(s):
    time.sleep(s)
    print("email has been sent to user")
    #raise ConnectionError('connection lost')