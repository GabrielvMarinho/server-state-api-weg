from fastapi import FastAPI
from WsManager import WsManager
from functions import new_broadcast

app = FastAPI()

app.websocket("/ws/subscribe")(WsManager.new_client_connection)

app.post("/broadcast")(new_broadcast)