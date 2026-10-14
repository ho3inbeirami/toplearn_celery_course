from celery import shared_task
## retry 

# @shared_task(queue = "tasks",  autoretry_for = (ConnectionError,), default_retry_delay = 5, retry_kwargs = {'max_retries':5})



## error handling in tasks group 
from celery import group

phone_numbers = [
    '09121234567',
    '09031234567',
    '09127434534',
    '09124234533'
    
]

@shared_task(queue = "tasks") 
def send_sms_to_user(phone_number  :str):
    if phone_number.startswith('0903'):
        raise ValueError('invalid phone number !!! ')
    
    return f'message has been sent to {phone_number}'




@shared_task(queue = 'dead_letter')
def handel_error_in_dead_letter(*args, **kwargs):
    print('error handel in dead letter')
    


def handle_tasks(result ):
    if result.successful():
        print(f'task completed : {result.get()}')
    elif result.failed() and isinstance(result.result , ValueError):
        print(f'task failed : {result.result}')
        print('process was sent to error handling Queue')
        handel_error_in_dead_letter.apply_async(args = ('this is data','this is another data'))
        

    elif result.status == 'REVOKED':
        print(f'task was revoked: {result.id}')
        
        
        
def run_tasks():
    task_group = group( send_sms_to_user.s(phone_number) for phone_number in phone_numbers)
    
    result_group = task_group.apply_async()
    
    result_group.get(disable_sync_subtasks = False , propagate =False )
    
    for result in result_group:
        handle_tasks(result)