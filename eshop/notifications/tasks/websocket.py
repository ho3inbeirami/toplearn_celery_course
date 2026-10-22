from celery import shared_task
from config.celery_base import SingleTonCustomTask

@shared_task(queue = "tasks", base=SingleTonCustomTask)
def send_notif_to_user():
    print("notif has been sent to user")