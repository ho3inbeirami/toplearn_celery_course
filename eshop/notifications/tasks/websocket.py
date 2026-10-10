from celery import shared_task


@shared_task(queue = "tasks")
def send_notif_to_user():
    print("notif has been sent to user")