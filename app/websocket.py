from fastapi import WebSocket
from structures import BroadcastDTO
from dotenv import load_dotenv
import uuid
load_dotenv()

clients = {}

async def new_client_connection(websocket: WebSocket):
    unique_id = uuid.uuid4()
    await websocket.accept()

    clients[unique_id] = (websocket)
    try:
        while True:
            await websocket.receive_text() 
    except:
        del clients[unique_id]
        

async def broadcast_action(broadcastDto :BroadcastDTO):
    try:
        for client in clients:
            await client.send_json(broadcastDto)
    except Exception as e:
        print(e)