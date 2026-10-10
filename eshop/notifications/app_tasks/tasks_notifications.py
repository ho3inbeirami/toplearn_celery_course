from eshop.config.celery_base  import app
from celery import shared_task

@shared_task(queue = 'tasks')
def my_task():
    try: 
        print("this is my task")
        raise ValueError('value is not valid')
        
    except Exception as e:
        print("an exception has been occurred")