import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_routs = {
    'notifications.tasks.send_sms':{'queue':'queue1'},
    'notifications.tasks.send_email':{'queue':'queue2'}
}


app.autodiscover_tasks()
