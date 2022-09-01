from tasks import calcservice_queue
from time import sleep

print("add 3+5")
ret = calcservice_queue.delay(3,5)
print(ret)
print(f"id={ret.id}, state={ret.state}, status={ret.status}")
ret.get()
print("Task ID:")
print(ret)
print(f"id={ret.id}, state={ret.state}, status={ret.status}")
#sleep(10)
print(ret.status)
print(ret.result)



from celery.task.http import HttpDispatchTask
res = HttpDispatchTask.delay(url="http://example.com/multiply", method="GET", x=10, y=10)
res.get()

from celery.task.http import URL
res = URL("http://example.com/multiply").get_async(x=10, y=10)