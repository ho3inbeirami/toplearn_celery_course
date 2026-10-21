from config.celery_base import app 
from datetime import timedelta

app.conf.beat_schedule = {
    'task_1':{
        'task':'notifications.tasks.schedule_tasks.task_1',
        'schedule':timedelta(seconds=5)
    },
    
    'task_2':{
        'task':'notifications.tasks.schedule_tasks.task_2',
        'schedule':timedelta(seconds=10)
    }
}



@app.task(queue='tasks')
def task_1():
    print('running tasks 1 ')




@app.task(queue='tasks')
def task_2():
    print('running tasks 2 ')