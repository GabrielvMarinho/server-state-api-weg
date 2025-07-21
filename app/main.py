from fastapi import FastAPI
import os 
from websocket import new_connection
app = FastAPI()


app.websocket("/ws")(new_connection)