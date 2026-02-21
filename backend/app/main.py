from fastapi import FastAPI, Request 
from prometheus_fastapi_instrumentator import Instrumentator 
import time 
from app.api.chat import router as chat_router 

app=FastAPI(title="GEMINI API") 


@app.middleware('http')
async def add_process_time_header(request:Request,call_next):
    start_time=time.time()
    response=await call_next(request)
    process_time=time.time()-start_time 

    response.headers['X-process-Time']=f'{process_time:.4f} sec'
    return response 

Instrumentator().instrument(app).expose(app,endpoint='/metrics')
app.include_router(chat_router,prefix='/app/v1',tags=['Chat'])
