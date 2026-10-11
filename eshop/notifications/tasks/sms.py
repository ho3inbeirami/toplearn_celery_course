from celery import shared_task


@shared_task(queue = "tasks",  autoretry_for = (ConnectionError,), default_retry_delay = 5, retry_kwargs = {'max_retries':5})
def send_sms_to_user():
    raise ConnectionError('connection error has been occurred')
    print("sms has been sent to user")