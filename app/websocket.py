from fastapi import WebSocket
from dotenv import load_dotenv
import os
import json
load_dotenv()

clients: list[WebSocket] = []

async def broadcast(message):
    print(clients)
    try:
        for client in clients:
            print("broad cast ", message)
            await client.send_json(message)
    except Exception as e:
        print(e)

async def new_connection(websocket: WebSocket):
    await websocket.accept(subprotocol="auth-protocol")
    
    token = None
    try:
        token = websocket.headers["sec-websocket-protocol"].split(", ")[1]
    except:
        pass
    
    
    if token and token==os.getenv("WS_SENDER_KEY"):
        await sender_await_communication(websocket)
    else:
        
        clients.append(websocket)
        await client_await_communication(websocket)
        


async def client_await_communication(websocket: WebSocket):
    try:
        while True:
            await websocket.receive_text() 
    except:
        clients.remove(websocket)

async def sender_await_communication(websocket):
    try:
        while True:   
            data = await websocket.receive()
            data = json.loads(data["text"])
            await broadcast(data)
    except Exception as e:
        print(e)
        pass