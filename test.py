from fastapi import FastAPI
#from tasks import calcservice_queue
#from asgiref.sync import sync_to_async
#from asgiref.sync import sync_to_async, async_to_sync

import uvicorn

application = FastAPI()

#def blocking_function(syncObject):
#    syncObject.wait()
    

#@application.get('/queue')
#async def request_sqs_taskqueue():  
#    result_queue = calcservice_queue.delay(3,5)
#    await result_queue.get()
    #await sync_to_async(blocking_function)(result_queue)
#    print(f"id={result_queue.id}, state={result_queue.state}, status={result_queue.status}")
#    return {"message": result_queue.result}

@application.get('/')
async def request_sqs_taskqueue():
    return {"message": "Welcome to FastAPI"}


# uvicorn test:application --reload
#if __name__ == "__main__":
#    uvicorn.run("test:application", port=9000)