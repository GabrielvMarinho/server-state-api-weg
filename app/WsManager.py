from fastapi import WebSocket
from structures import BroadcastDTO
from dotenv import load_dotenv
import uuid
import traceback
load_dotenv()

class WsManager:
    
    clients = {}
    lastBroadcast = BroadcastDTO()

    @staticmethod
    async def new_client_connection(websocket: WebSocket):
        unique_id = str(uuid.uuid4())
        await websocket.accept()
        WsManager.clients[unique_id] = (websocket)
        await websocket.send_json(WsManager.lastBroadcast.model_dump())
        try:
            while True:
                
                await websocket.receive_text() 
        except:
            del WsManager.clients[unique_id]
            
    @staticmethod
    async def send_json_or_delete(id, client, broadcastDto):
        try:
            await client.send_json(broadcastDto.model_dump())
        except Exception as e:
            print(e)
            del WsManager.clients[id]

    @staticmethod
    async def broadcast_action(broadcastDto :BroadcastDTO):
        try:
            for id, client in list(WsManager.clients.items()):
                WsManager.lastBroadcast = broadcastDto
                await WsManager.send_json_or_delete(id, client, broadcastDto)
        except:
            traceback.print_exc()
    