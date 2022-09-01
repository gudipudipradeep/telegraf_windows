from celery import Celery
# from time import sleep
# from fastapi import FastAPI
# import uvicorn
# from celery.result import AsyncResult

celery_task_queue = Celery('tasks')
celery_task_queue.config_from_object('celeryconfig')

def on_event(event):
    print("EVENT HAPPENED: ", event)

def on_task_failed(event):
    exception = event['exception']
    print("TASK FAILED!", event, " EXCEPTION: ", exception)
    
#with app.connection() as connection:
#    recv = app.events.Receiver(connection, handlers={
#        'task-sent': on_event,
#        'task-received': on_event,
#        'task-started': on_event,
#        'task-succeeded': on_event,
#        'task-failed': on_task_failed,
#        'task-rejected': on_event,
#        'task-revoked': on_event,
#        'task-retried': on_event
#    })
#    recv.capture(limit=None, timeout=10)

@celery_task_queue.task
def calcservice_queue(x, y):
    return x + y

# original_callback = uvicorn.main.callback

# def callback(**kwargs):
#     from celery.contrib.testing.worker import start_worker
#     import tasks

#     with start_worker(tasks.celery_task_queue, perform_ping_check=False, loglevel="info"):
#         original_callback(**kwargs)

# uvicorn.main.callback = callback


# if __name__ == "__main__":
#     uvicorn.main()
    
# python tasks.py test:application
# to run it as app
# https://stackoverflow.com/questions/33117676/run-celery-worker-from-flask-app

if __name__ == "__main__":
    celery_task_queue.start(["worker", "--pool=solo", "-l", "info"])
#celery flower -A tasks worker --pool=solo -l info
#celery -A tasks worker --address=127.0.0.6 --port=5566
#celery -A tasks flower --port=5555
#celery flower --broker=redis://127.0.0.1:6379/0
#redis-cli
#KEYS *
#get <key>
#type <key>
# -E event option
#CELERY_ALWAYS_EAGER = True
#set SQS_URL=sqs://sqs.us-east-2.amazonaws.com/986718270614/calcservice
#--concurrency=4 -Ofair -Q <random-tasks> queue name
#worker_prefetch_multiplier = 10
#-P eventlet
#celery -A celery_worker.celery worker --loglevel=info
#https://medium.com/koko-networks/a-complete-guide-to-production-ready-celery-configuration-5777780b3166
