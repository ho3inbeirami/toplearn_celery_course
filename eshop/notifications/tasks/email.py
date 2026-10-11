from celery import shared_task


@shared_task(queue = "tasks")
def send_email_to_user():
    print("email has been sent to user")
    raise ConnectionError('connection lost')