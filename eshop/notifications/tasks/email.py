from celery import shared_task
from config.celery_base import app
import time

#@shared_task(queue = "tasks")
@app.task(queue='tasks', time_limit = 10)
def send_email_to_user():
    time.sleep(6)
    print("email has been sent to user")
    #raise ConnectionError('connection lost')
    
    
    
def send_email():
    result = send_email_to_user.apply_async()
    
    
    try:
        task_result = result.get(timeout = 4)
    except TimeoutError:
        print('task timed out')
        