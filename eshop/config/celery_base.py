import os
from celery import Celery ,Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routs = {
#     'notifications.tasks.send_sms':{'queue':'queue1'},
#     'notifications.tasks.send_email':{'queue':'queue2'}
# }

# app.conf.broker_transport_options = {
#     'queue_order_strategy': 'priority',
# }

# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'sep': ':',
#     'queue_order_strategy': 'priority',
# }



# rabbitmq config start

from kombu import Exchange, Queue




app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
        queue_arguments={'x-max-priority': 10}),
    Queue('dead_letter', routing_key='dead_letter')
]

app.conf.task_max_priority = 10
app.conf.task_default_priority = 5

app.conf.worker_prefetch_multiplayer = 1
app.conf.worker_concurrency = 1
app.conf.task_acks_late = True

# rabbitmq config end


# import os 

# base_dir = os.getcwd()

# tasks_folder  = os.path.join(base_dir, 'notifications', 'app_tasks')

# if os.path.exists(tasks_folder) and os.path.isdir(base_dir):
#     tasks_module = []
#     for file_name in os.listdir(tasks_folder):
#         module_name = f'notifications.app_tasks.{file_name}'
        
#         module = __import__(module_name, fromlist=["*"])
#         for name in dir(module):
#             obj = getattr(module_name,name)
#             if callable(obj):
#                 tasks_module.append(f'{module_name}.{name}')
        
        



###  error handling using custom tasks 

import logging
from django.conf import settings

class CustomTask(Task):
    
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        
        if isinstance(exc, ConnectionError):
            logging.error("connection error occurred")
        
        else:
            print(f'task id : {task_id}')
        return super().on_failure(exc, task_id, args, kwargs, einfo)
    
    def apply_async(self, *args: tuple, **kwargs: dict):
        if settings.RUN_TASK_IN_CELERY:
            return super().apply_async(*args, **kwargs)
        else:
            return self(*args, **kwargs)


app.Task = CustomTask

app.autodiscover_tasks()

