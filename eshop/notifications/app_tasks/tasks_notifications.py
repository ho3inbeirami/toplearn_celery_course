from eshop.config.celery_base  import app

@app.task(queue = 'tasks')
def task():
    pass