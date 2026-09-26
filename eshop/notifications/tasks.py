from celery import shared_task
from time import sleep
import logging
logger = logging.getLogger(__name__)



# @shared_task(queue='celery')
# def task_1():
#     logger.info('task 1 started')
#     sleep(3)
#     logger.info('task 1 end')
#     return

# @shared_task(queue='celery:1')
# def task_2():
#     logger.info('task 2 started')
#     sleep(3)
#     logger.info('task 2 end')
#     return

# @shared_task(queue='celery:2')
# def task_3():
#     logger.info('task 3 started')
#     sleep(3)
#     logger.info('task 3 end')
#     return

# @shared_task(queue='celery:3')
# def task_4():
#     logger.info('task 4 started')
#     sleep(3)
#     logger.info('task 4 end')
#     return

from celery import group , chain

@shared_task()
def task_1():
    
    sleep(3)

    return 0



@shared_task()
def task_2(i):

    sleep(3)

    return i 



@shared_task()
def task_3(i):

    sleep(3)

    return i


@shared_task()
def task_4(i):

    sleep(3)

    return i


# task_group = group(task_1.s(),task_2.s(), task_3.s(),task_4.s())
# task_chain = chain(task_1.s(),task_2.s(), task_3.s(),task_4.s())