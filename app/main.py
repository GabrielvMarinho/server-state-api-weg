from fastapi import FastAPI, Request
import os 
from websocket import new_client_connection
from functions import new_broadcast
app = FastAPI()


app.websocket("/ws/subscribe")(new_client_connection)



@app.middleware("http")
async def log_request_body(request: Request, call_next):
    body = await request.body()
    print("Request body:", body.decode())  # imprime no terminal
    response = await call_next(request)
    return response


app.post("/broadcast")(new_broadcast)