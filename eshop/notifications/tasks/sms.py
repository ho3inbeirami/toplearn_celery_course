from celery import shared_task


@shared_task(queue = "tasks")
def send_sms_to_user():
    print("sms has been sent to user")