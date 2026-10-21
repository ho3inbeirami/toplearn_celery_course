from config.celery_base import app 
import sys

@app.task(queue = 'tasks')
def my_long_running_task(has_error):
    if has_error:
        raise ValueError(' value error has been occurred')
    sys.stdout.write('long running task has been done! ')

@app.task(queue = 'tasks')
def process_result(result):
    sys.stdout.write('process tasks result! ')
    sys.stdout.flush()



@app.task(queue = 'tasks') 
def process_error_result(task_id,exc, traceback):
    sys.stdout.write('----------------------------')
    sys.stdout.write(str(exc))
    sys.stdout.write('----------------------------')
    sys.stdout.flush()



def run_tasks(has_error):
    my_long_running_task.apply_async(args = [has_error], link = [process_result.s()] , link_error = [ process_error_result.s() ])