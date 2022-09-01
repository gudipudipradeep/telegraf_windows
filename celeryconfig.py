import os
from datetime import timedelta

# Celery configuration
broker_url = "redis://127.0.0.1:6363"#os.getenv('SQS_URL')
broker_transport_options = {
    'region': 'us-east-2',
    #'polling_interval': 5,  # number of sec to sleep between polls
    'wait_time_seconds': 5
}
task_default_queue = 'calcservice'
worker_enable_remote_control = False
worker_send_task_events = False
result_backend = "redis://127.0.0.1:6363"
result_serializer = 'json'
task_serializer = 'json'
result_expires = timedelta(hours=3)
enable_utc = True