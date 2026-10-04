import os
from celery import Celery

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
        
        



app.autodiscover_tasks()
