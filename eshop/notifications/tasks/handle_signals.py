
from config.celery_base import app
from celery.signals import task_failure
import sys



@app.task(queue='tasks')
def my_task():
    raise ValueError('task failed')


@app.task(queue='tasks')
def error_handler_task(task_id):
    sys.stdout.write(f'task id is : {task_id}')



@task_failure.connect(sender = my_task)
def handle_my_task_failure(sender = None, task_id= None, **kwargs):
    error_handler_task.apply_async(task_id)
    
    

def run_task():
    my_task.apply_async()