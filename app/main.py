from fastapi import FastAPI
from WsManager import WsManager
from functions import add_and_broadcast, remove_and_broadcast, remove_all_and_broadcast

app = FastAPI()

app.websocket("/api/ws/subscribe")(WsManager.new_client_connection)

app.post("/api/broadcast/add/macro")(add_and_broadcast)

app.delete("/api/broadcast/remove/macro")(remove_and_broadcast)

app.delete("/api/broadcast/remove/all")(remove_all_and_broadcast)