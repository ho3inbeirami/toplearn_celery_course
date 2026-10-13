from celery import shared_task

## error handling in tasks chain 
from celery import chain


@shared_task(queue = 'tasks')
def CustomSum(num1, num2):
    return num1 + num2





@shared_task(queue = 'tasks')
def power(num):
    if num ==5:
        raise ValueError('value can not bee 5')
    
    return num ** 2



        
def run_tasks():
    task_chain = chain([ CustomSum.s(2,3), power.s() ])
    
    result_chain = task_chain.apply_async()
    
    return result_chain.get() 