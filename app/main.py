from fastapi import FastAPI
from WsManager import WsManager
from functions import add_and_broadcast, remove_and_broadcast

app = FastAPI()

app.websocket("/ws/subscribe")(WsManager.new_client_connection)

app.post("/broadcast/add/macro")(add_and_broadcast)
app.post("/broadcast/remove/macro")(remove_and_broadcast)