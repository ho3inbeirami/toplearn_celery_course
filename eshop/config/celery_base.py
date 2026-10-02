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

app.autodiscover_tasks()
