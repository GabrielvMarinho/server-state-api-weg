from fastapi import WebSocket
from fastapi.encoders import jsonable_encoder
from structures import BroadcastDTO
from dotenv import load_dotenv
import uuid
import json
import traceback
load_dotenv()

class WsManager:
    
    clients = {}
    lastBroadcast = {}

    @staticmethod
    async def new_client_connection(websocket: WebSocket):
        unique_id = str(uuid.uuid4())
        await websocket.accept()
        WsManager.clients[unique_id] = (websocket)
        await websocket.send_json(WsManager.lastBroadcast)
        try:
            while True:
                
                await websocket.receive_text() 
        except:
            del WsManager.clients[unique_id]
            
    @staticmethod
    async def broadcast_action(broadcastDto :BroadcastDTO):
        try:
            for client in WsManager.clients.values():
                WsManager.lastBroadcast = broadcastDto
                await client.send_json(jsonable_encoder(broadcastDto))
        except:
            traceback.print_exc()