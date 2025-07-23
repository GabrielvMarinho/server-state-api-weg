from fastapi import WebSocket
from structures import MacroPost, MacroResponse
from dotenv import load_dotenv
import uuid
import traceback
from datetime import datetime

load_dotenv()

class WsManager:
    
    clients = {}
    currentStateMacros = []

    @staticmethod
    async def new_client_connection(websocket: WebSocket):
        unique_id = str(uuid.uuid4())
        await websocket.accept()
        WsManager.clients[unique_id] = (websocket)
        await websocket.send_json(WsManager.currentStateMacros)
        try:
            while True:
                await websocket.receive() 
        except:
            del WsManager.clients[unique_id]
            
    @staticmethod
    async def send_json_or_delete(id, client):
        try:
            await client.send_json(WsManager.currentStateMacros)
        except Exception as e:
            print(e)
            del WsManager.clients[id]

    @staticmethod
    async def broadcast_new_state():
        try:
            for id, client in list(WsManager.clients.items()):
                await WsManager.send_json_or_delete(id, client)
        except:
            traceback.print_exc()

    @staticmethod
    async def add_to_state(macro: MacroPost):
        alreadyExists = False
        for macroInList in WsManager.currentStateMacros:
            if macroInList["id"] == macro.id:
                alreadyExists = True

        if(not alreadyExists and len(WsManager.currentStateMacros) <= 6):
            macro_data = macro.model_dump()
            macro_data["time_started"] = f"{datetime.now().hour}:{datetime.now().minute}"
            finalMacro = MacroResponse(**macro_data)
            WsManager.currentStateMacros.append(finalMacro.model_dump())
            return

        raise Exception("Macro already existant")
    @staticmethod
    async def remove_from_state(id: str):
        for macroInList in list(WsManager.currentStateMacros):
            if macroInList["id"] == id:
                WsManager.currentStateMacros.remove(macroInList)
                return
        raise Exception("No macro to remove")