from celery import shared_task
from time import sleep

import logging


logger = logging.getLogger(__name__)

@shared_task(queue='celery')
def task_1():
    logger.info('task 1 started')
    sleep(3)
    logger.info('task 1 end')
    return

@shared_task(queue='celery:1')
def task_2():
    logger.info('task 2 started')
    sleep(3)
    logger.info('task 2 end')
    return

@shared_task(queue='celery:2')
def task_3():
    logger.info('task 3 started')
    sleep(3)
    logger.info('task 3 end')
    return

@shared_task(queue='celery:3')
def task_4():
    logger.info('task 4 started')
    sleep(3)
    logger.info('task 4 end')
    return


task_1.delay()
task_1.delay()
task_2.delay()
task_3.delay()
task_4.delay()
task_4.delay()
