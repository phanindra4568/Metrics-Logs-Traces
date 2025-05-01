from fastapi import FastAPI, Request
import logging
import time
import random
from prometheus_client import start_http_server, Summary, Counter
from prometheus_client import generate_latest

app = FastAPI()
logging.basicConfig(filename='app.log', level=logging.INFO)

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests')

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    log = f"{request.method} {request.url.path} completed_in={process_time:.4f}s"
    logging.info(log)
    return response

@app.get("/hello")
@REQUEST_TIME.time()
def read_root():
    REQUEST_COUNT.inc()
    return {"message": "Hello from observability app"}

@app.get("/metrics")
def metrics():
    return generate_latest()
